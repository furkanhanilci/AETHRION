# WP-001 — Commissioning Charter and Programme Authority

## Package card

| Field | Value |
|---|---|
| Work package | `WP-001` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Executive Sponsor |
| Independent verifier | Internal Audit / Commissioning Board |
| Hard dependencies | — |
| Related gates | Program |
| Related controls | CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The programme's purpose, its production boundary, its funding authority, its decision bodies and the single-cutover rule are brought into force through a signed charter. Until this charter exists, no other package has the standing to bind anyone.

## Out of scope

- Technology selection
- The detailed delivery calendar
- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- No hard dependency — this package can start as soon as the programme is authorised.
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-001-T01 | Write the business outcome, the scope and the explicit out-of-scope boundary | Implementation owner | Commit / configuration / record reference |
| WP-001-T02 | Assign the authorities of the Executive Sponsor, Programme Lead, Chief Architect, Assurance and Safety | Implementation owner | Commit / configuration / record reference |
| WP-001-T03 | Define who holds production cutover authority and who holds abort authority | Implementation owner | Commit / configuration / record reference |
| WP-001-T04 | Record the initial budget envelope together with procurement limits | Implementation owner | Commit / configuration / record reference |
| WP-001-T05 | Obtain approval of the success KPIs, the anti-metrics and the stop/pivot conditions | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `CommissioningCharter`
- `Program authority matrix`
- `Initial budget envelope`
- `Executive DecisionRecord`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Charter schema and mandatory-field validation
- An authority-collision tabletop exercise
- A cutover/abort decision walkthrough
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every accountable role is filled by a **named person**, not a job title.
- [ ] The single-cutover rule and the zero-critical-finding condition are stated explicitly.
- [ ] Budget, scope and stop/pivot authorities are signed.
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

If the charter is not accepted, no platform procurement and no production commitment is opened; the draft is archived with the reason for rejection recorded.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
