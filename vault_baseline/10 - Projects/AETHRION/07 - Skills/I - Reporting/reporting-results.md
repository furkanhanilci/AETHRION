---
title: "Reporting Results"
aliases:
  - "reporting-results"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/reporting-results/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/reporting-results/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: reporting-results
description: "Use when writing up results, drafting a report or paper section, preparing a publication package, or deciding what a result permits you to say; also when choosing which reporting guideline applies"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G9,G10"
  airl.roles: "Scientific Editor,Scientific Owner,Statistical Methods Owner,Data Steward"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "scope-discipline,evidence-before-claim,calibrating-confidence"
  airl.emits: "PublicationPackage,ScopeConformanceReport"
  airl.mechanical_checks: "every_sentence_resolves_to_a_claim,sentence_scope_within_claim_scope,reporting_checklist_complete,references_resolve"
---

# Reporting Results

## Iron law

> **NO SENTENCE THAT DOES NOT RESOLVE TO A CLAIM, AND NO CLAIM STATED MORE
> BROADLY THAN ITS EVIDENCE.**

A publication sentence must resolve to a `ClaimVersion`, and the sentence's
scope may not exceed that claim's `scope_qualification`. Both are checked
mechanically before a human reads the draft.

## Why this is stricter than ordinary writing advice

The characteristic failure of a model-written report is not a false statement —
it is a **true statement widened one step too far**:

| Evidence supports | The draft says | Verdict |
|---|---|---|
| "8 % improvement on CARLA Town05 under clear weather" | "improves autonomous driving performance" | **Scope violation** — domain, condition and magnitude all dropped |
| "27 of 33 registry sources corroborated" | "the evidence base is verified" | **Scope violation** — existence is not support |
| "the control fired in the positive case" | "monitoring works" | **Scope violation** — one control is not coverage |

Each widening is small. The accumulated distance is the whole problem.

## Procedure

### 1. Choose the reporting guideline before writing

Reporting guidelines are checklists developed by consensus for a study type.
Pick the one that matches, from the EQUATOR Network:

| Study type | Guideline |
|---|---|
| Systematic review | **PRISMA 2020** · search reporting **PRISMA-S** · living review **PRISMA-LSR** |
| Randomised trial | CONSORT · protocol SPIRIT |
| Observational study | STROBE |
| Prediction model, including ML | **TRIPOD+AI** |
| AI in medical imaging | **CLAIM** |
| Early clinical evaluation of an AI decision support system | **DECIDE-AI** |
| Animal research | ARRIVE |

**A guideline is a completeness standard, not a quality standard.** PRISMA says
*report what you did, fully*. It never says *what you did was sound*.

> Evidence to keep in view: eighteen months after TRIPOD+AI was published,
> reporting quality in its target field had **not** measurably improved.
> Publishing a checklist changes nothing; **enforcing it mechanically** does.
> That is why the checklist is a gate here rather than guidance.

### 2. Write the claim before the sentence

For each thing you intend to say: name the `ClaimVersion`, its
`scope_qualification`, and the `EvidenceSpan` or `ExperimentRun` behind it. If
there is no claim, there is no sentence — there is a finding to raise.

### 3. Report uncertainty as it was measured

State which quantity is shown — SD, SEM, 95 % CI, IQR — and never mix them in
one figure or table. **Never manufacture uncertainty** to make a result look
rigorous, and never drop it to make one look clean.

### 4. Report negative and null results in the same voice

Under in-principle acceptance the direction of a result does not change whether
it is reported. A result that did not go the intended way is written up with the
same completeness as one that did.

### 5. Separate what was preregistered from what was not

Anything decided after seeing data is **exploratory**, labelled as such, in the
text and in the claim. This is not a formality: the label is the difference
between a hypothesis test and a description.

### 6. Run the mechanical checks before a human reads it

| Check | Fails when |
|---|---|
| Sentence → claim resolution | any material sentence resolves to nothing |
| Scope conformance | sentence scope exceeds claim scope |
| Reference verification | a citation resolves in no bibliographic authority |
| Reporting checklist | a required item is missing |
| Method–code alignment | the method section does not describe what the code does |

The last three are CoE Audit checks; reference verification is implemented in
`scripts/verify_references.py`.

## Mechanical verification

```bash
uv run python scripts/verify_references.py    # every reference resolves
```

Scope conformance and checklist completeness are G9 gate checks, owned by the
Scientific Editor.

## Rationalization table

| What gets said | Ruling |
|---|---|
| "It's implied by the results section" | **Implication is not resolution.** Name the claim |
| "Broadening it slightly makes the abstract readable" | **That is the failure mode.** Readability never buys scope |
| "The null result isn't interesting enough to report" | **In-principle acceptance already settled this.** Report it |
| "We can label it confirmatory, the plan was basically the same" | **Basically the same is not locked.** It is exploratory |
| "The checklist is a formality" | **It is a gate.** An incomplete checklist blocks G9 |
| "Error bars look better than a bare mean" | **Only if they were measured.** Otherwise they are fabricated |

## Red flags

- A sentence you cannot trace to a claim in under a minute
- A conclusion broader than every result that supports it
- Uncertainty appearing in the text that appears in no analysis
- "Significant" used without a preregistered test behind it
- A citation nobody resolved
- A limitations section that lists nothing a reviewer would care about
