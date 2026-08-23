---
title: "ACC-104 — Major Specification Drift Blocks Confirmatory Status"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Major Specification Drift Blocks Confirmatory Status situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-104_scientific_major_spec_drift.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-104 — Major Specification Drift Blocks Confirmatory Status

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-104` |
| Category | Engineering/Assurance |
| Severity | **Critical** |
| Accountable owner | Research Director |
| Independent witness / verifier | Assurance Lead / Internal Audit |
| Related packages | `WP-081`, `WP-154` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Major Specification Drift Blocks Confirmatory Status** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A confirmatory study's frozen specification is implemented with a material deviation — a simplified algorithm, an omitted baseline or an altered data split — and it is not approved.

**When:** The conformance check runs and the package attempts to proceed.

**Then:** The deviation is classified `SCIENTIFIC_MAJOR`. The confirmatory package cannot proceed: the minimum consequence is relabelling to exploratory, or a re-freeze and a re-run. A clean implementation passes.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Freeze a confirmatory specification | Execution log + trace/event references |
| 2 | Implement it with each of the seven planted drift fixtures in turn | Execution log + trace/event references |
| 3 | Run the conformance check on each | Execution log + trace/event references |
| 4 | Attempt to proceed as confirmatory with an unapproved major deviation | Execution log + trace/event references |
| 5 | Exercise the relabel-to-exploratory consequence | Execution log + trace/event references |
| 6 | Run the check on a clean implementation as a negative control | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Each of the seven planted drifts is detected
- [ ] A material deviation is classified `SCIENTIFIC_MAJOR`
- [ ] An unapproved major deviation cannot carry a confirmatory package forward
- [ ] The clean implementation passes — the detector discriminates
- [ ] A comparison that cannot be made confidently reports `UNKNOWN`, not `NONE`
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `SpecificationConformanceRecord`
- `StudyModeRecord`
- `ClaimVersion`
- `GateRecord`

## Expected events

- `spec.deviation.detected`
- `gate.blocked`
- `study_mode.superseded`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-104-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-104-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-104-state-before.json` and `ACC-104-state-after.json`.
- `ACC-104-events.json`, `ACC-104-policy-decisions.json` and `ACC-104-audit-export.json`.
- `ACC-104-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test studies are marked `TEST_CLOSED`; every conformance record and both implementations are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
