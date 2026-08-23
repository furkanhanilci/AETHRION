---
title: "ACC-07 — Reviewer Order Bias"
aliases:
  - "ACC-07"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Reviewer Order Bias situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-07_reviewer_order_bias.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-07 — Reviewer Order Bias

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-07` |
| Category | Model/Eval |
| Severity | **High** |
| Accountable owner | Eval Office |
| Independent witness / verifier | Independent Human Calibrator |
| Related packages | `WP-043`, `WP-086`, `WP-088`, `WP-105` |
| Acceptance phase | `PRE_GO_LIVE` — initial qualification |
| Recurring counterpart | `WP-126` · WP-126 runs the recurring recalibration of the same measure in Day-2 |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Reviewer Order Bias** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A calibration fixture holds the same two solution or claim packages, presentable to a blind reviewer profile as A/B and as B/A.

**When:** An order-randomised repeated evaluation runs and verdict, score and finding differences are measured.

**Then:** A material order effect fails the profile's calibration; the reviewer is not admitted to a critical role, or is suspended from it.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create the frozen identical package pair | Execution log + trace/event references |
| 2 | Run the review batch across balanced orders and seeds | Execution log + trace/event references |
| 3 | Verify that no identity or label leakage occurs | Execution log + trace/event references |
| 4 | Compute the verdict, finding and latency differences | Execution log + trace/event references |
| 5 | Apply the threshold and the statistical rule | Execution log + trace/event references |
| 6 | Produce the `CapabilityProfile` disposition | Execution log + trace/event references |
| 7 | Confirm the embargo held before running the order-randomisation measurement | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] An order effect within threshold passes; outside it, fails
- [ ] A failed profile is excluded from critical routing
- [ ] Raw reviews and run manifests are reproducible
- [ ] The human calibration decision is recorded
- [ ] Order bias is now **structurally prevented before it can be measured**: peer output is embargoed until every initial position is sealed — ACC-082.
- [ ] The sealed positions are what distinguish independent agreement from deference afterwards; a diagnostic run without them measures the wrong thing.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

This scenario measured order bias. The independent-first protocol removes most of its cause, so the measurement becomes a check that the embargo worked rather than the primary control — `ADR-011`.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `EvalRun`
- `CalibrationReport`
- `ReviewRecords`
- `CapabilityProfileDecision`

## Expected events

- `review.calibration.started`
- `review.bias.detected`
- `capability.suspended_or_admitted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-07-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-07-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-07-state-before.json` and `ACC-07-state-after.json`.
- `ACC-07-events.json`, `ACC-07-policy-decisions.json` and `ACC-07-audit-export.json`.
- `ACC-07-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The calibration fixture is preserved in the golden store; the model/profile result is not purged from the test namespace.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
