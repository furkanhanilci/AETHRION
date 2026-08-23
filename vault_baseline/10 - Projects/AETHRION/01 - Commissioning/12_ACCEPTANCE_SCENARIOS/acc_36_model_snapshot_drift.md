---
title: "ACC-36 — Model Snapshot Drift"
aliases:
  - "ACC-36"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Model Snapshot Drift situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-36_model_snapshot_drift.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-36 — Model Snapshot Drift

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-36` |
| Category | Model/Monitoring |
| Severity | **Critical** |
| Accountable owner | Eval Office |
| Independent witness / verifier | Model Platform Lead / Safety |
| Related packages | `WP-037`, `WP-042`, `WP-044`, `WP-106`, `WP-108`, `WP-137` |
| Acceptance phase | `PRE_GO_LIVE` — initial qualification |
| Recurring counterpart | `WP-124` · WP-124 runs the recurring requalification of the same measure in Day-2 |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Model Snapshot Drift** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The provider alias looks unchanged, but the fingerprint, evaluation behaviour or dated snapshot has changed; the profile is in use on open tasks.

**When:** The model monitor and qualification check detect the drift.

**Then:** The profile moves to suspension or requalification, the router cache is invalidated and an `ImpactScan` opens for open tasks, runs and claims; there is no unsafe fallback.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed the admitted profile, its fingerprint and the open tasks | Execution log + trace/event references |
| 2 | Inject the changed provider response and fingerprint | Execution log + trace/event references |
| 3 | Run the drift detector and regression evaluation | Execution log + trace/event references |
| 4 | Observe the profile lifecycle and route cache behaviour | Execution log + trace/event references |
| 5 | Verify the `ImpactScan` affected set | Execution log + trace/event references |
| 6 | Issue a requalification or disable disposition | Execution log + trace/event references |
| 7 | Force a silent provider failover and confirm it appears in the fingerprint rather than in nothing | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The profile is not eligible until requalified
- [ ] New calls do not reach the old profile
- [ ] Open-task impact recall is 100% on the fixture
- [ ] Historical runs are unchanged
- [ ] With no eligible route the work is `BLOCKED`
- [ ] Snapshot drift is detected from the **`ModelExecutionFingerprint`**, which records the provider, snapshot, API version and any retry or fallback — ACC-115.
- [ ] A silent failover to a different provider mid-run is drift, and it invalidates any `EXACT` reproduction claim.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

The original scenario watched for an announced snapshot change. The fingerprint catches the unannounced one, which is the case that actually damages a result — WP-157.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `CapabilityProfileVersions`
- `DriftReport`
- `RouteDecisions`
- `ImpactCases`
- `AdmissionDecision`

## Expected events

- `model.drift_detected`
- `capability.suspended`
- `router.cache_invalidated`
- `impact.scan.started`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-36-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-36-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-36-state-before.json` and `ACC-36-state-after.json`.
- `ACC-36-events.json`, `ACC-36-policy-decisions.json` and `ACC-36-audit-export.json`.
- `ACC-36-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The provider fault fixture is removed; the profile returns only through an explicit requalification decision.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
