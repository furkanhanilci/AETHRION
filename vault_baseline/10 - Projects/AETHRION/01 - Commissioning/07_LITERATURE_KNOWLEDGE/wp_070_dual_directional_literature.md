# WP-070 — Human + Agent Two-Way Literature Discovery

## Package card

| Field | Value |
|---|---|
| Work package | `WP-070` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Independent Literature Reviewer |
| Hard dependencies | WP-007, WP-045, WP-047, WP-062, WP-065, WP-066, WP-069 |
| Related gates | G3 |
| Related controls | CTL-EPI-02, CTL-GOV-02 |
| Related acceptance scenarios | ACC-01, ACC-02 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Human seeds are expanded by agents and agent candidates are filtered by human selection and counter-evidence search; coverage and provenance stay visible from both directions.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-047 — Role Bundle Registry and Agent Contract Compiler](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-070-T01 | Separate the human seed branch from the agent discovery branch | Implementation owner | Commit / configuration / record reference |
| WP-070-T02 | Run the keyword, citation, snowball and semantic scout bundles | Implementation owner | Commit / configuration / record reference |
| WP-070-T03 | Merge results from different models and strategies through the resolver | Implementation owner | Commit / configuration / record reference |
| WP-070-T04 | Add the counter-evidence and minority-source branch | Implementation owner | Commit / configuration / record reference |
| WP-070-T05 | Treat candidate ranking as triage, never as a decision | Implementation owner | Commit / configuration / record reference |
| WP-070-T06 | Feed human inclusion decisions back into the next query iteration | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Dual-loop discovery workflow`
- `Discovery provenance`
- `Candidate/coverage matrix`
- `Counter-evidence log`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Human seed → agent snowball expansion
- Agent candidate → human inclusion
- Retention of minority and counter sources
- Partial state when one branch is unavailable
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An agent's popularity ordering is not an inclusion decision.
- [ ] Sources from both directions pass through the same resolver and deduplication.
- [ ] Search gaps and disagreements remain visible rather than being smoothed away.
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

A faulty scout profile or bundle is disabled; the candidates it produced are not invalidated but receive lower trust and a disposition through their source provenance.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
