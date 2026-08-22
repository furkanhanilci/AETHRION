---
title: "ACC-42 — Notification Broker Unavailable During an Escalating Condition"
aliases:
  - "ACC-42"
type: acceptance-scenario
category: commissioning
summary: "A laboratory that cannot reach a human must not conclude that no human was needed."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-42_notification_broker_outage.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-42 — Notification Broker Unavailable During an Escalating Condition

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-42` |
| Category | Communication/Reliability |
| Severity | **High** |
| Accountable owner | Platform Operations Lead |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-131`, `WP-140` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

A laboratory that cannot reach a human must not conclude that no human was needed. This scenario removes
the outbound path during a condition that requires attention and verifies that the condition is preserved and
re-raised rather than lost.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A condition that requires human attention, and a Notification Broker that is unavailable.

**When:** The condition is raised and the delivery attempt fails.

**Then:** The intent is queued and retried, the affected workflow does not proceed as though notification had succeeded, and the liveness signal reports the degraded path.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Raise the condition with the broker healthy and record the baseline | Delivery record |
| 2 | Disable the broker and raise the condition again | Failure record |
| 3 | Assert the workflow state after the failed delivery | Workflow state snapshot |
| 4 | Restore the broker and assert re-delivery | Delivery ledger |
| 5 | Assert the liveness signal reported the degradation | Liveness record |

## Mandatory invariants and assertions

- [ ] A failed notification never advances the workflow
- [ ] The intent survives the outage and is re-delivered exactly once
- [ ] The degraded path is visible in the liveness signal
- [ ] No silent drop occurs at any queue boundary
- [ ] Retry is bounded and does not amplify
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `NotificationIntent`
- `DeliveryRecord`
- `LivenessRecord`
- `AuditRecord`

## Expected events

- `notification.delivery.failed`
- `notification.requeued`
- `liveness.degraded`
- `notification.delivered`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-42-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-42-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-42-state-before.json` and `ACC-42-state-after.json`.
- `ACC-42-events.json`, `ACC-42-policy-decisions.json` and `ACC-42-audit-export.json`.
- `ACC-42-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The broker is restored; queued test intents are drained and their records retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
