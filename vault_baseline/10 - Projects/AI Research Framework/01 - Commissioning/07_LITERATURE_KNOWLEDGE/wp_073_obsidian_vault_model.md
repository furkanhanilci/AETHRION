# WP-073 — Obsidian Vault, Human/Generated Zones and Templates

## Package card

| Field | Value |
|---|---|
| Work package | `WP-073` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Knowledge Curator / Governance |
| Hard dependencies | WP-012, WP-017, WP-022, WP-061, WP-072 |
| Related gates | G3,G8,G10 |
| Related controls | CTL-OPS-03 |
| Related acceptance scenarios | ACC-22 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Obsidian carries human synthesis across project, source, concept, claim, decision and result notes, with stable AIRL identifiers, Git history and protected human/generated blocks.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-073-T01 | Establish the vault, directory, tag and property standard | Implementation owner | Commit / configuration / record reference |
| WP-073-T02 | Write the project, source, concept, claim, decision and result templates | Implementation owner | Commit / configuration / record reference |
| WP-073-T03 | Add the `source_registry_id`, `claim_id` and `run_id` link fields | Implementation owner | Commit / configuration / record reference |
| WP-073-T04 | Apply human-authored versus generated fenced-block semantics | Implementation owner | Commit / configuration / record reference |
| WP-073-T05 | Establish the Git branch, review, merge and backup rules | Implementation owner | Commit / configuration / record reference |
| WP-073-T06 | Make the Better BibTeX key an alias and the AIRL ID canonical | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Obsidian vault baseline`
- `Note templates`
- `Zone/merge policy`
- `Git workflow`
- `User guide`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Template and schema lint
- Preservation of a human edit across a generated refresh
- Alias and canonical ID link resolution
- Git restore
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Obsidian never substitutes for the Source Registry or the Claim Ledger.
- [ ] Free human synthesis is preserved unchanged.
- [ ] Every generated block carries provenance and a timestamp.
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

A corrupted generated block is rebuilt from the canonical record; human Git history is restored from version control.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
