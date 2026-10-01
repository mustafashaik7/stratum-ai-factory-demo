# Healthcare domain pack — planned

Own patient self-access policy, appointment proposal/confirmation rules, booking state, scheduling adapters, domain fixtures, and acceptance semantics. The platform hosts and operates these capabilities; domain owners approve the rules.

Begin with adult self-service, one synthetic organization, and a mock scheduler. Support atomic reservation, duplicate protection, concurrency conflicts, expiry, and unknown-result reconciliation. Preserve authoritative status from external systems. Vendor integrations are not implemented.

The pack is versioned independently from the generic core and thin portal. Its booking contract is a design specification, not executable authorization.
