---
title: "WP-142 — Study Mode, Bottleneck and Idea Card Model"
aliases:
  - "WP-142"
  - "WP-142 — Study Mode, Bottleneck and Idea Card Model"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A research question becomes an evidence-backed bottleneck and then a falsifiable idea, with the claim ceiling fixed by a declared study mode before any result is seen."
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-142_study_mode_bottleneck_idea.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g1
  - aethrion/gate/g2
  - aethrion/state/not-started
---

# WP-142 — Study Mode, Bottleneck and Idea Card Model

## Package card

| Field | Value |
|---|---|
| Work package | `WP-142` |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Methodologist |
| Hard dependencies | WP-005, WP-008, WP-013, WP-018, WP-034, WP-141 |
| Related gates | G0,G1,G2 |
| Related controls | CTL-EPI-03, CTL-GOV-03 |
| Related acceptance scenarios | ACC-56 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_142_study_mode_bottleneck_idea.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_142_study_mode_bottleneck_idea.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A research question becomes an evidence-backed bottleneck and then a falsifiable idea, with the claim ceiling fixed by a declared study mode before any result is seen.


## Analysis

### What this package actually decides

What a project is allowed to claim, decided before it has anything to claim. The
`StudyMode` — FEASIBILITY, EXPLORATORY or CONFIRMATORY — sets a claim ceiling at
G0, and everything downstream inherits it.

This is a separate axis from the R1/R2/R3 assurance class of WP-005, and the two
must not be collapsed. Assurance class answers *how much scrutiny this work has
to survive*. Study mode answers *what kind of statement this work can produce at
all*. A feasibility pilot can be R3 and still be unable to license a confirmatory
claim.

### Why feasibility cannot be promoted afterwards

The failure this blocks is the most common one in real research and the easiest
for an autonomous system to commit: run something exploratory, see a result you
like, and describe it afterwards as though it had been predicted. Once the
outcome has been seen, no amount of subsequent writing makes the analysis
confirmatory on that data.

So the mode is a record with an external timestamp, and a change of mode creates
a successor plus a deviation record. Downgrading the claim ceiling is always
available; raising it on the same data is not available at all.

### Why a bottleneck needs evidence before an idea is generated

Idea generation that starts from a prompt rather than from a diagnosed limitation
produces plausible novelty — ideas that read well and address nothing. The
`BottleneckRecord` requires the current best understanding, the limitation, the
evidence behind it and the competing explanations that have not been ruled out.

A bottleneck asserted by a model alone is not canonical. That constraint is what
makes the record worth having: it forces the literature work to happen before the
ideation work, rather than being written up afterwards to justify it.

### Falsification before promotion

An `IdeaCard` cannot be promoted to a hypothesis candidate without a
`falsification_plan`. This is the same move `preregistration-discipline` makes at
the analysis level, applied one stage earlier: an idea that cannot say what would
show it wrong is not yet a scientific idea, and the cheapest moment to notice
that is before compute is spent on it.

### Prior art on more than one axis

`PriorArtCollision` scores problem, mechanism, data, evaluation and contribution
overlap separately, because a single similarity scalar collapses the distinction
between "someone asked this question" and "someone answered it with this method
on this data". The verdict is model-mediated and therefore V2, which means it
needs a qualified verifier before it can satisfy anything at G6.

### Baseline v1.3.0 — collaboration context, and one conversion that stays forbidden

No ideation or discovery object is replaced. Two things are wired in:

**Collaboration and budget context.** A hypothesis proposed by a cohort carries
which cognitive functions contributed and under what independence conditions. A
search campaign carries its budget contract and its token ledger.

**The forbidden conversion, restated because it now has a second source.**
`ADR-006` already refuses a search score becoming a claim confidence. This
baseline adds communication utility, which is the same category error arriving
through the collaboration plane. Both are routing priorities. Neither may be
written into a `ClaimVersion`, a `VerifiedValue` or a `GateRecord`, and the
refusal is by schema and by policy rather than by convention.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md) | `Gate Policy v1` · `Gate artifact matrix` · `Reopen/return transition table` · `Gate owner matrix` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md) | `G0/G1 workflows` · `Intake/Charter UI API contract` · `ControlPlan generation` · `Gate fixtures` |
| [WP-141 — Upstream Assimilation, Lineage and Characterisation Governance](../14_SCIENTIFIC_INTELLIGENCE/wp_141_upstream_assimilation_governance.md) | `AssimilationCandidate schema` · `UpstreamLineage register` · `check_upstream_lineage.py` · `SPDX/REUSE policy` |

### Full prerequisite closure

**48 of 160 packages (30%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-059` |
| 27 | `WP-141` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-143` · `WP-147`
- **Transitively reachable:** **14 of 160 packages (9%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-S — Scientific intelligence |
| Dependency depth | level **28** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Methodologist |
| Gates touched | `G0` · `G1` · `G2` |
| Controls | `CTL-EPI-03` · `CTL-GOV-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-56 — Confirmatory Result Without a Frozen Analysis Plan](../12_ACCEPTANCE_SCENARIOS/acc_56_confirmatory_without_frozen_plan.md) | Critical | The gate refuses. The work may be relabelled exploratory only through an explicit, recorded policy decision that lowers the claim ceiling; it can never be relabelled confirmatory afterwards on the same data. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md), [WP-141 — Upstream Assimilation, Lineage and Characterisation Governance](wp_141_upstream_assimilation_governance.md)
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
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `StudyMode decision table` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Substantiality threshold for the multi-agent invariant` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Gate Policy v1` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate artifact matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Reopen/return transition table` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate owner matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `G0/G1 workflows` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Intake/Charter UI API contract` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `ControlPlan generation` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Gate fixtures` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `AssimilationCandidate schema` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `UpstreamLineage register` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `check_upstream_lineage.py` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `SPDX/REUSE policy` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `Characterisation test convention` | `WP-141` | `python3 scripts/progress.py show WP-141` |
| `Upstream drift review workflow` | `WP-141` | `python3 scripts/progress.py show WP-141` |

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
- **Research Director** carries the acceptance decision; **Assurance Lead / Methodologist** must verify independently of whoever implements.
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
| `ASM-012` — ResearchStudio-Idea — structured idea card and prior-art collision | `ADAPTIVE_REIMPLEMENT` | `MS-IDEA-001` · `MS-IDEA-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-052` — Registered Reports and in-principle acceptance | `STANDARD` | the running implementation | the contract this is held behind | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-012` | A PriorArtCollision is an assessment, not a verdict. A novelty judgement at R2 or above requires a qualified verifier and, where policy says so, a human. | The UI, the orchestrator and the post-paper artifact generation. |
| `ASM-052` | In-principle acceptance commits to publishing a result regardless of its direction. It does not commit to the result being correct. | The journal workflow. What is taken is the ordering: methods reviewed before data exist. |

### Where a plain row would mislead

- **`ASM-012`** — The 'reviewer-defensible idea card' framing is confirmed upstream. The 'bottleneck diagnosis' and 'Scoop-Check' names used in the source brief were NOT confirmed on the public landing page — BottleneckRecord and PriorArtCollision are therefore recorded as AETHRION constructs inspired by this system, not as upstream feature names.
- **`ASM-052`** — The model for G2 and G2b, and the mitigation for publication bias — PR-19. A gate structure that freezes a protocol and still rejects on the direction of the result has moved the bias rather than removed it.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-012` — ResearchStudio-Idea — structured idea card and prior-art collision** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-052` — Registered Reports and in-principle acceptance** · `STANDARD` · status `PROPOSED`

- a conformance suite against the published specification

**Acquisition readiness — 2 obligations open across 2 of 2 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-142-T01 | Define `StudyModeRecord` with claim ceiling and external timestamp semantics | Implementation owner | Commit / configuration / record reference |
| WP-142-T02 | Define `BottleneckRecord` with mandatory evidence references and competing explanations | Implementation owner | Commit / configuration / record reference |
| WP-142-T03 | Define `IdeaCard` with the falsification-plan promotion rule | Implementation owner | Commit / configuration / record reference |
| WP-142-T04 | Define `PriorArtCollision` with per-axis overlap and materiality | Implementation owner | Commit / configuration / record reference |
| WP-142-T05 | Bind the records to G0, G1 and G2 gate policy | Implementation owner | Commit / configuration / record reference |
| WP-142-T06 | Write the mode-change deviation path and the one-way ceiling rule | Implementation owner | Commit / configuration / record reference |
| WP-142-T07 | Expose the records in the projection and UI schema | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `StudyModeRecord`
- `BottleneckRecord`
- `IdeaCard`
- `PriorArtCollision`
- `Gate policy bindings for G0-G2`
- `Mode change deviation procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-142_study_mode_bottleneck_idea.tests.md`](wp_142_study_mode_bottleneck_idea.tests.md).

- A feasibility result must not be able to emit a confirmatory claim
- A confirmatory mode without a pre-result plan seal must block at the gate
- A bottleneck with no evidence reference must not be recordable as evidence-backed
- An idea with no falsification plan must fail promotion
- A planted prior-art duplicate must be scored HIGH on the matching axes
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-142_study_mode_bottleneck_idea.acceptance.md`](wp_142_study_mode_bottleneck_idea.acceptance.md), together with what this package still cannot establish.

- [ ] Study mode and assurance class are separate machine-readable fields with separate effects.
- [ ] A claim ceiling can be lowered by record and can never be raised on the same data.
- [ ] One project passes G0 to G2 producing every typed record, and one planted defect is caught.
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

- A search or ranking score that becomes a claim confidence is a category error. It has to be refused by a schema, not remembered by a convention.
- A mechanism adapted without a characterisation test cannot be told apart from a mechanism that was misunderstood.
- Cognition that is permitted to recommend will be read as authority unless a field — not a paragraph — says it is not.

## Rollback / compensation

A study mode or idea card is superseded by a successor version; the original and the reason for supersession are retained, because the sequence is the evidence.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
