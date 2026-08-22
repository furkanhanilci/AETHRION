---
title: "Escalating and Paging"
aliases:
  - "escalating-and-paging"
type: skill
category: skill
status: WORKING
source: "skills/escalating-and-paging/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/shared
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/escalating-and-paging/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: escalating-and-paging
description: "Use when an SLA is breached, when a budget hard limit is hit, when a pipeline integrity alert fires, or when a decision has been pending beyond its deadline"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.gates: "G0,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10"
  airl.roles: "Notification Broker,SRE Lead,Assurance Lead"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "notifying-humans"
  airl.emits: "EscalationRecord"
  airl.mechanical_checks: "no_auto_approve_on_timeout,escalation_chain_followed,acknowledgement_required"
---

# Escalating and Paging

## Iron law

> **A TIMEOUT NEVER BECOMES AN AUTOMATIC APPROVAL.**
>
> It escalates one level, or the workflow pauses.

## Escalation chain

```
Implementer → Package Owner → Workstream Lead
            → Chief Architect / Assurance / Safety (by topic)
            → Project Decision Owner
            → Executive Sponsor / Commissioning Board
```

**Acknowledgement is required at every level.** An unacknowledged escalation
rises to the next level; it does not expire quietly. This is what prevents an
alert from being "handled" by being ignored.

## Triggers and severity

| Trigger | Severity | Channel |
|---|---|---|
| Gate SLA exceeded by 1 day | WARN | Email |
| Gate SLA exceeded by 3 days | HIGH | Telegram + email |
| Budget at 80% | WARN | Email |
| **Budget hard limit** | **CRITICAL** | Push + Telegram + email; **work stops** |
| Third fix attempt on an anomaly | HIGH | Assurance Lead |
| **Integrity concern** | **CRITICAL** | Research Integrity Officer, directly |
| **Finding on a negative control** | **CRITICAL** | Line stops; Metascience Lead |
| `ORPHANED` evidence | CRITICAL | ImpactCase + Knowledge Steward |
| Tool Broker error rate above threshold | HIGH | SRE |
| Sandbox escape attempt | **CRITICAL** | Security; line stops |
| Periodic job silently stopped | HIGH | SRE (see `service liveness`) |

## Quiet hours

A quiet-hours policy exists — **but `CRITICAL` cuts through it.** Integrity,
security and budget hard-stops do not wait for morning.

## Noise control

Repeated escalations for the same event are **coalesced**, not resent.

> **Escalation fatigue is more dangerous than the escalation itself.** A team
> that has learned to ignore alerts is worse off than one with no alerts, because
> it believes it is covered.

Measured: mean response time per escalation, unacknowledged rate, false-positive
rate. High false positives means **retuning thresholds** — never disabling them.

## Rationalization table

| Justification | Ruling |
|---|---|
| "Nobody is responding — let's proceed" | **No.** Pause, or escalate a level. |
| "It's night, we'll look in the morning" | `CRITICAL` does not observe quiet hours. |
| "They already know" | Without an acknowledgement record, they do not. |
| "This threshold is too sensitive, disable it" | **Tune it by measurement.** Do not disable. |

## Red flags

- A state advanced by itself after an SLA expiry
- A `CRITICAL` notification suppressed during quiet hours
- An unacknowledged escalation that never rose a level
- A threshold disabled rather than retuned
