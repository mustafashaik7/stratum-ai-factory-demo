# Stratum — Reusable AI Factory

**Architecture and executive progress brief | 30 September 2026 | Proposed design**

## Purpose and strategic importance

Create a reusable foundation that builds, verifies, runs, and observes AI-enabled applications, with accountability for quality, cost, and operational impact.

**Working name: Stratum.** A foundational layer on which applications are built. The name is a proposal; brand and trademark availability have not been assessed.

The opportunity is to make software delivery a repeatable capability across a portfolio of performance-improvement applications. Expert knowledge, business rules, and successful delivery patterns become reusable assets. Leadership gains visibility into what was delivered, why it was prioritized, how it was verified, and whether it produced the intended result.

The Patient Portal is the first proposed application. Its appointment-booking journey will demonstrate the platform before expansion to other domains.

**Current position:** architecture, delivery boundaries, example specifications, and initial acceptance scenarios are drafted. A working factory, validated integrations, and measured benefits remain to be demonstrated.

## Goals

| Goal | Intended outcome | Evidence of success |
|---|---|---|
| Shorten delivery time | Move approved improvement priorities into usable software sooner | Time from approved requirement to accepted release |
| Increase team capacity | Reduce repeated setup and implementation work | Engineering effort and total cost per accepted change |
| Standardize quality | Apply consistent verification and release controls | First-pass acceptance, escaped defects, and release evidence completeness |
| Preserve domain expertise | Represent approved practices as versioned rules and tests | Reuse of validated components and configurations |
| Connect investment to value | Link each change to an operational objective | Business-owner review of post-release results |
| Scale across applications | Add domains without rewriting the factory | A second application using the same core lifecycle |

Targets will follow baseline measurement. Faster code generation alone will not count as success.

## Problems the platform will address

**Repeated work across teams:** similar setup, integration, testing, and release needs consume capacity. Shared templates and adapters make those investments reusable.

**A gap between insight and execution:** identifying an opportunity does not implement an improvement. The factory attaches an owner, acceptance criteria, a delivery workflow, and an outcome measure to approved work.

**Inconsistent AI-assisted delivery:** informal prompting and review can produce variable results. Versioned specifications, limited permissions, and independent checks establish a consistent operating model.

**Limited visibility into realized value:** completing a feature does not establish an operational benefit. Delivery evidence and post-release measures allow leaders to assess adoption, impact, and further investment.

These are design hypotheses; discovery will establish their magnitude in the participating environment.

## What differentiates this design

| Design choice | Why it matters |
|---|---|
| Business objective attached to each request | Connects prioritization to access, quality, efficiency, cost, or growth |
| Generic core with domain-specific configuration | Supports reuse with controlled local variation |
| Independent verification and release evidence | Makes acceptance reviewable beyond an agent's self-assessment |
| Expert practices represented as reusable assets | Makes knowledge repeatable and changes accountable |
| Shared outcome definitions | Supports meaningful comparison across applications and sites |
| Replaceable technology interfaces | Allows approved models, tools, and hosting to evolve |

The intended differentiator is the combination of governed delivery, reusable expertise, and outcome measurement. This is a proposed design advantage, not a claim of market exclusivity.

## Architecture

```mermaid
flowchart TB
    INTENT[Business goals and application configuration] --> DLC
    subgraph STRATUM[Stratum: reusable application foundation]
        DLC[AI DLC: specify, build and evolve] --> QE[AI QE: verify and evaluate]
        QE --> RELEASE[Approved versioned release]
        RELEASE --> RUN[Runtime services and capability APIs]
        PACKS[Versioned domain packs] --> RUN
        RUN --> OBS[AI Observability: quality, cost and outcomes]
        OBS --> DLC
        QE --> EVIDENCE[Evidence and governance]
        OBS --> EVIDENCE
    end
    RELEASE --> APP[Thin applications: Patient Portal and future experiences]
    APP --> RUN
    RUN --> SYSTEMS[Authorized enterprise systems]
```

Stratum has two separately operated environments: a **delivery control plane** that builds and verifies releases, and a **runtime plane** that serves deployed applications. The portal continues when delivery services are unavailable. It depends on runtime capability APIs for business operations; runtime outages require explicit degraded behavior and recovery.

| Platform layer | Responsibility | Application contribution |
|---|---|---|
| AI DLC | Intake, specification, planning, implementation, release, and improvement | Business intent and approved acceptance criteria |
| AI QE pipelines | Shared test execution, AI evaluations, quality gates, and evidence | Domain scenarios and expected outcomes |
| Runtime foundation | Identity enforcement, workflow state, models, tools, knowledge access, and capability APIs | Selected capabilities and approved configuration |
| Domain packs | Reusable business services, domain policy, integrations, and evaluation datasets | Local policy inputs reviewed by domain owners |
| AI Observability | Traces, metrics, quality signals, cost, audit, dashboards, and alerts | Journey event names and outcome definitions |

The generic core understands workflows, identity context, tools, policies, evaluations, and releases. Healthcare types and scheduling behavior live in a separately versioned healthcare pack hosted by Stratum. This keeps the portal thin while keeping the core reusable. Domain experts own pack rules; the platform operates the pack through common interfaces.

## AI DLC — AI Development Lifecycle

AI DLC covers both **software produced with AI** and **AI behavior deployed in an application**. Changes to code, prompts, models, retrieval content, tools, policies, and domain packs follow the same governed lifecycle.

| Stage | Shared platform service | Required output |
|---|---|---|
| Define | Intake, value assessment, risk classification, and scope review | Approved intent, owner, baseline, and acceptance criteria |
| Specify | Requirements, architecture, data contracts, and evaluation design | Versioned implementation and evaluation specification |
| Build | Isolated workers, approved templates, context assembly, and bounded repair | Candidate code and AI configuration |
| Verify | Independent AI QE pipeline | Results bound to candidate versions |
| Release | Approval, compatibility checks, staged rollout, and rollback controls | Approved release manifest and deployment record |
| Operate and improve | Observability, incident review, regression creation, and retirement | Reviewed improvement backlog and outcome assessment |

The release manifest binds application code, domain-pack version, model deployment, prompt version, tool schemas, retrieval snapshot or index version, policy version, and evaluation suite. Changing a material dependency triggers the applicable checks before promotion. Production observations cannot silently rewrite prompts or policies.

## AI QE — shared Quality Engineering pipelines

Quality Engineering is a platform service consumed by every application. The application supplies its scenarios; Stratum provisions the environment, runs the checks, manages evaluation datasets, enforces thresholds, and retains evidence.

| Pipeline stage | Coverage | Promotion rule |
|---|---|---|
| Change and dependency analysis | Changed code, prompts, models, content, tools, and policies | Select affected suites; required checks cannot be omitted |
| Software verification | Build, unit, API contracts, integration, browser journeys, accessibility, and dependency security | Required deterministic checks pass |
| AI behavior evaluation | Grounding, unsupported claims, task completion, tool choice, injection resistance, sensitive-data handling, and refusal behavior | Meet approved per-use-case thresholds |
| Workflow resilience | Authorization, concurrency, retries, timeouts, fallback, load, and recovery | No blocking security or transaction-integrity failures |
| Independent acceptance | Protected scenarios and domain-owner review | Candidate meets business acceptance criteria |
| Staged release validation | Synthetic probes and monitored rollout with stop conditions | Promote, hold, or roll back based on approved policy |

Use synthetic or approved de-identified datasets with controlled provenance. Keep holdout scenarios inaccessible to implementation workers. Version datasets and repeat probabilistic evaluations across representative cases; report uncertainty and regressions, not a single favorable score. Model-based judging is calibrated against human-reviewed examples and supplements deterministic checks. No universal accuracy threshold is assumed: domain owners approve thresholds before evaluation.

Missing evidence blocks promotion. AI-generated tests do not provide independent assurance by themselves. UI changes still require experience and accessibility verification even when business logic is supplied by the platform.

## AI Observability — shared operational intelligence

Stratum supplies instrumentation, collection, dashboards, alerts, and incident routing. A shared client library propagates request context; runtime services attach workflow and release metadata. Every application receives a standard operating view without building a separate monitoring stack.

| Signal | What the platform captures | Purpose |
|---|---|---|
| End-to-end traces | Application request, workflow steps, retrieval, model calls, tools, and integration outcomes | Locate failures and slow steps |
| AI quality | Grounding checks, user feedback, sampled reviewed outputs, evaluation regressions, and drift indicators | Detect degradation for investigation |
| Reliability | Availability, latency, errors, retries, queue time, pending operations, and fallback use | Manage service objectives and recovery |
| Cost | Tokens, model usage, workflow duration, and cost per completed task | Attribute consumption and enforce budgets |
| Audit | Actor, authorization decision, confirmation, action, outcome, and version references | Reconstruct consequential operations |
| Business outcomes | Completion, abandonment, assistance, and approved operational measures | Connect technical operation to value |

Correlate signals by application, organization, workflow, request, and release version using protected or pseudonymous identifiers. Do not log raw patient content or full prompts by default. Apply redaction, scoped access, retention, and separate audit storage. Sampling may reduce diagnostic volume but must not omit required audit records.

Define service objectives, alert thresholds, escalation owners, and runbooks before pilot. Breaches can pause rollout or disable optional AI while preserving deterministic workflows. Unknown external writes require reconciliation, not blind retry. Drift is a signal for evaluation, not proof that behavior is wrong. Incidents produce reviewed regression scenarios that return to AI QE and AI DLC.

## Thin application consumption model

An application registers a versioned manifest naming its capabilities, domain pack, experience configuration, acceptance scenarios, and service objectives. Stratum supplies a client SDK, versioned APIs, standard delivery pipelines, and default dashboards. All client inputs remain untrusted; identity and authorization are enforced server-side.

The Patient Portal owns screens, navigation, branding, accessibility, and the presentation of confirmation and status. Stratum hosts booking services, healthcare adapters, workflow state, authorization enforcement, AI assistance, and observability. A new application should not rebuild a model gateway, agent orchestrator, policy engine, evaluation runner, or telemetry backend.

Keep capabilities modular with published compatibility rules. Domain packs can be deployed independently where isolation or availability requires it; shared ownership does not require one monolithic runtime. Contract tests prevent a platform upgrade from breaking consumers.

## Delivery and governance

Each change follows **approve intent → plan → implement → verify → approve release → measure results**.

Implementation uses approved context and synthetic test data in an isolated environment. Independent verification checks the exact version proposed for release. Missing or failed mandatory checks block promotion. Execution budgets and retry limits stop unbounded repair loops.

Evidence links the business requirement, approved rules, software version, tests, reviewer decisions, and deployed artifact. Requirements or code changes invalidate affected evidence. Agents cannot grant themselves permissions or approve production release.

The platform team owns shared capabilities; domain experts own business rules; application teams own experience and integrations; independent reviewers own acceptance controls; operations owns deployed reliability. Production patient records and credentials are excluded from development-agent access.

Cross-organization reuse applies to approved patterns and definitions. Data remains scoped to authorized organizations. Comparative analysis requires data rights, consistent definitions, suitable cohorts, and privacy controls. No proprietary datasets or enterprise integrations are assumed available.

## Progress and investment milestones

| Milestone | Status | Exit evidence |
|---|---|---|
| Architecture and boundaries | Drafted | Reviewed and accepted platform scope |
| Example application specifications | Drafted | Approved requirements and executable checks |
| Factory delivery path | Planned | One application change completes all delivery stages |
| AI DLC and AI QE services | Specified; implementation planned | A code or prompt change traverses the lifecycle; a defective candidate is blocked |
| AI Observability | Specified; implementation planned | One trace spans portal, workflow, tools, and scheduler; alert and cost views work |
| Thin consumer boundary | Specified; implementation planned | Portal calls capability APIs without embedded domain orchestration |
| Reuse demonstration | Planned | Second application delivered without domain changes to the core |
| Controlled integration pilot | Pending access and ownership decisions | Integration validation, operational acceptance, and baseline measures |

The first proof point is a synthetic Patient Portal booking feature with functioning software, independent test results, and traceable release evidence. A small employee-service application can then establish reuse. Broader operational or service-line workflows require separate business cases.

## Executive scorecard and leadership decisions

Track delivery lead time, effort, total cost per accepted change, first-pass acceptance, escaped defects, evidence completeness, and reuse. Include verification and repair costs, and compare changes of similar complexity and risk.

For each application, track its intended operational outcome over an agreed observation period. Do not attribute gains to AI without accounting for other changes. Reliable releases, reuse, and measured improvement together determine expansion.

The next decision is support for a bounded demonstration: a platform owner, application owner, verification capacity, and approved environment. Delivery dates and cost estimates follow confirmation of those resources. Further investment should depend on evidence from the demonstration and reuse milestone.

**Companion:** [Patient Portal architecture](apps/patient-portal/Architecture.md).
