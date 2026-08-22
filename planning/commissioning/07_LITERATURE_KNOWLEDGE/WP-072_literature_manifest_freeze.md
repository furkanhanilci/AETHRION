# WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive

## Package card

| Field | Value |
|---|---|
| Work package | `WP-072` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Citation Auditor / Archivist |
| Hard dependencies | WP-014, WP-017, WP-026, WP-061, WP-062, WP-063, WP-067, WP-069, WP-070, WP-071 |
| Related gates | G3,G9,G10 |
| Related controls | CTL-EPI-01, CTL-LIT-01 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-04, ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-072_literature_manifest_freeze.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-072_literature_manifest_freeze.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Included and excluded sources, representation hashes, queries, screening decisions, status and actors become an immutable `LiteratureSetManifest`; the Zotero `90_Frozen_View` is only its mirror.


## Analysis
### What this package actually decides

The moment a literature set stops moving. A `LiteratureSetManifest` is written
immutably, and everything downstream — every claim, every review, every
publication — cites **the manifest**, not the registry.

### Why the freeze has to be an object, not a timestamp

A query against the registry "as of" a date depends on the registry's history being
perfect and its semantics never changing. A serialised, hashed, object-locked
manifest depends on nothing. `00_PROGRAM/01` names it: *`LiteratureSetManifest` is
written to an immutable object store as a Source Registry snapshot; a Zotero
collection is a human-readable mirror only.*

### Deterministic serialisation is what makes the hash mean something (T01)

Two serialisations of the same set must produce the same bytes. Key ordering,
number formatting, unicode normalisation — each is a way for an identical set to
hash differently, and a manifest whose digest depends on serialisation order cannot
be compared to itself.

### Excluded sources belong in the manifest (T02)

A set that records only what was included cannot be audited: a reader cannot tell
whether a source was never found or found and rejected. Both, with reason codes,
plus the queries and the screening decisions that produced them.

### The status field is what lets a retraction reach through the freeze (T02)

The manifest is immutable; the **status** of a source in it is not. WP-063 writes
retraction status against the source, and the manifest resolves it at read time —
so a frozen set shows *this source was included, and it has since been retracted*
without the set being mutated.

That is the loop closing, and it only works if the manifest stores identity plus
representation hash rather than a copy of the metadata.

### Diff and invalidation (T06)

A new manifest version is a new set. Anything synthesised from the old one is not
automatically valid against the new one, and the invalidation has to be explicit —
otherwise a set update silently changes what a published claim rests on.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

10, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md) | `Sync engine` · `Reconciliation queue` · `Full-resync runbook` · `Conflict metrics/dashboard` |
| [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md) | `SearchProtocol service` · `LiteratureCampaign workflow` · `Query log` · `Known-item/coverage tests` |
| [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md) | `Dual-loop discovery workflow` · `Discovery provenance` · `Candidate/coverage matrix` · `Counter-evidence log` |
| [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md) | `Screening service` · `Decision queue` · `Reason taxonomy` · `Coverage/flow report` |

### Full prerequisite closure

**62 of 141 packages (44%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-042` |
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

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-073` · `WP-074` · `WP-080` · `WP-090` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **42 of 141 packages (30%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **32** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Lead |
| Independent verifier | Citation Auditor / Archivist |
| Gates touched | `G3` · `G9` · `G10` |
| Controls | `CTL-EPI-01` · `CTL-LIT-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/ACC-01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-02 — Agent-Used Source Write-Back](../12_ACCEPTANCE_SCENARIOS/ACC-02_agent_used_source_writeback.md) | Critical | The source is written idempotently **only** into `40_Used` and the relevant project collection of the correct AIRL group library; the registry binding and a receipt are created. |
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/ACC-04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md)
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
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Source Resolver service` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Match rules/features` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Conflict queue` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Known-item/dedup test corpus` | `WP-062` | `python3 scripts/progress.py show WP-062` |
| `Representation ingest service` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `License/status policy` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Status monitor` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Format locator metadata` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Retention mapping` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Sync engine` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Reconciliation queue` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Full-resync runbook` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Conflict metrics/dashboard` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `SearchProtocol service` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `LiteratureCampaign workflow` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Query log` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Known-item/coverage tests` | `WP-069` | `python3 scripts/progress.py show WP-069` |
| `Dual-loop discovery workflow` | `WP-070` | `python3 scripts/progress.py show WP-070` |
| `Discovery provenance` | `WP-070` | `python3 scripts/progress.py show WP-070` |
| `Candidate/coverage matrix` | `WP-070` | `python3 scripts/progress.py show WP-070` |
| `Counter-evidence log` | `WP-070` | `python3 scripts/progress.py show WP-070` |
| `Screening service` | `WP-071` | `python3 scripts/progress.py show WP-071` |
| `Decision queue` | `WP-071` | `python3 scripts/progress.py show WP-071` |
| `Reason taxonomy` | `WP-071` | `python3 scripts/progress.py show WP-071` |
| `Coverage/flow report` | `WP-071` | `python3 scripts/progress.py show WP-071` |
| `Screening calibration set` | `WP-071` | `python3 scripts/progress.py show WP-071` |

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
- **Evidence Lead** carries the acceptance decision; **Citation Auditor / Archivist** must verify independently of whoever implements.
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
| WP-072-T01 | Write the manifest snapshot query and a deterministic serialiser | Implementation owner | Commit / configuration / record reference |
| WP-072-T02 | Add the included, excluded, query, screening, status and licence references | Implementation owner | Commit / configuration / record reference |
| WP-072-T03 | Apply hashing, signature and an object-lock write | Implementation owner | Commit / configuration / record reference |
| WP-072-T04 | Produce portable CSL-JSON, BibTeX and RIS exports | Implementation owner | Commit / configuration / record reference |
| WP-072-T05 | Perform the selective sync into the Zotero `90_Frozen_View` | Implementation owner | Commit / configuration / record reference |
| WP-072-T06 | Establish manifest diff, new-version and synthesis invalidation | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `LiteratureSetManifest`
- `Signed frozen package`
- `Portable exports`
- `Zotero frozen view`
- `Freeze/diff report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-072_literature_manifest_freeze.tests.md`](WP-072_literature_manifest_freeze.tests.md).

- The same inputs producing the same manifest hash
- A new source creating a v2 rather than mutating v1
- An edit in the Zotero frozen view leaving the manifest unchanged
- A hard fail on a missing locator or status
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-072_literature_manifest_freeze.acceptance.md`](WP-072_literature_manifest_freeze.acceptance.md), together with what this package still cannot establish.

- [ ] The manifest is a snapshot of the Source Registry.
- [ ] The Zotero archive is a convenience view, never the evidence itself.
- [ ] Older sets and their representations remain reachable.
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

An incomplete or incorrect manifest is marked `INVALIDATED` and a corrected new version is produced; the links from earlier claims and runs are preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
