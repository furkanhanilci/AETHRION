---
title: "Verification Before Completion"
aliases:
  - "verification-before-completion"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/verification-before-completion/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/shared
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/verification-before-completion/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: verification-before-completion
description: "Use before any statement implying work is done, correct, passing, ready, complete, or before any gate transition request"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:verification-before-completion"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G0,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10"
  airl.roles: "all"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.mechanical_checks: "fresh_command_execution,exit_code_captured"
---

# Verification Before Completion

## Iron law

> **NO COMPLETION CLAIM WITHOUT FRESH VERIFICATION EVIDENCE.**

## Procedure

1. **Identify** the command that would prove the claim
2. **Execute** it fresh — not from memory, not from a previous run, not from
   another agent's report
3. **Read** the full output: exit code, failure count, warnings
4. **Confirm** the output actually supports the claim being made
5. **Report** with the evidence attached to the claim

Step 4 is the one most often skipped. A command that runs successfully does not
automatically prove the thing you are claiming — check that it tests what you
say it tests.

## What counts as evidence

| Claim | Accepted evidence |
|---|---|
| Tests pass | Fresh run showing `0 failures`, exit 0 |
| Schema is valid | Validator output, 0 errors |
| Artifact is intact | Recomputed SHA-256 equals the manifest value |
| Anomaly is resolved | The original symptom no longer reproduces |
| Criterion is met | Line-by-line checklist against the stated criterion |
| Service is healthy | Fresh request and its response body |

## Forbidden language before verification

"should work", "probably correct", "appears to", "most likely", "Great!",
"Perfect!", "Done" — and **trusting an agent's report without independent
confirmation**.

These are not style objections. Each one is a claim of fact stated without the
fact having been checked.

## Rationalization table

| Justification | Ruling |
|---|---|
| "I ran it a moment ago" | **Run it fresh.** State can change between runs, including because of your own edits. |
| "The agent reported it passed" | **An agent report is not evidence.** Verify it yourself. |
| "Something this simple cannot break" | Simplicity is not a verification exemption. |
| "A partial check is enough" | A partial check yields a partial claim. State the partial claim instead. |
| "There is no time" | Then there is no claim. Leave the status at `IN_PROGRESS`. |
| "The previous step passed, so this one must" | Adjacent success is not evidence. |
| "It worked in a different environment" | Then verify it in this one. |

## Red flags

- A report with no exit code
- "Tests pass" with no output beside it
- Evidence that consists of another agent's prose
- A claim whose verifying command you cannot name
