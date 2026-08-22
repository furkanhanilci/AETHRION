# WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze

## Package card

| Field | Value |
|---|---|
| Work package | `WP-103` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Citation Auditor / Security |
| Hard dependencies | WP-035, WP-058, WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-094, WP-099 |
| Related gates | G3 |
| Related controls | CTL-LIT-01, CTL-LIT-03, CTL-SEC-01 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-03, ACC-05, ACC-28 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Human Zotero seeds and agent discovery results merge in the Source Registry, screening and annotation promotion run, and an immutable G3 set is frozen.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-094 — Literature Workbench and Reconciliation UI](../09_EXPERIENCE_OBSERVABILITY/WP-094_literature_workbench.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-103-T01 | Ingest the personal seed fixture | Implementation owner | Commit / configuration / record reference |
| WP-103-T02 | Run the agent literature campaign, snowball and counter-evidence search | Implementation owner | Commit / configuration / record reference |
| WP-103-T03 | Test duplicates, conflicts, 412 responses and human-field preservation | Implementation owner | Commit / configuration / record reference |
| WP-103-T04 | Complete the screening, disagreement, trust and status flow | Implementation owner | Commit / configuration / record reference |
| WP-103-T05 | Prepare an annotation for candidate → span promotion | Implementation owner | Commit / configuration / record reference |
| WP-103-T06 | Verify the manifest, exports, Zotero frozen view and audit trail | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Literature vertical dossier`
- `Frozen LiteratureSetManifest`
- `Zotero SyncReceipts`
- `Coverage/screening report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- ACC-01, 02, 03, 05 and 28
- Manifest hash reproducibility
- Preservation of a human note
- Containment of a prompt-injection PDF
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Source identifiers and representations are complete.
- [ ] Zotero never silently overwrites a canonical or human-authored field.
- [ ] The manifest is immutable and signed.
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

The test group collection and archive are preserved; connector writes are disabled and the slice is not accepted until every conflict is cleared.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
