---
name: writing-skills
description: "Use when authoring, editing or reviewing any AETHRION skill, or when a rule keeps being bypassed by agents"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:writing-skills"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.roles: "Metascience Lead,Assurance Lead"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "Skill,BaselineTestRecord"
---

# Writing Skills

## Core principle

A skill is test-driven development applied to documentation. First observe how
an agent fails **without** the skill, then write the minimum text that closes
those specific failures.

## Iron law

> **NO SKILL WITHOUT A FAILING BASELINE TEST FIRST.**

No exceptions: not for "a small addition", not for "just an update", not for
"an untested minor fix". Untested work is deleted and restarted.

## Procedure

**RED** — Run the baseline scenario without the skill. Record the agent's
behaviour and, **verbatim**, the justifications it produces for non-compliance.
Store them under `baselines/`.

**GREEN** — Write the minimum skill that closes exactly those failures. Re-run.
Confirm compliance.

**REFACTOR** — Find the new evasions the skill did not anticipate. Close them
explicitly. Re-test. Repeat until the loophole set stops growing.

## The `description` rule — critical

`description` states **trigger conditions only**, never the procedure.

- ✅ `Use when a ClaimCandidate exists without a linked EvidenceSpan`
- ❌ `Use for evidence extraction — find source, extract span, score confidence`

**Why:** a description that summarises the procedure causes the agent to follow
the summary instead of reading the skill. This is an observed failure mode, not
a style preference. In one documented case a description mentioning "code review
between tasks" produced one review where the skill's own flowchart required two.

## Required sections for discipline skills

- **Iron law** — one sentence, no exceptions clause
- **Rationalization table** — the real justifications observed in baseline
  testing, each with a ruling
- **Red flags** — observable signs the skill was skipped

Weak: *"Ran analysis without a plan? Label it."*

Strong: *"Ran analysis without a plan? It is `exploratory`. Permanently. No
exceptions: not as 'reference', not as 'that was just a pilot', not as 'it was
a small change'."*

The difference is that the strong form names the specific evasions in advance.

## Size limits

Entry skills `<150` words. Frequently loaded `<200`. Others `<500`. A skill is
loaded on every trigger; its size is a tax paid every time.

Heavy reference material belongs in a sibling `procedure.md`, not in `SKILL.md`.

## Composition

Reference dependent skills; do not inline them:

- ✅ `**REQUIRED BACKGROUND:** airl:anchoring-spans`
- ❌ Pasting the other skill's content — this burns context on every load

## Red flags

- A skill with no baseline test → invalid, not merged
- A discipline skill with no rationalization table → will not survive contact
  with a motivated agent
- Several skills authored in a batch without testing each → violation
- A rationalization table containing invented excuses rather than observed ones
