# WP-054 — gVisor Sandbox and Execution Cell Lifecycle

## Package card

| Field | Value |
|---|---|
| Work package | `WP-054` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Execution Security Lead |
| Independent verifier | Red Team / SRE |
| Hard dependencies | WP-006, WP-014, WP-027, WP-049, WP-052, WP-053 |
| Related gates | G5,Engineering |
| Related controls | CTL-SEC-04, CTL-SEC-05 |
| Related acceptance scenarios | ACC-15, ACC-17 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Every autonomous code execution runs in an ephemeral cell — resolve → allocate → attest → execute → capture → destroy — that is digest-pinned, privilege-free, scope-mounted and produces forensic evidence.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/wp_027_git_oci_supply_chain.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-054-T01 | Establish the RuntimeClass/gVisor and seccomp/capability baseline | Implementation owner | Commit / configuration / record reference |
| WP-054-T02 | Apply the ephemeral workspace, mount and path policy | Implementation owner | Commit / configuration / record reference |
| WP-054-T03 | Bind the OCI signature and SBOM attestation gate | Implementation owner | Commit / configuration / record reference |
| WP-054-T04 | Add CPU, memory, wall-clock and process limits | Implementation owner | Commit / configuration / record reference |
| WP-054-T05 | Write artifact capture, hashing, upload and teardown | Implementation owner | Commit / configuration / record reference |
| WP-054-T06 | Establish forensic snapshotting and escape detection | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Sandbox profiles`
- `Execution Cell controller`
- `SandboxAttestation`
- `Capture/destroy workflow`
- `Red-team tests`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of host mount, privilege and syscall escape attempts
- Denial of unsigned or mutable images
- Termination of a resource bomb
- Artifact capture followed by cell destruction
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] An agent has no direct access to the host kernel, credentials or network.
- [ ] Credentials and compute are destroyed at cell expiry.
- [ ] Artifact hashes and attestations return to the workflow.
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

- A control not exercised by a negative test is an assumption.
- Default-allow egress anywhere in the chain nullifies every other isolation control.
- Sandbox escape is tested by attempting it, not by reading the configuration.

## Rollback / compensation

A suspicious cell is contained and stopped, its forensic snapshot quarantined, and the node drain/reimage runbook is executed.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
