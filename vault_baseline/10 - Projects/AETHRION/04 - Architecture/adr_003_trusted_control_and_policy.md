---
title: "ADR-003 — Trusted Control, Untrusted Data, and Policy Enforcement"
aliases:
  - "ADR-003"
cssclasses:
  - aethrion-decision-record
type: decision-record
category: architecture
status: ACCEPTED
summary: "A laboratory that reads papers, emails and web pages is continuously fed text written by people who are not its operators, and some of that text will try to act."
source: "docs/architecture/ADR-003_trusted_control_and_policy.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
  - aethrion/adr
---

> [!info] Generated view
> This note is generated from `docs/architecture/ADR-003_trusted_control_and_policy.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# ADR-003 — Trusted Control, Untrusted Data, and Policy Enforcement

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | How untrusted content is prevented from acquiring authority, and what evaluates policy |
| Sibling documents | `AETHRION_COMPONENT_REUSE.md` §6 · WP-049 · WP-136 · ACC-44 |
| Status | **ACCEPTED — 2026-08-22.** Architecture decided; neither component is built |
| Date | 2026-08-22 |

**In one paragraph.** A laboratory that reads papers, emails and web pages is
continuously fed text written by people who are not its operators, and some of
that text will try to act. The naive defence is a detector that classifies input
as malicious. This record rejects the detector **as a boundary**: the boundary is
structural — control flow comes from trusted intent, untrusted content may only
supply values — and enforcement is delegated to a policy engine with a formal
semantics rather than to bespoke code.

---

## 1. The decision

> **Untrusted content is data. Control flow comes only from trusted intent.
> Policy is evaluated by Cedar, not by hand-written conditionals, and any
> evaluation anomaly fails closed.**

---

## 2. Why not a detector

A prompt-injection classifier answers *does this text look hostile?* — a
question with no reliable answer, judged by the same class of system being
attacked.

The CaMeL result is the alternative: derive the plan from the **trusted** query,
let a quarantined path handle untrusted content **without tool access**, and
enforce capabilities on every data flow. Reported AgentDojo performance under
provable security is **67–77 % of tasks depending on the paper version** — the
discrepancy is recorded here rather than rounded to the flattering figure.

```
Human intent ──► CommandIntent ──► trusted planner ──► allowed capabilities
                                                          │
══════════════════════════ trust boundary ════════════════╪═══════════════
                                                          │
Paper · PDF · email · web page · abstract ──► UNTRUSTED DATA
                                                          │
             may supply values ─────────────────────────► │
             may provide evidence ──────────────────────► │
             may NOT create actions ─────────────── ✗
             may NOT expand permissions ─────────── ✗
             may NOT authorise external effects ─── ✗
```

**A detector remains useful as defence in depth.** It is never the boundary, and
`AETHRION_COMPONENT_REUSE.md` §12 records detector libraries as *rejected as a
boundary* for exactly this reason.

**This applies today.** The working bridge already hands abstract text to a
model through `get_source` — recorded as ACC-44 — and the only thing bounding it
now is that no tool can write.

## 3. Why Cedar

| Requirement | Cedar |
|---|---|
| Matches the domain | `principal · action · resource · context` is already the shape of `TaskContract` |
| Deny wins | `forbid` overrides `permit`, so a prohibition cannot be out-voted by a permission |
| Analysable | Formal semantics and schema validation, rather than a pile of conditionals |
| Auditable | The decision, the policy that produced it and its inputs are all recordable |

**OPA/Rego** stays the recorded alternative, and the choice is fixed only after a
bake-off over the same 50 AIRL policies, scored on expressivity, readability,
failure semantics, static validation, audit output and integration cost.

### 3.1 The wrapper rule

> **Any policy-evaluation anomaly — an erroring policy, a missing entity, an
> unresolvable attribute — is a DENY.**

An authorisation layer whose failure mode is *allow* is not an authorisation
layer. This is the same fail-closed principle the assurance classes already use.

### 3.2 What Cedar does not decide

Cedar decides whether an **action is permitted**. It does not decide whether a
claim is **accepted**. Gate semantics stay in AETHRION, and a policy engine must
never become an acceptance authority.

## 4. How this is measured

| Layer | Component | Role |
|---|---|---|
| Test harness | **Inspect AI** | Runs the scenarios |
| Hostile scenarios | **AgentDojo** | Supplies attacks written by someone else |
| Security architecture | **CaMeL pattern** | What is being tested |
| Enforcement | **Cedar** | What refuses |
| Acceptance | **AETHRION** | What the refusal means for a gate |

Measuring the boundary against **someone else's** attack suite is the point.
A system evaluated only against attacks it imagined is measuring its imagination.

## 5. Consequences

| Package | Change |
|---|---|
| **WP-136** | From *inbound content quarantine and injection detection* to **trusted control / untrusted data architecture** |
| **WP-049** | From *build a policy evaluator* to **integrate Cedar**, with the bake-off recorded |
| **ACC-44** | Extends: an authenticated structured `CommandIntent` must still succeed, so the boundary separates persuasion from authentication rather than inbound from outbound |

## 6. Decision

| Field | Value |
|---|---|
| Decision | **CaMeL-style control/data separation as the boundary; Cedar as the first-candidate policy engine; any evaluation anomaly denies** |
| Decided by | Platform Security Lead · Engineering Owner |
| Date | 2026-08-22 |

> **Neither is built.** This record fixes the architecture so that the wrong
> thing is not built first — a detector wired in as a boundary is expensive to
> remove once gates depend on it.
