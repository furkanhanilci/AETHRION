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
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-085_repro_robustness_replication.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-085_repro_robustness_replication.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The four verification types run under separate protocols, tolerances, independence requirements and certificates; the risk class determines the minimum required combination.


## Analysis
### What this package actually decides

Which of the four verifications a claim actually needs, and it refuses to let one
stand in for another. WP-019 defined the four types; this package runs them under
**separate protocols, tolerances, independence requirements and certificates**.

### The architecture already split G7 for this reason

`00_PROGRAM/01` records the refinement: **G7a** deterministic reproduction and
**G7b** distributional replication, *which are different operations with different
tolerances*.

| Type | Question | Held constant | What a failure means |
|---|---|---|---|
| Repeatability | Same everything, same result? | Everything | The run is broken |
| Reproducibility | Same artifacts, different machine? | The manifest | The manifest is incomplete |
| Robustness | Does the conclusion survive perturbation? | The conclusion | The finding is fragile |
| Replication | Independent attempt, same conclusion? | The question | Possibly a real difference |

Reporting all four as "reproduction failed" destroys the diagnosis.

### The structural constraint that bounds this package

`00_PROGRAM/01` against invariant 4: hosted models carry no pinnable snapshot, so
**deterministic reproduction requires local open-weight models with a weight-file
hash**. A claim produced with a hosted model cannot reach G7a — and the selector
must refuse it on structural grounds rather than reporting a tolerance failure.

That is a real limit on what this laboratory can claim, and it belongs in the
certificate.

### Tolerances are pre-registered (T06)

A tolerance set after seeing the reproduction result is not a tolerance. It sits in
the frozen manifest (WP-019, WP-081), and widening it afterwards is refused.

### Root cause, not a boolean (T06)

Six categories: environment drift, data drift, seed handling, model change, genuine
non-determinism, defect in the original. **Only the last means the claim was
wrong**, and a report that cannot distinguish them turns every failure into an
alarm nobody can act on.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md) | `Method Registry` · `Protocol validators` · `Amendment workflow` · `Post-hoc change detector` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/WP-083_experiment_batch.md) | `ExperimentBatch workflow` · `Staging policy` · `Parameter manifest` · `Checkpoint/recovery logic` |
| [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.md) | `Clean-room platform` · `Reproducer profile` · `Environment resolver` · `Isolation attestation` |

### Full prerequisite closure

**68 of 141 packages (48%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-082` |
| 30 | `WP-067` · `WP-083` · `WP-084` |
| 31 | `WP-068` |
| 32 | `WP-076` |
| 33 | `WP-077` |

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-090` · `WP-095` · `WP-105` · `WP-106` · `WP-113` · `WP-126`
- **Transitively reachable:** **30 of 141 packages (21%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **34** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Reproducibility Lead |
| Independent verifier | Assurance Lead / Statistician |
| Gates touched | `G7` |
| Controls | `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/ACC-19_clean_room_pass.md) | High | The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass. |
| [ACC-20 — Clean-Room Reproduction Failure](../12_ACCEPTANCE_SCENARIOS/ACC-20_clean_room_fail.md) | Critical | G7 becomes FAIL/REVISE and the claim becomes `CHALLENGED`; an environment/data/code/stochastic/method root-cause classification is made and a controlled G4/G5 return is opened. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/WP-083_experiment_batch.md), [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Method Registry` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Protocol validators` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Amendment workflow` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Post-hoc change detector` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Run Registry` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Preflight validator` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `MLflow integration` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lineage queries` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lifecycle dashboard` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `ExperimentBatch workflow` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Staging policy` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Parameter manifest` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Checkpoint/recovery logic` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Batch report` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Clean-room platform` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Reproducer profile` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Environment resolver` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Isolation attestation` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Repro runbook` | `WP-084` | `python3 scripts/progress.py show WP-084` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Reproducibility Lead** carries the acceptance decision; **Assurance Lead / Statistician** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

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

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-085_repro_robustness_replication.tests.md`](WP-085_repro_robustness_replication.tests.md).

- Repeatability passing while reproducibility fails
- A robustness edge slice failing
- The replication-unavailable state
- Enforcement of a pre-declared tolerance
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-085_repro_robustness_replication.acceptance.md`](WP-085_repro_robustness_replication.acceptance.md), together with what this package still cannot establish.

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
