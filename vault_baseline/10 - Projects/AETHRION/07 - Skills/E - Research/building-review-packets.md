---
title: "Building Review Packets"
aliases:
  - "building-review-packets"
type: skill
category: skill
status: WORKING
source: "skills/building-review-packets/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/building-review-packets/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: building-review-packets
description: "Use when assembling a frozen packet for any reviewer, reproducer or arbiter"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.adopted_components: "PaperBench three-container pattern"
  airl.gates: "G6,G7"
  airl.roles: "Assurance Lead,Platform"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "ReviewPacket"
  airl.mechanical_checks: "allowlist_enforced_in_code,packet_hash_recorded,no_inline_context"
---

# Building Review Packets

## Adopted components

> **PaperBench three-container pattern**

The producer builds in one container, reproduction runs fresh in a second, grading happens in a third. The producer's environment never travels to the reproducer.

Adoption type and authority boundary: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Iron law

> **THE PACKET IS BUILT BY A PROGRAM, NOT BY A PROMPT.**

The allowlist is defined in code, has tests, and is enforced by ACL. It does not
expand because a human or an agent says "include this too".

## Why

**What the reviewer saw** is part of the evidence chain. A prompt-assembled
packet cannot be audited; a program-assembled packet can be hashed. The
difference is whether "the reviewer had access to X" is a checkable statement or
a recollection.

## Allowlist — what enters

```
protocol_manifest_hash
analysis_plan_hash
literature_set_hash
aggregated_metrics          # distribution summaries
figure_digests              # spec_hash + data_hash + renderer_version
claim_drafts
global_constraints          # VERBATIM from the spec
exclusion_rule_application  # which record was excluded, under which rule
```

## Denylist — what never enters

```
producer_worktree
intermediate_logs
model_reasoning_traces
self_scores
producer_identity / contact
other_reviewers_verdicts
session_history
```

## Exclusion transparency

A reviewer who sees only aggregate metrics **cannot audit selective exclusion**.
So `exclusion_rule_application` **is** in the packet: which record, under which
pre-specified rule, was excluded.

This is the resolution of the tension between context isolation and
auditability. Isolation hides the producer's *reasoning*; it must not hide the
producer's *choices*.

## Delivery

- **Files plus hashes.** Inline text is forbidden
- Access list, creation and expiry timestamps
- Download tracking enabled
- `packet_hash` written into the resulting `ReviewVerdict`

## Red flags

- The packet was assembled by hand
- `packet_hash` not recorded
- Supplementary information given to the reviewer in conversation
- A denylist item present in the packet
- Exclusion records absent while exclusions were applied
