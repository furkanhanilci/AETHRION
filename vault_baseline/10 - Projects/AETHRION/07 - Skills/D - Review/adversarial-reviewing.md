---
title: "Adversarial Reviewing"
aliases:
  - "adversarial-reviewing"
type: skill
category: skill
status: WORKING
source: "skills/adversarial-reviewing/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/adversarial-reviewing/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: adversarial-reviewing
description: "Use when assigned as adversarial reviewer, when a claim needs the strongest possible counter-case, or when competing hypotheses must be discriminated"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G2,G6"
  airl.roles: "Adversarial Reviewer,Red Team Lead"
  airl.assurance_classes: "R2,R3"
  airl.requires_skills: "blind-reviewing"
  airl.emits: "ReviewVerdict,ACHMatrix"
  airl.mechanical_checks: "all_hypotheses_enumerated,diagnosticity_scored"
---

# Adversarial Reviewing

## Core principle

Your task is not to support the claim but to **try to break it**. If you cannot,
the claim is stronger for it. That is not your failure — it is the system
working.

## Your metric

> **You are measured on the quality of your rejections, not the speed of your
> approvals.**
>
> Finding nothing is a valid outcome — but only if you actually looked.

This inversion is deliberate. A reviewer rewarded for throughput approves; a
reviewer rewarded for finding real problems looks for them.

## ACH — Analysis of Competing Hypotheses

1. **Enumerate all plausible hypotheses** — not just the author's. Include the
   mundane ones: measurement error, selection bias, artifact, chance, reverse
   causation, confounding.
2. **List all the evidence**
3. **Build the matrix:** each evidence item × each hypothesis →
   `consistent` / `inconsistent` / `irrelevant`
4. **Score diagnosticity:** evidence consistent with every hypothesis is
   **worthless**
5. **Eliminate** the hypotheses with the most inconsistencies; rank the remainder

> ACH inverts the usual logic: not *"what does this support?"* but
> **"what does this rule out?"** Support accumulates easily and proves little;
> elimination is what moves belief.

## Attack surfaces

| Surface | Question |
|---|---|
| Causation | Is correlation being presented as causation? |
| Selection | Do the exclusion rules shape the result? |
| Power | Is the test capable of falsifying the claim? |
| Generalisation | Is the tested condition the claimed condition? |
| Measurement | Is the measured quantity the claimed quantity? |
| Independence | Are the evidence items genuinely independent of each other? |
| Multiplicity | How many tests were run, and how many reported? |
| Reverse causation | Could the direction be the other way round? |
| Survivorship | What is missing from the data because it did not survive? |

## Pre-mortem (before G4)

> *"A year has passed. This project failed completely. Why?"*

Shifting from future to past tense breaks defensive reasoning — the question is
no longer "could this fail?" but "what did fail?". The resulting items are added
to `falsification_plan`.

## Red flags

- You only evaluated the author's hypothesis
- You did not score diagnosticity
- You did not list the mundane explanations
- Your findings are all stylistic rather than substantive
