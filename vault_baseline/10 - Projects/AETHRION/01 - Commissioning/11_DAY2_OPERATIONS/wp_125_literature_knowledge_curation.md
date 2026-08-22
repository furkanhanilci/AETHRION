# WP-125 — Literature, Zotero and Obsidian Curation Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-125` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Citation Auditor / Knowledge Curator |
| Hard dependencies | WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-073, WP-074, WP-121 |
| Related gates | G3,G10,Day-2 |
| Related controls | CTL-LIT-01, CTL-LIT-02, CTL-LIT-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Sync conflicts, candidate aging, screening backlog, broken links, source status, annotation promotion and human/generated zone quality are managed continuously under defined SLAs.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/wp_064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/wp_067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/wp_068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/wp_070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/wp_071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md), [WP-073 — Obsidian Vault, Human/Generated Zones and Templates](../07_LITERATURE_KNOWLEDGE/wp_073_obsidian_vault_model.md), [WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/wp_074_obsidian_projection_sync.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-125-T01 | Run the daily sync/conflict/lag check and the weekly curator queue review | Implementation owner | Commit / configuration / record reference |
| WP-125-T02 | Track candidate TTL, used-source promotion and duplicate metrics | Implementation owner | Commit / configuration / record reference |
| WP-125-T03 | Run the monthly status, retraction and broken-link scan | Implementation owner | Commit / configuration / record reference |
| WP-125-T04 | Check the Obsidian human/generated diff and projection integrity | Implementation owner | Commit / configuration / record reference |
| WP-125-T05 | Perform the quarterly library, group, permission and licence review | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Curation calendar`
- `Queue/SLA reports`
- `Library quality scorecard`
- `Knowledge integrity report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A full resync sample
- Human note preservation
- Broken locator and link repair
- Retraction impact sampling
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every conflict has a known SLA and owner.
- [ ] Library item count is never treated as a success metric.
- [ ] Used sources target 100% identity, locator and status coverage.
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

On a sync or projection problem the connector or renderer is stopped; personal and human-authored data is never overwritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
