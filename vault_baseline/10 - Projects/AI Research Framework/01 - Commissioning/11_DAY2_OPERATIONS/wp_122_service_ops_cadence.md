# WP-122 — Service Health, SLO and Error-Budget Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-122` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Service Owners / Internal Audit |
| Hard dependencies | WP-101, WP-121 |
| Related gates | Day-2 |
| Related controls | CTL-OBS-01, CTL-OPS-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Daily and weekly service health, SLO, dependency, capacity, alert quality and error-budget reviews become a permanent operating rhythm rather than an occasional exercise.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-122-T01 | Establish the daily health and weekly SLO review agenda | Implementation owner | Commit / configuration / record reference |
| WP-122-T02 | Apply the error-budget breach release freeze | Implementation owner | Commit / configuration / record reference |
| WP-122-T03 | Check ownership and runbook freshness | Implementation owner | Commit / configuration / record reference |
| WP-122-T04 | Track dependency risk and the toil backlog | Implementation owner | Commit / configuration / record reference |
| WP-122-T05 | Produce the monthly availability, correctness and freshness report | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Ops cadence calendar`
- `SLO review template`
- `Error-budget decisions`
- `Toil backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A synthetic alert review
- An error-budget-driven release block
- A scan for orphaned owners and runbooks
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every critical SLO breach carries a named action and owner.
- [ ] The error budget is not quietly ignored.
- [ ] Vanity uptime never substitutes for correctness.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

If the rhythm lapses it escalates through governance; the control is never permanently switched off.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
