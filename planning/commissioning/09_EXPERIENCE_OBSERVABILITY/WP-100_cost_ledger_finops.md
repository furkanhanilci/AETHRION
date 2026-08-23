# WP-100 — Cost Ledger, Budget Envelopes and FinOps

## Package card

| Field | Value |
|---|---|
| Work package | `WP-100` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | FinOps Lead |
| Independent verifier | Project Decision Owner / Internal Audit |
| Hard dependencies | WP-011, WP-013, WP-015, WP-016, WP-025, WP-028, WP-041, WP-045, WP-049, WP-052, WP-053, WP-082, WP-096 |
| Related gates | G0,G4,G5,G8 |
| Related controls | CTL-CST-01, CTL-CST-02 |
| Related acceptance scenarios | ACC-09, ACC-29 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-100_cost_ledger_finops.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-100_cost_ledger_finops.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Model, compute, retrieval, storage, verification and human triage costs are attributed to project, workflow, run, role, profile and outcome, with an 80% warning and a 100% hard stop.


## Analysis
### What this package actually decides

That spending is **reserved before it happens**. Estimate → reserve → commit →
release. The alternative — accounting after the fact — tells you what a runaway
cost, which is the definition of `PR-09`.

`00_PROGRAM/01` invariant 9: at the hard limit **no new expensive work opens** and
the workflow **pauses without losing state**.

### Attribution to outcome is the unusual half (T06)

Cost per project and per run is ordinary FinOps. Cost per **outcome** — what did
this claim cost, what did this reproduction cost, what did a rejected result cost —
is what makes the quality-adjusted comparisons in WP-044 and WP-045 possible.

It also makes an uncomfortable number visible: the cost of work that produced a
negative result, which a laboratory needs to be able to see without treating it as
waste.

### Fan-out and retry are where budgets actually fail (T03)

`PR-09`'s early signal is *fan-out, retry, token growth*. A council of five costs
five times; a retry storm costs without bound. Both must draw from the original
reservation rather than extending it silently, which is the rule WP-045 and WP-053
enforce and this package accounts for.

### Human triage is a cost and is usually uncounted (purpose sentence)

The purpose names it explicitly. `00_PROGRAM/08` treats human decision capacity as
a hard quota, and a cost model that counts tokens and ignores the hours a person
spent has mispriced the scarcest resource in the system.

### Invoice reconciliation is what keeps the ledger honest (T05)

Provider bills and internal accounting diverge — by rounding, by unmetered calls,
by a misattributed project. A variance case with an owner is what stops the ledger
quietly becoming approximate.

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

13, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md) | `EventEnvelope schema` · `Event Catalog seed` · `Subject/retention table` · `Consumer contract` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md) | `LiteLLM deployment` · `Provider configuration` · `Gateway policy adapter` · `Model-call audit/cost events` |
| [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md) | `Policy Router` · `RouteDecision service` · `Fan-out/budget rules` · `Routing conformance suite` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md) | `Kubernetes clusters` · `Node pool catalog` · `Namespace/security baseline` · `Upgrade/restore runbook` |
| [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md) | `Kueue configuration` · `Quota/priority policy` · `Budget admission adapter` · `Queue dashboard` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md) | `OTel platform` · `Semantic conventions` · `Instrumentation libraries` · `Trace completeness dashboard` |

### Full prerequisite closure

**53 of 160 packages (33%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |
| 30 | `WP-096` |

### What acceptance of this package releases

- **Directly unblocked:** 9 — `WP-101` · `WP-102` · `WP-104` · `WP-111` · `WP-117` · `WP-127` · `WP-145` · `WP-150` · `WP-153`
- **Transitively reachable:** **33 of 160 packages (21%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **31** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | FinOps Lead |
| Independent verifier | Project Decision Owner / Internal Audit |
| Gates touched | `G0` · `G4` · `G5` · `G8` |
| Controls | `CTL-CST-01` · `CTL-CST-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-09 — Budget Hard Stop](../12_ACCEPTANCE_SCENARIOS/ACC-09_budget_hard_stop.md) | Critical | An 80% warning is raised; at 100% new expensive work is denied, the workflow pauses with state and checkpoints preserved, and no duplicate cost or reservation is created. |
| [ACC-29 — Provider Invoice Variance](../12_ACCEPTANCE_SCENARIOS/ACC-29_invoice_variance.md) | Medium | A `VarianceCase` opens with a provider/project/model/time-bucket breakdown, an owner, an SLA and an adjustment or dispute path; ledger history is never deleted. |
| [ACC-59 — Discovery Search Stagnation](../12_ACCEPTANCE_SCENARIOS/ACC-59_discovery_search_stagnation.md) | High | The detector fires at the configured boundary, the configured action is taken, and the campaign terminates. An unbounded search is impossible even if every model in it recommends continuing. |
| [ACC-100 — Token Ledger Classification](../12_ACCEPTANCE_SCENARIOS/ACC-100_token_ledger_classification.md) | High | Every token carries one of the seven categories, the categories sum to the total, and the coordination overhead ratio is derivable from the ledger rather than estimated. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md)
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
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `EventEnvelope schema` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Event Catalog seed` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Subject/retention table` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Consumer contract` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `Post-commit event taxonomy for the collaboration plane` | `WP-015` | `python3 scripts/progress.py show WP-015` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |
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
| `LiteLLM deployment` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Provider configuration` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway policy adapter` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Model-call audit/cost events` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway runbook` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Policy Router` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `RouteDecision service` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Fan-out/budget rules` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Routing conformance suite` | `WP-045` | `python3 scripts/progress.py show WP-045` |
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
| `Kueue configuration` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Quota/priority policy` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Budget admission adapter` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Queue dashboard` | `WP-053` | `python3 scripts/progress.py show WP-053` |
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
| `OTel platform` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Semantic conventions` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Instrumentation libraries` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Trace completeness dashboard` | `WP-096` | `python3 scripts/progress.py show WP-096` |

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
- **FinOps Lead** carries the acceptance decision; **Project Decision Owner / Internal Audit** must verify independently of whoever implements.
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
| WP-100-T01 | Establish the `BudgetEnvelope`, C0–C4 classes and the reservation API | Implementation owner | Commit / configuration / record reference |
| WP-100-T02 | Ingest gateway, Kueue, tool, storage and human cost events | Implementation owner | Commit / configuration / record reference |
| WP-100-T03 | Write estimate → reserve → commit → release plus retry and fan-out attribution | Implementation owner | Commit / configuration / record reference |
| WP-100-T04 | Integrate the 80% and 100% thresholds with Temporal pause and decision flows | Implementation owner | Commit / configuration / record reference |
| WP-100-T05 | Add provider invoice reconciliation and variance cases | Implementation owner | Commit / configuration / record reference |
| WP-100-T06 | Build the quality-adjusted cost/outcome dashboard and forecast | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Cost Ledger`
- `Budget service`
- `Cost adapters`
- `Invoice reconciliation`
- `FinOps dashboard/runbook`
- `Token ledger categories`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-100_cost_ledger_finops.tests.md`](WP-100_cost_ledger_finops.tests.md).

- The 80% warning
- Denial of new expensive work at 100%
- Release of a cancelled reservation
- Idempotency against duplicate cost events
- An invoice variance case
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-100_cost_ledger_finops.acceptance.md`](WP-100_cost_ledger_finops.acceptance.md), together with what this package still cannot establish.

- [ ] Exceeding a hard budget never loses state.
- [ ] Cost is not measured in tokens alone.
- [ ] Critical assurance capacity is visible inside the budget policy.
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

The effect of a faulty cost adapter is corrected through reconciliation; a hard stop is never disabled manually — it requires an owner `DecisionRecord`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
