---
title: "ACC-21 — Derived Graph Corruption and Rebuild"
aliases:
  - "ACC-21"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Derived Graph Corruption and Rebuild situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-21_graph_corruption.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/high
  - aethrion/phase/pre-go-live
---

# ACC-21 — Derived Graph Corruption and Rebuild

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-21` |
| Category | Data/Knowledge |
| Severity | **High** |
| Accountable owner | Knowledge Data Lead |
| Independent witness / verifier | Data Platform Lead / Assurance |
| Related packages | `WP-012`, `WP-030`, `WP-074`, `WP-095`, `WP-113`, `WP-114` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A High scenario may be waived only by a time-bound residual risk accepted by the Commissioning Board |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Derived Graph Corruption and Rebuild** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** Node, edge and index corruption has been deliberately introduced into the Neo4j/pgvector/OpenSearch derived read model; the canonical records are intact.

**When:** The integrity check finds the corruption and the full rebuild and swap procedure runs.

**Then:** Canonical services are unaffected; a new projection is built with the expected counts, hashes and lineage and promoted atomically.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Take the canonical fixture snapshot, counts and hashes | Execution log + trace/event references |
| 2 | Corrupt derived nodes, edges and indexes | Execution log + trace/event references |
| 3 | Verify the integrity monitor alarm | Execution log + trace/event references |
| 4 | Perform a full replay and rebuild into a new namespace | Execution log + trace/event references |
| 5 | Run canonical-versus-projection reconciliation | Execution log + trace/event references |
| 6 | Swap the alias and read traffic, then retire the old index | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] No canonical mutation occurred
- [ ] The corruption was detected
- [ ] Rebuild counts and hashes match the fixture
- [ ] The claim lineage query is complete
- [ ] Downtime stays within the SLO policy
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `ProjectionIntegrityRecord`
- `RebuildManifest`
- `ReconciliationReport`
- `AliasPromotionDecision`

## Expected events

- `projection.corrupt`
- `projection.rebuild_started`
- `projection.verified`
- `projection.promoted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-21-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-21-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-21-state-before.json` and `ACC-21-state-after.json`.
- `ACC-21-events.json`, `ACC-21-policy-decisions.json` and `ACC-21-audit-export.json`.
- `ACC-21-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Delete the corrupt test index; remove the new test projection from the test alias or return it to baseline.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
