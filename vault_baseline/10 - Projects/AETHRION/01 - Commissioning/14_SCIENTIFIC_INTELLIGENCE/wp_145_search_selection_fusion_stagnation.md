---
title: "WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control"
aliases:
  - "WP-145"
  - "WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Which candidate is expanded next, when branches are recombined and when a campaign stops are decided by recorded policy under a budget contract, deterministically wherever no model is involved."
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-145_search_selection_fusion_stagnation.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/state/not-started
---

# WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control

## Package card

| Field | Value |
|---|---|
| Work package | `WP-145` |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | FinOps Lead / Assurance Lead |
| Hard dependencies | WP-083, WP-100, WP-144 |
| Related gates | G5 |
| Related controls | CTL-EPI-03, CTL-OPS-02 |
| Related acceptance scenarios | ACC-09, ACC-59 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_145_search_selection_fusion_stagnation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_145_search_selection_fusion_stagnation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Which candidate is expanded next, when branches are recombined and when a campaign stops are decided by recorded policy under a budget contract, deterministically wherever no model is involved.


## Analysis

### What this package actually decides

How research compute is allocated, and — more importantly — how it stops. An
unbounded search is not a research method; it is a bill.

Three mechanisms carry the package: a selection policy that decides what to
expand, a fusion mechanism that lets one branch use what another learned, and the
stopping controls that end the campaign.

### Selection may revisit, and priority is not confidence

The property worth taking from the published work here is that selection is not
restricted to leaves: a strong interior node can be expanded again. That is what
keeps a promising line from being abandoned because its immediate children were
weak.

The score that decides this is normalised, because raw metrics differ by orders of
magnitude between tasks and un-normalised values make search dynamics an artefact
of units. It is stored as a search priority and is structurally prevented from
being written anywhere epistemic — the same rule WP-143 applies to ranking.

### Fusion has to name what it inherits

Asking a model to "combine these two candidates" produces an opaque result with
no provenance: something improved, and nothing records what. A `FusionProposal`
must name which mechanism comes from which parent, what interaction is expected
and what would falsify it.

The fused candidate is a new node. It does not overwrite its inputs, and their
artifact digests are unchanged by its existence.

### Stopping is a control, not an outcome

The governor stops a campaign on cost, rounds, experiment count, compute or
convergence patience, and stagnation detection ends searches that are still
spending without improving.

The rule that matters is what a stop means: `STOPPED_BY_BUDGET` is a termination
classification and satisfies no gate. A campaign that ran out of money has not
demonstrated anything, and the record has to make that impossible to misread.
Budget reserved for VERIFY, FULL and G7 reproduction cannot be consumed by
exploration, because a campaign that spends its reproduction budget on search has
produced results nobody can check.

### Determinism where no model is involved

Given the same graph snapshot and the same policy configuration, selection,
fusion eligibility and stagnation must return the same decision. These are
arithmetic, and arithmetic that varies between runs cannot be replayed, audited or
debugged.

### Baseline v1.3.0 — two stopping rules that must not be shared

The campaign governor generalises into the `ResearchBudgetContract`'s nine
dimensions, with reserved verification and reproduction budget that exploration
cannot reach (ACC-101).

The distinction worth keeping: **search stopping and communication stopping are
different policies.** Search stops on frontier improvement, stagnation and
compute. Communication degrades on token spend and edge utility. They look alike
and coupling them would mean a campaign that stops exploring because its agents
talked too much, or keeps talking because its search is still improving.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/wp_083_experiment_batch.md) | `ExperimentBatch workflow` · `Staging policy` · `Parameter manifest` · `Checkpoint/recovery logic` |
| [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md) | `Cost Ledger` · `Budget service` · `Cost adapters` · `Invoice reconciliation` |
| [WP-144 — Discovery Search Graph and Candidate Lifecycle](../14_SCIENTIFIC_INTELLIGENCE/wp_144_discovery_search_graph.md) | `SearchNode` · `SearchEdge` · `Candidate lifecycle state machine` · `SearchGraph module` |

### Full prerequisite closure

**61 of 160 packages (38%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-075` · `WP-141` |
| 28 | `WP-081` · `WP-142` |
| 29 | `WP-082` · `WP-143` |
| 30 | `WP-083` · `WP-096` · `WP-144` |
| 31 | `WP-100` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-153`
- **Transitively reachable:** **1 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-S — Scientific intelligence |
| Dependency depth | level **32** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | FinOps Lead / Assurance Lead |
| Gates touched | `G5` |
| Controls | `CTL-EPI-03` · `CTL-OPS-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-09 — Budget Hard Stop](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) | Critical | An 80% warning is raised; at 100% new expensive work is denied, the workflow pauses with state and checkpoints preserved, and no duplicate cost or reservation is created. |
| [ACC-58 — Cross-Branch Fusion Lineage](../12_ACCEPTANCE_SCENARIOS/acc_58_cross_branch_fusion_lineage.md) | High | D retains both input references and the named inherited mechanisms end to end — in the canonical graph, after a derived-graph rebuild, and in the export. Neither A nor C is modified. |
| [ACC-59 — Discovery Search Stagnation](../12_ACCEPTANCE_SCENARIOS/acc_59_discovery_search_stagnation.md) | High | The detector fires at the configured boundary, the configured action is taken, and the campaign terminates. An unbounded search is impossible even if every model in it recommends continuing. |
| [ACC-101 — Reserved Assurance Budget Is Unreachable](../12_ACCEPTANCE_SCENARIOS/acc_101_budget_hard_stop_reserved_assurance.md) | Critical | The reserve is unreachable from the exploration path. The campaign stops on its exploration ceiling with the reserve intact, and the assurance work it was reserved for can still run. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-083 — ExperimentBatch and Staged Execution](../08_EVIDENCE_ASSURANCE/wp_083_experiment_batch.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md), [WP-144 — Discovery Search Graph and Candidate Lifecycle](wp_144_discovery_search_graph.md)
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
| `ExperimentBatch workflow` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Staging policy` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Parameter manifest` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Checkpoint/recovery logic` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Batch report` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `ExperimentPromotionRecord` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `ResearchCampaignGovernor` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `CampaignStopRecord` | `WP-083` | `python3 scripts/progress.py show WP-083` |
| `Cost Ledger` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Budget service` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Cost adapters` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Invoice reconciliation` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `FinOps dashboard/runbook` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Token ledger categories` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `SearchNode` | `WP-144` | `python3 scripts/progress.py show WP-144` |
| `SearchEdge` | `WP-144` | `python3 scripts/progress.py show WP-144` |
| `Candidate lifecycle state machine` | `WP-144` | `python3 scripts/progress.py show WP-144` |
| `SearchGraph module` | `WP-144` | `python3 scripts/progress.py show WP-144` |
| `Discovery graph projection` | `WP-144` | `python3 scripts/progress.py show WP-144` |

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
- **Experiment Platform Lead** carries the acceptance decision; **FinOps Lead / Assurance Lead** must verify independently of whoever implements.
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
| `ASM-002` — Scholar Loop — campaign governor | `DIRECT_ADAPT` | `scholarloop/governor.py` | the local module and contract surface this becomes — **named at refinement** | **3** |
| `ASM-008` — ERA — ScorableTask and Flat UCB Tree Search (FUTS) | `DIRECT_ADAPT` | `implementation/futs.py` | the local module and contract surface this becomes — **named at refinement** | **3** |
| `ASM-009` — MLEvolve — progressive MCGS, reference edges, cross-branch fusion, stagnation | `ADAPTIVE_REIMPLEMENT` | `MS-SRCH-003` · `MS-SRCH-004` · `MS-SRCH-005` | the local module and contract surface this becomes — **named at refinement** | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-002` | STOPPED_BY_BUDGET is a termination classification, never an acceptance. The governor may halt a campaign; it may not pass a gate. | The hard-coded model price table — cost data comes from WP-041 and WP-100. The orchestrator and the JSONL ledger. |
| `ASM-008` | A FUTS selection score allocates compute. Writing it into a ClaimVersion, a VerifiedValue or a GateRecord is a forbidden conversion enforced by schema and policy. | The execute_fn contract — candidate execution goes through the Execution Broker against a private frozen evaluator — and raw solution strings as the unit of state. |
| `ASM-009` | A reference edge lets one branch read another. It may not alter primary-parent ancestry, which is the credit path evidence lineage depends on. | The controller and runtime, and the reported stagnation thresholds as normative constants — they enter as an initial experimental profile to be calibrated, not as settings to copy. |

### Where a plain row would mislead

- **`ASM-002`** — A small pure state machine with a deterministic MockLLM path upstream, which is what makes characterisation before adaptation cheap.
- **`ASM-008`** — The published property that matters is that selection may return a previously expanded interior node, not only a leaf. Direct adaptation is viable because the reference implementation is compact and Apache-2.0; the decision is confirmed after reading the file at a pinned commit.
- **`ASM-009`** — Licence is permissive, so direct adaptation would be legal; it is still reimplemented because the native graph contract — typed SearchEdge, ArtifactRecord candidates, VerifiedValue metrics — matters more than importing the controller.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-002` — Scholar Loop — campaign governor** · `DIRECT_ADAPT` · status `PROPOSED`

- the register entry moved to `CHARACTERIZED` — upstream behaviour captured and the adaptation confirmed against the pinned tree, not against the paper
- a pinned upstream commit — a branch name is not a pin
- a characterisation suite capturing upstream behaviour **before** any code moves

**`ASM-008` — ERA — ScorableTask and Flat UCB Tree Search (FUTS)** · `DIRECT_ADAPT` · status `PROPOSED`

- the register entry moved to `CHARACTERIZED` — upstream behaviour captured and the adaptation confirmed against the pinned tree, not against the paper
- a pinned upstream commit — a branch name is not a pin
- a characterisation suite capturing upstream behaviour **before** any code moves

**`ASM-009` — MLEvolve — progressive MCGS, reference edges, cross-branch fusion, stagnation** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**Acquisition readiness — 7 obligations open across 3 of 3 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-145-T01 | Write the selection mechanism specification and its fixtures before implementing | Implementation owner | Commit / configuration / record reference |
| WP-145-T02 | Implement the selector with metric-direction, tie and missing-value handling | Implementation owner | Commit / configuration / record reference |
| WP-145-T03 | Define `SearchPolicyConfig` and the early, mid and late phase profiles | Implementation owner | Commit / configuration / record reference |
| WP-145-T04 | Implement `FusionProposal` with named mechanism inheritance and compatibility checks | Implementation owner | Commit / configuration / record reference |
| WP-145-T05 | Implement the stagnation detector and its configured actions | Implementation owner | Commit / configuration / record reference |
| WP-145-T06 | Implement the campaign governor against `ResearchBudgetContract` | Implementation owner | Commit / configuration / record reference |
| WP-145-T07 | Implement reserved budgets that exploration cannot consume | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Selection mechanism specification`
- `SearchPolicyConfig`
- `FusionProposal`
- `StagnationDetector`
- `ResearchCampaignGovernor`
- `CampaignStopRecord`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-145_search_selection_fusion_stagnation.tests.md`](wp_145_search_selection_fusion_stagnation.tests.md).

- A fixed graph fixture must select the expected node under both metric directions
- Ties and missing metrics must resolve deterministically
- A fusion must retain both parents and their named mechanisms
- Stagnation must fire exactly at the configured boundary and not before
- Budget, round and convergence caps must each stop the campaign at their boundary
- Reserved reproduction budget must be unreachable from exploration
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-145_search_selection_fusion_stagnation.acceptance.md`](wp_145_search_selection_fusion_stagnation.acceptance.md), together with what this package still cannot establish.

- [ ] A bounded campaign terminates deterministically under cost, round and convergence controls.
- [ ] A stop record satisfies no gate and cannot be read as an acceptance.
- [ ] Cross-branch information is exploitable without any loss of lineage.
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

A policy change takes effect for subsequent campaigns only; a running campaign keeps the configuration it started under, and the configuration is recorded with its results.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
