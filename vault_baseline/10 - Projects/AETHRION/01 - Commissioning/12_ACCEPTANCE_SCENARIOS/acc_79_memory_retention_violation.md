---
title: "ACC-79 — Epistemic Memory Retention Violation"
aliases:
  - "ACC-79"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Epistemic Memory Retention Violation situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-79_memory_retention_violation.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-79 — Epistemic Memory Retention Violation

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-79` |
| Category | Data/Knowledge |
| Severity | **High** |
| Accountable owner | Knowledge Lead |
| Independent witness / verifier | Archivist / Internal Audit |
| Related packages | `WP-026`, `WP-146` |
| Acceptance phase | `PRE_GO_LIVE` |
| Recurring counterpart | `WP-125` · WP-125 runs the recurring memory and source curation cycle in Day-2 |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Epistemic Memory Retention Violation** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A procedural-memory decay job is configured against a record set that deliberately mixes procedural entries with evidence artifacts and human intervention records.

**When:** The job runs.

**Then:** It excludes the immutable classes, reports exactly what it excluded and why, and expires only procedural entries. A planted evidence control survives, and a planted stale procedure does not.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed procedural entries, evidence artifacts and human intervention records together | Execution log + trace/event references |
| 2 | Plant an evidence control that must survive and a stale procedure that must expire | Execution log + trace/event references |
| 3 | Run the decay job | Execution log + trace/event references |
| 4 | Read the exclusion report | Execution log + trace/event references |
| 5 | Verify each planted control's state | Execution log + trace/event references |
| 6 | Attempt to reach evidence through the procedural-memory API | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The planted evidence control survives with an unchanged digest
- [ ] Every human intervention record survives
- [ ] The stale procedure is expired, so the job is not simply inert
- [ ] The exclusion report names the immutable classes it refused to touch
- [ ] The procedural-memory API cannot reach the evidence store
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `MethodExperience`
- `ArtifactRecord`
- `HumanInterventionRecord`
- `RetentionReport`

## Expected events

- `memory.decay_completed`
- `memory.retention_exclusion_reported`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-79-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-79-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-79-state-before.json` and `ACC-79-state-after.json`.
- `ACC-79-events.json`, `ACC-79-policy-decisions.json` and `ACC-79-audit-export.json`.
- `ACC-79-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test memory records are marked `TEST_CLOSED`; evidence and audit records are retained permanently.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
