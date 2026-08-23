# WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence

## Package card

| Field | Value |
|---|---|
| Work package | `WP-104` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Scientific Engineering Lead |
| Independent verifier | Methodologist / Evidence Auditor |
| Hard dependencies | WP-035, WP-054, WP-075, WP-076, WP-077, WP-078, WP-079, WP-080, WP-081, WP-082, WP-083, WP-095, WP-096, WP-097, WP-100 |
| Related gates | G4,G5 |
| Related controls | CTL-DAT-01, CTL-EPI-01, CTL-CST-01 |
| Related acceptance scenarios | ACC-08, ACC-09, ACC-23, ACC-32, ACC-39 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-104_vertical_slice_run_claim.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-104_vertical_slice_run_claim.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A staged run executes from the frozen protocol, literature set and baseline; the result becomes artifacts, evidence spans and a claim dependency and assessment chain.


## Analysis
### What this package actually decides

Whether a run becomes a claim without losing its provenance. This slice runs the
staged experiment (WP-083), captures artifacts, extracts evidence, anchors it,
audits the citations and builds the claim — then asks the question that matters:
**can the claim be traced back in one query?**

`00_PROGRAM/01` invariant 1, tested rather than asserted.

### The negative-result path is explicitly in scope (T05)

The sub-task names it, and it is the half a demonstration would skip. A run that
does not support the hypothesis must produce a first-class, citable negative result
(WP-082) and a claim whose state reflects it — not a quietly discarded batch.

`PR-19` starts with a system that makes negative results awkward.

### Correlation across five subsystems is the real test (T03)

Model call, tool call, sandbox execution, artifact, cost. Each is instrumented by a
different package, and a single missing propagation breaks the chain at exactly the
point where an auditor would look. WP-096's completeness SLO is what catches it.

### The citation audit runs here, before publication (T04)

WP-080's audit is a G9 blocker, but running it at claim construction is what makes
it cheap. A sentence whose span does not support it, found at G9, means the claim
is re-argued at the last gate.

### The lineage query is the acceptance test for the whole slice (T06)

Cockpit, graph and audit ledger must all return the same chain. Three views, one
answer — and any divergence is a canonical-ownership defect (`PR-03`).

### Baseline v1.3.0 — the slices exercise the cohort, and the regression injects faults

The vertical slices and the cutover path grow to cover what this baseline adds,
and one package changes character.

**WP-107 becomes the engineering completion slice.** Requirement and
specification → worktree → TDD → code review → CI → supply-chain attestation →
signed artifact → **eligibility to produce scientific evidence**. That last arrow
is the junction between the two disciplines, and before this baseline nothing
proved it end to end.

**The other slices exercise the collaboration plane**: a compiled cohort, sealed
initial positions, typed delta exchange over a sparse topology, an adaptive
assurance route, a fingerprinted reproduction and a firewalled benchmark run.

**The regression suite gains injections rather than cases.** Faulty agent,
malicious agent, split brain, duplicate and out-of-order events, communication
degradation under budget pressure, and benchmark contamination. These are
failures that are invisible in a healthy run and obvious only in a post-mortem,
which is why they are caused deliberately rather than waited for.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

15, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md) | `Sandbox profiles` · `Execution Cell controller` · `SandboxAttestation` · `Capture/destroy workflow` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md) | `Anchor resolver` · `Format adapters` · `Re-anchor queue` · `Anchor regression corpus` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md) | `Extraction pipeline` · `Extraction schemas` · `Evidence candidate store` · `Second-pass review queue` |
| [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md) | `SourceTrustCard engine` · `Rubric profiles` · `Calibration set` · `Trust review UI contract` |
| [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md) | `Citation audit service` · `Audit rubric` · `Mechanical locator checker` · `Audit report/scorecard` |
| [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md) | `Method Registry` · `Protocol validators` · `Amendment workflow` · `Post-hoc change detector` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/WP-083_experiment_batch.md) | `ExperimentBatch workflow` · `Staging policy` · `Parameter manifest` · `Checkpoint/recovery logic` |
| [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/WP-095_claim_evidence_explorer.md) | `Claim Explorer` · `Evidence preview` · `Provenance graph` · `Assessment/blocker panels` |
| [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md) | `OTel platform` · `Semantic conventions` · `Instrumentation libraries` · `Trace completeness dashboard` |
| [WP-097 — Langfuse Model/Agent Tracing and Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/WP-097_langfuse_llm_trace.md) | `Langfuse platform` · `Prompt registry` · `Trace/redaction policy` · `Retention/export runbook` |
| [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md) | `Cost Ledger` · `Budget service` · `Cost adapters` · `Invoice reconciliation` |

### Full prerequisite closure

**87 of 160 packages (54%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-100` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` · `WP-085` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` |
| 41 | `WP-095` |

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-105` · `WP-109` · `WP-110`
- **Transitively reachable:** **25 of 160 packages (16%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **42** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Scientific Engineering Lead |
| Independent verifier | Methodologist / Evidence Auditor |
| Gates touched | `G4` · `G5` |
| Controls | `CTL-DAT-01` · `CTL-EPI-01` · `CTL-CST-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/ACC-08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-09 — Budget Hard Stop](../12_ACCEPTANCE_SCENARIOS/ACC-09_budget_hard_stop.md) | Critical | An 80% warning is raised; at 100% new expensive work is denied, the workflow pauses with state and checkpoints preserved, and no duplicate cost or reservation is created. |
| [ACC-23 — Artifact Overwrite Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-23_artifact_overwrite.md) | Critical | The overwrite is rejected; the new bytes can only be written as a new content address and version, and existing references are unchanged. |
| [ACC-32 — Secret in Prompt or Trace](../12_ACCEPTANCE_SCENARIOS/ACC-32_secret_in_trace.md) | Critical | The secret never appears in raw telemetry, events or the UI; redaction or quarantine occurs, a security event is raised and the credential is revoked. |
| [ACC-39 — Negative Research Result](../12_ACCEPTANCE_SCENARIOS/ACC-39_negative_result.md) | Medium | The result is neither lost nor reframed as a success; a negative run and claim artifact, the limitations and a stop/pivot/continue `DecisionRecord` are produced. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/WP-083_experiment_batch.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/WP-095_claim_evidence_explorer.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-097 — Langfuse Model/Agent Tracing and Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/WP-097_langfuse_llm_trace.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md)
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
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Sandbox profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Execution Cell controller` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `SandboxAttestation` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Capture/destroy workflow` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Red-team tests` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Four-zone isolation profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Anchor resolver` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Format adapters` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Re-anchor queue` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Anchor regression corpus` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Extraction pipeline` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Extraction schemas` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Evidence candidate store` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Second-pass review queue` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Quality dashboard` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `SourceTrustCard engine` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Rubric profiles` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Calibration set` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Trust review UI contract` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Citation audit service` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit rubric` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Mechanical locator checker` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit report/scorecard` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Decomposed citation audit with per-question verification class` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Method Registry` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Protocol validators` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Amendment workflow` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Post-hoc change detector` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `SpecificationConformanceRecord binding` | `WP-081` | `python3 scripts/progress.py show WP-081` |
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
| `ExperimentBatch workflow` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Staging policy` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Parameter manifest` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Checkpoint/recovery logic` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Batch report` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `ExperimentPromotionRecord` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `ResearchCampaignGovernor` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `CampaignStopRecord` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Claim Explorer` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Evidence preview` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Provenance graph` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Assessment/blocker panels` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Audit drill-down` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `OTel platform` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Semantic conventions` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Instrumentation libraries` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Trace completeness dashboard` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Langfuse platform` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Prompt registry` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Trace/redaction policy` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Retention/export runbook` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Trace quality dashboard` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Cost Ledger` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Budget service` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Cost adapters` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Invoice reconciliation` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `FinOps dashboard/runbook` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Token ledger categories` | `WP-100` | `python3 scripts/progress.py show WP-100` |

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
- **Scientific Engineering Lead** carries the acceptance decision; **Methodologist / Evidence Auditor** must verify independently of whoever implements.
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

### No registered source names this package

Neither register binds an upstream mechanism or a runtime component to `WP-104`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-104-T01 | Create the baseline, falsification plan and preflight manifest | Implementation owner | Commit / configuration / record reference |
| WP-104-T02 | Run the staged experiment, smoke run and full run | Implementation owner | Commit / configuration / record reference |
| WP-104-T03 | Verify model, tool, sandbox, artifact and cost correlation | Implementation owner | Commit / configuration / record reference |
| WP-104-T04 | Perform evidence extraction, anchoring, trust and citation audit | Implementation owner | Commit / configuration / record reference |
| WP-104-T05 | Build the claim, dependency and state path, including the negative-result path | Implementation owner | Commit / configuration / record reference |
| WP-104-T06 | Query lineage in the cockpit, the graph and the audit ledger | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Run/claim vertical dossier`
- `Run manifests/artifacts`
- `Claim/Evidence records`
- `Cost/trace/audit evidence`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-104_vertical_slice_run_claim.tests.md`](WP-104_vertical_slice_run_claim.tests.md).

- Denial of a run with a missing manifest
- A hard budget stop
- Denial of an artifact overwrite
- The contradictory-evidence state
- A negative result being retained
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-104_vertical_slice_run_claim.acceptance.md`](WP-104_vertical_slice_run_claim.acceptance.md), together with what this package still cannot establish.

- [ ] Every run carries complete frozen lineage.
- [ ] Material claims are bound to a locator and to source status.
- [ ] A self-declaration never substitutes for mechanical evidence.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

The run or claim is invalidated within the synthetic project; canonical evidence is retained and corrections are made as new versions.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
