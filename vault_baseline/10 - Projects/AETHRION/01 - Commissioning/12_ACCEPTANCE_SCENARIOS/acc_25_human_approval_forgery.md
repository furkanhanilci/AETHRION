---
title: "ACC-25 — Human Approval Forgery"
aliases:
  - "ACC-25"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Human Approval Forgery situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-25_human_approval_forgery.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-25 — Human Approval Forgery

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-25` |
| Category | Security/Governance |
| Severity | **Critical** |
| Accountable owner | Governance Lead |
| Independent witness / verifier | Security / Internal Audit |
| Related packages | `WP-004`, `WP-038`, `WP-055`, `WP-060`, `WP-093`, `WP-102`, `WP-106`, `WP-112`, `WP-135` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Human Approval Forgery** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A G8/G9 decision request exists; an attacker attempts to submit an approval with a missing or invalid OIDC-MFA context, or by replaying a payload.

**When:** The Temporal Human Update API receives forged, expired and duplicate requests.

**Then:** The decision is rejected; gate state does not change and a security event and audit record are produced. A valid owner with MFA and an idempotent request passes as the counter-example.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the decision request and the evidence snapshot | Execution log + trace/event references |
| 2 | Try a missing token, an invalid signature, a wrong subject and an expired MFA context | Execution log + trace/event references |
| 3 | Capture and replay a valid request | Execution log + trace/event references |
| 4 | Check the gate, history and `DecisionRecord` | Execution log + trace/event references |
| 5 | Send a valid decision after re-authenticating as the correct owner | Execution log + trace/event references |
| 6 | Verify the security alert and incident threshold | Execution log + trace/event references |
| 7 | Attempt the forgery against the preliminary assessment and against the final decision separately | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Forged decisions = 0
- [ ] The gate is unchanged
- [ ] A replay produces exactly one decision
- [ ] A valid actor, role and evidence snapshot are required
- [ ] The audit trail contains every attempt
- [ ] A forged approval must also fail to produce a **`HumanPreliminaryAssessment`**, which is sealed before any recommendation is reachable — ACC-110.
- [ ] No timeout, learned preference or attention score creates an approval, through any interface — ACC-069.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

Baseline v1.3.0 splits a G8 decision into two sealed records. A forgery that produces one without the other is detectable in a way a single record could not be — `ADR-016`.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `DecisionRequest`
- `PolicyDecision`
- `SecurityEvent`
- `DecisionRecord(valid)`
- `TemporalHistory`

## Expected events

- `approval.forgery_detected`
- `decision.denied`
- `security.event`
- `decision.recorded`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-25-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-25-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-25-state-before.json` and `ACC-25-state-after.json`.
- `ACC-25-events.json`, `ACC-25-policy-decisions.json` and `ACC-25-audit-export.json`.
- `ACC-25-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test tokens are revoked; the synthetic decision and project are archived as `TEST_CLOSED`.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
