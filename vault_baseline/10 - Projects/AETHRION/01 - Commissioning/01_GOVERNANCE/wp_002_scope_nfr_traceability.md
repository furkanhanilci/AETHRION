# WP-002 — Scope, NFRs and Requirement Traceability

## Package card

| Field | Value |
|---|---|
| Work package | `WP-002` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Assurance Lead |
| Hard dependencies | WP-001 |
| Related gates | Program |
| Related controls | CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Functional scope and the durability, traceability, isolation, idempotency, audit, privacy, cost and accessibility NFRs are converted into testable requirements. A requirement that cannot be tested is a preference, and is recorded as one.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/wp_001_commissioning_charter.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-002-T01 | Extract the functional capability list with `REQ` identifiers | Implementation owner | Commit / configuration / record reference |
| WP-002-T02 | Assign a target, a measurement method and a test owner to every NFR | Implementation owner | Commit / configuration / record reference |
| WP-002-T03 | Separate out the areas that need a domain-specific profile from the generic core | Implementation owner | Commit / configuration / record reference |
| WP-002-T04 | Define the REQ → WP → TST/ACC traceability schema | Implementation owner | Commit / configuration / record reference |
| WP-002-T05 | Record the out-of-scope items and the rules for handling future requests | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Requirement Registry`
- `NFR scorecard`
- `Traceability matrix seed`
- `Scope boundary record`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An existence test proving every `REQ` carries measurable acceptance
- Owner review of every out-of-scope item
- An NFR contradiction and feasibility walkthrough
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] 100% of material requirements carry an owner and a test.
- [ ] No unquantified 'fast / secure / scalable' phrasing remains.
- [ ] Domain profiles are separated from the generic core.
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

Requirements that cannot be traced return to draft status; no downstream package may be marked `READY` against them.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
