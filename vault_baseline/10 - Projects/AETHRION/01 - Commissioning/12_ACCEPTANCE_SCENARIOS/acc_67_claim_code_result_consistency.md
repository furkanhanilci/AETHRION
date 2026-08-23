---
title: "ACC-67 — Claim–Code–Result Consistency Failure"
aliases:
  - "ACC-67"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Claim–Code–Result Consistency Failure situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-67_claim_code_result_consistency.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-67 — Claim–Code–Result Consistency Failure

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-67` |
| Category | Evidence/Reproduction |
| Severity | **Critical** |
| Accountable owner | Reproducibility Lead |
| Independent witness / verifier | Assurance Lead / Independent Grader |
| Related packages | `WP-085`, `WP-087`, `WP-113` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Claim–Code–Result Consistency Failure** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A reproduction script exits with status 0 and produces a result outside the declared tolerance, and a second run lands inside tolerance by a materially different method than the one the claim describes.

**When:** The consistency comparison is performed.

**Then:** Both are reported `INCONSISTENT` and G7 does not pass. Exit code 0 is not a reproduction, and a matching number reached by the wrong method is not one either.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Reproduce with a deliberate numeric deviation beyond tolerance | Execution log + trace/event references |
| 2 | Reproduce with a matching number produced by a substituted method | Execution log + trace/event references |
| 3 | Reproduce faithfully within tolerance | Execution log + trace/event references |
| 4 | Reproduce a claim whose method description is genuinely ambiguous | Execution log + trace/event references |
| 5 | Read the method, data and result consistency fields in each report | Execution log + trace/event references |
| 6 | Read the G7 gate state in each case | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The out-of-tolerance run is `INCONSISTENT` despite exit code 0
- [ ] The right-number-wrong-method run is `INCONSISTENT` on the method dimension
- [ ] The faithful run is `CONSISTENT` and passes
- [ ] The ambiguous case is `INCONCLUSIVE`, not forced to pass or fail
- [ ] Method, data and result consistency are reported separately, not collapsed into one verdict
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ClaimConsistencyReport`
- `VerifiedValue`
- `ReproductionRun`
- `GateRecord`

## Expected events

- `reproduction.consistency_failed`
- `gate.blocked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-67-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-67-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-67-state-before.json` and `ACC-67-state-after.json`.
- `ACC-67-events.json`, `ACC-67-policy-decisions.json` and `ACC-67-audit-export.json`.
- `ACC-67-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test reproductions are marked `TEST_CLOSED`; every report and its inputs are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
