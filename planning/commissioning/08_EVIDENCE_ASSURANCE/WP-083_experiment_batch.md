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

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-083_experiment_batch.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-083_experiment_batch.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Experiments proceed smoke → baseline → small sweep → full run inside a controlled batch workflow governed by success, stop and budget criteria and by checkpoints.


## Analysis
### What this package actually decides

That compute is spent in increasing increments against declared criteria. Smoke →
baseline → small sweep → full run, with a promotion check between each stage.

The alternative is the common one: a full run is launched, it produces something,
and the question of whether it should have been launched is answered by the
result.

### Staged promotion is a budget control and a methodological one (T02)

The budget half is obvious. The methodological half is that a smoke run reveals a
broken pipeline before the full run's results make the pipeline seem fine — and a
baseline reveals that the effect being measured is present in the control.

### Fan-out caps prevent the failure mode with the worst cost profile (T03)

A parameter × seed matrix multiplies. `PR-09`'s early signal is *fan-out, retry,
token growth*, and a matrix that expands unchecked spends a quarter's compute
before anyone notices. The cap is declared before dispatch and the reservation is
taken up front (WP-053).

### Partial results are results and must be marked (T04)

A preempted batch has done real work. Discarding it wastes compute; presenting it
as complete is a misrepresentation. Marked partial, with the completed fraction
recorded, is the only honest option.

### The stop/pivot/negative decision is the point of the whole workflow (T06)

`00_PROGRAM/08`'s stop conditions and `00_PROGRAM/01`'s G5 invariant meet here.
The batch stops when a declared rule fires, and the three outcomes — stop, pivot,
negative result — are all legitimate completions.

A batch that can only succeed will always find a way to.

### The invariant that must not bend

**No agentic methodological discretion during a frozen execution.** A threshold
moved mid-batch because the result looks wrong is the failure, and the workflow
stops rather than adjusts.

### Baseline v1.2.0 — a population and a funnel, not a batch

This package grows from *run a batch of experiments* into the fidelity funnel and
its governor, which is the largest single change in this baseline.

**`DRAFT → SMOKE → VERIFY → FULL`**, with each promotion producing an
`ExperimentPromotionRecord` carrying the criteria snapshot, the values that
decided it and whether the decision was `MECHANICAL_POLICY` or `HUMAN`. Where the
criterion is computable, the decision is computed — a model may recommend and may
not promote past a threshold that refused (ACC-60). Under `CONFIRMATORY` study
mode the rule is non-waivable.

**Seed counts are a domain profile, not a constant.** Multiple independent seeds
at VERIFY and the preregistered official evaluator at FULL are requirements; the
specific numbers are an initial profile to calibrate.

**The governor** stops on cost, rounds, experiment count, compute or convergence
patience and emits a `CampaignStopRecord`. `STOPPED_BY_BUDGET` satisfies no gate:
a campaign that ran out of money has demonstrated nothing. Budget reserved for
VERIFY, FULL and G7 reproduction is unreachable from exploration, because a
campaign that spends its reproduction budget on search produces results nobody
can check.

**Intra-agent rigor and inter-agent transition guards** run at each handoff, so
that agent B cannot infer A succeeded from A's confident prose. Every check that
can be deterministic is.

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

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md) | `Policy Router` · `RouteDecision service` · `Fan-out/budget rules` · `Routing conformance suite` |
| [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md) | `Kueue configuration` · `Quota/priority policy` · `Budget admission adapter` · `Queue dashboard` |
| [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md) | `Sandbox profiles` · `Execution Cell controller` · `SandboxAttestation` · `Capture/destroy workflow` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |

### Full prerequisite closure

**52 of 160 packages (32%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-085` · `WP-104` · `WP-111` · `WP-145`
- **Transitively reachable:** **34 of 160 packages (21%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **30** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Scientific Engineering Lead |
| Independent verifier | Methodologist / FinOps / SRE |
| Gates touched | `G4` · `G5` |
| Controls | `CTL-CST-01` · `CTL-DAT-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-09 — Budget Hard Stop](../12_ACCEPTANCE_SCENARIOS/ACC-09_budget_hard_stop.md) | Critical | An 80% warning is raised; at 100% new expensive work is denied, the workflow pauses with state and checkpoints preserved, and no duplicate cost or reservation is created. |
| [ACC-33 — Kueue Preemption](../12_ACCEPTANCE_SCENARIOS/ACC-33_kueue_preemption.md) | High | The scout is checkpointed, paused or evicted and the critical reproduction is admitted; canonical task state and artifacts are not lost and the scout resumes later. |
| [ACC-39 — Negative Research Result](../12_ACCEPTANCE_SCENARIOS/ACC-39_negative_result.md) | Medium | The result is neither lost nor reframed as a success; a negative run and claim artifact, the limitations and a stop/pivot/continue `DecisionRecord` are produced. |
| [ACC-54 — Producer Attempts Evaluator Mutation](../12_ACCEPTANCE_SCENARIOS/ACC-54_evaluator_mutation_attempt.md) | Critical | Every write is denied at the policy and sandbox boundary and audited. If any write nonetheless lands, the evaluator digest mismatch invalidates the run and the scenario FAILs as a critical security defect. |
| [ACC-60 — Failed Smoke Candidate Promotion Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-60_failed_smoke_promotion.md) | Critical | Both promotions are refused. Under a CONFIRMATORY study mode the rule is non-waivable; where an exceptional path exists at all it requires an explicit authorised exception with an owner and an expiry, and it is recorded as one. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-045 — Policy Router and Minimum-Sufficient Model Package](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
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
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Policy Router` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `RouteDecision service` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Fan-out/budget rules` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Routing conformance suite` | `WP-045` | `python3 scripts/progress.py show WP-045` |
| `Kueue configuration` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Quota/priority policy` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Budget admission adapter` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Queue dashboard` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Sandbox profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Execution Cell controller` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `SandboxAttestation` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Capture/destroy workflow` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Red-team tests` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Four-zone isolation profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Run Registry` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Preflight validator` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `MLflow integration` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lineage queries` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lifecycle dashboard` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `RawEvaluatorArtifact` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `VerifiedValue` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `PredictionRecord` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `FailureAssessment` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `ModelExecutionFingerprint` | `WP-082` | `python3 scripts/progress.py show WP-082` |

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
- **Scientific Engineering Lead** carries the acceptance decision; **Methodologist / FinOps / SRE** must verify independently of whoever implements.
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
- `ExperimentPromotionRecord`
- `ResearchCampaignGovernor`
- `CampaignStopRecord`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-083_experiment_batch.tests.md`](WP-083_experiment_batch.tests.md).

- A smoke failure preventing the full run
- A hard budget stop preserving state
- Resume after a Kueue preemption
- Partial batch result semantics
- Closure of a negative result
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-083_experiment_batch.acceptance.md`](WP-083_experiment_batch.acceptance.md), together with what this package still cannot establish.

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
