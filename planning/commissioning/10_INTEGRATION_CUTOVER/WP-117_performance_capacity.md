# WP-117 — Performance, Capacity and Load Commissioning

## Package card

| Field | Value |
|---|---|
| Work package | `WP-117` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Capacity Engineering Lead |
| Independent verifier | SRE / FinOps / Assurance |
| Hard dependencies | WP-053, WP-096, WP-098, WP-100, WP-101, WP-115 |
| Related gates | Commissioning |
| Related controls | CTL-CST-01, CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Under the approved workload envelope, the intake/gate, event, model, broker, registry, experiment, review and impact queues meet their SLO, quota and cost limits.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-098 — Grafana and the Six Operational Graphs](../09_EXPERIENCE_OBSERVABILITY/WP-098_grafana_six_graphs.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-117-T01 | Define the workload mix, concurrency, data size and fan-out envelope | Implementation owner | Commit / configuration / record reference |
| WP-117-T02 | Write the service, queue and end-to-end load tests | Implementation owner | Commit / configuration / record reference |
| WP-117-T03 | Measure bottlenecks across the database, NATS, Temporal, models, tools and sandboxes | Implementation owner | Commit / configuration / record reference |
| WP-117-T04 | Tune autoscaling, connection pools, caches and backpressure | Implementation owner | Commit / configuration / record reference |
| WP-117-T05 | Model the assurance queue and the human SLA capacity | Implementation owner | Commit / configuration / record reference |
| WP-117-T06 | Produce the cost curve, headroom and capacity plan | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Load test suite/results`
- `Capacity model`
- `Bottleneck/tuning report`
- `Cost/headroom forecast`
- `Capacity sign-off`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Nominal, peak, burst and soak profiles
- Backpressure that does not become data loss
- The review queue capacity reserve
- Budget fan-out caps
- Large manifest and event-reference handling
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] SLOs are met within the approved envelope.
- [ ] At least 20% headroom exists, or a named scale trigger is defined.
- [ ] Backpressure never produces an unsafe bypass.
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

If capacity fails, the date or the infrastructure size is corrected — not the production scope; the RC's READY status is withdrawn.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
