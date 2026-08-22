> [!info] Generated view
> This note is generated from `skills/receiving-review/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: receiving-review
version: 1.0.0
description: Use when a ReviewVerdict arrives, when review conditions must be addressed, or when you disagree with a finding
gates: [G6, G8]
roles: [Engineering Owner, Scientific Owner, Evidence Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [ProducerResponse]
mechanical_checks: [every_condition_has_stance, no_unanswered_condition_at_gate]
---

# Receiving Review

## Core principle

> **Verify before implementing. Ask before assuming.
> Technical correctness over social comfort.**

## Iron law

> **EVERY CONDITION MUST CARRY A STANCE.**
>
> Proceeding to G8 with an unanswered condition is forbidden.

## Sequence

```
Read → Understand → VERIFY → Evaluate → Respond → Implement
```

**If any item is unclear: STOP.** Implement nothing. Unclear items are often
coupled — misreading one corrupts the fix for another.

Then, in order: blocking issues → simple fixes → complex fixes. **One at a time,
each verified separately**, with a regression check at the end.

## Disagreement is legitimate

Push back when the finding:

- Breaks existing working behaviour
- Was made without full context
- Requests something outside scope (YAGNI)
- Contradicts the frozen protocol
- Is technically incorrect

**How:** with technical reasoning, without defensiveness. Point at a passing
test, a run record, or a manifest.

**Why this matters in a model-run lab:** models are sycophantic. Left
unspecified, a producer agrees where it should object — and review degenerates
into an approval ritual in which nobody learns anything. Making disagreement
explicitly legitimate is what keeps review informative.

## Forbidden: performative agreement

> "Great point!", "You're absolutely right!", "Good catch!"

Comprehension is demonstrated by **action**, not by compliment. When a
correction is warranted, one sentence suffices: *"Verified — you're right.
Fixing now."*

## `ProducerResponse` — required output

```yaml
per_condition:
  - condition_id: "C-01"
    stance: "ACCEPTED"          # ACCEPTED | DISPUTED | CLARIFICATION_NEEDED
    action_taken: "..."
    evidence_ref: "..."
    verified_by: "mechanical:scope-conformance"   # WHO verified it
  - condition_id: "C-02"
    stance: "DISPUTED"
    technical_rationale: "..."
    escalated_to: "DisagreementCase disagree-..."
```

`ACCEPTED` requires **independent verification** — the producer's own assertion
is not sufficient. `DISPUTED` is bound to a `DisagreementCase`.

## Rationalization table

| Justification | Ruling |
|---|---|
| "We already satisfy that condition" | **Prove it.** Fill `verified_by`. |
| "It's minor, we'll look later" | Minor still takes a stance: `PARKED` with owner and expiry. |
| "The reviewer misunderstood" | Possibly — write `DISPUTED` with reasoning. **Do not pass over it silently.** |
| "I agree with all of them" (all at once) | Suspicious. Each condition is verified separately. |
| "Arguing back will slow us down" | Unexamined agreement is slower — it surfaces at G7 instead. |

## Red flags

- All conditions `ACCEPTED` in a single move
- `verified_by` naming the producer itself
- A response containing compliments but no evidence
- A condition with no stance at gate time
