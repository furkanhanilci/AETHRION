# ACC-15 — Sandbox Escape Attempt

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-15` |
| Category | Security/Execution |
| Severity | **Critical** |
| Accountable owner | Execution Security Lead |
| Independent witness / verifier | Red Team / SRE |
| Related packages | `WP-006`, `WP-054`, `WP-060`, `WP-112` |
| Acceptance phase | `PRE_GO_LIVE` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Sandbox Escape Attempt** situation.

The test runs on the same release candidate, policy bundle, schema bundle and
environment manifest as every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A malicious code fixture attempts host mounts, privileged syscalls, namespace escape and access to metadata/credential endpoints.

**When:** The code runs inside a gVisor execution cell.

**Then:** Every escape path is denied or contained; no credential or host data leaks, the cell is stopped and a forensic `SecurityEvent` is produced.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Resolve the signed malicious test image from the attack registry | Execution log + trace/event references |
| 2 | Start the sandbox with its `ExecutionProfile` | Execution log + trace/event references |
| 3 | Run the syscall, mount, namespace and metadata attacks | Execution log + trace/event references |
| 4 | Monitor runtime, network and Vault telemetry | Execution log + trace/event references |
| 5 | Verify the contain, stop, snapshot and node action | Execution log + trace/event references |
| 6 | Check host and cluster integrity after the test | Execution log + trace/event references |
| 7 | Attempt the escape through a shared cache, an inherited credential and a warm layer, not only through the sandbox boundary | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Host file reads and writes = 0
- [ ] Privileged syscalls and escapes are denied
- [ ] Secret leases are minimal or absent
- [ ] Forensic artifacts are complete
- [ ] Neither the node nor other workloads are affected
- [ ] The isolation is **four zones**, not one sandbox: producer, evaluator, reproducer and independent grader.
- [ ] The quiet paths are tested explicitly — a shared cache, an inherited credential, a warm container layer — because none of them looks like an escape in a log — ACC-113.
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

### Baseline v1.3.0 — what this scenario must also show

A sandbox escape test that only attacks the sandbox misses the three routes that do not require one. WP-157 owns the leakage suite.

The additional assertions above are **extensions of this scenario, not a new
one.** Where the reliability layer needs a scenario of its own it has one in
ACC-081–120; what is added here is the case this scenario would otherwise pass
while the new failure went unexamined.

## Expected canonical records

- `SandboxAttestation`
- `RuntimeSecurityRecord`
- `ForensicArtifact`
- `SecurityIncident`
- `ExecutionLease`

## Expected events

- `sandbox.escape_attempted`
- `runtime.denied`
- `execution.contained`
- `incident.opened`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-15-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-15-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-15-state-before.json` and `ACC-15-state-after.json`.
- `ACC-15-events.json`, `ACC-15-policy-decisions.json` and `ACC-15-audit-export.json`.
- `ACC-15-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The malicious cell is destroyed; the node is drained and reimaged if required, and the fixture image is kept only in the test registry.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
