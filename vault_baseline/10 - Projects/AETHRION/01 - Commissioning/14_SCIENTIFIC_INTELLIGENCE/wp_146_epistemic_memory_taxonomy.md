---
title: "WP-146 — Epistemic Memory Taxonomy and Retention"
aliases:
  - "WP-146"
  - "WP-146 — Epistemic Memory Taxonomy and Retention"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "What the system remembers is separated into six stores with different authority, mutability and retention, so that a reusable lesson can never be presented as evidence."
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-146_epistemic_memory_taxonomy.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-146 — Epistemic Memory Taxonomy and Retention

## Package card

| Field | Value |
|---|---|
| Work package | `WP-146` |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Archivist / Internal Audit |
| Hard dependencies | WP-012, WP-026, WP-030, WP-075, WP-077, WP-144 |
| Related gates | G3,G5,G6,G10 |
| Related controls | CTL-DAT-03, CTL-EPI-04 |
| Related acceptance scenarios | ACC-70, ACC-79 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_146_epistemic_memory_taxonomy.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_146_epistemic_memory_taxonomy.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

What the system remembers is separated into six stores with different authority, mutability and retention, so that a reusable lesson can never be presented as evidence.


## Analysis

### What this package actually decides

That there is no such thing as "the memory". The common design — write everything
an agent might later need into one vector store — is wrong here for a reason that
has nothing to do with retrieval quality: a raw evaluator output, a failed
experiment, a debugging lesson and a working scientific principle do not have the
same epistemic status, and a store that treats them alike will eventually let one
be used as another.

The six stores are Evidence, Finding, Search Experience, Procedural, Principle
and Human Intervention. They differ on the only axes that matter here: can it
support a claim, can it change, can it expire, and who may read it.

### The two extremes define the design

Evidence is immutable and content-addressed and never decays. A source can be
retracted and a status can change, but the bytes stay, because a claim anchored to
them must remain traversable after the retraction — that is the whole point of
G10.

Procedural memory is the opposite. A debugging lesson is true about a version of a
library on a date, and it goes stale silently. It is versioned, it decays and it
is revalidated, and it can never support a claim. Putting these two in one store
forces one of them into the wrong regime.

### Reviewer isolation is a memory question

Independence is usually treated as a question about who reviews. It is also a
question about what the reviewer can read. A reviewer who can query the producer's
search-experience memory inherits the producer's dead ends and the producer's
framing, and the review is anchored rather than independent.

So a memory query carries the store, the task class, the assurance class and the
requesting role, and blind review policy excludes the producer's search and
procedural memory by default. ACC-72 asserts this from the review side; ACC-79
asserts the retention side.

### Failure has to be retrievable

A `FailedApproach` records that something was tried, in what context, why it
failed and what would have to change for a retry to be worth it. Without it the
question "have we tried this?" is answered from a chat log, which means it is
answered inconsistently.

The distinction that gives the record its value is the one WP-144 also draws: a
method that could not be applied and a hypothesis that was tested and not
supported are different outcomes, and only the second is about the science.

### Retention has to prove it can refuse

A decay job that has never been shown to exclude the immutable classes is a job
nobody has tested against the case that matters. The retention run reports what it
excluded and why, and ACC-79 runs it against a deliberately mixed record set with
a planted evidence control that must survive and a planted stale procedure that
must not.

### Baseline v1.3.0 — the read path over the six stores

WP-146 established the stores and their authority. This baseline adds the read
path: `MemoryMask`, `ContextProjection` and proactive intervention (WP-151).

The rule the mask enforces is one the taxonomy implied and did not state:
**`REFUTED`, `SUPERSEDED`, unverified interpretation and stale procedural advice
cannot enter ordinary reasoning context** — while remaining fully visible to a
failure-history query. Those are different questions, and a mask that answered
both the same way would either poison reasoning or destroy the failure record.

Search experience, procedural memory and principle memory still cannot leak into
evidence authority, including through a lesson derived from a failed approach.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-144 — Discovery Search Graph and Candidate Lifecycle](../14_SCIENTIFIC_INTELLIGENCE/wp_144_discovery_search_graph.md) | `SearchNode` · `SearchEdge` · `Candidate lifecycle state machine` · `SearchGraph module` |

### Full prerequisite closure

**70 of 160 packages (44%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 27 | `WP-058` · `WP-064` · `WP-075` · `WP-141` |
| 28 | `WP-062` · `WP-081` · `WP-142` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-082` · `WP-143` |
| 30 | `WP-067` · `WP-144` |
| 31 | `WP-068` |
| 32 | `WP-076` |
| 33 | `WP-077` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-151`
- **Transitively reachable:** **1 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-S — Scientific intelligence |
| Dependency depth | level **34** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Knowledge Lead |
| Independent verifier | Archivist / Internal Audit |
| Gates touched | `G3` · `G5` · `G6` · `G10` |
| Controls | `CTL-DAT-03` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-63 — Failed Experiment Must Be Recorded](../12_ACCEPTANCE_SCENARIOS/acc_63_failed_experiment_recorded.md) | High | It cannot advance until an immutable `ExperimentRun`, a `FailureAssessment` and a `FailedApproach` record exist, carrying the logs and artifacts the failure produced. |
| [ACC-70 — EvidenceGap Lifecycle](../12_ACCEPTANCE_SCENARIOS/acc_70_evidence_gap_lifecycle.md) | High | The wrong evidence does not close the gap; the qualifying evidence satisfies it; the retraction reopens it with its full history intact. An open gap never authorises work by itself. |
| [ACC-79 — Epistemic Memory Retention Violation](../12_ACCEPTANCE_SCENARIOS/acc_79_memory_retention_violation.md) | High | It excludes the immutable classes, reports exactly what it excluded and why, and expires only procedural entries. A planted evidence control survives, and a planted stale procedure does not. |
| [ACC-096 — A Refuted Memory Does Not Re-Enter Reasoning](../12_ACCEPTANCE_SCENARIOS/acc_096_refuted_memory_mask.md) | High | None of the three enters ordinary reasoning context. All three remain fully visible to the failure-history query, because *what did we try* and *what is true* are different questions. |
| [ACC-098 — Memory Poisoning Attempt](../12_ACCEPTANCE_SCENARIOS/acc_098_memory_poisoning_attempt.md) | Critical | The content is stored in a typed store whose authority field forbids claim support. It cannot be retrieved as evidence, cannot support a claim, and a lesson derived from a failed approach is not an accepted fact. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-144 — Discovery Search Graph and Candidate Lifecycle](wp_144_discovery_search_graph.md)
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
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Destructive projection rebuild proof` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
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
- **Knowledge Lead** carries the acceptance decision; **Archivist / Internal Audit** must verify independently of whoever implements.
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
| `ASM-009` — MLEvolve — progressive MCGS, reference edges, cross-branch fusion, stagnation | `ADAPTIVE_REIMPLEMENT` | `MS-SRCH-003` · `MS-SRCH-004` · `MS-SRCH-005` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-014` — PiEvo — evolving principle space and anomaly-aware augmentation | `ADAPTIVE_REIMPLEMENT` | `MS-PRIN-001` · `MS-PRIN-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-019` — DeepScientist — findings memory, failed routes, research map | `ADAPTIVE_REIMPLEMENT` | `MS-MEM-001` · `MS-MEM-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-020` — EvoScientist — ideation memory separated from procedural memory; failure classification | `DEFER` | nothing — recorded so it is not re-examined from scratch | everything — the implementation here is this repository's own | none |
| `ASM-040` — MAD-M2 — memory masking in multi-agent debate | `ADAPTIVE_REIMPLEMENT` | `MS-MEM-003` | the local module and contract surface this becomes — **named at refinement** | **1** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-009` | A reference edge lets one branch read another. It may not alter primary-parent ancestry, which is the credit path evidence lineage depends on. | The controller and runtime, and the reported stagnation thresholds as normative constants — they enter as an initial experimental profile to be calibrated, not as settings to copy. |
| `ASM-014` | A PrincipleVersion is a working belief. It uses a different status vocabulary from ClaimVersion on purpose, and a posterior belief is never an accepted claim. | The Bayesian agent runtime and the Gaussian-process machinery, unless a domain later shows it earns its complexity. |
| `ASM-019` | A FindingRecord is an interpretation of evidence. It never mutates the evidence it interprets, and it is not itself a ClaimVersion. | The autonomous studio runtime and its control loop, which would contend with Temporal. |
| `ASM-020` | N/A — deferred. | Everything, for now. |
| `ASM-040` | A mask decides what enters a reasoning context. It deletes nothing, re-labels nothing, and cannot make a masked item unavailable to a failure-history query. | Chat-memory pruning as the model. Upstream masks turns of a debate; here the same idea generalises to a typed ContextProjection over six canonical stores, which is a different object with different retention rules. |

### Where a plain row would mislead

- **`ASM-009`** — Licence is permissive, so direct adaptation would be legal; it is still reimplemented because the native graph contract — typed SearchEdge, ArtifactRecord candidates, VerifiedValue metrics — matters more than importing the controller.
- **`ASM-014`** — The canonical repository is amair-lab/PiEvo; the address circulating in the source brief (eurekaw/pievo) is a fork, and a fork is not a provenance anchor.
- **`ASM-019`** — The idea worth taking is that a failed route is an asset rather than something to delete — which is what makes 'have we tried this before?' answerable from records instead of from chat history.
- **`ASM-020`** — Named in the source brief but neither the repository nor the licence was confirmed on 2026-08-23. The two ideas attributed to it — separating ideation memory from procedural memory, and classifying why a run failed — are already carried by ASM-019 and by the failure taxonomy in WP-082. Deferred rather than adopted on an unverified attribution.
- **`ASM-040`** — The observation worth taking: an erroneous memory from a previous round degrades later reasoning even after it has been refuted. That is why REFUTED and SUPERSEDED items leave the reasoning context here while staying queryable as history — ACC-096.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-009` — MLEvolve — progressive MCGS, reference edges, cross-branch fusion, stagnation** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-014` — PiEvo — evolving principle space and anomaly-aware augmentation** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-019` — DeepScientist — findings memory, failed routes, research map** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-040` — MAD-M2 — memory masking in multi-agent debate** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**Acquisition readiness — 4 obligations open across 4 of 5 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-146-T01 | Define the six memory type contracts and their authority matrix rows | Implementation owner | Commit / configuration / record reference |
| WP-146-T02 | Define `FindingRecord`, `FailedApproach` and `NegativeResult` | Implementation owner | Commit / configuration / record reference |
| WP-146-T03 | Define `MethodExperience` with freshness, decay and revalidation | Implementation owner | Commit / configuration / record reference |
| WP-146-T04 | Define `SearchExperience` and its separation from the evidence store | Implementation owner | Commit / configuration / record reference |
| WP-146-T05 | Implement the typed `MemoryQuery` API and its role-aware policy | Implementation owner | Commit / configuration / record reference |
| WP-146-T06 | Implement retention and decay jobs with immutable-class exclusion reporting | Implementation owner | Commit / configuration / record reference |
| WP-146-T07 | Implement the G10 impact path across findings, principles and procedures | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Six memory type contracts`
- `FindingRecord`
- `FailedApproach`
- `NegativeResult`
- `MethodExperience`
- `MemoryQuery policy`
- `Retention and revalidation jobs`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-146_epistemic_memory_taxonomy.tests.md`](wp_146_epistemic_memory_taxonomy.tests.md).

- Evidence must be unaffected by any decay job
- A stale procedure must not be presentable as evidence
- A reviewer under blind policy must not reach the producer's search memory
- A source retraction must cascade to findings and principles without deleting artifacts
- A human intervention record must be immutable
- A planted evidence control must survive a mixed-class retention run
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-146_epistemic_memory_taxonomy.acceptance.md`](wp_146_epistemic_memory_taxonomy.acceptance.md), together with what this package still cannot establish.

- [ ] A typed query returns only the stores the requesting role is permitted.
- [ ] The retention job passes a planted never-delete-evidence control and still expires stale procedures.
- [ ] No store other than Evidence can be cited in support of a claim.
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

Retention is reversible only forwards: an expired procedural entry is marked expired rather than removed, and evidence and audit classes are outside the job's reach entirely.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
