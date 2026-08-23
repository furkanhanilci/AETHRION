---
title: "ACC-65 — Reproduction in the Producer Environment"
aliases:
  - "ACC-65"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Reproduction in the Producer Environment situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-65_reproduction_in_producer_environment.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-65 — Reproduction in the Producer Environment

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-65` |
| Category | Evidence/Reproduction |
| Severity | **Critical** |
| Accountable owner | Reproducibility Lead |
| Independent witness / verifier | Assurance Lead / Internal Audit |
| Related packages | `WP-007`, `WP-084`, `WP-085` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Reproduction in the Producer Environment** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A G7 reproduction is scheduled where the reproducer would inherit the producer's workspace, container layer or cached state.

**When:** The reproduction is launched.

**Then:** The `IndependenceProfile` detects the shared environment lineage and refuses to award reproduced status. A run may still be executed and recorded, but it is classified as repeatability, not reproducibility.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Attempt reproduction inside the producer workspace | Execution log + trace/event references |
| 2 | Attempt it in a fresh container built from the producer's cached layers | Execution log + trace/event references |
| 3 | Attempt it with the producer's model and tool credentials still bound | Execution log + trace/event references |
| 4 | Attempt it with the same actor identity as the producer | Execution log + trace/event references |
| 5 | Run it in a genuinely independent environment | Execution log + trace/event references |
| 6 | Compare the status awarded in each case | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The first four attempts are refused reproduced status
- [ ] Any run that does execute is classified as repeatability with its reason recorded
- [ ] Only the independent environment yields reproducibility
- [ ] The environment digest lineage, not a declaration, decides the classification
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `IndependenceProfile`
- `ReproductionRun`
- `GateRecord`
- `Finding`

## Expected events

- `reproduction.independence_violation`
- `gate.blocked`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-65-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-65-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-65-state-before.json` and `ACC-65-state-after.json`.
- `ACC-65-events.json`, `ACC-65-policy-decisions.json` and `ACC-65-audit-export.json`.
- `ACC-65-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test environments are destroyed; the environment digests and refusal records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
