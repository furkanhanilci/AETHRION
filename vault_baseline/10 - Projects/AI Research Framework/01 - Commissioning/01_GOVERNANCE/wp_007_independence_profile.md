# WP-007 — IndependenceProfile and Separation-of-Duties Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-007` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Internal Audit / Safety Owner |
| Hard dependencies | WP-003, WP-005 |
| Related gates | G6,G7,G8 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | ACC-06, ACC-38 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The separation of producer, reviewer and reproducer becomes auditable across seven dimensions: human, model family, context, credential, environment, data path and economic interest.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-007-T01 | Define the seven independence dimensions | Implementation owner | Commit / configuration / record reference |
| WP-007-T02 | Write the minimum required sets for R1, R2 and R3 | Implementation owner | Commit / configuration / record reference |
| WP-007-T03 | Identify the non-compensable dimensions and their blocker rules | Implementation owner | Commit / configuration / record reference |
| WP-007-T04 | Define the frozen-package and context-contamination controls | Implementation owner | Commit / configuration / record reference |
| WP-007-T05 | Design re-evaluation at assignment time and again at gate time | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `IndependenceProfile rubric`
- `Eligibility matrix`
- `Conflict-of-interest declaration`
- `Violation response`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A negative test for planner self-review
- A same-model-family and context-contamination test
- A fail-closed test for the reviewer-unavailable case
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] There is no single averaged independence score.
- [ ] If human separation cannot be achieved for R3, the workflow becomes `BLOCKED`.
- [ ] A reviewer sees only the frozen package and the context it is permitted to see.
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

Review and reproduction records produced under a violated profile are marked `INVALIDATED` and a fresh independent assignment is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
