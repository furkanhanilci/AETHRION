---
title: "ACC-108 — Escalation Is Not Selective Enforcement"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Escalation Is Not Selective Enforcement situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-108_selective_verifier_escalation.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-108 — Escalation Is Not Selective Enforcement

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-108` |
| Category | Assurance/Governance |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Internal Audit |
| Related packages | `WP-155` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Escalation Is Not Selective Enforcement** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The assurance router is active, the human queue is long, and a high-consequence claim is presented alongside several low-consequence ones.

**When:** Routing is performed under queue pressure.

**Then:** The high-consequence claim is routed by consequence, not by queue length. No route is lowered because the queue is long or the budget is tight, and a downgrade attempt is refused and audited.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Present a high-consequence claim with the human queue at capacity | Execution log + trace/event references |
| 2 | Read the route assigned and the inputs that decided it | Execution log + trace/event references |
| 3 | Attempt to lower the route because of queue length | Execution log + trace/event references |
| 4 | Attempt to lower it because of budget pressure | Execution log + trace/event references |
| 5 | Present low-consequence claims and confirm they route cheaply | Execution log + trace/event references |
| 6 | Read the audit trail for both downgrade attempts | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The high-consequence claim routes by consequence regardless of queue state
- [ ] A queue-length downgrade is refused and audited
- [ ] A budget-pressure downgrade is refused and audited
- [ ] Low-consequence claims do route cheaply — routing discriminates rather than maximising everywhere
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VerificationResult`
- `AssuranceRoute`
- `PolicyDecision`
- `Finding`

## Expected events

- `policy.denied`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-108-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-108-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-108-state-before.json` and `ACC-108-state-after.json`.
- `ACC-108-events.json`, `ACC-108-policy-decisions.json` and `ACC-108-audit-export.json`.
- `ACC-108-evidence-manifest.json`: the hash, producer and environment reference of every file.
- The independent witness's `VerificationRecord`, plus any finding and disposition records.

## PASS criteria

- All scenario-specific assertions and the common integrity assertions pass.
- **An expected fail-closed, block or revise behaviour is as valid a PASS as a happy-path success** — provided it matches the expected state exactly.
- No open Critical or High findings remain.
- The evidence manifest is complete, its hashes verified and the package signed by the witness.
- Results from a different release candidate have not been merged into this one.

## FAIL and retest

The scenario FAILs if any invariant, evidence-integrity check, or expected
record/event assertion fails. A correction is opened only against a `VALIDATED`
finding. If the target revision or any related policy, schema, model or tool
bundle changes, the previous result becomes void and the scenario plus its
affected regression set are rerun.

## Cleanup and reversal

Test claims are marked `TEST_CLOSED`; routing decisions and denials are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
