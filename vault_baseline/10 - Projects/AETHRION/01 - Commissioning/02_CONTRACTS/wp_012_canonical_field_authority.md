---
title: "WP-012 — Canonical Ownership and Field-Level Authority Matrix"
aliases:
  - "WP-012"
  - "WP-012 — Canonical Ownership and Field-Level Authority Matrix"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Where the same data appears on more than one surface, the system-of-record, the field authority, the sync direction and the conflict behaviour are settled in advance rather than discovered during an incident."
source: "planning/commissioning/02_CONTRACTS/WP-012_canonical_field_authority.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-012 — Canonical Ownership and Field-Level Authority Matrix

## Package card

| Field | Value |
|---|---|
| Work package | `WP-012` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Internal Audit / Knowledge Lead |
| Hard dependencies | WP-010, WP-011 |
| Related gates | Platform,G3,G10 |
| Related controls | CTL-LIT-01, CTL-OPS-01 |
| Related acceptance scenarios | ACC-03, ACC-21, ACC-22 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_012_canonical_field_authority.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_012_canonical_field_authority.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Where the same data appears on more than one surface, the system-of-record, the field authority, the sync direction and the conflict behaviour are settled in advance rather than discovered during an incident.


## Analysis

### What this package actually decides

Which surface is allowed to be wrong. When the same field lives in two places,
one of them is the record and the other is a view — and the failure this package
prevents is the state where neither has been designated, so both are edited and
whichever wrote last wins.

`PR-03` rates this **critical**: *Zotero/Registry/Obsidian values diverge.* Its
early signal is the one that makes it dangerous — divergence is invisible until
someone compares, and nobody compares until an incident.

### The three-surface problem this system actually has

| Surface | What it owns | What it must never own |
|---|---|---|
| Zotero | The human's own bibliographic fields and annotations | Canonical source identity, dedup state, trust |
| Source Registry | Identity, dedup, status, trust | The human's notes and keywords |
| Obsidian | Human synthesis in the numbered areas | Anything under a generated banner |

The rule already runs in the working slice and should be lifted verbatim into the
matrix: **the projection deletes only files listed in its own manifest**, so a
human note dropped in the generated folder survives. That is field authority
implemented as a file-level invariant, and `tests/test_obsidian.py` proves it.

### Where the running system already violates this

Finding **H2**: a source deleted in Zotero persists in the registry and in
Obsidian indefinitely. That is not a missing feature — it is an **unassigned
canonical authority for deletion**. Nobody decided whether Zotero's deletion is
authoritative over the registry's existence. T05 is where that gets an owner, and
until it does, H2 cannot be fixed correctly, only patched.

### Why the rebuild rule (T04) is a canonical-ownership question

`00_PROGRAM/01` success invariant 6: derived graphs and indexes can be rebuilt
from canonical records from scratch. That is the operational test of whether
something is canonical: **if you cannot delete it and rebuild it, it holds state
nothing else has**, and it is therefore canonical whether or not the matrix says
so. The rebuild rule is how the matrix gets falsified.

### The failure mode

A matrix that assigns authority per *record* rather than per *field*. Zotero owns
the abstract; the registry owns whether the source is retracted. Same record, two
authorities. A record-level matrix cannot express that, and the system will
resolve it by whichever sync ran last.

### Baseline v1.2.0 — authority for the records that did not exist when this was written

The matrix must cover every record added by WP-141–147 and, separately, the six
memory stores. For each: canonical owner, who may read, who may write, whether a
change creates a version, and — the field that is new — **whether it may support
a claim.**

Only the evidence store may. Finding memory supports a claim indirectly, by being
what a claim is drafted from. Search experience, procedural memory and principle
memory may not, at all, and a retrieval API that lets a caller ask across stores
by default makes that rule unenforceable. `MemoryQuery` therefore names the
stores it is asking, and the policy decides from the requesting role. ADR-005.

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

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md) | `Signed ADR bundle` · `Rejected alternatives register` · `Reopen trigger register` · `Architecture baseline digest` |
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |

### Full prerequisite closure

**11 of 160 packages (7%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 11 — `WP-014` · `WP-015` · `WP-017` · `WP-018` · `WP-030` · `WP-061` · `WP-064` · `WP-066` · `WP-073` · `WP-091` · `WP-146`
- **Transitively reachable:** **145 of 160 packages (91%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **9** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **M** |
| Accountable owner | Chief Architect |
| Independent verifier | Internal Audit / Knowledge Lead |
| Gates touched | `Platform` · `G3` · `G10` |
| Controls | `CTL-LIT-01` · `CTL-OPS-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-03 — Duplicate and Metadata Collision](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) | High | The safe exact match binds to a single `SourceRecord`; conflicting fields are **not** silently overwritten and a curator `ConflictCase` is opened. |
| [ACC-21 — Derived Graph Corruption and Rebuild](../12_ACCEPTANCE_SCENARIOS/acc_21_graph_corruption.md) | High | Canonical services are unaffected; a new projection is built with the expected counts, hashes and lineage and promoted atomically. |
| [ACC-22 — Obsidian Human Edit Preservation](../12_ACCEPTANCE_SCENARIOS/acc_22_obsidian_human_edit.md) | High | The human field is preserved byte- and semantically; only the generated zone updates, and an unexpected conflict opens a curator case instead of an automatic overwrite. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
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
| `Signed ADR bundle` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Rejected alternatives register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Reopen trigger register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Architecture baseline digest` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |

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
- **Chief Architect** carries the acceptance decision; **Internal Audit / Knowledge Lead** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-012`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-012-T01 | Assign the canonical record for every bounded context | Implementation owner | Commit / configuration / record reference |
| WP-012-T02 | Define human versus agent field authority across the Source Registry and Zotero | Implementation owner | Commit / configuration / record reference |
| WP-012-T03 | Write the authority rules for the human and generated blocks in Obsidian | Implementation owner | Commit / configuration / record reference |
| WP-012-T04 | Add the rebuild rule for derived graphs and indexes | Implementation owner | Commit / configuration / record reference |
| WP-012-T05 | Assign owners for conflict, merge, tombstone and reconciliation cases | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Canonical Ownership Matrix`
- `Field Authority Table`
- `Sync direction map`
- `Conflict ownership matrix`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-012_canonical_field_authority.tests.md`](wp_012_canonical_field_authority.tests.md).

- A sweep for dual-canonical contradictions
- A negative test for overwriting a human-authored field
- A derived-view rebuild tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-012_canonical_field_authority.acceptance.md`](wp_012_canonical_field_authority.acceptance.md), together with what this package still cannot establish.

- [ ] Every field has exactly one authority.
- [ ] Two-way sync does not create ownership ambiguity.
- [ ] Loss of derived data is not counted as data loss and is demonstrably rebuildable.
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

No automatic winner is chosen in a conflict; the last safe canonical version is preserved and a reconciliation case is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
