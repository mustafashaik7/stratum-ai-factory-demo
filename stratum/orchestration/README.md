# Orchestration — blueprint

Graphs declare success paths and a blocked failure terminal. Approval nodes pause with persisted state; resume must revalidate subject, policy, expiry and exact payload. Timeout, cancellation and budget exhaustion terminate safely. Checkpoints do not make external writes exactly-once: use idempotency and reconcile unknown results.

See catalog.json for linked design contracts. All execution adapters remain unbound.
