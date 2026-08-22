# WP-045 — Policy Router and Minimum-Sufficient Model Package

## Package card

| Field | Value |
|---|---|
| Work package | `WP-045` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Model Platform Lead |
| Independent verifier | Safety / Eval / FinOps |
| Hard dependencies | WP-005, WP-006, WP-007, WP-013, WP-016, WP-041, WP-042, WP-044 |
| Related gates | G1,G5,G6 |
| Related controls | CTL-DAT-02, CTL-CST-01, CTL-MOD-01 |
| Related acceptance scenarios | ACC-09, ACC-10, ACC-11, ACC-18, ACC-38 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

From the `TaskContract` role, risk, data, tool, latency, budget and independence inputs, the router deterministically selects only the eligible and **minimum sufficient** model/agent package.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-045-T01 | Bind the OPA pre-filter and the Capability Registry query | Implementation owner | Commit / configuration / record reference |
| WP-045-T02 | Write the quality-adjusted cost and latency selection ordering | Implementation owner | Commit / configuration / record reference |
| WP-045-T03 | Define the rules separating a single model from parallel or council fan-out | Implementation owner | Commit / configuration / record reference |
| WP-045-T04 | Apply independence-aware reviewer routing | Implementation owner | Commit / configuration / record reference |
| WP-045-T05 | Add fallback, retry and fan-out budget reservation | Implementation owner | Commit / configuration / record reference |
| WP-045-T06 | Emit the `RouteDecision` explanation and telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Policy Router`
- `RouteDecision service`
- `Fan-out/budget rules`
- `Routing conformance suite`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Low risk routing to the cheapest eligible option
- R3 enforcing the cross-family constraint
- A pause on insufficient budget
- `BLOCKED` when no eligible route exists
- Independence recalculation on fallback
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A prohibited provider or profile never enters the candidate list.
- [ ] Council routing is never the default.
- [ ] Every route records the rule, profile and budget decision behind it.
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

- A model alias is not a pinned identity; results obtained under an alias are not reproducible.
- An agent holding a credential defeats the entire broker design.
- Fallback routes are the least tested and most consequential path in this workstream.

## Rollback / compensation

Router rule releases are promoted after shadow comparison; on anomaly the previous bundle is restored and mis-routed tasks receive an impact scan.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
