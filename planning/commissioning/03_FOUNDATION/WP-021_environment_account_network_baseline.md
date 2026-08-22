# WP-021 — Development, Staging and Production Environment Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-021` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Lead |
| Independent verifier | Security Architect / SRE |
| Hard dependencies | WP-001, WP-006, WP-010, WP-020 |
| Related gates | Platform |
| Related controls | CTL-DAT-02, CTL-SEC-02 |
| Related acceptance scenarios | ACC-18, ACC-27 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Accounts and subscriptions, regions, VPC and network layout, DNS, encryption, administrative access and the environment promotion boundaries are separated in a production-ready configuration.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/WP-001_commissioning_charter.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-021-T01 | Separate the dev, staging and production accounts and their trust boundaries | Implementation owner | Commit / configuration / record reference |
| WP-021-T02 | Design the management, data and execution network segments | Implementation owner | Commit / configuration / record reference |
| WP-021-T03 | Establish the region, data-residency and encryption-key model | Implementation owner | Commit / configuration / record reference |
| WP-021-T04 | Restrict administrative and break-glass access behind MFA | Implementation owner | Commit / configuration / record reference |
| WP-021-T05 | Write the environment promotion and seed-data rules | Implementation owner | Commit / configuration / record reference |
| WP-021-T06 | Review the baseline IaC plan | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Environment topology`
- `Account/network IaC`
- `Access baseline`
- `Environment promotion policy`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A cross-environment access negative test
- An encryption and key-ownership verification
- A production-route and break-glass tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No production credential exists in any lower environment.
- [ ] The D3/D4 region and network policy is enforceable, not merely stated.
- [ ] The whole environment can be rebuilt from IaC.
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

On an IaC apply failure, roll back or destroy within the transaction scope; no manual intervention is performed against a shared production resource.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
