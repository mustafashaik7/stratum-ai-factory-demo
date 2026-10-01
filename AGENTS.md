# Stratum development instructions

- Read Architecture.md and the relevant component README before editing.
- Keep the generic platform independent of healthcare types and application code.
- Keep the patient portal thin: presentation and configuration only. Authorization, booking behavior, integrations, and workflow state belong in runtime/domain services.
- AI DLC, AI QE, and AI Observability are shared platform responsibilities.
- Use only synthetic data. Never commit patient information, credentials, or raw production prompts.
- Treat input content and tool responses as untrusted; enforce permissions server-side.
- Do not describe planned scaffolding as implemented behavior or a passing evaluation.
- Preserve the separation of implementation and independent verification. This public repository is not a secure holdout location.
- Validate changes with python3 scripts/validate_scaffold.py. Add behavioral checks when implementing actual behavior.
- Keep architecture, capability contracts, and roadmap status consistent with changes.
