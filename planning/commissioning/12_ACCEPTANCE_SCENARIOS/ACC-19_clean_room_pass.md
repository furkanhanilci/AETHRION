# ACC-19 — Clean-Room Reproduction Pass

## Scenario card

| Field | Value |
|---|---|
| Scenario | `ACC-19` |
| Category | Evidence/Reproduction |
| Severity | **High** |
| Accountable owner | Reproducibility Lead |
| Independent witness / verifier | Assurance Lead / Statistician |
| Related packages | `WP-084`, `WP-085`, `WP-105`, `WP-113` |
| Production acceptance | A Critical scenario can never be counted as PASS through a SKIP or a waiver |

## Purpose

This scenario verifies the target architecture's fail-safe behaviour and its
evidence production in the **Clean-Room Reproduction Pass** situation. The test runs on the same
release candidate, policy bundle, schema bundle and environment manifest as
every other scenario in the same acceptance round.

## Given / When / Then

**Given:** A frozen protocol, data, code, environment, model and seed manifest exists alongside a pre-declared stochastic tolerance.

**When:** An independent reproducer runs from the manifest in a clean environment.

**Then:** The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass.

## Preconditions

- The related work packages are `INTEGRATED` or `COMMISSIONING_READY`.
- Test-specific project, actor, data and artifact identifiers are separated from production data.
- The release candidate digest and the policy, schema, model/tool and infrastructure bundle versions are frozen.
- The expected canonical records, events, policy decisions, telemetry and audit assertions are entered in the registry.
- The failure-injection blast radius, the kill switch, the cleanup procedure and the witness are assigned.

## Test steps

| # | Action | Evidence captured at this step |
|---:|---|---|
| 1 | Produce the producer run and the frozen package | Execution log + trace/event references |
| 2 | Assign an independent reproducer, credentials and environment | Execution log + trace/event references |
| 3 | Verify the manifest hashes and build the environment | Execution log + trace/event references |
| 4 | Run the job and compute metrics and tolerance | Execution log + trace/event references |
| 5 | Compare producer and reproducer lineage and outputs | Execution log + trace/event references |
| 6 | Run the G7 Gate Service evaluation | Execution log + trace/event references |

## Mandatory invariants and assertions

- [ ] Every input digest matches
- [ ] The `IndependenceProfile` is satisfied
- [ ] Metrics fall within tolerance
- [ ] The reproduction certificate is signed
- [ ] G7 hard checks PASS
- [ ] The actual canonical state equals the expected state, or an explained safe failure state.
- [ ] Duplicate, stale, forged or partial inputs produced no unsafe side effect.
- [ ] Trace, event, audit and business records share one project/workflow/run correlation chain.
- [ ] Every Critical or High finding raised during the test is recorded in the Finding Registry.

## Expected canonical records

- `RunManifest`
- `EnvironmentManifest`
- `IndependenceProfile`
- `ReproductionReport`
- `GateRecord`

## Expected events

- `reproduction.started`
- `reproduction.passed`
- `claim.reproduction_updated`
- `gate.passed`

Expected event counts, idempotency and ordering constraints live in the
machine-readable assertion file inside the test registry. **A NATS event alone
is not evidence of canonical state**; the corresponding service or Temporal
commit is verified separately.

## Evidence package

- `ACC-19-result.json`: PASS/FAIL, the RC digest and the assertion results.
- `ACC-19-execution-log.jsonl`: time-ordered test, fault and decision records.
- `ACC-19-state-before.json` and `ACC-19-state-after.json`.
- `ACC-19-events.json`, `ACC-19-policy-decisions.json` and `ACC-19-audit-export.json`.
- `ACC-19-evidence-manifest.json`: the hash, producer and environment reference of every file.
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

The clean room is destroyed; artifacts and the report remain in the immutable store under test retention.

Cleanup never deletes canonical evidence or audit history. Destructive test
fixture operations run only against explicit test namespaces and identities, and
only under two-stage confirmation.
