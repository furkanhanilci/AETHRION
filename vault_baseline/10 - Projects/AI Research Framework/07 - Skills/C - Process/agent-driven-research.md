> [!info] Generated view
> This note is generated from `skills/agent-driven-research/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: agent-driven-research
version: 1.0.0
description: Use when dispatching an agent to produce any research artifact, when a produced artifact needs review, or when review findings remain open after fixes
gates: [G2, G3, G5, G6]
roles: [Task Compiler, Assurance Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [independence-discipline, requesting-review, receiving-review]
emits: [TaskContract, ProducerReport, ReviewVerdict, FindingLedger]
mechanical_checks: [no_session_history_passed, artifacts_passed_as_files, finding_ledger_complete]
---

# Agent-Driven Research

## Core principle

Fresh agent per task, plus task-level review, plus a broad final review. High
quality, fast iteration, and — critically — an auditable record of who saw what.

## Dispatch package

Every producer dispatch receives **exactly**:

1. One line placing the task in the project
2. **The task brief file path** — extracted mechanically, with exact values
3. Only the interfaces from prior tasks that this task touches
4. Your resolutions of any ambiguity in the spec
5. The report file path and its contract

**Session history is never passed.** Not as a summary, not as "context".

## Information asymmetry

| | Producer | Reviewer |
|---|---|---|
| Task brief | ✅ | ✅ |
| Global constraints (**verbatim** from spec) | ✅ | ✅ |
| Prior interfaces | ✅ | — |
| Producer's report | writes | ✅ |
| Produced artifact / diff | produces | ✅ |
| **Producer's internal reasoning** | — | ❌ **never** |
| Session history | ❌ | ❌ |

## Dispatch rules

- **Fresh** agent per task
- **One** producer dispatch per task — never parallel producers on the same
  artifact (they conflict, and the conflict is invisible in the record)
- Small, same-shaped work is **batched into one dispatch**
- **No context pasting** — artifacts are handed over as files with hashes, never
  as inline text
- **The producer never dispatches an agent** (see `independence-discipline`)

The file-not-text rule exists so that "what did the reviewer see" has a
verifiable answer. Inline text leaves no hash.

## Escalation ladder

```
Rounds 1–3   Same producer. Context preserved.
             Open findings passed VERBATIM — never summarised.
             Fix report APPENDED to the same file (persistent memory).
             Only the changed portion is re-reviewed.

Rounds 4–5   FRESH producer, MORE CAPABLE model.
             Framing: "A prior producer attempted this N times; you own it now."

Round 5+     ►► BREAKER ◄◄
             Dispatch stops. A human adjudicates each open finding
             individually. Every ruling is written to the ledger.
             SILENT DISCARD IS FORBIDDEN.
```

Passing findings verbatim matters: a summarised finding loses the specific
detail that made it actionable, and the next round addresses a paraphrase.

## Finding ledger

A `DisagreementCase` closes only when **every** ledger row is `RESOLVED` or
`PARKED` with a rationale, an owner and an expiry. Closing with an
unstatused finding is **forbidden**.

## Final review

Separately from task reviews, **one final review over the whole package** on the
most capable available model. A whole assembled from individually-passing parts
can still be inconsistent as a whole.

## Red flags

- Inline text passed to a reviewer
- Findings summarised rather than passed verbatim
- No round counter present
- An unstatused finding in the ledger
- Two producers dispatched against the same artifact
