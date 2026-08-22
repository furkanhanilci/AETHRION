# WP-121 — Hypercare, Stabilisation and Programme Closure

## Package card

| Field | Value |
|---|---|
| Work package | `WP-121` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead / Program Lead |
| Independent verifier | Executive Sponsor / Assurance |
| Hard dependencies | WP-120 |
| Related gates | Cutover,Day-2 |
| Related controls | All controls |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

After go-live, intensive observation, fast incident and reconciliation handling, SLO/cost/quality measurement and explicit exit criteria hand the system over to normal Day-2 operations.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-120 — Production Cutover and Go-Live Decision](../10_INTEGRATION_CUTOVER/wp_120_production_cutover.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-121-T01 | Establish the hypercare command centre, rota and decision cadence | Implementation owner | Commit / configuration / record reference |
| WP-121-T02 | Monitor the critical journeys, synthetic tests, queues, cost, security and evidence dashboards | Implementation owner | Commit / configuration / record reference |
| WP-121-T03 | Operate incident, finding, change-freeze and rollback authority | Implementation owner | Commit / configuration / record reference |
| WP-121-T04 | Run user support, feedback and knowledge capture | Implementation owner | Commit / configuration / record reference |
| WP-121-T05 | Verify the SLO, error budget and quality KPI baseline | Implementation owner | Commit / configuration / record reference |
| WP-121-T06 | Sign the exit review and the Day-2 owner handoff | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Hypercare log`
- `Incident/finding summary`
- `Production KPI baseline`
- `Day-2 handoff`
- `Program closure report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A synthetic G0 → decision journey
- Zotero sync, impact and queue health
- A budget and invoice sample
- An audit export sample
- On-call response
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Open critical incidents at hypercare exit = 0.
- [ ] The SLO and evidence integrity targets are met.
- [ ] Day-2 owners, runbooks and operating rhythms are active.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

On critical instability the cutover rollback authority is used; operation does not continue by bypassing part of the feature set.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
