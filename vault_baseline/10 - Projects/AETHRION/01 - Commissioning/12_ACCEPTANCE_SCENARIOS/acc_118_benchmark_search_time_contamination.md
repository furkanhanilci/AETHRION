---
title: "ACC-118 — Search-Time Benchmark Contamination"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Search-Time Benchmark Contamination situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-118_benchmark_search_time_contamination.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-118 — Search-Time Benchmark Contamination

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-118` |
| Category | Evaluation/Integrity |
| Severity | **Critical** |
| Accountable owner | Eval Office |
| Independent witness / verifier | Assurance Lead / Research Director |
| Related packages | `WP-057`, `WP-158` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Search-Time Benchmark Contamination** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A benchmark run executes with retrieval enabled, and benchmark question or answer material is reachable through ordinary search.

**When:** The run completes and its search log is scanned.

**Then:** The run is labelled `CONTAMINATED` or `REVIEW_REQUIRED` and its score is never reported as a clean score. A run with no benchmark material in its log is reported clean, and a contaminated run is not silently rerun.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Freeze the benchmark policy, dataset manifest and allowed domains | Execution log + trace/event references |
| 2 | Run with benchmark material reachable through retrieval | Execution log + trace/event references |
| 3 | Scan the retrieval audit log and read the label assigned | Execution log + trace/event references |
| 4 | Confirm the score is not reported as clean | Execution log + trace/event references |
| 5 | Attempt to rerun and report a clean score from the retry | Execution log + trace/event references |
| 6 | Run under a restricted network mode with no benchmark material reachable | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] A run that reached benchmark material is labelled and not reported clean
- [ ] The clean run under restricted retrieval is reported clean — the scanner discriminates
- [ ] A contaminated run cannot be silently rerun to obtain a clean score
- [ ] Gold answers, rubrics and grader prompts were unreachable from the agent throughout
- [ ] The label travels with the score into the release dossier
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `BenchmarkRunPolicy`
- `ContaminationFinding`
- `MetascienceReport`

## Expected events

- `benchmark.contamination_detected`
- `benchmark.run_completed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-118-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-118-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-118-state-before.json` and `ACC-118-state-after.json`.
- `ACC-118-events.json`, `ACC-118-policy-decisions.json` and `ACC-118-audit-export.json`.
- `ACC-118-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Both runs are marked `TEST_CLOSED`; search logs and labels are retained with the scores.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
