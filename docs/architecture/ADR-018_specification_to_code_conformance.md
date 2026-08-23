# ADR-018 — Frozen Specification and Running Code Must Still Agree

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | What happens when the implementation quietly diverges from the method it is supposed to implement |
| Sibling documents | `ADR-012` (dual disciplines) · `ADR-007` · WP-154 · WP-081 · ACC-103 · ACC-104 |
| Status | **ACCEPTED — 2026-08-23.** Severity model decided; no conformance check exists |
| Date | 2026-08-23 |

**In one paragraph.** A protocol is frozen at G2 and the code is written afterwards. Between those two
points sits the failure mode that autonomous research keeps reporting:
implementation drift. Under execution pressure the method quietly changes — a
different metric scale, a simplified algorithm, an omitted baseline, an altered
data split — and every downstream artifact stays internally consistent. The paper
describes the frozen method; the results come from a different one; nothing
disagrees with anything.

---

## 1. The decision

> **The frozen specification is compared against the code that actually ran, and
> the deviation carries a severity that can change the study's scientific
> status.** An unapproved `SCIENTIFIC_MAJOR` deviation cannot carry a confirmatory
> package forward — the minimum consequence is relabelling to exploratory, or a
> re-freeze and a re-run.

---

## 2. Why review does not catch this

Code review asks whether the code is correct. It is: the simplified algorithm is
implemented cleanly, the tests pass, the metric computes. Scientific review reads
the method section, which describes the frozen protocol, and the described method
is sound.

**Neither reviewer compares the two documents**, and that is the gap. Catching
drift requires putting the frozen specification and the running code side by side
and asking whether they are the same method — which is a distinct check with a
distinct record.

The frozen inputs are already digested for other reasons:
`AlgorithmUnderstandingRecord`, `EvaluationContract`, `ExperimentPlan`,
`AnalysisPlanManifest`, `MutationPolicy`.

---

## 3. The severity ladder is the whole design

| Severity | Meaning | Consequence |
|---|---|---|
| `NONE` | Implements the specification | — |
| `ENGINEERING_ONLY` | Refactor, performance, structure. Same method | Recorded; no scientific effect |
| `SCIENTIFIC_MINOR` | Real but bounded — a tolerance, a default, a logged deviation | Recorded and reported with the result — ACC-103 |
| `SCIENTIFIC_MAJOR` | Changes what the result *means* | Confirmatory status cannot survive unapproved — ACC-104 |
| `UNKNOWN` | The comparison could not be made confidently | **Escalates.** Not a pass |

`ENGINEERING_ONLY` is what keeps the check usable. Without it every refactor
becomes a scientific event, the check produces constant noise, and it gets turned
off — which is how a control designed too strictly ends up providing nothing.

`UNKNOWN` is what keeps it honest. Method–code alignment is a **V2** judgement
under `ADR-008`, model-mediated with a measured error rate, and a verifier that
cannot tell must say so rather than defaulting to `NONE`.

---

## 4. Measured in both directions

Positive fixtures — deliberate drifts the detector must catch: metric scale swap,
simplified algorithm, omitted baseline, changed seed policy, altered data split,
hidden preprocessing, removed stopping criterion.

**And a clean implementation it must pass.** A detector that flags every
implementation is not a detector, it is an obstacle, and its findings will be
routinely dismissed — which is worse than not having it, because the dismissal
becomes habitual.

---

## 5. Consequences

**Accepted:** the frozen specification must be precise enough to compare against.
Vague protocol prose makes this check impossible, which is a useful pressure on
G2 and an annoying one.

**Accepted:** a false `SCIENTIFIC_MAJOR` on a real confirmatory study is
expensive — hence the qualification requirement and the human in the loop before
relabelling.

**Gained:** "the code does what the method says" becomes an artifact with a
severity and a decision, rather than an assumption nobody was assigned to check.

**Rejected:** trusting the method section. It describes intent, and drift is
precisely the case where intent and execution parted company.

---

## 6. Decision

**Accepted, 2026-08-23.** The record and its severity model are what WP-154
delivers. **No conformance check exists**, no drift fixture has been built, and
no specification in this repository has ever been compared against code.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-011`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
