> [!info] Generated view
> This note is generated from `skills/measuring-agreement/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: measuring-agreement
description: "Use when assigning reviewers or reproducers, when independence must be demonstrated, or when multiple raters produce verdicts"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.adopted_components: "krippendorff · statsmodels (Fleiss κ)"
  airl.gates: "G6,G7"
  airl.roles: "Metascience Lead,Assurance Lead"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "AgreementReport,IndependenceRecord"
  airl.mechanical_checks: "pairwise_error_correlation_computed,quota_rule_enforced"
---

# Measuring Agreement

## Adopted components

> **krippendorff · statsmodels (Fleiss κ)**

Standard estimators. The different-family rule is a **proxy** for measured pairwise error correlation and is retired once the measurement exists.

Adoption type and authority boundary: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Core principle

> **Using a different model family does not guarantee independence.**
>
> Frontier models are trained on heavily overlapping corpora. They can make the
> same error with the same confidence. Two reviewers agreeing carries no
> evidential weight until their error correlation has been measured.

## Iron law

> **`Model Lineage` IS A MEASUREMENT, NOT A DECLARATION.**
>
> Two profiles whose error correlation exceeds the threshold **cannot both count**
> toward the same claim's independence quota.

## Agreement calibration set

A standing set is maintained:
- Review tasks with known correct answers
- Every qualified model profile processes it periodically
- Measured: accuracy, **pairwise error correlation** `ρ`, chance-corrected
  agreement (κ / α)

The set must be refreshed as models change; a stale calibration measures a model
that no longer exists.

## Agreement statistics

| Measure | When |
|---|---|
| Cohen's κ | Two raters, categorical |
| Fleiss' κ | More than two raters |
| Krippendorff's α | Missing data, mixed scales |
| Pairwise error correlation | **Primary measure for the independence quota** |

## Interpretation — alarms in both directions

| Situation | Meaning | Action |
|---|---|---|
| Low agreement | Task ambiguous or criteria unclear | Clarify the criteria |
| Healthy agreement | Expected | — |
| **κ ≈ 1.0** | **Independence is suspect** | Separate the profiles; measure ρ |
| High `ρ` | They make the same mistakes | **Cannot share a quota** |

> Very high agreement is not good news. Independent judges do not agree
> perfectly; perfect agreement means either the task was trivial or the judges
> were not independent.

## Quota rule

```
independent reviewers per claim:
  R1: 1   R2: 2   R3: 3
and the selected profiles' pairwise ρ must be BELOW the threshold
```

Where a pair exceeds the threshold, only one of them counts; the other is an
additional opinion, not an additional check.

## Red flags

- Independence marked `PASS` with no correlation measurement
- The same two profiles paired on every claim
- The calibration set untouched for months
- A quota satisfied by two tiers of the same provider family
