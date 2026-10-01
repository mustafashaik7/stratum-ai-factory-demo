# Healthcare adapters — planned

Implement a synthetic scheduler first. Future EHR/scheduling adapters must validate supported operations, status mapping, authorization, concurrency, and retry semantics. A free slot does not guarantee booking. Expose request-only behavior where a vendor cannot confirm a booking atomically.

Adapter credentials and patient records stay behind the platform boundary. No production connection is configured.
