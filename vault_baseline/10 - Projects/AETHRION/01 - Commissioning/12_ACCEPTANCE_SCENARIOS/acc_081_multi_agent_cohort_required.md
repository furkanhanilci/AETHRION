---
title: "ACC-081 — Multi-Agent Cohort Required"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Multi-Agent Cohort Required situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-081_multi_agent_cohort_required.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-081 — Multi-Agent Cohort Required

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-081` |
| Category | Collaboration/Governance |
| Severity | **Critical** |
| Accountable owner | Research Director |
| Independent witness / verifier | Assurance Lead / Chief Architect |
| Related packages | `WP-047`, `WP-148` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Multi-Agent Cohort Required** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A substantial scientific task is submitted, and the requested configuration names one cognitive actor.

**When:** The Task Compiler compiles the task.

**Then:** Compilation refuses, or adds the independent cognitive actors the invariant requires. There is no silent single-agent downgrade, and a cohort of several instances of the same model profile on the same context does not satisfy the requirement either.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Submit a substantial task with one cognitive actor | Execution log + trace/event references |
| 2 | Read the compiler's refusal and the invariant it names | Execution log + trace/event references |
| 3 | Submit the same task with five instances of one model profile on identical context | Execution log + trace/event references |
| 4 | Submit it with three differentiated cognitive functions and distinct evidence exposure | Execution log + trace/event references |
| 5 | Compare the `CognitiveDiversityProfile` produced in each case | Execution log + trace/event references |
| 6 | Submit a task below the substantiality threshold and confirm the invariant does not apply | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The single-actor compile is refused and names `ADR-011`
- [ ] Five identical profiles do **not** satisfy independence; the diversity profile shows why
- [ ] Three differentiated functions do satisfy it
- [ ] A non-substantial task compiles without a cohort — the rule discriminates rather than blocking everything
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `AgentCohortRecord`
- `CognitiveDiversityProfile`
- `TaskContract`
- `PolicyDecision`

## Expected events

- `cohort.compiled`
- `task.compilation_refused`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-081-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-081-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-081-state-before.json` and `ACC-081-state-after.json`.
- `ACC-081-events.json`, `ACC-081-policy-decisions.json` and `ACC-081-audit-export.json`.
- `ACC-081-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test cohort and its compiled task are marked `TEST_CLOSED`; the diversity profiles are retained for the calibration set.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
