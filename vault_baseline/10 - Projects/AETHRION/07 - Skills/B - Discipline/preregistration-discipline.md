> [!info] Generated view
> This note is generated from `skills/preregistration-discipline/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: preregistration-discipline
description: "Use when any analysis is about to run, when a confirmatory claim is being drafted, or when analysis choices are being changed after seeing results"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.derived_from: "superpowers:test-driven-development"
  airl.upstream_commit: "b36e0829c6d0140e93cfef2ca599b1b07d4a7797"
  airl.gates: "G2,G4,G5,G6"
  airl.roles: "Scientific Owner,Statistical Methods Owner,Engineering Owner"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "writing-analysis-plans"
  airl.emits: "AnalysisPlanManifest,ClaimVersion"
  airl.mechanical_checks: "plan_hash_precedes_result_timestamp,claim_labeled_exploratory_or_confirmatory"
---

# Preregistration Discipline

## Iron law

> **NO CONFIRMATORY CLAIM WITHOUT A LOCKED PREREGISTRATION.**
>
> Any result computed before the plan was locked is permanently relabelled
> `exploratory`.

## Why this is stricter than its coding equivalent

In code, work written before the test can be deleted. In research, **you cannot
un-see a result.** The penalty is therefore not deletion but permanent
relabelling: that analysis can never be `confirmatory`, at any later point, by
any subsequent action.

## Procedure

**FREEZE** — Lock the `AnalysisPlanManifest`. It states what each possible
result will mean, which test applies, the exclusion rules, and the stopping
rule. Record its hash. Anchor the hash externally (see WP-139) so the ordering
is provable to someone who does not trust this system.

**SEVERITY** — Confirm the falsification plan is genuinely discriminating: *if
the claim were false, would this test actually catch it?* A test that would not
catch a false claim produces no evidence when it passes.

**EXECUTE** — Follow the plan exactly.

**REPORT** — List every deviation explicitly. Any analysis outside the plan is
`exploratory`, and is reported as such in the same document rather than in a
footnote.

## Exploratory is not a lesser status

Exploratory work is how hypotheses are generated and is genuinely valuable. The
discipline is not "avoid exploratory work" — it is "never present exploratory
work as confirmatory". Mislabelling is the offence, not exploration.

## Rationalization table

| Justification | Ruling |
|---|---|
| "The analysis plan is already implied by the protocol" | **Implication is not a lock.** `AnalysisPlanManifest` is a separate hash. |
| "I could not know which test was appropriate without seeing the data" | **Correct — and that is exactly why it is `exploratory`.** Label it and continue. |
| "This is only a small covariate addition" | **There is no such thing as a small change here.** Every post-lock change is exploratory. |
| "The pilot analysis was exploratory; the real one follows the plan" | If the pilot used the same data, they are not independent. **Both are exploratory.** |
| "There is schedule pressure" | G5 does not start before the plan is locked. |
| "The result is unambiguous anyway" | Clarity is not a preregistration exemption. |
| "I wrote the hypothesis down, just not formally" | An unhashed, untimestamped note is not a preregistration. |

## Verification checklist

- [ ] Every confirmatory claim has a locked `AnalysisPlanManifest`
- [ ] The plan hash was recorded **before** any result existed, with external
      timestamp evidence
- [ ] The falsification test was assessed for severity, not just presence
- [ ] Every deviation from the plan is listed in the report
- [ ] Every out-of-plan analysis is labelled `exploratory`
- [ ] If blinded analysis applied, the unblinding record exists

If you cannot tick all of these, the claim cannot be `confirmatory`.

## Red flags

- Analysis plan and results appear in the same commit
- The hypothesis reads as though it was written after the results (HARKing)
- An exclusion rule was added after the results were seen
- A claim is labelled `confirmatory` with no plan hash recorded
