# Implementation roadmap

| Milestone | Status | Required evidence |
|---|---|---|
| M0: architecture and scaffold | Complete | Component boundaries, sample contracts, acceptance catalog, scaffold validation |
| M1: runtime capability contracts | Planned | Authenticated synthetic context, proposal/confirmation/status APIs, contract tests |
| M2: healthcare booking pack | Planned | Atomic mock scheduler, duplicate protection, pending reconciliation, authorization tests |
| M3: thin patient experience | Planned | Accessible manual booking UI consuming SDK/APIs without domain logic |
| M4: AI DLC | Planned | Approved intent to versioned candidate and release evidence; bounded retries |
| M5: AI QE | Planned | Independent tests/evaluations; missing or failed mandatory gates block promotion |
| M6: AI Observability | Planned | Correlated journey/tool/scheduler trace, redacted audit, cost and reliability dashboard, alert exercise |
| M7: optional administrative AI | Planned | Grounded help and booking preferences, evaluated tool policy and fallback |
| M8: reuse demonstration | Planned | Second application consumes unchanged generic core |
| M9: integration pilot | Not started | Approved identity/EHR test access, privacy/security review, operational ownership |

M1–M3 demonstrate application behavior. M4–M6 demonstrate the factory. Production deployment is outside this scaffold. Hosting and technology choices are unresolved; do not equate a passing scaffold check with these milestone exit criteria.
