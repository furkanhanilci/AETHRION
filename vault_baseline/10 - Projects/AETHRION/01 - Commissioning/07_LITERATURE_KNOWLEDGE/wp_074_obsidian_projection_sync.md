---
title: "WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back"
aliases:
  - "WP-074"
  - "WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Source, claim, run and decision changes update only the generated zones; human synthesis links are checked, and the concept graph is a derived projection that can be rebuilt."
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-074_obsidian_projection_sync.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back

## Package card

| Field | Value |
|---|---|
| Work package | `WP-074` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Knowledge Curator / Data Platform Lead |
| Hard dependencies | WP-028, WP-030, WP-061, WP-072, WP-073 |
| Related gates | G8,G9,G10 |
| Related controls | CTL-OPS-03, CTL-EPI-01 |
| Related acceptance scenarios | ACC-21, ACC-22, ACC-31 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_074_obsidian_projection_sync.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_074_obsidian_projection_sync.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Source, claim, run and decision changes update only the generated zones; human synthesis links are checked, and the concept graph is a derived projection that can be rebuilt.


## Analysis
### What this package actually decides

How the repository reaches the vault without ever destroying human work. This is
the package that owns the most dangerous operation in the system, and the running
implementation already carries its scar tissue.

### The hazard is documented and has actually happened

`AGENTS.md` §10 records it: `mirror_plan.py` **replaces its target directory**, and
pointed at a vault root instead of the commissioning subtree it *deleted the whole
vault*. The guard that exists now — refusing any target holding files it does not
generate — was added after that.

The projection has the same shape and a different guard: `obsidian.py` deletes only
files listed in `.airl-projection-manifest.json`, which is why a human note dropped
into the generated folder survives.

Both guards are the package's real content.

### `M9` before `H1`, and this is where M9 lives

`src/airl_bridge/service.py` states the ordering:

> `project_obsidian` reads at most 10,000 sources. Above that the projection would
> not see some sources and `_remove_stale` would then delete their files as stale.
> The 100-record ingest cap (finding **H1**) masks this today; **fix M9 before
> fixing H1**, or the H1 fix opens an active data-loss path.

So WP-074 gates WP-065. Paginating ingest before this package removes the
projection cap converts a masked truncation into deletion of a researcher's files.

### Event-driven rendering, not polling (T01)

A projection that re-renders everything on a timer produces churn; one driven by
change events renders what changed. The repository already learned the churn
lesson: an earlier projection stamped `generated_at` from the wall clock and
rewrote all 36 vault files every 30 minutes while reporting `unchanged: 33`.

The fix was to derive the timestamp from the registry, and the property to preserve
is: **unchanged input, byte-identical output**.

### Three-way zone merge (T03)

Human zone, generated zone, and what the generator now wants to write. A two-way
merge cannot tell a human edit from a stale generation, and will pick wrong.

### Full rebuild is the falsification test (T06)

Delete every generated file and rebuild. Anything that does not come back was
never generated — it was somebody's work living in a generated area, and the
matrix that said otherwise is wrong.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md) | `NATS cluster` · `Outbox relay` · `Consumer SDK` · `DLQ/replay runbook` |
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md) | `LiteratureSetManifest` · `Signed frozen package` · `Portable exports` · `Zotero frozen view` |
| [WP-073 — Obsidian Vault, Human/Generated Zones and Templates](../07_LITERATURE_KNOWLEDGE/wp_073_obsidian_vault_model.md) | `Obsidian vault baseline` · `Note templates` · `Zone/merge policy` · `Git workflow` |

### Full prerequisite closure

**65 of 141 packages (46%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` |
| 28 | `WP-062` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-071` |
| 32 | `WP-072` |
| 33 | `WP-073` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-106` · `WP-125`
- **Transitively reachable:** **24 of 141 packages (17%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **34** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Knowledge Curator / Data Platform Lead |
| Gates touched | `G8` · `G9` · `G10` |
| Controls | `CTL-OPS-03` · `CTL-EPI-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-21 — Derived Graph Corruption and Rebuild](../12_ACCEPTANCE_SCENARIOS/acc_21_graph_corruption.md) | High | Canonical services are unaffected; a new projection is built with the expected counts, hashes and lineage and promoted atomically. |
| [ACC-22 — Obsidian Human Edit Preservation](../12_ACCEPTANCE_SCENARIOS/acc_22_obsidian_human_edit.md) | High | The human field is preserved byte- and semantically; only the generated zone updates, and an unexpected conflict opens a curator case instead of an automatic overwrite. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-028 — NATS JetStream and Transactional Outbox Foundation](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md), [WP-073 — Obsidian Vault, Human/Generated Zones and Templates](../07_LITERATURE_KNOWLEDGE/wp_073_obsidian_vault_model.md)
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
| `NATS cluster` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Outbox relay` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Consumer SDK` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `DLQ/replay runbook` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Event dashboards` | `WP-028` | `python3 scripts/progress.py show WP-028` |
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `LiteratureSetManifest` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Signed frozen package` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Portable exports` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Zotero frozen view` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Freeze/diff report` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Obsidian vault baseline` | `WP-073` | `python3 scripts/progress.py show WP-073` |
| `Note templates` | `WP-073` | `python3 scripts/progress.py show WP-073` |
| `Zone/merge policy` | `WP-073` | `python3 scripts/progress.py show WP-073` |
| `Git workflow` | `WP-073` | `python3 scripts/progress.py show WP-073` |
| `User guide` | `WP-073` | `python3 scripts/progress.py show WP-073` |

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
- **Knowledge Platform Lead** carries the acceptance decision; **Knowledge Curator / Data Platform Lead** must verify independently of whoever implements.
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
| WP-074-T01 | Write the event-driven generated-block renderer | Implementation owner | Commit / configuration / record reference |
| WP-074-T02 | Establish the AIRL ID link resolver and backlink index | Implementation owner | Commit / configuration / record reference |
| WP-074-T03 | Apply human-edit detection and three-way zone merge | Implementation owner | Commit / configuration / record reference |
| WP-074-T04 | Add the broken/orphan link report and the curator queue | Implementation owner | Commit / configuration / record reference |
| WP-074-T05 | Bind concept and entity edge extraction to the derived graph | Implementation owner | Commit / configuration / record reference |
| WP-074-T06 | Write the full vault projection rebuild procedure | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Obsidian projection service`
- `Link checker`
- `Human-preservation diff`
- `Concept graph projection`
- `Rebuild runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-074_obsidian_projection_sync.tests.md`](wp_074_obsidian_projection_sync.tests.md).

- A human edit arriving during a generated refresh
- A broken source or claim link
- A full projection rebuild
- A superseded-claim banner update
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-074_obsidian_projection_sync.acceptance.md`](wp_074_obsidian_projection_sync.acceptance.md), together with what this package still cannot establish.

- [ ] The renderer cannot write into a human zone.
- [ ] A broken material link can block G9.
- [ ] Loss of the derived graph is not loss of the vault or of canonical records.
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

- Identity errors in sources propagate into every claim that cites them.
- A write into a shared library without a version precondition can silently destroy a human edit.
- A literature set that is not frozen cannot support a reproducible claim.

## Rollback / compensation

The projection is rebuilt on a new branch and merged after a diff review; conflicts go to the curator queue rather than being auto-resolved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
