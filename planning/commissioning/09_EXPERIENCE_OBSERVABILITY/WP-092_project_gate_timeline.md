# WP-092 — Project Workspace and G0–G10 Gate Timeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-092` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experience Lead |
| Independent verifier | Research Operations / Assurance |
| Hard dependencies | WP-008, WP-032, WP-033, WP-034, WP-035, WP-036, WP-037, WP-091 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-OPS-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Every project gains a working surface that explains its current gate, frozen versions, blockers, budget, owner, residual risk, reopen history and next action.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md), [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-036 — G5 Execute through G9 Publish Workflows](../04_CONTROL_EVENT/WP-036_g5_g9_workflows.md), [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-092-T01 | Write the project overview, charter and control profile views | Implementation owner | Commit / configuration / record reference |
| WP-092-T02 | Display the G0–G10 timeline and `GateRecord` diffs | Implementation owner | Commit / configuration / record reference |
| WP-092-T03 | Bind the artifact, manifest, review, reproduction and decision panels | Implementation owner | Commit / configuration / record reference |
| WP-092-T04 | Design the `BLOCKED` / `REVISE` / `DISAGREEMENT` explanation surface | Implementation owner | Commit / configuration / record reference |
| WP-092-T05 | Add reopen, supersession and history comparison | Implementation owner | Commit / configuration / record reference |
| WP-092-T06 | Bind the authorised command and update forms to the Temporal API | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Project Workspace`
- `Gate Timeline`
- `Artifact/evidence panels`
- `Command/update forms`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Visualisation of a G7 failure as a controlled return
- Risk depth shown alongside separate `GateRecord`s
- Denial of an unauthorised transition
- Projection lag versus a live canonical query
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A user can see **why** they are blocked, with the rule and the evidence.
- [ ] There is no free-form state mutation from the UI.
- [ ] Older versions and decision history remain reachable.
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

A frontend rollback loses no state; a faulty command is rejected server-side by policy regardless of client version.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
