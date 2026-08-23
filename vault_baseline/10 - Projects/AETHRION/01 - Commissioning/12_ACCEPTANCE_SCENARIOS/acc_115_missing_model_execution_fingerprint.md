---
title: "ACC-115 — Missing Model Execution Fingerprint"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Missing Model Execution Fingerprint situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-115_missing_model_execution_fingerprint.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-115 — Missing Model Execution Fingerprint

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-115` |
| Category | Evidence/Reproduction |
| Severity | **Critical** |
| Accountable owner | Reproducibility Lead |
| Independent witness / verifier | AI Observability Lead |
| Related packages | `WP-082`, `WP-157` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Missing Model Execution Fingerprint** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A model invocation contributes to a published result, and a second invocation silently fails over to a different provider mid-run.

**When:** Both runs are recorded and a reproduction level is asserted.

**Then:** An invocation without a complete fingerprint fails the run. The failover appears in the fingerprint's retry and fallback history and invalidates any `EXACT` claim.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Execute a contributing invocation with fingerprint capture disabled | Execution log + trace/event references |
| 2 | Confirm the run fails rather than recording an incomplete result | Execution log + trace/event references |
| 3 | Execute a run that silently fails over to another provider | Execution log + trace/event references |
| 4 | Read the retry and fallback history in the fingerprint | Execution log + trace/event references |
| 5 | Attempt to assert `EXACT` for that run | Execution log + trace/event references |
| 6 | Confirm a complete fingerprint on a clean run permits its declared level | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] A contributing invocation with no fingerprint fails the run
- [ ] A silent failover appears in the retry and fallback history
- [ ] `EXACT` cannot be asserted for a run that failed over
- [ ] A clean run with a complete fingerprint supports its declared level
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ModelExecutionFingerprint`
- `ExperimentRun`
- `ReproductionRun`

## Expected events

- `run.fingerprint_recorded`
- `run.rejected`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-115-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-115-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-115-state-before.json` and `ACC-115-state-after.json`.
- `ACC-115-events.json`, `ACC-115-policy-decisions.json` and `ACC-115-audit-export.json`.
- `ACC-115-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test runs are marked `TEST_CLOSED`; fingerprints are retained permanently as part of the run record.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
