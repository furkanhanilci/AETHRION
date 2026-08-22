---
title: "ACC-24 — Policy Bundle Rollback"
aliases:
  - "ACC-24"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Policy Bundle Rollback situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-24_policy_bundle_rollback.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-24 — Policy Bundle Rollback

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-24` |
| Category | Security/Governance |
| Severity | **High** |
| Accountable owner | Policy Platform Lead |
| Independent witness / verifier | Safety / Internal Audit |
| Related packages | `WP-009`, `WP-056`, `WP-112` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Policy Bundle Rollback** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A newly signed policy bundle wrongly blocks a valid workload; the previously signed bundle is known.

**When:** The canary/shadow difference and a production denial alert trigger the rollback procedure.

**Then:** The previous bundle is restored atomically, decision logs and bundle digests are preserved, open tasks are re-evaluated and no unsafe temporary allow is granted.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the old and new signed bundles and the golden decisions | Execution log + trace/event references |
| 2 | Run the new bundle in canary/shadow and diff the decisions | Execution log + trace/event references |
| 3 | Promote in a controlled way and produce the expected false denial | Execution log + trace/event references |
| 4 | Apply the rollback authorisation and procedure | Execution log + trace/event references |
| 5 | Check `PolicyDecision` history and cache convergence | Execution log + trace/event references |
| 6 | Re-evaluate the affected tasks | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The rollback target's signature is valid
- [ ] All enforcement points converge on the restored bundle
- [ ] Both old and new decisions are retained
- [ ] No manual permanent bypass is created
- [ ] Open tasks undergo safe re-evaluation
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `PolicyBundles`
- `Promotion/RollbackDecision`
- `PolicyDecisionLogs`
- `ImpactScanResult`

## Expected events

- `policy.bundle.promoted`
- `policy.regression_detected`
- `policy.bundle.rolled_back`
- `task.re_evaluated`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-24-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-24-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-24-state-before.json` and `ACC-24-state-after.json`.
- `ACC-24-events.json`, `ACC-24-policy-decisions.json` and `ACC-24-audit-export.json`.
- `ACC-24-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test bundle is disabled and revoked; the false-denial finding enters the correction backlog.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
