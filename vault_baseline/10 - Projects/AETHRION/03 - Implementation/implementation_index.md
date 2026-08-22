---
title: "Implementation Index"
airl_id: AETHRION-IMPLEMENTATION-INDEX
type: index
category: vault
status: active
summary: "Session handovers and the implementation log — where the last session stopped."
generated: false
tags:
  - aethrion/index
  - aethrion/execution
---

# Implementation Index

The project view of the real implementation steps. The detailed chronology lives
in [[10 - Projects/AETHRION/implementation_log|Implementation Log]].

## What every step record must carry

Each step records these separately:

- what was done
- why it was done
- which WP or ACC it is bound to
- **the evidence and the fresh test output**
- what is still missing
- the exact next step

## Session handovers

A handover is written at the end of a working session so the next session — human
or model — resumes without re-reading the corpus.

| Handover | Ends at commit | Next action |
|---|---|---|
| [[10 - Projects/AETHRION/03 - Implementation/session_handover_2026-08-22|Session Handover — 2026-08-22]] | `cf57f1f` | Decide the role → model assignment |

## Step history

| Step | Date | Status |
|---|---|---|
| Step 005 — File-by-file review of the whole repository | 2026-08-22 | `DOCUMENTATION_COMPLETE` |
| Step 004 — Full English revision of the corpus | 2026-08-22 | `DOCUMENTATION_COMPLETE` |
| Step 003 — Independent audit and target-structure design | 2026-08-22 | `DESIGN_PROPOSED` |
| Step 002 — Central project organisation | 2026-08-21 | `DOCUMENTATION_VISIBLE` |
| Step 001 — Foundation and contract core | 2026-08-22 | `TECH_COMPLETE` |
| Step 000-A…G — Retrospective record | 2026-08-21 | complete |
| [[10 - Projects/AETHRION/03 - Implementation/operations_runbook\|Operations Runbook]] | How do I run and verify the slice? |
| [[10 - Projects/AETHRION/03 - Implementation/executing_a_work_package\|Executing a Work Package]] | What is the loop for running one package? |

## Implementation discipline

A step may reach `TECH_COMPLETE`; reaching `ACCEPTED` depends on an independent
verifier's decision. See [[verification-before-completion]].

> The Bridge is tracked here as **one component** of the framework, not as its
> root.

<!-- generated:folder-maps -->

## The folders the implementation runs on

Each is the repository's own index of a directory: what lives there, what
it is for, and which of it runs.

- [[10 - Projects/AETHRION/03 - Implementation/scripts_index|Scripts]]
- [[10 - Projects/AETHRION/03 - Implementation/tests_index|Tests]]
- [[10 - Projects/AETHRION/03 - Implementation/deployment_index|Deploy]]
- [[10 - Projects/AETHRION/03 - Implementation/claude_harness_index|Harness configuration]]

<!-- /generated:folder-maps -->
