# WP-053 — Kueue Queue, Quota and Priority Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-053` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Compute Platform Lead |
| Independent verifier | FinOps / Assurance / SRE |
| Hard dependencies | WP-006, WP-052 |
| Related gates | G5–G7 |
| Related controls | CTL-CST-01, CTL-SEC-04 |
| Related acceptance scenarios | ACC-09, ACC-33 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Research scouting, experiments, review, reproduction, incident and critical assurance work are scheduled under budget, quota, admission and safe preemption.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-053-T01 | Establish the ClusterQueue/LocalQueue and cohort model | Implementation owner | Commit / configuration / record reference |
| WP-053-T02 | Define the project and portfolio quotas and the resource flavours | Implementation owner | Commit / configuration / record reference |
| WP-053-T03 | Apply PriorityClasses and the assurance capacity reserve | Implementation owner | Commit / configuration / record reference |
| WP-053-T04 | Bind budget reservation to the Temporal task | Implementation owner | Commit / configuration / record reference |
| WP-053-T05 | Write the preemption, checkpoint and retry behaviour | Implementation owner | Commit / configuration / record reference |
| WP-053-T06 | Add queue wait, utilisation and cost telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Kueue configuration`
- `Quota/priority policy`
- `Budget admission adapter`
- `Queue dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Preemption of a low-priority scout job
- Capacity reservation for a critical reproduction
- Quota and budget denial
- Resume after checkpoint
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Preemption never loses canonical state or artifacts.
- [ ] Assurance work is never starved by feature fan-out.
- [ ] No service account can bypass quota.
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

A wrong priority or quota bundle returns to its previous version; queued workloads are re-evaluated and running workloads are not forcibly lost.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
