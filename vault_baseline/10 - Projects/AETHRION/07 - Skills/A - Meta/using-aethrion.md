---
title: "Using AETHRION"
aliases:
  - "using-aethrion"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/using-aethrion/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/shared
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/using-aethrion/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: using-aethrion
description: "Use when starting any AETHRION work — research or software — when unsure which procedure applies, when a gate transition is about to be attempted, or when choosing between the engineering and scientific skill families"
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

# Using AETHRION

## Core principle

No work happens without a procedure. At every step a skill is loaded, and the
skill you loaded is part of the evidence trail.

## First: which family is this?

AETHRION carries **two skill families and one shared core**. Classify before you
start; when the task is both, load from both.

| The task is… | Family | Router entry |
|---|---|---|
| Building AETHRION itself — services, adapters, schemas, scripts, CI | **engineering** (`airl.domain: engineering`, vendored from `obra/superpowers`) | the engineering table below |
| Conducting research through AETHRION — protocol, evidence, claim, review | **scientific-research** | the research table below |
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

## Where to start — engineering (building AETHRION)

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

## Where to start — research (working through AETHRION)

| Situation | Skill |
|---|---|
| A new research idea arrives | `framing-research` |
| Method needs writing | `writing-protocols` → `writing-analysis-plans` |
| A literature campaign starts | `searching-literature` → `screening-sources` |
| Sources must be read from or written to Zotero | `curating-zotero` |
| A claim needs an evidence span | `extracting-evidence` → `anchoring-spans` |
| Anything touches files, state or compute | `using-isolated-environments` |
| An experiment is about to run | `preregistration-discipline` → `executing-experiments` |
| The same data admits more than one defensible analysis | `dispatching-parallel-analysts` |
| Work is being handed to an agent | `agent-driven-research` |
| A packet must be frozen for a reviewer | `building-review-packets` |
| An artifact is ready for review | `requesting-review` |
| You have been assigned as a reviewer | `blind-reviewing` · `adversarial-reviewing` |
| A review verdict arrived | `receiving-review` |
| Verdicts conflict, or a finding will not close | `arbitrating-disagreement` |
| Reviewer agreement needs measuring | `measuring-agreement` |
| The lab's own error rate must be measured | `injecting-controls` |
| A confidence number is produced or displayed | `calibrating-confidence` |
| A result is unexpected | `investigating-anomalies` |
| Fabrication or tampering is suspected | `investigating-integrity-concerns` |
| A result is being written up | `reporting-results` |
| A document must be planned, drafted or rendered | `authoring-research-documents` |
| A figure is about to be made | `producing-figures` |
| A protocol, plan or package needs an external record | `submitting-external-records` |
| A recurring summary is due | `publishing-digests` |
| An external feed must be watched | `monitoring-external-feeds` |
| A human needs to be informed | `notifying-humans` |
| A human decision is required | `routing-decision-requests` |
| You are about to say "done" | `verification-before-completion` |
| A project is closing | `finishing-a-project` |

> **Every skill in the registry appears in one of these tables or in the shared
> list below, and `scripts/check_skill_baseline.py` fails if one does not.**
> Seventeen did not, until v1.3.1. A skill nobody can be routed to never loads,
> so whatever it says is unreachable rather than merely untested — and two of the
> seventeen were the scientific halves of pairs whose engineering counterparts
> *were* routable, which meant a task needing `dispatching-parallel-analysts`
> landed on `dispatching-parallel-agents`. That is the substitution `ADR-012`
> forbids, arrived at not through a bad judgement but through the correct option
> being absent from the table.

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
