---
title: "ACC-61 — Unqualified Semantic Verifier"
aliases:
  - "ACC-61"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Unqualified Semantic Verifier situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-61_unqualified_semantic_verifier.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-61 — Unqualified Semantic Verifier

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-61` |
| Category | Assurance/Model |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Eval Office / Internal Audit |
| Related packages | `WP-044`, `WP-087` |
| Acceptance phase | `PRE_GO_LIVE` |
| Recurring counterpart | `WP-126` · WP-126 runs the recurring verifier recalibration and requalification in Day-2 |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Unqualified Semantic Verifier** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A V2 semantic verifier is asked for a citation-entailment verdict, and its `VerifierQualificationRecord` for that task type is missing, expired, or was measured at a different threshold.

**When:** G6 requires that verification to pass.

**Then:** The verdict is recorded as advisory and cannot satisfy the requirement; the gate blocks with `INCONCLUSIVE` rather than passing or failing the claim on an unqualified judgement.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Register a V2 verifier with no qualification for the task type | Execution log + trace/event references |
| 2 | Request a required entailment verification at G6 | Execution log + trace/event references |
| 3 | Repeat with a qualification that has expired | Execution log + trace/event references |
| 4 | Repeat with a valid qualification measured at a different threshold | Execution log + trace/event references |
| 5 | Repeat with a current, matching qualification | Execution log + trace/event references |
| 6 | Read the gate state and the verification classes in each case | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The unqualified, expired and threshold-mismatched cases all yield `INCONCLUSIVE` and block the gate
- [ ] The advisory verdict is retained and labelled, not discarded
- [ ] Only the current, matching qualification satisfies the requirement
- [ ] A threshold change on the same verifier version invalidates the qualification
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VerificationResult`
- `VerifierQualificationRecord`
- `GateRecord`

## Expected events

- `verification.inconclusive`
- `gate.blocked`
- `qualification.expired`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-61-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-61-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-61-state-before.json` and `ACC-61-state-after.json`.
- `ACC-61-events.json`, `ACC-61-policy-decisions.json` and `ACC-61-audit-export.json`.
- `ACC-61-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test qualification records are marked `TEST_CLOSED`; the verifier registry is restored to its baseline.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
