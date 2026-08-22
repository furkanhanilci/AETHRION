> [!info] Generated view
> This note is generated from `skills/framing-research/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: framing-research
version: 1.0.0
description: Use when a research idea arrives, when scope is unclear, or before any protocol, experiment or implementation work begins
gates: [G0, G1]
roles: [Scientific Owner, Project Decision Owner, Knowledge Steward]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [ResearchOpportunity, ProjectCharter, RiskProfile]
mechanical_checks: [assurance_class_computed_by_policy_engine, duplicate_scan_executed]
---

# Framing Research

## Core principle

No work starts until what will be done, and what will count as success, is
written down.

## Classify first

| Class | What it is | Output |
|---|---|---|
| **Exploratory** | Feasibility or discovery; produces no claims | Recommendation plus findings labelled `exploratory` |
| **Replication** | Re-derivation of an existing result | `ReproductionRecord` |
| **Confirmatory** | Produces new claims | Full G0–G10 |

> **When in doubt, take the heavier class.** If you cannot decide between two,
> choose the heavier one and downgrade later with evidence.

## The approval gate never disappears

> **No agent fleet runs, no budget opens, and no protocol freezes before the
> charter is approved.**

The ceremony scales: for exploratory work a two-sentence frame is enough. The
**gate itself** never scales away. This distinction matters because "simple"
tasks are where unexamined assumptions cost the most.

## Procedure

1. **Scan existing work** — duplicate and near-duplicate search via Knowledge
   Steward. A question already answered is not a research project.
2. **Ask one question at a time** — purpose, constraints, success criterion.
   Prefer multiple choice where the option space is known.
3. **Report scope problems immediately** — if the request spans several
   independent subsystems, **split it** rather than accepting a compound project.
4. **Fill the `RiskProfile` vector** (7 dimensions). Leave no field blank.
5. **The policy engine computes `AssuranceClass`** — not a model, not a person.
6. **A human writes the decision question.** An agent may draft it; it may not
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
