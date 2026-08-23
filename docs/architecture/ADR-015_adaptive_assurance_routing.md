# ADR-015 — Assurance Is Routed by Risk and Uncertainty, and a Verifier May Abstain

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | When each verification class runs, what happens when a verifier is unsure, and why abstention is a result |
| Sibling documents | **Extends `ADR-008`** (the V0–V3 taxonomy and qualification) · WP-155 · WP-126 · ACC-107 – ACC-109 |
| Status | **ACCEPTED — 2026-08-23.** Routing decided; no verifier is built or qualified |
| Date | 2026-08-23 |

**In one paragraph.** `ADR-008` fixed what verification *is* — four classes, and a semantic verifier
that cannot satisfy a requirement without a current qualification. It left open
what happens next: which class runs when, and what a verifier does when the
honest answer is *I cannot tell*. Forcing a binary verdict out of an uncertain
judge is how an error rate becomes invisible, so this record adds routing and
makes `ABSTAIN` a first-class outcome.

---

## 1. The decision

> **Assurance is routed, not uniformly applied.** V0 always runs first; V1 runs
> where the claim type demands it; V2 runs only on qualified task classes; V3 is
> reached by consequence or by uncertainty. **A semantic verifier may return
> `ABSTAIN`, and abstention is an escalation signal — never a pass, never a
> failure, never an error.**

> This record **extends `ADR-008`** and does not restate it. The class
> definitions, the qualification requirement and the rule that "mechanical" means
> V0 and V1 are all there.

---

## 2. Why uniform assurance is the wrong shape

Running every check on everything is the intuitive design and it fails in both
directions at once. Expensive semantic verification on an exploratory
`FEASIBILITY` run wastes the qualified verifier budget that a confirmatory claim
needs. And applying the same depth everywhere means the depth is set by what is
affordable across the whole workload, which is to say: too shallow where it
matters.

Routing inputs: the claim's consequence, the study mode's claim ceiling, the
assurance class, the verifier's measured uncertainty on this task class, and
whether a cheaper class already resolved the question.

---

## 3. The cascade

```
V0 deterministic ──fail──► non-waivable stop
     │ pass
     ▼
V1 computational ──fail──► non-waivable stop
     │ pass
     ▼
V2 qualified semantic ──┬── confident PASS/FAIL ──► finding, routed to review
                        └── ABSTAIN / low confidence
                                 │
                                 ▼
              stronger independent verifier, or V3 human
```

**The number of verifiers is not fixed.** It is set by marginal information gain
and by the independence requirement — a second verifier that shares the first's
training sources and prompt ancestry adds cost and very little information, which
is why `ADR-008` requires error correlation to be *measured* rather than inferred
from a provider name.

---

## 4. Abstention is the load-bearing addition

A judge forced to choose between PASS and FAIL on a case it cannot resolve will
choose, and the choice will look exactly like a confident one in the record.
Every downstream reader then inherits a verdict whose real content was a coin
flip.

So `ABSTAIN` and `INSUFFICIENT_CONFIDENCE` are valid verdicts, and three rules
follow:

- **Abstention never satisfies a required verification.** It escalates.
- **Abstention is not a verifier failure.** A verifier that never abstains on a
  genuinely ambiguous fixture is miscalibrated, and its qualification should say
  so — ACC-109.
- **Abstention rate is a qualification metric**, tracked alongside precision and
  recall. A verifier abstaining on 90% of its task class has coverage, not
  accuracy.

---

## 5. What routing may never do

**Escalation is not selective enforcement.** A router that sends only the
convenient cases to a human, or that lowers the class because the queue is long,
has converted an assurance mechanism into a throughput mechanism. ACC-108 plants
exactly that: a high-consequence claim routed to the cheap path.

**Budget pressure does not lower an assurance route.** `ADR-011`'s cohort and
this record's route are both outside the budget governor's reach; what degrades
under budget pressure is communication verbosity (`ADR-013`), and a task that
cannot afford its required assurance is `BLOCKED`, not quietly downgraded.

---

## 6. Consequences

**Accepted:** more `INCONCLUSIVE` and `ESCALATED` outcomes, and a human queue
that grows when verifiers are honest about uncertainty. That is the correct
direction for the queue to grow.

**Accepted:** routing logic is a place where a subtle bug silently weakens
assurance for a whole class of claims, which is why ACC-108 exists.

**Gained:** the expensive classes are spent where consequence is highest rather
than spread evenly and thinly.

**Rejected:** a fixed verifier count per gate. It is easy to specify, easy to
audit, and it buys correlated opinions at high assurance while over-verifying
low-consequence work.

---

## 7. Decision

**Accepted, 2026-08-23.** Routing is what WP-155 delivers; the qualification
records it depends on are WP-126's. **No verifier is built, none is qualified,
and no calibration set exists**, so every route in this record currently resolves
to the same place: unavailable.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-008`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
