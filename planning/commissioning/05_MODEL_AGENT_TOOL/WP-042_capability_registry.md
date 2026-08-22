# WP-042 — Capability Registry and Profile Lifecycle

## Package card

| Field | Value |
|---|---|
| Work package | `WP-042` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Eval Office |
| Independent verifier | Model Platform Lead / Safety |
| Hard dependencies | WP-005, WP-006, WP-007, WP-011, WP-013, WP-016, WP-020, WP-025, WP-041 |
| Related gates | G1,G5,G10 |
| Related controls | CTL-MOD-01, CTL-MOD-02 |
| Related acceptance scenarios | ACC-36 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

For each model-snapshot × runtime-adapter combination, the admitted roles, data classes, tools, risk classes, evaluation evidence, cost, expiry and ejection state are held in a canonical registry.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-042-T01 | Build the `CapabilityProfile` persistence layer and API | Implementation owner | Commit / configuration / record reference |
| WP-042-T02 | Write the REGISTERED → SHADOW → ADVISORY → CONDITIONAL → MANDATORY / SUSPENDED / DISABLED state machine | Implementation owner | Commit / configuration / record reference |
| WP-042-T03 | Add the role, data, tool and risk eligibility query | Implementation owner | Commit / configuration / record reference |
| WP-042-T04 | Apply the expiry, requalification and ejection triggers | Implementation owner | Commit / configuration / record reference |
| WP-042-T05 | Bind the open-task impact event | Implementation owner | Commit / configuration / record reference |
| WP-042-T06 | Define the change and audit UI contract | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Capability Registry service`
- `Profile state machine`
- `Eligibility API`
- `Expiry/revoke scheduler`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- An expired profile being excluded from routing
- A suspended profile never used as a fallback
- A snapshot change forcing requalification
- Revocation raising an `ImpactCase` for open tasks
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No model-to-role assignment can be made outside the registry.
- [ ] A profile whose qualification period expires is suspended automatically.
- [ ] Every profile carries an immutable evaluation bundle reference.
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

A wrong profile is revoked; the router cache is invalidated and an impact scan runs, while historical run lineage is preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
