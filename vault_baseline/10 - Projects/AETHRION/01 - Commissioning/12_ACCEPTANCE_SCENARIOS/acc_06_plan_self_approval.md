---
title: "ACC-06 — Planner Self-Approval Attempt"
aliases:
  - "ACC-06"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Planner Self-Approval Attempt situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-06_plan_self_approval.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-06 — Planner Self-Approval Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-06` |
| Category | Governance/Assurance |
| Severity | **Critical** |
| Accountable owner | Assurance Lead |
| Independent witness / verifier | Internal Audit |
| Related packages | `WP-000`, `WP-003`, `WP-007`, `WP-056`, `WP-060`, `WP-086`, `WP-088`, `WP-102`, `WP-105`, `WP-107`, `WP-147` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Planner Self-Approval Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The actor or model profile that produced a plan is offered as a reviewer or approver assignment candidate for the same artifact.

**When:** The assignment service performs the `IndependenceProfile` eligibility check.

**Then:** The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Record the producer identity, model, context and credential fields | Execution log + trace/event references |
| 2 | Assign the same actor as reviewer | Execution log + trace/event references |
| 3 | Try the variant with the same human, a different model, but a contaminated context | Execution log + trace/event references |
| 4 | Compare the R1 and R3 policy outcomes | Execution log + trace/event references |
| 5 | Assign a suitable independent reviewer and continue the flow | Execution log + trace/event references |
| 6 | Attempt the self-approval as a cohort member and as a scientific council session, not only as a planner | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Self-assignment is denied
- [ ] Context contamination is non-compliant
- [ ] R3 enforces the required human and model separation
- [ ] A denied attempt never turns the gate into `PASS`
- [ ] The audit record carries the rule, bundle and input
- [ ] A **cohort member** cannot approve its own gate either, through any interface including the event plane — ACC-093.
- [ ] A council or cohort that contributed to the design cannot be bound as reviewer of the same artefact where the independence profile forbids it — ACC-072.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

Baseline v1.3.0 adds cognitive actors that did not exist when this scenario was written. Each is a new surface for the same attempt, and none of them holds authority — `ADR-011`, `ADR-014`.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `IndependenceProfile`
- `AssignmentDecision`
- `PolicyDecision`
- `GateRecord`
- `AuditRecord`

## Expected events

- `review.assignment.denied`
- `independence.violated`
- `workflow.blocked`
- `review.assignment.created`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-06-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-06-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-06-state-before.json` and `ACC-06-state-after.json`.
- `ACC-06-events.json`, `ACC-06-policy-decisions.json` and `ACC-06-audit-export.json`.
- `ACC-06-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test assignments are cancelled; denial and audit records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
