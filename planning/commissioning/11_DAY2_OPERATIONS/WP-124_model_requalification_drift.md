# WP-124 — Model Requalification, Drift and Ejection Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-124` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Eval Office |
| Independent verifier | Admission Board / Safety / FinOps |
| Hard dependencies | WP-042, WP-043, WP-044, WP-045, WP-108, WP-121 |
| Related gates | G10,Day-2 |
| Related controls | CTL-MOD-01, CTL-MOD-02 |
| Related acceptance scenarios | — a Day-2 rhythm is exercised in operation, not as a go-live gate |
| Recurring counterpart of | ACC-10, ACC-11, ACC-36 — those scenarios verify the **initial** qualification before cutover; this package owns the **recurring** one afterwards |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

A change in model snapshot, provider behaviour, evaluation quality, latency, cost, safety or data contract produces periodic requalification and, where warranted, ejection.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/WP-043_model_eval_golden_sets.md), [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/WP-044_model_qualification_admission.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-124-T01 | Operate the profile expiry calendar and the provider change monitor | Implementation owner | Commit / configuration / record reference |
| WP-124-T02 | Run the role regression and adversarial evaluations | Implementation owner | Commit / configuration / record reference |
| WP-124-T03 | Analyse production validated precision, quality and cost drift | Implementation owner | Commit / configuration / record reference |
| WP-124-T04 | Manage the SHADOW → admission and admitted → suspend/eject decisions | Implementation owner | Commit / configuration / record reference |
| WP-124-T05 | Run the open task/run/claim impact scan and invalidate the router cache | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Requalification reports`
- `CapabilityProfile decisions`
- `Drift/ejection events`
- `ImpactCase results`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A silent snapshot change
- Quality, latency and cost drift
- A safety or data-contract change
- No eligible route remaining after an ejection
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An expired profile leaves the routing pool automatically.
- [ ] An ejection does not alter past runs but does produce an impact assessment.
- [ ] A newly popular model does not enter a role without evaluation.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

A wrong ejection can be superseded by a `DecisionRecord`; re-admission still requires fresh evidence.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
