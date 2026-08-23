---
title: "ACC-73 — Upstream Assimilation Drift"
aliases:
  - "ACC-73"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Upstream Assimilation Drift situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-73_upstream_assimilation_drift.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/day2-continuous
---

# ACC-73 — Upstream Assimilation Drift

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-73` |
| Category | Supply Chain |
| Severity | **High** |
| Accountable owner | Supply Chain Security Lead |
| Independent witness / verifier | Chief Architect / Internal Audit |
| Related packages | `WP-059`, `WP-130`, `WP-141` |
| Acceptance phase | `DAY2_CONTINUOUS` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Upstream Assimilation Drift** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A mechanism was adapted from a pinned upstream commit and carries a characterisation suite.

**When:** Upstream moves, and one of the changed commits alters behaviour the characterisation suite covers.

**Then:** The drift checker reports the divergence and opens a review item. Nothing is auto-merged, and the characterisation suite must be rerun and reviewed before the pin moves.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Record a pinned commit and its characterisation suite | Execution log + trace/event references |
| 2 | Advance the upstream reference past the pin | Execution log + trace/event references |
| 3 | Run the drift checker and read what it reports | Execution log + trace/event references |
| 4 | Attempt an automatic update of the pin | Execution log + trace/event references |
| 5 | Rerun the characterisation suite against the new upstream behaviour | Execution log + trace/event references |
| 6 | Move the pin through the review path and read the record | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The drift is detected and named, with the old and new references
- [ ] No automatic update occurs — the auto-update attempt is refused
- [ ] A review item exists before the pin can move
- [ ] A behavioural difference the suite covers is reported as semantic, not cosmetic
- [ ] Moving the pin produces a recorded decision, not a silent edit
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `UpstreamLineage`
- `AssimilationCandidate`
- `Finding`
- `DecisionRecord`

## Expected events

- `supplychain.upstream_drift_detected`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-73-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-73-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-73-state-before.json` and `ACC-73-state-after.json`.
- `ACC-73-events.json`, `ACC-73-policy-decisions.json` and `ACC-73-audit-export.json`.
- `ACC-73-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The test pin is restored; the drift report and the review item are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
