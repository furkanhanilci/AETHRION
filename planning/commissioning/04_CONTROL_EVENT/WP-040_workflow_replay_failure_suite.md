# WP-040 — Workflow Replay, Versioning and Failure Test Suite

## Package card

| Field | Value |
|---|---|
| Work package | `WP-040` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Independent SRE / Control Plane Reviewer |
| Hard dependencies | WP-024, WP-031, WP-032, WP-033, WP-034, WP-035, WP-036, WP-037, WP-038, WP-039 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-OPS-01, CTL-OPS-02 |
| Related acceptance scenarios | ACC-10, ACC-11, ACC-13, ACC-14, ACC-35 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-040_workflow_replay_failure_suite.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-040_workflow_replay_failure_suite.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Open workflow histories continue without state loss across code deployments, worker/provider/database loss, retries, timeouts and compensation.


## Analysis
### What this package actually decides

Whether an open workflow survives the next deployment. Everything else in
`04_CONTROL_EVENT` is about behaviour when things go right; this package is the
only one about behaviour when they do not.

### Golden histories are the asset, and they age (T01)

A recorded history from a real execution, replayed against every subsequent build.
It catches the specific failure that no unit test can: a code change that is
correct for new executions and nondeterministic for existing ones.

The maintenance burden is real — a golden history must be *replaced* when a
version marker legitimately changes behaviour, and the replacement has to be a
recorded decision rather than a refresh. Otherwise the suite silently stops
testing the thing it exists for.

### Replay in CI is the enforcement point (T02)

The determinism rule (WP-032) is unenforceable by review; nondeterminism looks
like ordinary code. Running replay on every workflow build is what turns it into a
build failure — and it depends on WP-024, like everything else that fails a build.

### Fault injection has to reach the provider layer (T04)

Killing a worker tests the worker. Losing the database, losing NATS, and losing a
model provider test three different assumptions, and each has a distinct correct
behaviour: block and retry, buffer and resume, fail over or fail closed. A suite
that only kills workers has tested the easiest case.

### The comparison report is what makes the run evidence (T06)

"It recovered" is an impression. State equality, artifact digest equality and
integrity-query results are a claim. This is the same distinction as WP-025's
restore: the service starting is not the test.

### Baseline v1.3.0 — new policies at the gates, without moving authority

G0–G10 consumes the collaboration, conformance, assurance and reproduction
policies this baseline adds. **None of that moves authority.** Temporal still
owns lifecycle transitions and LangGraph still owns bounded cognition inside one
task, and a checkpoint in the second cannot transition a gate in the first.

Three concrete additions:

- **G5 and G6** consume the cohort, the topology, the specification conformance
  result and the assurance route.
- **G7** consumes the model execution fingerprint and the reproduction level it
  supports — a hosted black-box model does not yield `EXACT`.
- **G8** runs the human preliminary flow: the recommendation is unreachable
  until the human assessment is sealed, through **every** interface rather than
  only the UI.

And the write path becomes explicit: a canonical transaction and its outbox
record commit atomically, the publisher reads the outbox afterwards, and a
consumer validates identity and version rather than trusting a payload. The
failure suite gains the injections that make split brain visible — publisher
crash, duplicate delivery, out-of-order delivery, a cancelled task's late
result, and two concurrent gate transitions.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

10, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md) | `CI pipelines` · `Verification summary schema adapter` · `Test ownership registry` · `Flake policy` |
| [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md) | `Temporal platform` · `Namespace/queue catalog` · `Worker identity policy` · `HA/failover runbook` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md) | `Gate Service` · `GateRecord persistence` · `Verdict rule tests` · `Gate explanation format` |
| [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md) | `G0/G1 workflows` · `Intake/Charter UI API contract` · `ControlPlan generation` · `Gate fixtures` |
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-036 — G5 Execute through G9 Publish Workflows](../04_CONTROL_EVENT/WP-036_g5_g9_workflows.md) | `G5–G9 workflows` · `Review/repro integration contracts` · `Decision update flow` · `Publication transition` |
| [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md) | `ImpactScan workflow` · `Schedule registry` · `ImpactCase service contract` · `Supersession trigger` |
| [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/WP-038_human_updates_compensation.md) | `Human Update API` · `Cancellation contract` · `Compensation registry` · `Decision authentication tests` |
| [WP-039 — Event Consumer, DLQ and Safe Replay Framework](../04_CONTROL_EVENT/WP-039_event_consumer_dlq_replay.md) | `Consumer SDK` · `DLQ service/runbook` · `Replay controller` · `Conformance tests` |

### Full prerequisite closure

**37 of 160 packages (23%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-023` · `WP-025` · `WP-026` |
| 17 | `WP-024` · `WP-028` |
| 18 | `WP-027` |
| 19 | `WP-031` |
| 20 | `WP-032` |
| 21 | `WP-033` · `WP-037` · `WP-039` |
| 22 | `WP-034` · `WP-038` |
| 23 | `WP-035` |
| 24 | `WP-036` |

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-109` · `WP-111` · `WP-116` · `WP-130`
- **Transitively reachable:** **22 of 160 packages (14%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **25** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Independent SRE / Control Plane Reviewer |
| Gates touched | `G0–G10` · `Platform` |
| Controls | `CTL-OPS-01` · `CTL-OPS-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-10 — Primary Model Provider Outage](../12_ACCEPTANCE_SCENARIOS/ACC-10_provider_outage.md) | High | Only an admitted fallback is chosen; route, family and independence are recomputed, SLO and cost records are written, and the task is not duplicated. |
| [ACC-11 — No Eligible Fallback](../12_ACCEPTANCE_SCENARIOS/ACC-11_no_eligible_fallback.md) | Critical | No unsafe route is selected; the task and workflow become `BLOCKED` and a human planning/escalation queue item opens. |
| [ACC-13 — Temporal Worker Crash](../12_ACCEPTANCE_SCENARIOS/ACC-13_temporal_worker_crash.md) | Critical | Workflow history and state are not lost; the activity retries and reconciles, no duplicate effect is produced, and a new worker continues. |
| [ACC-14 — Workflow Code Deployment and Replay](../12_ACCEPTANCE_SCENARIOS/ACC-14_workflow_code_deploy.md) | Critical | Every golden and open history replays deterministically; an incompatible workflow stays on the appropriate worker version and no state drift occurs. |
| [ACC-35 — Tool Partial Failure](../12_ACCEPTANCE_SCENARIOS/ACC-35_tool_partial_failure.md) | Critical | A blind retry does not produce a second side effect; a read and reconcile finds the remote effect, and exactly one `ToolReceipt` is finalized — or the call becomes `RECONCILIATION_REQUIRED`. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md), [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-036 — G5 Execute through G9 Publish Workflows](../04_CONTROL_EVENT/WP-036_g5_g9_workflows.md), [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-038 — Human Update, Cancellation and Compensation Semantics](../04_CONTROL_EVENT/WP-038_human_updates_compensation.md), [WP-039 — Event Consumer, DLQ and Safe Replay Framework](../04_CONTROL_EVENT/WP-039_event_consumer_dlq_replay.md)
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
| `CI pipelines` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Verification summary schema adapter` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Test ownership registry` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Flake policy` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `SPDX/REUSE and OSV admission checks` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Temporal platform` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Namespace/queue catalog` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `Worker identity policy` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `HA/failover runbook` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `SLO dashboard` | `WP-031` | `python3 scripts/progress.py show WP-031` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Gate Service` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `GateRecord persistence` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Verdict rule tests` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Gate explanation format` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `G0/G1 workflows` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Intake/Charter UI API contract` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `ControlPlan generation` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Gate fixtures` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `G5–G9 workflows` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Review/repro integration contracts` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Decision update flow` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Publication transition` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Gate consumption of collaboration and assurance policies` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `ImpactScan workflow` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Schedule registry` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `ImpactCase service contract` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Supersession trigger` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Human Update API` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Cancellation contract` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Compensation registry` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Decision authentication tests` | `WP-038` | `python3 scripts/progress.py show WP-038` |
| `Consumer SDK` | `WP-039` | `python3 scripts/progress.py show WP-039` |
| `DLQ service/runbook` | `WP-039` | `python3 scripts/progress.py show WP-039` |
| `Replay controller` | `WP-039` | `python3 scripts/progress.py show WP-039` |
| `Conformance tests` | `WP-039` | `python3 scripts/progress.py show WP-039` |

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
- **Platform Assurance Lead** carries the acceptance decision; **Independent SRE / Control Plane Reviewer** must verify independently of whoever implements.
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
| WP-040-T01 | Create the golden event histories | Implementation owner | Commit / configuration / record reference |
| WP-040-T02 | Add deterministic replay CI to every workflow build | Implementation owner | Commit / configuration / record reference |
| WP-040-T03 | Write worker-kill and activity-timeout fault injection | Implementation owner | Commit / configuration / record reference |
| WP-040-T04 | Build the database, NATS and provider outage scenarios | Implementation owner | Commit / configuration / record reference |
| WP-040-T05 | Add patch/version-marker and Continue-as-New tests | Implementation owner | Commit / configuration / record reference |
| WP-040-T06 | Produce the state, artifact and integrity comparison report | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Replay test suite`
- `Golden histories`
- `Fault-injection harness`
- `Workflow compatibility report`
- `Split-brain injection suite`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-040_workflow_replay_failure_suite.tests.md`](WP-040_workflow_replay_failure_suite.tests.md).

- Replaying an open history against new code
- A worker crash mid-activity
- `BLOCKED` when a provider times out and no fallback exists
- Recovery from a NATS or database outage
- A partial compensation failure
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-040_workflow_replay_failure_suite.acceptance.md`](WP-040_workflow_replay_failure_suite.acceptance.md), together with what this package still cannot establish.

- [ ] 100% of the critical replay tests pass.
- [ ] Workflow state is preserved at RPO = 0.
- [ ] No failure path produces an unsafe route or a duplicated effect.
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

- Any consumer that can change gate state creates dual authority over the workflow.
- At-least-once delivery means every consumer must be idempotent, without exception.
- A workflow change that breaks open executions is a data incident, not a deploy.

## Rollback / compensation

A worker build that fails replay is not promoted; the previous compatible worker version keeps processing open workflows.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
