---
title: "WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze"
aliases:
  - "WP-103"
  - "WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Human Zotero seeds and agent discovery results merge in the Source Registry, screening and annotation promotion run, and an immutable G3 set is frozen."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-103_vertical_slice_literature.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/state/not-started
---

# WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze

## Package card

| Field | Value |
|---|---|
| Work package | `WP-103` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Lead |
| Independent verifier | Citation Auditor / Security |
| Hard dependencies | WP-035, WP-058, WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-094, WP-099 |
| Related gates | G3 |
| Related controls | CTL-LIT-01, CTL-LIT-03, CTL-SEC-01 |
| Related acceptance scenarios | ACC-01, ACC-02, ACC-03, ACC-05, ACC-28 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_103_vertical_slice_literature.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_103_vertical_slice_literature.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Human Zotero seeds and agent discovery results merge in the Source Registry, screening and annotation promotion run, and an immutable G3 set is frozen.


## Analysis
### What this package actually decides

Whether the literature path survives a real library. Seeds, discovery, resolution,
screening, annotation promotion, and a frozen set — end to end, against fixtures
that include the cases that actually break things.

### The four fixtures that matter (T03)

The sub-task names them and each is a known failure mode:

- **Duplicates** — two records that are one work (`ACC-03`, WP-062's false-merge
  guard)
- **Conflicts** — human and agent editing the same field (WP-067)
- **412 responses** — a human edit landing between an agent's read and write
  (WP-066)
- **Human-field preservation** — invariant 5, the promise the researcher relies on

A slice that runs on clean fixtures has tested the case that was never in doubt.

### This is where the running system's findings get exercised

The V0 bridge holds 33 real sources and three open findings that this slice will
meet directly:

- **H1** — the 100-record ingest cap. A fixture library above 100 items exercises
  it, and **M9 must already be fixed** (WP-074) or the test causes data loss.
- **H2** — deletion reconciliation. Removing a seed source is one of the fixtures.
- **H3** — the read-only boundary, proven behaviourally here if not before.

### Annotation promotion is the boundary this slice checks (T05)

A highlight becoming an `EvidenceCandidate` becoming an `EvidenceSpan` supporting a
claim. Three hops, three packages, and the property that must hold throughout is
that the human's annotation is never treated as evidence on its own.

### Counter-evidence search is required to close (T02)

WP-070 refuses to close a campaign without it. This slice is where that refusal is
demonstrated rather than described.

### Baseline v1.3.0 — the slices exercise the cohort, and the regression injects faults

The vertical slices and the cutover path grow to cover what this baseline adds,
and one package changes character.

**WP-107 becomes the engineering completion slice.** Requirement and
specification → worktree → TDD → code review → CI → supply-chain attestation →
signed artifact → **eligibility to produce scientific evidence**. That last arrow
is the junction between the two disciplines, and before this baseline nothing
proved it end to end.

**The other slices exercise the collaboration plane**: a compiled cohort, sealed
initial positions, typed delta exchange over a sparse topology, an adaptive
assurance route, a fingerprinted reproduction and a firewalled benchmark run.

**The regression suite gains injections rather than cases.** Faulty agent,
malicious agent, split brain, duplicate and out-of-order events, communication
degradation under budget pressure, and benchmark contamination. These are
failures that are invisible in a healthy run and obvious only in a post-mortem,
which is why they are caused deliberately rather than waited for.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

16, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/wp_058_content_quarantine_firewall.md) | `Content firewall` · `Parser workers` · `ContentSafetyRecord` · `Injection detector` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/wp_064_zotero_library_access.md) | `Zotero topology` · `Collection template` · `Credential/permission matrix` · `Library lifecycle SOP` |
| [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md) | `Personal seed adapter` · `Opt-in configuration` · `Sync state/receipts` · `Seed ingest dashboard` |
| [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md) | `Zotero write-back service` · `Field mapping` · `Eligibility policy` · `SyncReceipt ledger` |
| [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/wp_067_zotero_sync_reconciliation.md) | `Sync engine` · `Reconciliation queue` · `Full-resync runbook` · `Conflict metrics/dashboard` |
| [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/wp_068_zotero_annotation_ingest.md) | `Annotation ingest service` · `AnnotationObservation records` · `EvidenceCandidate queue` · `Promotion/disposition UI contract` |
| [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md) | `SearchProtocol service` · `LiteratureCampaign workflow` · `Query log` · `Known-item/coverage tests` |
| [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/wp_070_dual_directional_literature.md) | `Dual-loop discovery workflow` · `Discovery provenance` · `Candidate/coverage matrix` · `Counter-evidence log` |
| [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/wp_071_screening_inclusion.md) | `Screening service` · `Decision queue` · `Reason taxonomy` · `Coverage/flow report` |
| [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md) | `LiteratureSetManifest` · `Signed frozen package` · `Portable exports` · `Zotero frozen view` |
| [WP-094 — Literature Workbench and Reconciliation UI](../09_EXPERIENCE_OBSERVABILITY/wp_094_literature_workbench.md) | `Literature Workbench` · `Resolver/reconciliation UI` · `Screening UI` · `Manifest freeze UI` |
| [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md) | `Audit Ledger` · `Hash-chain service` · `Audit export/verify tooling` · `Retention/access policy` |

### Full prerequisite closure

**73 of 160 packages (46%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-099` |
| 32 | `WP-072` |
| 33 | `WP-094` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-109` · `WP-110`
- **Transitively reachable:** **25 of 160 packages (16%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **34** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Evidence Lead |
| Independent verifier | Citation Auditor / Security |
| Gates touched | `G3` |
| Controls | `CTL-LIT-01` · `CTL-LIT-03` · `CTL-SEC-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-02 — Agent-Used Source Write-Back](../12_ACCEPTANCE_SCENARIOS/acc_02_agent_used_source_writeback.md) | Critical | The source is written idempotently **only** into `40_Used` and the relevant project collection of the correct AIRL group library; the registry binding and a receipt are created. |
| [ACC-03 — Duplicate and Metadata Collision](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) | High | The safe exact match binds to a single `SourceRecord`; conflicting fields are **not** silently overwritten and a curator `ConflictCase` is opened. |
| [ACC-05 — Prompt-Injection PDF](../12_ACCEPTANCE_SCENARIOS/acc_05_prompt_injection_pdf.md) | Critical | The content stays untrusted quoted data; extraction continues read-only, no tool, secret or write call occurs, and security event and scan evidence is produced. |
| [ACC-28 — Zotero Full Resync](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) | High | Item versions and bindings reconcile without producing duplicates or overwriting a human field; conflicts go to the curator queue. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/wp_058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/wp_064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/wp_067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Pipeline](../07_LITERATURE_KNOWLEDGE/wp_068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol and LiteratureCampaign Orchestration](../07_LITERATURE_KNOWLEDGE/wp_069_search_protocol_campaign.md), [WP-070 — Human + Agent Two-Way Literature Discovery](../07_LITERATURE_KNOWLEDGE/wp_070_dual_directional_literature.md), [WP-071 — Screening, Inclusion/Exclusion and Coverage](../07_LITERATURE_KNOWLEDGE/wp_071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md), [WP-094 — Literature Workbench and Reconciliation UI](../09_EXPERIENCE_OBSERVABILITY/wp_094_literature_workbench.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md)
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
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Content firewall` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Parser workers` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `ContentSafetyRecord` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Injection detector` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Quarantine UI/API` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Capability gate for untrusted content` | `WP-058` | `python3 scripts/progress.py show WP-058` |
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
| `Literature Workbench` | `WP-094` | `python3 scripts/progress.py show WP-094` |
| `Resolver/reconciliation UI` | `WP-094` | `python3 scripts/progress.py show WP-094` |
| `Screening UI` | `WP-094` | `python3 scripts/progress.py show WP-094` |
| `Manifest freeze UI` | `WP-094` | `python3 scripts/progress.py show WP-094` |
| `Sync health view` | `WP-094` | `python3 scripts/progress.py show WP-094` |
| `Audit Ledger` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Hash-chain service` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Audit export/verify tooling` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Retention/access policy` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Integrity dashboard` | `WP-099` | `python3 scripts/progress.py show WP-099` |

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
- **Evidence Lead** carries the acceptance decision; **Citation Auditor / Security** must verify independently of whoever implements.
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
| WP-103-T01 | Ingest the personal seed fixture | Implementation owner | Commit / configuration / record reference |
| WP-103-T02 | Run the agent literature campaign, snowball and counter-evidence search | Implementation owner | Commit / configuration / record reference |
| WP-103-T03 | Test duplicates, conflicts, 412 responses and human-field preservation | Implementation owner | Commit / configuration / record reference |
| WP-103-T04 | Complete the screening, disagreement, trust and status flow | Implementation owner | Commit / configuration / record reference |
| WP-103-T05 | Prepare an annotation for candidate → span promotion | Implementation owner | Commit / configuration / record reference |
| WP-103-T06 | Verify the manifest, exports, Zotero frozen view and audit trail | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Literature vertical dossier`
- `Frozen LiteratureSetManifest`
- `Zotero SyncReceipts`
- `Coverage/screening report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-103_vertical_slice_literature.tests.md`](wp_103_vertical_slice_literature.tests.md).

- ACC-01, 02, 03, 05 and 28
- Manifest hash reproducibility
- Preservation of a human note
- Containment of a prompt-injection PDF
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-103_vertical_slice_literature.acceptance.md`](wp_103_vertical_slice_literature.acceptance.md), together with what this package still cannot establish.

- [ ] Source identifiers and representations are complete.
- [ ] Zotero never silently overwrites a canonical or human-authored field.
- [ ] The manifest is immutable and signed.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

The test group collection and archive are preserved; connector writes are disabled and the slice is not accepted until every conflict is cleared.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
