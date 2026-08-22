# WP-041 — LiteLLM Model Gateway Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-041` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Model Platform Lead |
| Independent verifier | Security / FinOps / SRE |
| Hard dependencies | WP-006, WP-011, WP-013, WP-016, WP-020, WP-021, WP-025 |
| Related gates | G2–G7 |
| Related controls | CTL-DAT-02, CTL-CST-01, CTL-MOD-01 |
| Related acceptance scenarios | ACC-09, ACC-10, ACC-11, ACC-18 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Every model call passes through a provider-independent gateway that applies identity, data-class control, budget, rate limiting and observability. No component holds a provider credential of its own.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-041-T01 | Deploy the gateway in HA and configure the provider adapters | Implementation owner | Commit / configuration / record reference |
| WP-041-T02 | Bind workload identity, project/role tags and authentication | Implementation owner | Commit / configuration / record reference |
| WP-041-T03 | Apply the data, region and retention routing filters | Implementation owner | Commit / configuration / record reference |
| WP-041-T04 | Add timeouts, rate limits, circuit breakers and the admitted-fallback rule | Implementation owner | Commit / configuration / record reference |
| WP-041-T05 | Emit usage and cost events with prompt/output redaction | Implementation owner | Commit / configuration / record reference |
| WP-041-T06 | Apply pinned-snapshot and cache policy | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `LiteLLM deployment`
- `Provider configuration`
- `Gateway policy adapter`
- `Model-call audit/cost events`
- `Gateway runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of a D3 payload to a public provider
- Primary 5xx failing over only to an admitted fallback
- `BLOCKED` when no eligible fallback exists
- Hard-budget denial
- Snapshot-to-usage correlation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No direct provider credential use exists anywhere in the system.
- [ ] A fallback must be admitted under the same policy scope as the primary.
- [ ] The pinned snapshot is recorded, never the alias.
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

Provider and configuration changes are promoted through canary plus shadow traffic; on failure, routing returns to the previous signed configuration.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
