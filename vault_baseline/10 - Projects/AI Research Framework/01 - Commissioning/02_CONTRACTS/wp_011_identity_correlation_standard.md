# WP-011 — Identity and End-to-End Correlation Standard

## Package card

| Field | Value |
|---|---|
| Work package | `WP-011` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Platform Lead |
| Independent verifier | Security Architect |
| Hard dependencies | WP-010 |
| Related gates | Platform |
| Related controls | CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Project, workflow, gate, task, actor, source, representation, claim, evidence, run, artifact, review, decision, cost and event identifiers become collision-free and queryable as one chain.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-011-T01 | Assign the UUIDv7 and opaque-ID formats per entity type | Implementation owner | Commit / configuration / record reference |
| WP-011-T02 | Write the project → workflow → run → artifact → claim/cost correlation chain | Implementation owner | Commit / configuration / record reference |
| WP-011-T03 | Define the identity fields for human, model and service actors | Implementation owner | Commit / configuration / record reference |
| WP-011-T04 | Model external locators such as Zotero keys, DOIs and ORCIDs as aliases, never as canonical identity | Implementation owner | Commit / configuration / record reference |
| WP-011-T05 | Establish the ID minting, tombstone and merge rules | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Identifier Standard`
- `Correlation envelope`
- `ID library contract`
- `Merge/tombstone rules`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Uniqueness and property-based tests
- A cross-service correlation fixture
- An alias-collision and merge test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No canonical ID depends on an external key.
- [ ] Every event and artifact carries an actor and a correlation identifier.
- [ ] A merge does not break existing references.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

A faulty ID mapping is corrected with a tombstone plus a replacement event; historical records are never overwritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
