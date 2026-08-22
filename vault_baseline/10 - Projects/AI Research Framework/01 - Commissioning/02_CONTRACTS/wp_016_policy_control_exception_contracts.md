# WP-016 — PolicyDecision, Control and Exception Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-016` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Policy Platform Lead |
| Independent verifier | Internal Audit |
| Hard dependencies | WP-006, WP-009, WP-011 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-GOV-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Every authorisation, routing and gate decision becomes an auditable record carrying its inputs, bundle version, rule ID, explanation and any linked exception.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-016-T01 | Write the `PolicyDecision` allow/deny/obligations fields | Implementation owner | Commit / configuration / record reference |
| WP-016-T02 | Add the `ControlRecord` owner, evidence and frequency fields | Implementation owner | Commit / configuration / record reference |
| WP-016-T03 | Define the `ExceptionRecord` scope, approver and expiry schema | Implementation owner | Commit / configuration / record reference |
| WP-016-T04 | Fix the format of the policy explanation and the input hash | Implementation owner | Commit / configuration / record reference |
| WP-016-T05 | Define the re-evaluation triggers | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `PolicyDecision schema`
- `ControlRecord schema`
- `ExceptionRecord schema`
- `Example decision fixtures`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A negative test for a missing bundle digest or rule ID
- Validation of expired exceptions
- An input-hash determinism test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every decision carries an explainable rule ID and a bundle digest.
- [ ] An exception cannot be used outside its declared scope.
- [ ] An `UNKNOWN` policy result never resolves to allow.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

A policy record is never edited; a superseding decision is written and the affected tasks are re-evaluated.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
