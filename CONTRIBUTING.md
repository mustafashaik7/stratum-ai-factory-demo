# Contributing

Start with one roadmap milestone and its acceptance evidence. Keep changes scoped and document any changed interface or ownership boundary.

1. Read the platform and application architecture.
2. Define expected behavior and failure cases before implementation.
3. Implement behind a versioned capability contract.
4. Add meaningful behavior checks appropriate to the change.
5. Run `python3 scripts/validate_scaffold.py` and any implemented component checks.
6. Update documentation to distinguish completed work from planned work.

Do not commit generated traces or test outputs containing sensitive information. Independent holdouts will require a separately controlled verifier environment. No open-source license has been selected for this repository.
