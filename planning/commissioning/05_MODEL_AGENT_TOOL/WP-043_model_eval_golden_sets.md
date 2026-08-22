# WP-043 — Role-Based Model Evaluation and Golden Set Management

## Package card

| Field | Value |
|---|---|
| Work package | `WP-043` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Eval Office |
| Independent verifier | Independent Domain/Assurance Reviewer |
| Hard dependencies | WP-007, WP-014, WP-018, WP-019, WP-020, WP-029, WP-042 |
| Related gates | Platform,G6 |
| Related controls | CTL-MOD-01, CTL-EPI-04 |
| Related acceptance scenarios | ACC-07, ACC-37 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Contamination-protected, versioned evaluation sets and measurement rubrics are built for the planner, scout, extractor, coder, reviewer and arbiter roles.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-029 — MLflow Experiment and Evaluation Tracking Foundation](../03_FOUNDATION/WP-029_mlflow_foundation.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-043-T01 | Derive the role-specific capability and failure taxonomy | Implementation owner | Commit / configuration / record reference |
| WP-043-T02 | Prepare the golden, adversarial and regression sets | Implementation owner | Commit / configuration / record reference |
| WP-043-T03 | Establish dataset split, access, canary and contamination controls | Implementation owner | Commit / configuration / record reference |
| WP-043-T04 | Calibrate the deterministic graders and the human rubrics | Implementation owner | Commit / configuration / record reference |
| WP-043-T05 | Add validated-precision, incremental-finding, cost, triage and latency metrics | Implementation owner | Commit / configuration / record reference |
| WP-043-T06 | Write the evaluation manifest and its release process | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Eval dataset manifests`
- `Role eval harness`
- `Grader/rubric bundle`
- `Contamination controls`
- `Eval scorecard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Known-answer and edge-case validation
- Inter-rater calibration
- A negative access test against golden items
- Order, verbosity and self-preference bias probes
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The evaluation set lives outside the credential scope of production prompts and logs.
- [ ] A single aggregate score never substitutes for role eligibility.
- [ ] On detected contamination the set is invalidated rather than patched.
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

A contaminated bundle is marked `INVALIDATED`, a new version is created, and every profile qualified against it is re-evaluated.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
