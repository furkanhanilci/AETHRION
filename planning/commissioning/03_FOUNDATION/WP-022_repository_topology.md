# WP-022 — Repository Topology and Code Ownership

## Package card

| Field | Value |
|---|---|
| Work package | `WP-022` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Platform Lead / Security |
| Hard dependencies | WP-010, WP-020 |
| Related gates | Platform |
| Related controls | CTL-SUP-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Boundaries and owners for the control plane, services, schemas, policy, IaC, workflows, agents, tests and docs are made explicit in the repository structure.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-022-T01 | Close the monorepo versus polyrepo decision with an ADR | Implementation owner | Commit / configuration / record reference |
| WP-022-T02 | Create the service and bounded-context directories | Implementation owner | Commit / configuration / record reference |
| WP-022-T03 | Define CODEOWNERS and the protected paths | Implementation owner | Commit / configuration / record reference |
| WP-022-T04 | Write the shared-library and dependency-direction rules | Implementation owner | Commit / configuration / record reference |
| WP-022-T05 | Separate the generated-code, migration and test-fixture areas | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Repository skeleton`
- `CODEOWNERS`
- `Dependency rules`
- `Developer guide`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An architecture dependency lint
- A protected-path approval test
- A build-graph smoke test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The canonical schema, policy and IaC owners are distinct.
- [ ] No circular dependency exists between bounded contexts.
- [ ] A standard scaffold exists for creating a new service.
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

A wrong topology is reversed on a migration branch; repository history is never rewritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
