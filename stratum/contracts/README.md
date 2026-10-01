# Generic platform contracts

Use [../blueprint.json](../blueprint.json) as the local composition manifest. IDs connect agents, prompts, tools, skills, workflows, provider routes, memory, policies, and telemetry. Each registry is versioned and validated without importing any application.

Healthcare capability descriptors live in domain-packs/healthcare, not the generic contract layer. The JSON format is specific to this blueprint and is not a deployed API specification. A future HTTP/OpenAPI implementation must enforce authenticated context, typed input/output, timeout, cancellation, trace propagation, and structured errors.
