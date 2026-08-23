# WP-017 — Source Registry and Literature Contract Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-017` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Citation Auditor / Data Architect |
| Hard dependencies | WP-011, WP-012, WP-014 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01, CTL-LIT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-017_source_literature_contracts.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-017_source_literature_contracts.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Source identity, representation, trust, search, screening, set manifest, Zotero binding and status-event schemas are defined canonically, so that a citation means the same thing everywhere in the system.


## Analysis
### What this package actually decides

That a citation means the same thing everywhere. The purpose says it plainly, and
the reason it needs a package is that a "source" is at least four different
objects that are routinely conflated: the **work**, the **representation** of that
work this system actually read, the **binding** to a human's Zotero item, and the
**status** of the work in the outside world.

Conflating the first two is the common failure. A claim anchored to "the paper"
cannot be checked, because the reader has a different PDF with different
pagination. A claim anchored to a `SourceRepresentation` with a content hash can
be — which is why `SourceRepresentation` carries hash, format, licence and locator
separately from `SourceRecord`.

### What already exists, and where it is a prototype

The running bridge has a `SourceRecord` — identity, canonical payload, content
hash — and it is a genuine first slice of this contract. It is also missing every
part that makes the contract useful:

| This package requires | The bridge today |
|---|---|
| `SourceRepresentation` with hash, format, licence, locator | none — no representation layer at all |
| `SourceTrustCard`, `RetractionStatus` | none — `monitor_sources.py` sweeps Crossref but writes to no status field |
| `SearchProtocol`, `ScreeningDecision`, `LiteratureSetManifest` | none |
| `ZoteroBinding`, `SyncReceipt`, `AnnotationObservation` | the binding exists as a derived string; no receipt, no annotations |
| Merge lineage on `SourceRecord` | none — finding **L2**, and no merge path |

So this package is not greenfield: it has to define contracts that the existing
registry can migrate onto, and the migration is the risky part.

### `SourceTrustCard` and `RetractionStatus` are the loop-closing fields

`00_PROGRAM/01` requires the chain to be traversable **backwards**: a retracted
source must reach every dependent claim. `monitor_sources.py` already sweeps
Crossref for retractions and expressions of concern, and its measurement file
records the gap honestly: `claim_impact_analysis: "not implemented — no Claim
Ledger exists"`.

The status field defined here is what that sweep will eventually write into. Until
it exists, G10 monitoring produces a report nobody's claims are connected to.

### The Zotero direction rule is a canonical-authority decision (T05)

`ZoteroBinding` and `SyncReceipt` encode WP-012's field authority for one specific
pair. The plan's own binding decision is that the personal library is a
**read-only seed** and group libraries are a controlled collaboration view. The
contract has to make the read-only direction structural rather than behavioural —
the bridge's strongest security claim today rests on there being no write code,
which is a fact about the implementation, not about the contract (finding **H3**).

### `AnnotationObservation` — why "observation"

A human's Zotero annotation is evidence of what a human thought, not a claim the
system may assert. Naming it an *observation* keeps that boundary in the type
system rather than in a convention.

### Baseline v1.3.0 — new records, and the authority typing that keeps them honest

The contract surface gains the records this baseline's capabilities need, and
one field that matters more than any of them.

**New canonical records:** `AgentCohortRecord`, `CognitiveDiversityProfile`,
`CommunicationEdgePolicy`, `BlackboardEntry`, `TypedAgentMessage`,
`CommunicationUtilityRecord`, `ContextProjectionRecord`,
`MemoryInterventionRecord`, `ResearchBudgetContract`, `TokenLedgerEntry`,
`SpecificationConformanceRecord`, `HumanPreliminaryAssessment`, `DecisionDelta`,
`ModelExecutionFingerprint`, `BenchmarkRunPolicy`, `ContaminationFinding`,
`UpstreamAssimilationRecord`.

**Explicit authority typing.** Every record carries what it may never become. The
three conversions this baseline forbids are all of the same kind, and each has
already been attempted somewhere in the field:

| Forbidden conversion | Why it is tempting |
|---|---|
| A blackboard entry into evidence | It is where the interesting sentences appear |
| A communication or search utility score into a claim confidence | It is a number, and it correlates with something |
| An event payload into gate authority | It is the fastest path and it usually works |

The rule that makes them checkable rather than remembered: **events, blackboard
entries and derived read models cannot masquerade as canonical scientific
state**, and the schema is where that is enforced.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |

### Full prerequisite closure

**13 of 160 packages (8%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 9 | `WP-012` |
| 10 | `WP-014` |

### What acceptance of this package releases

- **Directly unblocked:** 19 — `WP-018` · `WP-020` · `WP-030` · `WP-035` · `WP-037` · `WP-058` · `WP-061` · `WP-062` · `WP-063` · `WP-064` · `WP-065` · `WP-066` · `WP-068` · `WP-069` · `WP-071` · `WP-072` · `WP-073` · `WP-076` · `WP-079`
- **Transitively reachable:** **142 of 160 packages (89%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **11** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Knowledge Lead |
| Independent verifier | Citation Auditor / Data Architect |
| Gates touched | `G3` · `G10` |
| Controls | `CTL-LIT-01` · `CTL-LIT-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/WP-011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md)
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
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
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

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Knowledge Lead** carries the acceptance decision; **Citation Auditor / Data Architect** must verify independently of whoever implements.
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
| WP-017-T01 | Write the `SourceRecord` identifier and merge-lineage fields | Implementation owner | Commit / configuration / record reference |
| WP-017-T02 | Add the `SourceRepresentation` hash, format, licence and locator fields | Implementation owner | Commit / configuration / record reference |
| WP-017-T03 | Define `SourceTrustCard` and `RetractionStatus` | Implementation owner | Commit / configuration / record reference |
| WP-017-T04 | Write the `SearchProtocol`, `ScreeningDecision` and `LiteratureSetManifest` schemas | Implementation owner | Commit / configuration / record reference |
| WP-017-T05 | Add the `ZoteroBinding`, `SyncReceipt` and `AnnotationObservation` schemas | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Literature schema bundle`
- `Status lifecycle`
- `Sample manifests`
- `Zotero binding contract`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-017_source_literature_contracts.tests.md`](WP-017_source_literature_contracts.tests.md).

- DOI and title-collision fixtures
- A manifest-immutability test
- A test requiring an attachment hash on every annotation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-017_source_literature_contracts.acceptance.md`](WP-017_source_literature_contracts.acceptance.md), together with what this package still cannot establish.

- [ ] A Zotero item key is never treated as the canonical source ID.
- [ ] A manifest is a frozen snapshot of the Source Registry.
- [ ] New status or representation versions do not alter a previously frozen set.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

A wrong merge is corrected through a split event; older set manifests and bindings are preserved unchanged.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
