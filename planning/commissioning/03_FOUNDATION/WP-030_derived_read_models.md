# WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models

## Package card

| Field | Value |
|---|---|
| Work package | `WP-030` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Data Lead |
| Independent verifier | Data Platform Lead / Assurance |
| Hard dependencies | WP-012, WP-017, WP-018, WP-025, WP-026, WP-028 |
| Related gates | Platform,G10 |
| Related controls | CTL-OPS-03, CTL-OBS-01 |
| Related acceptance scenarios | ACC-21 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The provenance graph, semantic retrieval and full-text indexes become read models that can be rebuilt from scratch out of canonical events and records.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-030-T01 | Define the projection schemas and their source events | Implementation owner | Commit / configuration / record reference |
| WP-030-T02 | Build the Neo4j claim/source/run/review graph projection | Implementation owner | Commit / configuration / record reference |
| WP-030-T03 | Add the embedding model and version metadata to pgvector | Implementation owner | Commit / configuration / record reference |
| WP-030-T04 | Establish the OpenSearch index, retention and data-class policy | Implementation owner | Commit / configuration / record reference |
| WP-030-T05 | Add projection checkpoints and lag telemetry | Implementation owner | Commit / configuration / record reference |
| WP-030-T06 | Write the full rebuild and index-swap procedure | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Projection services`
- `Graph/vector/search indexes`
- `Rebuild jobs`
- `Integrity/lag dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Canonical → projection count and hash reconciliation
- A full rebuild after deliberate graph corruption
- A reindex test following an embedding model change
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No derived store accepts a canonical write.
- [ ] A projection can be deleted and rebuilt.
- [ ] Data class, deletion and legal-hold propagate into the projection.
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

- Infrastructure built by hand once is infrastructure that cannot be rebuilt under pressure.
- A backup that has never been restored is not a backup.
- Environment parity erodes from the staging side first, and quietly.

## Rollback / compensation

A corrupted index is rebuilt in a new namespace; once verified, the alias is switched atomically.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
