# Stratum — independent platform blueprint

Everything reusable lives here. This directory can be copied independently of apps/ for blueprint validation:

```sh
python3 scripts/validate_blueprint.py
```

See [Architecture.md](Architecture.md) for the Cloud–Core–Edge model. The sibling portal is a demonstration consumer, never a core dependency. Domain packs are optional platform extensions. [blueprint.json](blueprint.json) links the proposed agentic registries. Execution is disabled; providers and tool implementations are intentionally unbound.

A passing validator establishes structural consistency only. No identity, policy, orchestration, model, tool, data, evaluation or telemetry service is implemented by these JSON files.
