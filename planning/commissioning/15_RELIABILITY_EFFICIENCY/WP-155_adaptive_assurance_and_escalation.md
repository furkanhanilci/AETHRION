# WP-155 — Adaptive Assurance, Verifier Qualification and Escalation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-155` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Assurance Lead |
| Independent verifier | Eval Office / Internal Audit |
| Hard dependencies | WP-044, WP-087, WP-126 |
| Related gates | G6,G7 |
| Related controls | CTL-EPI-01, CTL-EPI-04 |
| Related acceptance scenarios | ACC-107, ACC-108, ACC-109 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-155_adaptive_assurance_and_escalation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-155_adaptive_assurance_and_escalation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Verification classes are routed by consequence and uncertainty rather than applied uniformly, and a verifier that cannot tell says so instead of choosing.


## Analysis

### What this package actually decides

When each verification class runs, and what happens when the honest answer is
*I cannot tell*.

`ADR-008` fixed what verification is — four classes, qualification required for
V2. This package is the router, and `ADR-015` is its decision record.

### Why uniform assurance fails in both directions

Running everything on everything wastes qualified verifier budget on exploratory
work **and** sets the depth by what is affordable across the whole workload —
which is to say too shallow exactly where consequence is highest.

Routing inputs: claim consequence, the study mode's claim ceiling, the assurance
class, the verifier's measured uncertainty on this task class, and whether a
cheaper class already resolved the question.

### Abstention is the load-bearing addition

A judge forced to choose on a case it cannot resolve will choose, and the choice
looks identical to a confident one in the record.

So `ABSTAIN` and `INSUFFICIENT_CONFIDENCE` are valid verdicts:

- Abstention **never satisfies** a required verification — it escalates.
- Abstention is **not a verifier failure**. A verifier that never abstains on a
  genuinely ambiguous fixture is miscalibrated, and its qualification record
  should say so — ACC-109.
- Abstention **rate is a qualification metric**. Ninety per cent abstention is
  coverage, not accuracy.

### What routing may never become

**Selective enforcement.** A router that sends only convenient cases to a human,
or lowers a class because the queue is long, has turned assurance into
throughput — ACC-108 plants exactly that.

**A budget lever.** Budget pressure degrades communication verbosity (WP-153),
never assurance depth. A task that cannot afford its route blocks.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management](../05_MODEL_AGENT_TOOL/WP-043_model_eval_golden_sets.md) | `Eval dataset manifests` · `Role eval harness` · `Grader/rubric bundle` · `Contamination controls` |
| [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/WP-044_model_qualification_admission.md) | `Qualification pipeline` · `Admission dossier` · `CapabilityProfile update` · `Regression schedule` |
| [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md) | `Verification Engine` · `Validator catalog` · `VerificationRecord service` · `Regression fixtures` |

### Full prerequisite closure

**75 of 160 packages (47%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-126`
- **Transitively reachable:** **2 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **38** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Assurance Lead |
| Independent verifier | Eval Office / Internal Audit |
| Gates touched | `G6` · `G7` |
| Controls | `CTL-EPI-01` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-092 — Inspector Reviews High-Consequence Output](../12_ACCEPTANCE_SCENARIOS/ACC-092_inspector_high_consequence_review.md) | High | Inconsistencies are raised as findings and routed. The Inspector holds no gate authority, and a clean Inspector result does not by itself satisfy any required verification. |
| [ACC-107 — Expired Verifier Qualification](../12_ACCEPTANCE_SCENARIOS/ACC-107_expired_verifier_qualification.md) | Critical | Both yield `INCONCLUSIVE` and block the gate. Their verdicts are retained as advisory. Only a current, matching qualification satisfies the requirement. |
| [ACC-108 — Escalation Is Not Selective Enforcement](../12_ACCEPTANCE_SCENARIOS/ACC-108_selective_verifier_escalation.md) | Critical | The high-consequence claim is routed by consequence, not by queue length. No route is lowered because the queue is long or the budget is tight, and a downgrade attempt is refused and audited. |
| [ACC-109 — Verifier Abstention Is a Valid Result](../12_ACCEPTANCE_SCENARIOS/ACC-109_verifier_abstention_is_valid.md) | High | The ambiguous case yields `ABSTAIN`, which escalates rather than passing or failing. The unambiguous cases yield verdicts. A verifier that never abstains on the ambiguous set fails qualification. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-044 — Model Qualification and Admission Pipeline](../05_MODEL_AGENT_TOOL/WP-044_model_qualification_admission.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-126 — Reviewer, Judge and Reproducer Calibration](../11_DAY2_OPERATIONS/WP-126_assurance_calibration.md)
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
| `Eval dataset manifests` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Role eval harness` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Grader/rubric bundle` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Contamination controls` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Eval scorecard` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Cross-model × cross-harness compliance matrix` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Qualification pipeline` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Admission dossier` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `CapabilityProfile update` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Regression schedule` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Ejection procedure` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Fingerprint and abstention scope on qualification records` | `WP-044` | `python3 scripts/progress.py show WP-044` |
| `Verification Engine` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Validator catalog` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerificationRecord service` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Regression fixtures` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `V0-V3 verification routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerifierQualificationRecord` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Positive and negative control suite` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Adaptive assurance routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Abstention verdicts` | `WP-087` | `python3 scripts/progress.py show WP-087` |

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
- **Assurance Lead** carries the acceptance decision; **Eval Office / Internal Audit** must verify independently of whoever implements.
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
| `ASM-046` — Trust or Escalate — cascaded selective evaluation | `ADAPTIVE_REIMPLEMENT` | `MS-ASSUR-001` · `MS-ASSUR-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-046` | A cascade decides which verifier answers. It cannot decide that a claim is true, and a coverage guarantee is not a substitute for human authority at G8. | The framing of a statistical human-agreement guarantee as sufficient. Selective evaluation reports the fraction of cases it is willing to judge at a target agreement level; that is a useful property and it is not scientific authority. |

### Where a plain row would mislead

- **`ASM-046`** — Uses judge confidence to escalate uncertain cases from a cheap judge to a stronger one, reporting roughly 80% coverage at an 80% human-agreement target. The mechanism taken is the cascade and, more importantly, **abstention as a first-class outcome** — ADR-015. A judge forced to choose on a case it cannot resolve produces a verdict indistinguishable from a confident one.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-046` — Trust or Escalate — cascaded selective evaluation** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**Acquisition readiness — 1 obligation open across 1 of 1 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-155-T01 | Implement the assurance router and its five routing inputs | Implementation owner | Commit / configuration / record reference |
| WP-155-T02 | Implement the V0 → V1 → V2 → V3 cascade with independence-aware verifier selection | Implementation owner | Commit / configuration / record reference |
| WP-155-T03 | Add `ABSTAIN` and `INSUFFICIENT_CONFIDENCE` as first-class verdicts | Implementation owner | Commit / configuration / record reference |
| WP-155-T04 | Make abstention rate a tracked qualification metric | Implementation owner | Commit / configuration / record reference |
| WP-155-T05 | Extend `VerifierQualificationRecord` with fingerprint, coverage and human agreement | Implementation owner | Commit / configuration / record reference |
| WP-155-T06 | Prevent consequence-based downgrade and budget-based route reduction | Implementation owner | Commit / configuration / record reference |
| WP-155-T07 | Build the ambiguous fixture set that a calibrated verifier must abstain on | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Assurance router`
- `Cascade and escalation path`
- `Abstention verdicts`
- `Extended VerifierQualificationRecord`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-155_adaptive_assurance_and_escalation.tests.md`](WP-155_adaptive_assurance_and_escalation.tests.md).

- An expired or missing qualification must yield INCONCLUSIVE and block the gate
- A high-consequence claim must not be routable to the cheap path
- Abstention must escalate and must never satisfy a required verification
- A verifier that never abstains on the ambiguous fixture set must fail qualification
- Budget pressure must not lower an assurance route
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-155_adaptive_assurance_and_escalation.acceptance.md`](WP-155_adaptive_assurance_and_escalation.acceptance.md), together with what this package still cannot establish.

- [ ] Routing depends on consequence and uncertainty, and cannot be lowered by queue length or budget.
- [ ] `ABSTAIN` is reachable, escalates, and is tracked as a qualification metric.
- [ ] No V2 verdict satisfies a requirement without a current, matching qualification.
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

- An efficiency measure that improves a cost number and quietly lowers assurance has moved the failure, not removed it. Every optimisation here is anchored to a quality guard and rolls back when it trips.
- A coordination defect is invisible in a healthy run and obvious only in a post-mortem. These packages are specified as injection suites for that reason, not as properties.
- Multi-agent cost pressure always argues for fewer agents. The cohort is fixed by ADR-011 and is not a lever any package here may pull.

## Rollback / compensation

A routing policy change applies to subsequent verifications only; verdicts already issued keep the route and qualification that produced them, so a historical assurance decision stays interpretable.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
