---
title: "ACC-10 — Primary Model Provider Outage"
aliases:
  - "ACC-10"
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Primary Model Provider Outage situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-10_provider_outage.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-10 — Primary Model Provider Outage

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-10` |
| Category | Reliability/Model |
| Severity | **High** |
| Accountable owner | Model Platform Lead |
| Independent witness / verifier | SRE / Eval Office |
| Related packages | `WP-040`, `WP-041`, `WP-044`, `WP-045`, `WP-111` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Primary Model Provider Outage** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The primary profile is failing and an admitted fallback exists for the same role, data class, tools and risk class.

**When:** The gateway circuit breaker opens and the router re-selects.

**Then:** Only an admitted fallback is chosen; route, family and independence are recomputed, SLO and cost records are written, and the task is not duplicated.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Inject 5xx/timeout faults at the primary provider | Execution log + trace/event references |
| 2 | Drive the circuit breaker to its threshold | Execution log + trace/event references |
| 3 | Obtain a fallback route for the same `TaskContract` | Execution log + trace/event references |
| 4 | Recompute reviewer independence where required | Execution log + trace/event references |
| 5 | Verify `AgentResult` and cost/trace correlation | Execution log + trace/event references |
| 6 | Attempt half-open recovery of the primary | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Fallback eligibility is fully satisfied
- [ ] There is exactly one task result
- [ ] No unsafe provider route is taken
- [ ] The `RouteDecision` carries its rationale and profile references
- [ ] The outage alert and SLO impact are measured
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `RouteDecision`
- `CapabilityProfileRefs`
- `ModelCallRecords`
- `TaskResult`
- `Incident/SLORecord`

## Expected events

- `model.provider.degraded`
- `route.fallback_selected`
- `task.completed`
- `provider.recovered`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-10-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-10-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-10-state-before.json` and `ACC-10-state-after.json`.
- `ACC-10-events.json`, `ACC-10-policy-decisions.json` and `ACC-10-audit-export.json`.
- `ACC-10-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The fault is removed; the circuit breaker is reset in a controlled way and synthetic health is verified.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
