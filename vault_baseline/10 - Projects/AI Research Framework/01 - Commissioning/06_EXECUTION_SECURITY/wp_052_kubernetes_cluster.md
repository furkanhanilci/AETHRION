# WP-052 — Kubernetes Cluster and Node Pool Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-052` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Infrastructure Lead |
| Independent verifier | SRE / Security |
| Hard dependencies | WP-021, WP-027, WP-051 |
| Related gates | G5,Platform |
| Related controls | CTL-SEC-04, CTL-OPS-03 |
| Related acceptance scenarios | ACC-27, ACC-33 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Management, service, standard execution, secure/D3+ and untrusted compute node pools are established with HA, quotas, isolation and signed workload admission.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/wp_051_trust_zone_network.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-052-T01 | Establish the cluster topology and control-plane HA | Implementation owner | Commit / configuration / record reference |
| WP-052-T02 | Apply the node pool, taint and toleration separation | Implementation owner | Commit / configuration / record reference |
| WP-052-T03 | Write the Pod Security, namespace and resource quota baseline | Implementation owner | Commit / configuration / record reference |
| WP-052-T04 | Establish the storage, network and ingress classes | Implementation owner | Commit / configuration / record reference |
| WP-052-T05 | Add autoscaling, capacity reserve and maintenance policy | Implementation owner | Commit / configuration / record reference |
| WP-052-T06 | Write the cluster backup, upgrade and restore runbook | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Kubernetes clusters`
- `Node pool catalog`
- `Namespace/security baseline`
- `Upgrade/restore runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Node failure and rescheduling
- Denial of a secure workload scheduled onto the wrong node
- A canary cluster upgrade
- A capacity pressure test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] D3/D4 and untrusted workloads never run outside their designated pool.
- [ ] Control-plane worker pods are separated from the execution namespace.
- [ ] Critical assurance capacity is reserved and cannot be consumed by feature work.
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

Cluster and node upgrades roll back, or use a blue-green control plane; workload manifests and artifacts are preserved throughout.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
