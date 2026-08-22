# WP-100 — Cost Ledger, Budget Envelopes and FinOps

## Package card

| Field | Value |
|---|---|
| Work package | `WP-100` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | FinOps Lead |
| Independent verifier | Project Decision Owner / Internal Audit |
| Hard dependencies | WP-011, WP-013, WP-015, WP-016, WP-025, WP-028, WP-041, WP-045, WP-049, WP-052, WP-053, WP-082, WP-096 |
| Related gates | G0,G4,G5,G8 |
| Related controls | CTL-CST-01, CTL-CST-02 |
| Related acceptance scenarios | ACC-09, ACC-29 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Model, compute, retrieval, storage, verification and human triage costs are attributed to project, workflow, run, role, profile and outcome, with an 80% warning and a 100% hard stop.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-100-T01 | Establish the `BudgetEnvelope`, C0–C4 classes and the reservation API | Implementation owner | Commit / configuration / record reference |
| WP-100-T02 | Ingest gateway, Kueue, tool, storage and human cost events | Implementation owner | Commit / configuration / record reference |
| WP-100-T03 | Write estimate → reserve → commit → release plus retry and fan-out attribution | Implementation owner | Commit / configuration / record reference |
| WP-100-T04 | Integrate the 80% and 100% thresholds with Temporal pause and decision flows | Implementation owner | Commit / configuration / record reference |
| WP-100-T05 | Add provider invoice reconciliation and variance cases | Implementation owner | Commit / configuration / record reference |
| WP-100-T06 | Build the quality-adjusted cost/outcome dashboard and forecast | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Cost Ledger`
- `Budget service`
- `Cost adapters`
- `Invoice reconciliation`
- `FinOps dashboard/runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- The 80% warning
- Denial of new expensive work at 100%
- Release of a cancelled reservation
- Idempotency against duplicate cost events
- An invoice variance case
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Exceeding a hard budget never loses state.
- [ ] Cost is not measured in tokens alone.
- [ ] Critical assurance capacity is visible inside the budget policy.
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

The effect of a faulty cost adapter is corrected through reconciliation; a hard stop is never disabled manually — it requires an owner `DecisionRecord`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
