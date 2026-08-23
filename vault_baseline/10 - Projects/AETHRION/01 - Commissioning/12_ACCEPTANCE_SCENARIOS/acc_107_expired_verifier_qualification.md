---
title: "ACC-107 — Expired Verifier Qualification"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Expired Verifier Qualification situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-107_expired_verifier_qualification.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-107 — Expired Verifier Qualification

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-107` |
| Category | Assurance/Model |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Eval Office |
| Related packages | `WP-044`, `WP-155` |
| Acceptance phase | `PRE_GO_LIVE` |
| Recurring counterpart | `WP-126` · WP-126 runs the recurring verifier recalibration and requalification in Day-2 |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Expired Verifier Qualification** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A V2 verifier's qualification for the task class has passed its `valid_until` date, and a second verifier's threshold has changed since it was measured.

**When:** A required verification is requested from each.

**Then:** Both yield `INCONCLUSIVE` and block the gate. Their verdicts are retained as advisory. Only a current, matching qualification satisfies the requirement.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Request a required verification from a verifier with an expired qualification | Execution log + trace/event references |
| 2 | Request one from a verifier whose threshold changed after measurement | Execution log + trace/event references |
| 3 | Request one from a verifier with a current, matching qualification | Execution log + trace/event references |
| 4 | Read the gate state in each case | Execution log + trace/event references |
| 5 | Confirm the advisory verdicts are retained and labelled | Execution log + trace/event references |
| 6 | Requalify the expired verifier and repeat | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The expired qualification yields `INCONCLUSIVE` and blocks the gate
- [ ] A threshold change invalidates the qualification independently of the expiry date
- [ ] Only the current, matching qualification satisfies the requirement
- [ ] Advisory verdicts are retained and labelled, not discarded
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VerifierQualificationRecord`
- `VerificationResult`
- `GateRecord`

## Expected events

- `qualification.expired`
- `verification.inconclusive`
- `gate.blocked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-107-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-107-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-107-state-before.json` and `ACC-107-state-after.json`.
- `ACC-107-events.json`, `ACC-107-policy-decisions.json` and `ACC-107-audit-export.json`.
- `ACC-107-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test qualifications are marked `TEST_CLOSED`; the verifier registry is restored to baseline.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
