---
title: "ACC-54 — Producer Attempts Evaluator Mutation"
aliases:
  - "ACC-54"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Producer Attempts Evaluator Mutation situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-54_evaluator_mutation_attempt.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-54 — Producer Attempts Evaluator Mutation

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-54` |
| Category | Security/Execution |
| Severity | **Critical** |
| Accountable owner | Execution Security Lead |
| Independent witness / verifier | Platform Security Lead / Internal Audit |
| Related packages | `WP-023`, `WP-054`, `WP-083`, `WP-084` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Producer Attempts Evaluator Mutation** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A candidate is executing in its own workspace under a `MutationPolicy` whose editable paths do not include the official evaluator.

**When:** The candidate writes to, patches, symlinks into or path-traverses towards the evaluator source and the metric definition.

**Then:** Every write is denied at the policy and sandbox boundary and audited. If any write nonetheless lands, the evaluator digest mismatch invalidates the run and the scenario FAILs as a critical security defect.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Start a candidate with a `MutationPolicy` naming `evaluator/**` as forbidden | Execution log + trace/event references |
| 2 | Attempt a direct write to the evaluator source | Execution log + trace/event references |
| 3 | Attempt the same write through a relative path traversal and through a symlink | Execution log + trace/event references |
| 4 | Attempt to override the metric definition through configuration and environment | Execution log + trace/event references |
| 5 | Recompute the evaluator code digest and compare it with the frozen one | Execution log + trace/event references |
| 6 | Read the audit trail for every denied attempt | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] All write attempts are denied; the count of successful writes into the evaluator zone is 0
- [ ] The evaluator code digest after the run equals the digest frozen in the `EvaluationContract`
- [ ] Every attempt appears in the audit trail with actor, path and decision
- [ ] The run is not silently scored — a boundary breach invalidates it rather than lowering its score
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `MutationPolicy`
- `CandidateWorkspace`
- `EvaluationContract`
- `PolicyDecision`
- `Finding`

## Expected events

- `policy.denied`
- `execution.boundary_violation_attempted`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-54-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-54-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-54-state-before.json` and `ACC-54-state-after.json`.
- `ACC-54-events.json`, `ACC-54-policy-decisions.json` and `ACC-54-audit-export.json`.
- `ACC-54-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The candidate workspace and its worktree are destroyed; the audit trail and the policy decisions are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
