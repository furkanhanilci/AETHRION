---
title: "ACC-16 — Egress Exfiltration Attempt"
aliases:
  - "ACC-16"
cssclasses:
  - aethrion-acceptance-scenario
type: acceptance-scenario
category: commissioning
summary: "This scenario verifies the target architecture's fail-safe behaviour and its evidence production in the Egress Exfiltration Attempt situation."
source: "planning/commissioning/12_ACCEPTANCE_SCENARIOS/ACC-16_egress_exfiltration.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/acceptance-scenario
  - aethrion/severity/critical
  - aethrion/phase/pre-go-live
---

# ACC-16 — Egress Exfiltration Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-16` |
| Category | Security/Network |
| Severity | **Critical** |
| Accountable owner | Network Security Lead |
| Independent witness / verifier | Red Team / Privacy Owner |
| Related packages | `WP-051`, `WP-057`, `WP-060`, `WP-112` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Egress Exfiltration Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A payload inside the sandbox attempts to send a canary secret over an unknown domain, a raw IP and a DNS tunnel.

**When:** Execution proceeds through the egress proxy and DLP.

**Then:** The traffic is denied, the canary never leaves, the credential lease is revoked and a security incident and audit record are created.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Set up the canary secret and the attack destination | Execution log + trace/event references |
| 2 | Issue a scoped lease to the sandbox workload | Execution log + trace/event references |
| 3 | Run the HTTPS, raw IP, DNS and proxy-bypass attempts | Execution log + trace/event references |
| 4 | Observe the egress, DLP, Vault and network logs | Execution log + trace/event references |
| 5 | Verify lease revocation and the incident workflow | Execution log + trace/event references |
| 6 | Confirm that no byte reached the canary destination | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Exfiltrated bytes = 0
- [ ] Unknown domains, raw IPs and DNS tunnels are denied
- [ ] DLP matches the canary
- [ ] The lease is revoked
- [ ] Security event correlation is complete
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `EgressDecision`
- `DLPRecord`
- `VaultLeaseRecord`
- `SecurityIncident`
- `NetworkTrace`

## Expected events

- `egress.denied`
- `dlp.secret_detected`
- `credential.revoked`
- `incident.opened`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-16-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-16-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-16-state-before.json` and `ACC-16-state-after.json`.
- `ACC-16-events.json`, `ACC-16-policy-decisions.json` and `ACC-16-audit-export.json`.
- `ACC-16-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

Canary credentials are revoked and rotated; the malicious workload is destroyed and the destination and log fixtures are cleaned up.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
