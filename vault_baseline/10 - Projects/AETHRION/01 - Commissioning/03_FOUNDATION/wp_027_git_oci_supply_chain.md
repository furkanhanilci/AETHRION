# WP-027 — Git, OCI Registry and Build Provenance Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-027` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Supply Chain Security Lead |
| Independent verifier | Security Reviewer / SRE |
| Hard dependencies | WP-021, WP-022, WP-024, WP-026 |
| Related gates | G5,Platform |
| Related controls | CTL-SEC-05, CTL-SUP-01 |
| Related acceptance scenarios | ACC-17 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

The chain from source commit to a digest-pinned OCI image is established, covering SBOM, provenance, signature, vulnerability status and promotion.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/wp_024_ci_quality_gates.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-027-T01 | Set up the OCI registry environment and repository structure | Implementation owner | Commit / configuration / record reference |
| WP-027-T02 | Produce reproducible builds and provenance metadata | Implementation owner | Commit / configuration / record reference |
| WP-027-T03 | Add SBOM generation and vulnerability scanning | Implementation owner | Commit / configuration / record reference |
| WP-027-T04 | Bind the Sigstore keyless or key policy | Implementation owner | Commit / configuration / record reference |
| WP-027-T05 | Prohibit the use of mutable tags | Implementation owner | Commit / configuration / record reference |
| WP-027-T06 | Establish the dev → staging → prod digest promotion flow | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `OCI registry`
- `Build/promotion pipeline`
- `SBOM/provenance artifacts`
- `Signature policy seed`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- A negative promotion test with an unsigned image
- An admission fixture rejecting a mutable tag
- A reproducible-build comparison from the same commit
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] Production runs only signed digests.
- [ ] Every build artifact is bound to a source commit and a dependency lock.
- [ ] A critical vulnerability does not promote without an explicit policy decision.
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

- Infrastructure built by hand once is infrastructure that cannot be rebuilt under pressure.
- A backup that has never been restored is not a backup.
- Environment parity erodes from the staging side first, and quietly.

## Rollback / compensation

A compromised digest is revoked and quarantined; the previous signed image is restored and an impact scan is performed.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
