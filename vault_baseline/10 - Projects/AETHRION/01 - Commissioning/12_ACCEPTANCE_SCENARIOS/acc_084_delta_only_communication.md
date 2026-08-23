---
title: "ACC-084 — Delta-Only Communication"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Delta-Only Communication situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-084_delta_only_communication.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-084 — Delta-Only Communication

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-084` |
| Category | Collaboration/Efficiency |
| Severity | **High** |
| Accountable owner | Chief Architect |
| Independent witness / verifier | FinOps Lead |
| Related packages | `WP-149`, `WP-150` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Delta-Only Communication** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** An agent has produced a large reasoning output and wishes to share its conclusion.

**When:** It emits a message carrying the full transcript.

**Then:** The message is rejected in favour of a delta plus an artifact pointer. The full content is written to the artifact store and the message carries its digest.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Emit a message carrying a full reasoning transcript | Execution log + trace/event references |
| 2 | Read the rejection and the size threshold it names | Execution log + trace/event references |
| 3 | Re-emit as a delta with an artifact pointer | Execution log + trace/event references |
| 4 | Resolve the pointer and confirm the full content is retrievable | Execution log + trace/event references |
| 5 | Compare inter-agent token counts before and after | Execution log + trace/event references |
| 6 | Confirm the receiving agent can act on the delta alone | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The full-transcript message is rejected
- [ ] The delta plus pointer is accepted and the pointer resolves to the complete content
- [ ] Inter-agent token spend falls measurably between the two forms
- [ ] No content is lost — the artifact store holds what the message did not
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `TypedAgentMessage`
- `ArtifactRecord`
- `TokenLedgerEntry`

## Expected events

- `message.routed`
- `artifact.created`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-084-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-084-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-084-state-before.json` and `ACC-084-state-after.json`.
- `ACC-084-events.json`, `ACC-084-policy-decisions.json` and `ACC-084-audit-export.json`.
- `ACC-084-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test messages are marked `TEST_CLOSED`; the referenced artifacts are retained under test retention.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
