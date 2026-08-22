> [!info] Generated view
> This note is generated from `skills/screening-sources/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: screening-sources
version: 1.0.0
description: Use when candidate sources must be included or excluded, when a literature set is being narrowed, or before freezing a LiteratureSetManifest
gates: [G3]
roles: [Evidence Lead]
assurance_classes: [R1, R2, R3]
requires_skills: [searching-literature]
emits: [ScreeningDecision, LiteratureSetManifest]
mechanical_checks: [every_exclusion_has_reason, criteria_locked_before_screening]
---

# Screening Sources

## Core principle

Inclusion criteria are locked **before** screening. If they change afterwards,
screening restarts.

## Iron law

> **EVERY EXCLUSION CARRIES A REASON.**
>
> An unexplained exclusion cannot be written to `90_Excluded`.

## Two-stage screening

**Stage 1 — Title and abstract.** Fast, inclusive. **When in doubt, include.**
**Stage 2 — Full text.** Decisive. Every exclusion receives a reason code.

The asymmetry is intentional: a wrongly excluded source at stage 1 is never seen
again, while a wrongly included one is caught at stage 2.

## Active learning for large sets

For hundreds or thousands of candidates, use active-learning screening: the
human labels a sample, the model ranks the remainder, the human continues down
the ranking.

**The stopping rule is written in advance** — for example, "no inclusions in the
last N records". The model's ranking does not decide when to stop; the human
does, against the pre-written rule.

## Reason codes

| Code | Meaning |
|---|---|
| `DUPLICATE` | Another representation of the same source |
| `OUT_OF_SCOPE` | Not relevant to the research question |
| `WRONG_POPULATION` | Different context or sample |
| `NO_FULLTEXT` | Not obtainable (**the retrieval attempt is recorded**) |
| `RETRACTED` | Withdrawn |
| `LANGUAGE` | Outside the language policy |
| `INSUFFICIENT_METHOD` | Method reporting too thin to assess |

## Double screening (R2, R3)

Two independent screeners; disagreements go to a third. **Agreement is measured**
(`measuring-agreement`). Low agreement means the criteria are ambiguous — clarify
them and re-screen rather than arbitrating case by case.

## Flow report

Candidates → duplicates → stage 1 exclusions → stage 2 exclusions → included,
with counts and a reason distribution at each stage.

## Red flags

- Criteria changed during screening
- A high `NO_FULLTEXT` rate with no retrieval attempt recorded
- Agreement not measured in double screening
- Stage 1 applied strictly (exclusions that should have been stage 2)
