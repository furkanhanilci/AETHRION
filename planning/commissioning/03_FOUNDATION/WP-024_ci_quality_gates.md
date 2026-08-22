# WP-024 — CI Foundation and Deterministic Quality Gates

## Package card

| Field | Value |
|---|---|
| Work package | `WP-024` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Engineering Productivity Lead |
| Independent verifier | Mechanical Verifier |
| Hard dependencies | WP-020, WP-022, WP-023 |
| Related gates | G5–G9,Engineering |
| Related controls | CTL-SUP-01, CTL-OPS-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Format, lint, type, unit, integration, schema, policy, security and build checks produce a standard interface and machine-readable evidence output.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/WP-022_repository_topology.md), [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/WP-023_git_worktree_branch_policy.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-024-T01 | Define the CI job taxonomy and pin the target revision | Implementation owner | Commit / configuration / record reference |
| WP-024-T02 | Add the schema, policy and architecture linters | Implementation owner | Commit / configuration / record reference |
| WP-024-T03 | Emit test results as machine-readable artifacts | Implementation owner | Commit / configuration / record reference |
| WP-024-T04 | Establish the split between fail-fast checks and the full suite | Implementation owner | Commit / configuration / record reference |
| WP-024-T05 | Define flaky-test quarantine and the owner SLA for clearing it | Implementation owner | Commit / configuration / record reference |
| WP-024-T06 | Trigger signed build provenance | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `CI pipelines`
- `Verification summary schema adapter`
- `Test ownership registry`
- `Flake policy`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A known-fail fixture that must stop CI
- A negative test mixing artifacts from different commits
- A retry and flaky-classification test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A failing required check cannot be bypassed.
- [ ] Evidence carries the target commit and the environment.
- [ ] Deleting or weakening a test requires owner review.
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

A faulty pipeline returns to its previous signed version; required checks are never switched off to unblock a merge.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
