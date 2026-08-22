> [!info] Generated view
> This note is generated from `skills/investigating-integrity-concerns/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: investigating-integrity-concerns
version: 1.0.0
description: Use when fabrication, falsification or plagiarism is suspected, when a mechanical forensic check fails, or when data cannot be traced to a source
gates: [G5, G6, G7, G8, G9, G10]
roles: [Research Integrity Officer]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [IntegrityCase]
mechanical_checks: [statcheck, grim, grimmer, citation_entailment, artifact_hash]
---

# Investigating Integrity Concerns

## Core principle

Fabricated citations and fabricated numbers are the best-documented failure mode
of language models. In an AI-operated lab this risk **increases**, not decreases
— and it arrives looking exactly like competent work.

## Iron law

> **AN INTEGRITY CONCERN HALTS ANY GATE.**
>
> The Research Integrity Officer reports independently of the Assurance Lead and
> may stop any gate. Independent reporting matters: an integrity concern about
> work the Assurance Lead approved cannot route through the Assurance Lead.

## Mechanical triggers — no human interpretation required

| Check | What it catches |
|---|---|
| **statcheck** | Reported test statistic inconsistent with the reported p-value |
| **GRIM** | A reported mean that is **impossible** given N and granularity |
| **GRIMMER** | The same for standard deviations |
| **SPRITE** | Reconstructs plausible data from mean + SD + N |
| **Citation entailment** | Quote **not present** in the source span |
| **Artifact hash** | Manifest and bytes disagree |
| **Benford** | Digit-distribution anomaly |

Any red result opens an `IntegrityCase` **automatically**. This is deliberate:
these checks are cheap, deterministic, and not subject to the social cost of a
human raising a concern.

## Lifecycle

```
ALLEGED → TRIAGED → INVESTIGATING → SUBSTANTIATED    → CLOSED
                                  ↘ UNSUBSTANTIATED  → CLOSED
```

## Procedure

1. **Preserve** — freeze the relevant artifacts. Nothing is deleted or corrected
2. **Scope** — which claims, which runs, which model profile
3. **Reproduce** — repeat the mechanical check independently
4. **Go to source** — the primary source, never the producer's cache
5. **Rule** — `SUBSTANTIATED` / `UNSUBSTANTIATED`
6. **Apply consequences**

Step 1 comes first for a reason: the natural instinct on discovering an error is
to fix it, and fixing it destroys the evidence of how it arose.

## After `SUBSTANTIATED`

- Affected claims → `RETRACTED`
- The producing **model profile** → `SUSPENDED` in the Capability Registry
- All prior outputs from that profile are screened
- An `ImpactCase` opens; dependent publications are notified
- The event is recorded for Metascience

## After `UNSUBSTANTIATED`

The record closes and is **retained**. The person or process that raised the
concern is not penalised. The false-positive rate is tracked by Metascience — a
system that punishes false alarms stops receiving true ones.

## Red flags

- A mechanical check is red but no case was opened
- An artifact was modified before the case opened
- The case was closed by the same role that produced the output
- A pattern of concerns clustering on one model profile, unexamined
