---
title: "ACC-102 — Deterministic Tool-Result Reuse"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Deterministic Tool-Result Reuse situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-102_tool_result_reuse.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-102 — Deterministic Tool-Result Reuse

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-102` |
| Category | FinOps/Efficiency |
| Severity | **Medium** |
| Accountable owner | FinOps Lead |
| Independent witness / verifier | Platform Assurance Lead |
| Related packages | `WP-049`, `WP-153` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Medium scenario may be deferred with a named owner and an expiry date |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Deterministic Tool-Result Reuse** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A deterministic tool is called twice within one campaign with identical inputs, and a third call crosses a freshness boundary the protocol declares.

**When:** All three calls are made.

**Then:** The second is served from the recorded result and marked as reused. The third re-executes because the freshness boundary forbids reuse. A reused result is distinguishable from a fresh one in the record.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Call a deterministic tool and record the result | Execution log + trace/event references |
| 2 | Repeat with identical inputs inside the freshness window | Execution log + trace/event references |
| 3 | Confirm the second is served from the record and marked reused | Execution log + trace/event references |
| 4 | Cross the declared freshness boundary and call again | Execution log + trace/event references |
| 5 | Confirm the third re-executes | Execution log + trace/event references |
| 6 | Confirm a non-deterministic tool is never reused | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The identical in-window call is reused and marked as reused
- [ ] The call crossing the freshness boundary re-executes
- [ ] A non-deterministic tool is never served from a record
- [ ] A reused result is distinguishable from a fresh one in the run record
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ToolInvocationRecord`
- `TokenLedgerEntry`
- `ArtifactRecord`

## Expected events

- `tool.result_reused`
- `tool.invoked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-102-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-102-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-102-state-before.json` and `ACC-102-state-after.json`.
- `ACC-102-events.json`, `ACC-102-policy-decisions.json` and `ACC-102-audit-export.json`.
- `ACC-102-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test tool records are marked `TEST_CLOSED`; the reuse cache is cleared.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
