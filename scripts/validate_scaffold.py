"""Validate the scaffold, not application behavior or AI quality."""
import json
from pathlib import Path
import re
import sys
import runpy

ROOT = Path(__file__).resolve().parents[1]

def require(condition, message):
    if not condition:
        raise ValueError(message)

def read_json(path):
    return json.loads((ROOT / path).read_text())

def validate():
    runpy.run_path(str(ROOT / "stratum/scripts/validate_blueprint.py"), run_name="__main__")
    required = [
        'stratum/Architecture.md', 'apps/patient-portal/Architecture.md',
        'stratum/lifecycle/ai-dlc/README.md', 'stratum/lifecycle/ai-qe/README.md',
        'stratum/observability/README.md', 'stratum/runtime/README.md',
        'stratum/sdk/client/README.md', 'stratum/sdk/ui/README.md',
        'stratum/domain-packs/healthcare/README.md', 'docs/ROADMAP.md',
    ]
    for path in required:
        require((ROOT / path).is_file(), f'Missing required file: {path}')
    json_files = list(ROOT.rglob('*.json'))
    for path in json_files:
        if '.git' in path.parts:
            continue
        data = json.loads(path.read_text())
        require(data.get('schema_version') == 1, f'Unsupported schema: {path}')
    app = read_json('apps/patient-portal/application.json')
    pack = read_json('stratum/domain-packs/healthcare/pack.json')
    capabilities = read_json('stratum/domain-packs/healthcare/capabilities.json')
    contract = read_json('stratum/domain-packs/healthcare/contracts/appointment-booking.json')
    catalog = read_json('verification/patient-portal.acceptance.json')
    qe = read_json('stratum/lifecycle/ai-qe/pipeline.json')
    known = [item['id'] for item in capabilities['capabilities']]
    require(len(known) == len(set(known)), 'Duplicate capability IDs')
    require(set(app['capabilities']) <= set(known), 'Unknown application capability')
    require(set(app['capabilities']) <= set(pack['capabilities']), 'Pack missing requested capability')
    require(app['domain_pack'] == pack['id'] + '@' + pack['version'], 'Domain pack version mismatch')
    require(app['runtime_contract'] == capabilities['id'] + '@' + capabilities['version'], 'Runtime contract version mismatch')
    for key in ('acceptance_catalog', 'architecture'):
        require((ROOT / 'apps/patient-portal' / app[key]).is_file(), f'Broken application reference: {key}')
    require((ROOT / 'stratum/domain-packs/healthcare' / pack['contract']).is_file(), 'Broken pack contract reference')
    ids = [case['id'] for case in catalog['scenarios']]
    require(len(ids) == len(set(ids)), 'Duplicate scenario IDs')
    require(set(ids) == set(contract['acceptance_ids']), 'Acceptance traceability mismatch')
    require(catalog['contract_id'] == contract['id'], 'Contract ID mismatch')
    require(catalog['application_id'] == app['application_id'], 'Application ID mismatch')
    require(app['data_class'] == 'synthetic_only', 'Demo must use synthetic data')
    require(app['production_enabled'] is False, 'Production is not implemented')
    require(qe['production_promotion_enabled'] is False, 'Promotion is not implemented')
    require(qe['missing_required_evidence'] == 'block', 'Missing evidence must block')
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        content = path.read_text()
        require(content.count('```') % 2 == 0, f'Unbalanced code fences: {path}')
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in target or target.startswith('#'):
                continue
            target = target.split('#')[0]
            require((path.parent / target).exists(), f'Broken link in {path}: {target}')
    print(f'PASS: scaffold structure, {len(json_files)} JSON design files, links and traceability.')
    print(f'{len(ids)} acceptance scenarios declared; none executed by this validator.')
    print('Application behavior, AI evaluations and production readiness are NOT verified.')

if __name__ == '__main__':
    try:
        validate()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
