# WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive

## Package card

| Field | Value |
|---|---|
| Work package | `WP-072` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Citation Auditor / Archivist |
| Hard dependencies | WP-014, WP-017, WP-026, WP-061, WP-062, WP-063, WP-067, WP-069, WP-070, WP-071 |
| Related gates | G3,G9,G10 |
| Related controls | CTL-EPI-01, CTL-LIT-01 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-04, ACC-30 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Included and excluded sources, representation hashes, queries, screening decisions, status and actors become an immutable `LiteratureSetManifest`; the Zotero `90_Frozen_View` is only its mirror.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-072-T01 | Write the manifest snapshot query and a deterministic serialiser | Implementation owner | Commit / configuration / record reference |
| WP-072-T02 | Add the included, excluded, query, screening, status and licence references | Implementation owner | Commit / configuration / record reference |
| WP-072-T03 | Apply hashing, signature and an object-lock write | Implementation owner | Commit / configuration / record reference |
| WP-072-T04 | Produce portable CSL-JSON, BibTeX and RIS exports | Implementation owner | Commit / configuration / record reference |
| WP-072-T05 | Perform the selective sync into the Zotero `90_Frozen_View` | Implementation owner | Commit / configuration / record reference |
| WP-072-T06 | Establish manifest diff, new-version and synthesis invalidation | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `LiteratureSetManifest`
- `Signed frozen package`
- `Portable exports`
- `Zotero frozen view`
- `Freeze/diff report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- The same inputs producing the same manifest hash
- A new source creating a v2 rather than mutating v1
- An edit in the Zotero frozen view leaving the manifest unchanged
- A hard fail on a missing locator or status
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The manifest is a snapshot of the Source Registry.
- [ ] The Zotero archive is a convenience view, never the evidence itself.
- [ ] Older sets and their representations remain reachable.
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

An incomplete or incorrect manifest is marked `INVALIDATED` and a corrected new version is produced; the links from earlier claims and runs are preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
