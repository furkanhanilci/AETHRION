> [!info] Generated view
> This note is generated from `skills/calibrating-confidence/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: calibrating-confidence
description: "Use when confidence scores are produced or displayed, when a claim reaches a terminal outcome, or when confidence numbers need interpreting"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G6,G8,G10"
  airl.roles: "Metascience Lead,Statistical Methods Owner"
  airl.assurance_classes: "R1,R2,R3"
  airl.emits: "CalibrationReport"
  airl.mechanical_checks: "raw_and_calibrated_stored,uncalibrated_flag_when_insufficient_data"
---

# Calibrating Confidence

## Core principle

An unmeasured confidence score is decoration. And decoration is exactly what
**false rigor** consists of.

## Iron law

> **AN UNCALIBRATED SCORE IS NOT DISPLAYED AS A NUMBER.**
>
> Without sufficient outcome data, the field reads `UNCALIBRATED`. Fake
> precision is forbidden.

The difference between `0.95` and `0.87` means nothing until it has been
measured. Displaying it anyway transfers unearned certainty to the reader.

## Two fields, one truth

```yaml
confidence_dimensions:
  entailment:
    raw: 0.90            # the model's raw output
    calibrated: 0.72     # calibrated against outcomes
    n_outcomes: 47       # how many outcomes informed this
    status: CALIBRATED   # CALIBRATED | UNCALIBRATED
```

## Calibration loop

1. **Record the prediction** — raw scores at claim creation
2. **Wait for the outcome** — G7 verification, G10 survival
3. **Score it** — Brier score plus a calibration curve
4. **Recalibrate** — isotonic regression or Platt scaling
5. **Publish** — which dimension is how trustworthy

## Combination rule — no multiplying, no averaging

The seven dimensions are neither independent nor commensurable. Multiplying
produces an artificially low number; averaging produces an artificially high one.
Both are arithmetic performed on quantities that do not support it.

> **Weakest link:** `claim_strength = min(calibrated_dimensions)`,
> and **which dimension binds** is displayed alongside it.

A claim is exactly as strong as its weakest evidential dimension. Naming that
dimension is more informative than any composite.

## Interpreting Brier

| Brier | Meaning |
|---|---|
| Low | Well calibrated — the numbers carry information |
| High + overconfident | Compress the scores |
| High + underconfident | Expand the scores |

## Red flags

- Three-decimal precision with no `n_outcomes`
- `raw` equal to `calibrated`
- Seven dimensions collapsed into one via multiplication
- Calibration never refreshed after the first fit
