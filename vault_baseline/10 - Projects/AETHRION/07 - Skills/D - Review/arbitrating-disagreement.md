---
title: "Arbitrating Disagreement"
aliases:
  - "arbitrating-disagreement"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/arbitrating-disagreement/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/arbitrating-disagreement/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: arbitrating-disagreement
description: "Use when reviewer verdicts conflict, when a producer disputes a finding, or when a finding remains open after repeated fix rounds"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G6"
  airl.roles: "Assurance Lead,Arbiter"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "agent-driven-research"
  airl.emits: "DisagreementCase,FindingLedger,ArbitrationRecord"
  airl.mechanical_checks: "finding_ledger_complete,round_counter_present"
---

# Arbitrating Disagreement

## Core principle

Disagreement is not a malfunction. It is the moment the system produces
information. It may not close silently.

## Iron law

> **NO OPEN FINDING MAY CLOSE WITHOUT A STATUS.**
>
> Every finding is either `RESOLVED`, or `PARKED` with a rationale, an owner and
> an expiry.

## Delphi rounds — instead of a single arbiter

```
Round 1  N reviewers give independent verdicts with reasoning.
         They do NOT see each other.

Round 2  An anonymised summary of the reasoning is distributed.
         Anyone may revise their verdict.
         ►► ANYONE WHO CHANGES MUST STATE WHY ◄◄

Round 3  Still no convergence → human Arbiter.
         The Arbiter sees ALL rounds — not just the final state.
```

**Convergence is measured.** The rate of verdict change between rounds is
recorded. Very rapid convergence indicates herding and is itself a signal to
Metascience, not a success.

A single arbiter is a single point of failure — and if that arbiter is a model,
it carries its own biases into the resolution.

## The Arbiter's questions

1. **Locator check** — did the verdicts look at the same evidence?
2. **Definitional alignment** — is the disagreement about a term rather than a fact?
3. **Scope** — would a scope restriction dissolve it?
4. **Counter-test** — what single additional observation would settle it?

Question 2 resolves a surprising share of disagreements. Question 4 is what
converts an argument into an experiment.

## Resolution forms

| Resolution | When |
|---|---|
| `ACCEPT` | The finding is invalid or already satisfied |
| `QUALIFIED_ACCEPT` | A scope restriction resolves the disagreement |
| `REJECT` | The finding is valid and cannot be remedied |
| `ADVERSARIAL_COLLABORATION` | The disagreement is real and deep |

## Adversarial collaboration — the R3 default

When arbitration cannot resolve it: **the two sides jointly design** the
experiment that would settle the matter, and write down **in advance** what each
possible outcome would mean.

It is expensive. It is also the only resolution that cannot be decided by
looking at the result afterwards — which is precisely why it is the default at R3.

## Breaker

If findings remain open at the end of round 5: dispatch stops, **a human rules
on each finding individually**, and every ruling is written to the ledger.

## Red flags

- The Arbiter saw only the final verdicts
- A reviewer changed verdict without stating why
- A case closed with unstatused ledger rows
- Full agreement in a single round (κ ≈ 1.0)
