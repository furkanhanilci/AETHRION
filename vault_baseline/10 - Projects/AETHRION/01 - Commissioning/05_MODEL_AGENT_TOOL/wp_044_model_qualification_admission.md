---
title: "WP-044 — Model Qualification and Admission Pipeline"
aliases:
  - "WP-044"
  - "WP-044 — Model Qualification and Admission Pipeline"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A new or changed model profile is admitted to a role only on evidence from shadow running, quality, safety, data handling, availability and quality-adjusted cost."
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-044_model_qualification_admission.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g1
  - aethrion/gate/g5
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-044 — Model Qualification and Admission Pipeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-044` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Eval Office |
| Independent verifier | Admission Board / Safety / FinOps |
| Hard dependencies | WP-041, WP-042, WP-043 |
| Related gates | G1,G5,G10 |
| Related controls | CTL-MOD-01, CTL-MOD-02 |
| Related acceptance scenarios | ACC-10, ACC-36, ACC-37 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_044_model_qualification_admission.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_044_model_qualification_admission.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A new or changed model profile is admitted to a role only on evidence from shadow running, quality, safety, data handling, availability and quality-adjusted cost.


## Analysis
### What this package actually decides

What evidence is enough to let a model do research work. The registry (WP-042)
holds the verdict; this package is the process that reaches it, and its integrity
depends on one property: **the decision is made against an immutable snapshot**
(T01), not against "the current version of the model".

### Shadow running is the evidence nothing else can substitute (T02)

Benchmark scores measure a model on a task someone else chose. Shadow running
measures it on *your* tasks, alongside the incumbent, with the output recorded and
unused. It is slower and more expensive than a benchmark and it is the only
evidence that transfers.

### Incremental value, not absolute quality (T03)

The question at admission is never "is this model good". It is "is this model
better than what is already admitted for this role, by enough to justify the
switch". A model that scores well and adds nothing over the incumbent is a cost
with no benefit — and switching carries its own cost, because every run before
and after is now under different conditions.

### The data and provider contract is a research constraint, not procurement (T04)

Retention terms decide whether a D3 source can be sent at all, and whether a
prompt containing unpublished work is retained by a third party. `PR-14`'s licence
concerns apply to what goes *out* as much as to what comes in. A model qualified
on quality and unqualified on retention is not admitted.

### Expiry and the ejection path are what make admission reversible (T05, T06)

An admission with no expiry is permanent by default. The regression schedule is
what detects drift between expiries, and the ejection procedure is what makes a
negative result actionable rather than a note. `PR-15`'s contamination is one
trigger; a provider silently changing a model behind a stable name is another.

### Baseline v1.3.0 — the Task Compiler stops emitting a skill list

This is the largest change in the model and agent layer, and it is a change of
kind rather than of size. The compiler's output was a skill bundle and a model
choice. It becomes the full execution shape of a task:

`AgentCohortRecord` · `CognitiveDiversityProfile` · skill bundles **by family** ·
`CommunicationTopology` · `ContextProjectionPolicy` · `ResearchBudgetContract` ·
`AssuranceRoute` · `ExecutionProfile` · `IndependenceProfile`.

A coding-science task compiles **both** skill families — preregistration
discipline beside test-driven development, scientific review beside code review
— without either aliasing the other (`ADR-012`).

Two other bindings:

- **Qualification records gain scope.** A verifier's qualification is keyed by
  verifier, version, task class, domain profile *and* threshold, and now also
  carries a model execution fingerprint and an abstention rate.
- **The Tool Broker gains a capability gate.** An action is unavailable unless
  policy grants it — not available-but-discouraged. Untrusted content can supply
  values and can never create an action, which is `ADR-003` enforced at the tool
  boundary rather than asserted at the prompt. Deterministic tool results are
  reusable within a declared freshness window and are marked as reused.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md) | `LiteLLM deployment` · `Provider configuration` · `Gateway policy adapter` · `Model-call audit/cost events` |
| [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md) | `Capability Registry service` · `Profile state machine` · `Eligibility API` · `Expiry/revoke scheduler` |
| [WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md) | `Eval dataset manifests` · `Role eval harness` · `Grader/rubric bundle` · `Contamination controls` |

### Full prerequisite closure

**27 of 160 packages (17%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 19 | `WP-043` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-045` · `WP-088` · `WP-108` · `WP-124` · `WP-155`
- **Transitively reachable:** **111 of 160 packages (69%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **20** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Eval Office |
| Independent verifier | Admission Board / Safety / FinOps |
| Gates touched | `G1` · `G5` · `G10` |
| Controls | `CTL-MOD-01` · `CTL-MOD-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-10 — Primary Model Provider Outage](../12_ACCEPTANCE_SCENARIOS/acc_10_provider_outage.md) | High | Only an admitted fallback is chosen; route, family and independence are recomputed, SLO and cost records are written, and the task is not duplicated. |
| [ACC-36 — Model Snapshot Drift](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) | Critical | The profile moves to suspension or requalification, the router cache is invalidated and an `ImpactScan` opens for open tasks, runs and claims; there is no unsafe fallback. |
| [ACC-37 — Evaluation Set Contamination](../12_ACCEPTANCE_SCENARIOS/acc_37_eval_contamination.md) | Critical | The evaluation bundle is invalidated; the qualification and profile decisions that depended on it are suspended, and a clean set and re-evaluation process opens. |
| [ACC-61 — Unqualified Semantic Verifier](../12_ACCEPTANCE_SCENARIOS/acc_61_unqualified_semantic_verifier.md) | Critical | The verdict is recorded as advisory and cannot satisfy the requirement; the gate blocks with `INCONCLUSIVE` rather than passing or failing the claim on an unqualified judgement. |
| [ACC-107 — Expired Verifier Qualification](../12_ACCEPTANCE_SCENARIOS/acc_107_expired_verifier_qualification.md) | Critical | Both yield `INCONCLUSIVE` and block the gate. Their verdicts are retained as advisory. Only a current, matching qualification satisfies the requirement. |
| [ACC-109 — Verifier Abstention Is a Valid Result](../12_ACCEPTANCE_SCENARIOS/acc_109_verifier_abstention_is_valid.md) | High | The ambiguous case yields `ABSTAIN`, which escalates rather than passing or failing. The unambiguous cases yield verdicts. A verifier that never abstains on the ambiguous set fails qualification. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-041 — LiteLLM Model Gateway Foundation](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-042 — Capability Registry and Profile Lifecycle](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-043 — Role-Based Model Evaluation and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md)
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
| `LiteLLM deployment` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Provider configuration` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway policy adapter` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Model-call audit/cost events` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Gateway runbook` | `WP-041` | `python3 scripts/progress.py show WP-041` |
| `Capability Registry service` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Profile state machine` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eligibility API` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Expiry/revoke scheduler` | `WP-042` | `python3 scripts/progress.py show WP-042` |
| `Eval dataset manifests` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Role eval harness` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Grader/rubric bundle` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Contamination controls` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Eval scorecard` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Cross-model × cross-harness compliance matrix` | `WP-043` | `python3 scripts/progress.py show WP-043` |

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
- **Eval Office** carries the acceptance decision; **Admission Board / Safety / FinOps** must verify independently of whoever implements.
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
| `ASM-029` — AstaBench — cost-controlled scientific agent benchmark suite | `BENCHMARK` | a measurement of this system — nothing enters it | the contract this is held behind | none |
| `CMP-020` — OpenSSF model-signing | `DEPENDENCY` | Signing and verification of model files. | The requirement that a local open-weight model file has a verified identity before it is admitted. | **2** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-029` | Qualification evidence for a model or actor profile on a task class. Never a gate. | Its agent implementations. |
| `CMP-020` | A signed model file is an admitted *artifact*, not a qualified *actor*. Qualification is WP-044's measurement. | A vendor signature as evidence of capability. |

### Where a plain row would mislead

- **`ASM-029`** — Not in the source brief; added here. Eleven benchmarks and over 2,400 examples spanning literature search, code execution, data analysis and end-to-end discovery, with standardised tools, a date-restricted literature corpus for reproducibility, and explicit control for model cost and tool access. That last property is what the rest of the benchmark portfolio lacks: without cost normalisation, a governed-versus-ungoverned comparison cannot separate the effect of governance from the effect of spend.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`CMP-020` — OpenSSF model-signing** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 2 obligations open across 1 of 2 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-044-T01 | Resolve the qualification request against an immutable model snapshot | Implementation owner | Commit / configuration / record reference |
| WP-044-T02 | Run the role evaluation, safety, latency and cost batches | Implementation owner | Commit / configuration / record reference |
| WP-044-T03 | Compute the baseline comparison and the incremental value | Implementation owner | Commit / configuration / record reference |
| WP-044-T04 | Verify the data and provider contract and its retention terms | Implementation owner | Commit / configuration / record reference |
| WP-044-T05 | Write the Admission Board decision workflow and the profile expiry | Implementation owner | Commit / configuration / record reference |
| WP-044-T06 | Bind the regression/drift schedule to the revocation path | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Qualification pipeline`
- `Admission dossier`
- `CapabilityProfile update`
- `Regression schedule`
- `Ejection procedure`
- `Fingerprint and abstention scope on qualification records`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-044_model_qualification_admission.tests.md`](wp_044_model_qualification_admission.tests.md).

- Passing and failing candidate fixtures
- A silent provider snapshot change
- An availability/SLO failure
- A data-policy failure
- The human triage cost threshold
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-044_model_qualification_admission.acceptance.md`](wp_044_model_qualification_admission.acceptance.md), together with what this package still cannot establish.

- [ ] Admission rests on role evaluation, not on model popularity or vendor claims.
- [ ] An expired or failed profile cannot be routed to.
- [ ] Qualification evidence carries a reproducible run manifest.
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

A failed admission leaves the profile in `SHADOW` or `SUSPENDED`; existing admitted profiles are unaffected.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
