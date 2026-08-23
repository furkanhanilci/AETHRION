---
title: "ACC-62 — Semantic Verifier Recorded as Mechanical"
aliases:
  - "ACC-62"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Semantic Verifier Recorded as Mechanical situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-62_verifier_class_misdeclaration.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-62 — Semantic Verifier Recorded as Mechanical

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-62` |
| Category | Assurance/Contracts |
| Severity | **High** |
| Accountable owner | Chief Architect |
| Independent witness / verifier | Assurance Lead / Internal Audit |
| Related packages | `WP-018`, `WP-087` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Semantic Verifier Recorded as Mechanical** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A model-mediated entailment result is submitted to the ledger with verification class V0 or V1.

**When:** The submission is processed.

**Then:** It is refused. A verification class is set by the authorised verifier service from the procedure that actually ran, not by the caller, and the attempt raises an audit finding.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Submit a model-mediated result declared as V0 | Execution log + trace/event references |
| 2 | Submit the same result declared as V1 | Execution log + trace/event references |
| 3 | Submit it through the authorised verifier service and read the class it assigns | Execution log + trace/event references |
| 4 | Attempt to edit the class on a stored `VerificationResult` | Execution log + trace/event references |
| 5 | Confirm no V0 result in the ledger invoked a model | Execution log + trace/event references |
| 6 | Read the audit findings raised | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Both misdeclared submissions are refused
- [ ] The authorised service assigns V2 for the model-mediated procedure
- [ ] The class field on a stored result is immutable
- [ ] Zero results classified V0 have an associated model invocation record
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `VerificationResult`
- `ModelInvocationRecord`
- `Finding`

## Expected events

- `contract.write_refused`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-62-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-62-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-62-state-before.json` and `ACC-62-state-after.json`.
- `ACC-62-events.json`, `ACC-62-policy-decisions.json` and `ACC-62-audit-export.json`.
- `ACC-62-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test verification results are marked `TEST_CLOSED` and retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
