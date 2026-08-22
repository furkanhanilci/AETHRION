# WP-094 — Literature Workbench and Reconciliation UI

## Package card

| Field | Value |
|---|---|
| Work package | `WP-094` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Product Lead |
| Independent verifier | Knowledge Curator / Citation Auditor |
| Hard dependencies | WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-091 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01, CTL-LIT-02, CTL-LIT-03 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-03, ACC-04, ACC-28 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Researchers and curators manage seeds, candidates, resolver conflicts, screening, trust, annotation promotion, set freezing and status impact on one working surface.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-094-T01 | Write the campaign, query and coverage dashboard | Implementation owner | Commit / configuration / record reference |
| WP-094-T02 | Build the source identity, representation and trust detail views | Implementation owner | Commit / configuration / record reference |
| WP-094-T03 | Add the duplicate, merge and conflict reconciliation screen | Implementation owner | Commit / configuration / record reference |
| WP-094-T04 | Bind the screening include/exclude/disagreement queue | Implementation owner | Commit / configuration / record reference |
| WP-094-T05 | Write the annotation → `EvidenceCandidate` promotion view | Implementation owner | Commit / configuration / record reference |
| WP-094-T06 | Add Zotero sync receipts, lag and conflict views plus manifest freeze/diff | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Literature Workbench`
- `Resolver/reconciliation UI`
- `Screening UI`
- `Manifest freeze UI`
- `Sync health view`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A concurrent conflict resolving without overwrite
- A personal source rendered read-only
- A manifest diff producing a new version
- A retraction impact banner
- Accessible bulk screening
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The UI changes Source Registry state only through the field authority rules.
- [ ] The Zotero view is never presented as manifest evidence.
- [ ] Every human disposition carries an actor and a rationale.
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

A UI rollback preserves the canonical queues and cases; batch actions reconcile through their idempotency token.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
