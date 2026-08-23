---
title: "WP-143 — Hypothesis and Principle Evolution and Proximity Graph"
aliases:
  - "WP-143"
  - "WP-143 — Hypothesis and Principle Evolution and Proximity Graph"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Hypotheses, the principles beneath them and the assumptions they rest on are immutable versions with explicit evolution operators, and their proximity is a derived read model rather than a source of truth."
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-143_hypothesis_principle_evolution.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g2
  - aethrion/gate/g4
  - aethrion/gate/g6
  - aethrion/state/not-started
---

# WP-143 — Hypothesis and Principle Evolution and Proximity Graph

## Package card

| Field | Value |
|---|---|
| Work package | `WP-143` |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Methodologist / Knowledge Lead |
| Hard dependencies | WP-018, WP-020, WP-030, WP-035, WP-142 |
| Related gates | G2,G4,G6 |
| Related controls | CTL-EPI-01, CTL-EPI-04 |
| Related acceptance scenarios | ACC-57 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_143_hypothesis_principle_evolution.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_143_hypothesis_principle_evolution.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Hypotheses, the principles beneath them and the assumptions they rest on are immutable versions with explicit evolution operators, and their proximity is a derived read model rather than a source of truth.


## Analysis

### What this package actually decides

That a hypothesis has a history. An autonomous system that edits a hypothesis in
place after seeing a result destroys the only record that would show the
hypothesis changed to fit the data — and it destroys it silently, because the
edited version looks exactly like a hypothesis that was always stated that way.

Immutable versions with a named evolution operator make that move visible instead
of impossible to detect. `REFINE_SCOPE`, `ADDRESS_COUNTEREVIDENCE`, `NARROW` and
`GENERALIZE` are not equivalent, and a reviewer reading the chain can see which
one was used and when.

### Why principles are a separate layer from hypotheses

A hypothesis is testable now. A principle is the working belief that made the
hypothesis seem worth testing, and it usually survives several hypotheses. When a
result is surprising, the question is whether one hypothesis failed or whether
something underneath it is wrong, and a model with only one layer cannot express
the difference.

`PrincipleVersion` therefore uses a deliberately different status vocabulary —
PROPOSED, SUPPORTED, CHALLENGED, SUPERSEDED — from `ClaimVersion`. A working
belief with a high posterior is still not an accepted claim, and the two must not
be able to be confused by reading a status field.

### Assumptions are versioned so a broken result names what broke

When a result changes, the useful question is which assumption stopped holding.
`AssumptionVersion` makes assumptions first-class and links them to the protocol,
analysis plan and hypothesis that used them, so the answer is a query rather than
an act of recollection.

### Proximity is derived and priority is not confidence

The hypothesis similarity graph exists for duplicate detection, coverage and
diversity-aware allocation. It is recomputable from canonical records and holds
no truth of its own.

Pairwise ranking has the same status. A tournament that decides which of two
hypotheses is more worth testing next is answering a resource question. The score
it produces is a `SearchPriorityScore`, stored in a different field from anything
epistemic, and converting it into a claim assessment is refused by schema and by
policy rather than discouraged by documentation.

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

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-142 — Study Mode, Bottleneck and Idea Card Model](../14_SCIENTIFIC_INTELLIGENCE/wp_142_study_mode_bottleneck_idea.md) | `StudyModeRecord` · `BottleneckRecord` · `IdeaCard` · `PriorArtCollision` |

### Full prerequisite closure

**51 of 160 packages (32%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 26 | `WP-059` |
| 27 | `WP-141` |
| 28 | `WP-142` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-144`
- **Transitively reachable:** **5 of 160 packages (3%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-S — Scientific intelligence |
| Dependency depth | level **29** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Platform Lead |
| Independent verifier | Methodologist / Knowledge Lead |
| Gates touched | `G2` · `G4` · `G6` |
| Controls | `CTL-EPI-01` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-57 — Hypothesis In-Place Mutation Attempt](../12_ACCEPTANCE_SCENARIOS/acc_57_hypothesis_in_place_mutation.md) | High | The write is refused with a conflict. A successor version is required, and it must name its parent and the evolution operator that produced it. |
| [ACC-64 — Implementation Failure Must Not Refute a Hypothesis](../12_ACCEPTANCE_SCENARIOS/acc_64_implementation_failure_not_refutation.md) | Critical | Both are classified — IMPLEMENTATION and DATA — and any transition that would set `HYP-002` to REFUTED is refused. Only a validly executed run under the frozen plan can support a HYPOTHESIS failure class. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md), [WP-142 — Study Mode, Bottleneck and Idea Card Model](wp_142_study_mode_bottleneck_idea.md)
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
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Destructive projection rebuild proof` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `StudyModeRecord` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `BottleneckRecord` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `IdeaCard` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `PriorArtCollision` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `Gate policy bindings for G0-G2` | `WP-142` | `python3 scripts/progress.py show WP-142` |
| `Mode change deviation procedure` | `WP-142` | `python3 scripts/progress.py show WP-142` |

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
- **Evidence Platform Lead** carries the acceptance decision; **Methodologist / Knowledge Lead** must verify independently of whoever implements.
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
| WP-143-T01 | Define `HypothesisVersion` with parent, operator and immutability rules | Implementation owner | Commit / configuration / record reference |
| WP-143-T02 | Define the evolution operator vocabulary and its review requirements | Implementation owner | Commit / configuration / record reference |
| WP-143-T03 | Define `PrincipleVersion` with its distinct status vocabulary | Implementation owner | Commit / configuration / record reference |
| WP-143-T04 | Define `AssumptionVersion` and its links to protocol and analysis plan | Implementation owner | Commit / configuration / record reference |
| WP-143-T05 | Build the `HypothesisSimilarityEdge` projection and its rebuild path | Implementation owner | Commit / configuration / record reference |
| WP-143-T06 | Type `SearchPriorityScore` so it cannot be written to a claim assessment | Implementation owner | Commit / configuration / record reference |
| WP-143-T07 | Implement the anomaly-to-principle-challenge flow with its review gate | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `HypothesisVersion`
- `PrincipleVersion`
- `AssumptionVersion`
- `HypothesisSimilarityEdge projection`
- `Evolution operator vocabulary`
- `Anomaly to principle challenge procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-143_hypothesis_principle_evolution.tests.md`](wp_143_hypothesis_principle_evolution.tests.md).

- An in-place hypothesis edit must be refused with a conflict
- An evolution must preserve the parent version and name its operator
- A ranking score written to a claim assessment must be refused
- A challenged principle must retain its full history
- The proximity graph must rebuild deterministically from canonical records
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-143_hypothesis_principle_evolution.acceptance.md`](wp_143_hypothesis_principle_evolution.acceptance.md), together with what this package still cannot establish.

- [ ] A multi-generation hypothesis family reconstructs with its evidence and principle ancestry intact.
- [ ] No history is lost by any evolution, challenge or supersession.
- [ ] Priority and confidence are separately typed and cannot be assigned to one another.
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

A superseded hypothesis or principle version is never deleted; a reverted evolution is expressed as a further version referencing what it reverts.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
