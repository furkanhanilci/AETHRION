# WP-003 — Role Catalogue and RACI Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-003` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Governance Lead |
| Independent verifier | Internal Audit |
| Hard dependencies | WP-001, WP-002 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-GOV-02 |
| Related acceptance scenarios | ACC-06, ACC-38 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The mandate, decision rights, forbidden actions, required artifacts and escalation boundaries of every human, service and model actor are fixed in a single catalogue.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/WP-001_commissioning_charter.md), [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-003-T01 | Map the 36 core roles onto durable functions and duty cells | Implementation owner | Commit / configuration / record reference |
| WP-003-T02 | Write the mandate, the input/output contract and the forbidden actions for each role | Implementation owner | Commit / configuration / record reference |
| WP-003-T03 | Establish the RACI for G0–G10 and for platform release decisions | Implementation owner | Commit / configuration / record reference |
| WP-003-T04 | Define the role-combination rules that apply to a small team | Implementation owner | Commit / configuration / record reference |
| WP-003-T05 | Define `RoleContract` versioning and the assignment lifecycle | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Role Catalog`
- `RACI matrix`
- `Role-combination policy`
- `Role assignment workflow`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A sweep for decisions with no accountable role
- A negative test for self-approval on the same artifact
- A small-team R1/R3 tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every material decision has exactly one accountable (A) role.
- [ ] A producer cannot review, reproduce or accept its own output.
- [ ] No permitted role combination violates the independence policy.
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

Conflicting assignments are cancelled and the last signed role baseline is restored.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
