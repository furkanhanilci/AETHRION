# WP-087 — Mechanical Verification Engine

## Package card

| Field | Value |
|---|---|
| Work package | `WP-087` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Verification Engineering Lead |
| Independent verifier | Independent Test Engineer |
| Hard dependencies | WP-020, WP-024, WP-026, WP-027, WP-075, WP-076, WP-080, WP-081, WP-082, WP-086 |
| Related gates | G2–G9 |
| Related controls | CTL-EPI-01, CTL-SUP-01 |
| Related acceptance scenarios | ACC-08, ACC-17, ACC-23, ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Schema, hash, test, policy, manifest, signature, locator, lineage and report-to-claim links are verified by deterministic records, independent of any LLM assertion.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-087-T01 | Establish the validator plugin interface and registry | Implementation owner | Commit / configuration / record reference |
| WP-087-T02 | Add the schema, hash, signature, SBOM and policy validators | Implementation owner | Commit / configuration / record reference |
| WP-087-T03 | Bind the test/CI, run, manifest, locator and lineage validators | Implementation owner | Commit / configuration / record reference |
| WP-087-T04 | Write structural validation of findings and the target revision check | Implementation owner | Commit / configuration / record reference |
| WP-087-T05 | Produce the `VerificationRecord` and its evidence map | Implementation owner | Commit / configuration / record reference |
| WP-087-T06 | Establish validator versioning, calibration and regression | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Verification Engine`
- `Validator catalog`
- `VerificationRecord service`
- `Regression fixtures`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Failure on a tampered hash or signature
- Failure on missing lineage or locator
- Invalidation of a finding pointing at the wrong file or symbol
- Deterministic results on the same target
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A self-declaration is never counted as verification.
- [ ] Every validator records its input, output, version and artifact hash.
- [ ] A critical mechanical failure cannot be overridden by a reviewer majority.
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

- Independence asserted in a record but not enforced by the router is decorative.
- A review that sees the producer's conclusion first is anchored, not independent.
- Reproduction that reuses the producer's environment reproduces the environment, not the result.

## Rollback / compensation

A faulty validator release is revoked; affected `VerificationRecord`s are re-run and receive an impact assessment.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
