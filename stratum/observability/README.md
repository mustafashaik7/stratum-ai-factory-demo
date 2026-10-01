# AI Observability — planned shared service

Own instrumentation conventions, collection, trace correlation, quality and drift signals, cost attribution, audit, dashboards, and alert routing.

Trace application → workflow → retrieval/model → authorized tool → integration outcome. Bind metadata to release, domain-pack, model and prompt versions. Use pseudonymous correlation identifiers. Do not log raw patient content, secrets, or full prompts by default. Audit retention and access differ from general telemetry.

`telemetry-contract.json` is a design input. No collector, dashboard, or alert is deployed. Define objectives, alert owners, retention, redaction, and incident exercises before pilot.
