# WP-067 — Zotero Two-Way Sync and Reconciliation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-067` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Knowledge Curator / SRE |
| Hard dependencies | WP-061, WP-062, WP-064, WP-065, WP-066 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01, CTL-OPS-01 |
| Related acceptance scenarios | ACC-03, ACC-28 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Human edits, agent proposals, concurrent versions, deletions, duplicates and loss of bridge state are reconciled — automatically or under human control — according to field authority.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-067-T01 | Establish the per-library and per-item version and `since` checkpoint store | Implementation owner | Commit / configuration / record reference |
| WP-067-T02 | Write the field-level three-way merge classes | Implementation owner | Commit / configuration / record reference |
| WP-067-T03 | Raise a `ConflictCase` for 412, deletion, permission and duplicate situations | Implementation owner | Commit / configuration / record reference |
| WP-067-T04 | Bind the manual reconciliation UI/API and the curator SLA | Implementation owner | Commit / configuration / record reference |
| WP-067-T05 | Write the full-resync plus dedup/rebind procedure | Implementation owner | Commit / configuration / record reference |
| WP-067-T06 | Establish sync lag, error and overwrite-detector telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Sync engine`
- `Reconciliation queue`
- `Full-resync runbook`
- `Conflict metrics/dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Concurrent human and agent edits
- A remotely deleted item
- Full resync after bridge state loss
- A cross-library duplicate
- Preservation of a human-authored note
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] There is no silent last-write-wins anywhere in the sync.
- [ ] A full resync produces no duplicates.
- [ ] A human-authoritative field is never overwritten by an agent merge.
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

Sync is stopped while checkpoints and receipts are preserved; a controlled rebuild is performed from the resolver plus remote versions.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
