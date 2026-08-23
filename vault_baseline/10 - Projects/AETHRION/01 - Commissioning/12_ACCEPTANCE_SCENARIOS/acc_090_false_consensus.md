---
title: "ACC-090 — False Consensus Cannot Close a Challenge"
cssclasses:
  - aethrion-reference
type: reference
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the False Consensus Cannot Close a Challenge situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-090_false_consensus.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
---

# ACC-090 — False Consensus Cannot Close a Challenge

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-090` |
| Category | Collaboration/Assurance |
| Severity | **Critical** |
| Accountable owner | Research Director |
| Independent witness / verifier | Assurance Lead / Internal Audit |
| Related packages | `WP-148`, `WP-089` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **False Consensus Cannot Close a Challenge** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Four cohort members agree, and a Skeptic has raised a material methodological challenge that none of them has answered.

**When:** The cohort attempts to converge.

**Then:** Convergence is refused while the challenge is unresolved. A majority cannot close it. It closes by being answered, by being explicitly accepted as a stated limitation, or by escalating.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Convene a cohort with a Skeptic function | Execution log + trace/event references |
| 2 | Raise a material methodological challenge and leave it unanswered | Execution log + trace/event references |
| 3 | Have four members record agreement | Execution log + trace/event references |
| 4 | Attempt to converge | Execution log + trace/event references |
| 5 | Close the challenge by explicit accepted limitation and attempt convergence again | Execution log + trace/event references |
| 6 | Confirm the limitation travels into the finding and the publication assertion | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Convergence is refused while the material challenge is open
- [ ] Majority agreement does not close the challenge
- [ ] An explicitly accepted limitation closes it and is recorded as a limitation
- [ ] The accepted limitation is visible downstream, not absorbed into the synthesis
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `MaterialChallenge`
- `ConvergenceAssessment`
- `FindingRecord`
- `PublicationAssertion`

## Expected events

- `material.challenge.opened`
- `material.challenge.closed`
- `gate.blocked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-090-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-090-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-090-state-before.json` and `ACC-090-state-after.json`.
- `ACC-090-events.json`, `ACC-090-policy-decisions.json` and `ACC-090-audit-export.json`.
- `ACC-090-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The cohort is marked `TEST_CLOSED`; the challenge, its closure and the recorded limitation are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
