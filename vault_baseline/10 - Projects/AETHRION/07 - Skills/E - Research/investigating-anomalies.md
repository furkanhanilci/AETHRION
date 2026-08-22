---
title: "Investigating Anomalies"
aliases:
  - "investigating-anomalies"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/investigating-anomalies/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/investigating-anomalies/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: investigating-anomalies
description: "Use when a result is unexpected, when a run fails, when metrics disagree between runs, or when data looks wrong"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:systematic-debugging"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G5,G6,G7"
  airl.roles: "Engineering Owner,Statistical Methods Owner,Research Software Engineer"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "AnomalyRecord,ProtocolChallenge"
  airl.mechanical_checks: "reproduced_before_explained,no_exclusion_without_root_cause"
---

# Investigating Anomalies

## Iron law

> **NO ANOMALY MAY BE "FIXED" OR EXCLUDED WITHOUT ROOT-CAUSE INVESTIGATION.**

An exclusion applied without understanding the cause is not data cleaning. It is
result shaping — and it is indistinguishable from result shaping in the record.

## Four phases

**Phase 1 — Root cause**
1. Read the error and warning output **in full**
2. **Reproduce the anomaly consistently** — if you cannot reproduce it, it is an
   observation, not yet an anomaly
3. Check recent changes: code, data, environment, model, policy
4. Add instrumentation **at pipeline boundaries** — where does it break?
5. Trace the data **backwards to its source**

**Phase 2 — Pattern**
1. Find the **working** runs of the same condition
2. Read the reference **completely**, not partially
3. List **every** difference: seed, node, version, data slice, ordering
4. Extract the assumptions and dependencies

**Phase 3 — Hypothesis**
1. State it specifically: *"X is the root cause because Y"*
2. Test it with the **smallest possible** change
3. Verify the result
4. If it fails, form a **new** hypothesis — do not stack fixes

**Phase 4 — Implementation**
1. First a failing verification run
2. **One** fix, aimed at the root cause
3. Regression check
4. The anomaly run receives its own `run_id`; it is not merged into the main
   result set

## The three-fix rule

> **If three explanation attempts have failed, STOP.**
> What is in question is not the implementation but the **`ProtocolManifest`**.
> → Open a `ProtocolChallenge`; consider returning to G2.

And the second signal: **if every fix produces a new problem in a different
area**, the problem is in the model, not the measurement. Continuing to patch
past that point produces a system nobody understands.

## Labelling

Anomaly investigation runs as **`exploratory`**. No fix arising from it
retroactively alters a `confirmatory` result.

## Rationalization table

| Justification | Ruling |
|---|---|
| "Clearly an outlier" | Outlier status is not a root cause. **Why is it an outlier?** |
| "Probably hardware noise" | "Probably" is not evidence. Show it. |
| "It went away on re-run" | **It did not go away, it hid.** Find the difference between the two runs. |
| "No time — let's exclude it" | Apply the exclusion rule if it was pre-specified. If not, no exclusion. |
| "It's a known flake" | Then it has a known cause. Cite it. |

## Red flags

- The anomaly was explained without being reproduced
- An exclusion rule was added **after** the anomaly appeared
- A third fix attempt with no `ProtocolChallenge`
- Anomaly runs merged into the main result set
