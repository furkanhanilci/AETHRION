---
title: "WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding"
aliases:
  - "WP-101"
  - "WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Every service's owner, tier, dependencies, data class, SLIs/SLOs, error budget, dashboard, alerts, runbook and DR class are held in one catalogue."
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding

## Package card

| Field | Value |
|---|---|
| Work package | `WP-101` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Service Owners / Internal Audit |
| Hard dependencies | WP-002, WP-022, WP-025, WP-026, WP-028, WP-031, WP-041, WP-049, WP-052, WP-055, WP-056, WP-061, WP-075, WP-096, WP-098, WP-099, WP-100 |
| Related gates | Platform |
| Related controls | CTL-OBS-01, CTL-OPS-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_101_service_slo_alerting.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_101_service_slo_alerting.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every service's owner, tier, dependencies, data class, SLIs/SLOs, error budget, dashboard, alerts, runbook and DR class are held in one catalogue.


## Analysis
### What this package actually decides

That every service has an owner who will be paged. The catalogue is the artifact,
and its enforcement property is simple: **a service with no owner cannot be
released**.

`CODEOWNERS` in this repository already states the same rule for paths — *a path
with no owner has no accountable reviewer and cannot reach `ACCEPTED`*.

### Correctness and freshness are SLIs, and they are the ones that get omitted (T03)

Availability and latency are standard. Two others matter more here:

- **Correctness** — the projection matches its canonical source, the chain
  verifies, the manifest resolves. A service that is up and returning wrong data
  has an availability of 100%.
- **Freshness** — the read model's lag. WP-091 displays it; this is where it gets a
  threshold and an error budget.

A laboratory whose SLIs cover only uptime is measuring the least interesting
failure mode it has.

### Error budgets and the release freeze (T04)

An error budget nobody enforces is a metric. The freeze rule is what converts it
into a control — and it needs an explicit exception path, because a freeze during a
security incident is itself a risk.

### Tiering follows the critical user journeys, not the org chart (T02)

The journeys that matter: a claim reaching publication, a decision reaching an
owner, a retraction reaching a dependent claim. A service on one of those paths is
tier 1 regardless of how simple it is.

### The runbook link checker (T05)

Same lesson as WP-098: a runbook link that rots is discovered during an incident.
Checking them on a schedule is trivial and it is exactly the kind of check that
gets skipped.

### Dependency roll-up makes a hidden single point of failure visible (T06)

Six tier-2 services depending on one tier-3 service means the tier-3 service is
effectively tier-1. The roll-up computes it rather than waiting for an outage to
demonstrate it.

### Baseline v1.3.0 — showing the cost of collaboration, and the shape of a decision

The experience and observability layer gains three things it could not
previously display, because they did not exist to be displayed.

**Collaboration cost.** Coordination overhead ratio, redundant message rate,
useful challenge rate, rounds, and the token ledger's seven categories. A single
cost total says a campaign was expensive; the categories say whether it was
expensive because it did science or because it held a meeting.

**The human decision surface, reordered.** Evidence first, recommendation second,
and a `DecisionDelta` when the second changes the first (`ADR-016`). The queue
uses evidence-delta priority — what changed since the last decision, not the full
state every time. **Attention priority orders and never authorises**, and no
timeout or learned preference produces an approval.

**Verifier abstention, surfaced.** An `ABSTAIN` is an escalation signal and has to
look like one in the interface. A surface that renders it as a soft pass has
undone `ADR-015`.

New SLOs: coordination overhead, challenge rate, contamination and security
findings, and the quality/cost Pareto frontier.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

17, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md) | `Requirement Registry` · `NFR scorecard` · `Traceability matrix seed` · `Scope boundary record` |
| [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md) | `Repository skeleton` · `CODEOWNERS` · `Dependency rules` · `Developer guide` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md) | `Temporal platform` · `Namespace/queue catalog` · `Worker identity policy` · `HA/failover runbook` |
| [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md) | `LiteLLM deployment` · `Provider configuration` · `Gateway policy adapter` · `Model-call audit/cost events` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md) | `Kubernetes clusters` · `Node pool catalog` · `Namespace/security baseline` · `Upgrade/restore runbook` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |
| [WP-056 — Policy Decision Point and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md) | `Policy decision point` · `PolicyDecision interface conformance suite` · `Policy bundle v1` · `Policy test suite` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md) | `OTel platform` · `Semantic conventions` · `Instrumentation libraries` · `Trace completeness dashboard` |
| [WP-098 — Grafana and the Six Operational Graphs](../09_EXPERIENCE_OBSERVABILITY/wp_098_grafana_six_graphs.md) | `Grafana platform` · `Six graph dashboards` · `Alert rules` · `Dashboard/alert ownership catalog` |
| [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md) | `Audit Ledger` · `Hash-chain service` · `Audit export/verify tooling` · `Retention/access policy` |
| [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md) | `Cost Ledger` · `Budget service` · `Cost adapters` · `Invoice reconciliation` |

### Full prerequisite closure

**60 of 160 packages (38%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |
| 30 | `WP-096` |
| 31 | `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-098` |

### What acceptance of this package releases

- **Directly unblocked:** 8 — `WP-102` · `WP-114` · `WP-116` · `WP-117` · `WP-118` · `WP-122` · `WP-128` · `WP-140`
- **Transitively reachable:** **24 of 160 packages (15%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **33** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | SRE Lead |
| Independent verifier | Service Owners / Internal Audit |
| Gates touched | `Platform` |
| Controls | `CTL-OBS-01` · `CTL-OPS-03` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md), [WP-098 — Grafana and the Six Operational Graphs](../09_EXPERIENCE_OBSERVABILITY/wp_098_grafana_six_graphs.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Requirement Registry` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `NFR scorecard` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Traceability matrix seed` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Scope boundary record` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Repository skeleton` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CODEOWNERS` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Dependency rules` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Developer guide` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `NATS cluster` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Outbox relay` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Consumer SDK` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `DLQ/replay runbook` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Event dashboards` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Temporal platform` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Namespace/queue catalog` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Worker identity policy` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `HA/failover runbook` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `SLO dashboard` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `LiteLLM deployment` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Provider configuration` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway policy adapter` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Model-call audit/cost events` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway runbook` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Kubernetes clusters` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Node pool catalog` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Namespace/security baseline` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Upgrade/restore runbook` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Policy decision point` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `PolicyDecision interface conformance suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `OTel platform` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Semantic conventions` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Instrumentation libraries` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Trace completeness dashboard` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Grafana platform` | `WP-098` | `python3 scripts/progress.py show WP-098` |
| `Six graph dashboards` | `WP-098` | `python3 scripts/progress.py show WP-098` |
| `Alert rules` | `WP-098` | `python3 scripts/progress.py show WP-098` |
| `Dashboard/alert ownership catalog` | `WP-098` | `python3 scripts/progress.py show WP-098` |
| `Audit Ledger` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Hash-chain service` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Audit export/verify tooling` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Retention/access policy` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Integrity dashboard` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Cost Ledger` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Budget service` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Cost adapters` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Invoice reconciliation` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `FinOps dashboard/runbook` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Token ledger categories` | `WP-100` | `python3 scripts/progress.py show WP-100` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **SRE Lead** carries the acceptance decision; **Service Owners / Internal Audit** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-101-T01 | Establish the Service Catalogue schema and registry | Implementation owner | Commit / configuration / record reference |
| WP-101-T02 | Map service tiers onto the critical user journeys | Implementation owner | Commit / configuration / record reference |
| WP-101-T03 | Define the availability, latency, correctness, freshness and durability SLIs | Implementation owner | Commit / configuration / record reference |
| WP-101-T04 | Write the error-budget and release-freeze rules | Implementation owner | Commit / configuration / record reference |
| WP-101-T05 | Add the alert owner, escalation and runbook link checker | Implementation owner | Commit / configuration / record reference |
| WP-101-T06 | Establish dependency/SLO roll-up and a quarterly review | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Service Catalog`
- `SLO catalog`
- `Error-budget policy`
- `Alert-runbook link checker`
- `Ownership dashboard`
- `Coordination overhead and Pareto SLOs`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-101_service_slo_alerting.tests.md`](wp_101_service_slo_alerting.tests.md).

- Detection of orphaned services and alerts
- A synthetic SLO breach
- An error-budget-driven release freeze
- Owner-departure continuity
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-101_service_slo_alerting.acceptance.md`](wp_101_service_slo_alerting.acceptance.md), together with what this package still cannot establish.

- [ ] No production service opens without an owner, a runbook and an SLO.
- [ ] Correctness and freshness SLOs are measured alongside uptime.
- [ ] Every critical alert carries a 24×7 escalation path.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A wrong SLO change is rolled back under service owner plus SRE review; silencing an alert counts as disabling a control and requires a time-bound exception.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
