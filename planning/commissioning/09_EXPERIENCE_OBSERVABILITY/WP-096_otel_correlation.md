# WP-096 — OpenTelemetry End-to-End Correlation Spine

## Package card

| Field | Value |
|---|---|
| Work package | `WP-096` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Observability Lead |
| Independent verifier | Security / SRE |
| Hard dependencies | WP-011, WP-015, WP-020, WP-021, WP-025, WP-028, WP-031, WP-041, WP-046, WP-049, WP-052, WP-055, WP-057, WP-082 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-096_otel_correlation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-096_otel_correlation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The same project/workflow/run/trace correlation travels from a console command through the Temporal workflow, agent/model/tool calls, the sandbox, the database and event bus, and into artifact, claim and cost records.


## Analysis
### What this package actually decides

That one correlation identifier survives every hop. Console → workflow → agent →
model → tool → sandbox → database → event bus → artifact → claim → cost.

`00_PROGRAM/01` invariant 1 needs it: a material claim resolves to its source span,
run, review and decision **in a single query**. That join is only possible if the
identifier was propagated at every boundary, and every boundary is a place it can
be dropped.

### Trace completeness is an SLO, not a nice-to-have (T06)

A trace that is 90% complete is a trace with a gap exactly where something went
wrong, because failures are where instrumentation is thinnest. Measuring
completeness — what fraction of spans in a workflow resolve to a full parent chain
— is what turns propagation from an intention into a monitored property.

### Data-class routing at the collector (T01)

Traces carry payloads. A span attribute containing D3 content routed to a
general-purpose store has moved data across a boundary, and telemetry is the path
nobody threat-models. The collector is where the class is enforced.

### Semantic conventions must be fixed before instrumentation, not after (T02)

Renaming a span attribute later means every dashboard, alert and query built on it
breaks silently — they return empty rather than erroring. The conventions are a
contract (WP-020's rules apply), and they are cheapest to fix first.

### The clock policy is the detail that breaks distributed traces (T05)

Spans from machines with skewed clocks produce negative durations and impossible
orderings. A declared clock policy and a skew alarm are what keep a trace readable
across the execution fabric.

### Error escalation, because sampled traces lose the interesting ones (T05)

Head sampling drops most traces. The ones worth keeping are the ones that failed —
so an error must escalate its trace to always-sampled, or the system will be best
instrumented for the paths that work.

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

14, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md) | `Temporal platform` · `Namespace/queue catalog` · `Worker identity policy` · `HA/failover runbook` |
| [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md) | `LiteLLM deployment` · `Provider configuration` · `Gateway policy adapter` · `Model-call audit/cost events` |
| [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md) | `LangGraph runtime` · `Temporal adapter` · `Checkpoint policy` · `Agent graph SDK` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md) | `Kubernetes clusters` · `Node pool catalog` · `Namespace/security baseline` · `Upgrade/restore runbook` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |
| [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md) | `Egress proxy` · `Allowlist registry` · `DLP pipeline` · `Egress audit/alerts` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |

### Full prerequisite closure

**51 of 160 packages (32%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |

### What acceptance of this package releases

- **Directly unblocked:** 10 — `WP-097` · `WP-098` · `WP-099` · `WP-100` · `WP-101` · `WP-104` · `WP-107` · `WP-117` · `WP-150` · `WP-152`
- **Transitively reachable:** **40 of 160 packages (25%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **30** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Observability Lead |
| Independent verifier | Security / SRE |
| Gates touched | `G0–G10` · `Platform` |
| Controls | `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
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
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Environment topology` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Account/network IaC` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Access baseline` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Environment promotion policy` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
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
| `LangGraph runtime` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Temporal adapter` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Checkpoint policy` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Agent graph SDK` | `WP-046` | `python3 scripts/progress.py show WP-046` |
| `Conformance tests` | `WP-046` | `python3 scripts/progress.py show WP-046` |
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
| `Egress proxy` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Allowlist registry` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `DLP pipeline` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Egress audit/alerts` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Exception runbook` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Run Registry` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Preflight validator` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `MLflow integration` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lineage queries` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lifecycle dashboard` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `RawEvaluatorArtifact` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `VerifiedValue` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `PredictionRecord` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `FailureAssessment` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `ModelExecutionFingerprint` | `WP-082` | `python3 scripts/progress.py show WP-082` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Observability Lead** carries the acceptance decision; **Security / SRE** must verify independently of whoever implements.
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
| WP-096-T01 | Deploy the OTel collector/gateway in HA with tenant and data-class routing | Implementation owner | Commit / configuration / record reference |
| WP-096-T02 | Write the trace, span, log and metric semantic conventions | Implementation owner | Commit / configuration / record reference |
| WP-096-T03 | Bind the context-propagation SDKs into every service | Implementation owner | Commit / configuration / record reference |
| WP-096-T04 | Add Temporal activity, LangGraph, model, tool, database, NATS and Kubernetes instrumentation | Implementation owner | Commit / configuration / record reference |
| WP-096-T05 | Apply the sampling, error-escalation and clock policy | Implementation owner | Commit / configuration / record reference |
| WP-096-T06 | Establish trace-completeness SLOs and queries | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `OTel platform`
- `Semantic conventions`
- `Instrumentation libraries`
- `Trace completeness dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-096_otel_correlation.tests.md`](WP-096_otel_correlation.tests.md).

- An end-to-end request trace
- Asynchronous NATS causation linking
- Retry and duplicate span semantics
- An alert on missing correlation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-096_otel_correlation.acceptance.md`](WP-096_otel_correlation.acceptance.md), together with what this package still cannot establish.

- [ ] Correlation identifiers match the canonical records exactly.
- [ ] A missing trace is not business state loss, but it is an SLO violation.
- [ ] No D3/D4 raw payload becomes a span attribute.
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

A collector outage never makes the workflow unsafe — telemetry buffers or drops per policy; configuration is rolled back and the gap opens an `IncidentRecord`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
