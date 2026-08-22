---
title: "WP-067 — Zotero Two-Way Sync and Reconciliation"
aliases:
  - "WP-067"
  - "WP-067 — Zotero Two-Way Sync and Reconciliation"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Human edits, agent proposals, concurrent versions, deletions, duplicates and loss of bridge state are reconciled — automatically or under human control — according to field authority."
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-067 — Zotero Two-Way Sync and Reconciliation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-067` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Knowledge Curator / SRE |
| Hard dependencies | WP-061, WP-062, WP-064, WP-065, WP-066 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01, CTL-OPS-01 |
| Related acceptance scenarios | ACC-03, ACC-28 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_067_zotero_sync_reconciliation.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_067_zotero_sync_reconciliation.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Human edits, agent proposals, concurrent versions, deletions, duplicates and loss of bridge state are reconciled — automatically or under human control — according to field authority.


## Analysis
### What this package actually decides

What happens when the human and the system disagree about a source. Every other
Zotero package defines a direction; this one handles the case where both wrote.

### Field-level three-way merge, not item-level (T02)

Item-level merge means one side's whole record wins. Field-level means the human's
abstract and the agent's DOI can both survive, because they were never in
conflict. WP-012 already decides authority per field; this is where that decision
becomes a merge class.

### 412 is not an error, it is the control working (T03)

WP-066 writes conditionally. A 412 means a human edited between read and write —
exactly what the conditional write exists to detect. The wrong response is a retry;
the right one is a re-read, a merge, and a `ConflictCase` if the merge is not safe.

### Loss of bridge state is the case that must be recoverable (T05)

The checkpoint store holds per-library and per-item versions. If it is lost, the
system does not know what it has seen — and the tempting recovery is a full resync
that re-creates everything, producing duplicates and re-writing items a human has
since edited.

The full-resync procedure has to include **dedup and rebind**, or recovery is
worse than the outage.

### The overwrite detector is the honesty control (T06)

An agent write that silently replaced a human value is the failure invariant 5
forbids, and it will happen at least once through a path nobody predicted. A
detector that compares written values against the prior human value — and alerts
rather than repairs — is what makes that discoverable instead of permanent.

### Curator SLA (T04)

A `ConflictCase` with no deadline sits in a queue. `00_PROGRAM/06`'s rule applies:
every finding reaches a terminal state, and one neither closed nor explicitly
parked has been forgotten.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md) | `Source Resolver service` · `Match rules/features` · `Conflict queue` · `Known-item/dedup test corpus` |
| [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/wp_064_zotero_library_access.md) | `Zotero topology` · `Collection template` · `Credential/permission matrix` · `Library lifecycle SOP` |
| [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md) | `Personal seed adapter` · `Opt-in configuration` · `Sync state/receipts` · `Seed ingest dashboard` |
| [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md) | `Zotero write-back service` · `Field mapping` · `Eligibility policy` · `SyncReceipt ledger` |

### Full prerequisite closure

**52 of 141 packages (37%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` |
| 28 | `WP-062` |
| 29 | `WP-065` · `WP-066` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-068` · `WP-072` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **49 of 141 packages (35%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **30** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Knowledge Platform Lead |
| Independent verifier | Knowledge Curator / SRE |
| Gates touched | `G3` · `G10` |
| Controls | `CTL-LIT-01` · `CTL-OPS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-03 — Duplicate and Metadata Collision](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) | High | The safe exact match binds to a single `SourceRecord`; conflicting fields are **not** silently overwritten and a curator `ConflictCase` is opened. |
| [ACC-28 — Zotero Full Resync](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) | High | Item versions and bindings reconcile without producing duplicates or overwriting a human field; conflicts go to the curator queue. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Source Identity Resolution, Deduplication and Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-064 — Zotero Library, Collection and Permission Model](../07_LITERATURE_KNOWLEDGE/wp_064_zotero_library_access.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/wp_065_zotero_seed_ingest.md), [WP-066 — Agent Candidate and Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/wp_066_zotero_agent_writeback.md)
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
- **Knowledge Platform Lead** carries the acceptance decision; **Knowledge Curator / SRE** must verify independently of whoever implements.
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
| WP-067-T01 | Establish the per-library and per-item version and `since` checkpoint store | Implementation owner | Commit / configuration / record reference |
| WP-067-T02 | Write the field-level three-way merge classes | Implementation owner | Commit / configuration / record reference |
| WP-067-T03 | Raise a `ConflictCase` for 412, deletion, permission and duplicate situations | Implementation owner | Commit / configuration / record reference |
| WP-067-T04 | Bind the manual reconciliation UI/API and the curator SLA | Implementation owner | Commit / configuration / record reference |
| WP-067-T05 | Write the full-resync plus dedup/rebind procedure | Implementation owner | Commit / configuration / record reference |
| WP-067-T06 | Establish sync lag, error and overwrite-detector telemetry | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Sync engine`
- `Reconciliation queue`
- `Full-resync runbook`
- `Conflict metrics/dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-067_zotero_sync_reconciliation.tests.md`](wp_067_zotero_sync_reconciliation.tests.md).

- Concurrent human and agent edits
- A remotely deleted item
- Full resync after bridge state loss
- A cross-library duplicate
- Preservation of a human-authored note
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-067_zotero_sync_reconciliation.acceptance.md`](wp_067_zotero_sync_reconciliation.acceptance.md), together with what this package still cannot establish.

- [ ] There is no silent last-write-wins anywhere in the sync.
- [ ] A full resync produces no duplicates.
- [ ] A human-authoritative field is never overwritten by an agent merge.
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

Sync is stopped while checkpoints and receipts are preserved; a controlled rebuild is performed from the resolver plus remote versions.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
