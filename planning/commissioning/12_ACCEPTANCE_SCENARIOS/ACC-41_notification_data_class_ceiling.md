# ACC-41 — Outbound Notification Exceeds the Channel Data-Class Ceiling

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-41` |
| Category | Communication/Security |
| Severity | **Critical** |
| Accountable owner | Platform Security Lead |
| Independent witness / verifier | Safety & Governance Owner |
| Related packages | `WP-131`, `WP-132`, `WP-133` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

An agent must never hold channel credentials, and a notification must never carry content above the
channel's data-class ceiling. This scenario verifies that the broker enforces both, and that an attempt to
exceed the ceiling degrades to a reference rather than leaking the payload.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A `NotificationIntent` whose payload contains D2 content and a channel whose registry entry declares a D1 ceiling.

**When:** The Notification Broker resolves the intent against the channel registry.

**Then:** The payload is refused or degraded to a signed reference with no D2 content; the agent never touches the channel credential; the decision and its rule are audited.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Emit a `NotificationIntent` at D1 and confirm normal delivery | Delivery record + audit entry |
| 2 | Emit the same intent carrying D2 content | Policy decision record |
| 3 | Assert what actually left the boundary | Egress capture |
| 4 | Attempt to send directly from the agent, bypassing the broker | Refusal record |
| 5 | Re-send the same intent twice and assert idempotency | Delivery ledger |

## Mandatory invariants and assertions

- [ ] Content above the channel ceiling never leaves the boundary
- [ ] Degradation to a reference is recorded, not silent
- [ ] The agent holds no channel credential at any point
- [ ] A direct agent-to-channel send is refused
- [ ] Duplicate intents produce one delivery
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `NotificationIntent`
- `ChannelRegistryEntry`
- `PolicyDecision`
- `DeliveryRecord`
- `AuditRecord`

## Expected events

- `notification.intent.created`
- `notification.degraded`
- `policy.denied`
- `notification.delivered`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-41-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-41-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-41-state-before.json` and `ACC-41-state-after.json`.
- `ACC-41-events.json`, `ACC-41-policy-decisions.json` and `ACC-41-audit-export.json`.
- `ACC-41-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test channels are disabled; delivery, refusal and audit records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
