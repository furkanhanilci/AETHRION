# WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-085` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Reproducibility Lead |
| Independent verifier | Assurance Lead / Statistician |
| Hard dependencies | WP-005, WP-007, WP-019, WP-077, WP-081, WP-082, WP-083, WP-084 |
| Related gates | G7 |
| Related controls | CTL-EPI-03 |
| Related acceptance scenarios | ACC-19, ACC-20 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The four verification types run under separate protocols, tolerances, independence requirements and certificates; the risk class determines the minimum required combination.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/WP-083_experiment_batch.md), [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-085-T01 | Write the verification type selector and its policy | Implementation owner | Commit / configuration / record reference |
| WP-085-T02 | Establish the same-code, same-environment repeatability job | Implementation owner | Commit / configuration / record reference |
| WP-085-T03 | Establish the independent-environment reproducibility job | Implementation owner | Commit / configuration / record reference |
| WP-085-T04 | Apply the seed, parameter and data-slice robustness matrix | Implementation owner | Commit / configuration / record reference |
| WP-085-T05 | Write the independent data/method replication request lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-085-T06 | Produce tolerance, pre-registration, root-cause, disposition and certificate records | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Verification pipeline`
- `Type-specific protocols`
- `Robustness matrix`
- `Reproduction certificates`
- `Failure taxonomy`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Repeatability passing while reproducibility fails
- A robustness edge slice failing
- The replication-unavailable state
- Enforcement of a pre-declared tolerance
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The four types are never substituted for one another.
- [ ] R3 does not pass without a clean-room run and the required robustness checks.
- [ ] A failure moves the claim to `CHALLENGED` and opens a root-cause queue item.
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

A failed certificate is never deleted; a corrected manifest produces a new verification run and a new certificate version.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
