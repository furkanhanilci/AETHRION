# WP-023 — Git, Worktree and Protected-Path Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-023` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Engineering Lead |
| Independent verifier | Security Reviewer |
| Hard dependencies | WP-022 |
| Related gates | G5,Engineering |
| Related controls | CTL-GOV-02, CTL-SUP-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Human and agent changes proceed on separate branches and worktrees, within a permitted file scope and pinned to a fixed target commit.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-023-T01 | Write the branch/commit naming and signed-commit policy | Implementation owner | Commit / configuration / record reference |
| WP-023-T02 | Define the agent task worktree lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-023-T03 | Apply the allowed/protected path manifest | Implementation owner | Commit / configuration / record reference |
| WP-023-T04 | Establish freeze-commit and correction-branch behaviour | Implementation owner | Commit / configuration / record reference |
| WP-023-T05 | Add the cleanup, abandoned-task and forensic retention rules | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Git policy`
- `Worktree controller contract`
- `Protected-path rules`
- `Freeze procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A negative test with two agents in the same ownership zone
- A protected-path write denial test
- A test proving a review is invalidated when its frozen target changes
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Every task carries a base commit and a target commit.
- [ ] An agent writes only inside its task worktree and its allowed paths.
- [ ] A correction produces a new frozen commit rather than amending the old one.
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

- Infrastructure built by hand once is infrastructure that cannot be rebuilt under pressure.
- A backup that has never been restored is not a backup.
- Environment parity erodes from the staging side first, and quietly.

## Rollback / compensation

When a task is cancelled the worktree is quarantined; artifacts and evidence are retained and the branch is archived on the owner's decision.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
