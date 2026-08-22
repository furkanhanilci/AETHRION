---
title: "Scope Discipline"
aliases:
  - "scope-discipline"
type: skill
category: skill
status: WORKING
source: "skills/scope-discipline/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/shared
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/scope-discipline/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: scope-discipline
description: "Use when writing a report, abstract, conclusion or any prose that states what the research found"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.gates: "G6,G8,G9"
  airl.roles: "Scientific Editor,Scientific Owner,Project Decision Owner"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "ScopeConformanceReport"
  airl.mechanical_checks: "prose_sentence_maps_to_claim,prose_scope_within_claim_scope"
---

# Scope Discipline

## Iron law

> **PROSE MAY NOT EXCEED `ClaimVersion.scope_qualification`.**
>
> A sentence that cannot be mapped to a claim, or whose scope exceeds it,
> blocks publication.

## Why this is mechanical rather than editorial

Overgeneralisation is the most consistent failure mode of language models, and
it is detectable by comparing two structured records. Leaving it to reviewer
judgement means catching it sometimes; making it mechanical means catching it
every time.

## Procedure

1. Extract every assertive sentence from the prose
2. Map each to a `ClaimVersion`
3. Compare the sentence's scope against the claim's `scope_qualification`
4. Qualify or delete any sentence that exceeds it
5. Verify every obligation in `DecisionRecord.obligations` appears in the text

## Scope-overrun patterns

| Prose | Claim | Ruling |
|---|---|---|
| "Consensus is robust" | "robust under synchronous Byzantine conditions with an honest majority" | **OVERRUN** |
| "The method generalises" | tested in one scenario | **OVERRUN** |
| "X causes Y" | correlational evidence only | **OVERRUN** — causal claim |
| "Shown for the first time" | literature review does not establish this | **OVERRUN** — priority claim |
| "Consistently outperforms" | outperformed on 3 of 5 benchmarks | **OVERRUN** — selective |
| "Suggests that X" | interpretive claim, marked | acceptable |

## Where qualification must appear

The scope limit appears **in the title and the abstract**, not only in the
Limitations section. A scope limit deferred to Limitations is not a scope
limit — most readers of an abstract never reach it.

## Rationalization table

| Justification | Ruling |
|---|---|
| "I wrote it in the Limitations section" | **Insufficient.** The assertion itself is qualified. |
| "The reader will infer it from context" | They may not. **Write it.** |
| "Qualified, it sounds weak" | Weak-sounding and correct beats strong-sounding and wrong. |
| "Other papers in the field write it this way" | Their error is not our standard. |
| "The qualification is in the methods section" | Methods are read after the conclusion, if at all. |

## Red flags

- The abstract asserts more strongly than the results section
- The title carries no scope limit while the claim does
- `DecisionRecord.obligations` are unmet
- A sentence maps to no claim at all
