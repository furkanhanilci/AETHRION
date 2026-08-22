# WP-084 — Clean-Room Reproduction Environment

## Package card

| Field | Value |
|---|---|
| Work package | `WP-084` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Reproducibility Lead |
| Independent verifier | Security / Independent SRE |
| Hard dependencies | WP-007, WP-014, WP-019, WP-026, WP-027, WP-052, WP-053, WP-054, WP-055, WP-059, WP-082 |
| Related gates | G7 |
| Related controls | CTL-GOV-02, CTL-EPI-03, CTL-SEC-04 |
| Related acceptance scenarios | ACC-19, ACC-20 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The reproducer runs in a clean environment built from the frozen manifest, isolated from the producer's workspace, credentials, caches and intermediate traces.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-084-T01 | Establish the dedicated reproduction queue, nodes, namespace and identity | Implementation owner | Commit / configuration / record reference |
| WP-084-T02 | Write the frozen package resolver and the image/data/code fetch verification | Implementation owner | Commit / configuration / record reference |
| WP-084-T03 | Block access to the producer's cache, workspace and credentials | Implementation owner | Commit / configuration / record reference |
| WP-084-T04 | Apply seed and hardware tolerance and capture the environment | Implementation owner | Commit / configuration / record reference |
| WP-084-T05 | Bind the network/offline policy and output capture | Implementation owner | Commit / configuration / record reference |
| WP-084-T06 | Write environment destruction and forensic retention | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Clean-room platform`
- `Reproducer profile`
- `Environment resolver`
- `Isolation attestation`
- `Repro runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of access to producer credentials and caches
- Building the environment from the manifest alone
- Tolerance across different hardware
- Hash failure on a tampered artifact
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] The reproducer never sees the producer's intermediate output.
- [ ] Every input is resolved from a frozen digest.
- [ ] The clean-room attestation is attached to the report.
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

A suspect reproduction cell is contained; the run is re-planned in a fresh clean cell with independent credentials.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
