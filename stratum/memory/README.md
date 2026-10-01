# Memory — blueprint

Separate ephemeral conversation context, workflow checkpoints, knowledge indexes and evidence. Scope caches and state by tenant and subject. Restore only approved artifacts; never replay external writes blindly. Retention and deletion need runtime implementation.

See catalog.json for linked design contracts. All execution adapters remain unbound.
