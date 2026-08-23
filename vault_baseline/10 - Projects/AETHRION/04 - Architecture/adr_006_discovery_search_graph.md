---
title: "ADR-006 — The Discovery Search Graph Holds No Epistemic Authority"
aliases:
  - "ADR-006"
cssclasses:
  - aethrion-decision-record
type: decision-record
category: architecture
status: ACCEPTED
summary: "Automated discovery — generate a candidate, run it, look at the number, try again — is the part of an AI research system that works best and produces the least defensible record."
source: "docs/architecture/ADR-006_discovery_search_graph.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
  - aethrion/adr
---

> [!info] Generated view
> This note is generated from `docs/architecture/ADR-006_discovery_search_graph.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# ADR-006 — The Discovery Search Graph Holds No Epistemic Authority

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | How computational discovery is structured, and the boundary between searching and knowing |
| Sibling documents | `AETHRION_ARCHITECTURE.md` · WP-144 · WP-145 · WP-143 · ADR-007 · ACC-58 · ACC-59 · ACC-64 |
| Status | **ACCEPTED — 2026-08-23.** Structure decided; nothing is built |
| Date | 2026-08-23 |

**In one paragraph.** Automated discovery — generate a candidate, run it, look at
the number, try again — is the part of an AI research system that works best and
produces the least defensible record. The loop is effective and its output is a
conversation: a result arrives with no lineage, and nobody can say which change
produced it or whether the previous attempt failed because the idea was wrong or
because the code did not compile. This record fixes the structure as a typed
graph, and fixes the one boundary that matters more than the structure: **a
search score allocates compute and never becomes a confidence.**

---

## 1. The decision

> **Discovery runs as a typed candidate graph.** Nodes carry a state — `DRAFT`,
> `DEBUG`, `IMPROVE`, `FUSE` — an artifact, a workspace and its executions.
> Edges carry a class — `PRIMARY_PARENT`, `REFERENCE`, `FUSION_INPUT`.
> **Every number the graph produces is a search priority.** Writing one into a
> `ClaimVersion`, a `VerifiedValue`, a `GateRecord` or a publication is a
> forbidden conversion, refused by schema and by policy rather than discouraged
> by documentation.

---

## 2. Why `DEBUG` is a state and not a comment

This is the scientifically load-bearing decision in the record, and it looks like
an implementation detail.

A candidate fails to run — a syntax error, a missing dependency, an out-of-memory
kill. Nothing has been learned about the hypothesis. If the next step is recorded
as "tried a different approach", the system has silently converted an
implementation defect into evidence about a scientific question, and the
resulting record is indistinguishable from one where the idea genuinely failed.

`DEBUG` preserves the scientific direction while the implementation is repaired.
`IMPROVE` changes the mechanism. They are different states because they license
different conclusions:

```
DRAFT ──executes?──┬── no ──► DEBUG ──repaired──► same mechanism, new node
                   │              └── attempts exhausted ──► FailedApproach
                   │                                          (IMPLEMENTATION)
                   └── yes ─► IMPROVE ──► different mechanism, new node
                                 └──► FUSE ──► mechanisms from ≥2 branches
```

**Only a validly executed run under the frozen plan can support a `HYPOTHESIS`
failure class.** ACC-64 plants a compile error, a corrupted dataset and a genuine
preregistered null result, and requires the three to be classified differently.

---

## 3. Why edges have classes

`PRIMARY_PARENT` is the ancestry and credit path. It is the spine that lineage,
reproduction and evidence export depend on, and it must stay acyclic.

`REFERENCE` lets a node consult a sibling branch without changing its ancestry —
the mechanism that makes cross-branch information flow possible at all.

`FUSION_INPUT` records that a candidate genuinely inherits from more than one
parent.

Collapsing these into a single edge type is what makes a good result
untraceable: the useful mechanism arrived from somewhere, and nothing records
where. ACC-58 requires a fused candidate to still name both sources after an
export **and** after a derived-graph rebuild, because a lineage that survives one
but not the other is not lineage.

### Fusion must name what it inherits

Asking a model to "combine these two candidates" returns an opaque result with no
provenance. A `FusionProposal` therefore names which mechanism comes from which
parent, what interaction is expected and what would falsify it. The fused
candidate is a new node; its inputs are unchanged, digests included.

---

## 4. Search priority is not confidence

The graph produces several numbers, and none of them is epistemic:

| Number | What it means | What it is not |
|---|---|---|
| Selection score | which node to expand next | how likely the approach is to be right |
| Normalised rank | the same, comparable across tasks | a measurement |
| Tournament rank | which hypothesis is more worth testing | which hypothesis is more likely true |
| Frontier metric | the best result so far in this campaign | a verified value |

Normalisation is necessary because raw metrics differ by orders of magnitude
between tasks, and un-normalised values make search dynamics an artefact of
units. It also makes the separation easy to state: **a normalised search reward
has no unit and no referent outside this campaign, and cannot be written anywhere
a result belongs.**

Results reach the evidence path through the same door as everything else — an
immutable artifact, an official run against a frozen evaluator, a
`RawEvaluatorArtifact` and a `VerifiedValue` (ADR-007). The graph produces
candidates; it does not produce findings.

---

## 5. Stopping is a control, not an outcome

An unbounded search is not a research method. The campaign stops on cost, rounds,
experiment count, compute, convergence patience or detected stagnation, and each
stop produces a `CampaignStopRecord` naming which one fired.

The rule that matters is what a stop *means*: **`STOPPED_BY_BUDGET` satisfies no
gate.** A campaign that ran out of money has demonstrated nothing, and the record
has to make that impossible to misread — ACC-09 and ACC-59.

Budget reserved for VERIFY, FULL and G7 reproduction cannot be consumed by
exploration. A campaign that spends its reproduction budget on search produces
results nobody can check, which is a worse outcome than producing fewer results.

---

## 6. Determinism where no model is involved

Given the same graph snapshot and the same policy configuration, node selection,
fusion eligibility and stagnation detection must return the same decision. These
are arithmetic. Arithmetic that varies between runs cannot be replayed, audited or
debugged, and a campaign that cannot be replayed cannot be reproduced.

This is also the boundary with the control plane. Temporal owns the G4 and G5
transitions and calls the campaign one slice at a time; generation, execution and
evaluation are non-deterministic and live in activities, never in workflow code.

---

## 7. Consequences

**Accepted:** the graph is more expensive to write to than a list of attempts.
Four node states, three edge classes and an artifact per candidate is real
overhead on every iteration.

**Accepted:** search will sometimes be slower than an unconstrained loop, because
a promotion a threshold refused cannot be taken on a model's recommendation.

**Gained:** every candidate can answer where it came from, whether the change was
a repair or a scientific move, what code changed and what official value resulted.

**Gained:** implementation failure and hypothesis failure are separable, which is
the difference between a research record and a build log.

**Rejected:** an unstructured agent loop with a transcript as its record. It is
faster, and its output cannot support a claim.

---

## 8. Decision

**Accepted, 2026-08-23.** The structure is the contract WP-144 and WP-145
deliver. **Nothing is built** — there is no search graph, no selector, no
governor and no campaign runtime, and the mechanisms behind the selection and
fusion policies are recorded in `provenance/upstreams.json` as decisions on paper
under ADR-004.
