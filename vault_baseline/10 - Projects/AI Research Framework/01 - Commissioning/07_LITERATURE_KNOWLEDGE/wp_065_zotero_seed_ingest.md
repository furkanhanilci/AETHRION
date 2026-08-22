# WP-065 — Personal Zotero Seed Ingest Pipeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-065` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Knowledge Curator / Security |
| Hard dependencies | WP-017, WP-049, WP-050, WP-061, WP-062, WP-064 |
| Related gates | G3 |
| Related controls | CTL-LIT-01, CTL-LIT-03 |
| Related acceptance scenarios | ACC-01 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Seed sources the researcher selects in their personal Zotero are pulled into the Source Registry and the project intake queue through a read-only incremental sync.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/wp_050_tool_connectors.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/wp_064_zotero_library_access.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-065-T01 | Establish a dedicated read-only API key or OAuth scope | Implementation owner | Commit / configuration / record reference |
| WP-065-T02 | Write the selected-collection and tag opt-in mechanism | Implementation owner | Commit / configuration / record reference |
| WP-065-T03 | Implement the version/`since` token incremental reader | Implementation owner | Commit / configuration / record reference |
| WP-065-T04 | Normalise the item, attachment, note and annotation bindings | Implementation owner | Commit / configuration / record reference |
| WP-065-T05 | Bind the resolver, deduplication and project seed event | Implementation owner | Commit / configuration / record reference |
| WP-065-T06 | Add behaviour for deletions, moves and permission changes | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Personal seed adapter`
- `Opt-in configuration`
- `Sync state/receipts`
- `Seed ingest dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Ingest of a new seed
- Re-reading the same seed without creating a duplicate
- A personal edit producing a new version
- Denial of any write attempt on the credential
- A pause when the permission is revoked
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] AIRL does not ingest the entire personal library by default.
- [ ] No personal record is ever modified.
- [ ] The Source Registry mapping carries a version and its provenance.
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

If sync state is lost, a full read plus deduplication is performed; no reconciliation write is ever sent to personal Zotero.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
