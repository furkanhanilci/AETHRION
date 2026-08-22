---
name: writing-analysis-plans
description: "Use before any data is analysed, when defining decision rules for results, or when the statistical approach is being chosen"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G2,G4"
  airl.roles: "Statistical Methods Owner"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.emits: "AnalysisPlanManifest"
  airl.mechanical_checks: "locked_before_execution,decision_rules_precommitted"
---

# Writing Analysis Plans

## Core principle

The protocol says **what we measure**. The analysis plan says **how we decide**.
They are locked separately.

## Why separate

If they are combined, the door stays open to changing the decision rule after
seeing the result. In clinical research the Statistical Analysis Plan is a
separate artifact locked before unblinding for exactly this reason — the
separation is the control, not the paperwork.

## Required content

| Field | What it states |
|---|---|
| `primary_endpoint` | One primary outcome measure. One. |
| `secondary_endpoints` | Ordered list — nothing may be added later |
| `decision_rule` | Which value leads to which decision |
| `power_analysis` | Minimum detectable effect and its assumptions |
| `n_and_stopping` | Repetitions, seed matrix, stopping rule |
| `multiplicity` | Multiple-comparison correction |
| `missing_data` | Policy for missing or failed observations |
| `deviation_policy` | What happens when the plan is deviated from |
| `tolerance` | Separate definitions for G7a and G7b (below) |

## Tolerance — two distinct definitions

- **G7a Reproduction:** same manifest, same seed, same image digest →
  **deterministic**. Tolerance is effectively zero, not a percentage.
- **G7b Replication:** different seed, different implementation, different
  environment → **distributional comparison** (confidence-interval overlap or an
  equivalence test). A single point-estimate percentage is not used.

Conflating these two is the most common error in reproducibility claims. A
"±2% match" statement is meaningless without saying which of the two it refers to.

## Locking

The plan hash is recorded **before any result exists**, and the timestamp
evidence is anchored externally (WP-139). Internal timestamps prove ordering
only to someone who already trusts this system.

## Rationalization table

| Justification | Ruling |
|---|---|
| "The analysis is already in the protocol" | Separate hash, separate lock. **Write it again.** |
| "Power analysis needs pilot data" | Pilot data comes from a separate `exploratory` run, never from the main data. |
| "We will choose the primary endpoint later" | **One primary endpoint, chosen in advance.** Everything else is secondary. |
| "Multiple-comparison correction is overkill at this scale" | The Statistical Methods Owner decides that, not the implementer. |
| "We can reuse the plan from the last project" | Reuse is fine; re-locking is still required, with this project's numbers. |

## Red flags

- More than one "primary" endpoint
- No power analysis but a fixed sample size
- Tolerance stated as a single percentage
- Plan and results committed together
