# WP-020 — Schema Registry, Compatibility and Contract SDK

## Package card

| Field | Value |
|---|---|
| Work package | `WP-020` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Architecture Lead |
| Independent verifier | Consumer Service Owners |
| Hard dependencies | WP-011, WP-013, WP-014, WP-015, WP-016, WP-017, WP-018, WP-019 |
| Related gates | Platform |
| Related controls | CTL-OPS-01, CTL-SUP-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Current status | `NOT_STARTED` |

## Adopted component

> **LinkML** — the contract surface is generated from one model rather than hand-written

Generate JSON Schema, Pydantic, JSON-LD, SHACL and SQL DDL from a single LinkML model. This package's failure mode is contracts defined three times in three shapes, which is how the bridge and the contract core came to disagree about digest format.

Rationale and adoption type: `docs/architecture/AIRL_OS_COMPONENT_REUSE.md`.

## Purpose and expected outcome

All canonical contracts are published in a single versioned registry; producer/consumer compatibility and the shared identity and validation SDKs are enforced by CI rather than by review discipline.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-015 — Event Envelope, Subject and Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-020-T01 | Set up the schema repository and its CODEOWNERS ownership | Implementation owner | Commit / configuration / record reference |
| WP-020-T02 | Apply the JSON Schema versus Protobuf choice per bounded context | Implementation owner | Commit / configuration / record reference |
| WP-020-T03 | Write the compatibility checker and the semantic linter | Implementation owner | Commit / configuration / record reference |
| WP-020-T04 | Generate the ID, correlation, policy and artifact helper SDKs | Implementation owner | Commit / configuration / record reference |
| WP-020-T05 | Publish the fixture set and the contract-test harness | Implementation owner | Commit / configuration / record reference |
| WP-020-T06 | Define the deprecation and migration process | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Schema Registry v1`
- `Generated SDKs`
- `Compatibility CI`
- `Contract fixture catalog`
- `Deprecation policy`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Validate every schema against its fixtures
- A negative CI run on a deliberate breaking change
- Old-consumer/new-producer and new-consumer/old-producer contract tests
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No canonical schema exists outside the registry.
- [ ] A breaking change cannot merge without a major version and an adapter.
- [ ] The generated SDKs produce identical semantics across target languages.
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

A faulty schema release is not yanked; a new patch version is published and the registry pointer returns to the last verified bundle.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
