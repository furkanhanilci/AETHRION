# WP-019 — Run, Environment and Reproduction Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-019` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Hard dependencies | WP-011, WP-014, WP-018 |
| Related gates | G4–G7 |
| Related controls | CTL-DAT-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-19, ACC-20 |
| Current status | `NOT_STARTED` |

## Purpose and expected outcome

Experiment and verification runs are fully manifested with dataset, code, environment, prompt, model snapshot, seed, metric and tolerance. A run whose manifest is incomplete can never support a confirmatory claim.

## Out of scope


- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-019-T01 | Write the `RunManifest` input, output and lineage fields | Implementation owner | Commit / configuration / record reference |
| WP-019-T02 | Make the protocol, baseline and analysis-plan references mandatory | Implementation owner | Commit / configuration / record reference |
| WP-019-T03 | Add the `EnvironmentManifest` hardware, driver, image and SBOM fields | Implementation owner | Commit / configuration / record reference |
| WP-019-T04 | Separate repeatability, reproducibility, robustness and replication as distinct types | Implementation owner | Commit / configuration / record reference |
| WP-019-T05 | Write the `ReproductionReport` tolerance and root-cause schema | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Run schema bundle`
- `EnvironmentManifest`
- `ReproductionReport`
- `Tolerance policy examples`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Negative tests for a missing seed, model or image hash
- A determinism fixture running the same manifest twice
- A test detecting a mislabelled reproduction type
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] A run records the version of every frozen input.
- [ ] A reproduction result carries pass/fail **and** the tolerance rationale.
- [ ] Replication is never substituted for reproduction, nor the reverse.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

A run with an incomplete manifest stays `INVALID` or `EXPLORATORY`; it is not promoted to a publication or a critical claim.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
