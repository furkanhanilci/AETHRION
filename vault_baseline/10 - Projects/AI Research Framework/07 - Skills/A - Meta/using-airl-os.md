> [!info] Generated view
> This note is generated from `skills/using-airl-os/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: using-airl-os
version: 1.0.0
description: Use when starting any AIRL-OS work, when unsure which procedure applies, or when a gate transition is about to be attempted
gates: [G0, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10]
roles: [all]
assurance_classes: [R1, R2, R3]
non_waivable: true
---

# Using AIRL-OS

## Core principle

No work happens without a procedure. At every step a skill is loaded, and the
skill you loaded is part of the evidence trail.

## Where to start

| Situation | Skill |
|---|---|
| A new research idea arrives | `framing-research` |
| Method needs writing | `writing-protocols` → `writing-analysis-plans` |
| An experiment is about to run | `preregistration-discipline` → `executing-experiments` |
| Work is being handed to an agent | `agent-driven-research` |
| An artifact is ready for review | `requesting-review` |
| A review verdict arrived | `receiving-review` |
| A result is unexpected | `investigating-anomalies` |
| Fabrication or tampering is suspected | `investigating-integrity-concerns` |
| A human needs to be informed | `notifying-humans` |
| A human decision is required | `routing-decision-requests` |
| You are about to say "done" | `verification-before-completion` |
| A project is closing | `finishing-a-project` |

## The three invariants

1. **Agents produce, machines verify, humans decide.** This order is never
   inverted. An agent may recommend a decision; it may not make one.
2. **Nothing is complete without fresh verification evidence.** Not memory, not
   a prior run, not another agent's report.
3. **When in doubt, take the heavier path.** Missing or ambiguous information
   resolves to the highest assurance class, never the lowest.

## What this system is defending against

Not incompetence — plausibility. A model-run lab can produce work that looks
rigorous, cites real-looking sources, reports precise-looking numbers, and is
wrong. Every gate, every mechanical check, and every independence requirement
exists to make that failure mode visible rather than invisible.

## Red flags

- You cannot name the skill currently loaded → stop and read this file
- A gate transition looks "obviously fine" → the gate record is still produced
- You are about to report a result you have not independently verified
- You are about to accept another agent's claim without checking it
