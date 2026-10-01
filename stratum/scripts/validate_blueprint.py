"""Validate the unbound design graph. This does not enforce runtime controls."""
import json
from pathlib import Path
import sys

REQUIRED = {'agents', 'prompts', 'tools', 'skills', 'models', 'memory', 'policies',
            'workflows', 'data', 'registry', 'telemetry', 'deployment', 'messages'}


def require(value, message):
    if not value:
        raise ValueError(message)


def contained(root, name):
    target = (root / name).resolve()
    require(target.is_relative_to(root.resolve()), f'Path escapes module: {name}')
    require(target.is_file(), f'Missing file: {name}')
    return target


def read(path):
    doc = json.loads(path.read_text())
    require(doc.get('schema_version') == 1, f'Unsupported schema: {path}')
    return doc


def indexed(items):
    require(isinstance(items, list) and items, 'Registry must contain items')
    result = {}
    for item in items:
        name = item['id']
        require(isinstance(name, str) and name and name not in result, f'Duplicate or invalid ID: {name}')
        result[name] = item
    return result


def positive(item, key):
    require(type(item[key]) is int and item[key] > 0, f'Invalid budget: {key}')


def validate(root=None):
    root = Path(root) if root else Path(__file__).resolve().parents[1]
    blueprint = read(root / 'blueprint.json')
    require(blueprint['execution_enabled'] is False, 'Blueprint execution must stay disabled')
    require(set(blueprint['registries']) == REQUIRED, 'Missing or unknown registry')
    catalogs = {key: indexed(read(contained(root, value))['items'])
                for key, value in blueprint['registries'].items()}

    def ref(kind, name):
        require(name in catalogs[kind], f'Unknown {kind} reference: {name}')
        return catalogs[kind][name]

    for policy in catalogs['policies'].values():
        require(policy['default'] == 'deny' and policy['network'] == 'broker_only', 'Invalid policy boundary')
    for model in catalogs['models'].values():
        require(model['enabled'] is False and model['provider'] == 'unbound'
                and model['endpoint'] is None, 'Model must remain unbound')
        positive(model, 'max_output_tokens')
        positive(model, 'timeout_seconds')
    for prompt in catalogs['prompts'].values():
        contained(root / 'prompts', prompt['file'])
    for tool in catalogs['tools'].values():
        require(tool['implementation'] == 'unbound', 'Tool must remain unbound')
        require(tool['credentials'] == 'broker_managed', 'Tool credentials must be broker managed')
        positive(tool, 'timeout_seconds')
        policy = ref('policies', tool['policy'])
        require(tool['effect'] in policy['allow_effects'], 'Tool effect not allowed by policy')
        ref('messages', tool['input_contract'])
        ref('messages', tool['output_contract'])
        if tool['effect'] in ('external_write', 'release'):
            require(tool['requires_idempotency'] is True and policy['approval'] != 'none',
                    'Consequential tool requires approval and idempotency')
    for skill in catalogs['skills'].values():
        for name in skill['tools']:
            ref('tools', name)
    for agent in catalogs['agents'].values():
        for field, kind in [('model', 'models'), ('memory', 'memory'), ('prompt', 'prompts'), ('policy', 'policies')]:
            ref(kind, agent[field])
        positive(agent, 'max_steps')
        positive(agent, 'budget_tokens')
        require(agent['can_approve'] is False, 'Agent cannot approve')
        policy = ref('policies', agent['policy'])
        for name in agent['tools']:
            tool = ref('tools', name)
            require(tool['effect'] in policy['allow_effects'], 'Agent permission exceeds policy')
            require(tool['effect'] not in ('external_write', 'release'), 'Writes require explicit workflow approval')
        for name in agent['skills']:
            require(set(ref('skills', name)['tools']) <= set(agent['tools']), 'Skill exceeds agent tools')
    for workflow in catalogs['workflows'].values():
        positive(workflow, 'max_steps')
        positive(workflow, 'timeout_seconds')
        nodes = indexed(workflow['nodes'])
        require(workflow['start'] in nodes and workflow['on_failure'] in nodes, 'Invalid workflow entry/exit')
        require(nodes[workflow['on_failure']]['kind'] == 'terminal', 'Failure must terminate')
        for node in nodes.values():
            kind = node['kind']
            require(kind in ('agent', 'tool', 'approval', 'terminal'), 'Unknown node kind')
            if kind != 'terminal':
                require(node['next'] in nodes, 'Unknown next node')
                ref({'agent': 'agents', 'tool': 'tools', 'approval': 'policies'}[kind], node['ref'])
            else:
                require('next' not in node, 'Terminal cannot have next node')
        visited, approvals = set(), set()
        current = workflow['start']
        while True:
            require(current not in visited, 'Workflow cycle is unsupported')
            visited.add(current)
            require(len(visited) <= workflow['max_steps'], 'Workflow exceeds step bound')
            node = nodes[current]
            if node['kind'] == 'terminal':
                break
            if node['kind'] == 'approval':
                require(ref('policies', node['ref'])['approval'] != 'none', 'Empty approval policy')
                approvals.add(node['ref'])
            if node['kind'] == 'tool':
                tool = ref('tools', node['ref'])
                if tool['effect'] in ('external_write', 'release'):
                    require(tool['policy'] in approvals, 'Missing preceding approval')
                    approvals.remove(tool['policy'])
            current = node['next']
        require(visited | {workflow['on_failure']} == set(nodes), 'Unreachable workflow nodes')
    for item in catalogs['deployment'].values():
        require(item['provisioned'] is False and item['connections_enabled'] is False, 'Deployment must remain unbound')
    for item in catalogs['telemetry'].values():
        require(item['sink'] == 'unbound' and item['raw_content_logging'] is False
                and item['audit_sampling'] is False, 'Invalid blueprint telemetry settings')
    for item in catalogs['data'].values():
        require(item['source'] == 'unbound' and item['data_class'] == 'synthetic'
                and item['automatic_training'] is False, 'Invalid blueprint data settings')
    return sum(len(items) for items in catalogs.values())


if __name__ == '__main__':
    try:
        print(f'PASS: {validate()} connected blueprint entries; no services executed.')
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
