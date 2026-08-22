# WP-127 — FinOps, Capacity and Portfolio Review Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-127` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | FinOps Lead / Research Director |
| Independent verifier | Internal Audit / Assurance |
| Hard dependencies | WP-100, WP-117, WP-121 |
| Related gates | G0,G4,G8,Day-2 |
| Related controls | CTL-CST-01, CTL-CST-02 |
| Related acceptance scenarios | — a Day-2 rhythm is exercised in operation, not as a go-live gate |
| Recurring counterpart of | ACC-09, ACC-29 — those scenarios verify the **initial** qualification before cutover; this package owns the **recurring** one afterwards |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Monthly invoice reconciliation, forecasting, quality-adjusted cost versus outcome, queue capacity, model mix and stop/pivot portfolio decisions become permanent practice.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/WP-117_performance_capacity.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-127-T01 | Run the invoice, provider, compute and storage reconciliation | Implementation owner | Commit / configuration / record reference |
| WP-127-T02 | Produce the project and outcome budget variance and forecast | Implementation owner | Commit / configuration / record reference |
| WP-127-T03 | Analyse model/agent fan-out and the expected value of verification | Implementation owner | Commit / configuration / record reference |
| WP-127-T04 | Update the capacity, headroom and queue-wait plan | Implementation owner | Commit / configuration / record reference |
| WP-127-T05 | Record the stop/pivot decision for low-value, high-cost projects | Implementation owner | Commit / configuration / record reference |
| WP-127-T06 | Trigger the annual cost policy benchmark and reopen | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Monthly FinOps report`
- `Invoice cases`
- `Portfolio decision records`
- `Capacity forecast`
- `Optimization backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An invoice variance sample
- A hard budget event audit
- Cost allocation completeness
- A quality-adjusted route comparison
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Cost is never optimised on token price alone.
- [ ] The human cost of assurance is visible in the report.
- [ ] Every budget override carries a named decision and an expiry.
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

A wrong allocation is fixed through a reconciliation adjustment; historical invoices and ledger events are never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
