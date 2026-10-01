"""Mutation tests for structural validation, not AI behavior or runtime security."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'stratum'
spec = importlib.util.spec_from_file_location('blueprint', SOURCE / 'scripts/validate_blueprint.py')
blueprint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(blueprint)


class BlueprintValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'stratum'
        shutil.copytree(SOURCE, self.root)

    def mutate(self, path, change):
        target = self.root / path
        doc = json.loads(target.read_text())
        change(doc)
        target.write_text(json.dumps(doc))

    def test_standalone_without_apps(self):
        self.assertGreater(blueprint.validate(self.root), 0)

    def test_unknown_tool_rejected(self):
        self.mutate('agents/catalog.json', lambda d: d['items'][0]['tools'].append('unknown'))
        with self.assertRaisesRegex(ValueError, 'Unknown tools'):
            blueprint.validate(self.root)

    def test_bypassed_approval_rejected(self):
        self.mutate('orchestration/catalog.json', lambda d: d['items'][1]['nodes'][0].update(next='execute'))
        with self.assertRaisesRegex(ValueError, 'Missing preceding approval'):
            blueprint.validate(self.root)

    def test_duplicate_id_rejected(self):
        self.mutate('models/catalog.json', lambda d: d['items'].append(d['items'][0].copy()))
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            blueprint.validate(self.root)

    def test_enabled_model_rejected(self):
        self.mutate('models/catalog.json', lambda d: d['items'][0].update(enabled=True))
        with self.assertRaisesRegex(ValueError, 'unbound'):
            blueprint.validate(self.root)

    def test_path_escape_rejected(self):
        self.mutate('blueprint.json', lambda d: d['registries'].update(models='../outside.json'))
        with self.assertRaisesRegex(ValueError, 'escapes'):
            blueprint.validate(self.root)

    def test_agent_tool_escalation_rejected(self):
        self.mutate('agents/catalog.json', lambda d: d['items'][0]['tools'].append('capability.write'))
        with self.assertRaisesRegex(ValueError, 'permission exceeds'):
            blueprint.validate(self.root)

    def test_cycle_rejected(self):
        self.mutate('orchestration/catalog.json', lambda d: d['items'][0]['nodes'][0].update(next='plan'))
        with self.assertRaisesRegex(ValueError, 'cycle'):
            blueprint.validate(self.root)


if __name__ == '__main__':
    unittest.main()
