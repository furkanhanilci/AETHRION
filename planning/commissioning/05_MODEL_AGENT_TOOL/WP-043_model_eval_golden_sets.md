# WP-043 — Role-Based Model and **Skill** Evaluation, and Golden Set Management

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
| Related acceptance scenarios | ACC-07, ACC-37, ACC-48, ACC-49 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Inspect AI** — encode behaviours as tasks and scorers, do not build an evaluation engine

Inspect's `Dataset → Solver → Scorer` model, sandboxing, limits, retry/resume and transcripts are what skill-behaviour testing needs, and it can drive real agent harnesses as evaluation subjects. The contribution of this package is the behaviours and their pass criteria, not the runner.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-043_model_eval_golden_sets.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-043_model_eval_golden_sets.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Contamination-protected, versioned evaluation sets and measurement rubrics are built for the planner, scout, extractor, coder, reviewer and arbiter roles.


## Analysis
### What this package actually decides

Whether the laboratory can measure the things it depends on. This is the largest
package in the workstream and it carries two jobs that are usually separate:
**model evaluation** (T01–T06) and **skill behaviour testing** (T20–T25).

The second is here because of a specific, recorded gap.

### The largest untested claim in the repository

`docs/STATUS.md` states it every run: *skills conform to a format; none has a
behaviour baseline.* `tests/README.md` calls it **the largest untested claim in
the repository**. Fifty-two skills are validated for structure by
`scripts/validate_skills.py` and **none has ever been shown to change what an
agent does.**

T20 is the answer and its design is the important part: run the scenario
**without** the skill and capture the failure **verbatim**. That is a RED
baseline. Without it, a skill that changes nothing passes, because the agent would
have done the right thing anyway.

### Observed rationalizations, not anticipated ones (T21)

The distinction is sharp and easy to lose. An anticipated rationalization table is
what an author imagines a model will say to avoid a rule. An observed one is what
it actually said. They differ, and only the second is evidence — the first is a
guess that will be treated as a finding.

### Pressure scenarios are where discipline actually fails (T22)

Time pressure, authority pressure, sunk cost, partial success, "just this once".
A skill that holds under calm conditions and yields under pressure has not been
tested where it matters, and every one of those five is a real research-integrity
failure mode with a literature behind it.

### Trigger resolution and survival (T23, T24)

Right skill, wrong skill, no skill, two competing skills — four outcomes, and only
the first is success. And a skill that is loaded and then lost to context
compaction has produced a run whose discipline changed halfway through, which is
undetectable in the output.

### Contamination is the control that protects everything else (T03)

`PR-15`. A golden set that has appeared in a prompt or a trace measures memory,
not capability, and the metric improves — which is why nobody investigates. The
canary is what makes contamination detectable rather than assumed absent.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

7, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-029 — MLflow Experiment and Evaluation Tracking Foundation](../03_FOUNDATION/WP-029_mlflow_foundation.md) | `MLflow deployment` · `Run naming/tag policy` · `Access controls` · `Tracking SDK wrapper` |
| [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md) | `Capability Registry service` · `Profile state machine` · `Eligibility API` · `Expiry/revoke scheduler` |

### Full prerequisite closure

**26 of 141 packages (18%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 15 | `WP-021` |
| 16 | `WP-025` · `WP-026` |
| 17 | `WP-029` · `WP-041` |
| 18 | `WP-042` |

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-044` · `WP-088` · `WP-124` · `WP-126`
- **Transitively reachable:** **93 of 141 packages (66%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **19** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Eval Office |
| Independent verifier | Independent Domain/Assurance Reviewer |
| Gates touched | `Platform` · `G6` |
| Controls | `CTL-MOD-01` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-07 — Reviewer Order Bias](../12_ACCEPTANCE_SCENARIOS/ACC-07_reviewer_order_bias.md) | High | A material order effect fails the profile's calibration; the reviewer is not admitted to a critical role, or is suspended from it. |
| [ACC-37 — Evaluation Set Contamination](../12_ACCEPTANCE_SCENARIOS/ACC-37_eval_contamination.md) | Critical | The evaluation bundle is invalidated; the qualification and profile decisions that depended on it are suspended, and a clean set and re-evaluation process opens. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-029 — MLflow Experiment and Evaluation Tracking Foundation](../03_FOUNDATION/WP-029_mlflow_foundation.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md)
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
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `MLflow deployment` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Run naming/tag policy` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Access controls` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Tracking SDK wrapper` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Restore procedure` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Capability Registry service` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Profile state machine` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eligibility API` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Expiry/revoke scheduler` | `WP-042` | `python3 scripts/progress.py show WP-042` |

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
- **Eval Office** carries the acceptance decision; **Independent Domain/Assurance Reviewer** must verify independently of whoever implements.
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
| WP-043-T01 | Derive the role-specific capability and failure taxonomy | Implementation owner | Commit / configuration / record reference |
| WP-043-T02 | Prepare the golden, adversarial and regression sets | Implementation owner | Commit / configuration / record reference |
| WP-043-T03 | Establish dataset split, access, canary and contamination controls | Implementation owner | Commit / configuration / record reference |
| WP-043-T04 | Calibrate the deterministic graders and the human rubrics | Implementation owner | Commit / configuration / record reference |
| WP-043-T05 | Add validated-precision, incremental-finding, cost, triage and latency metrics | Implementation owner | Commit / configuration / record reference |
| WP-043-T06 | Write the evaluation manifest and its release process | Implementation owner | Commit / configuration / record reference |
| WP-043-T20 | Build the **skill behaviour baseline (RED) harness**: run the scenario *without* the skill and capture the failure verbatim | Implementation owner | Baseline transcripts per skill |
| WP-043-T21 | Capture **rationalizations verbatim** and replace every anticipated rationalization table with observed ones | Implementation owner | Diff of anticipated → observed tables |
| WP-043-T22 | Write **pressure scenarios**: time pressure, authority pressure, sunk cost, partial success, "just this once" | Implementation owner | Pressure transcripts + verdicts |
| WP-043-T23 | Test **trigger resolution**: right skill, wrong skill, no skill, two competing skills | Implementation owner | Trigger confusion matrix |
| WP-043-T24 | Test **skill survival**: context compaction, session restart, long-run drift | Implementation owner | Recovery transcripts |
| WP-043-T25 | Run **cross-model and cross-harness** compliance for every non-waivable skill | Implementation owner | Compliance matrix per model × harness |

### What "skill evaluation" means here

Format conformance is checked by `scripts/validate_skills.py` and is **not**
evaluation. This package answers the questions that script explicitly does not:

| Question | Failure it catches |
|---|---|
| Does the agent load the skill in the situation the trigger describes? | The skill exists and is never reached |
| Does loading it change behaviour? | Decorative procedure |
| Does it hold under pressure? | Compliance that evaporates when it costs something |
| What does the agent say while evading it? | The rationalization table, which is the only defence a non-waivable rule has |
| Does the procedure survive compaction and restart? | Silent loss of governance mid-run |

**A skill without an observed baseline is not `ACCEPTED`**, regardless of how
well written it is.

## Mandatory deliverables

- `Eval dataset manifests`
- `Role eval harness`
- `Grader/rubric bundle`
- `Contamination controls`
- `Eval scorecard`
- `Skill behaviour baseline harness` and the per-skill RED transcripts
- `Observed rationalization tables` replacing the anticipated ones
- `Pressure`, `trigger` and `survival` scenario suites
- `Cross-model × cross-harness compliance matrix`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-043_model_eval_golden_sets.tests.md`](WP-043_model_eval_golden_sets.tests.md).

- Known-answer and edge-case validation
- Inter-rater calibration
- A negative access test against golden items
- Order, verbosity and self-preference bias probes
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-043_model_eval_golden_sets.acceptance.md`](WP-043_model_eval_golden_sets.acceptance.md), together with what this package still cannot establish.

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
