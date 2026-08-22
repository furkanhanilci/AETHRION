> [!info] Generated view
> This note is generated from `docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# AIRL-OS — Ideal Structure Proposal, Contributions and Architecture Review

| Field | Value |
|---|---|
| Document type | Architectural contribution + design audit |
| Input | `AIRL-OS-Architecture.md` v1.0 (3,434 lines), `planning/commissioning/` (186 files), `obra/superpowers` |
| Sibling document | `AIRL_OS_SKILL_LAYER.md` — the operational skill layer (full Superpowers integration) |
| Author | Claude Opus 5 (independent) |
| Date | 2026-08-22 |
| Status | Proposal — awaiting a human decision |

**In one paragraph.** This document reviews the target architecture against what a rigorous laboratory would need and proposes what is missing: seven durable roles, ten review mechanisms, a metascience plane that measures the laboratory's own error rate, the operational discipline worth taking from agent engineering practice, and a tool stack. It closes with the gaps in the current design, ranked, and an implementation order. It is a **proposal** throughout except where a later decision record overrides it.

> **Reading order:** Section C (the 7th plane) and Section D (role → model) are
> the spine of this document. Sections A and B are a contribution catalogue;
> Section G is the audit of the existing design.
> If you are short of time: **C → D → G.**

---

> **Adoption note, 2026-08-22.** Several proposals below now have an adopted
> external standard behind them rather than a format to invent — see
> [`AIRL_OS_EXTERNAL_STANDARDS.md`](AIRL_OS_EXTERNAL_STANDARDS.md): G3 reporting
> (PRISMA 2020 / PRISMA-S / PRISMA-LSR and a preregistered screening stopping
> rule) and evidence attestation (in-toto + Sigstore + Rekor, which resolves the
> storage half of C1 as **WP-000**) are decided; the claim model
> (nanopublication / micropublication / SEPIO), run provenance (Workflow Run
> RO-Crate), evidence appraisal (GRADE, RoB 2, ROBINS-I) and the G8 assurance
> case (CAE / GSN) are queued with reasons. A narrative, diagrammed overview of
> the whole system is in [`AIRL_OS_ARCHITECTURE.md`](AIRL_OS_ARCHITECTURE.md).

## 0. What this document does

The existing `AIRL-OS-Architecture.md` is **a strong architecture**. The division
of authority is right, the Temporal/LangGraph separation is right, the Tool
Broker pattern is right, and the re-anchoring state machine is of a quality
rarely seen.

This document does three things:

1. **Adds** — roles, review mechanisms and tools that exist in real research
   organisations and are absent from your plan.
2. **Proposes a structural addition** — the current architecture measures *the
   research*; it does not measure *the laboratory's own capacity to produce
   correct results*. For that I propose a **seventh plane**.
3. **Audits** — it extracts the gaps in the current design relative to that ideal
   structure.

**The central thesis:** in a laboratory operated by models, "independent review"
cannot be an *assumption*. It has to become **a measured quantity**.

---

# PART A — Roles added

Your current structure: 6 durable functions plus a temporary project cell
(Decision Owner, Scientific Owner, Evidence Lead, Engineering Owner, Assurance
Lead, Safety/Data Owner).

Roles that exist in real research organisations and are missing here:

## A1. Statistical Methods Owner — 🔴 critical

**Real-world counterpart:** the biostatistician in clinical research. They write
the **SAP** (Statistical Analysis Plan) and lock it before unblinding. The data
is not opened until the SAP is locked. This role is **blocking**.

**Why it is missing here:** your `ProtocolManifest` carries `uncertainty`,
`confidence_target: 0.95`, `exclusion_rules` and `stop_rules` — all statistical
decisions. But **none of them has an owner**. The Scientific Owner writes the
protocol; nobody signs off on statistical validity.

**In AIRL-OS:**
- At G2, produces and locks an **`AnalysisPlanManifest` separate from the
  `ProtocolManifest`**.
- At the G4 baseline, supplies the power analysis and the minimum detectable
  effect size.
- At G6, can **block** on the `statistical_validity` dimension.
- **Owns the exploratory / confirmatory distinction.** Any analysis absent from
  the preregistration is reported under the `exploratory` label and cannot
  produce a `confirmatory` claim.

**A critical addition:** the `AnalysisPlanManifest` must lock **separately** from
the `ProtocolManifest`. The reason: the protocol says "what we will measure"; the
analysis plan says "how we will decide". Merging them leaves open the door to
changing the decision rule after seeing the results.

---

## A2. Research Integrity Officer (RIO) — 🔴 critical

**Real-world counterpart:** under US ORI regulations (42 CFR Part 93), every
institution must have a RIO. They manage FFP (Fabrication, Falsification,
Plagiarism) allegations and have a reporting line **independent** of the research
chain.

**Why it is missing here:** your G6 non-waivable blocker list contains
*"suspicion of fabrication/tampering (raised by a reviewer)"*. But:
- **Who** investigates the suspicion?
- What is the process? Does the suspect work stop, or continue?
- Where is the outcome recorded?
- How does a false accusation get closed?

None of this is defined. In an AI laboratory this risk **increases** rather than
decreases — fabricated citations and fabricated numbers are among the
best-documented LLM failure modes.

**In AIRL-OS:**
- **Authority to stop any gate**, with a reporting line independent of the
  Assurance Lead.
- An `IntegrityCase` object:
  `ALLEGED → TRIAGED → INVESTIGATING → SUBSTANTIATED / UNSUBSTANTIATED → CLOSED`
- The mechanical triggers (B7 below — statistical forensic checks) open an
  `IntegrityCase` **directly**, without waiting for human interpretation.
- If the outcome is `SUBSTANTIATED`: the affected claims become `RETRACTED`, the
  producing model profile is `SUSPENDED`, and all of its historical output is
  swept.

---

## A3. Data Steward

**Real-world counterpart:** the owner of the FAIR principles (Findable,
Accessible, Interoperable, Reusable) and the author of the **DMP** (Data
Management Plan) that funders require. A different profession from the librarian.

**Why it is missing here:** the `Evidence Lead` handles bibliographic management.
But a research laboratory **produces data sets** — and in your architecture the
lifecycle of a produced dataset has no owner. `SourceEntity.source_type` includes
`'dataset'`, but dataset *production* is not modelled.

**In AIRL-OS:**
- At G1, produces the `DataManagementPlan`: which data will be produced, where it
  will be stored, for how long, who may access it and how it will be cited.
- **Croissant** (MLCommons) metadata plus a DOI (Zenodo) for every produced
  dataset.
- Owns the retention and legal-hold policy.
- Applies the D0–D4 classification jointly with the Safety/Data Owner.

---

## A4. Research Software Engineer (RSE)

**Real-world counterpart:** now a distinct profession (Society of RSE, US-RSE).
Owns scientific code quality, sustainability and *packageable reproducibility*.
Not a data engineer, and not a platform engineer.

**Why it is missing here:** the `Engineering Owner` does three jobs at once:
writing code, building infrastructure and running experiments. Real laboratories
separate these because the incentives conflict — the person who wants to run the
experiment does not want to package the code reproducibly.

**In AIRL-OS:**
- Owns the G7 reproduction package: `RO-Crate` + `CITATION.cff` + `CodeMeta`.
- **Assigns the ACM artifact badge level** (see B4).
- Responsible for environment determinism: Nix/Apptainer, digest-pinned images,
  seed control.
- The Engineering Owner **produces**; the RSE **makes it packageable** — separate
  incentives.

---

## A5. Scientific Editor / Claims Discipline

**Real-world counterpart:** a journal editor plus in-house technical writing.
Their job: ensure the text does not say more than the data permits.

**Why this is critical in an AI laboratory:** the most consistent LLM error is
**overgeneralisation**. Even your own example `ReviewVerdict` contains
`claim_scope_assessment: "Overstated in places"` — you have already observed it.

**In AIRL-OS — and this can be enforced mechanically:**

> **Scope Conformance Check:** every assertion in the G9 publication text must map
> to a `ClaimVersion` in the Claim Ledger, and that sentence's scope may not
> exceed `ClaimVersion.scope_qualification`. A sentence that cannot be mapped →
> publication BLOCKED.

This is one of the cheapest and most effective mechanical controls against "false
rigor". Your `DecisionRecord.obligations` field (*"Publication must include scope
restriction"*) already asks for it, but **no mechanism audits it**.

---

## A6. Red Team Lead (a durable function)

**Real-world counterpart:** "Team B" in intelligence analysis and the structured
analytic techniques. Permanent, not attached to a single assignment.

**Why it is missing here:** your `Adversarial Reviewer` is a **task role** —
assigned per project and working within that project's context. A permanent red
team does something different: it finds **the laboratory's systematic blind
spots**, not the flaws of individual projects.

**In AIRL-OS:**
- Portfolio-based rather than project-based: "which error type recurs across the
  last ten projects?"
- Runs the **pre-mortem** (see B8) — before G4.
- Owns control injection (see C4) — and keeps it hidden from the agents.
- Distinct from the *security* attack suite in WP-060; this is the **scientific**
  red team.

---

## A7. Knowledge Steward (institutional memory)

**Real-world counterpart:** in human laboratories this role sits *implicitly* in
senior researchers — "we tried that in 2019, it didn't work."

**Why it must be an explicit role in an AI laboratory:** models have no
institutional memory. Every project starts from zero. After ten projects you walk
into the same dead end for the tenth time.

**In AIRL-OS:**
- **Cross-project claim contradiction detection**: when a new `ClaimVersion` is
  produced, is there an older claim to which a `refutes` relation should be
  established?
- **A negative-result catalogue**: your `ACC-39` scenario tests negative results
  but nothing makes them *searchable*.
- **Method reuse**: similarity across `ProtocolManifest`s; "this protocol has been
  used before, and these were its results."
- Neo4j genuinely earns its place here — a derived view, as you note, but the
  right tool for these queries.

---

## A8. Role catalogue — summary

> **A role is a function, not a person.** The fourteen entries below are durable
> *functions*; they do not require fourteen people. Each is bound through a
> `RoleBinding` carrying `must_be_independent_from`, `can_combine_with` and
> `cannot_combine_with`, so a small operation can hold several roles legally and
> the constraint engine states which combinations destroy independence. This is
> the shape of the answer to **C2**, not the answer itself — which combinations
> are acceptable remains a human decision.

| Role | Status | Type | Can block |
|---|---|---|---|
| Project Decision Owner | existing | **human** | G8, G9 |
| Scientific Owner | existing | human + model-assisted | G2 |
| Evidence Lead | existing | human + model-assisted | G3 |
| Engineering Owner | existing | human + model-assisted | G4, G5 |
| Assurance Lead | existing | human + model-assisted | G6, G7 |
| Safety/Data Owner | existing | human | all (data class) |
| **Statistical Methods Owner** | **added** | human + model | **G2, G4, G6** |
| **Research Integrity Officer** | **added** | **human** | **all** |
| **Data Steward** | **added** | human + model | G1, G9 |
| **Research Software Engineer** | **added** | model + human approval | G7 |
| **Scientific Editor** | **added** | model + mechanical check | **G9** |
| **Red Team Lead** | **added** | human + model | G4 (pre-mortem) |
| **Knowledge Steward** | **added** | model + mechanical | G0 (duplicates) |
| **Metascience Lead** | **added** | human + mechanical | — (measures, does not block) |

---

# PART B — Review mechanisms added

Your existing mechanisms: mechanical, blind, adversarial, citation audit,
security, arbitration, reproduction. A good set. What is missing:

## B1. Stage-1 Registered Report acceptance — 🔴 the highest-impact addition

**Real world:** in the Registered Reports format, the protocol is peer-reviewed
**before data collection**, and if accepted (*in-principle acceptance*)
publication is guaranteed **independently of the result**. It is the only
mechanism that kills publication bias at the root.

**Why it is missing here:** you freeze the protocol at G2 ✅, but the G8 decision
is taken **while looking at the results**. That is:

```
G2: the protocol is frozen
G5: the result arrives — negative
G8: the Decision Owner can say "REJECT"
→ the negative result is not published → publication bias survives
```

Your `ACC-39 — Negative Research Result` scenario *tests* this risk, but nothing
in the architecture *prevents* it.

**In AIRL-OS:**

> **`InPrincipleAcceptance` is produced at G2.** If the protocol plus the analysis
> plan were accepted independently, the G8 decision may only turn on one axis:
> *"was the protocol followed?"* — never *"do I like the result?"*
>
> The only grounds on which G8 may `REJECT` are a protocol violation, an integrity
> problem, or a G7 reproduction failure. **The direction of the result is never a
> reason.**

This single change raises your laboratory's scientific credibility more than all
the other mechanisms combined.

---

## B2. Blinded analysis

**Real world:** standard in particle physics. The analyst cannot see the real
result until the analysis is locked — the data is "salted", labels are shuffled,
or the signal region is masked. LIGO used blind injections.

**Why it is missing here:** your "blind review" blinds the **reviewer** (who does
not see the producer's trace). But **the analyst** performs the analysis while
seeing the result. That is where the real degrees of freedom sit.

**In AIRL-OS:**
- G5 output is given to the analysis agent with **condition labels masked**.
- The analysis pipeline is locked against the `AnalysisPlanManifest`.
- Unblinding follows the lock; any change made after the lock is `exploratory`.
- Applicability: not possible for every experiment type — **mandatory at R2/R3**,
  optional at R1.

---

## B3. Multi-analyst + multiverse analysis — 🔴 ideal for an AI laboratory

**Real world:** Silberzahn et al. (2018) gave the same dataset to 29 independent
teams; the effect sizes spread widely and some pointed in opposite directions.
Same data, same question, different defensible analysis paths → different
results. These are **analytical degrees of freedom**.

**Why this fits your system exactly:** human laboratories cannot do this — 29
teams is expensive. **Your laboratory can.** Running N independent analysis agents
is cheap.

**In AIRL-OS:**

```
G5 result → N independent analysis agents (different model families,
            the same AnalysisPlan)
          → the distribution of results
          → is the distribution narrow? the claim is robust.
          → is the distribution wide? the claim's confidence DROPS and
            scope_qualification becomes mandatory.
```

And **specification curve / multiverse**: instead of a single analysis path, run
all the defensible ones (exclusion rules, transformations, covariates) and report
the **distribution** of the result. A direct defence against p-hacking.

**This gives your `reproducibility` confidence dimension a real measurement basis.**

---

### B3.1 The universe must be frozen before the results exist

Multiverse analysis without a pre-committed universe is a p-hacking engine with
better vocabulary: run a thousand defensible analyses, report the pleasing one,
and every individual step remains defensible.

```yaml
AnalysisUniverseManifest:
  hash: "sha256:..."            # locked at G2b, before any result exists
  dimensions:
    - {name: outlier_rule,    options: [none, 3sd, iqr]}
    - {name: covariate_set,   options: [minimal, full]}
    - {name: estimator,       options: [ols, robust]}
  enumeration: exhaustive        # or an explicitly declared, seeded sample
  reporting: "the FULL distribution, not a selected member"
  primary_specification: <one member, named in advance>
```

Two rules make it work: **the universe is enumerated before results exist**, and
**the whole distribution is reported** — the primary specification is named in
advance and reported alongside the spread, never chosen from it afterwards.

## B4. ACM artifact badge levels — a terminology correction

**The problem:** your document mentions the triple `repeatability,
reproducibility, replication` in the introduction and defines none of them. And
the G7 methodology says *"a different solver (Gurobi vs CPLEX), a different
seed"* while expecting a `±2%` match — that is **replication**, not reproduction.

**A ready, established solution — the ACM/NISO badge vocabulary:**

| Level | Meaning | AIRL-OS gate |
|---|---|---|
| **Artifacts Available** | The artifact is in a permanent archive with a DOI | G9 |
| **Artifacts Evaluated — Functional** | Documented, consistent, complete, it runs | end of G5 |
| **Artifacts Evaluated — Reusable** | The above plus reusable quality | G7 (RSE) |
| **Results Reproduced** | **A different team obtained the result with the same artifact** | **G7** |
| **Results Replicated** | **A different team obtained the result with a different artifact** | **G7+ / independent** |

And the NASEM definitions: *reproducibility* = same data + same code → same result
(**deterministic**, tolerance ≈ 0); *replicability* = new data or a new
implementation → a consistent result (**statistical**, tolerance judged by
distribution comparison).

**Conclusion:** your G7 should really be **two separate gates**:

- **G7a — Reproduction:** same manifest, same seed, same image digest → **bit-level
  or `< 0.1%`**. No tolerance. No model judgement. It either holds or it does not.
- **G7b — Replication:** different seed, different implementation, different
  environment → **a distribution comparison** (CI overlap / equivalence testing),
  not a single `%`.

The current three-way contradiction (`±2% / >=95% / >5%`) resolves itself under
this split.

---

## B5. Delphi consensus (instead of a single arbiter)

**Real world:** RAND's Delphi method. Multi-round, **anonymous**, with controlled
feedback. Designed to prevent anchoring and to stop a dominant opinion dragging
the others along.

**Why it is missing here:** `DisagreementCase` → a single `arbiter`. A single
arbiter is a single point of failure, and if it is a model it brings its own
biases.

**In AIRL-OS:**
```
Round 1: N reviewers give an independent verdict plus rationale
         (they do not see each other)
Round 2: an anonymised rationale summary is circulated; everyone may revise
         their verdict — A REVISION REQUIRES A RATIONALE
Round 3: if there is still no consensus → a human arbiter, who sees ALL rounds
```
Convergence is measured: the verdict-change rate between rounds. Very fast
convergence = suspicion of herding, and is itself a separate signal.

---

## B6. Analysis of Competing Hypotheses (ACH)

**Real world:** Richards Heuer, CIA. A structured analytic technique. It inverts
the logic: not *"which hypothesis does this support?"* but
**"which hypotheses does it ELIMINATE?"**

The mechanics:
1. List all plausible hypotheses (not just the favourite one)
2. List all the evidence
3. Build the evidence × hypothesis matrix: consistent / inconsistent / irrelevant
4. **Diagnosticity**: a piece of evidence consistent with *every* hypothesis is
   **worthless** — it discriminates nothing
5. Eliminate the hypotheses with the most *inconsistencies*; rank the rest

**Why it fits your Claim Ledger perfectly:** `EvidenceSpan.support_type` is
already `supports | contradicts | qualifies | contextualizes` — that is the cell
of an ACH matrix. The only missing piece is a **diagnosticity score**: does this
evidence discriminate between the competing hypotheses?

**This is the only mechanism that measures the difference between "we collected a
lot of evidence" and "we collected discriminating evidence."** And it is the exact
antidote to `PR-12 False Rigor`.

---

## B7. Mechanical statistical forensic checks — 🔴 cheap, automatic, high-yield

These require **no model judgement**. They are deterministic, fast and automatic.
They run in the E1 layer (mechanical), **before** expensive model review.

| Check | What it does | Where |
|---|---|---|
| **statcheck** | Checks the internal consistency of a reported test statistic and its p-value | G6 mechanical |
| **GRIM** | Checks whether a reported mean is **possible** given N and measurement granularity | G6 mechanical |
| **GRIMMER** | The same for standard deviations | G6 mechanical |
| **SPRITE** | Reconstructs the possible data distributions from a given mean + SD + N | Integrity Case |
| **Benford analysis** | Digit-distribution anomalies | Integrity Case |
| **Citation entailment** | Checks that each citation's source span genuinely supports it | G6 (WP-080) |
| **Scope conformance** | Publication text ↔ ClaimVersion scope mapping (A5) | G9 |
| **Hash/manifest** | Artifact integrity | all gates |

**The critical principle:** all of these can open an `IntegrityCase` or produce a
`GATE_BLOCKED` without any model decision. **A number an LLM invented cannot pass
GRIM.**

---

### B7.1 Applicability is part of the check

statcheck, GRIM, GRIMMER, SPRITE and Benford are **conditionally valid
instruments**, not universal verifiers. GRIM is meaningful only for a mean
reported from a known-size sample on a discrete scale; Benford's law is a false
positive factory when applied to data that has no reason to follow it. A check
run outside its applicability conditions does not produce a weak signal — it
produces a wrong one.

```yaml
ForensicCheckRegistry:
  - check: GRIM
    applicability:
      discrete_scale: true
      mean_reported: true
      sample_size_known: true
    verdict: PASS | FAIL | NOT_APPLICABLE      # NOT_APPLICABLE is a first-class result
```

**And a failing check opens a flag, not an accusation:**

```
ForensicFlag  →  triage  →  IntegrityCase
```

An anomaly is not fabrication. Wiring `GRIM failed` directly to an integrity
case means the laboratory manufactures accusations at the rate of its own false
positive rate — and for a system whose central claim is that it distinguishes
signal from plausibility, that failure would be self-refuting.

## B8. Pre-mortem (before G4)

**Real world:** Gary Klein. Before the project starts: *"A year has passed and the
project failed completely. Why?"* Prospective hindsight breaks defensiveness by
moving from the future tense into the past tense.

**In AIRL-OS:** before the G4 (Baseline & Budget) approval, the Red Team runs a
pre-mortem over the `ProtocolManifest` and the `AnalysisPlanManifest`. Its output
**adds new items to the `falsification_plan`**. It costs an hour and returns a
great deal.

---

## B9. Severity assessment

**Real world:** Deborah Mayo's error statistics. A test is **severe** if and only
if: were the claim false, this test would **very probably** have caught it.

**Why it is missing here:** your `falsification_plan` says *"if consensus < 90%:
the method fails"*. But it never asks: **"if the method really had failed, would
this test have caught it?"** — that is, the test's **power**.

Passing a weak test is not evidence. This is the difference between "we ran many
tests" and "we ran demanding tests".

**In AIRL-OS:** a `severity_assessment` for every `ClaimVersion`:
`{test_id, would_detect_if_false: probability, basis}` — signed by the Statistical
Methods Owner.

---

## B10. Adversarial collaboration (for genuine disagreements)

**Real world:** Kahneman's proposal. Two disagreeing parties **jointly design** the
experiment that will settle the disagreement and agree **in advance** what each
outcome will mean.

**In AIRL-OS:** if a `DisagreementCase` does not close through arbitration, then
instead of an automatic arbiter ruling: the two sides jointly produce a new
`ProtocolManifest`, write the decision rule in advance, and run the experiment.
Not cheap, but conclusive. It should be the default path for the
`arbitration_failed` state at R3.

---

## B11. Review mechanisms — summary

| Mechanism | Status | Gate | Model or mechanical? |
|---|---|---|---|
| Mechanical verification (hash, manifest) | existing | all | **mechanical** |
| Blind review | existing | G6 | model |
| Adversarial review | existing | G6 | model |
| Citation/entailment audit | existing | G6 | mechanical + model |
| Security review | existing | G6 | mechanical + model |
| Arbitration | existing | G6 | human |
| Reproduction | existing | G7 | **mechanical** |
| **Stage-1 in-principle acceptance** | **added** | **G2** | model + human |
| **Blinded analysis** | **added** | **G5→G6** | mechanical |
| **Multi-analyst / multiverse** | **added** | **G6** | model (N of them) |
| **ACM badge levelling** | **added** | **G7a/G7b** | mechanical |
| **Delphi consensus** | **added** | **G6** | model (N rounds) |
| **ACH + diagnosticity** | **added** | **G6** | model + mechanical matrix |
| **statcheck/GRIM/GRIMMER/SPRITE** | **added** | **G6 mechanical** | **mechanical** |
| **Pre-mortem** | **added** | **G4** | model + human |
| **Severity assessment** | **added** | **G2, G6** | human-signed |
| **Adversarial collaboration** | **added** | **G6 escalation** | human + model |
| **Scope conformance** | **added** | **G9** | **mechanical** |

---

# PART C — The 7th plane: Metascience & Calibration

## C0. Why a new plane is needed

Your six existing planes manage **the research**. None of them asks:

> **"Is this laboratory producing correct results? How do we know?"**

In a human laboratory that question is answered indirectly: reputation, citations,
replications, time. In a laboratory **operated by models** those routes do not
exist — and because they do not exist, the question has to be measured.

And one empirical fact makes it unavoidable:

> **Using a different model family is not a guarantee of independence.**
> Frontier models are trained on heavily overlapping corpora. They can make the
> same mistake with the same confidence. Two reviewers agreeing carries no
> evidential value until the error correlation between them has been measured.

Your `IndependenceMatrix` marks Model Lineage as **not non-compensable** — that is
the right instinct. But it follows that the only remaining genuinely independent
axis is **mechanical verification**, and that has to be measured.

---

## C1. Agreement calibration — measuring independence

**The mechanism:**

```
A permanent "agreement calibration set" is maintained:
  - N review tasks whose correct answer is known
  - Every qualified model profile processes the set periodically
  - Measured:
      * accuracy
      * pairwise error correlation
      * beyond-chance agreement (Fleiss' κ / Krippendorff's α)
```

**And the decision rule:**

> If the **error correlation** `ρ` between two model profiles exceeds the
> threshold, the two cannot both count toward the independence quota for the same
> claim. The `Model Lineage` dimension of the Independence Matrix becomes
> **a measurement rather than a declaration**.

This is the only mechanism that converts WP-007 from paper independence into real
independence. And measuring it is cheap.

**A second signal:** agreement that is *too* high is also an alarm — κ ≈ 1.0 is not
expected among independent judges. Either the task is trivial, or the judges are
not independent.

---

## C2. Confidence calibration — rescuing the seven scales

**The problem:** `ClaimVersion` carries seven confidence dimensions
(`identity_confidence`, `entailment`, `method_validity`, `independence`,
`reproducibility`, `scope_fit`, `currency`) — all `0.0–1.0`, at two or three
decimal places.

**Today those numbers mean nothing**, because:
- Their producers (LLMs) are not calibrated
- No combination rule is defined
- They are never compared against outcomes

Until it is measured, the difference between `0.95` and `0.87` is **decoration.**
And that is precisely the definition of your own `PR-12 — False Rigor` risk.

**The fix — three steps:**

1. **Measure.** Every predicted confidence eventually meets an outcome (was the
   claim verified at G7? did it survive G10?). Compute the **Brier score** and the
   calibration curve.
2. **Recalibrate.** Convert raw model scores into calibrated probabilities via
   isotonic regression or Platt scaling. `ClaimVersion` stores **both**:
   `raw_confidence` and `calibrated_confidence`.
3. **If it is not calibrated, do not display it.** Where there is insufficient
   outcome data for a dimension, display `UNCALIBRATED` instead of a number.
   **False precision is forbidden.**

**And the combination rule:** do not multiply, do not average. These dimensions
are not independent and they measure different things.

**Revised, 2026-08-22 — the vector is canonical; the scalar is not published.**
The weakest-link idea survives, because it is the anti-false-rigor choice: a
claim is only as strong as its weakest evidential dimension. What does not
survive is emitting that as a *number*, because `0.72` invites reading as a
probability that nothing in the system computes.

```yaml
claim_assurance:                 # canonical, always the vector
  identity:        calibrated
  entailment:      calibrated
  method_validity: qualified
  independence:    weak
  reproducibility: strong
  scope_fit:       strong
  currency:        current
binding_constraint: independence   # the weakest dimension, named
```

`binding_constraint` preserves the ordering that `min()` gave — two claims can
still be compared by their weakest dimension — without asserting a magnitude the
dimensions cannot support. **`claim_strength` is not a published field.** Where a
dimension lacks outcome data it reads `UNCALIBRATED`, and a claim whose binding
constraint is `weak` says so in words rather than hiding inside an average.

---

## C3. Gate yield — which gate is actually working?

**The measurement:** for each gate — how many items entered, how many were blocked
or sent back, and did those findings later turn out to be **real**?

```
gate_yield(G6-adversarial) = confirmed findings / total findings
false_positive_rate(G6-adversarial) = rejected findings / total findings
cost(G6-adversarial) = tokens + wall-clock + human minutes
```

**Why this is critical:** assurance has a cost and infinite depth is not possible.
If you do not know which gate actually catches errors, assurance decays into
**ritual** — many artifacts, little protection. That is the common root of `PR-04`
(verification backlog) and `PR-12`.

A gate with low yield is either removed or redesigned. A gate with high yield is
deepened.

---

## C4. Control injection — the laboratory's own error rate — 🔴

**Real world:** standard in genomics and epidemiology — positive controls (whose
answer is known) and negative controls (where no effect should exist, e.g.
permuted data). If a pipeline "finds an effect" in shuffled data, the pipeline is
broken.

**In AIRL-OS:**

> A small proportion of projects (**say 5–10%**) are opened *seeded*:
> - **Positive control:** a question whose answer is known in advance
> - **Negative control:** null or permuted data — there is no effect to find
>
> These must be **indistinguishable** from real projects and **hidden from the
> agents** (the Red Team Lead and the Metascience Lead know).
>
> Measured: the laboratory's **false positive rate** and **false negative rate**.

**This is the laboratory's only real measure of correctness.** Everything else is a
process metric; this is an outcome metric.

It is also the concrete solution to the gap noted earlier — "the laboratory has no
evaluation harness of its own". MLE-bench and PaperBench measure from the outside;
control injection measures **on the live line, under real conditions**.

---

## C5. Human attention budget and rubber-stamping detection

**The problem:** `PR-11 — Human rubber-stamping` is in your own risk register. But
the architecture contains no mechanism against it — only an SLA, and SLA pressure
**increases** rubber-stamping.

In a model-operated laboratory this risk is structural: models produce far faster
than humans; the human becomes the bottleneck; a bottlenecked human starts
approving.

**The mechanism:**

> **Architecture states that a quota exists; policy holds the number.** The
> figure below is an initial `HumanAttentionPolicy` value, not an architectural
> constant — it is expected to change with evidence, and a number frozen into an
> architecture document is a number nobody dares revise. The invariant is *there
> is a hard quota and it is enforced*; `5` is this policy version's value.

```yaml
HumanAttentionPolicy:
  policy_version: "attention@1.0.0"
  max_g8_decisions_per_week: 5          # A HARD QUOTA, not an SLA
  min_evidence_view_seconds: <computed from the packet>
  mandatory_disagreement_exposure: true  # open disagreement cannot be hidden

  measured:
    decision_time_distribution      # very short = alarm
    evidence_sections_actually_opened
    reversal_rate_at_G10            # accepted at G8, reversed at G10
    dissent_override_rate           # ACCEPT despite an adversarial REJECT
```

**What happens when the quota is exhausted:** the queue **waits**. No auto-approve,
no SLA extension, no "quick review" mode. The laboratory's throughput is bounded by
human decision capacity — and that is not a defect, it is **the design**.

---

## C6. Claim survival — the laboratory's final score

**The measurement:** the status of claims accepted at G8 after 6, 12 and 24 months.

```
survival_rate = RECONFIRMED / (RECONFIRMED + REVISED + SUPERSEDED + RETRACTED)
```

Your G10 `ImpactCase` infrastructure **already produces** this data. The only thing
needed is to track it as a time series.

And this is the true KPI of the whole system. Every other metric is intermediate.
If the survival rate falls, C3 tells you which gate's yield fell with it.

---

## C7. The Metascience Plane — summary

| Measurement | Question it answers | Input | Frequency |
|---|---|---|---|
| **Agreement calibration** (κ, ρ) | Are my reviewers genuinely independent? | the calibration set | monthly |
| **Confidence calibration** (Brier) | Do the confidence numbers mean anything? | claim outcomes | quarterly |
| **Gate yield** | Which gate actually catches errors? | finding → confirmation | quarterly |
| **Control injection** | What are the lab's FP/FN rates? | seeded projects | continuous |
| **Attention budget** | Is the human genuinely deciding? | decision telemetry | weekly |
| **Claim survival** | Does the knowledge we produce hold up? | G10 ImpactCase | continuous |

**The critical rule:** the metascience plane **blocks no gate.** It measures and
reports. If it were given blocking authority, pressure to optimise the measured
quantity would appear (Goodhart's law) and the measurement would be destroyed. The
single exception: **finding an effect in a negative control** during control
injection — that is a broken pipeline, and it stops the line.

---

# PART D — Role → model assignment architecture

> **Decided separately:** the concrete model pool, the gate→actor table, the
> effort→R class mapping and the snapshot-pinning constraint live in
> `AIRL_OS_ROLE_MODEL_ASSIGNMENT.md`.

## D1. The assignment principle: verification asymmetry

For every gate there is one question:

> **Is a mechanical verification possible at this step?**
> - **Yes** → the mechanical check runs first, and **the model cannot override it**
> - **No** → the model produces, but its output must be *falsifiable*

**A model is a hypothesis generator, not a verifier.** If a model's output cannot
be reduced to a form that a machine can check, that output is a suggestion, not
evidence.

## D2. Gate → actor matrix

| Gate | Mechanical (deterministic) | Model | Human |
|---|---|---|---|
| **G0 Intake** | duplicate search (Neo4j + embeddings) | triage, similarity summary | greenlight (5 min) |
| **G1 Charter** | `RiskProfile → AssuranceClass` (**a policy engine, not a model**) | charter draft, risk vector proposal | **writes the decision question**, approves |
| **G2 Protocol** | template completeness check | protocol draft, pre-mortem, Stage-1 review (different family) | Scientific Owner + Statistical Methods Owner **sign** |
| **G2b Analysis Plan** | — | analysis plan draft, power analysis | **the Statistical Methods Owner locks it** |
| **G3 Literature** | GROBID extraction, DOI resolution, dedup, hashing | discovery, query planning, screening (active learning) | Evidence Lead **freezes** |
| **G4 Baseline** | the baseline run (deterministic) | compute plan, red-team pre-mortem | budget approval (FinOps + Eng) |
| **G5 Execute** | **the experiment run itself** | — *(not in the loop unless the model is the subject)* | — |
| **G6-0 Mechanical** | statcheck, GRIM/GRIMMER, entailment, hashes, manifests | — | — |
| **G6-1 Blind** | `ReviewPacketBuilder` (**a program**, not a prompt) | N reviewers from **measured-independent** families | — |
| **G6-2 Adversarial** | — | adversarial review + the ACH diagnosticity matrix | — |
| **G6-3 Disagreement** | verdict comparison | Delphi rounds | arbiter (**only if it fails to converge**) |
| **G7a Reproduction** | **same manifest, same seed → deterministic** | — | — |
| **G7b Replication** | different seed/implementation → **distribution test** | — | the RSE assigns the badge |
| **G8 Decision** | evidence package completeness | **may produce a recommendation, never a decision** | **HUMAN ONLY** (under quota) |
| **G9 Publish** | **scope conformance** (mechanical), RO-Crate, hashes | text draft | Decision Owner + Editor |
| **G10 Monitor** | feeds (Crossref / Retraction Watch / CVE) | signal triage, materiality proposal | decides on a material signal |

**Three rules:**
1. If there is no model at G5 (unless the model is the subject of the experiment),
   the result is **free of model bias**. That is the laboratory's cleanest layer —
   protect it.
2. There is **no model at all** at G7a. It either holds or it does not.
3. At G8 the model produces **only a recommendation**. This is already
   non-waivable in your design ✅.

## D3. Model pool and quota architecture

```yaml
ModelPool:
  producer_tier:      # production: balanced speed and cost
  reviewer_tier:      # review: MEASURED independent of the producer (C1)
  adversarial_tier:   # most capable; rewarded on refutation rate
  arbiter_tier:       # only on disagreement; sees both sides
  local_tier:         # open-weight, LOCAL — MANDATORY for R3 and G7

Rules:
  - the producer and the final reviewer of a claim MUST NOT be the same profile
  - two profiles whose error correlation ρ exceeds the threshold cannot both
    count toward the independence quota for the same claim   # output of C1
  - the adversarial reviewer's metric is the QUALITY OF ITS REFUTATION,
    not its approval speed
  - a run producing an R3 claim uses a LOCAL / open-weight model   # see D4
```

## D4. Model snapshot retention — a structural requirement for G7

> **The problem:** `ExperimentRun.model_snapshot: "Claude Sonnet 5 20260801"` and
> reproducibility is **non-waivable**. But hosted providers do not retain snapshots
> indefinitely. If you run G7a six months later and that snapshot is gone, the
> guarantee of "reproduce from the frozen manifest" collapses.

> **Implementation note.** The R3 requirement now has off-the-shelf tooling:
> `sigstore/model-transparency` and the OpenSSF Model Signing spec hash and sign
> the local weights, and the frozen manifest points at that signature.

**The unavoidable conclusion:**

| Assurance class | Model policy | Rationale |
|---|---|---|
| R1 | hosted OK | Reproduction tolerance at low criticality |
| R2 | hosted OK + **full I/O logging** (Langfuse) | When the snapshot disappears, at least the input/output evidence remains |
| **R3** | **local / open-weight MANDATORY** (GGUF + SHA-256) | The weights are yours; G7a is genuinely possible |

Your 2× RTX A5000 plus a local GGUF stack is therefore **not an optional
preference but a precondition for R3.** The `system_fingerprint` freezing practice
you already apply on the SILBO side is exactly the right reflex — lift it to
framework level.

---

# PART E — Operational mechanics to take from `obra/superpowers`

Superpowers is a *coding* methodology, but the problem it solves is the same as
yours: **how do you trust the work an agent produced?** And it has
operationalised things that exist **conceptually but not operationally** in your
architecture.

## E1. Defining information asymmetry at the file level

In Superpowers, exactly which files the implementer and the reviewer see is
defined:

| | Implementer sees | Reviewer sees |
|---|---|---|
| Task brief | ✅ | ✅ |
| The *interfaces* of previous tasks | ✅ | ✅ (global constraints) |
| The implementer's report | writes it | ✅ |
| The code diff | produces it | ✅ |
| **The implementer's internal reasoning** | — | ❌ **never** |
| Session history | ❌ | ❌ |

Your `ReviewPacket.excluded_from_packet` list already agrees ✅. But Superpowers
goes one step further: **"No context pasting — hand artifacts as files, not inline
text."**

**To take:** `ReviewPacketBuilder` must be a **program**, not a prompt. The
allowlist lives in code, in the ACL and in a test. No inline text is passed to the
reviewer; only a file path and a hash. That makes the question "what did the
reviewer see?" **auditable** — which is exactly what your `evidence_packet_hash`
field is asking for.

## E2. "The implementer never dispatches subagents" — 🔴 a critical rule

> *"the implementer never dispatches subagents — not helpers, and never a reviewer."*

**Your architecture does not contain this rule.** The `Assurance Lead` assigns
reviewers ✅, but nowhere is the **producer forbidden from summoning its own
helpers**. Without that prohibition:

```
Producer agent → calls a "helper" agent → the helper does part of the work
→ the helper is effectively a co-author → but does not appear in the
   independence ledger
→ the IndependenceMatrix issues a false PASS
```

**To take — an 8th dimension for the Independence Matrix:**

```yaml
- dimension: "Delegation Boundary"
  description: "Was the producer able to summon its own verifier or helper?"
  controls:
    - "Producer cannot spawn sub-agents"
    - "Reviewer assignment only by Assurance Lead / Task Compiler"
    - "All agent invocations recorded in the correlation chain"
  R1_requirement: "PASS"
  R2_requirement: "PASS"
  R3_requirement: "PASS (hard block)"
  non_compensable_for: [R1, R2, R3]
```

This dimension must be **non-compensable in every class** — because if it is
violated, the measurement of the other six dimensions becomes void as well.

## E3. A bounded escalation ladder plus "the breaker"

Superpowers' disagreement resolution:

```
Rounds 1–3: the same implementer, context preserved, findings relayed VERBATIM
Rounds 4–5: a FRESH implementer on a MORE CAPABLE model,
            framed explicitly: "a previous one tried N times; it is yours now"
Still open at the end of round 5 → THE BREAKER:
            dispatch STOPS, a human adjudicates every open finding one by one,
            every ruling is written into the ledger — SILENT DISCARD FORBIDDEN
```

**What is missing from your `DisagreementCase`:** there is no bound. How many
rounds? When does it reach a human? Does the model change? And most importantly:
**there is no guarantee that open findings do not vanish silently.**

**To take:** add `round`, `escalation_tier`, `max_rounds` and a **`FindingLedger`**
to `DisagreementCase`. Every open finding is either resolved or marked `PARKED`
with a rationale, an owner and an expiry. Your finding lifecycle in the evidence
and acceptance strategy is correct, but it is **not bound to a round-based
escalation.**

## E4. Classify first, and "when in doubt, choose the heavier path"

> *"when in doubt between two paths, take the heavier one"*

**Your `determine_assurance_class` function does the opposite:**

```python
    # ...
    return R1     # ← the fall-through default is the LIGHTEST
```

That is **fail-open**. A missing or ambiguous `RiskProfile` field drops the project
into the lowest assurance class.

**To take:**
```python
if not risk_profile.is_complete():
    return R3            # missing information = the heaviest path
# ...
return R2                # the fall-through default is R2, not R1
```

## E5. Path escalation (mid-project risk reclassification)

> *"Hidden complexity discovered mid-task requires path escalation — stop,
> announce the upgrade, restart at the heavier level."*

**Your architecture does not have this.** What happens when a project that started
as R1 discovers at G5 that it is touching D3 data? The document is silent.

**To take:** a `RiskReclassificationEvent`. On an escalation:
- The workflow **pauses**
- The gate depth of the new class is applied
- **Gates already passed at the lighter class are re-evaluated**
- A downgrade (R3 → R2) requires a joint decision by the Safety/Data Owner and the
  Assurance Lead

## E6. A mandatory self-review before reaching human approval

> *"Specs must pass a self-review (checking for placeholders, contradictions,
> scope drift) before user review."*

A cheap mechanical gate before an expensive human one. Your E0–E5 evidence-layer
model is already in this spirit ✅ but it is **not applied to the packet that
reaches G8**.

**To take:** an automatic check before a `DecisionRequest` enters the human queue —
are there placeholders, contradictory verdicts, scope drift, missing mandatory
fields? If it does not pass, no human time is spent.

## E7. Ledger-driven recovery

In Superpowers, when context runs out, `progress.md` supplies the completed work
and Git supplies the commits. **Deterministic recovery.**

Your `implementation_log.md` agrees in spirit, but it is **not machine-readable** —
it is free text. An agent cannot parse it reliably.

**To take:** alongside the human-readable log, a `progress.jsonl` (append-only):
`{step_id, wp_ids, status, target_sha, evidence_manifest, timestamp}`.

## E8. Decisions of yours that Superpowers independently confirms

These confirm you were right — two independent designs reached the same
conclusion:

| Superpowers | AIRL-OS | The shared insight |
|---|---|---|
| "Approval ceremony scales, the gate never disappears" | "Sessions may merge; gate records must stay separate" (Decision #4) | The ritual flexes; the record does not |
| Final whole-branch review with the most capable model | *(absent in yours)* | Reviewing the parts ≠ reviewing the whole |
| A fresh subagent per task, no session history | Context Isolation (non-compensable at R2/R3) | Context contamination kills independence |
| TDD: code written before the test is **deleted** | *(absent in yours)* | If the order reverses, the evidence is void |

**The last row matters most.** The research counterpart of TDD:

> **Results computed before the preregistration (the G2b analysis plan) cannot be
> used as `confirmatory` evidence.** They are reported only as `exploratory`.

And `E8-2`: at G9, a single final review **over the whole publication package**
with the most capable model — separate from the piecewise claim review. A whole
whose parts each passed can still be inconsistent as a whole.

---

# PART F — Tool stack

Organised by function. **Bold** entries are absent from the current design and
close a gap directly.

## F1. Literature and evidence

| Tool | Job | Why |
|---|---|---|
| **GROBID** | PDF → structured TEI XML | **Far better** section, reference and coordinate extraction than pdfplumber — it raises your span-anchoring quality directly |
| **OpenAlex** | Citation network, coverage | Broader than Crossref, free, fully open |
| Crossref + Retraction Watch | Retraction feed | G10 — already in your plan |
| **Semantic Scholar / S2ORC** | Full text, citation context | Citation-intent classification |
| **Unpaywall** | Open-access full text | Lawful PDF access (`PR-14` licence risk) |
| **ASReview** | Active-learning screening | **An exact match for WP-071 screening/inclusion — ready and open source** |
| **anystyle** | Reference parsing | Bibliography normalisation |
| **Nougat / PDFFigures2** | Figure and table extraction | Binding data inside a figure to evidence |
| PaperQA2 | Citation-verified QA | A reference implementation for entailment auditing |

## F2. Evidence standards and provenance

| Tool / standard | Job | Why |
|---|---|---|
| W3C Web Annotation | Span anchoring | Already in use ✅ |
| **W3C PROV-O** | Lineage model | Align to the standard instead of a bespoke lineage schema — the tool ecosystem is ready |
| **Nanopublications** | Atomic, citable claim + provenance | **Your `ClaimVersion` is almost exactly a nanopub** — aligning gives you export and interoperability for free |
| **CiTO (SPAR)** | Citation typing ontology | The standard counterpart of your `support_type` enum: `cito:supports`, `cito:disputes`, `cito:extends` |
| RO-Crate | Publication package | Already in WP-090 ✅ |
| **Croissant (MLCommons)** | ML dataset metadata | For the Data Steward (A3) |
| CITATION.cff + CodeMeta | Software citation | For the RSE (A4) |
| Zenodo / Software Heritage | Permanent archive + DOI | The "Artifacts Available" badge |

## F3. Statistical discipline and forensic checking

| Tool | Job | Layer |
|---|---|---|
| **statcheck** | Internal consistency of reported statistics | **G6 mechanical** |
| **GRIM / GRIMMER / SPRITE** | Whether a mean or SD is possible given N | **G6 mechanical** |
| **specr / multiverse / boba** | Specification curve, multiverse analysis | **G6 (B3)** |
| **DABEST** | Effect size + CI (instead of p-values) | G6 reporting |
| PyMC / Stan | Bayesian uncertainty | Statistical Methods Owner |
| **p-curve / z-curve** | The evidential value of a set of findings | Metascience (C3) |
| scikit-learn `calibration` | Isotonic / Platt calibration | **Metascience (C2)** |
| statsmodels / pingouin | General statistics | G6 |

## F4. Reproducibility

| Tool | Job |
|---|---|
| **Nix or Apptainer** | Real bit-level environment determinism — a Docker digest is not enough |
| DVC / lakeFS | Data versioning |
| MLflow | Run registry — already in your plan ✅ |
| **marimo** | Reactive, Git-friendly, deterministic notebooks — solves Jupyter's non-reproducibility problem |
| sigstore/cosign + in-toto | Artifact signing — already in your plan ✅ |
| **Quarto** | Literate publishing, cross-references, multi-format — **ideal for the G9 PublicationPackage** |

## F5. Visualisation (an area you specifically asked about)

| Tool | For what | Why this one |
|---|---|---|
| **Vega-Lite** | All statistical charts | **A chart = a spec + a data hash.** The spec is JSON: versionable, diffable, reproducible. It fits your manifest philosophy exactly |
| **Observable Framework** | Static, data-driven dashboards | Build-time data, no runtime dependency; can be frozen as an artifact |
| **Cytoscape.js / Sigma.js** | The claim–evidence–source graph | This will be your primary knowledge visualisation |
| **Great Tables** | Publication-quality tables | G9 |
| **Mermaid** | Architecture and flow diagrams | Text-based, Git-friendly, natively supported by Obsidian |
| **Kroki** | Multi-format diagram rendering service | One service, many diagram languages |
| **Label Studio** | Evidence span verification interface | **Where a human confirms a span — this interface does not exist in the architecture today** |
| **Argilla** | LLM output review/annotation | Human control over reviewer verdicts |
| Perfetto / Jaeger | Trace visualisation | The OTel correlation chain |
| Grafana | Operational dashboards | Already in your plan ✅ |

**A proposed architectural rule for visualisation:**

> Every figure is an **artifact**: `{spec_hash, data_hash, renderer_version}`.
> No figure may appear in a publication without those three in the manifest.
> That makes "does the curve in this figure come from the data?" a mechanically
> answerable question. Your `figure_1_digest` field already exists — extend it with
> the spec/data separation.

## F6. Model and agent infrastructure

| Tool | Job |
|---|---|
| LiteLLM | Model gateway — already in your plan ✅ |
| **vLLM / llama.cpp** | Local open-weight serving — **mandatory for R3 (D4)** |
| **Instructor / Outlines** | Structured output enforcement — stop parsing free text |
| **Inspect (UK AISI)** | Rigorous model evaluation framework — **for Capability Registry qualification** |
| **DSPy** | Metric-driven prompt optimisation — improve prompts by measurement, not by hand |
| promptfoo / DeepEval | Evaluation pipeline | The golden set (WP-043) |
| Langfuse | LLM tracing — already in your plan ✅ |
| **Ragas** | Retrieval quality | G3 coverage analysis |

## F7. Security

| Tool | Job |
|---|---|
| gVisor | Sandbox — already in your plan ✅ |
| **Kata Containers / Firecracker** | Real VM isolation for the critical profile (your document already says "a VM, not a container") |
| **Falco** | Runtime behaviour monitoring — sandbox escape detection (ACC-15) |
| **Presidio** | PII detection | DLP (ACC-32 secret-in-trace) |
| Trivy / Grype | SBOM + vulnerabilities | WP-059 |
| **Kyverno** | Kubernetes admission policy | An alternative or complement to OPA |
| Vault + SPIFFE/SPIRE | Identity — already in your plan ✅ |
| **mitmproxy / Squid+ICAP** | Egress inspection | WP-057 |

## F8. Communication and notification

These require **a new component** in the architecture: the **Notification
Broker** — a subclass of the Tool Broker. The agent produces a notification
*intent*; the broker sends it.

| Tool | Role | Data-class ceiling |
|---|---|---|
| **Apprise** | Transport abstraction — 143 services, one URL format | — (policy sits above it) |
| **ntfy (self-hosted)** | Push notification, no account required | **D2** |
| **Matrix (self-hosted)** | E2E encrypted messaging on your own homeserver | **D2** |
| Signal (`signal-cli`) | E2E; hard to automate | D2 |
| SMTP (own server) + DKIM/SPF/DMARC | Email, digests | D1 |
| **Telegram Bot API** | The lowest-friction interactive channel | **D1** |
| Discord / Slack | Team visibility, queues | D1 |
| **WhatsApp Business Cloud API** | ⚠️ 24-hour window + approved templates | **D0** |
| **Presidio** | Pre-send PII/secret scanning | — |

**MCP integration:** MCP servers exist for Telegram, Discord and Slack. Since
Hermes already uses MCP, that is the natural connection path — but the MCP tool is
**never exposed directly to an agent**; it sits behind the Notification Broker.

### External records and archives

| Tool | For what | Gate |
|---|---|---|
| **OSF Registries** | **External, timestamped, immutable preregistration + DOI** | **G2** |
| **Zenodo** | Permanent archive + DOI (code, data, publication) | G9 |
| Software Heritage | Permanent source-code archive | G9 |
| ORCID | Persistent author identity | G9 |
| arXiv / bioRxiv | Preprint (submission automation is limited) | G9 |

**Why OSF matters at G2:** the internal `AnalysisPlanManifest` hash lives in *your*
system. An external record is evidence even to someone who does **not** trust your
system. That is the external anchor for the in-principle acceptance in B1. For
sensitive work, OSF offers an embargo option: timestamped now, private for a
defined period.

### Three architectural rules

1. **A notification is a flare, not a data channel.** Send a signed link, not the
   content.
2. **An inbound message is never an instruction.** Zone 3 — quarantine, tagging, no
   instruction extraction. (Outbound traffic is a data-exfiltration risk; **inbound
   traffic is a control-takeover risk.**)
3. **Messaging is not an authorisation channel.** A `DecisionRecord` is signed only
   on an authenticated surface. A chat reply is not an approval.

---

# PART G — Review against the ideal structure: gaps in the current architecture

An audit of the current `AIRL-OS-Architecture.md` v1.0 against the ideal structure
defined in Parts A–F.

## G1. Critical gaps

| # | Gap | Impact | Fix |
|---|---|---|---|
| **K1** | **Independence is assumed, not measured** — `Model Lineage` is a declaration; error correlation is never measured | The evidential value of all of G6 is unfounded. When two correlated models agree it is counted as "independent verification" | **C1 Agreement Calibration** |
| **K2** | **The 7 confidence scales have no measurement basis** — the producer is uncalibrated and no combination rule exists | The exact definition of `PR-12 False Rigor`. The system's most visible output rests on its weakest foundation | **C2 Confidence Calibration** + the min rule |
| **K3** | **The laboratory's own error rate is unknown** | No metric answers "are we producing correct results?" | **C4 Control injection** |
| **K4** | **Publication bias is open** — G2 freezes, but G8 can reject on the result | Negative results are lost systematically | **B1 In-principle acceptance** |
| **K5** | **A producer summoning its own helper is not forbidden** | The IndependenceMatrix can issue a false PASS; the other seven dimensions become void | **E2 Delegation Boundary dimension** |
| **K6** | **R3 + a hosted model = an impossible G7** | Reproducibility is "non-waivable" but cannot be delivered | **D4 R3 → local/open-weight mandatory** |
| **K7** | **`determine_assurance_class` is fail-open** | A missing risk profile → the lightest class | **E4: missing → R3, fall-through → R2** |
| **K8** | **Who is human and who is a model is unclear** | The org chart describes humans, the RoleContract describes models. At R3, Human Identity is non-compensable → in a solo operation every R3 project is permanently BLOCKED | **A decision is required — the A8 table must be filled in** |

## G2. High-priority gaps

| # | Gap | Fix |
|---|---|---|
| **Y1** | The analysis plan is not locked separately from the protocol → the decision rule can be changed after seeing the result | **A1 + a G2b `AnalysisPlanManifest`** |
| **Y2** | The analyst is not blinded (only the reviewer is) | **B2 Blinded analysis** |
| **Y3** | `repeatability/reproducibility/replication` are undefined; the tolerance appears at **three different values** (±2% / ≥95% / >5%) | **B4 ACM badges + the G7a/G7b split** |
| **Y4** | Suspicion of fabrication has no process and no owner | **A2 Research Integrity Officer** |
| **Y5** | Disagreement has a single arbiter, no round limit, and open findings can vanish silently | **B5 Delphi + E3 breaker + FindingLedger** |
| **Y6** | No mechanism against rubber-stamping (`PR-11` is in the register but not in the architecture) | **C5 Attention budget (a quota, not an SLA)** |
| **Y7** | The reviewer sees only aggregates → selective exclusion cannot be audited | A **separate mechanical audit** for exclusion decisions; the applied `exclusion_rules` are hashed into the packet |
| **Y8** | Which gates are working is never measured | **C3 Gate yield** |
| **Y9** | There is no mid-project risk escalation mechanism | **E5 RiskReclassificationEvent** |
| **Y10** | Publication text ↔ claim scope is not audited (`obligations` exists, nothing audits it) | **A5 + mechanical scope conformance** |
| **Y11** | There is no memory across projects | **A7 Knowledge Steward** |
| **Y12** | A Zotero group library is cloud egress; the D2+ data policy is undefined | The group library's data-class ceiling must be set **explicitly** (suggestion: **≤ D1**) |
| **Y13** | **There is no human notification/messaging layer at all** — a decision queue exists but no defined path to reach a human | **F8 Notification Broker** + the data-class ceiling + `notifying-humans` |
| **Y14** | The inbound quarantine chain was designed for PDFs and literature only; the email/message surface widens ACC-05 | `receiving-external-messages` — Zone 3 tagging, no instruction extraction |
| **Y15** | The preregistration is protected only by an internal hash — no external anchor | **OSF Registries** for an external timestamp and DOI at G2 |

## G3. Medium-priority gaps

| # | Gap | Fix |
|---|---|---|
| **O1** | A gVisor contradiction for the Light ExecutionProfile (§2 "optional" ↔ §9 `gvisor-kvm`) | One authoritative table; suggestion: **always gVisor**, differing only in the seccomp profile |
| **O2** | Unreachable code inside `determine_assurance_class` (the `downstream_user_count` block sits outside the function) | Move it into the function |
| **O3** | A point estimate is compared by percentage in a stochastic experiment | **Distribution comparison** (CI overlap / equivalence testing) |
| **O4** | The *power* of a test is never questioned | **B9 Severity assessment** |
| **O5** | The *diagnosticity* of evidence is never questioned — much evidence ≠ discriminating evidence | **B6 ACH matrix** |
| **O6** | A single analysis path; analytical degrees of freedom are unmeasured | **B3 Multi-analyst / multiverse** |
| **O7** | Whether `ReviewPacketBuilder` is a prompt or a program is ambiguous | **E1: a program, with a tested allowlist** |
| **O8** | There is no final review over the whole publication package | **E8-2: whole-package review with the most capable model** |
| **O9** | Produced datasets have no lifecycle owner | **A3 Data Steward + Croissant + DOI** |
| **O10** | Figure reproducibility is undefined | **F5: a figure = spec_hash + data_hash + renderer_version** |
| **O11** | pdfplumber is weak for span anchoring | **GROBID** |
| **O12** | The status of a result computed before preregistration is undefined | **E8: it cannot be `confirmatory`; it is reported as `exploratory`** |

## G4. Strengths of the current design that must be preserved

Do not touch these:

1. **The agent produces intent, the broker produces effect** — the architecture
   closes privilege escalation.
2. **RoleContract ≠ model** — the correct foundation for "let different models run
   it".
3. **The re-anchoring cascade** (RELOCATED/AMBIGUOUS/NEEDS_REANCHOR/ORPHANED) — a
   rare quality.
4. **412 → reconciliation, never a blind retry** — it genuinely protects human data.
5. **G10 = a Schedule, not a workflow** — it avoids the replay trap.
6. **Independent versioning of child workflows** — the same reason.
7. **A timeout is never an auto-approval** — fail-closed.
8. **Adversarial Reviewer as a separate role** — absent in most systems.
9. **Neo4j is derived, not canonical** — rebuildable.
10. **Sessions may merge; gate records stay separate** — a decision Superpowers
    independently confirms.
11. **A four-axis ExecutionProfile** — it rejects the "D0 = light sandbox" fallacy.
12. **`SourceRepresentation` versioning with the old hash immutable** — old evidence
    stays verifiable forever.

---

# PART H — Implementation order

By dependency. Each step is marked `decision` / `mechanical` / `model`.

## Phase 0 — Decisions (no code, but everything depends on them)

| # | Work | Type |
|---|---|---|
| 0.1 | **Fill in the A8 role table**: is each role human, model, mechanical or deferred | `decision` |
| 0.2 | **The model roster**: which profile in which tier (D3) | `decision` |
| 0.3 | **R3 scope**: is R3 possible in a solo operation? If not, which projects may be R3? | `decision` |
| 0.4 | **Accept D4**: R3 → local/open-weight mandatory | `decision` |
| 0.5 | **Accept B1**: G8 may not reject on the direction of the result | `decision` |
| 0.6 | The group library's data-class ceiling (suggestion ≤ D1) | `decision` |

## Phase 1 — Cheap mechanical wins (no models needed; immediate value)

| # | Work | Closes |
|---|---|---|
| 1.1 | The statcheck + GRIM/GRIMMER pipeline | B7, part of K2 |
| 1.2 | Scope conformance checking (publication text ↔ ClaimVersion) | A5, Y10 |
| 1.3 | Convert `ReviewPacketBuilder` into a program + an allowlist test | E1, O7 |
| 1.4 | Make `determine_assurance_class` fail-closed + fix the unreachable code | K7, O2 |
| 1.5 | Add the Delegation Boundary dimension to the Independence Matrix | **K5** |
| 1.6 | The G7a/G7b split + the ACM badge vocabulary; resolve the tolerance contradiction | **Y3** |
| 1.7 | The machine-readable `progress.jsonl` ledger | E7 |

## Phase 2 — Preregistration discipline

| # | Work | Closes |
|---|---|---|
| 2.1 | `AnalysisPlanManifest` as a separate object with a separate lock | **Y1** |
| 2.2 | `InPrincipleAcceptance` (G2 Stage-1) | **K4** |
| 2.3 | Mandatory exploratory / confirmatory labelling | O12, E8 |
| 2.4 | The severity assessment field | O4 |
| 2.5 | A mandatory pre-mortem before G4 | B8 |

## Phase 3 — The metascience plane

| # | Work | Closes |
|---|---|---|
| 3.1 | The agreement calibration set + κ/ρ measurement | **K1** |
| 3.2 | Confidence calibration: raw + calibrated + the `UNCALIBRATED` state | **K2** |
| 3.3 | Control injection (positive/negative, hidden from the agents) | **K3** |
| 3.4 | The human attention budget + its telemetry | **Y6** |
| 3.5 | Gate yield measurement | Y8 |
| 3.6 | The claim survival time series (from G10 data) | C6 |

## Phase 4 — Advanced review mechanisms

| # | Work | Closes |
|---|---|---|
| 4.1 | Delphi rounds + FindingLedger + the breaker | **Y5** |
| 4.2 | Multi-analyst (N independent analysis agents) | O6 |
| 4.3 | The ACH diagnosticity matrix | O5 |
| 4.4 | Blinded analysis | **Y2** |
| 4.5 | Multiverse / specification curve | O6 |
| 4.6 | Whole-package final review | O8 |

## Phase 5 — Roles and process

| # | Work |
|---|---|
| 5.1 | Research Integrity Officer + the `IntegrityCase` lifecycle (**Y4**) |
| 5.2 | Statistical Methods Owner authorities (**A1**) |
| 5.3 | Data Steward + Croissant + DOI (**O9**) |
| 5.4 | RSE + RO-Crate + Nix/Apptainer (**A4**) |
| 5.5 | Knowledge Steward + cross-project contradiction detection (**Y11**) |
| 5.6 | `RiskReclassificationEvent` (**Y9**) |

---

## Closing

Your current architecture is one of the most complete governance designs I have
seen for an AI-operated research laboratory. The division of authority, the broker
pattern and the re-anchoring cascade are genuinely good.

The one thing missing is **reflexivity**: the system audits the research but does
not audit itself. And in a laboratory operated by models that is not an optional
extra — **because what replaces the independent human referee is a set of models
that may be correlated, and until that correlation is measured the entire evidence
chain rests on an assumption.**

The seventh plane (Part C) closes that. The seven mechanical wins in Phase 1
require no models, cost little and produce value immediately — start there.

---

**Continued:** this document defines *what* should be added. *How* agents will
execute it — the skill layer, the iron laws, the rationalisation tables, the
escalation ladder and `ProducerResponse` — lives in the sibling document:
`AIRL_OS_SKILL_LAYER.md`
