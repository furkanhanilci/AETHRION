---
title: "Finishing a Project"
aliases:
  - "finishing-a-project"
type: skill
category: skill
status: WORKING
source: "skills/finishing-a-project/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/finishing-a-project/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: finishing-a-project
description: "Use when work appears complete, when a project is about to be closed, published, superseded, retracted or abandoned"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:finishing-a-development-branch"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G8,G9"
  airl.roles: "Project Decision Owner,Assurance Lead"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "verification-before-completion,scope-discipline"
  airl.emits: "DecisionRecord,PublicationPackage"
  airl.mechanical_checks: "all_verifications_green,exact_confirmation_word_received"
---

# Finishing a Project

## Core principle

Closure is not a presentation sign-off. **If verification is red, the menu is
never shown.**

## Closure checklist

1. **Run the full verification suite** — fresh
   - Tests, schema checks, mechanical forensics (statcheck, GRIM)
   - Scope conformance
   - Manifest and hash integrity
   - **If any is red: STOP and report.** Do not proceed to step 2.
2. **Capture environment state** — which target, which bundle versions
3. **Confirm the base reference** — which manifest this derives from
4. **List open findings** — is any ledger row unstatused?
5. **PRESENT THE MENU TO THE HUMAN**
6. Apply the choice
7. Clean up — evidence excepted

## The human menu

| Option | Result |
|---|---|
| `ACCEPT` | `DecisionRecord` signed; proceeds to G9 |
| `CONDITIONAL_ACCEPT` | Accepted with scope restriction; `obligations` recorded |
| `REVISE` | Specific changes requested; the return gate is named |
| `ADDITIONAL_EVIDENCE` | Further runs or reviews requested |
| `REJECT` | Only for protocol violation, integrity concern, or G7 failure |

> **`REJECT` may not be justified by "the result was not what I hoped for".**
> Where an in-principle acceptance exists, the direction of the result is not a
> valid ground for rejection. This is the mechanism that keeps negative results
> in the literature.

## Exact-word confirmation for destructive actions

These are authorised **only** when the exact word is typed:

| Action | Required word |
|---|---|
| Retract a claim | `RETRACT` |
| Supersede a publication | `SUPERSEDE` |
| Abandon a project | `ABANDON` |
| Unfreeze a literature set | `UNFREEZE` |
| Submit an external record | `SUBMIT` |

> "Yes remove it", "sure, cancel it", "go ahead" are **not** authorisation.

The rule exists because these actions are irreversible and an approximate
agreement is easy to produce by accident — or to fabricate.

## Timeout

When a decision SLA expires there is **no auto-approve.** It escalates one level
or the workflow pauses. Silence is not consent.

## Red flags

- The menu was presented while verification was red
- A decision was requested without listing open findings
- A destructive action taken without the exact word
- Decision time anomalously short (see attention-budget telemetry)
