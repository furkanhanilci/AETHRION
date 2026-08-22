---
title: "Injecting Controls"
aliases:
  - "injecting-controls"
type: skill
category: skill
status: WORKING
source: "skills/injecting-controls/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/injecting-controls/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: injecting-controls
description: "Use when the lab's own false positive or false negative rate must be measured, or when validating that the research pipeline detects known signals and rejects null data"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G0,G5,G6"
  airl.roles: "Metascience Lead,Red Team Lead"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "ControlInjectionRecord,PipelineIntegrityAlert"
  airl.mechanical_checks: "controls_indistinguishable_from_real,agents_blind_to_control_status"
---

# Injecting Controls

## Core principle

Every other metric is a **process** metric. This is the **outcome** metric: does
the lab produce correct results?

Process metrics tell you the machine ran. Only controls tell you it was right.

## Iron law

> **CONTROL PROJECTS ARE HIDDEN FROM AGENTS.**
>
> Only the Metascience Lead and Red Team Lead know. They must be
> indistinguishable from real projects — otherwise you measure behaviour under
> observation, not behaviour.

## Two control types

| Type | What it is | Expected |
|---|---|---|
| **Positive control** | A question with a known answer | The lab **should find it** |
| **Negative control** | Null data / permuted data — no effect exists | The lab **should find nothing** |

## Rate

**5–10%** of projects are seeded. Too few and there is no statistical power; too
many and the cost is prohibitive.

## What is measured

```
false_positive_rate = "findings" on negative controls / total negative controls
false_negative_rate = missed signals on positive controls / total positive controls
```

And **which gate caught it** is recorded — this feeds gate-yield measurement and
tells you which parts of the assurance stack are earning their cost.

## The one exception: this skill can block

The Metascience plane measures and does not block (Goodhart's law — a measure
that gates becomes a target and stops measuring). **The single exception:**

> **If a negative control produces an "effect", the pipeline is broken.**
> The line stops. No new confirmatory run opens until root cause is found.

A pipeline that finds effects in permuted data will find them anywhere.

## Confidentiality management

- Control status lives in a separate record, not the main database
- It is not flagged in the correlation chain
- If exposed: that control is void, a new one is created, and the leak is recorded

## Ethical boundary

Controls also test **human decision makers**. This is disclosed in advance —
not *which* project is a control, but **that controls exist**. Testing people
without telling them that testing happens is not acceptable; telling them which
test is which destroys the measurement.

## Red flags

- Control projects distinguishable from real ones
- An agent correctly guessing that a project is a control
- FP/FN rate never reported
- A finding on a negative control with the line still running
