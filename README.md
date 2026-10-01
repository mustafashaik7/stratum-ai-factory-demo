# Stratum AI Factory Demo

Stratum is an independent, reusable AI platform blueprint. Applications remain thin consumers.

**Status:** declarative plumbing and executable structural validation. No model, cloud, agent runner, identity service, policy engine, booking service, database, collector, or application UI is connected or implemented.

## Architecture

![Cloud–Core–Edge solution model](docs/diagrams/stratum-solution-architecture.svg)

- [Stratum architecture](stratum/Architecture.md)
- [Patient Portal architecture](apps/patient-portal/Architecture.md)
- [Reference research and tailored design](docs/research/architecture-reference-mapping.md)
- [Roadmap](docs/ROADMAP.md)

## Structure

```text
stratum/                    # Independent platform root
  Architecture.md
  blueprint.json            # Composition manifest; execution disabled
  agents/ prompts/ skills/  # Versioned behavior and roles
  orchestration/ tools/     # Bounded graphs and authorized operations
  models/ data/ memory/     # Inference, knowledge and state boundaries
  policies/ registry/       # Governance and immutable release bindings
  lifecycle/ai-dlc/          # Shared delivery lifecycle
  lifecycle/ai-qe/           # Shared tests and AI evaluations
  observability/            # Agent, model, infrastructure and business signals
  runtime/                  # Capability gateway and services
  contracts/ sdk/           # Public contracts and thin-client boundaries
  domain-packs/healthcare/   # Optional healthcare extension
  infrastructure/           # Local, hybrid and distributed profiles
  scripts/                  # Standalone blueprint validation
apps/patient-portal/         # Experience configuration and future UI only
docs/                       # Solution diagram, research and decisions
verification/               # Public unexecuted scenarios; not private holdouts
examples/synthetic/         # Invented fixtures only
scripts/                    # Repository-wide integration validation
```

## Validate

Python 3.10+; no dependencies, credentials or GPU required.

```sh
python3 stratum/scripts/validate_blueprint.py
python3 scripts/validate_scaffold.py
python3 -m unittest discover -s tests -v
```

The first validator can run with only the stratum/ directory present. Checks cover local references, tool permissions, graph reachability, write-approval checkpoints, bounded execution and disabled provider bindings. They do not execute workflows or prove runtime security. Repository checks additionally validate application/domain contracts and links.

Use synthetic data only. The delivery plane builds releases; the runtime plane serves applications. A portal owns screens and presentation, while Stratum supplies business capability services through optional domain packs. The generic core has no dependency on apps/.

The deployment progression is Deploy → Interconnect → Extend. Begin with one synthetic workflow; connect approved systems only after verification; extend by application and region based on evidence. No vendor hardware configuration or production readiness is claimed.
