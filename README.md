# Stratum AI Factory Demo

A reusable foundation for building, verifying, running, and observing AI-enabled applications. The Patient Portal is the first thin consumer.

**Status: architecture and repository skeleton.** The only executable capability currently included is scaffold validation. No application, model integration, identity service, booking API, AI lifecycle engine, evaluation runner, or observability backend is implemented. Passing CI validates repository structure, not healthcare behavior or production readiness.

## Start here

- [Platform architecture](Architecture.md)
- [Patient Portal architecture](apps/patient-portal/Architecture.md)
- [Implementation roadmap](docs/ROADMAP.md)
- [Platform/application boundaries](docs/decisions/0001-thin-applications.md)
- [Contributor guide](CONTRIBUTING.md)

## Repository layout

```text
platform/
  ai-dlc/                # Requirements through delivery and improvement
  ai-qe/                 # Shared software and AI evaluation pipelines
  observability/         # Traces, quality, cost, audit, alerts and outcomes
  runtime/               # Capability gateway, authorization and workflows
packages/
  contracts/             # Versioned platform consumption contracts
  client-sdk/            # Future thin client library
  ui/                    # Future shared experience components
  domain-packs/
    healthcare/          # Booking rules, adapters and domain scenarios
apps/
  patient-portal/         # Experience configuration and future UI
examples/synthetic/      # Synthetic fixtures only
infra/                   # Future local and deployed infrastructure
scripts/                 # Executable scaffold validation
verification/            # Public acceptance catalog; not private holdouts
.github/workflows/       # Scaffold CI only
```

## Validate locally

Requires Python 3.10 or later; no third-party packages or credentials.

```sh
python3 scripts/validate_scaffold.py
```

## Architectural rule

The portal renders options, collects explicit confirmation, and displays authoritative results. Stratum services execute workflows, enforce identity and authorization, run healthcare integrations, and manage AI, quality engineering, and observability. Healthcare-specific logic belongs to a versioned domain pack; the core remains generic.

The delivery control plane builds releases. The runtime plane serves patient requests independently of delivery-service availability. Optional AI failure does not disable deterministic booking; runtime booking-service failure requires an unavailable or pending state.

## First demonstration to implement

Deliver one synthetic appointment-booking journey through shared AI DLC and AI QE, then trace it through shared observability. Demonstrate patient isolation, duplicate protection, concurrency, uncertain-result reconciliation, and manual fallback. See the roadmap for acceptance milestones.

Use synthetic data only. No production credentials or patient information belong in this repository. Model, UI, backend, cloud, and vendor implementations remain replaceable decisions.
