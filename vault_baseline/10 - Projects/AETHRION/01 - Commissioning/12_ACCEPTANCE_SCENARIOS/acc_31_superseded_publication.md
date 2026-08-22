---
title: "ACC-31 — Superseded Publication"
aliases:
  - "ACC-31"
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Superseded Publication situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-31_superseded_publication.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-31 — Superseded Publication

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-31` |
| Category | Publication/Monitoring |
| Severity | **High** |
| Accountable owner | Publication Owner |
| Independent witness / verifier | Archivist / Citation Auditor |
| Related packages | `WP-037`, `WP-074`, `WP-075`, `WP-090`, `WP-095`, `WP-106`, `WP-108`, `WP-113`, `WP-137` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Superseded Publication** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** New evidence or a new decision requires a corrected replacement for an already-published package.

**When:** The new package is published and the supersession relation and event are processed.

**Then:** The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare publication v1 with a stable URL and hash | Execution log + trace/event references |
| 2 | Produce the new claim, decision and package v2 | Execution log + trace/event references |
| 3 | Run the supersession decision and the release | Execution log + trace/event references |
| 4 | Query the v1 and v2 landing metadata and links | Execution log + trace/event references |
| 5 | Observe the search index, consumer and Obsidian projection updates | Execution log + trace/event references |
| 6 | Verify the audit chain | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] v1 bytes and hash are unchanged and still accessible
- [ ] v1 carries a superseded banner and link
- [ ] v2 records that it supersedes v1 and why
- [ ] Consumers are notified exactly once
- [ ] The ledger and history are complete
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `PublicationPackages v1/v2`
- `SupersessionRecord`
- `DecisionRecord`
- `ProjectionRecords`
- `AuditExport`

## Expected events

- `publication.released`
- `publication.superseded`
- `consumers.impact_notified`
- `knowledge.projection_updated`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-31-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-31-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-31-state-before.json` and `ACC-31-state-after.json`.
- `ACC-31-events.json`, `ACC-31-policy-decisions.json` and `ACC-31-audit-export.json`.
- `ACC-31-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The synthetic publications move to TEST/unpublished visibility; the supersession chain is retained.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
