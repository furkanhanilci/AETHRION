# WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows

## Package card

| Field | Value |
|---|---|
| Work package | `WP-035` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Scientific Workflow Lead |
| Independent verifier | Methodologist / Evidence Lead / Falsification Lead |
| Hard dependencies | WP-008, WP-013, WP-017, WP-019, WP-032, WP-033, WP-034 |
| Related gates | G2,G3,G4 |
| Related controls | CTL-EPI-02, CTL-LIT-01, CTL-CST-01 |
| Related acceptance scenarios | ACC-01, ACC-39 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Method, literature set, baseline, falsification plan, stop rules and the decision to open compute are frozen as versioned artifacts behind gates.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-035-T01 | Write the protocol authoring, review and amendment workflow | Implementation owner | Commit / configuration / record reference |
| WP-035-T02 | Bind the `LiteratureCampaign` child and task contracts | Implementation owner | Commit / configuration / record reference |
| WP-035-T03 | Add the `LiteratureSetManifest` freeze activity | Implementation owner | Commit / configuration / record reference |
| WP-035-T04 | Establish baseline and `FalsificationPlan` validation | Implementation owner | Commit / configuration / record reference |
| WP-035-T05 | Add the leakage/contamination and budget-readiness checks | Implementation owner | Commit / configuration / record reference |
| WP-035-T06 | Apply the G2–G4 revise and reopen transitions | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `G2–G4 workflows`
- `Protocol amendment flow`
- `Literature freeze integration`
- `Compute-open decision`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A version test on a material protocol change
- A test proving a literature-set change forces a new synthesis
- Denial of a post-result baseline mutation
- A hard fail on identified leakage risk
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No expensive execution opens before G4 passes.
- [ ] Protocol and baseline carry a frozen hash.
- [ ] A newly added source never silently alters an existing manifest.
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

- Any consumer that can change gate state creates dual authority over the workflow.
- At-least-once delivery means every consumer must be idempotent, without exception.
- A workflow change that breaks open executions is a data incident, not a deploy.

## Rollback / compensation

A G2/G3/G4 revise opens a new artifact version; the relationships of previously frozen sets and runs are preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
