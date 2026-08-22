---
title: "ACC-32 — Secret in Prompt or Trace"
aliases:
  - "ACC-32"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Secret in Prompt or Trace situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-32_secret_in_trace.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-32 — Secret in Prompt or Trace

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-32` |
| Category | Security/Observability |
| Severity | **Critical** |
| Accountable owner | AI Observability Lead |
| Independent witness / verifier | Privacy/Security Reviewer |
| Related packages | `WP-057`, `WP-060`, `WP-097`, `WP-104`, `WP-112` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Secret in Prompt or Trace** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A synthetic canary credential is present in a model prompt or tool input.

**When:** The gateway, LangGraph, Langfuse, OTel and log pipelines process the request.

**Then:** The secret never appears in raw telemetry, events or the UI; redaction or quarantine occurs, a security event is raised and the credential is revoked.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Prepare the canary secret and its lookup detector | Execution log + trace/event references |
| 2 | Insert the canary into the prompt and tool input | Execution log + trace/event references |
| 3 | Run the model and tool trace pipeline | Execution log + trace/event references |
| 4 | Scan the Langfuse, OTel, log, NATS, audit and search stores | Execution log + trace/event references |
| 5 | Check a UI and export sample | Execution log + trace/event references |
| 6 | Verify the revoke and incident behaviour | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Raw canary occurrences in permitted stores = 0
- [ ] A redaction marker and its provenance are present
- [ ] A security event is raised and the lease is revoked
- [ ] The DLP detector produces no false negative
- [ ] The canonical task result remains policy-compliant
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `DLPRecord`
- `RedactedTrace`
- `SecurityEvent`
- `VaultLeaseRecord`
- `AuditRecord`

## Expected events

- `trace.secret_detected`
- `telemetry.redacted_or_quarantined`
- `credential.revoked`
- `incident.opened`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-32-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-32-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-32-state-before.json` and `ACC-32-state-after.json`.
- `ACC-32-events.json`, `ACC-32-policy-decisions.json` and `ACC-32-audit-export.json`.
- `ACC-32-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The canary is revoked and deleted; telemetry test records are retained in redacted form under retention policy.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
