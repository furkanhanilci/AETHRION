# WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back

## Package card

| Field | Value |
|---|---|
| Work package | `WP-074` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Knowledge Curator / Data Platform Lead |
| Hard dependencies | WP-028, WP-030, WP-061, WP-072, WP-073 |
| Related gates | G8,G9,G10 |
| Related controls | CTL-OPS-03, CTL-EPI-01 |
| Related acceptance scenarios | ACC-21, ACC-22, ACC-31 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Source, claim, run and decision changes update only the generated zones; human synthesis links are checked, and the concept graph is a derived projection that can be rebuilt.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md), [WP-073 — Obsidian Vault, Human/Generated Zones and Templates](../07_LITERATURE_KNOWLEDGE/wp_073_obsidian_vault_model.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-074-T01 | Write the event-driven generated-block renderer | Implementation owner | Commit / configuration / record reference |
| WP-074-T02 | Establish the AIRL ID link resolver and backlink index | Implementation owner | Commit / configuration / record reference |
| WP-074-T03 | Apply human-edit detection and three-way zone merge | Implementation owner | Commit / configuration / record reference |
| WP-074-T04 | Add the broken/orphan link report and the curator queue | Implementation owner | Commit / configuration / record reference |
| WP-074-T05 | Bind concept and entity edge extraction to the derived graph | Implementation owner | Commit / configuration / record reference |
| WP-074-T06 | Write the full vault projection rebuild procedure | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Obsidian projection service`
- `Link checker`
- `Human-preservation diff`
- `Concept graph projection`
- `Rebuild runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A human edit arriving during a generated refresh
- A broken source or claim link
- A full projection rebuild
- A superseded-claim banner update
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The renderer cannot write into a human zone.
- [ ] A broken material link can block G9.
- [ ] Loss of the derived graph is not loss of the vault or of canonical records.
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

The projection is rebuilt on a new branch and merged after a diff review; conflicts go to the curator queue rather than being auto-resolved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
