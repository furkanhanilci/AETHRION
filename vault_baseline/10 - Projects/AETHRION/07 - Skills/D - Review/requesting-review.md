> [!info] Generated view
> This note is generated from `skills/requesting-review/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: requesting-review
description: "Use when an artifact is ready for independent assessment, before any gate transition that requires review, or when a claim needs a verdict"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:requesting-code-review"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G2,G6,G9"
  airl.roles: "Assurance Lead,Engineering Owner,Scientific Owner"
  airl.assurance_classes: "R1,R2,R3"
  airl.requires_skills: "building-review-packets,independence-discipline"
  airl.emits: "ReviewPacket,ReviewVerdict"
  airl.mechanical_checks: "packet_hash_recorded,reviewer_independence_verified"
---

# Requesting Review

## Core principle

A reviewer receives a **standalone package** — never session history, never the
producer's reasoning.

## Package contents

| Included | Excluded |
|---|---|
| A short statement of what was produced | The producer's workspace |
| `ProtocolManifest` and `AnalysisPlanManifest` hashes | Intermediate logs |
| Aggregate metrics | Model reasoning traces |
| Figure digests (`spec_hash` + `data_hash` + renderer) | Self-scores |
| Claim drafts | Producer identity or contact |
| **Exclusion-rule application record** | Prior reviews and their verdicts |
| Global constraints, **verbatim** | Anything not on the allowlist |

The package is handed over as **files with hashes**. Inline text is not passed —
because inline text leaves no record of what was actually seen.

## Severity tiers

| Tier | Meaning | Action |
|---|---|---|
| **Critical** | Work cannot proceed | Fix immediately; the gate is BLOCKED |
| **Important** | The next step cannot begin | Resolve at this gate |
| **Minor** | Recorded | Documented for later |

## What the reviewer assesses

- Soundness of method
- Sufficiency **and diagnosticity** of evidence
- Whether claim scope matches what the data permits
- Reproducibility from the manifests as given
- Error risk and edge cases

## Output format

```
1. Strengths
2. Findings — grouped by severity, each with location and rationale
3. Assessment — ACCEPT | CONDITIONAL_PASS | REJECT
4. If CONDITIONAL_PASS: conditions, individually numbered
```

Conditions must be numbered because the producer answers each one separately
(`receiving-review`). An unnumbered block of conditions cannot be tracked to
closure.

## Review early, review often

Do not defer review to the end. Early review prevents findings from compounding,
and the producer's context is still fresh when the fix is made.

## Red flags

- Packet hash not recorded → what the reviewer saw is unauditable
- Reviewer assigned by the producer
- Conditions not numbered
- Supplementary information given to the reviewer outside the packet
