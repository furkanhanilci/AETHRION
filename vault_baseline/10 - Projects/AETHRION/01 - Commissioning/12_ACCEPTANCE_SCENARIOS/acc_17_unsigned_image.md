---
title: "ACC-17 — Unsigned or Mutable Image"
aliases:
  - "ACC-17"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Unsigned or Mutable Image situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-17_unsigned_image.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-17 — Unsigned or Mutable Image

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-17` |
| Category | Security/Supply Chain |
| Severity | **Critical** |
| Accountable owner | Supply Chain Security Lead |
| Independent witness / verifier | Independent Security Reviewer |
| Related packages | `WP-027`, `WP-054`, `WP-059`, `WP-060`, `WP-087`, `WP-107`, `WP-112` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Unsigned or Mutable Image** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A workload is submitted to a production or staging secure namespace with an unsigned image or a mutable tag.

**When:** The Kubernetes admission controller evaluates the manifest.

**Then:** The pod is not created; the signature, provenance and digest policy denies it and produces audit and alert records. A signed-digest counter-example passes.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Push the unsigned image fixture | Execution log + trace/event references |
| 2 | Submit a manifest with a mutable tag | Execution log + trace/event references |
| 3 | Try a signed fixture with provenance from the wrong builder | Execution log + trace/event references |
| 4 | Collect the admission denial reason and audit record | Execution log + trace/event references |
| 5 | Submit an approved signed digest | Execution log + trace/event references |
| 6 | Observe the impact behaviour for a running revoked digest | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Pods from unsigned, mutable-tag or wrong-provenance images = 0
- [ ] The denial rule and digest are visible
- [ ] An approved signed digest runs
- [ ] Revocation produces an alert and an impact assessment
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `AdmissionDecision`
- `ImageSignature/SBOM/Provenance`
- `SecurityEvent`
- `WorkloadRecord`

## Expected events

- `supply_chain.denied`
- `unsigned_image.detected`
- `artifact.revoked`
- `workload.admitted`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-17-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-17-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-17-state-before.json` and `ACC-17-state-after.json`.
- `ACC-17-events.json`, `ACC-17-policy-decisions.json` and `ACC-17-audit-export.json`.
- `ACC-17-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Test images are quarantined or deleted under retention policy; the approved fixture workload is destroyed.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
