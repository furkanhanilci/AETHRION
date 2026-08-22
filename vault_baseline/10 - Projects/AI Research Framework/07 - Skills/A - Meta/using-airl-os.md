> [!info] Generated view
> This note is generated from `skills/using-airl-os/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: using-airl-os
description: "Use when starting any AIRL-OS work — research or software — when unsure which procedure applies, when a gate transition is about to be attempted, or when choosing between the engineering and scientific skill families"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:using-superpowers"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G0,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10"
  airl.roles: "all"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
---

# Using AIRL-OS

## Core principle

No work happens without a procedure. At every step a skill is loaded, and the
skill you loaded is part of the evidence trail.

## First: which family is this?

AIRL-OS carries **two skill families and one shared core**. Classify before you
start; when the task is both, load from both.

| The task is… | Family | Router entry |
|---|---|---|
| Building AIRL-OS itself — services, adapters, schemas, scripts, CI | **engineering** (`airl.domain: engineering`, vendored from `obra/superpowers`) | the engineering table below |
| Conducting research through AIRL-OS — protocol, evidence, claim, review | **scientific-research** | the research table below |
| Either — completion, independence, evidence, scope, human contact | **shared** | applies to both, always |

**Research adaptations extend their engineering counterparts; they do not
replace them.** `preregistration-discipline` is what TDD becomes when the
artefact is a claim rather than a function — but building the Claim Ledger is
still `test-driven-development` work.

Classify on **two axes**, and when in doubt take the heavier value on each:

```
research_mode:  exploratory | replication | confirmatory
execution_path: spike | bounded | architectural
```

## Where to start — engineering (building AIRL-OS)

| Situation | Skill |
|---|---|
| A feature or fix is about to be written | `test-driven-development` |
| The shape of the work is unclear | `brainstorming` |
| Work needs breaking into tasks | `writing-plans` → `executing-plans` |
| Implementation is handed to agents | `subagent-driven-development` |
| Independent work can run in parallel | `dispatching-parallel-agents` |
| A bug will not resolve | `systematic-debugging` |
| The workspace must be isolated | `using-git-worktrees` |
| Code is ready for review | `requesting-code-review` → `receiving-code-review` |
| A branch is closing | `finishing-a-development-branch` |

## Where to start — research (working through AIRL-OS)

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

## Shared discipline — loaded regardless of family

`verification-before-completion` · `independence-discipline` ·
`evidence-before-claim` · `scope-discipline` · `writing-skills` ·
`notifying-humans` · `routing-decision-requests` · `escalating-and-paging` ·
`receiving-external-messages`

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
- You are writing production code and have loaded only research skills — or
  running an experiment having loaded only engineering skills
