---
title: "ACC-34 — DLQ Repair and Corrected Replay"
aliases:
  - "ACC-34"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the DLQ Repair and Corrected Replay situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-34_dlq_repair.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-34 — DLQ Repair and Corrected Replay

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-34` |
| Category | Event/Reliability |
| Severity | **High** |
| Accountable owner | Event Platform Lead |
| Independent witness / verifier | SRE / Schema Owner |
| Related packages | `WP-015`, `WP-028`, `WP-039`, `WP-111` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **DLQ Repair and Corrected Replay** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** An incompatible or poison payload exists for a consumer.

**When:** Consumer validation fails, the event moves to the DLQ, and the repair workflow replays it through a corrective adapter or schema.

**Then:** No consumer loop forms; owner, diagnostics and audit are complete, the corrected event is processed exactly once and the original causation is preserved.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Publish the poison event fixture | Execution log + trace/event references |
| 2 | Observe validation, the retry threshold and the DLQ transfer | Execution log + trace/event references |
| 3 | Check the DLQ case, owner and diagnostics | Execution log + trace/event references |
| 4 | Produce the schema adapter or the corrected payload | Execution log + trace/event references |
| 5 | Run a dry run, then the corrected replay | Execution log + trace/event references |
| 6 | Verify business effect, idempotency, offset and audit records | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Business effects from the original event = 0
- [ ] One DLQ record and no loop
- [ ] Corrected effect count = 1
- [ ] Causation and the original reference are retained
- [ ] The queue drains
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `DLQRecord`
- `RepairCase`
- `CorrectedEvent`
- `ConsumerIdempotencyRecord`
- `AuditRecord`

## Expected events

- `event.rejected`
- `event.dlq_entered`
- `event.repaired`
- `event.replayed`
- `consumer.effect_committed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-34-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-34-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-34-state-before.json` and `ACC-34-state-after.json`.
- `ACC-34-events.json`, `ACC-34-policy-decisions.json` and `ACC-34-audit-export.json`.
- `ACC-34-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test DLQ case is `CLOSED`; the fixture subject and consumer are cleaned up and evidence is retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
