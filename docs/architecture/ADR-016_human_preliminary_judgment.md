# ADR-016 — The Human Judges Before the Machine Recommends

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | The order in which a G8 decision surface reveals things, and why the order is the control |
| Sibling documents | `ADR-011` · `AETHRION_ROLES.md` · WP-156 · WP-093 · WP-004 · ACC-110 – ACC-112 |
| Status | **ACCEPTED — 2026-08-23.** Ordering decided; no decision surface exists |
| Date | 2026-08-23 |

**In one paragraph.** "Humans decide" is the third clause of this system's thesis, and it is the one
most easily satisfied on paper and lost in practice. A human shown a confident AI
recommendation before the evidence does not evaluate the evidence — they evaluate
the recommendation, and published work on automation bias is consistent about
which way that goes. The control is not more training or a warning banner. It is
the order of reveal.

---

## 1. The decision

> **At G8 the human records a `HumanPreliminaryAssessment` from the evidence,
> before any AI or reviewer recommendation is revealed.** The preliminary
> assessment is sealed. The recommendation is then shown, and any change produces
> a recorded `DecisionDelta`. **Rejecting must never cost more effort than
> accepting.**

---

## 2. Why ordering rather than warning

An automation-bias warning asks a person to discount information they have
already read, which is not a thing people can do on request. Withholding it until
they have formed a view is a thing the *system* can do, and it costs one screen.

The evidence a human sees first: the claim, its evidence, the counter-evidence,
protocol deviations, reproduction status, limitations, and every unresolved
finding. Not the recommendation, not the confidence score, not the reviewer's
verdict.

**The `DecisionDelta` is the measurement.** Where a human's preliminary
assessment and their final decision diverge, something moved them — and
aggregated over time, that is the only direct evidence of how much the
recommendation is actually driving. A system that never records the preliminary
view cannot distinguish a human who agreed from a human who deferred.

---

## 3. Friction symmetry

The second failure is quieter than anchoring. If accepting is one click and
rejecting requires a written justification, a form and a reviewer, the interface
has expressed a preference — and under load, people follow interfaces.

So: **the correction path may not be more laborious than the approval path.**
Evidence deep links open in one action. A rejection needs a reason and does not
need a ceremony. ACC-112 tests the two paths for effort symmetry, which is an
unusual thing to test and is the point.

---

## 4. Six decision values, because two is a false choice

`ACCEPT` · `ACCEPT_WITH_LIMITATIONS` · `REVISE` · `REJECT` · `ESCALATE` ·
`INSUFFICIENT_BASIS`.

The last one is the one that matters and the one usually missing. A human who
cannot tell, and whose only options are accept and reject, will accept — and
published work reports that access to AI advice measurably reduces people's
willingness to say they do not know. `INSUFFICIENT_BASIS` is a legitimate
terminal state that returns the package for more evidence, and ACC-111 requires
it to be reachable in one action.

---

## 5. What still holds from before

Nothing here weakens the existing rules, and they are restated because this is
the record a decision-surface implementer will read:

- **A timeout never approves.** It escalates and pages — ACC-069.
- **A learned preference never approves.** That this operator usually approves
  this class may order the queue and may not sign.
- **`HumanAttentionScore` orders and does not authorise.** A mandatory gate at
  the bottom of the queue still blocks.
- **Every intervention is atomically audited.** If the audit write fails, the
  edit fails — ACC-068.

---

## 6. Consequences

**Accepted:** G8 becomes slower by one deliberate step, on the gate where slower
is the intent.

**Accepted:** a determined human can click through the preliminary screen without
reading. The control reduces anchoring; it cannot manufacture attention, and no
mechanism in this architecture claims to.

**Gained:** how much the recommendation moves the decision becomes a measured
quantity — one of the few automation-bias signals that can be read off a system
rather than inferred.

**Rejected:** showing the recommendation first with a bias warning. It is the
common design, it is cheaper, and it measures nothing.

---

## 7. Decision

**Accepted, 2026-08-23.** The flow is what WP-156 delivers into WP-093's decision
queue. **No decision surface exists**, no `HumanPreliminaryAssessment` has been
recorded, and G8 has never run.

---

## Provenance

Proposed by the reliability completion delta of 2026-08-23 as its `ADR-009`.
Renumbered here because that identifier was already taken — see
[`../review/2026-08-23_reliability_delta_id_remap.md`](../review/2026-08-23_reliability_delta_id_remap.md).
