---
title: "ACC-26 — Approval, Delegation and Exception Expiry"
aliases:
  - "ACC-26"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Approval, Delegation and Exception Expiry situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-26_approval_expiry.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-26 — Approval, Delegation and Exception Expiry

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-26` |
| Category | Governance |
| Severity | **Critical** |
| Accountable owner | Safety & Governance Owner |
| Independent witness / verifier | Internal Audit |
| Related packages | `WP-004`, `WP-009`, `WP-038`, `WP-055`, `WP-056`, `WP-059`, `WP-093`, `WP-102`, `WP-112`, `WP-134`, `WP-135` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Approval, Delegation and Exception Expiry** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A time-bound delegation, control exception or approval is in use by an open or running task.

**When:** The expiry time arrives and the scheduled policy re-evaluation runs.

**Then:** The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create a record with a short expiry and a scoped task | Execution log + trace/event references |
| 2 | Run a permitted operation before expiry | Execution log + trace/event references |
| 3 | Trigger expiry via the clock or schedule | Execution log + trace/event references |
| 4 | Observe the behaviour of new and running operations | Execution log + trace/event references |
| 5 | Check escalation, the owner queue and the audit trail | Execution log + trace/event references |
| 6 | Attempt a replay with the expired token | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The record is `EXPIRED`/`REVOKED`
- [ ] New actions are denied
- [ ] The running task is re-evaluated
- [ ] There is no auto-extension
- [ ] Owner, escalation and audit records are complete
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `Delegation/ExceptionRecord`
- `PolicyDecisions`
- `WorkflowState`
- `Revocation/AuditRecord`

## Expected events

- `authorization.expired`
- `credential_or_exception.revoked`
- `task.re_evaluated`
- `workflow.paused`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-26-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-26-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-26-state-before.json` and `ACC-26-state-after.json`.
- `ACC-26-events.json`, `ACC-26-policy-decisions.json` and `ACC-26-audit-export.json`.
- `ACC-26-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test scope is cleared; record history is retained and the task closes by controlled cancellation.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
