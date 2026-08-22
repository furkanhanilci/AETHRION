# WP-071 — Screening, Inclusion/Exclusion and Coverage

## Package card

| Field | Value |
|---|---|
| Work package | `WP-071` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Methodologist / Blind Literature Reviewer |
| Hard dependencies | WP-007, WP-017, WP-061, WP-062, WP-069, WP-070 |
| Related gates | G3 |
| Related controls | CTL-GOV-02, CTL-EPI-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Title/abstract and full-text screening reaches a freezable set through reason-coded inclusion and exclusion, recorded disagreement, sampling and risk-based independent review.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-071-T01 | Define the screening criteria, rubric and reason codes | Implementation owner | Commit / configuration / record reference |
| WP-071-T02 | Establish the title/abstract and full-text queues | Implementation owner | Commit / configuration / record reference |
| WP-071-T03 | Add blind human/agent assignment and conflict-of-interest checks | Implementation owner | Commit / configuration / record reference |
| WP-071-T04 | Apply R1/R2/R3 dual-review and sampling depth | Implementation owner | Commit / configuration / record reference |
| WP-071-T05 | Bind `DisagreementCase` and arbiter escalation | Implementation owner | Commit / configuration / record reference |
| WP-071-T06 | Produce the PRISMA-style flow, coverage and unknown-status report | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Screening service`
- `Decision queue`
- `Reason taxonomy`
- `Coverage/flow report`
- `Screening calibration set`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Include/exclude boundary calibration
- A case with conflicting reviewers
- The missing-full-text state
- The R3 independence requirement
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every exclusion carries a reason code and an actor.
- [ ] Material disagreement is never hidden by aggregation.
- [ ] An unavailable source is never counted as `INCLUDED` by default.
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

A criteria change opens an amendment and a rescreen queue for the affected decisions; previous decisions are preserved as history.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
