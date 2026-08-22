---
title: "ACC-50 — Procedure Lost to Context Compaction or Restart"
aliases:
  - "ACC-50"
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Procedure Lost to Context Compaction or Restart situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-50_skill_lost_on_compaction.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-50 — Procedure Lost to Context Compaction or Restart

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-50` |
| Category | Agent/Skill Governance |
| Severity | **High** |
| Accountable owner | Control Plane Lead |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-046`, `WP-048` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Procedure Lost to Context Compaction or Restart** situation.

A long-running task outlives its context window. If the loaded procedure
silently disappears at compaction, governance ends mid-run while the run
continues to look healthy — the most deniable failure in the whole layer.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A long-running task with a loaded skill bundle, driven past its context limit and through a session restart.

**When:** Compaction occurs and the session is resumed.

**Then:** The procedure is restored or the task halts; it never continues silently without it, and the recovery is visible in the audit trail.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Start a long-running task and record `skill_bundle_hash` | Task record |
| 2 | Drive the session past its context limit | Execution log |
| 3 | Assert the loaded skill set after compaction | Loaded-skill listing |
| 4 | Kill and resume the session | Recovery transcript |
| 5 | Confirm the resumed run carries the same bundle hash, or halted | Task record + audit export |

## Mandatory invariants and assertions

- [ ] The loaded skill set survives compaction, or the task halts
- [ ] `skill_bundle_hash` after recovery equals the hash before it
- [ ] A silent continuation without the procedure is impossible
- [ ] The recovery or halt is visible in the audit trail
- [ ] Behaviour is identical across supported harnesses
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `TaskContract`
- `HarnessSession`
- `RecoveryRecord`
- `AuditRecord`

## Expected events

- `session.compacted`
- `skill.bundle.restored`
- `task.halted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-50-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-50-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-50-state-before.json` and `ACC-50-state-after.json`.
- `ACC-50-events.json`, `ACC-50-policy-decisions.json` and `ACC-50-audit-export.json`.
- `ACC-50-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test sessions are closed; recovery and audit records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
