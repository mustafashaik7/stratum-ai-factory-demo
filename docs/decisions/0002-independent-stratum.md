# ADR 0002: independent Stratum root and distributed solution model

Status: accepted for the blueprint.

Move all reusable runtime, lifecycle, quality, observability, contracts, SDK and deployment modules beneath stratum/. Keep apps/patient-portal separate. Healthcare is a domain extension, not a dependency of the generic core. A standalone structural validator runs without apps/.

Adopt Cloud–Core–Edge as the solution view. Cloud contains optional managed services, Core contains Stratum and governed data, and Edge contains consumers and enterprise systems. These are logical trust and placement boundaries, not a prescribed rack layout.

Agent graphs, providers, tools, memory and policies are linked design artifacts. All execution remains disabled until implementations, identity integration, evaluation and operational checks exist. Promote exact versions through shared AI DLC and AI QE. Observe business outcomes as well as inference and infrastructure behavior.
