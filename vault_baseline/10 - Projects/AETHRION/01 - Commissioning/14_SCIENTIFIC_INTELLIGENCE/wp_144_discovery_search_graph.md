---
title: "WP-144 — Discovery Search Graph and Candidate Lifecycle"
aliases:
  - "WP-144"
  - "WP-144 — Discovery Search Graph and Candidate Lifecycle"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Computational discovery runs as a typed candidate graph with explicit node states and edge classes, so every candidate can say where it came from and whether the change was a repair or a scientific move."
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-144_discovery_search_graph.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/state/not-started
---

# WP-144 — Discovery Search Graph and Candidate Lifecycle

## Package card

| Field | Value |
|---|---|
| Work package | `WP-144` |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer / Chief Architect |
| Hard dependencies | WP-014, WP-019, WP-023, WP-030, WP-082, WP-143 |
| Related gates | G4,G5 |
| Related controls | CTL-DAT-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-58, ACC-64 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_144_discovery_search_graph.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_144_discovery_search_graph.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Computational discovery runs as a typed candidate graph with explicit node states and edge classes, so every candidate can say where it came from and whether the change was a repair or a scientific move.


## Analysis

### What this package actually decides

That the search loop leaves a record a reviewer can read. The alternative — an
agent thinks, edits code, tries again — produces results with no lineage, and a
result whose provenance is a conversation cannot support a claim.

The graph is typed: `SearchNode` carries a state, a candidate artifact, a
workspace and its execution references; `SearchEdge` carries a class.

### Why DEBUG is a separate state from IMPROVE

This is the scientifically load-bearing distinction in the package. A candidate
that fails to run because of a dependency error has not told you anything about
the hypothesis. If the next step is recorded as "tried a new direction", the
system has silently converted an implementation defect into evidence about a
scientific question.

`DEBUG` preserves the scientific direction while the implementation is repaired.
`IMPROVE` changes the mechanism. The two are different node states because they
license different conclusions, and ACC-64 exists to prove the conversion cannot
happen.

### Why edges have classes

`PRIMARY_PARENT` is the ancestry and credit path — it is the spine that lineage
and reproduction depend on, and it must stay acyclic. `REFERENCE` lets a node
consult a sibling branch without changing its ancestry. `FUSION_INPUT` records
that a candidate genuinely inherits from more than one parent.

Collapsing these into one edge type is what makes cross-branch information flow
untraceable: the useful mechanism arrives from somewhere, and nothing records
where. Keeping them separate is what lets ACC-58 assert that a fused candidate
still names both of its sources after an export and a graph rebuild.

### The search graph holds no epistemic authority

A node's metric allocates the next unit of compute. It is never a claim
assessment, never a gate input and never a publication support. Everything the
graph produces enters the evidence path through the same door as everything else:
an immutable artifact, an official run, a raw evaluator output and a verified
value.

### Where this runs

Canonical search records live in the domain store. Temporal remains the
authority over the G4 and G5 transitions and calls the campaign one slice at a
time; the non-deterministic parts — generation, execution, evaluation — live in
activities, never in workflow code, so replay stays deterministic.

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
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md) | `Git policy` · `Worktree controller contract` · `Protected-path rules` · `Freeze procedure` |
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-143 — Hypothesis and Principle Evolution and Proximity Graph](../14_SCIENTIFIC_INTELLIGENCE/wp_143_hypothesis_principle_evolution.md) | `HypothesisVersion` · `PrincipleVersion` · `AssumptionVersion` · `HypothesisSimilarityEdge projection` |

### Full prerequisite closure

**56 of 160 packages (35%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 26 | `WP-059` · `WP-061` |
| 27 | `WP-075` · `WP-141` |
| 28 | `WP-081` · `WP-142` |
| 29 | `WP-082` · `WP-143` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-145` · `WP-146`
- **Transitively reachable:** **4 of 160 packages (2%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-S — Scientific intelligence |
| Dependency depth | level **30** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer / Chief Architect |
| Gates touched | `G4` · `G5` |
| Controls | `CTL-DAT-01` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-58 — Cross-Branch Fusion Lineage](../12_ACCEPTANCE_SCENARIOS/acc_58_cross_branch_fusion_lineage.md) | High | D retains both input references and the named inherited mechanisms end to end — in the canonical graph, after a derived-graph rebuild, and in the export. Neither A nor C is modified. |
| [ACC-64 — Implementation Failure Must Not Refute a Hypothesis](../12_ACCEPTANCE_SCENARIOS/acc_64_implementation_failure_not_refutation.md) | Critical | Both are classified — IMPLEMENTATION and DATA — and any transition that would set `HYP-002` to REFUTED is refused. Only a validly executed run under the frozen plan can support a HYPOTHESIS failure class. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-143 — Hypothesis and Principle Evolution and Proximity Graph](wp_143_hypothesis_principle_evolution.md)
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
| `Git policy` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Worktree controller contract` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Protected-path rules` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Freeze procedure` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Destructive projection rebuild proof` | `WP-030` | `python3 scripts/progress.py show WP-030` |
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
| `HypothesisVersion` | `WP-143` | `python3 scripts/progress.py show WP-143` |
| `PrincipleVersion` | `WP-143` | `python3 scripts/progress.py show WP-143` |
| `AssumptionVersion` | `WP-143` | `python3 scripts/progress.py show WP-143` |
| `HypothesisSimilarityEdge projection` | `WP-143` | `python3 scripts/progress.py show WP-143` |
| `Evolution operator vocabulary` | `WP-143` | `python3 scripts/progress.py show WP-143` |
| `Anomaly to principle challenge procedure` | `WP-143` | `python3 scripts/progress.py show WP-143` |

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
- **Experiment Platform Lead** carries the acceptance decision; **Reproducibility Engineer / Chief Architect** must verify independently of whoever implements.
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
| WP-144-T01 | Define `SearchNode` with its state machine and artifact bindings | Implementation owner | Commit / configuration / record reference |
| WP-144-T02 | Define `SearchEdge` classes and the acyclicity rule on primary parents | Implementation owner | Commit / configuration / record reference |
| WP-144-T03 | Implement DRAFT, DEBUG, IMPROVE and FUSE transitions with policy checks | Implementation owner | Commit / configuration / record reference |
| WP-144-T04 | Bind candidate artifacts and workspaces to nodes | Implementation owner | Commit / configuration / record reference |
| WP-144-T05 | Bind node executions to the run registry and verified values | Implementation owner | Commit / configuration / record reference |
| WP-144-T06 | Build the derived discovery-graph projection and its rebuild | Implementation owner | Commit / configuration / record reference |
| WP-144-T07 | Integrate the campaign slice with the Temporal activity boundary | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `SearchNode`
- `SearchEdge`
- `Candidate lifecycle state machine`
- `SearchGraph module`
- `Discovery graph projection`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-144_discovery_search_graph.tests.md`](wp_144_discovery_search_graph.tests.md).

- A primary-parent cycle must be rejected
- A DEBUG transition must preserve the mechanism identity of its parent
- An implementation failure must not be able to refute a hypothesis
- A FUSE node with fewer than two inputs must be rejected
- A reference edge must not mutate ancestry
- Persistence and replay must reproduce the graph exactly
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-144_discovery_search_graph.acceptance.md`](wp_144_discovery_search_graph.acceptance.md), together with what this package still cannot establish.

- [ ] A synthetic multi-branch search containing debug, improve and fusion rebuilds with complete lineage.
- [ ] Every executed candidate resolves to an immutable artifact and a workspace commit.
- [ ] No search state is the only copy of anything the evidence path needs.
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

A campaign is stopped rather than rolled back: nodes and artifacts are retained, and a superseding campaign references what it supersedes.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
