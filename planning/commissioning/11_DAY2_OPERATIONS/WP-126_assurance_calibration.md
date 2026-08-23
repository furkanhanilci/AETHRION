# WP-126 — Reviewer, Judge and Reproducer Calibration

## Package card

| Field | Value |
|---|---|
| Work package | `WP-126` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Eval Office / Independent Human Reviewer |
| Hard dependencies | WP-007, WP-043, WP-085, WP-086, WP-087, WP-088, WP-089, WP-113, WP-121 |
| Related gates | G6,G7,Day-2 |
| Related controls | CTL-GOV-02, CTL-EPI-04 |
| Related acceptance scenarios | — a Day-2 rhythm is exercised in operation, not as a go-live gate |
| Recurring counterpart of | ACC-07, ACC-08, ACC-38 — those scenarios verify the **initial** qualification before cutover; this package owns the **recurring** one afterwards |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-126_assurance_calibration.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-126_assurance_calibration.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Reviewer precision, disagreement, order/identity/verbosity bias, false positives, escaped defects and reproducer consistency are measured on a schedule against golden and counter-tests.


## Analysis
### What this package actually decides

Whether the laboratory's own reviewers are any good. This is the package that
closes — or at least measures — the largest unmeasured assumption in the whole
programme.

### `PR-16` is this package's reason for existing

*Independence is assumed, never measured.* `PR-05` addresses **paper** independence:
different human, different model family, different credential. It says nothing about
whether two genuinely different reviewers make **correlated errors** — and if they
do, every independence claim in the system is weaker than it reads.

`00_PROGRAM/10`'s go-live condition names it directly: *independence measured, not
assumed — pairwise error correlation measured for the reviewer pool.*

### Validated precision is the metric that matters (T03)

Not how many findings a reviewer raised. How many survived arbitration and
reproduction. A reviewer producing many findings that never survive is producing
noise that consumes the scarcest resource in the system.

Recall matters too and is harder: it needs **hidden counter-tests** — known defects
the reviewer was not told about.

### Three biases, each measurable (T02)

**Order** — does verdict change with finding order? WP-088 randomises; this measures
whether the randomisation was necessary.
**Identity** — does a reviewer's verdict change when they can infer the producer?
**Verbosity** — does a longer, more confident submission get an easier verdict?

The third is the one most specific to model reviewers and the least often tested.

### Blind leakage audit (T02)

WP-086 redacts. This measures whether the redaction held — by checking whether
reviewers' verdicts correlate with producer identity they should not have had.

### Reviewer profiles expire (T04)

Same discipline as model admission. A reviewer qualified once stays qualified
unless something forces re-examination, and reviewers drift for the same reasons
models do.

### Baseline v1.2.0 — verifiers are calibrated too, and separately

This package covers reviewers, judges and reproducers. **Verifiers** are added,
and their record is deliberately a different one.

A reviewer is a scientific role, measured on agreement, decision accuracy against
controls, confidence calibration and order effects. A verifier is a bounded check,
measured on precision, recall, specificity and false positive and negative rates
against a labelled evaluation set. The same model may serve both; the records stay
separate because they answer different questions.

`VerifierQualificationRecord` is keyed by **verifier + version + task type +
domain profile + threshold**. All five: citation entailment, method–code alignment
and novelty grading are different tasks, and a threshold change on the same
version invalidates the qualification, because the threshold is part of what was
measured.

**Independence is measured, not configured.** Two verifiers from different
providers may share training sources, prompt ancestry, retrieved evidence or a
misreading of a specification. Error correlation between verifier families is
tracked on shared control sets rather than inferred from the provider name.

### Baseline v1.3.0 — Day-2 measures what this baseline added

The recurring rhythms gain six subjects, each of which is a number that only
means something when tracked over time:

- **Multi-agent efficiency** — coordination overhead against the naive
  fully-connected baseline, and whether the optimisation still holds.
- **Verifier calibration** — precision, recall, **abstention rate** and error
  correlation between verifier families, requalified on a schedule.
- **Source and upstream drift** — pinned mechanisms whose upstream moved, and
  sources whose status changed.
- **Supply-chain posture** — OSV and Scorecard findings, and residual risks that
  reached their expiry.
- **Failure taxonomy distribution** — including how often attribution returned
  `UNKNOWN`, which is a system-health signal rather than a defect count.
- **The Pareto frontier** — quality against cost, so an optimisation that stopped
  paying is visible.

Incident learning consumes the typed `FailureAssessment` and retains negative
results. A failed approach that is deleted is a lesson the next campaign pays for
again.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

10, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management](../05_MODEL_AGENT_TOOL/WP-043_model_eval_golden_sets.md) | `Eval dataset manifests` · `Role eval harness` · `Grader/rubric bundle` · `Contamination controls` |
| [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md) | `Verification pipeline` · `Type-specific protocols` · `Robustness matrix` · `Reproduction certificates` |
| [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md) | `Review Package Builder` · `Blind/redaction rules` · `Package manifests` · `Leak detection tests` |
| [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md) | `Verification Engine` · `Validator catalog` · `VerificationRecord service` · `Regression fixtures` |
| [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md) | `Review service` · `Assignment/eligibility engine` · `Review rubrics` · `ReviewRecord storage` |
| [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md) | `Disagreement service` · `Arbitration rubric` · `Disposition workflow` · `Appeal/decision integration` |
| [WP-113 — Evidence, Reproduction and Publication Acceptance Package](../10_INTEGRATION_CUTOVER/WP-113_evidence_repro_acceptance.md) | `Evidence/repro scenario results` · `Reproduction certificates` · `Lineage/integrity reports` · `Assurance sign-off` |
| [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md) | `Hypercare log` · `Incident/finding summary` · `Production KPI baseline` · `Day-2 handoff` |
| [WP-155 — Adaptive Assurance, Verifier Qualification and Escalation](../15_RELIABILITY_EFFICIENCY/WP-155_adaptive_assurance_and_escalation.md) | `Assurance router` · `Cascade and escalation path` · `Abstention verdicts` · `Extended VerifierQualificationRecord` |

### Full prerequisite closure

**123 of 160 packages (77%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-039` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-048` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-040` · `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-060` · `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` · `WP-154` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` · `WP-155` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |
| 47 | `WP-110` · `WP-111` · `WP-112` · `WP-113` · `WP-114` |
| 48 | `WP-115` |
| 49 | `WP-116` · `WP-117` |
| 50 | `WP-118` |
| 51 | `WP-119` |
| 52 | `WP-120` |
| 53 | `WP-121` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-130`
- **Transitively reachable:** **1 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W9 — Day-2 |
| Dependency depth | level **54** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Assurance Lead |
| Independent verifier | Eval Office / Independent Human Reviewer |
| Gates touched | `G6` · `G7` · `Day-2` |
| Controls | `CTL-GOV-02` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/WP-043_model_eval_golden_sets.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-113 — Evidence, Reproduction and Publication Acceptance Package](../10_INTEGRATION_CUTOVER/WP-113_evidence_repro_acceptance.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
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
| `Evaluator and memory-context independence constraints` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Cohort independence dimensions` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eval dataset manifests` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Role eval harness` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Grader/rubric bundle` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Contamination controls` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Eval scorecard` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Cross-model × cross-harness compliance matrix` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Verification pipeline` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Type-specific protocols` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Robustness matrix` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Reproduction certificates` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Failure taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `AlgorithmUnderstandingRecord` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ReproductionPackage` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ClaimConsistencyReport` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Five-level reproduction taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Review Package Builder` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Blind/redaction rules` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Package manifests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Leak detection tests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Verification Engine` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Validator catalog` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerificationRecord service` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Regression fixtures` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `V0-V3 verification routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerifierQualificationRecord` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Positive and negative control suite` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Adaptive assurance routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Abstention verdicts` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Review service` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Assignment/eligibility engine` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Review rubrics` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `ReviewRecord storage` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Calibration dashboard` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Disagreement service` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Arbitration rubric` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Disposition workflow` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Appeal/decision integration` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Evidence/repro scenario results` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Reproduction certificates` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Lineage/integrity reports` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Assurance sign-off` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Hypercare log` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Incident/finding summary` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Production KPI baseline` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Day-2 handoff` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Program closure report` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Assurance router` | `WP-155` | `python3 scripts/progress.py show WP-155` |
| `Cascade and escalation path` | `WP-155` | `python3 scripts/progress.py show WP-155` |
| `Abstention verdicts` | `WP-155` | `python3 scripts/progress.py show WP-155` |
| `Extended VerifierQualificationRecord` | `WP-155` | `python3 scripts/progress.py show WP-155` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Assurance Lead** carries the acceptance decision; **Eval Office / Independent Human Reviewer** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation acquisition and assimilation

<!-- generated:implementation-sources — produced by scripts/expand_acquisition.py; do not edit inside this block -->

**What is already solved elsewhere, and on what terms.** Before the first task starts, an implementer has to know which parts of this package are called at runtime, which are copied and refactored, which are reimplemented from a specification, and which have no upstream at all. Those decisions are recorded in [`provenance/upstreams.json`](../../../provenance/upstreams.json) — mechanisms assimilated into this repository's own code — and in [`provenance/components.json`](../../../provenance/components.json) — components adopted at runtime. This block is derived from both, so a decision and the place it is used cannot drift apart.

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-003` — Scholar Loop — predict-then-verify calibration | `DIRECT_ADAPT` | `scholarloop/calibration.py` | the local module and contract surface this becomes — **named at refinement** | **3** |
| `ASM-024` — PaperBench — producer / reproducer / grader separation and JudgeEval | `PATTERN` | the idea only — no code and nothing called at runtime | everything — the implementation here is this repository's own | none |
| `ASM-028` — CORE-Bench — computational reproducibility agent benchmark | `BENCHMARK` | a measurement of this system — nothing enters it | the contract this is held behind | none |
| `ASM-029` — AstaBench — cost-controlled scientific agent benchmark suite | `BENCHMARK` | a measurement of this system — nothing enters it | the contract this is held behind | none |
| `ASM-046` — Trust or Escalate — cascaded selective evaluation | `ADAPTIVE_REIMPLEMENT` | `MS-ASSUR-001` · `MS-ASSUR-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `CMP-033` — krippendorff · statsmodels · scikit-learn | `DEPENDENCY` | The estimators. | Which estimator answers which question, and the decision rule written before the data is seen. | **2** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-003` | A calibration profile qualifies an actor for a task class. It is not a claim confidence and cannot be attached to a ClaimVersion. | The two-kind prediction vocabulary — AETHRION needs DIRECTIONAL_DELTA, CONTINUOUS, BINARY, PROBABILITY and RANKING — and the in-memory list as the store of record. |
| `ASM-024` | A benchmark measures the system and never gates it. JudgeEval measures the grader, which is why a grader's verdict needs its own qualification record. | The runtime as an embedded dependency. |
| `ASM-028` | Measures G7a; never gates it. | Any runtime dependency. |
| `ASM-029` | Qualification evidence for a model or actor profile on a task class. Never a gate. | Its agent implementations. |
| `ASM-046` | A cascade decides which verifier answers. It cannot decide that a claim is true, and a coverage guarantee is not a substitute for human authority at G8. | The framing of a statistical human-agreement guarantee as sufficient. Selective evaluation reports the fraction of cases it is willing to judge at a target agreement level; that is a useful property and it is not scientific authority. |
| `CMP-033` | An agreement coefficient measures agreement, not correctness. Two reviewers who agree may both be wrong, and a high coefficient is never evidence that a verdict is right. | An estimator chosen after seeing the result — `preregistration-discipline` forbids it. |

### Where a plain row would mislead

- **`ASM-003`** — Actor calibration and verifier qualification are separate records here, because they answer different questions.
- **`ASM-024`** — Already registered as PATTERN + BENCHMARK in AETHRION_COMPONENT_REUSE.md §4.
- **`ASM-028`** — Not in the source brief; added here. 270 tasks over 90 papers across computer science, social science and medicine, at three difficulty levels, including vision-language tasks. It is the oldest and most-cited of the reproduction benchmarks and covers disciplines the others do not, which is why the G7 suite should not consist only of 2026 preprints.
- **`ASM-029`** — Not in the source brief; added here. Eleven benchmarks and over 2,400 examples spanning literature search, code execution, data analysis and end-to-end discovery, with standardised tools, a date-restricted literature corpus for reproducibility, and explicit control for model cost and tool access. That last property is what the rest of the benchmark portfolio lacks: without cost normalisation, a governed-versus-ungoverned comparison cannot separate the effect of governance from the effect of spend.
- **`ASM-046`** — Uses judge confidence to escalate uncertain cases from a cheap judge to a stronger one, reporting roughly 80% coverage at an 80% human-agreement target. The mechanism taken is the cascade and, more importantly, **abstention as a first-class outcome** — ADR-015. A judge forced to choose on a case it cannot resolve produces a verdict indistinguishable from a confident one.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-003` — Scholar Loop — predict-then-verify calibration** · `DIRECT_ADAPT` · status `PROPOSED`

- the register entry moved to `CHARACTERIZED` — upstream behaviour captured and the adaptation confirmed against the pinned tree, not against the paper
- a pinned upstream commit — a branch name is not a pin
- a characterisation suite capturing upstream behaviour **before** any code moves

**`ASM-046` — Trust or Escalate — cascaded selective evaluation** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`CMP-033` — krippendorff · statsmodels · scikit-learn** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 6 obligations open across 3 of 6 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-126-T01 | Run the calibration set and hidden counter-tests periodically | Implementation owner | Commit / configuration / record reference |
| WP-126-T02 | Audit order swaps and blind/unblind leakage | Implementation owner | Commit / configuration / record reference |
| WP-126-T03 | Compute validated precision and recall, disagreement rates and triage time | Implementation owner | Commit / configuration / record reference |
| WP-126-T04 | Establish reviewer and reproducer profile expiry and suspension | Implementation owner | Commit / configuration / record reference |
| WP-126-T05 | Correct rubrics, training and bundles, then requalify | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Calibration reports`
- `Reviewer capability decisions`
- `Bias/quality dashboard`
- `Improvement actions`
- `VerifierQualificationRecord`
- `Verifier and reviewer error correlation measurement`
- `Abstention-rate and error-correlation calibration`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-126_assurance_calibration.tests.md`](WP-126_assurance_calibration.tests.md).

- Order bias
- Identity leakage
- A strong counter-test
- A false-positive reproducer
- A correlated miss across model families
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-126_assurance_calibration.acceptance.md`](WP-126_assurance_calibration.acceptance.md), together with what this package still cannot establish.

- [ ] More reviewers is never assumed to mean higher quality.
- [ ] A calibration failure suspends eligibility for the critical role.
- [ ] Human and model reviewers are measured against the same evidence rubric.
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

A failed reviewer profile is suspended; open reviews receive an impact assessment and reassignment.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
