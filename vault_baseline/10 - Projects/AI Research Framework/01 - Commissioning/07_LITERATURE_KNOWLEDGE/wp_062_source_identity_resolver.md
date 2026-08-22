# WP-062 — Source Identity Resolution, Deduplication and Merge

## Package card

| Field | Value |
|---|---|
| Work package | `WP-062` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Source Resolver Lead |
| Independent verifier | Knowledge Curator / Citation Auditor |
| Hard dependencies | WP-017, WP-050, WP-058, WP-061 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01 |
| Related acceptance scenarios | ACC-03, ACC-28 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

DOI, PMID, arXiv, ISBN, URL, title/author/year and file-hash signals resolve to a single `SourceRecord` with an explainable confidence; ambiguous collisions go to a human.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/wp_050_tool_connectors.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/wp_058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-062-T01 | Write the identifier normalisation and resolver chain | Implementation owner | Commit / configuration / record reference |
| WP-062-T02 | Bind Crossref and provider lookups through the broker | Implementation owner | Commit / configuration / record reference |
| WP-062-T03 | Define exact and fuzzy candidate generation and the match features | Implementation owner | Commit / configuration / record reference |
| WP-062-T04 | Apply safe auto-merge thresholds through small explicit rules | Implementation owner | Commit / configuration / record reference |
| WP-062-T05 | Write the `ConflictCase`, curator queue and split/merge lineage | Implementation owner | Commit / configuration / record reference |
| WP-062-T06 | Build the duplicate metrics and the known-item test set | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Source Resolver service`
- `Match rules/features`
- `Conflict queue`
- `Known-item/dedup test corpus`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Duplicate prevention on an identical DOI
- Separation of two different works sharing a title
- A manual case for contradicting title and year
- Cross-library Zotero duplicate mapping
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An ambiguous match never auto-merges silently.
- [ ] A merge preserves every external binding and every prior reference.
- [ ] Duplicate detection is not bounded by a single Zotero library.
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

A wrong merge is corrected by a split operation; an `ImpactCase` is opened for the affected manifests and claims.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
