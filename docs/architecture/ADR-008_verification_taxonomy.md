# ADR-008 — Verification Taxonomy V0–V3 and Verifier Qualification

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | What "machines verify" means when the machine is a language model |
| Sibling documents | `AETHRION_ARCHITECTURE.md` · `AETHRION_COMPONENT_REUSE.md` §4 · **`ADR-015`, which extends this record with routing and abstention** · WP-087 · WP-080 · WP-126 · ACC-61 · ACC-62 · ACC-76 |
| Status | **ACCEPTED — 2026-08-23.** Taxonomy decided; no verifier is built or qualified |
| Date | 2026-08-23 |

**In one paragraph.** This system's thesis is *agents produce, machines verify,
humans decide*. The word doing the most work is "verify", and it has been
carrying two incompatible meanings: a hash comparison that is either right or
wrong, and a language model judging whether a cited passage supports a sentence.
Calling both "mechanical verification" manufactures confidence — it lends the
certainty of the first to the fallibility of the second, in the one place where
this architecture is supposed to be most careful. This record splits the word
into four classes and requires the fallible ones to be measured before they can
satisfy anything.

---

## 1. The decision

> **Verification has four classes.** V0 deterministic · V1 computational or
> statistical · V2 model-mediated semantic · V3 human judgement. Every
> `VerificationResult` carries its class, assigned by the verifier service from
> the procedure that actually ran — never by the caller. **A V2 verdict cannot
> satisfy a required verification without a current `VerifierQualificationRecord`
> for that task type at that threshold.** The word "mechanical" is reserved for
> V0 and V1.

---

## 2. The four classes

| Class | What it is | Examples | Property |
|---|---|---|---|
| **V0** | Deterministic | digest comparison · schema validation · signature · reference resolution · timestamp ordering · artifact existence | Same input, same answer, always. **Never invokes a model.** |
| **V1** | Computational / statistical | score recomputation · statistical test · GRIM/statcheck-style consistency · tolerance comparison · row counts | Deterministic given pinned software and configuration |
| **V2** | Model-mediated semantic | citation entailment · claim scope and overclaim · method–code alignment · prior-art overlap · rubric grading | A judgement with an error rate. Machine-performed is not machine-proved |
| **V3** | Human scientific judgement | residual methodological interpretation · high-risk arbitration · G8 · integrity findings | Authority, not throughput |

The boundary that matters is **V1 | V2**. Everything at or below V1 either
succeeds or fails for a reason that can be stated exactly. Everything at V2 has a
false-positive rate and a false-negative rate, and those numbers exist whether or
not anyone has measured them.

---

## 3. Why "mechanical" was too broad

The prior vocabulary had one category for machine checks, and its most important
consumer was the gate rule *a mechanical check runs first and cannot be
overridden by a model.* That rule is correct for V0 and V1. Applied to V2 it says
something absurd: **that a model's judgement cannot be overridden by a model.**

Splitting the word repairs the rule rather than weakening it:

- A **V0** failure — a digest mismatch, a missing artifact — is non-waivable. No
  review and no human narrative overrides it.
- A **V2** failure is a finding with a confidence and a measured error rate,
  routed to review or to a human.

WP-087's scope changes accordingly: from *mechanical verification engine* to a
verification engine that **routes by class and records which class answered.**

---

## 4. Decomposing a single check

"Citation audit passed" is four different questions with four different
epistemic statuses, and reporting one verdict hides which of them actually ran:

| Question | Class |
|---|---|
| Does the reference exist and resolve? | V0 |
| Does the locator resolve in this representation version? | V0 |
| Does the quoted span match the source text digest? | V0/V1 |
| Does the cited passage **support** the sentence? | **V2** |
| Does the sentence claim **more** than the passage supports? | **V2** |

The first three are cheap and certain. The last two are the ones that catch a
hallucinated argument, and they are exactly the ones with an error rate. ACC-76
plants a sentence whose citation is real, resolvable and on-topic and does not
support it: the V0 checks must pass and the V2 checks must fail.

**Existence is not support.** The reference-verification measurement already in
this repository reports 27 of 33 sources corroborated, and that number says
records exist in public authorities — not that any claim is supported by them.

---

## 5. Why a verifier must be qualified

A judge that has never been measured is an opinion with institutional weight.

`VerifierQualificationRecord` carries precision, recall, specificity, false
positive and false negative rates on a labelled evaluation set, the threshold,
known failure modes and an expiry. It is keyed by:

```
verifier + version + task_type + domain profile + threshold
```

All five, because none is substitutable. Citation entailment, method–code
alignment and novelty grading are different tasks; a verifier good at one is not
thereby good at another, and a single global "reliability" number for a model is
the most misleading form this could take.

A threshold change on the same verifier version invalidates the qualification —
the threshold is part of what was measured. ACC-61 requires missing, expired and
threshold-mismatched qualifications all to yield `INCONCLUSIVE` and block the
gate, and only a current matching one to satisfy it.

### Reviewer calibration is a different record

A reviewer is a scientific role; a verifier is a bounded check. The same model may
serve both, and the records stay separate: verifiers are measured on
precision/recall against labelled sets; reviewers on agreement, decision accuracy
against controls, confidence calibration and order effects.

---

## 6. Controls have to fire

A detector suite reports "no findings" in the same words whether it is working or
inert. Every critical verifier therefore carries both a known-positive case that
must fail and a known-negative case that must pass, and **the suite fails if a
planted control stays silent.**

This is the discipline `scripts/monitor_sources.py` already applies — it exits
non-zero if its planted retracted DOI is not detected — generalised to every
verifier. It is also why ACC-76 includes a control sentence whose citation
genuinely supports it: a verifier that fails everything is not a verifier.

The known limitation is recorded rather than hidden: where support exists only in
a table or figure, a text-only verifier will miss it, and that case is measured
as a stated multimodal limitation rather than reported as a pass.

---

## 7. Independence is not "a different model"

Two verifiers from different providers may still share training sources, a prompt
ancestry, the same retrieved evidence or the same misreading of a specification.
Different is not independent.

So independence is **measured** on shared control sets rather than asserted from
configuration, and error correlation between verifier families is tracked. A
producer never selects its own verifier: the task compiler binds one from the
qualified pool under the independence profile.

---

## 8. Consequences

**Accepted:** V2 checks cannot be used until a labelled evaluation set exists.
Building those sets is real work and is a precondition, not a follow-up.

**Accepted:** more gates will report `INCONCLUSIVE`. That is the honest state
when the only available judge is unqualified, and it is better than a verdict
whose error rate nobody knows.

**Gained:** every verdict says which kind of thing produced it, so a reader can
tell a proof from an opinion.

**Gained:** the non-waivable rule becomes coherent — V0 failures are absolute
because they are the class where absolute means something.

---

## 8.1 What this record leaves open, and where it is decided

This record fixes what verification **is**. It does not say **when** each class
runs, or what a verifier does when the honest answer is *I cannot tell*.

Both are decided by [`ADR-015`](ADR-015_adaptive_assurance_routing.md): assurance
is routed by consequence and uncertainty rather than applied uniformly, and
`ABSTAIN` is a valid verdict that escalates rather than a failure. Nothing in
this record changes; the taxonomy and the qualification requirement below are
what that routing routes between.

---

## 9. Decision

**Accepted, 2026-08-23.** The taxonomy is the contract WP-087 delivers and WP-126
maintains. **No verifier is built and none is qualified.** The V0 checks that run
today — the plan seal, the evidence attestation, the reference resolver — predate
this record and are reclassified by it rather than created by it.
