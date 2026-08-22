# WP-099 — WORM Audit Ledger and Independent Export

## Package card

| Field | Value |
|---|---|
| Work package | `WP-099` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Internal Audit Platform Lead |
| Independent verifier | Independent Auditor / Security |
| Hard dependencies | WP-011, WP-015, WP-016, WP-025, WP-026, WP-028, WP-049, WP-055, WP-056, WP-059, WP-075, WP-082, WP-096 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-GOV-01, CTL-OPS-03 |
| Related acceptance scenarios | ACC-40 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Policy, identity, model, tool, workflow, source, claim, artifact, cost and human decision events are kept in a hash-chained WORM record and exported per project in a verifiable form.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-099-T01 | Write audit event canonicalisation and the sequence/hash chain | Implementation owner | Commit / configuration / record reference |
| WP-099-T02 | Establish the WORM store, retention and access separation | Implementation owner | Commit / configuration / record reference |
| WP-099-T03 | Add sensitive-field encryption/redaction and audit-of-audit logging | Implementation owner | Commit / configuration / record reference |
| WP-099-T04 | Write the project, time, actor and control export API | Implementation owner | Commit / configuration / record reference |
| WP-099-T05 | Build the signature, manifest and verifier CLI | Implementation owner | Commit / configuration / record reference |
| WP-099-T06 | Add tamper and gap detection with incident triggers | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Audit Ledger`
- `Hash-chain service`
- `Audit export/verify tooling`
- `Retention/access policy`
- `Integrity dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Detection of a tampered record
- Detection of a missing sequence gap
- Denial of unauthorised delete or modify
- Full project export with chain verification
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An audit administrator cannot alter the records.
- [ ] An export carries the complete policy, model, tool, cost, artifact and decision chain.
- [ ] Retention respects legal hold.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A corrupted replica is restored from an intact WORM copy; a hash gap is a critical incident and a cutover blocker.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
