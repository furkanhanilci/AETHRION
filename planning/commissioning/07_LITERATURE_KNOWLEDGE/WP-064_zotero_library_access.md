# WP-064 — Zotero Library, Collection and Permission Model

## Package card

| Field | Value |
|---|---|
| Work package | `WP-064` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Security / Governance |
| Hard dependencies | WP-004, WP-012, WP-017, WP-049, WP-050, WP-061 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-03, CTL-SEC-03 |
| Related acceptance scenarios | ACC-01, ACC-02 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The personal Zotero library becomes a read-only seed surface, AIRL group libraries become collaboration surfaces bounded by trust and membership, and agent-managed collections carry an explicit namespace.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-064-T01 | Verify the personal-library read-only credential and its access boundary | Implementation owner | Commit / configuration / record reference |
| WP-064-T02 | Define the criteria for opening a group library: membership, confidentiality, licence, retention and ownership | Implementation owner | Commit / configuration / record reference |
| WP-064-T03 | Create the project collection template | Implementation owner | Commit / configuration / record reference |
| WP-064-T04 | Establish 00_Human_Seeds / 10_Agent_Candidates / 20_Screening / 30_Included / 40_Used / 50_Excluded / 80_Updates / 90_Frozen_View | Implementation owner | Commit / configuration / record reference |
| WP-064-T05 | Apply agent versus human authority and the R3 intake/curated separation | Implementation owner | Commit / configuration / record reference |
| WP-064-T06 | Write the organisation owner/admin continuity plan | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Zotero topology`
- `Collection template`
- `Credential/permission matrix`
- `Library lifecycle SOP`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A negative write test against the personal library
- Denial of a write to the wrong group or collection
- R3 intake → curated promotion
- An owner-continuity tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A group per project is not the default; the trust boundary decides.
- [ ] An agent cannot write to the personal library.
- [ ] A collection namespace alone is never counted as a security control.
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

A wrong group or permission release is revoked; the write connector is disabled and the `SyncReceipt` ledger is audited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
