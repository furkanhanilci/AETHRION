# WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-059` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Independent Security Reviewer |
| Hard dependencies | WP-027, WP-052, WP-054, WP-056 |
| Related gates | G5,Platform |
| Related controls | CTL-SEC-05, CTL-SUP-01 |
| Related acceptance scenarios | ACC-17, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Purpose and expected outcome

Kubernetes and tool/runtime deployments accept only digest-pinned, signed artifacts with SBOM and provenance that satisfy policy.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-059-T01 | Deploy the admission controller and its trust roots | Implementation owner | Commit / configuration / record reference |
| WP-059-T02 | Write the Cosign signature, provenance and SBOM policy | Implementation owner | Commit / configuration / record reference |
| WP-059-T03 | Define the allowed builders, source repositories and dependency thresholds | Implementation owner | Commit / configuration / record reference |
| WP-059-T04 | Bind the CVE exception and expiry workflow | Implementation owner | Commit / configuration / record reference |
| WP-059-T05 | Add signature checks for tool, MCP and plugin artifacts | Implementation owner | Commit / configuration / record reference |
| WP-059-T06 | Establish revocation behaviour and its impact on running workloads | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Admission policies`
- `Trust root management`
- `CVE/exception workflow`
- `Revocation/impact runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial of an unsigned image
- Denial of a mutable tag
- Denial of provenance from an untrusted builder
- Denial under an expired CVE exception
- An alert on a running workload with a revoked digest
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Production never runs an unsigned artifact.
- [ ] Every exception is time-bound and owned.
- [ ] Revocation produces an impact assessment for open and running workloads.
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

On a policy false positive the previous signed bundle is restored; no permanent manual allowlist bypass is granted for an artifact.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
