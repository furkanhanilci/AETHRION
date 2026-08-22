# WP-083 — ExperimentBatch and Staged Execution

## Package card

| Field | Value |
|---|---|
| Work package | `WP-083` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Scientific Engineering Lead |
| Independent verifier | Methodologist / FinOps / SRE |
| Hard dependencies | WP-032, WP-035, WP-045, WP-053, WP-054, WP-082 |
| Related gates | G4,G5 |
| Related controls | CTL-CST-01, CTL-DAT-01 |
| Related acceptance scenarios | ACC-09, ACC-33, ACC-39 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Experiments proceed smoke → baseline → small sweep → full run inside a controlled batch workflow governed by success, stop and budget criteria and by checkpoints.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/wp_054_gvisor_sandbox.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-083-T01 | Write the `ExperimentBatch` workflow and the batch/item state model | Implementation owner | Commit / configuration / record reference |
| WP-083-T02 | Establish the staged compute promotion checks | Implementation owner | Commit / configuration / record reference |
| WP-083-T03 | Apply the parameter/seed matrix and fan-out caps | Implementation owner | Commit / configuration / record reference |
| WP-083-T04 | Add checkpointing, preemption, resume and partial-result behaviour | Implementation owner | Commit / configuration / record reference |
| WP-083-T05 | Bind budget reservation, release and cost attribution | Implementation owner | Commit / configuration / record reference |
| WP-083-T06 | Implement the stop / pivot / negative-result decision | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ExperimentBatch workflow`
- `Staging policy`
- `Parameter manifest`
- `Checkpoint/recovery logic`
- `Batch report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A smoke failure preventing the full run
- A hard budget stop preserving state
- Resume after a Kueue preemption
- Partial batch result semantics
- Closure of a negative result
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Expensive compute never opens without G4 and the preceding stage passing.
- [ ] The batch preserves every run manifest it produced.
- [ ] Plans and metrics cannot be changed after looking at the result.
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

- Independence asserted in a record but not enforced by the router is decorative.
- A review that sees the producer's conclusion first is anchored, not independent.
- Reproduction that reuses the producer's environment reproduces the environment, not the result.

## Rollback / compensation

Pausing or cancelling a batch releases compute and leases; completed run artifacts are preserved and resume proceeds under a new lease.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
