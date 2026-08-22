# WP-061 — Canonical Source Registry Service

## Package card

| Field | Value |
|---|---|
| Work package | `WP-061` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Data Architect / Citation Auditor |
| Hard dependencies | WP-012, WP-017, WP-020, WP-025, WP-026, WP-028, WP-055, WP-056 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01, CTL-OPS-01 |
| Related acceptance scenarios | ACC-03, ACC-28 |
| Current status | `NOT_STARTED` |

## Adopted component

> **GROBID** + **Pub2TEI** — one canonical TEI representation

PDFs go through GROBID, publisher XML through Pub2TEI, into the same TEI. An `EvidenceSpan` then addresses `tei_xpath` with a `representation_digest`, and a later parser produces `representation-v2` without invalidating claims anchored to v1.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Purpose and expected outcome

The canonical PostgreSQL service for bibliographic identity, representations, trust, status, project membership and Zotero bindings is established. This is where a source acquires the identity everything else cites.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-061-T01 | Migrate the `SourceRecord`, representation, trust and binding tables | Implementation owner | Commit / configuration / record reference |
| WP-061-T02 | Write the create, read, version, merge and tombstone APIs | Implementation owner | Commit / configuration / record reference |
| WP-061-T03 | Bind optimistic concurrency and outbox event emission | Implementation owner | Commit / configuration / record reference |
| WP-061-T04 | Apply field authority and data-class RBAC | Implementation owner | Commit / configuration / record reference |
| WP-061-T05 | Add search, filter, history and bulk ingest APIs | Implementation owner | Commit / configuration / record reference |
| WP-061-T06 | Establish backups, SLOs and the audit queries | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Source Registry service`
- `Database migrations`
- `API/OpenAPI`
- `Outbox events`
- `Service runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A concurrent update producing a 409 or a merge case
- An unauthorised field write
- Source history traversal
- Database failure and retry idempotency
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The Source Registry owns canonical identity and status.
- [ ] No Zotero key or DOI is ever the primary key on its own.
- [ ] Every mutation carries a version and an actor.
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

- Identity errors in sources propagate into every claim that cites them.
- A write into a shared library without a version precondition can silently destroy a human edit.
- A literature set that is not frozen cannot support a reproducible claim.

## Rollback / compensation

A faulty migration is corrected through expand-contract; a wrong merge emits a split or supersession event, and records are never deleted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
