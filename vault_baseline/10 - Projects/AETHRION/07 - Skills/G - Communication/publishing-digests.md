---
title: "Publishing Digests"
aliases:
  - "publishing-digests"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/publishing-digests/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/publishing-digests/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: publishing-digests
description: "Use when producing a recurring status summary, portfolio report, cost report or metascience report for humans"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G10"
  airl.roles: "Notification Broker,Metascience Lead,FinOps Lead"
  airl.assurance_classes: "R1,R2,R3"
  airl.requires_skills: "notifying-humans"
  airl.emits: "DigestReport"
  airl.mechanical_checks: "read_only_sources,dlp_scan_passed,no_decision_embedded"
---

# Publishing Digests

## Core principle

A digest is a **read-only derivative**. It carries no decision and changes no
state.

## Rhythm

| Frequency | Content | Audience |
|---|---|---|
| **Daily** | Open decisions, SLA risk, yesterday's runs, budget, attention-budget usage | Decision Owner |
| **Weekly** | Portfolio state, gate flow, blocked work, open findings | All roles |
| **Monthly** | **Metascience**: calibration, agreement, gate yield, control FP/FN, claim survival | Assurance + Metascience |
| **Quarterly** | Cost deep-dive, model requalification, incident review | FinOps + Platform |

## Daily digest — required sections

```
1. Awaiting decision   → count, oldest pending, SLA risk
2. Blocked gates       → which project, which blocker, which owner
3. Open CRITICAL findings → count and age
4. Budget              → utilisation, remaining to hard limit
5. Completed yesterday → runs, reviews, decisions
6. Attention budget    → decisions made this week / quota
```

## Monthly metascience digest — the most valuable one

```
- Confidence calibration: Brier score, per dimension
- Reviewer agreement: κ and pairwise error correlation; pairs breaking quota
- Gate yield: real findings caught per gate, and unit cost
- Control injection: false positive / false negative rate
- Claim survival: 6 / 12 / 24-month survival rate
- Human decisions: time distribution, reversal rate, dissent-override rate
```

> **This report is the lab's report card.** If it looks bad, it is not hidden.
> It appears at the top, not in an appendix. A report card that only shows good
> months is not a report card.

## Rules

- Sources are read-only; producing a digest changes no state
- The data-class ceiling applies exactly as in `notifying-humans`
- Numbers shown are the **calibrated** ones; `UNCALIBRATED` fields are shown as
  such, never as numbers
- Bad news is not buried — it leads

## Red flags

- Digest generation changed a state
- `UNCALIBRATED` fields presented as numbers
- The monthly metascience digest has never been produced
- Poor metrics appear only in an appendix
