# WP-081 — Protocol, Analysis, Baseline and Falsification Registry

## Package card

| Field | Value |
|---|---|
| Work package | `WP-081` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Method Office Lead |
| Independent verifier | Statistician / Falsification Lead |
| Hard dependencies | WP-008, WP-014, WP-019, WP-025, WP-026, WP-035, WP-075 |
| Related gates | G2,G4,G5 |
| Related controls | CTL-EPI-02, CTL-DAT-01 |
| Related acceptance scenarios | ACC-39 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

`ProtocolManifest`, `AnalysisPlan`, `BaselineBundle` and `FalsificationPlan` are held in a canonical registry with freeze/amendment, owner, hash and gate references.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-081-T01 | Establish the registry data model, API and outbox events | Implementation owner | Commit / configuration / record reference |
| WP-081-T02 | Write validation for variables, outcomes, controls, sample and stop rules | Implementation owner | Commit / configuration / record reference |
| WP-081-T03 | Make the baseline, null, counter-test and leakage fields mandatory | Implementation owner | Commit / configuration / record reference |
| WP-081-T04 | Apply the freeze/signature and amendment/supersession lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-081-T05 | Add run and claim linkage plus a post-hoc change detector | Implementation owner | Commit / configuration / record reference |
| WP-081-T06 | Bind the review and approval workflow API | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Method Registry`
- `Protocol validators`
- `Amendment workflow`
- `Post-hoc change detector`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Failure when a stop rule is missing
- Denial of a post-result baseline edit
- A protocol amendment preserving the older runs
- A leakage detector fixture
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No G5 run opens without a frozen protocol hash.
- [ ] Any post-hoc change is a visible amendment.
- [ ] Negative results and stop rules are preserved rather than quietly dropped.
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

A wrong protocol version is marked `INVALIDATED`; dependent runs and claims receive an impact assessment and the old artifacts remain.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
