# WP-125 — Literature, Zotero and Obsidian Curation Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-125` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Citation Auditor / Knowledge Curator |
| Hard dependencies | WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-073, WP-074, WP-121 |
| Related gates | G3,G10,Day-2 |
| Related controls | CTL-LIT-01, CTL-LIT-02, CTL-LIT-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-125_literature_knowledge_curation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-125_literature_knowledge_curation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Sync conflicts, candidate aging, screening backlog, broken links, source status, annotation promotion and human/generated zone quality are managed continuously under defined SLAs.


## Analysis
### What this package actually decides

That the knowledge base does not rot. Seven ongoing concerns — sync conflicts,
candidate ageing, screening backlog, broken links, source status, annotation
promotion, and zone quality — each with an SLA.

### The Zotero panel is the one with a data-loss path (T01)

Sync lag and conflicts are not cosmetic. A curator who cannot see that the last
sync failed will assume the library is current, and `PR-03`'s early signal is that
divergence is invisible until someone compares.

### Candidate TTL prevents the queue becoming a graveyard (T02)

Agent-discovered candidates that nobody screens accumulate. A TTL forces a decision
— screen it or expire it — and the expiry is recorded so the coverage claim stays
honest.

### The monthly status scan is where `ACC-04` lives in Day-2 (T03)

Retractions and corrections do not stop after commissioning. The scan runs, the
positive control must fire, and the **monitored fraction** must be reported — 15 of
33 sources carry a DOI today, so the scan covers less than half the registry.

### The Obsidian diff check protects the researcher's work (T04)

Human and generated zones diverging, a projection that rewrote something it should
not have, an orphaned note. `scripts/check_vault.py` already runs this in the
verification bundle; this is the cadence that acts on it.

### The quarterly licence and permission review is the compliance half (T05)

Group membership, library permissions and source licences all change without
notice. `PR-14` — source licences violated — is the risk, and a quarterly review is
the control.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

15, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_library_access.md) | `Zotero topology` · `Collection template` · `Credential/permission matrix` · `Library lifecycle SOP` |
| [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md) | `Personal seed adapter` · `Opt-in configuration` · `Sync state/receipts` · `Seed ingest dashboard` |
| [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md) | `Zotero write-back service` · `Field mapping` · `Eligibility policy` · `SyncReceipt ledger` |
| [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md) | `Sync engine` · `Reconciliation queue` · `Full-resync runbook` · `Conflict metrics/dashboard` |
| [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md) | `Annotation ingest service` · `AnnotationObservation records` · `EvidenceCandidate queue` · `Promotion/disposition UI contract` |
| [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md) | `SearchProtocol service` · `LiteratureCampaign workflow` · `Query log` · `Known-item/coverage tests` |
| [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md) | `Dual-loop discovery workflow` · `Discovery provenance` · `Candidate/coverage matrix` · `Counter-evidence log` |
| [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md) | `Screening service` · `Decision queue` · `Reason taxonomy` · `Coverage/flow report` |
| [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md) | `LiteratureSetManifest` · `Signed frozen package` · `Portable exports` · `Zotero frozen view` |
| [WP-073 — Obsidian Vault, Human/Generated Zones and Templates](../07_LITERATURE_KNOWLEDGE/WP-073_obsidian_vault_model.md) | `Obsidian vault baseline` · `Note templates` · `Zone/merge policy` · `Git workflow` |
| [WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/WP-074_obsidian_projection_sync.md) | `Obsidian projection service` · `Link checker` · `Human-preservation diff` · `Concept graph projection` |
| [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md) | `Hypercare log` · `Incident/finding summary` · `Production KPI baseline` · `Day-2 handoff` |

### Full prerequisite closure

**121 of 141 packages (86%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-039` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-048` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-040` · `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-060` · `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |
| 47 | `WP-110` · `WP-111` · `WP-112` · `WP-113` · `WP-114` |
| 48 | `WP-115` |
| 49 | `WP-116` · `WP-117` |
| 50 | `WP-118` |
| 51 | `WP-119` |
| 52 | `WP-120` |
| 53 | `WP-121` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-130`
- **Transitively reachable:** **1 of 141 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W9 — Day-2 |
| Dependency depth | level **54** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Knowledge Lead |
| Independent verifier | Citation Auditor / Knowledge Curator |
| Gates touched | `G3` · `G10` · `Day-2` |
| Controls | `CTL-LIT-01` · `CTL-LIT-02` · `CTL-LIT-03` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-073 — Obsidian Vault, Human/Generated Zones and Templates](../07_LITERATURE_KNOWLEDGE/WP-073_obsidian_vault_model.md), [WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/WP-074_obsidian_projection_sync.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
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
| `Zotero topology` | `WP-064` | `python3 scripts/progress.py show WP-064` |
| `Collection template` | `WP-064` | `python3 scripts/progress.py show WP-064` |
| `Credential/permission matrix` | `WP-064` | `python3 scripts/progress.py show WP-064` |
| `Library lifecycle SOP` | `WP-064` | `python3 scripts/progress.py show WP-064` |
| `Personal seed adapter` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Opt-in configuration` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Sync state/receipts` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Seed ingest dashboard` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Zotero write-back service` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `Field mapping` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `Eligibility policy` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `SyncReceipt ledger` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `Connector tests` | `WP-066` | `python3 scripts/progress.py show WP-066` |
| `Sync engine` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Reconciliation queue` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Full-resync runbook` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Conflict metrics/dashboard` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Annotation ingest service` | `WP-068` | `python3 scripts/progress.py show WP-068` |
| `AnnotationObservation records` | `WP-068` | `python3 scripts/progress.py show WP-068` |
| `EvidenceCandidate queue` | `WP-068` | `python3 scripts/progress.py show WP-068` |
| `Promotion/disposition UI contract` | `WP-068` | `python3 scripts/progress.py show WP-068` |
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
| `Obsidian projection service` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Link checker` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Human-preservation diff` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Concept graph projection` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Rebuild runbook` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Hypercare log` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Incident/finding summary` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Production KPI baseline` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Day-2 handoff` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Program closure report` | `WP-121` | `python3 scripts/progress.py show WP-121` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Knowledge Lead** carries the acceptance decision; **Citation Auditor / Knowledge Curator** must verify independently of whoever implements.
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
| WP-125-T01 | Run the daily sync/conflict/lag check and the weekly curator queue review | Implementation owner | Commit / configuration / record reference |
| WP-125-T02 | Track candidate TTL, used-source promotion and duplicate metrics | Implementation owner | Commit / configuration / record reference |
| WP-125-T03 | Run the monthly status, retraction and broken-link scan | Implementation owner | Commit / configuration / record reference |
| WP-125-T04 | Check the Obsidian human/generated diff and projection integrity | Implementation owner | Commit / configuration / record reference |
| WP-125-T05 | Perform the quarterly library, group, permission and licence review | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Curation calendar`
- `Queue/SLA reports`
- `Library quality scorecard`
- `Knowledge integrity report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-125_literature_knowledge_curation.tests.md`](WP-125_literature_knowledge_curation.tests.md).

- A full resync sample
- Human note preservation
- Broken locator and link repair
- Retraction impact sampling
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-125_literature_knowledge_curation.acceptance.md`](WP-125_literature_knowledge_curation.acceptance.md), together with what this package still cannot establish.

- [ ] Every conflict has a known SLA and owner.
- [ ] Library item count is never treated as a success metric.
- [ ] Used sources target 100% identity, locator and status coverage.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

On a sync or projection problem the connector or renderer is stopped; personal and human-authored data is never overwritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
