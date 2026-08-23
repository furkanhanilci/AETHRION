# WP-026 — Content-Addressed Object Store and WORM

## Package card

| Field | Value |
|---|---|
| Work package | `WP-026` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Platform Lead |
| Independent verifier | Archivist / Security |
| Hard dependencies | WP-021, WP-014 |
| Related gates | G3–G10 |
| Related controls | CTL-DAT-03, CTL-SUP-01 |
| Related acceptance scenarios | ACC-23, ACC-27 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Object-lock / WORM backend** — integrate and verify, do not build

The requirement is compliance-mode retention that no account, including root, can delete. AETHRION owns the `ImmutableObjectStore` contract and the verification that the backend actually refuses deletion; it does not own the storage engine. `lakeFS`-style versioning covers *working* data, which is a different problem.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-026_object_store_worm.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-026_object_store_worm.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

PDF, dataset, artifact, evidence and publication bytes are stored immutably under a content hash, with object lock, encryption, retention and legal-hold.


## Analysis
### What this package actually decides

Where "immutable" stops being a design intention and becomes a storage
configuration. WP-014 defines what an immutable artifact *is*; this package is the
object lock that makes overwriting impossible rather than merely forbidden.

The distinction is the whole point of `PR-08` — *different bytes at the same URI*
— and it is rated critical because the failure is silent: every claim citing the
artifact stays valid-looking, and nothing indicates that what it cited has changed.

### This is the package the whole programme was deadlocked on

`00_PROGRAM/05` records it: the Definition of Done requires a signed manifest in
an immutable store, that store is WP-026, and WP-026 sits ten dependency levels
below WP-001 — so **no package could ever be accepted, including the first**. That
is audit finding **C1**, and WP-000 exists only to make the programme startable
until this package lands.

So WP-026's acceptance has an obligation no other package has: **it must retire
WP-000's interim profile.** `airl-interim-v0.1` is a local key, a local clock and
one operator holding the repository, the key, the generator and the anchor. Once
this store exists, keeping the interim profile is a choice rather than a
constraint, and the migration path is part of this package's deliverable set.

### Three areas, and the one that is easy to skip (T05)

Quarantine, canonical, publication. The quarantine area is where untrusted
content lands before anything trusts it — ADR-003's data plane given a bucket.
Without it, a fetched PDF goes straight into the canonical store and the boundary
exists only in the code path that happened to be taken.

### The bit-rot scan is what makes the store's claim checkable over time (T06)

Object lock prevents deliberate overwrite. It does not prevent silent corruption,
and a store nobody re-hashes is a store whose integrity claim ages without being
tested. The scan is cheap and its absence is invisible until a restore fails.

### Baseline v1.3.0 — new record classes, no new database

**No new storage technology.** What changes is the schema and retention surface:

- the canonical records this baseline adds, in PostgreSQL;
- **immutable evaluator outputs and model execution fingerprints** in the object
  store, under WORM retention — a fingerprint that can be edited is not a
  fingerprint;
- retention classes for the collaboration plane, which is deliberately *not*
  permanent: a blackboard entry expires, and `ADR-013` requires that expiry to
  lose nothing canonical.

Migration tests cover every new record, including the round trip that proves a
restore reproduces it exactly.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |

### Full prerequisite closure

**21 of 160 packages (13%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` |

### What acceptance of this package releases

- **Directly unblocked:** 24 — `WP-027` · `WP-029` · `WP-030` · `WP-031` · `WP-049` · `WP-058` · `WP-061` · `WP-063` · `WP-072` · `WP-075` · `WP-076` · `WP-081` · `WP-082` · `WP-084` · `WP-086` · `WP-087` · `WP-090` · `WP-097` · `WP-099` · `WP-101` · `WP-114` · `WP-139` · `WP-146` · `WP-158`
- **Transitively reachable:** **129 of 160 packages (81%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **16** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Data Platform Lead |
| Independent verifier | Archivist / Security |
| Gates touched | `G3–G10` |
| Controls | `CTL-DAT-03` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-23 — Artifact Overwrite Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-23_artifact_overwrite.md) | Critical | The overwrite is rejected; the new bytes can only be written as a new content address and version, and existing references are unchanged. |
| [ACC-27 — Regional / Management Plane DR](../12_ACCEPTANCE_SCENARIOS/ACC-27_regional_dr.md) | Critical | Temporal workflow state holds at RPO = 0, canonical registries, artifacts and audit records are intact, service returns within the RTO target, and derived views are rebuilt. |
| [ACC-71 — Multi-Parent Artifact Lineage](../12_ACCEPTANCE_SCENARIOS/ACC-71_artifact_multi_parent_lineage.md) | Critical | Parent identity, parent order and every digest are identical across all three operations. A lineage that survives export but not a rebuild is not lineage. |
| [ACC-78 — Raw Evidence Versus Interpretation](../12_ACCEPTANCE_SCENARIOS/ACC-78_raw_evidence_versus_interpretation.md) | Critical | The finding gains a new version; every raw artifact's bytes and digest are unchanged. The direct raw edit is refused. Interpretation is revisable; evidence is not. |
| [ACC-79 — Epistemic Memory Retention Violation](../12_ACCEPTANCE_SCENARIOS/ACC-79_memory_retention_violation.md) | High | It excludes the immutable classes, reports exactly what it excluded and why, and expires only procedural entries. A planted evidence control survives, and a planted stale procedure does not. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Environment topology` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Account/network IaC` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Access baseline` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Environment promotion policy` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Data Platform Lead** carries the acceptance decision; **Archivist / Security** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-026-T01 | Establish the bucket/namespace layout and the data-class separation | Implementation owner | Commit / configuration / record reference |
| WP-026-T02 | Apply content-addressed keys and multipart hash verification | Implementation owner | Commit / configuration / record reference |
| WP-026-T03 | Enable object lock/WORM and the retention policy | Implementation owner | Commit / configuration / record reference |
| WP-026-T04 | Bind the encryption keys and access logging | Implementation owner | Commit / configuration / record reference |
| WP-026-T05 | Separate the quarantine, canonical and publication areas | Implementation owner | Commit / configuration / record reference |
| WP-026-T06 | Set up replication, restore and a bit-rot scan | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Object storage IaC`
- `Object address service`
- `Retention matrix`
- `Integrity scan job`
- `Restore procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-026_object_store_worm.tests.md`](WP-026_object_store_worm.tests.md).

- A denial test for overwriting the same key
- Hash detection of a corrupted byte range
- A cross-region restore and legal-hold test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-026_object_store_worm.acceptance.md`](WP-026_object_store_worm.acceptance.md), together with what this package still cannot establish.

- [ ] A canonical object cannot be overwritten.
- [ ] Every object is bound to an `ArtifactRecord` and its hash.
- [ ] A retention deletion policy does not execute without an owner approval.
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

A corrupt replica is repaired from a good hash; the restore produces a new physical object and the canonical reference is re-verified.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
