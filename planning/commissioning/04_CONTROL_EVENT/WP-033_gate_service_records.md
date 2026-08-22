# WP-033 — Gate Service and GateRecord Evaluation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-033` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Control Plane Lead |
| Independent verifier | Assurance Lead |
| Hard dependencies | WP-008, WP-016, WP-018, WP-032 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-EPI-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

A service deterministically evaluates gate artifact, policy, review, budget and blocker inputs and writes a `PASS` / `REVISE` / `REJECT` / `BLOCKED` / `DISAGREEMENT` outcome into the Temporal history.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-033-T01 | Write the gate evaluation input adapters | Implementation owner | Commit / configuration / record reference |
| WP-033-T02 | Apply hard and soft checks with an explicit verdict precedence | Implementation owner | Commit / configuration / record reference |
| WP-033-T03 | Emit separate records for gates that close within the same session | Implementation owner | Commit / configuration / record reference |
| WP-033-T04 | Produce a gate explanation and the list of failed checks | Implementation owner | Commit / configuration / record reference |
| WP-033-T05 | Bind reopen, supersession and the evidence snapshot | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Gate Service`
- `GateRecord persistence`
- `Verdict rule tests`
- `Gate explanation format`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A hard-fail fixture for every gate
- A test proving risk depth still yields separate records
- Fail-closed behaviour on `UNKNOWN` policy or budget input
- Rejection of a stale input snapshot
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A gate outcome is not valid until it is written to the Temporal event history.
- [ ] A verdict carrying a critical blocker can never be `PASS`.
- [ ] Identical inputs and policy produce an identical verdict.
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

A faulty gate evaluation is corrected by a superseding record; the workflow is paused at its last safe state.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
