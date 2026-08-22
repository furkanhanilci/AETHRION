# WP-056 — OPA Policy Platform and Bundle Distribution

## Package card

| Field | Value |
|---|---|
| Work package | `WP-056` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Policy Platform Lead |
| Independent verifier | Safety / Security / Internal Audit |
| Hard dependencies | WP-005, WP-006, WP-007, WP-009, WP-016, WP-020, WP-021, WP-055 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-GOV-02, CTL-DAT-02, CTL-SEC-02 |
| Related acceptance scenarios | ACC-06, ACC-18, ACC-24, ACC-26 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Role, data, tool, model, environment, gate, exception and budget decisions are distributed to every enforcement point as tested, signed, explainable OPA bundles.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-056-T01 | Establish the policy repository and its module boundaries | Implementation owner | Commit / configuration / record reference |
| WP-056-T02 | Apply the input-document and decision API standard | Implementation owner | Commit / configuration / record reference |
| WP-056-T03 | Write the unit, negative and property test harness | Implementation owner | Commit / configuration / record reference |
| WP-056-T04 | Establish signed bundle build, promotion and rollback | Implementation owner | Commit / configuration / record reference |
| WP-056-T05 | Bind decision-log redaction and WORM export | Implementation owner | Commit / configuration / record reference |
| WP-056-T06 | Add shadow evaluation with drift and coverage telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `OPA platform`
- `Policy bundle v1`
- `Policy test suite`
- `Bundle promotion pipeline`
- `Decision log pipeline`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of a D3 route, a T4 action and a self-review
- Denial under an expired exception
- Bundle rollback
- Fail-closed behaviour on unknown input
- A shadow decision diff
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An untested or unsigned bundle cannot reach production.
- [ ] Every decision carries a rule ID, a bundle digest and its obligations.
- [ ] If policy is unavailable, critical actions fail closed.
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

- A control not exercised by a negative test is an assumption.
- Default-allow egress anywhere in the chain nullifies every other isolation control.
- Sandbox escape is tested by attempting it, not by reading the configuration.

## Rollback / compensation

A faulty bundle returns atomically to the previous signed version; decision history is preserved and an impact scan is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
