---
title: "ACC-087 — Communication Optimisation Rollback"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Communication Optimisation Rollback situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-087_communication_optimization_rollback.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-087 — Communication Optimisation Rollback

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-087` |
| Category | Collaboration/Efficiency |
| Severity | **High** |
| Accountable owner | Chief Architect |
| Independent witness / verifier | Assurance Lead |
| Related packages | `WP-150` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Communication Optimisation Rollback** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A topology optimisation is active and the quality guard is armed with a declared tolerance.

**When:** A pruning decision causes a quality regression beyond that tolerance.

**Then:** The topology rolls back automatically, without human intervention, and the regression and the rollback are both recorded. The campaign continues under the previous topology rather than stopping.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Arm the quality guard with a declared tolerance | Execution log + trace/event references |
| 2 | Apply a pruning decision engineered to remove a load-bearing edge | Execution log + trace/event references |
| 3 | Observe the quality measurement cross the tolerance | Execution log + trace/event references |
| 4 | Confirm the rollback occurs without human intervention | Execution log + trace/event references |
| 5 | Confirm the campaign continues under the previous topology | Execution log + trace/event references |
| 6 | Read the rollback record and the retained regression measurement | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The regression is detected against the declared tolerance, not a post-hoc one
- [ ] Rollback is automatic and recorded
- [ ] The campaign continues rather than failing
- [ ] The regression measurement is retained, not discarded on rollback
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `CommunicationGraph`
- `CommunicationUtilityRecord`
- `MetascienceReport`

## Expected events

- `topology.rolled_back`
- `metascience.quality_regression_detected`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-087-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-087-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-087-state-before.json` and `ACC-087-state-after.json`.
- `ACC-087-events.json`, `ACC-087-policy-decisions.json` and `ACC-087-audit-export.json`.
- `ACC-087-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The campaign is marked `TEST_CLOSED`; both topologies and the regression record are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
