# WP-004 — Human Decision, SLA, Delegation and Escalation Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-004` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Project Decision Owner |
| Independent verifier | Safety & Governance Owner |
| Hard dependencies | WP-003 |
| Related gates | G1,G8,G9 |
| Related controls | CTL-GOV-01, CTL-GOV-03 |
| Related acceptance scenarios | ACC-25, ACC-26 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Every decision type in the Human Decision Queue receives an SLA, an evidence summary, a delegation boundary, an expiry and an explicit fail-closed behaviour. Human decision capacity is the scarcest resource in the system, and this package is where it is budgeted.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-004-T01 | Classify decision types as material or non-material | Implementation owner | Commit / configuration / record reference |
| WP-004-T02 | Assign an SLA and an escalation chain to each decision | Implementation owner | Commit / configuration / record reference |
| WP-004-T03 | Write the scope, duration and role rules for a `DelegationRecord` | Implementation owner | Commit / configuration / record reference |
| WP-004-T04 | Lock the non-delegable G8, publication, retraction and cutover decisions | Implementation owner | Commit / configuration / record reference |
| WP-004-T05 | Define approval expiry, revocation and evidence-delta behaviour | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Decision policy`
- `SLA/escalation table`
- `Delegation matrix`
- `Decision rationale rubric`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A test proving an SLA timeout never produces an automatic approval
- A negative test with forged and expired delegations
- An attempt to delegate a non-delegable decision
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A timeout produces only `BLOCKED` or an escalation — never an approval.
- [ ] Every material decision carries a named owner and a written rationale.
- [ ] Out-of-scope use of a delegation is rejected by policy, not by convention.
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

A faulty delegation is revoked and every open decision it touched is returned to the re-evaluation queue.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
