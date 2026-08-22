# WP-055 — SPIFFE/SPIRE Workload Identity and Vault

## Package card

| Field | Value |
|---|---|
| Work package | `WP-055` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Identity Platform Lead |
| Independent verifier | Security / Internal Audit |
| Hard dependencies | WP-004, WP-016, WP-021, WP-025, WP-031, WP-049, WP-051, WP-052 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-SEC-03, CTL-GOV-01 |
| Related acceptance scenarios | ACC-25, ACC-26 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Human, service, worker and sandbox actors use attested identity and short-lived, purpose-bound credentials instead of long-lived shared secrets.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-031 — Temporal Platform, Namespaces and HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-055-T01 | Deploy the SPIRE server and agents and define the trust domain | Implementation owner | Commit / configuration / record reference |
| WP-055-T02 | Write the service and workload registration selectors | Implementation owner | Commit / configuration / record reference |
| WP-055-T03 | Establish the Vault auth methods, secret engines and lease policies | Implementation owner | Commit / configuration / record reference |
| WP-055-T04 | Bind human OIDC/MFA/RBAC and the decision actor binding | Implementation owner | Commit / configuration / record reference |
| WP-055-T05 | Add credential injection, rotation and revocation telemetry | Implementation owner | Commit / configuration / record reference |
| WP-055-T06 | Establish the two-person break-glass workflow | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `SPIRE/Vault deployments`
- `Identity registry mapping`
- `Lease policies`
- `Break-glass procedure`
- `Identity audit dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial on a wrong workload selector
- Denial of access under an expired lease
- Lease revocation on task cancellation
- Denial of a forged approval identity
- A break-glass audit trail
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No shared static production credential exists.
- [ ] Every lease carries a task, purpose and target scope.
- [ ] Every human decision is bound to a verified MFA context.
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

A compromised identity or lease is revoked; affected workloads pause and an incident plus impact scan is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
