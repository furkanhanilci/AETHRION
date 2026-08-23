---
title: "ACC-095 — Failure Taxonomy Routing"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Failure Taxonomy Routing situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-095_failure_taxonomy_routing.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-095 — Failure Taxonomy Routing

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-095` |
| Category | Resilience/Diagnostics |
| Severity | **High** |
| Accountable owner | Incident Commander / SRE Lead |
| Independent witness / verifier | Research Director |
| Related packages | `WP-082`, `WP-152` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Failure Taxonomy Routing** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** One failure of each class is available: implementation, methodology, data, hypothesis, infrastructure, coordination, verification, security and unknown.

**When:** Each is classified and routed.

**Then:** Each reaches its owning discipline. A `HYPOTHESIS` class is reachable only from a validly executed run under the frozen plan — the other classes cannot produce it however the run failed.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Produce one failure of each class | Execution log + trace/event references |
| 2 | Classify each and read the routing | Execution log + trace/event references |
| 3 | Confirm each reaches its named owner | Execution log + trace/event references |
| 4 | Attempt to classify a compile failure as `HYPOTHESIS` | Execution log + trace/event references |
| 5 | Attempt to classify a corrupted-data failure as `HYPOTHESIS` | Execution log + trace/event references |
| 6 | Classify a valid preregistered null result and confirm `HYPOTHESIS` is reachable | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Every class routes to its named owning discipline
- [ ] A compile failure cannot be classified `HYPOTHESIS`
- [ ] A data failure cannot be classified `HYPOTHESIS`
- [ ] A validly executed null result can be, and produces a `NegativeResult`
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `FailureAssessment`
- `FailedApproach`
- `NegativeResult`
- `ExperimentRun`

## Expected events

- `failure.assessed`
- `knowledge.failed_approach_recorded`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-095-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-095-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-095-state-before.json` and `ACC-095-state-after.json`.
- `ACC-095-events.json`, `ACC-095-policy-decisions.json` and `ACC-095-audit-export.json`.
- `ACC-095-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

All test failures are marked `TEST_CLOSED` and retained; failure records are never deleted.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
