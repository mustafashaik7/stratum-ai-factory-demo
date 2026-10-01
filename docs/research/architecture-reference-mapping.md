# Architecture reference mapping

Reviewed 1 October 2026. This document separates source observations from proposed Stratum decisions. The diagram and implementation boundaries are original adaptations. References do not establish vendor certification, production readiness, or measured benefits for this demo.

## Primary reference: distributed AI Factory solution guide

The [Dell AI Factory / Digital Realty solution guide](https://go2.digitalrealty.com/rs/087-YZJ-646/images/Solution_Guide_Dell_AI_Factory_Review.pdf) is the principal visual and deployment-model reference. All eight pages were read; the architecture, configuration, and deployment diagrams on pages 2–5 were inspected.

| Reference element | Source location | Stratum adaptation |
|---|---|---|
| Distributed, data-centered hybrid model | Page 2 | Keep reusable AI execution and governed data services in a logical core; place services according to data access, latency, and operating needs. |
| Cloud–Core–Edge arrangement | Page 3 | Cloud holds optional managed services; core contains Stratum and data services; edge holds the portal, enterprise systems, and operational users. |
| AI Factory and lakehouse as complementary services | Pages 2–3 | Separate agent execution from ingestion, retrieval, checkpoints, artifacts, and evidence. A lakehouse is optional, not a prerequisite for transactional booking. |
| Interconnection between clouds, core, and sites | Page 3 | Define authenticated ingress, approved egress, adapter ownership, and data-class rules. Private connectivity supplements service authorization. |
| Physical configuration and capacity | Page 4 | Retain capacity planning as a deployment concern. Do not inherit the example rack, power, hardware, or storage quantities. |
| Deploy → Interconnect → Extend | Page 5 | Prove a bounded synthetic workflow, connect approved enterprise dependencies, then demonstrate reuse and justified geographic expansion. |
| Hybrid, multicloud, and localization use cases | Page 6 | Support replaceable providers and deployment profiles; choose each based on an actual requirement. |
| Location availability and qualification | Pages 7–8 | Treat location and vendor availability as procurement inputs to a future deployment review. |

**Design interpretation:** the guide supplies a useful enterprise solution layout, but it does not specify Stratum's development lifecycle, patient workflows, agent permissions, or quality gates. Those are explicit additions. “Core” is a service boundary; it need not mean a single facility. “Edge” identifies consumers and source systems; it does not imply an edge-computing installation.

## NVIDIA source review

The six requested references complement the primary guide. The review below records both what was accessible and what each source changes in the proposal.

| Source and review coverage | Observation | Decision for Stratum |
|---|---|---|
| [GTC25 S71405: Accelerating AI Adoption with AI Factories](https://resources.nvidia.com/en-us-dgx-platform/gtc25-s71405). Landing page and session identity accessible; recording/transcript inaccessible. | The session could not be reviewed in depth. Browser access to the recording failed verification. | No technical assertion is attributed to the recording. Keep this as an outstanding source-review item. |
| [AI Factory glossary](https://www.nvidia.com/en-us/glossary/ai-factory/). Full available page reviewed. | The factory spans data processing, training/fine-tuning, inference, and supporting infrastructure; intelligence is its output. | Stratum must cover deployed AI and its data lifecycle as well as software delivery. Training remains optional. Measure useful completed tasks alongside tokens and latency. |
| [AI Factories in Action ebook](https://resources.nvidia.com/en-us-dgx-h100/ai-factories-in-action-ebook/), [seven-page PDF](https://dam-cdn.nvd.orangelogic.com/AssetLink/p8i50vq115dxe2gd0l6u3tem43x45p4k.pdf). Full text reviewed. | BNY illustrates a common platform serving many applications; Bristol Myers Squibb illustrates centralized hybrid research infrastructure; Lockheed Martin emphasizes shared model access; MediaTek emphasizes provisioning and performance. | Make onboarding, model access, operations, and application reuse shared services. These are vendor-reported examples, not evidence of Stratum's expected savings or outcomes. |
| [Enterprise innovation case study](https://www.nvidia.com/en-us/case-studies/ai-factory-drives-enterprise-innovation-at-scale/). Full available page reviewed. | A governed common platform, enterprise knowledge retrieval, phased adoption, and repeatable performance measurement support scale. | Establish an approved capability catalog, release evidence, retrieval provenance, and workload benchmarks before broad onboarding. No productivity claims are transferred to this demo. |
| [Enterprise Reference Architecture](https://www.nvidia.com/en-us/technologies/enterprise-reference-architecture/). Landing page and linked design/deep-dive documentation reviewed. | Compute, network, storage, and management must be designed together; configuration depends on workload and scale. | Separate runtime, management, and integration concerns. Record deployment profiles now; select physical infrastructure only after workload and resilience testing. |
| [DGX SuperPOD](https://www.nvidia.com/en-us/data-center/dgx-superpod/). Full available landing page reviewed. | Integrated infrastructure supports large training and inference workloads with operational management. | Treat accelerated private infrastructure as a later deployment option. The skeleton requires neither GPUs nor an appliance purchase. |

The ebook and product pages can describe different time-specific adoption counts. Those snapshots are not combined into a current benchmark. Business outcomes for Stratum require its own baseline, observation period, and evidence.

## Deeper technical implications

### Agent execution is a managed service

The [agentic AI factory guidance](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-white-paper/latest/agentic-ai-in-the-factory.html) describes stateful agent workflows, workspaces, tools, and operating services. Stratum translates this into separate registries for agents, prompts, models, skills, tools, memory, policies, and bounded workflows.

Proposed enforcement belongs outside prompts: the gateway resolves identity, the tool broker checks permission, the runtime limits steps and cost, and durable workflow state pauses for human approval. Implementation agents cannot approve their own release. A write binds authenticated approval to an immutable proposal and idempotency key. The current JSON catalog describes these seams; it does not execute or enforce them.

### Data services are more than an application database

The [enterprise RAG deployment guidance](https://docs.nvidia.com/enterprise-reference-architectures/enterprise-rag-deployment-guide/latest/enterprise-rag-on-enterprise-ra.html) distinguishes ingestion and indexing from runtime retrieval and generation. Stratum similarly separates approved knowledge preparation from query-time access.

Proposed stores have different responsibilities: knowledge indexes retain source and access lineage; checkpoints retain bounded workflow state; an artifact registry retains versioned release inputs; audit storage retains consequential decisions. Enterprise systems remain authoritative for appointments. Retrieval never substitutes for transactional authorization, and patient records are not automatically copied into a knowledge index. Deletions must reach derived chunks, indexes, and caches. Feedback requires review before reuse as training data.

### Infrastructure observation does not establish AI quality

The [observability data-source guide](https://docs.nvidia.com/enterprise-reference-architectures/observability-guide/latest/configuration-of-data-sources.html) covers infrastructure and inference signals. Its [scope boundary](https://docs.nvidia.com/enterprise-reference-architectures/observability-guide/latest/out-of-scope.html) reinforces that an infrastructure monitoring setup is not the complete application-observation design.

Stratum therefore proposes three correlated views: infrastructure health and capacity; agent, retrieval, model, tool, and workflow behavior; and business completion, cost, and quality. GPU signals apply only to operated GPU infrastructure. Retain action and version metadata without collecting hidden reasoning or raw patient prompts. Required audits are unsampled. Collectors and dashboards require authenticated, encrypted connections.

### Deployment needs repeatability and separation

The [deployment-strategy guidance](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-factory-white-paper/latest/deployment-strategies.html) distinguishes provisioning from configuration and ongoing deployment. Stratum proposes infrastructure definitions, pinned artifact manifests, isolated environments, and reviewed promotion as separate responsibilities.

The [reference architecture design tenets](https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/design-tenets.html) and [configuration deep dive](https://docs.nvidia.com/enterprise-reference-architectures/white-paper/latest/reference-architectures-deep-dive.html) inform workload-based sizing and network separation. Their physical deployment assumptions are not automatically suitable for a multitenant patient-facing service. Stratum must independently validate tenant isolation, recovery, data placement, and availability.

## What to adopt, defer, and prove

**Adopt now:** Cloud–Core–Edge layout; separate AI and data services; explicit connections and ownership; modular agentic registries; AI DLC, AI QE, and observability as shared core services; phased Deploy → Interconnect → Extend delivery.

**Defer until justified:** GPU clusters, training infrastructure, dedicated colocation, multiple regions, a lakehouse, and additional cloud providers. None is provisioned by this repository.

**Prove next:** one synthetic booking journey, server-side identity and authorization, confirmation-bound writes, timeout reconciliation, an end-to-end trace, and a quality gate that rejects a deliberately defective candidate. Then onboard a second application to test the reuse claim.

**Leadership interpretation:** the near-term investment is a reusable delivery and runtime capability. The initial proof is reliable task completion and reviewable release evidence. Hardware investment follows measured demand. The portal demonstrates consumption; it must not accumulate its own orchestration, model routing, evaluation infrastructure, or monitoring backend.
