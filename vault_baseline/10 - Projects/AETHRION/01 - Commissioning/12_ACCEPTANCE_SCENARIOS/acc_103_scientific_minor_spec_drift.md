---
title: "ACC-103 — Minor Specification Drift Is Recorded"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Minor Specification Drift Is Recorded situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-103_scientific_minor_spec_drift.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-103 — Minor Specification Drift Is Recorded

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-103` |
| Category | Engineering/Assurance |
| Severity | **High** |
| Accountable owner | Chief Architect |
| Independent witness / verifier | Methodologist / Assurance Lead |
| Related packages | `WP-081`, `WP-154` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Minor Specification Drift Is Recorded** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A frozen specification is implemented with a bounded deviation — a tolerance changed, a default altered — and separately with a pure refactor.

**When:** The conformance check compares each against the frozen specification.

**Then:** The bounded deviation is classified `SCIENTIFIC_MINOR`, recorded and reported with the result. The refactor is `ENGINEERING_ONLY` and changes no scientific status.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Freeze a specification and implement it faithfully | Execution log + trace/event references |
| 2 | Introduce a bounded tolerance change and run the conformance check | Execution log + trace/event references |
| 3 | Introduce a pure refactor and run it again | Execution log + trace/event references |
| 4 | Read the severity assigned in each case | Execution log + trace/event references |
| 5 | Confirm the minor deviation is reported with the result | Execution log + trace/event references |
| 6 | Confirm the refactor changes no scientific status | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The bounded deviation is classified `SCIENTIFIC_MINOR` and travels with the result
- [ ] The refactor is classified `ENGINEERING_ONLY`
- [ ] Neither is classified `NONE`
- [ ] The scientific status is unchanged by the engineering-only deviation
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SpecificationConformanceRecord`
- `AnalysisPlanManifest`
- `ArtifactRecord`

## Expected events

- `spec.deviation.detected`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-103-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-103-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-103-state-before.json` and `ACC-103-state-after.json`.
- `ACC-103-events.json`, `ACC-103-policy-decisions.json` and `ACC-103-audit-export.json`.
- `ACC-103-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test specifications and implementations are marked `TEST_CLOSED`; conformance records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
