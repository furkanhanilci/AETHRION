# WP-013 — Project, Task and Role Contract Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-013` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Control Plane Lead |
| Independent verifier | Governance Lead |
| Hard dependencies | WP-003, WP-004, WP-005, WP-006, WP-007, WP-011 |
| Related gates | G0–G6 |
| Related controls | CTL-GOV-01, CTL-DAT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Project intent, role, risk, data, tooling, budget, acceptance and independence fields travel between the lifecycle and the agent runtime as versioned contracts, so that no provider-specific detail leaks into the canonical layer.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md), [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-013-T01 | Define the `ProjectCharter` and `ControlPlan` contract | Implementation owner | Commit / configuration / record reference |
| WP-013-T02 | Write the `TaskContract` input, output, non-goal and acceptance fields | Implementation owner | Commit / configuration / record reference |
| WP-013-T03 | Add the `RoleContract` mandate, tool, data, risk and prohibited-action fields | Implementation owner | Commit / configuration / record reference |
| WP-013-T04 | Define the `AgentResult` format including gaps and assumptions | Implementation owner | Commit / configuration / record reference |
| WP-013-T05 | Write the backward-compatibility and contract versioning rules | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ProjectContract schemas`
- `TaskContract schema`
- `RoleContract schema`
- `AgentResult schema`
- `Contract examples`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Positive and negative schema fixtures
- Unknown-field and version-compatibility tests
- Forbidden-tool and missing-acceptance tests
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No runtime- or provider-specific field leaks into a canonical contract.
- [ ] Every task carries an owner, a budget, acceptance criteria and an allowed scope.
- [ ] Gaps and assumptions are visible as self-declarations and are never counted as a pass.
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

An incompatible contract is rejected; the adapter continues to support the previous contract version through an explicit converter.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
