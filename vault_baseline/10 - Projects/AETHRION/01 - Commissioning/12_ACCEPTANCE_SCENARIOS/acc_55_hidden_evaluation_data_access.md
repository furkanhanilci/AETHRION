---
title: "ACC-55 — Hidden Evaluation Data Access Attempt"
aliases:
  - "ACC-55"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Hidden Evaluation Data Access Attempt situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-55_hidden_evaluation_data_access.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-55 — Hidden Evaluation Data Access Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-55` |
| Category | Security/Execution |
| Severity | **Critical** |
| Accountable owner | Execution Security Lead |
| Independent witness / verifier | Network Security Lead / Internal Audit |
| Related packages | `WP-054`, `WP-057`, `WP-060`, `WP-084` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Hidden Evaluation Data Access Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** The official evaluator holds hidden validation material and answer keys in a private zone with its own identity and policy.

**When:** The candidate attempts to reach that material through the filesystem, the process table, mount points, environment variables, the evaluator's return channel and the network.

**Then:** Access is denied under the supported threat model, no hidden content appears in any candidate artifact, log or trace, and each attempt raises a security finding.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Seed the private zone with a canary record that appears nowhere else | Execution log + trace/event references |
| 2 | Attempt filesystem and mount traversal from the candidate shell | Execution log + trace/event references |
| 3 | Attempt to read the evaluator process environment and credentials | Execution log + trace/event references |
| 4 | Attempt to widen the evaluator's returned fields beyond the permitted score projection | Execution log + trace/event references |
| 5 | Attempt an outbound network call carrying a probe | Execution log + trace/event references |
| 6 | Scan every candidate artifact, log and trace for the canary | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The canary appears in zero candidate artifacts, logs or traces
- [ ] Every access route in the supported threat model is denied and audited
- [ ] The evaluator returns only the permitted fields; hidden labels are absent from the projection
- [ ] The egress attempt is blocked and recorded
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `CandidateWorkspace`
- `ExecutionProfile`
- `PolicyDecision`
- `Finding`

## Expected events

- `policy.denied`
- `egress.blocked`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-55-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-55-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-55-state-before.json` and `ACC-55-state-after.json`.
- `ACC-55-events.json`, `ACC-55-policy-decisions.json` and `ACC-55-audit-export.json`.
- `ACC-55-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The canary is rotated; the private zone is restored from its baseline; the attempt log is retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
