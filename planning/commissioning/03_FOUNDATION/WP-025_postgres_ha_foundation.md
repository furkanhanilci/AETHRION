# WP-025 — PostgreSQL HA and Registry Data Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-025` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Database Platform Lead |
| Independent verifier | SRE / Security |
| Hard dependencies | WP-021, WP-020 |
| Related gates | Platform |
| Related controls | CTL-OPS-03, CTL-SEC-03 |
| Related acceptance scenarios | ACC-27 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-025_postgres_ha_foundation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-025_postgres_ha_foundation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

An encrypted, replicated, point-in-time-restorable PostgreSQL foundation is established for the project, source, claim, policy, cost and ledger services.


## Analysis
### What this package actually decides

Whether the canonical record can be lost. Six services — project, source, claim,
policy, cost and ledger — put their system-of-record here, and `00_PROGRAM/01`'s
invariant 6 says derived state can be rebuilt from canonical records. That
invariant has a silent precondition: **the canonical records still exist.**

### Restore is the deliverable; backup is a by-product (T04)

`PR-13` names the failure precisely — *restore exists only on paper*, early signal
*backups present, no rehearsal*. A backup that has never been restored is an
untested claim about the future, and it is the most common single point of
catastrophic failure in systems that otherwise look well run.

The go-live checklist demands **two independent restore rehearsals** and an RPO of
0 for workflow state. This package is where the first of those becomes possible.

### Integrity queries are what make a restore verifiable (T06)

Restoring a database produces a database. Whether it is *the* database is a
different question, and it needs queries defined in advance: row counts per
canonical table, referential closure across the correlation chain, the digest of
a known artifact record. Without them a restore is verified by whether the
service starts.

### Schema ownership belongs here, not in each service (T03)

One migration framework and an owner per schema. Two services migrating the same
table is the canonical-ownership defect `PR-03` describes, expressed in DDL, and
it is discovered during an incident rather than during review.

### Connection pooling has a specific relevance to this repository

Finding **M8**: the running bridge never closes SQLite connections — `with
self.connect()` is a transaction context manager, not a closer, and every request
leaks one until garbage collection. The V0 registry tolerates it. A pooled
PostgreSQL foundation will not, and the pattern must not be carried across.

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
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |

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

- **Directly unblocked:** 19 — `WP-028` · `WP-029` · `WP-030` · `WP-031` · `WP-041` · `WP-042` · `WP-049` · `WP-055` · `WP-061` · `WP-075` · `WP-081` · `WP-082` · `WP-091` · `WP-096` · `WP-097` · `WP-099` · `WP-100` · `WP-101` · `WP-114`
- **Transitively reachable:** **128 of 160 packages (80%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **16** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Database Platform Lead |
| Independent verifier | SRE / Security |
| Gates touched | `Platform` |
| Controls | `CTL-OPS-03` · `CTL-SEC-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-27 — Regional / Management Plane DR](../12_ACCEPTANCE_SCENARIOS/ACC-27_regional_dr.md) | Critical | Temporal workflow state holds at RPO = 0, canonical registries, artifacts and audit records are intact, service returns within the RTO target, and derived views are rebuilt. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
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
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |

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
- **Database Platform Lead** carries the acceptance decision; **SRE / Security** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation acquisition and assimilation

<!-- generated:implementation-sources — produced by scripts/expand_acquisition.py; do not edit inside this block -->

**What is already solved elsewhere, and on what terms.** Before the first task starts, an implementer has to know which parts of this package are called at runtime, which are copied and refactored, which are reimplemented from a specification, and which have no upstream at all. Those decisions are recorded in [`provenance/upstreams.json`](../../../provenance/upstreams.json) — mechanisms assimilated into this repository's own code — and in [`provenance/components.json`](../../../provenance/components.json) — components adopted at runtime. This block is derived from both, so a decision and the place it is used cannot drift apart.

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `CMP-036` — PostgreSQL | `DEPENDENCY` | Relational storage, HA, replication and backup mechanics. | The canonical record model and which registry is the authority for which field — WP-012's field-level authority matrix. | **2** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `CMP-036` | The database stores canonical records; it never decides what is canonical. Two stores holding the same field is a defect in the ownership matrix, not a reconciliation problem to solve at query time. | Application logic in the database, and any derived read model treated as a source of truth. |

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`CMP-036` — PostgreSQL** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 2 obligations open across 1 of 1 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-025-T01 | Choose the HA topology and the failure domains | Implementation owner | Commit / configuration / record reference |
| WP-025-T02 | Bind encryption, TLS, RBAC and workload identity | Implementation owner | Commit / configuration / record reference |
| WP-025-T03 | Establish the migration framework and schema ownership | Implementation owner | Commit / configuration / record reference |
| WP-025-T04 | Prepare PITR backups, retention and a restore environment | Implementation owner | Commit / configuration / record reference |
| WP-025-T05 | Add connection pooling, quotas and slow-query telemetry | Implementation owner | Commit / configuration / record reference |
| WP-025-T06 | Define the RPO/RTO targets and the integrity queries | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `PostgreSQL clusters`
- `DB role matrix`
- `Migration pipeline`
- `Backup/restore configuration`
- `DB SLO dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-025_postgres_ha_foundation.tests.md`](WP-025_postgres_ha_foundation.tests.md).

- A primary failover test
- A PITR restore followed by integrity queries
- A cross-service role-permission negative test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-025_postgres_ha_foundation.acceptance.md`](WP-025_postgres_ha_foundation.acceptance.md), together with what this package still cannot establish.

- [ ] Failover preserves data consistency.
- [ ] A restore meets the target RPO and RTO.
- [ ] No service uses a shared superuser.
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

On a migration failure, apply a forward fix or a verified down migration; irreversible operations are performed through dual-write / expand-contract in two stages.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
