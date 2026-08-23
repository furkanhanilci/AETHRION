---
title: "ACC-63 — Failed Experiment Must Be Recorded"
aliases:
  - "ACC-63"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Failed Experiment Must Be Recorded situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-63_failed_experiment_recorded.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-63 — Failed Experiment Must Be Recorded

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-63` |
| Category | Experiment/Knowledge |
| Severity | **High** |
| Accountable owner | Experiment Platform Lead |
| Independent witness / verifier | Knowledge Lead / Internal Audit |
| Related packages | `WP-082`, `WP-146` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Failed Experiment Must Be Recorded** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A candidate execution crashes partway through a discovery campaign.

**When:** The campaign moves on to the next candidate.

**Then:** It cannot advance until an immutable `ExperimentRun`, a `FailureAssessment` and a `FailedApproach` record exist, carrying the logs and artifacts the failure produced.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Run a candidate that crashes after producing partial output | Execution log + trace/event references |
| 2 | Observe the campaign's attempt to advance | Execution log + trace/event references |
| 3 | Read the failure records created before the advance | Execution log + trace/event references |
| 4 | Confirm the partial artifacts are retained and addressable | Execution log + trace/event references |
| 5 | Query the failed-approach memory for the same context | Execution log + trace/event references |
| 6 | Delete nothing and rerun the query after the campaign closes | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The campaign does not advance before the three records exist
- [ ] The partial artifacts are retained, not discarded as noise
- [ ] The failed approach remains retrievable after the campaign closes
- [ ] The failure class is recorded, not left as a bare error string
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ExperimentRun`
- `FailureAssessment`
- `FailedApproach`
- `ArtifactRecord`

## Expected events

- `experiment.run_failed`
- `knowledge.failed_approach_recorded`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-63-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-63-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-63-state-before.json` and `ACC-63-state-after.json`.
- `ACC-63-events.json`, `ACC-63-policy-decisions.json` and `ACC-63-audit-export.json`.
- `ACC-63-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The campaign is marked `TEST_CLOSED`; failure records and artifacts are retained deliberately.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
