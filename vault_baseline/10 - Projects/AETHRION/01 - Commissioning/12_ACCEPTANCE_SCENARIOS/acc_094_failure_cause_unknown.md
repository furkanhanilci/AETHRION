---
title: "ACC-094 — An Unattributable Failure Is `UNKNOWN`"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the An Unattributable Failure Is UNKNOWN situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-094_failure_cause_unknown.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-094 — An Unattributable Failure Is `UNKNOWN`

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-094` |
| Category | Resilience/Diagnostics |
| Severity | **High** |
| Accountable owner | Incident Commander / SRE Lead |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-152` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **An Unattributable Failure Is `UNKNOWN`** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A multi-agent run fails in a way whose exact cause cannot be established from the trace.

**When:** The attribution pipeline runs.

**Then:** The failure is classified `UNKNOWN` and routed to human diagnosis. It is not forced into a named class, and `UNKNOWN` is a terminal classification rather than a pipeline defect.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Construct a failure whose cause is genuinely ambiguous in the trace | Execution log + trace/event references |
| 2 | Run the attribution pipeline | Execution log + trace/event references |
| 3 | Read the assigned class and the confidence recorded with it | Execution log + trace/event references |
| 4 | Confirm routing to human diagnosis | Execution log + trace/event references |
| 5 | Run the pipeline on a failure with an unambiguous cause | Execution log + trace/event references |
| 6 | Compare the confidence recorded in both cases | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The ambiguous failure is classified `UNKNOWN`, not forced into a named class
- [ ] `UNKNOWN` routes to human diagnosis and is terminal, not an error state
- [ ] The unambiguous failure is classified correctly — the pipeline discriminates
- [ ] Attribution confidence is recorded in both cases
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `FailureAssessment`
- `Finding`
- `AuditEntry`

## Expected events

- `failure.assessed`
- `failure.escalated`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-094-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-094-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-094-state-before.json` and `ACC-094-state-after.json`.
- `ACC-094-events.json`, `ACC-094-policy-decisions.json` and `ACC-094-audit-export.json`.
- `ACC-094-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test run is marked `TEST_CLOSED`; both assessments are retained for attribution calibration.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
