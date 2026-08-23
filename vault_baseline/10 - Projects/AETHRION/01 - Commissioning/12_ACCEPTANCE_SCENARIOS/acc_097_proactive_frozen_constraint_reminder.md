---
title: "ACC-097 — Proactive Reminder of a Frozen Constraint"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Proactive Reminder of a Frozen Constraint situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-097_proactive_frozen_constraint_reminder.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-097 — Proactive Reminder of a Frozen Constraint

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-097` |
| Category | Knowledge/Assurance |
| Severity | **High** |
| Accountable owner | Knowledge Lead |
| Independent witness / verifier | Methodologist |
| Related packages | `WP-151` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Proactive Reminder of a Frozen Constraint** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** An analysis plan is frozen with an explicit stopping rule, and an agent is about to take a step that would violate it.

**When:** The memory subsystem evaluates whether a reminder is material.

**Then:** A reminder is emitted carrying canonical artifact references. It creates no claim and asserts nothing new. On an ordinary step with no material constraint at stake, no reminder is emitted.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Freeze an analysis plan with an explicit stopping rule | Execution log + trace/event references |
| 2 | Drive an agent towards a step that would violate it | Execution log + trace/event references |
| 3 | Read the reminder and the artifact references it carries | Execution log + trace/event references |
| 4 | Confirm the reminder introduced no new assertion | Execution log + trace/event references |
| 5 | Run an ordinary step with no constraint at stake | Execution log + trace/event references |
| 6 | Confirm no reminder is emitted on that step | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The reminder fires on the material step and carries canonical artifact references
- [ ] The reminder creates no `ClaimVersion` and no new assertion
- [ ] No reminder fires on the ordinary step — the mechanism is selective, not per-turn
- [ ] The referenced artifacts resolve
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `MemoryInterventionRecord`
- `AnalysisPlanManifest`
- `ContextProjectionRecord`

## Expected events

- `memory.reminder`
- `memory.projection_assembled`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-097-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-097-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-097-state-before.json` and `ACC-097-state-after.json`.
- `ACC-097-events.json`, `ACC-097-policy-decisions.json` and `ACC-097-audit-export.json`.
- `ACC-097-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test interventions are marked `TEST_CLOSED`; the frozen plan and the intervention records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
