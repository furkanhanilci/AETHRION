# WP-038 — Human Update, Cancellation and Compensation Semantics

## Package card

| Field | Value |
|---|---|
| Work package | `WP-038` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Control Plane Lead |
| Independent verifier | Governance Lead / Tool Platform Lead |
| Hard dependencies | WP-004, WP-013, WP-016, WP-032, WP-033 |
| Related gates | G1,G8,G9 |
| Related controls | CTL-GOV-03, CTL-OPS-01 |
| Related acceptance scenarios | ACC-25, ACC-26, ACC-35 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-038_human_updates_compensation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-038_human_updates_compensation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Human decisions are processed through an authenticated Temporal Update, and cancellation with external side effects is handled through an explicit compensation plan.


## Analysis
### What this package actually decides

Two things that look unrelated and are the same problem: how a human's decision
enters the system, and how work is undone when it should not have started. Both
are about **external effects that cannot be replayed away**.

### The Update must be authenticated *and* idempotent (T01)

A decision is a durable authorisation. If it can be replayed, a retry approves
twice; if it can be forged, the authorisation means nothing. Both properties are
required and neither is the default.

### The evidence snapshot check is what stops a stale approval (T02)

WP-004 requires an approval to be bound to the evidence it was taken against. Here
it becomes an enforcement point: the Update carries the snapshot digest, and if
the current evidence differs, the decision is **refused** rather than applied to
the new state. Without this, an approval granted under one set of facts silently
authorises another.

### Compensation is not rollback (T04)

A database transaction rolls back. A tool that posted to an external system, a
sandbox that consumed budget, a lease that granted access — none of those roll
back, and pretending they do is how cancellation becomes a lie.

The compensation registry names, per effect, what undoing it actually means:
revoke the lease, stop the sandbox, post the reversing action, or **record that it
cannot be undone**. That last outcome is legitimate and must be representable —
`00_PROGRAM/09` already accepts it for immutable artifacts.

### `INVALIDATED` rather than delete (T05)

An artifact produced by cancelled work is not removed; it is marked. WP-014 fixed
the semantics and this is the workflow that applies them. Deleting would break the
lineage of anything that already referenced it, which is the failure the immutable
store exists to prevent.

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

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md) | `Decision policy` · `SLA/escalation table` · `Delegation matrix` · `Decision rationale rubric` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md) | `Gate Service` · `GateRecord persistence` · `Verdict rule tests` · `Gate explanation format` |

### Full prerequisite closure

**31 of 160 packages (19%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` |

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-040` · `WP-093` · `WP-156`
- **Transitively reachable:** **30 of 160 packages (19%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **22** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Control Plane Lead |
| Independent verifier | Governance Lead / Tool Platform Lead |
| Gates touched | `G1` · `G8` · `G9` |
| Controls | `CTL-GOV-03` · `CTL-OPS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-25 — Human Approval Forgery](../12_ACCEPTANCE_SCENARIOS/ACC-25_human_approval_forgery.md) | Critical | The decision is rejected; gate state does not change and a security event and audit record are produced. A valid owner with MFA and an idempotent request passes as the counter-example. |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/ACC-26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |
| [ACC-35 — Tool Partial Failure](../12_ACCEPTANCE_SCENARIOS/ACC-35_tool_partial_failure.md) | Critical | A blind retry does not produce a second side effect; a read and reconcile finds the remote effect, and exactly one `ToolReceipt` is finalized — or the call becomes `RECONCILIATION_REQUIRED`. |
| [ACC-68 — Human Intervention Without an Audit Record](../12_ACCEPTANCE_SCENARIOS/ACC-68_human_intervention_audit.md) | Critical | The edit fails and rolls back. There is no path by which a human action changes canonical state without an atomically written `HumanInterventionRecord` carrying before and after references. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md)
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
| `Decision policy` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `SLA/escalation table` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Delegation matrix` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Decision rationale rubric` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Human intervention vocabulary` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Timeout escalation path with no approval branch` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Gate Service` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `GateRecord persistence` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Verdict rule tests` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Gate explanation format` | `WP-033` | `python3 scripts/progress.py show WP-033` |

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
- **Control Plane Lead** carries the acceptance decision; **Governance Lead / Tool Platform Lead** must verify independently of whoever implements.
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
| WP-038-T01 | Write the decision-update authentication and idempotency logic | Implementation owner | Commit / configuration / record reference |
| WP-038-T02 | Verify the evidence snapshot and the actor context | Implementation owner | Commit / configuration / record reference |
| WP-038-T03 | Define the cancellation scope and its child/activity propagation | Implementation owner | Commit / configuration / record reference |
| WP-038-T04 | Bind lease revocation, sandbox stop and tool compensation steps | Implementation owner | Commit / configuration / record reference |
| WP-038-T05 | Apply `INVALIDATED` behaviour for immutable artifacts | Implementation owner | Commit / configuration / record reference |
| WP-038-T06 | Set up the timeout and escalation timers | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Human Update API`
- `Cancellation contract`
- `Compensation registry`
- `Decision authentication tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-038_human_updates_compensation.tests.md`](WP-038_human_updates_compensation.tests.md).

- Duplicate approvals resolving to one decision
- Denial of a forged or expired actor
- Compensation triggered by a mid-tool timeout
- Artifact retention after a cancellation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-038_human_updates_compensation.acceptance.md`](WP-038_human_updates_compensation.acceptance.md), together with what this package still cannot establish.

- [ ] A signal with a free-form payload cannot pass a gate.
- [ ] Cancellation never deletes canonical evidence.
- [ ] A failed compensation opens a reconciliation case or an incident.
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

An update-service rollback preserves workflow version compatibility; an erroneous human decision is revoked and superseded rather than edited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
