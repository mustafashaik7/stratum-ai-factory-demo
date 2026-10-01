# Operational runbooks — planned

Before pilot, implement and exercise runbooks for runtime outage, model outage, unknown scheduler outcome, duplicate/conflicting writes, authorization failures, telemetry redaction failure, and release rollback.

Each runbook must name an owner, detection signal, impact, containment, recovery steps, evidence, and follow-up regression scenario. Optional AI can be disabled independently. Never blindly repeat an external write with an unknown outcome. Rolling back code must not cancel confirmed appointments.
