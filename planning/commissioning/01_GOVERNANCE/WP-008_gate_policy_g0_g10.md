# WP-008 — G0–G10 Gate and Assurance Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-008` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Safety Owner |
| Hard dependencies | WP-004, WP-005, WP-007 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-EPI-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Each gate's invariant purpose, entry and exit artifacts, hard blockers, risk-based depth, reopen behaviour and escalation path are closed out in a single policy baseline.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-008-T01 | Write the entry/exit conditions and `GateRecord` fields for G0–G10 | Implementation owner | Commit / configuration / record reference |
| WP-008-T02 | Bind the R1/R2/R3 assurance overlays to each gate | Implementation owner | Commit / configuration / record reference |
| WP-008-T03 | Define the rule that gates may close in one session but must still produce separate records | Implementation owner | Commit / configuration / record reference |
| WP-008-T04 | Write the reopen rules for protocol, literature, run, review and reproduction changes | Implementation owner | Commit / configuration / record reference |
| WP-008-T05 | Map the non-waivable blockers and the residual-risk acceptance boundary | Implementation owner | Commit / configuration / record reference |
| WP-008-T06 | Define G10 supersession and impact behaviour | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Gate Policy v1`
- `Gate artifact matrix`
- `Reopen/return transition table`
- `Gate owner matrix`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A happy-path state walkthrough
- At least one hard-fail test per gate
- A test of risk-based depth and of separate `GateRecord` emission
- A G7 fail → `CHALLENGED` return-path test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] All eleven gates have an owner, entry/exit artifacts, acceptance criteria and blockers.
- [ ] A low risk class reduces depth but never removes a gate.
- [ ] A critical blocker cannot be passed by human override.
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

- A policy that is written but not machine-checkable is an intention, not a control.
- Role and authority documents drift silently; every change here needs a baseline bump.
- The hardest failure in this workstream is a rule that everyone agrees with and nobody can enforce.

## Rollback / compensation

A new gate policy is never applied directly to open workflows; it is promoted through an impact scan and a versioned transition.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
