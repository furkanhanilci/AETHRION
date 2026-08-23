---
title: "WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models"
aliases:
  - "WP-030"
  - "WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "The provenance graph, semantic retrieval and full-text indexes become read models that can be rebuilt from scratch out of canonical events and records."
source: "planning/commissioning/03_FOUNDATION/WP-030_derived_read_models.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models

## Package card

| Field | Value |
|---|---|
| Work package | `WP-030` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Data Lead |
| Independent verifier | Data Platform Lead / Assurance |
| Hard dependencies | WP-012, WP-017, WP-018, WP-025, WP-026, WP-028 |
| Related gates | Platform,G10 |
| Related controls | CTL-OPS-03, CTL-OBS-01 |
| Related acceptance scenarios | ACC-21 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_030_derived_read_models.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_030_derived_read_models.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The provenance graph, semantic retrieval and full-text indexes become read models that can be rebuilt from scratch out of canonical events and records.


## Analysis
### What this package actually decides

That every index is disposable. Graph, vector and search are **read models**, and
the test of a read model is that you can delete it and rebuild it from canonical
records — `00_PROGRAM/01`'s success invariant 6, stated as an operation rather
than a principle.

The consequence is sharper than it sounds: **anything that cannot be rebuilt is
canonical**, whether or not the ownership matrix says so. This package is where
WP-012's matrix gets falsified rather than agreed with.

### The embedding model is part of the index identity (T03)

A vector index built with one embedding model and queried with another returns
plausible nonsense — the distances are computed in different spaces. Recording the
model and its version *in the index metadata* is what makes a mismatch detectable
instead of a slow degradation nobody attributes to anything.

This is the same class as WP-019's model-pinning problem and has the same shape:
the artifact must carry what produced it.

### Projection lag is a correctness property, not a performance metric (T05)

A cockpit reading a projection that is four hours behind shows a state that is not
current, and the human decides against it. Lag telemetry with a threshold is what
turns that from an invisible staleness into an alert — and the checkpoint is what
lets the projection resume rather than restart.

### The index swap is the part that makes a rebuild safe (T06)

Rebuilding in place means the index is wrong for the whole rebuild window. Build
beside, verify, swap — and keep the previous index until the swap is confirmed.
Without it, a rebuild is an outage with extra steps.

### Retention and data class apply to derived state too (T04)

A search index over D3 content is D3 content, however it was derived. Indexes are
routinely exempted from classification because they feel like metadata, and they
are the most queryable copy of the data in the system.

### Baseline v1.3.0 — modular monolith first, and a projection that can be destroyed

The collaboration plane, the conformance checker and the release assurance work
land as **modules**, not as services. A logical plane is an ownership boundary;
turning each into a deployment unit before there is a consumer buys operational
cost and no assurance.

Two guarantees the foundation now owes:

**Every derived projection is destroyable.** The graph, the vector index and the
search index are rebuilt from canonical stores as a routine, tested operation —
ACC-119. A rebuild path that is an emergency procedure will not work on the day
it is needed.

**Release artifacts carry provenance.** SLSA provenance, Sigstore signatures, an
SBOM and its scan result, and the upstream register accounting for every adapted
file. `ADR-019`, delivered by WP-159 and admitted against by WP-024's CI.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |

### Full prerequisite closure

**24 of 160 packages (15%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-025` · `WP-026` |
| 17 | `WP-028` |

### What acceptance of this package releases

- **Directly unblocked:** 10 — `WP-074` · `WP-075` · `WP-091` · `WP-095` · `WP-098` · `WP-114` · `WP-130` · `WP-143` · `WP-144` · `WP-146`
- **Transitively reachable:** **76 of 160 packages (48%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **18** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Knowledge Data Lead |
| Independent verifier | Data Platform Lead / Assurance |
| Gates touched | `Platform` · `G10` |
| Controls | `CTL-OPS-03` · `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-21 — Derived Graph Corruption and Rebuild](../12_ACCEPTANCE_SCENARIOS/acc_21_graph_corruption.md) | High | Canonical services are unaffected; a new projection is built with the expected counts, hashes and lineage and promoted atomically. |
| [ACC-71 — Multi-Parent Artifact Lineage](../12_ACCEPTANCE_SCENARIOS/acc_71_artifact_multi_parent_lineage.md) | Critical | Parent identity, parent order and every digest are identical across all three operations. A lineage that survives export but not a rebuild is not lineage. |
| [ACC-119 — Destructive Projection Rebuild](../12_ACCEPTANCE_SCENARIOS/acc_119_derived_projection_destructive_rebuild.md) | Critical | The rebuild is lossless. No injection produces a silent divergence: each ends with canonical state correct and the projection agreeing, or with an explicit recorded failure. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md)
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
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `NATS cluster` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Outbox relay` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Consumer SDK` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `DLQ/replay runbook` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Event dashboards` | `WP-028` | `python3 scripts/progress.py show WP-028` |

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
- **Knowledge Data Lead** carries the acceptance decision; **Data Platform Lead / Assurance** must verify independently of whoever implements.
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
| WP-030-T01 | Define the projection schemas and their source events | Implementation owner | Commit / configuration / record reference |
| WP-030-T02 | Build the Neo4j claim/source/run/review graph projection | Implementation owner | Commit / configuration / record reference |
| WP-030-T03 | Add the embedding model and version metadata to pgvector | Implementation owner | Commit / configuration / record reference |
| WP-030-T04 | Establish the OpenSearch index, retention and data-class policy | Implementation owner | Commit / configuration / record reference |
| WP-030-T05 | Add projection checkpoints and lag telemetry | Implementation owner | Commit / configuration / record reference |
| WP-030-T06 | Write the full rebuild and index-swap procedure | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Projection services`
- `Graph/vector/search indexes`
- `Rebuild jobs`
- `Integrity/lag dashboard`
- `Destructive projection rebuild proof`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-030_derived_read_models.tests.md`](wp_030_derived_read_models.tests.md).

- Canonical → projection count and hash reconciliation
- A full rebuild after deliberate graph corruption
- A reindex test following an embedding model change
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-030_derived_read_models.acceptance.md`](wp_030_derived_read_models.acceptance.md), together with what this package still cannot establish.

- [ ] No derived store accepts a canonical write.
- [ ] A projection can be deleted and rebuilt.
- [ ] Data class, deletion and legal-hold propagate into the projection.
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

A corrupted index is rebuilt in a new namespace; once verified, the alias is switched atomically.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
