---
title: "ACC-64 — Implementation Failure Must Not Refute a Hypothesis"
aliases:
  - "ACC-64"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Implementation Failure Must Not Refute a Hypothesis situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-64_implementation_failure_not_refutation.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-64 — Implementation Failure Must Not Refute a Hypothesis

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-64` |
| Category | Research/Integrity |
| Severity | **Critical** |
| Accountable owner | Research Director |
| Independent witness / verifier | Methodologist / Assurance Lead |
| Related packages | `WP-082`, `WP-143`, `WP-144` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Implementation Failure Must Not Refute a Hypothesis** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A candidate testing `HYP-002` fails to compile, and a second candidate fails on a corrupted input dataset.

**When:** The system classifies both failures and any downstream transition is attempted.

**Then:** Both are classified — IMPLEMENTATION and DATA — and any transition that would set `HYP-002` to REFUTED is refused. Only a validly executed run under the frozen plan can support a HYPOTHESIS failure class.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Run a candidate with a deliberate syntax error | Execution log + trace/event references |
| 2 | Run a second candidate against a deliberately corrupted dataset | Execution log + trace/event references |
| 3 | Run a third candidate that executes correctly and produces a preregistered null result | Execution log + trace/event references |
| 4 | Attempt to set `HYP-002` REFUTED after each of the first two | Execution log + trace/event references |
| 5 | Read the failure classes assigned | Execution log + trace/event references |
| 6 | Read the hypothesis status after all three | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The compile failure is classified IMPLEMENTATION, not HYPOTHESIS
- [ ] The corrupted-data failure is classified DATA, not HYPOTHESIS
- [ ] Both attempts to mark the hypothesis REFUTED are refused
- [ ] The valid null result is eligible for assessment and can produce a `NegativeResult`
- [ ] `HYP-002` remains untested after the first two runs, not refuted
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `FailureAssessment`
- `HypothesisVersion`
- `NegativeResult`
- `ExperimentRun`

## Expected events

- `experiment.run_failed`
- `hypothesis.status_transition_refused`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-64-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-64-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-64-state-before.json` and `ACC-64-state-after.json`.
- `ACC-64-events.json`, `ACC-64-policy-decisions.json` and `ACC-64-audit-export.json`.
- `ACC-64-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test hypothesis and its runs are marked `TEST_CLOSED`; all three runs are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
