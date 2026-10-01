# AI QE — planned shared Quality Engineering

Own test execution, controlled datasets, independent acceptance, AI evaluations, quality gates, and evidence. Applications provide scenarios; the platform provides execution infrastructure.

Cover software behavior, access control, concurrency, recovery, accessibility, AI grounding, tool misuse, injection resistance, and sensitive-data handling. Set domain-approved thresholds before execution. Calibrate model judges against human review; use repeated representative cases for probabilistic results.

`pipeline.json` declares planned stages. It does not run them. The repository CI only validates the scaffold. Missing/failed required evidence must block promotion once the gate controller is implemented. Real holdouts require separate access controls, not a folder here.
