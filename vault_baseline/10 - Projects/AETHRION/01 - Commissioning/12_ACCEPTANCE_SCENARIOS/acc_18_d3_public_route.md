---
title: "ACC-18 — D3 Data to a Public Provider"
aliases:
  - "ACC-18"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the D3 Data to a Public Provider situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-18_d3_public_route.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-18 — D3 Data to a Public Provider

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-18` |
| Category | Security/Privacy |
| Severity | **Critical** |
| Accountable owner | Safety & Governance Owner |
| Independent witness / verifier | Privacy Reviewer |
| Related packages | `WP-006`, `WP-021`, `WP-041`, `WP-045`, `WP-056`, `WP-057`, `WP-060`, `WP-112` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **D3 Data to a Public Provider** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A `TaskContract` contains D3 restricted data and a public external model profile is requested.

**When:** The router, OPA and gateway make the routing decision.

**Then:** No public provider call is made; a secure or local eligible route is chosen if one exists, otherwise the task is `BLOCKED`, and an audit record is written.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create the D3 synthetic data and `TaskContract` | Execution log + trace/event references |
| 2 | Request the public provider explicitly | Execution log + trace/event references |
| 3 | Run the OPA and router candidate filter | Execution log + trace/event references |
| 4 | Try both the secure-route-available and unavailable variants | Execution log + trace/event references |
| 5 | Query the gateway provider call logs | Execution log + trace/event references |
| 6 | Check the decision and explanation UI | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Public provider calls = 0
- [ ] The policy denial carries the D3 rule and bundle
- [ ] A secure route is used only if it is admitted
- [ ] With no route available the task is `BLOCKED`
- [ ] No sensitive raw data appears in traces or events
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `TaskContract`
- `PolicyDecision`
- `RouteDecision`
- `GatewayAudit`
- `WorkflowState`

## Expected events

- `data.route.denied`
- `route.secure_selected_or_blocked`
- `workflow.blocked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-18-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-18-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-18-state-before.json` and `ACC-18-state-after.json`.
- `ACC-18-events.json`, `ACC-18-policy-decisions.json` and `ACC-18-audit-export.json`.
- `ACC-18-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Synthetic D3 data is removed under the secure deletion policy; audit and evidence are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
