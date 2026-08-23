---
title: "Framing Research"
aliases:
  - "framing-research"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/framing-research/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/framing-research/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: framing-research
description: "Use when a research idea arrives, when scope is unclear, or before any protocol, experiment or implementation work begins"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:brainstorming"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G0,G1"
  airl.roles: "Scientific Owner,Project Decision Owner,Knowledge Steward"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "ResearchOpportunity,ProjectCharter,RiskProfile,StudyModeRecord"
  airl.mechanical_checks: "assurance_class_computed_by_policy_engine,duplicate_scan_executed"
---

# Framing Research

## Core principle

No work starts until what will be done, and what will count as success, is
written down.

## Classify first — two axes, not one

Two independent classifications happen here, and collapsing them is the common
error. **Assurance class** answers *how much scrutiny must this survive*.
**Study mode** answers *what kind of statement may this produce at all*. A
feasibility pilot can be R3 and still be unable to license a confirmatory claim.

### Study mode — the claim ceiling

| Mode | What it is | Claim ceiling |
|---|---|---|
| **Feasibility** | Can this be run at all? Does the metric compute, does the data load, does the pipeline survive one pass? | **No claims.** The outcome informs a future protocol; it never becomes evidence for one |
| **Exploratory** | Discovery. Analysis choices may change as the data is seen | Findings labelled `exploratory`, with a deviation trace |
| **Replication** | Re-derivation of an existing result | `ReproductionRecord` |
| **Confirmatory** | Produces new claims | Locked protocol · separate analysis plan · preregistration · frozen evaluator · full G0–G10 |

> **The ceiling moves one way.** It can be lowered by record at any time. It can
> **never** be raised on the same data — once an outcome has been seen, no
> subsequent writing makes the analysis confirmatory. Answering that question
> needs a second study, on data nobody has looked at.

Declare the mode as a `StudyModeRecord` with an external timestamp, before the
first result exists. A mode change creates a successor record plus a deviation
record; it never edits the original.

> **When in doubt, take the heavier assurance class and the *lower* claim
> ceiling.** They move in opposite directions on purpose: more scrutiny is
> cheap to add later, and a claim ceiling raised later is not a ceiling.

### Why feasibility is its own mode rather than a kind of exploratory

Exploratory work produces findings that may be reported as exploratory.
Feasibility work produces the answer *the pipeline runs* — and the most common
way a research record goes wrong is that this answer, plus a number that came
out of it, gets written up afterwards as though it had been predicted.

Naming the mode makes the temptation visible at the moment it is cheapest to
refuse: before the run, not after the number.

## The approval gate never disappears

> **No agent fleet runs, no budget opens, and no protocol freezes before the
> charter is approved.**

The ceremony scales: for exploratory work a two-sentence frame is enough. The
**gate itself** never scales away. This distinction matters because "simple"
tasks are where unexamined assumptions cost the most.

## Procedure

1. **Declare the study mode** — before anything else that could produce a
   number. `StudyModeRecord`, externally timestamped, with the claim ceiling and
   the rationale.
2. **Scan existing work** — duplicate and near-duplicate search via Knowledge
   Steward. A question already answered is not a research project.
3. **Ask one question at a time** — purpose, constraints, success criterion.
   Prefer multiple choice where the option space is known.
4. **Report scope problems immediately** — if the request spans several
   independent subsystems, **split it** rather than accepting a compound project.
5. **Fill the `RiskProfile` vector** (7 dimensions). Leave no field blank.
6. **The policy engine computes `AssuranceClass`** — not a model, not a person.
7. **A human writes the decision question.** An agent may draft it; it may not
   own it.

## Fail-closed classification

```
RiskProfile incomplete            → R3
decision_external_impact ≥ material → R3
safety_critical                   → R3
data_class ∈ {D3, D4}             → R3
fallthrough (ambiguous)           → R2      # NOT R1
```

The fallthrough is R2 rather than R1 deliberately. A default of R1 means every
unclassified project receives the lightest scrutiny — which is exactly backwards.

## Path escalation

If hidden complexity appears mid-project: **stop, announce the upgrade, restart
at the heavier level.** A `RiskReclassificationEvent` is emitted, and gates
already passed at the lighter class are re-evaluated. Escalation is never
retroactively waived because "we already got that far".

## Rationalization table

| Justification | Ruling |
|---|---|
| "Simple question, no charter needed" | **Simple tasks are where assumptions cost most.** The charter shortens; it does not vanish. |
| "We will settle the class later" | Class determines gate depth. **First.** |
| "It looks like R1" | If it merely looks like R1, write R2. Doubt resolves upward. |
| "The user already explained it verbally" | Verbal is not a charter. Write it. |

## Red flags

- The decision question was authored by an agent
- `RiskProfile` has blank fields but the class is R1
- The scope covers several independent subsystems
- No duplicate scan was run
