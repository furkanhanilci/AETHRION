# WP-114 — Operations, DR and Restore Acceptance Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-114` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Independent DR Witness / Internal Audit |
| Hard dependencies | WP-025, WP-026, WP-028, WP-030, WP-031, WP-052, WP-099, WP-101, WP-109 |
| Related gates | Commissioning |
| Related controls | CTL-OPS-02, CTL-OPS-03 |
| Related acceptance scenarios | ACC-21, ACC-27, ACC-28, ACC-40 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Regional and control-plane loss, registry, object, event, graph and Zotero restore and audit integrity meet the RPO/RTO targets across at least two independent drills.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-114-T01 | Plan DR-1 component restore and DR-2 regional/management-plane restore | Implementation owner | Commit / configuration / record reference |
| WP-114-T02 | Restore PostgreSQL PITR, objects, NATS, Temporal, registries, audit and projections | Implementation owner | Commit / configuration / record reference |
| WP-114-T03 | Perform a Zotero full resync and a graph and vault rebuild | Implementation owner | Commit / configuration / record reference |
| WP-114-T04 | Run the workflow, run, claim, source and artifact integrity queries | Implementation owner | Commit / configuration / record reference |
| WP-114-T05 | Measure the on-call, incident, communication and decision timeline | Implementation owner | Commit / configuration / record reference |
| WP-114-T06 | Produce the DR dossier, its gaps and the sign-off | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Two DR drill reports`
- `Restore manifests`
- `Integrity query results`
- `RPO/RTO scorecard`
- `DR sign-off`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- ACC-21, 27, 28 and 40
- Temporal open-workflow continuity
- Object and audit hash integrity
- Projection rebuild
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Both restore drills PASS.
- [ ] Workflow state holds at RPO = 0 within the approved RTO.
- [ ] Canonical and derived integrity queries PASS.
- [ ] No open critical DR gap remains.
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

A DR failure blocks cutover; the restore environment stays quarantined and the production baseline is not modified.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
