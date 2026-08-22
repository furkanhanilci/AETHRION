# WP-062 — Source Identity Resolution, Deduplication and Merge

## Package card

| Field | Value |
|---|---|
| Work package | `WP-062` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Source Resolver Lead |
| Independent verifier | Knowledge Curator / Citation Auditor |
| Hard dependencies | WP-017, WP-050, WP-058, WP-061 |
| Related gates | G3,G10 |
| Related controls | CTL-LIT-01 |
| Related acceptance scenarios | ACC-03, ACC-28 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-062_source_identity_resolver.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-062_source_identity_resolver.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

DOI, PMID, arXiv, ISBN, URL, title/author/year and file-hash signals resolve to a single `SourceRecord` with an explainable confidence; ambiguous collisions go to a human.


## Analysis
### What this package actually decides

When two references are the same work. It is a matching problem with an asymmetric
cost: a false merge silently combines two distinct works and every claim citing
either becomes wrong; a false split duplicates a source and wastes attention.

The first is much worse, which is why the auto-merge thresholds are deliberately
conservative and ambiguity goes to a human.

### Small explicit rules, not a learned scorer (T04)

`00_PROGRAM/01` states the pattern for risk and execution profiles, and it applies
here: small decision tables rather than a combinatorial score. A learned matcher
is more accurate on average and unexplainable in the individual case — and the
individual case is where a curator has to decide.

`PR-02`'s early signal is *unexplainable decisions*.

### The running system's duplicate detection is a review queue, deliberately

`src/airl_bridge/catalog.py` groups by normalised title and says why that is
acceptable:

> Normalising by title alone is a weak signal … That is acceptable precisely
> because the output is a **review queue rather than an action**.

That distinction is the design this package inherits. The moment matching becomes
automatic, the weak signal becomes a data-loss mechanism — and `ACC-03`, the
duplicate collision scenario, is where that gets tested.

### The known-item test set is what makes accuracy measurable (T06)

Pairs known to be the same work and pairs known to be different, held out. Without
it, precision and recall are claims. With it, the auto-merge threshold can be set
from a measured false-merge rate rather than from intuition.

### Split lineage is as important as merge lineage (T05)

One record turning out to be two is rarer and messier: prior citations become
ambiguous rather than wrong. The honest resolution is a **disambiguation state**
that a reader must resolve, not an arbitrary reassignment.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md) | `Versioned connectors` · `Connector permission profiles` · `Connector contract tests` · `Compensation/reconciliation playbooks` |
| [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md) | `Content firewall` · `Parser workers` · `ContentSafetyRecord` · `Injection detector` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |

### Full prerequisite closure

**48 of 141 packages (34%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 27 | `WP-058` |

### What acceptance of this package releases

- **Directly unblocked:** 11 — `WP-063` · `WP-065` · `WP-066` · `WP-067` · `WP-069` · `WP-070` · `WP-071` · `WP-072` · `WP-094` · `WP-103` · `WP-125`
- **Transitively reachable:** **57 of 141 packages (40%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **28** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Source Resolver Lead |
| Independent verifier | Knowledge Curator / Citation Auditor |
| Gates touched | `G3` · `G10` |
| Controls | `CTL-LIT-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-03 — Duplicate and Metadata Collision](../12_ACCEPTANCE_SCENARIOS/ACC-03_duplicate_collision.md) | High | The safe exact match binds to a single `SourceRecord`; conflicting fields are **not** silently overwritten and a curator `ConflictCase` is opened. |
| [ACC-28 — Zotero Full Resync](../12_ACCEPTANCE_SCENARIOS/ACC-28_zotero_full_resync.md) | High | Item versions and bindings reconcile without producing duplicates or overwriting a human field; conflicts go to the curator queue. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md)
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
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Versioned connectors` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector permission profiles` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector contract tests` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Compensation/reconciliation playbooks` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Content firewall` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Parser workers` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `ContentSafetyRecord` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Injection detector` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Quarantine UI/API` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |

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
- **Source Resolver Lead** carries the acceptance decision; **Knowledge Curator / Citation Auditor** must verify independently of whoever implements.
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
| WP-062-T01 | Write the identifier normalisation and resolver chain | Implementation owner | Commit / configuration / record reference |
| WP-062-T02 | Bind Crossref and provider lookups through the broker | Implementation owner | Commit / configuration / record reference |
| WP-062-T03 | Define exact and fuzzy candidate generation and the match features | Implementation owner | Commit / configuration / record reference |
| WP-062-T04 | Apply safe auto-merge thresholds through small explicit rules | Implementation owner | Commit / configuration / record reference |
| WP-062-T05 | Write the `ConflictCase`, curator queue and split/merge lineage | Implementation owner | Commit / configuration / record reference |
| WP-062-T06 | Build the duplicate metrics and the known-item test set | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Source Resolver service`
- `Match rules/features`
- `Conflict queue`
- `Known-item/dedup test corpus`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-062_source_identity_resolver.tests.md`](WP-062_source_identity_resolver.tests.md).

- Duplicate prevention on an identical DOI
- Separation of two different works sharing a title
- A manual case for contradicting title and year
- Cross-library Zotero duplicate mapping
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-062_source_identity_resolver.acceptance.md`](WP-062_source_identity_resolver.acceptance.md), together with what this package still cannot establish.

- [ ] An ambiguous match never auto-merges silently.
- [ ] A merge preserves every external binding and every prior reference.
- [ ] Duplicate detection is not bounded by a single Zotero library.
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

A wrong merge is corrected by a split operation; an `ImpactCase` is opened for the affected manifests and claims.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
