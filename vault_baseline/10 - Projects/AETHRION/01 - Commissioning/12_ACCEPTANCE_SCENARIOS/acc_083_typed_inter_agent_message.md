---
title: "ACC-083 — Typed Inter-Agent Message"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Typed Inter-Agent Message situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-083_typed_inter_agent_message.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-083 — Typed Inter-Agent Message

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-083` |
| Category | Collaboration/Contracts |
| Severity | **High** |
| Accountable owner | Chief Architect |
| Independent witness / verifier | Platform Assurance Lead |
| Related packages | `WP-015`, `WP-149` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Typed Inter-Agent Message** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The collaboration plane is running and the ten message types are registered.

**When:** An agent emits a free-text message with no type, and separately a message whose declared type does not match its content.

**Then:** Both are rejected at the contract boundary. A correctly typed message passes, and its type is what makes a `CHALLENGE` trackable to resolution.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Emit a message with no declared type | Execution log + trace/event references |
| 2 | Emit a message declaring `STATUS` while carrying a challenge | Execution log + trace/event references |
| 3 | Emit a correctly typed `CHALLENGE` | Execution log + trace/event references |
| 4 | Track that challenge to resolution through the convergence rule | Execution log + trace/event references |
| 5 | Attempt to close convergence with the challenge still open | Execution log + trace/event references |
| 6 | Read the message-type distribution for the round | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The untyped message is rejected
- [ ] The mistyped message is rejected or normalised only through the authorised path, and audited
- [ ] The correctly typed challenge is tracked and appears in the convergence assessment
- [ ] Convergence cannot close while the challenge is open
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `TypedAgentMessage`
- `BlackboardEntry`
- `MaterialChallenge`
- `ConvergenceAssessment`

## Expected events

- `message.routed`
- `material.challenge.opened`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-083-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-083-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-083-state-before.json` and `ACC-083-state-after.json`.
- `ACC-083-events.json`, `ACC-083-policy-decisions.json` and `ACC-083-audit-export.json`.
- `ACC-083-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test messages are marked `TEST_CLOSED`; the challenge and its resolution record are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
