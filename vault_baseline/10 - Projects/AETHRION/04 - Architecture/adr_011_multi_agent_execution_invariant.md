---
title: "ADR-011 — Substantial Scientific Execution Stays Multi-Agent"
aliases:
  - "ADR-011"
cssclasses:
  - aethrion-decision-record
type: decision-record
category: architecture
status: ACCEPTED
summary: "Every efficiency pressure on a multi-agent system points the same way: fewer agents."
source: "docs/architecture/ADR-011_multi_agent_execution_invariant.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
  - aethrion/adr
---

> [!info] Generated view
> This note is generated from `docs/architecture/ADR-011_multi_agent_execution_invariant.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# ADR-011 — Substantial Scientific Execution Stays Multi-Agent

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | Whether one cognitive actor may carry a substantial scientific task alone, and what independence means when it may not |
| Sibling documents | `ADR-001` (independence with one operator) · `AETHRION_ROLES.md` §1.1 · WP-148 · WP-147 · ACC-081 · ACC-082 |
| Status | **ACCEPTED — 2026-08-23.** Invariant decided; no collaboration plane exists |
| Date | 2026-08-23 |

**In one paragraph.** Every efficiency pressure on a multi-agent system points the same way: fewer
agents. It is the largest single cost lever, it is trivially measurable, and the
quality loss is often small enough to argue about. This record refuses that lever
— not because agents are good, but because the reason for having more than one
here is epistemic rather than operational, and a cost argument cannot answer an
epistemic requirement. Optimisation is redirected at what is actually wasteful:
the conversation between them.

---

## 1. The decision

> **Substantial scientific execution requires at least two epistemically
> independent cognitive contributions before synthesis.** Optimisation targets
> the communication graph, the context each actor sees and the verification
> route — **never the cohort itself.** A single-agent downgrade of a substantial
> task is refused at compile time, not warned about.

---

## 2. Why the cost lever is the wrong one

The case for cutting agents is real: coordination is expensive, most inter-agent
messages carry little, and a strong model alone often scores close to a team.

The case against is that **this system's failure mode is not low capability, it
is plausibility** — fluent, well-cited, confident output that is wrong and that
no amount of further capability detects from the inside. That is the sentence the
whole architecture follows from, and it has a structural consequence: a second
independent look is not redundancy, it is the only mechanism that sees what the
first one could not.

Cutting the cohort to save tokens trades the thing the system exists for against
the thing it costs. Cutting the *conversation* costs nothing epistemic, and the
published work on communication pruning suggests most of it is recoverable —
which is `ADR-013`'s subject.

---

## 3. What "independent" means, and what it does not

**Two instances of the same model, given the same context, are one contribution.**
They will agree, and the agreement carries no information. Independence is
therefore recorded as a profile rather than counted:

| Dimension | Question |
|---|---|
| Cognitive function | Are they applying different kinds of scrutiny — methodologist, statistician, skeptic? |
| Evidence exposure | Did they derive from the same evidence, or from different subsets? |
| Peer visibility | Did the second see the first's output before forming a position? |
| Model profile | Different family, provider, snapshot — necessary, and on its own not sufficient |
| Prompt perspective | Different framing, or the same framing twice? |

A `CognitiveDiversityProfile` records all five. **Model-instance multiplicity
alone does not satisfy the invariant**, and ACC-081 tests exactly that: a cohort
of five identical profiles is refused where a cohort of three differentiated ones
passes.

---

## 4. Independent-first, because order is the whole mechanism

Peer output is hidden for round zero. Each actor produces an
`InitialPositionArtifact`; the artifacts are sealed; only then are material
differences exposed for targeted exchange.

The reason is that anchoring is not a preference, it is an effect. An actor shown
a confident prior answer converges on it, and the record afterwards shows two
agreeing actors — indistinguishable from two that independently agreed. Sealing
the first position is what makes the difference visible later.

**Convergence is not a majority vote.** A cohort converges when no material
methodological challenge is unresolved, no critical evidence contradiction is
open, and every protocol blocker is closed or explicitly escalated. Four actors
agreeing does not close a skeptic's unanswered objection — ACC-090.

---

## 5. What this costs, stated plainly

More tokens, more latency, more orchestration surface, and more places for a
coordination bug to live. `ADR-013` and WP-150 exist to recover most of the token
cost; none of them recovers the latency, and a cohort is genuinely slower than
one actor.

The exchange being made: **throughput for the ability to detect a confident
wrong answer.** Where a task is not substantial — a formatting pass, a
mechanical extraction, an exploratory sketch with no claim ceiling above
`FEASIBILITY` — the invariant does not apply, and applying it there would be
ceremony rather than assurance.

---

## 6. Consequences

**Accepted:** the Task Compiler gains real work. It must compile a cohort, a
diversity profile, a communication topology and a context projection, not just a
skill list.

**Accepted:** a cost optimiser will eventually propose reducing the cohort, and
the answer has to be a refusal rather than a judgement call. That is why this is
an ADR and not a guideline.

**Gained:** "was this reviewed independently?" becomes a query against a profile
rather than an assertion in prose.

**Rejected:** single-agent default with optional review. Optional independent
review is independent review that does not happen under deadline.

---

## 7. Decision

**Accepted, 2026-08-23.** The invariant is the contract WP-148 delivers. **No
collaboration plane exists** — there is no cohort record, no scheduler, no
diversity profile and no Task Compiler to emit them.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-004`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
