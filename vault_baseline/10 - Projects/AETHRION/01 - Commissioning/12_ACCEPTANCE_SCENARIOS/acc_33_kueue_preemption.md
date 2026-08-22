---
title: "ACC-33 — Kueue Preemption"
aliases:
  - "ACC-33"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Kueue Preemption situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-33_kueue_preemption.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-33 — Kueue Preemption

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-33` |
| Category | Execution/Reliability |
| Severity | **High** |
| Accountable owner | Compute Platform Lead |
| Independent witness / verifier | SRE / Assurance |
| Related packages | `WP-052`, `WP-053`, `WP-083`, `WP-111` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Kueue Preemption** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A low-priority scout workload is consuming resources while a critical reproduction queue requests capacity.

**When:** The Kueue priority and preemption policy runs.

**Then:** The scout is checkpointed, paused or evicted and the critical reproduction is admitted; canonical task state and artifacts are not lost and the scout resumes later.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Start a low-priority, checkpoint-capable scout | Execution log + trace/event references |
| 2 | Create queue and resource saturation | Execution log + trace/event references |
| 3 | Submit the critical reproduction workload | Execution log + trace/event references |
| 4 | Observe the preemption, lease, budget and checkpoint events | Execution log + trace/event references |
| 5 | Complete the reproduction | Execution log + trace/event references |
| 6 | Re-admit and resume the scout, then compare state | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The critical reproduction's wait time is within SLO
- [ ] Scout state and artifacts are preserved
- [ ] No duplicated scout work effect occurs
- [ ] Budget reservations are correct
- [ ] The priority rule and audit record are visible
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `WorkloadRecords`
- `CheckpointArtifact`
- `KueueAdmission`
- `ExecutionLeases`
- `CostReservations`

## Expected events

- `workload.preempted`
- `checkpoint.captured`
- `reproduction.admitted`
- `workload.resumed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-33-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-33-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-33-state-before.json` and `ACC-33-state-after.json`.
- `ACC-33-events.json`, `ACC-33-policy-decisions.json` and `ACC-33-audit-export.json`.
- `ACC-33-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Fixture workloads complete or are cancelled; queue quotas return to baseline.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
