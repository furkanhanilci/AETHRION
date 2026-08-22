# WP-082 — Run Registry and MLflow Lineage Integration

## Package card

| Field | Value |
|---|---|
| Work package | `WP-082` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Hard dependencies | WP-014, WP-019, WP-025, WP-026, WP-029, WP-032, WP-081 |
| Related gates | G4,G5 |
| Related controls | CTL-DAT-01, CTL-CST-01 |
| Related acceptance scenarios | ACC-39 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Workflow Run RO-Crate** for provenance · **MLflow + OpenTelemetry** for telemetry

The run record is emitted as a Process/Workflow/Provenance Run Crate — machine-actionable, engine-independent, PROV-O mapped. MLflow answers *what did the system do*; the crate plus a signed `EvidenceManifest` answers *what may be believed*. **Operational telemetry is never the scientific truth store.**

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Purpose and expected outcome

A run is not admitted until the protocol, literature set, dataset, code, environment, prompt, model, seed, budget and execution attestation are complete; MLflow is only the tracking view.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/WP-025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-029 — MLflow Experiment and Evaluation Tracking Foundation](../03_FOUNDATION/WP-029_mlflow_foundation.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-082-T01 | Establish the Run Registry state model and API | Implementation owner | Commit / configuration / record reference |
| WP-082-T02 | Write the pre-run manifest completeness and admission checks | Implementation owner | Commit / configuration / record reference |
| WP-082-T03 | Bind Temporal, execution and MLflow correlation | Implementation owner | Commit / configuration / record reference |
| WP-082-T04 | Add metric, artifact and result ingestion with hash validation | Implementation owner | Commit / configuration / record reference |
| WP-082-T05 | Define the failed, cancelled and negative run lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-082-T06 | Add run comparison, query APIs and outbox events | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Run Registry`
- `Preflight validator`
- `MLflow integration`
- `Run lineage queries`
- `Run lifecycle dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

- Denial when a dataset, image or model reference is missing
- End-to-end run identifier correlation
- A failed run whose artifacts are retained
- Queued ingest during an MLflow outage
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

- [ ] No run starts with incomplete metadata.
- [ ] MLflow never owns canonical workflow or artifact state.
- [ ] A negative result is a first-class run outcome.
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

A tracking failure does not lose execution evidence; an idempotent backfill runs and no invalid run is published.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
