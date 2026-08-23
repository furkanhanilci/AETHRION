---
title: "WP-082 — Run Registry and MLflow Lineage Integration"
aliases:
  - "WP-082"
  - "WP-082 — Run Registry and MLflow Lineage Integration"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A run is not admitted until the protocol, literature set, dataset, code, environment, prompt, model, seed, budget and execution attestation are complete; MLflow is only the tracking view."
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/state/not-started
---

# WP-082 — Run Registry and MLflow Lineage Integration

## Package card

| Field | Value |
|---|---|
| Work package | `WP-082` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Hard dependencies | WP-014, WP-019, WP-025, WP-026, WP-029, WP-032, WP-081 |
| Related gates | G4,G5 |
| Related controls | CTL-DAT-01, CTL-CST-01 |
| Related acceptance scenarios | ACC-39 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Workflow Run RO-Crate** for provenance · **MLflow + OpenTelemetry** for telemetry

The run record is emitted as a Process/Workflow/Provenance Run Crate — machine-actionable, engine-independent, PROV-O mapped. MLflow answers *what did the system do*; the crate plus a signed `EvidenceManifest` answers *what may be believed*. **Operational telemetry is never the scientific truth store.**

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_082_run_registry_mlflow.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_082_run_registry_mlflow.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A run is not admitted until the protocol, literature set, dataset, code, environment, prompt, model, seed, budget and execution attestation are complete; MLflow is only the tracking view.


## Analysis
### What this package actually decides

That a run is not admitted until its manifest is complete. The purpose sentence
names the ten required elements and the demotion: *MLflow is only the tracking
view.*

That demotion is the package's architectural content. A tracking server that
becomes the run's system-of-record is a canonical-ownership defect (`PR-03`), and
it makes the run's provenance depend on a tool the programme adopted rather than
on a contract it controls.

### Admission before execution, not validation after (T02)

A run whose manifest is completed retrospectively has provenance assembled from
memory. Checking completeness **at admission** means the missing field is found
when it costs nothing, and it is what makes WP-019's rule enforceable: *a run whose
manifest is incomplete can never support a confirmatory claim.*

### Hash validation on ingestion (T04)

Metrics and artifacts arrive from the execution fabric. Validating that the
artifact hash matches what the run manifest declared is what stops a result being
attributed to a run that did not produce it — accidentally or otherwise.

### Failed, cancelled and negative runs are three different things (T05)

- **Failed** — the run did not complete; it has no result.
- **Cancelled** — a human or a control stopped it; it may have partial results.
- **Negative** — it completed and the result did not support the hypothesis.

The third is a scientific result and must be as recordable and as citable as a
positive one. `PR-19` — publication bias survives the gate structure — starts with
a system that makes negative results awkward to store.

### Run comparison is what makes reproduction assessable (T06)

Two runs, one manifest difference. The comparison API is what a reproducer uses to
say *these differ only in environment*, and what a reviewer uses to check that
claim.

### Baseline v1.2.0 — where a number comes from, and why a run failed

Four records the run registry does not currently hold:

**`RawEvaluatorArtifact`** — the evaluator's output stored immutably **before any
agent interprets it**, with the evaluator code digest, the dataset snapshot and
the environment digest. The ordering is the mechanism: if an agent summarises
first, the record of what happened is a paraphrase by an interested party.

**`VerifiedValue`** — a published number as a typed record with its metric
definition, aggregation, seed set, uncertainty and scope. It cannot be rebound to
a different raw output; a recomputation creates a successor — ACC-77.

**`PredictionRecord`** — what an actor predicted before the outcome, scored
against it afterwards. Aggregated per actor, model, task class and domain — a
single global reliability number is the most misleading form this could take.

**`FailureAssessment`** — `IMPLEMENTATION`, `METHODOLOGY`, `DATA`, `HYPOTHESIS`,
`INFRASTRUCTURE`, `POLICY`, `UNKNOWN`. Only a validly executed run under the
frozen plan can support `HYPOTHESIS`. A compile error classified as a refuted
hypothesis is the single most damaging record this system could produce, and
ACC-64 exists to make it impossible.

MLflow remains operational observability. It answers what the system did; it is
never where a scientific result lives.

### Baseline v1.3.0 — the assurance layer stops using one word for two things

Three changes, and the first is a vocabulary correction with real consequences.

**"Mechanical verifier" is retired as a broad term.** It becomes V0 deterministic
· V1 computational · V2 qualified semantic · V3 human (`ADR-008`), and the class
is assigned by the verifier service from the procedure that actually ran — never
by the caller. The reason is that the gate rule *a mechanical check cannot be
overridden by a model* is correct for V0 and V1 and absurd at V2, where it says a
model's judgement cannot be overridden by a model.

**Assurance becomes routed** (`ADR-015`): by consequence and uncertainty rather
than uniformly, with a cascade to a stronger independent verifier or to a human,
and with `ABSTAIN` as a valid verdict that escalates. A route cannot be lowered
because the queue is long or the budget is tight.

**Three hard bindings** into the evidence and publication path:

- **Specification conformance** — the frozen method and the running code are
  compared, and an unapproved `SCIENTIFIC_MAJOR` deviation cannot carry a
  confirmatory package forward (`ADR-018`, ACC-104).
- **Model execution fingerprint** — every invocation contributing to a result
  records what actually executed, retry and fallback history included, and a
  hosted black-box model does not yield an `EXACT` reproduction claim
  (ACC-115, ACC-116).
- **Publication compiler** — no prose without a claim, no number without a
  `VerifiedValue`, and a complete evidence chain checked link by link
  (ACC-105, ACC-106).

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

7, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-029 — MLflow Experiment and Evaluation Tracking Foundation](../03_FOUNDATION/wp_029_mlflow_foundation.md) | `MLflow deployment` · `Run naming/tag policy` · `Access controls` · `Tracking SDK wrapper` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md) | `Method Registry` · `Protocol validators` · `Amendment workflow` · `Post-hoc change detector` |

### Full prerequisite closure

**49 of 160 packages (31%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |

### What acceptance of this package releases

- **Directly unblocked:** 14 — `WP-083` · `WP-084` · `WP-085` · `WP-086` · `WP-087` · `WP-090` · `WP-095` · `WP-096` · `WP-099` · `WP-100` · `WP-104` · `WP-107` · `WP-144` · `WP-152`
- **Transitively reachable:** **62 of 160 packages (39%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **29** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Gates touched | `G4` · `G5` |
| Controls | `CTL-DAT-01` · `CTL-CST-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-39 — Negative Research Result](../12_ACCEPTANCE_SCENARIOS/acc_39_negative_result.md) | Medium | The result is neither lost nor reframed as a success; a negative run and claim artifact, the limitations and a stop/pivot/continue `DecisionRecord` are produced. |
| [ACC-53 — Unverified Numeric Result](../12_ACCEPTANCE_SCENARIOS/acc_53_unverified_numeric_result.md) | Critical | The build fails regardless of the quality of the surrounding prose; the report lists the value refs that were permitted and the one that was not. A declared rounding or display transform of a registered value passes. |
| [ACC-63 — Failed Experiment Must Be Recorded](../12_ACCEPTANCE_SCENARIOS/acc_63_failed_experiment_recorded.md) | High | It cannot advance until an immutable `ExperimentRun`, a `FailureAssessment` and a `FailedApproach` record exist, carrying the logs and artifacts the failure produced. |
| [ACC-64 — Implementation Failure Must Not Refute a Hypothesis](../12_ACCEPTANCE_SCENARIOS/acc_64_implementation_failure_not_refutation.md) | Critical | Both are classified — IMPLEMENTATION and DATA — and any transition that would set `HYP-002` to REFUTED is refused. Only a validly executed run under the frozen plan can support a HYPOTHESIS failure class. |
| [ACC-77 — VerifiedValue Rebinding Attempt](../12_ACCEPTANCE_SCENARIOS/acc_77_verified_value_rebinding.md) | Critical | Both are refused. The binding is immutable and digest-checked; a changed evaluation produces a new value, and a tampered raw artifact fails its digest. |
| [ACC-095 — Failure Taxonomy Routing](../12_ACCEPTANCE_SCENARIOS/acc_095_failure_taxonomy_routing.md) | High | Each reaches its owning discipline. A `HYPOTHESIS` class is reachable only from a validly executed run under the frozen plan — the other classes cannot produce it however the run failed. |
| [ACC-106 — A Number Without a VerifiedValue](../12_ACCEPTANCE_SCENARIOS/acc_106_numeric_value_without_verifiedvalue.md) | Critical | The build fails and names the ungrounded figure. A registered value passes, and a declared rounding of a registered value passes and records its display transform. |
| [ACC-115 — Missing Model Execution Fingerprint](../12_ACCEPTANCE_SCENARIOS/acc_115_missing_model_execution_fingerprint.md) | Critical | An invocation without a complete fingerprint fails the run. The failover appears in the fingerprint's retry and fallback history and invalidates any `EXACT` claim. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-029 — MLflow Experiment and Evaluation Tracking Foundation](../03_FOUNDATION/wp_029_mlflow_foundation.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md)
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
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `CandidateWorkspace` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionPackage` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ClaimConsistencyReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `MLflow deployment` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Run naming/tag policy` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Access controls` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Tracking SDK wrapper` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `Restore procedure` | `WP-029` | `python3 scripts/progress.py show WP-029` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Method Registry` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Protocol validators` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Amendment workflow` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Post-hoc change detector` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `SpecificationConformanceRecord binding` | `WP-081` | `python3 scripts/progress.py show WP-081` |

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
- **Experiment Platform Lead** carries the acceptance decision; **Reproducibility Engineer** must verify independently of whoever implements.
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
| `ASM-004` — Scholar Loop — SMOKE / VERIFY / FULL fidelity funnel | `ADAPTIVE_REIMPLEMENT` | `MS-FUN-001` · `MS-FUN-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `CMP-017` — MLflow | `DEPENDENCY` | Experiment tracking, parameter/metric storage and the tracking UI. | The Run Registry, the preflight validator and the binding from a run to a `RawEvaluatorArtifact` and a `VerifiedValue`. | **2** |
| `CMP-022` — Workflow Run RO-Crate | `STANDARD` | The crate format and its PROV mapping. | Which run facts must be present for a run to be re-executable by someone who was not there. | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-004` | An ExperimentPromotionRecord is a mechanical policy decision where the criteria are computable. A model may not promote a candidate a threshold refused. | The monolithic orchestrator the funnel is spread across, and the upstream seed counts as universal law — 3-seed VERIFY and 5-seed FULL are an initial profile to calibrate, not a constant. |
| `CMP-017` | MLflow answers *what did the system do*. It never answers *what may be believed* — that is a signed `EvidenceManifest` plus Workflow Run RO-Crate. Operational telemetry is not provenance, and an MLflow metric is not a `VerifiedValue`. | MLflow as the scientific truth store, and its model registry as the admission authority. |
| `CMP-022` | A crate records what ran. It does not assert that the result supports a claim; that binding is the `EvidenceManifest`'s. | Any AETHRION-specific run format that would fork the standard. |

### Where a plain row would mislead

- **`ASM-004`** — Reimplemented rather than adapted because the logic is not isolated in one module upstream.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-004` — Scholar Loop — SMOKE / VERIFY / FULL fidelity funnel** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`CMP-017` — MLflow** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 3 obligations open across 2 of 3 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-082-T01 | Establish the Run Registry state model and API | Implementation owner | Commit / configuration / record reference |
| WP-082-T02 | Write the pre-run manifest completeness and admission checks | Implementation owner | Commit / configuration / record reference |
| WP-082-T03 | Bind Temporal, execution and MLflow correlation | Implementation owner | Commit / configuration / record reference |
| WP-082-T04 | Add metric, artifact and result ingestion with hash validation | Implementation owner | Commit / configuration / record reference |
| WP-082-T05 | Define the failed, cancelled and negative run lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-082-T06 | Add run comparison, query APIs and outbox events | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Run Registry`
- `Preflight validator`
- `MLflow integration`
- `Run lineage queries`
- `Run lifecycle dashboard`
- `RawEvaluatorArtifact`
- `VerifiedValue`
- `PredictionRecord`
- `FailureAssessment`
- `ModelExecutionFingerprint`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-082_run_registry_mlflow.tests.md`](wp_082_run_registry_mlflow.tests.md).

- Denial when a dataset, image or model reference is missing
- End-to-end run identifier correlation
- A failed run whose artifacts are retained
- Queued ingest during an MLflow outage
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-082_run_registry_mlflow.acceptance.md`](wp_082_run_registry_mlflow.acceptance.md), together with what this package still cannot establish.

- [ ] No run starts with incomplete metadata.
- [ ] MLflow never owns canonical workflow or artifact state.
- [ ] A negative result is a first-class run outcome.
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

A tracking failure does not lose execution evidence; an idempotent backfill runs and no invalid run is published.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
