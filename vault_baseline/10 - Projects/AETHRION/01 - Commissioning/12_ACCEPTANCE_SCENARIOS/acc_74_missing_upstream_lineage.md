---
title: "ACC-74 — Missing Upstream Lineage or Licence"
aliases:
  - "ACC-74"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Missing Upstream Lineage or Licence situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-74_missing_upstream_lineage.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-74 — Missing Upstream Lineage or Licence

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-74` |
| Category | Supply Chain |
| Severity | **High** |
| Accountable owner | Supply Chain Security Lead |
| Independent witness / verifier | Engineering Productivity Lead / Internal Audit |
| Related packages | `WP-024`, `WP-059`, `WP-141` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Missing Upstream Lineage or Licence** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A file adapted from an external source is introduced with no SPDX identifier, no register entry and no pinned commit.

**When:** The change is submitted for merge and then for release.

**Then:** Admission fails at CI before merge. A second variant, correctly registered, passes — so the check discriminates rather than blocking all new files.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Introduce an adapted file with no lineage or licence metadata | Execution log + trace/event references |
| 2 | Submit it and read the CI result | Execution log + trace/event references |
| 3 | Introduce a correctly registered adapted file with a pin and a characterisation suite | Execution log + trace/event references |
| 4 | Submit it and read the CI result | Execution log + trace/event references |
| 5 | Register a direct-adapt entry under a non-permissive licence | Execution log + trace/event references |
| 6 | Run the lineage checker's own self-test | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] The unregistered file fails admission before merge
- [ ] The correctly registered file passes
- [ ] The non-permissive direct-adapt entry is refused
- [ ] The lineage checker's injected controls all fire; none is silent
- [ ] `NOTICE` and the register agree on every adapted file
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `UpstreamLineage`
- `AssimilationCandidate`
- `Finding`

## Expected events

- `ci.admission_failed`
- `assurance.finding_raised`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-74-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-74-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-74-state-before.json` and `ACC-74-state-after.json`.
- `ACC-74-events.json`, `ACC-74-policy-decisions.json` and `ACC-74-audit-export.json`.
- `ACC-74-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test files are removed from the branch; the CI records are retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
