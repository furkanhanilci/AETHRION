---
title: "ACC-77 — VerifiedValue Rebinding Attempt"
aliases:
  - "ACC-77"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the VerifiedValue Rebinding Attempt situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-77_verified_value_rebinding.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-77 — VerifiedValue Rebinding Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-77` |
| Category | Data/Integrity |
| Severity | **Critical** |
| Accountable owner | Evidence Platform Lead |
| Independent witness / verifier | Internal Audit / Reproducibility Engineer |
| Related packages | `WP-082`, `WP-087` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **VerifiedValue Rebinding Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A `VerifiedValue` is bound to a specific raw evaluator artifact and run.

**When:** A client attempts to reuse the same trusted value identifier against a different raw output, and separately to alter the raw artifact the value points at.

**Then:** Both are refused. The binding is immutable and digest-checked; a changed evaluation produces a new value, and a tampered raw artifact fails its digest.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Create a `VerifiedValue` bound to a raw evaluator artifact | Execution log + trace/event references |
| 2 | Attempt to rebind the identifier to a different raw output | Execution log + trace/event references |
| 3 | Attempt to modify the raw artifact bytes | Execution log + trace/event references |
| 4 | Recompute the digest and compare | Execution log + trace/event references |
| 5 | Produce a legitimate recomputation and observe a new value version | Execution log + trace/event references |
| 6 | Read every publication assertion that referenced the original | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The rebinding attempt is refused
- [ ] The raw artifact modification is refused, and a tampered copy fails its digest check
- [ ] A legitimate recomputation creates a successor value rather than editing one
- [ ] Assertions referencing the original still resolve to the original
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VerifiedValue`
- `RawEvaluatorArtifact`
- `PublicationAssertion`
- `Finding`

## Expected events

- `contract.write_refused`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-77-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-77-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-77-state-before.json` and `ACC-77-state-after.json`.
- `ACC-77-events.json`, `ACC-77-policy-decisions.json` and `ACC-77-audit-export.json`.
- `ACC-77-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test values and artifacts are marked `TEST_CLOSED` and retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
