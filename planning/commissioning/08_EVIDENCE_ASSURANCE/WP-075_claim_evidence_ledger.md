# WP-075 — Canonical Claim/Evidence Ledger Service

## Package card

| Field | Value |
|---|---|
| Work package | `WP-075` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Data Architect / Assurance Lead |
| Hard dependencies | WP-018, WP-020, WP-025, WP-026, WP-028, WP-030, WP-055, WP-056, WP-061 |
| Related gates | G5–G10 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-04, ACC-08, ACC-30, ACC-31 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Claim, evidence span, dependency, assessment, review link, decision and supersession records are held in an immutable, versioned canonical ledger. This is the system's memory of what it believes and why.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-075-T01 | Migrate the claim, evidence, dependency and assessment tables | Implementation owner | Commit / configuration / record reference |
| WP-075-T02 | Write the version, create, challenge and supersede APIs | Implementation owner | Commit / configuration / record reference |
| WP-075-T03 | Bind optimistic locking, actor, policy and outbox events | Implementation owner | Commit / configuration / record reference |
| WP-075-T04 | Apply field-level and data-class RBAC plus access logging | Implementation owner | Commit / configuration / record reference |
| WP-075-T05 | Add the lineage and impact query APIs | Implementation owner | Commit / configuration / record reference |
| WP-075-T06 | Establish backup, integrity checks and the WORM audit export | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Claim Ledger service`
- `Migrations/API`
- `State transition engine`
- `Lineage queries`
- `Service runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Immutable versioning and supersession
- Denial of an unauthorised claim verification
- A claim → source/run/review/decision query
- Concurrent challenges to the same claim
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Correcting the text of a claim produces a new version.
- [ ] `VERIFIED` is not a permanent or irreversible state.
- [ ] A material claim with a missing link cannot appear in a publication.
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

- Independence asserted in a record but not enforced by the router is decorative.
- A review that sees the producer's conclusion first is anchored, not independent.
- Reproduction that reuses the producer's environment reproduces the environment, not the result.

## Rollback / compensation

A faulty transition is corrected by a superseding event; historical decisions and references remain unchanged.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
