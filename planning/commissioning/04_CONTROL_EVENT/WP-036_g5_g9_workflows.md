# WP-036 — G5 Execute through G9 Publish Workflows

## Package card

| Field | Value |
|---|---|
| Work package | `WP-036` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Workflow Engineering Lead |
| Independent verifier | Assurance Lead / Decision Owner |
| Hard dependencies | WP-004, WP-007, WP-008, WP-019, WP-032, WP-033, WP-035 |
| Related gates | G5–G9 |
| Related controls | CTL-GOV-02, CTL-EPI-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-08, ACC-19, ACC-20, ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Execution, claim freeze, blind review, reproduction, human decision and publication gates operate over a canonical artifact and decision chain.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-036-T01 | Write the G5 `RunBatch` dispatch, checkpoint and stop flow | Implementation owner | Commit / configuration / record reference |
| WP-036-T02 | Bind the G6 frozen review package and its dispositions | Implementation owner | Commit / configuration / record reference |
| WP-036-T03 | Establish the G7 reproduction request, result and reopen flow | Implementation owner | Commit / configuration / record reference |
| WP-036-T04 | Apply the G8 evidence-delta human decision update | Implementation owner | Commit / configuration / record reference |
| WP-036-T05 | Bind the G9 citation, provenance and security release checklist | Implementation owner | Commit / configuration / record reference |
| WP-036-T06 | Add cancellation, compensation and supersession | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `G5–G9 workflows`
- `Review/repro integration contracts`
- `Decision update flow`
- `Publication transition`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Recovery from a partial execution failure
- `BLOCKED` on an unresolved critical review finding
- A G7 tolerance failure returning to `CHALLENGED`
- Negative tests for invalid approval and incomplete publication lineage
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A producer cannot issue its own acceptance.
- [ ] G9 fails when claim lineage is incomplete.
- [ ] A G7 failure produces a controlled return, never a deletion of history.
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

A pre-release fault pauses the workflow at the last safe gate; external draft side effects are compensated explicitly.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
