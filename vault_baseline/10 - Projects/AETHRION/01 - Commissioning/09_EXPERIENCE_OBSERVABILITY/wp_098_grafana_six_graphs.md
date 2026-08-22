# WP-098 — Grafana and the Six Operational Graphs

## Package card

| Field | Value |
|---|---|
| Work package | `WP-098` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Observability Lead |
| Independent verifier | Service Owners / FinOps / Assurance |
| Hard dependencies | WP-030, WP-096, WP-097 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-OBS-01, CTL-OBS-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Correlated dashboards and alerts are built for the execution, workflow, experiment, knowledge/evidence, service/SLO and cost graphs.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md), [WP-097 — Langfuse Model/Agent Tracing and Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/wp_097_langfuse_llm_trace.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-098-T01 | Establish the metric, log and trace stores and Grafana RBAC | Implementation owner | Commit / configuration / record reference |
| WP-098-T02 | Write the workflow, gate latency and blocker dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T03 | Write the execution queue, sandbox and tool dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T04 | Write the experiment, reproduction and evaluation quality dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T05 | Write the literature, claim and impact integrity dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T06 | Write the service/SLO/incident and cost/budget dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T07 | Add alert routing, owners and runbook links | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Grafana platform`
- `Six graph dashboards`
- `Alert rules`
- `Dashboard/alert ownership catalog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A synthetic SLO breach alert
- Budget 80% and 100% events
- Projection lag
- G6/G7 backlog growth
- A security deny or egress event
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every alert carries a named owner and a runbook.
- [ ] Dashboards support decisions and actions rather than vanity metrics.
- [ ] Sensitive labels and logs are redacted.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A faulty alert or dashboard configuration is rolled back through GitOps; alert suppression is time-bound, owned and audited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
