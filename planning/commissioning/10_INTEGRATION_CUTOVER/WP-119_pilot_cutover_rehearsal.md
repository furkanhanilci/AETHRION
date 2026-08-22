# WP-119 — Controlled Pilot and Cutover Rehearsal

## Package card

| Field | Value |
|---|---|
| Work package | `WP-119` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Program Lead |
| Independent verifier | Commissioning Board / Independent Observer |
| Hard dependencies | WP-115, WP-116, WP-117, WP-118 |
| Related gates | Commissioning |
| Related controls | All controls |
| Related acceptance scenarios | ACC-01..ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

A low-risk but realistic pilot and a full end-to-end cutover/abort/rollback rehearsal are completed in a production-equivalent, non-production environment using the same procedure as the real event.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/WP-117_performance_capacity.md), [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operational_readiness.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-119-T01 | Define the pilot selection criteria and apply data minimisation | Implementation owner | Commit / configuration / record reference |
| WP-119-T02 | Run a G0–G10 pilot on production-equivalent RC, configuration and data volume | Implementation owner | Commit / configuration / record reference |
| WP-119-T03 | Measure the operations, decision and assurance SLAs and human usability | Implementation owner | Commit / configuration / record reference |
| WP-119-T04 | Rehearse the cutover runbook: freeze, migration, smoke, abort and rollback | Implementation owner | Commit / configuration / record reference |
| WP-119-T05 | Convert pilot feedback into a correction package | Implementation owner | Commit / configuration / record reference |
| WP-119-T06 | Produce the final rehearsal report and the go/no-go recommendation | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Pilot dossier`
- `Cutover rehearsal log`
- `Usability/ops findings`
- `Rollback proof`
- `Go/no-go recommendation`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A full G0–G10 pilot
- An abort threshold trigger
- Rollback to the prior baseline
- On-call and human decision timing
- An audit export
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The pilot satisfies every invariant.
- [ ] Rollback is proven by evidence from the rehearsal.
- [ ] No open critical or high pilot finding remains.
- [ ] The real cutover procedure is timeboxed and owned.
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

The pilot produces no production side effects; rehearsal state is closed out through environment teardown and archival.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
