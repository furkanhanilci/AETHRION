# WP-094 — Literature Workbench and Reconciliation UI

## Package card

| Field | Value |
|---|---|
| Work package | `WP-094` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Product Lead |
| Independent verifier | Knowledge Curator / Citation Auditor |
| Hard dependencies | WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-091 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01, CTL-LIT-02, CTL-LIT-03 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-03, ACC-04, ACC-28 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-094_literature_workbench.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-094_literature_workbench.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Researchers and curators manage seeds, candidates, resolver conflicts, screening, trust, annotation promotion, set freezing and status impact on one working surface.


## Analysis
### What this package actually decides

Where a curator does the work the literature workstream generates. Seven queues
feed this surface — candidates, resolver conflicts, screening, trust, annotation
promotion, Zotero conflicts, status impact — and the design decision is that each
one has a **visible depth and a terminal state**.

A queue nobody can see the bottom of is a queue nobody works.

### The coverage dashboard must publish what is *not* covered (T01)

WP-063 records the number: 15 of 33 registry sources carry a DOI, so the Crossref
sweep monitors 45% of them. A dashboard showing *0 retractions found* without
showing that fraction reports clean for the same reason a monitor covering nothing
would.

### The reconciliation screen is where a false merge is prevented (T03)

WP-062 sends ambiguity here rather than deciding. The screen has to show **both
candidates side by side with the features that produced the match**, because the
curator's job is to reject a merge the resolver was tempted by — and `ACC-03` is
the scenario.

### Screening is where independence costs least (T04)

Blind assignment, both decisions visible only after both are in, disagreements
routed rather than reconciled by whoever looks second (WP-071).

### Annotation promotion is the boundary crossing (T05)

An `AnnotationObservation` becoming an `EvidenceCandidate` is where a reader's
highlight starts to license a claim. The promotion needs the actor, the reason, and
the locator state (WP-076) visible at the moment of promotion — promoting a span in
`NEEDS_REANCHOR` should be possible and should be *obvious*.

### The Zotero panel exists because the sync fails silently otherwise (T06)

Sync lag, receipts and conflicts. A curator who cannot see that the last sync
failed will assume the library is current — and `PR-03`'s early signal is that
divergence is invisible until someone compares.

### Baseline v1.3.0 — showing the cost of collaboration, and the shape of a decision

The experience and observability layer gains three things it could not
previously display, because they did not exist to be displayed.

**Collaboration cost.** Coordination overhead ratio, redundant message rate,
useful challenge rate, rounds, and the token ledger's seven categories. A single
cost total says a campaign was expensive; the categories say whether it was
expensive because it did science or because it held a meeting.

**The human decision surface, reordered.** Evidence first, recommendation second,
and a `DecisionDelta` when the second changes the first (`ADR-016`). The queue
uses evidence-delta priority — what changed since the last decision, not the full
state every time. **Attention priority orders and never authorises**, and no
timeout or learned preference produces an approval.

**Verifier abstention, surfaced.** An `ABSTAIN` is an escalation signal and has to
look like one in the interface. A surface that renders it as a soft pass has
undone `ADR-015`.

New SLOs: coordination overhead, challenge rate, contamination and security
findings, and the quality/cost Pareto frontier.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

13, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

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
| [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md) | `Cockpit application shell` · `Navigation/IA` · `BFF/read APIs` · `RBAC matrix` |

### Full prerequisite closure

**66 of 160 packages (41%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 25 | `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` |
| 28 | `WP-062` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-103`
- **Transitively reachable:** **23 of 160 packages (14%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **33** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Knowledge Product Lead |
| Independent verifier | Knowledge Curator / Citation Auditor |
| Gates touched | `G3` · `G10` |
| Controls | `CTL-LIT-01` · `CTL-LIT-02` · `CTL-LIT-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/ACC-01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-02 — Agent-Used Source Write-Back](../12_ACCEPTANCE_SCENARIOS/ACC-02_agent_used_source_writeback.md) | Critical | The source is written idempotently **only** into `40_Used` and the relevant project collection of the correct AIRL group library; the registry binding and a receipt are created. |
| [ACC-03 — Duplicate and Metadata Collision](../12_ACCEPTANCE_SCENARIOS/ACC-03_duplicate_collision.md) | High | The safe exact match binds to a single `SourceRecord`; conflicting fields are **not** silently overwritten and a curator `ConflictCase` is opened. |
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/ACC-04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-28 — Zotero Full Resync](../12_ACCEPTANCE_SCENARIOS/ACC-28_zotero_full_resync.md) | High | Item versions and bindings reconcile without producing duplicates or overwriting a human field; conflicts go to the curator queue. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/WP-070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md)
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
| `Cockpit application shell` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Navigation/IA` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `BFF/read APIs` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `RBAC matrix` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Accessibility baseline` | `WP-091` | `python3 scripts/progress.py show WP-091` |

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
- **Knowledge Product Lead** carries the acceptance decision; **Knowledge Curator / Citation Auditor** must verify independently of whoever implements.
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

### No registered source names this package

Neither register binds an upstream mechanism or a runtime component to `WP-094`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-094-T01 | Write the campaign, query and coverage dashboard | Implementation owner | Commit / configuration / record reference |
| WP-094-T02 | Build the source identity, representation and trust detail views | Implementation owner | Commit / configuration / record reference |
| WP-094-T03 | Add the duplicate, merge and conflict reconciliation screen | Implementation owner | Commit / configuration / record reference |
| WP-094-T04 | Bind the screening include/exclude/disagreement queue | Implementation owner | Commit / configuration / record reference |
| WP-094-T05 | Write the annotation → `EvidenceCandidate` promotion view | Implementation owner | Commit / configuration / record reference |
| WP-094-T06 | Add Zotero sync receipts, lag and conflict views plus manifest freeze/diff | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Literature Workbench`
- `Resolver/reconciliation UI`
- `Screening UI`
- `Manifest freeze UI`
- `Sync health view`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-094_literature_workbench.tests.md`](WP-094_literature_workbench.tests.md).

- A concurrent conflict resolving without overwrite
- A personal source rendered read-only
- A manifest diff producing a new version
- A retraction impact banner
- Accessible bulk screening
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-094_literature_workbench.acceptance.md`](WP-094_literature_workbench.acceptance.md), together with what this package still cannot establish.

- [ ] The UI changes Source Registry state only through the field authority rules.
- [ ] The Zotero view is never presented as manifest evidence.
- [ ] Every human disposition carries an actor and a rationale.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A UI rollback preserves the canonical queues and cases; batch actions reconcile through their idempotency token.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
