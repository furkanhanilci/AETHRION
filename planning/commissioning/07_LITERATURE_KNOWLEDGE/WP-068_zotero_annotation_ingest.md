# WP-068 — Zotero Annotation → EvidenceCandidate Pipeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-068` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Intake Lead |
| Independent verifier | Citation Auditor / Knowledge Curator |
| Hard dependencies | WP-017, WP-058, WP-061, WP-063, WP-065, WP-067 |
| Related gates | G3,G5 |
| Related controls | CTL-EPI-01, CTL-LIT-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-068_zotero_annotation_ingest.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-068_zotero_annotation_ingest.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Zotero highlights and comments become `AnnotationObservation` and `EvidenceCandidate` records carrying the parent attachment, representation hash, locator and actor — never evidence on their own.


## Analysis
### What this package actually decides

That a highlight is **not** evidence. An `AnnotationObservation` records that a
human marked a passage; an `EvidenceSpan` licenses a claim. The gap between them
is a promotion decision, and collapsing it would let a reader's yellow highlighter
become a citation.

The naming carries the boundary: *observation*, not finding.

### The attachment hash is what makes an annotation locatable later (T04)

A Zotero annotation carries a page and a position, relative to **a specific PDF**.
Bind it to the `SourceRepresentation` hash and the annotation stays resolvable; bind
it to the work and it resolves to whichever file someone has.

This is the same argument WP-018 makes for the three-part anchor, one layer earlier.

### The mismatch state is the honest outcome (T04)

A researcher re-downloads a paper and the new PDF is paginated differently. The
annotation's locator no longer resolves. The correct behaviour is a **mismatch
state** — *this annotation was made against a representation we can identify and no
longer have* — which is different from *this annotation is wrong* and different
again from *this annotation is fine*.

### Deleted and edited annotations have downstream consequences (T06)

If an observation was promoted to an `EvidenceCandidate` and then to an
`EvidenceSpan` supporting a claim, deleting the annotation does not delete the
claim. It should raise an impact case — the same loop WP-037 runs for retractions,
applied to the human's own change of mind.

### Duplicate logic matters because researchers re-highlight (T05)

The same passage marked twice, or marked in two copies of the same paper, is one
observation. Without dedup the promotion queue fills with the same span.

### Baseline v1.3.0 — unchanged ownership, new cross-cutting obligations

No semantic ownership changes here. What changes is what these packages must
remain compatible with:

- the **trace and correlation** fields every plane now carries, so a divergence
  is traceable to a cause;
- **context projection**, so that a record's canonical status does not depend on
  whether it happened to be in an agent's context;
- **provenance rules** for anything adapted from an upstream source.

Generated counts, indexes and the new cross-cutting acceptance references must
stay consistent — which is a mechanical obligation, and the one most likely to be
skipped because nothing in the package's own subject matter changed.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md) | `Content firewall` · `Parser workers` · `ContentSafetyRecord` · `Injection detector` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md) | `Representation ingest service` · `License/status policy` · `Status monitor` · `Format locator metadata` |
| [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md) | `Personal seed adapter` · `Opt-in configuration` · `Sync state/receipts` · `Seed ingest dashboard` |
| [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md) | `Sync engine` · `Reconciliation queue` · `Full-resync runbook` · `Conflict metrics/dashboard` |

### Full prerequisite closure

**55 of 160 packages (34%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-037` · `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` |
| 28 | `WP-062` |
| 29 | `WP-063` · `WP-065` · `WP-066` |
| 30 | `WP-067` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-076` · `WP-078` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **57 of 160 packages (36%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **31** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Evidence Intake Lead |
| Independent verifier | Citation Auditor / Knowledge Curator |
| Gates touched | `G3` · `G5` |
| Controls | `CTL-EPI-01` · `CTL-LIT-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-063 — Source Representation, Licence and Status Monitoring](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-065 — Personal Zotero Seed Ingest Pipeline](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-067 — Zotero Two-Way Sync and Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md)
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
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
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
| `Representation ingest service` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `License/status policy` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Status monitor` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Format locator metadata` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Retention mapping` | `WP-063` | `python3 scripts/progress.py show WP-063` |
| `Personal seed adapter` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Opt-in configuration` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Sync state/receipts` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Seed ingest dashboard` | `WP-065` | `python3 scripts/progress.py show WP-065` |
| `Sync engine` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Reconciliation queue` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Full-resync runbook` | `WP-067` | `python3 scripts/progress.py show WP-067` |
| `Conflict metrics/dashboard` | `WP-067` | `python3 scripts/progress.py show WP-067` |

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
- **Evidence Intake Lead** carries the acceptance decision; **Citation Auditor / Knowledge Curator** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-068`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-068-T01 | Write the incremental reader for annotation items | Implementation owner | Commit / configuration / record reference |
| WP-068-T02 | Map the parent attachment to its `SourceRepresentation` | Implementation owner | Commit / configuration / record reference |
| WP-068-T03 | Normalise the text, comment, colour, page, position, author and version fields | Implementation owner | Commit / configuration / record reference |
| WP-068-T04 | Apply attachment hash and locator resolution, including the mismatch state | Implementation owner | Commit / configuration / record reference |
| WP-068-T05 | Add the `EvidenceCandidate` promotion queue and duplicate logic | Implementation owner | Commit / configuration / record reference |
| WP-068-T06 | Establish the impact behaviour for deleted and edited annotations | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Annotation ingest service`
- `AnnotationObservation records`
- `EvidenceCandidate queue`
- `Promotion/disposition UI contract`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-068_zotero_annotation_ingest.tests.md`](WP-068_zotero_annotation_ingest.tests.md).

- Promotion of a highlight on the correct attachment
- `NEEDS_REANCHOR` on a mismatched PDF
- Versioning of an edited or deleted annotation
- Duplicate note and annotation handling
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-068_zotero_annotation_ingest.acceptance.md`](WP-068_zotero_annotation_ingest.acceptance.md), together with what this package still cannot establish.

- [ ] An annotation never becomes an `EvidenceSpan` or a `VERIFIED` claim automatically.
- [ ] No promotion occurs without an attachment representation hash.
- [ ] Human commentary is kept in a separate field with its own provenance.
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

A wrong mapping marks the candidate `INVALIDATED`; nothing is ever written back onto the canonical Zotero annotation.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
