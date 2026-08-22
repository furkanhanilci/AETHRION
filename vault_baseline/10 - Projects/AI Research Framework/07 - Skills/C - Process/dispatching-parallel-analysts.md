> [!info] Generated view
> This note is generated from `skills/dispatching-parallel-analysts/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: dispatching-parallel-analysts
version: 1.0.0
description: Use when the same data can be analysed in more than one defensible way, when multiple independent failures span different subsystems, or when analytic degrees of freedom need measuring
gates: [G6]
roles: [Assurance Lead, Statistical Methods Owner, Metascience Lead]
assurance_classes: [R2, R3]
requires_skills: [independence-discipline, measuring-agreement]
emits: [MultiAnalystReport]
mechanical_checks: [analysts_blind_to_each_other, same_analysis_plan_hash]
---

# Dispatching Parallel Analysts

## Core principle

The same data, the same question, and several defensible analysis paths produce
different answers. That spread is called **analytic degrees of freedom**, and it
is measurable.

Human labs cannot afford to measure it — running the analysis twenty times is
prohibitive. **This lab can.** Treat that as a capability, not a curiosity: it
converts an unquantified source of error into a reported number.

## When to fan out

**Yes:** the analysis paths are genuinely independent and each can proceed
without the others' results.

**No:** the paths are causally linked, or the work requires understanding the
whole system at once. Fanning out dependent work produces confident nonsense in
parallel.

## What each analyst receives

- The same `AnalysisPlanManifest` (same hash)
- The same data (same artifact hash)
- A narrow, **self-contained** brief
- The constraint: **do not see or use any other analyst's output**
- A different model family — with independence **measured**, not assumed
  (`measuring-agreement`)

## Merging results

1. Read every report
2. **Conflict check** — did any two analysts mutate the same intermediate artifact?
3. Produce the **distribution** of results, not a selected point estimate
4. Interpret:

| Distribution | Meaning | Action |
|---|---|---|
| Narrow | Result is insensitive to analytic choice | `reproducibility` dimension rises |
| Wide | Result depends on analysis choice | **Confidence falls**; `scope_qualification` becomes mandatory |
| Bimodal | A genuine methodological disagreement exists | Open a `DisagreementCase` |
| **Extremely narrow (κ ≈ 1.0)** | **Independence is suspect** | Signal to Metascience |

The last row is the counter-intuitive one: near-perfect agreement between
supposedly independent analysts is evidence that they were not independent.

## Multiverse extension

Rather than a single path, run **all defensible paths** — transformations,
covariates, exclusion thresholds — and report the specification curve. This is
the direct defence against p-hacking: if the result only holds on one of forty
defensible paths, the curve shows it.

## Reporting rule

The distribution is reported, always. Reporting only the best-looking analysis
while having run several is selective reporting, whatever the intent.

## Red flags

- One analyst saw another's output
- Only the "best" analysis was reported and the spread was not
- The spread is wide but confidence did not fall
- Analysts differed in model but the correlation was never measured
