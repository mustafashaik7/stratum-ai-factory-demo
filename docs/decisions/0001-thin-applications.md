# ADR 0001: thin applications on a generic platform

Status: accepted for this demo scaffold.

## Decision

Applications own presentation and approved experience configuration. The runtime exposes versioned capabilities. Domain packs own domain behavior and enterprise adapters. AI DLC, AI QE, and AI Observability are shared services.

## Dependency direction

Application → client SDK → capability API → runtime workflow → domain pack → external adapter.

Generic platform code must not import application code or healthcare types. Healthcare modules implement generic capability interfaces. UI validation improves usability but never grants authorization.

## Consequences

Runtime APIs become an availability dependency, with explicit pending/unavailable responses and recovery. The delivery control plane is not a runtime dependency. Shared services can be independently deployed; this decision does not require a monolith. Versioned API/pack contracts and consumer checks are required before upgrades.
