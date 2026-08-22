---
title: "WP-011 — Identity and End-to-End Correlation Standard"
aliases:
  - "WP-011"
  - "WP-011 — Identity and End-to-End Correlation Standard"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Project, workflow, gate, task, actor, source, representation, claim, evidence, run, artifact, review, decision, cost and event identifiers become collision-free and queryable as one chain."
source: "planning/commissioning/02_CONTRACTS/WP-011_identity_correlation_standard.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-011 — Identity and End-to-End Correlation Standard

## Package card

| Field | Value |
|---|---|
| Work package | `WP-011` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Platform Lead |
| Independent verifier | Security Architect |
| Hard dependencies | WP-010 |
| Related gates | Platform |
| Related controls | CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_011_identity_correlation_standard.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_011_identity_correlation_standard.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Project, workflow, gate, task, actor, source, representation, claim, evidence, run, artifact, review, decision, cost and event identifiers become collision-free and queryable as one chain.


## Analysis

### What this package actually decides

That an identifier is minted, never inferred. Every downstream question — can
this claim be traced to its source span, did these two runs use the same dataset,
is this the reviewer who saw the producer's trace — is a join, and a join is only
as good as the key.

The decision with the longest reach is T04: **external locators are aliases, not
identity.** A DOI, a Zotero key and an ORCID are things the outside world assigns
and can reassign. Binding canonical identity to one of them means an upstream
correction rewrites your primary key.

### The defect already in the running system

`src/airl_bridge/zotero.py` mints `airl_id` as `SRC-ZOT-` plus a **64-bit
truncated** SHA-256 of the Zotero binding, with no collision handling — recorded
as finding **L2**. At 33 sources this is invisible. It is not a property to
discover at scale, and it is exactly what T01 exists to settle: the identifier
format is a decision, and the current one was a default.

It does one thing right, and the standard should keep it: the hash covers the
**binding**, not the title, so editing a title does not mint a new identity.
`tests/test_zotero.py::test_normalize_item_uses_stable_binding` asserts it.

### The tombstone and merge rules are the hard half

T05 is the sub-task most likely to be under-specified, because merging is rare
until it is urgent. Two records turn out to be one work; one record turns out to
be two. Both cases need an answer to the same question: **what happens to
everything that already pointed at the old identifier?**

A tombstone that redirects preserves the join. A tombstone that deletes breaks
every claim, run and review downstream — and `00_PROGRAM/01`'s success invariant 1
requires that a material claim resolve to its source in a *single query*. A merge
without a lineage record makes that query silently wrong rather than empty, which
is worse.

### Why UUIDv7 rather than UUIDv4

T01 names it, and the reason is operational: UUIDv7 is time-ordered, so it
indexes without page splits and sorts into insertion order for free. That matters
when the correlation chain is queried by range — "every artifact this workflow
produced" — which is the query the cockpit runs constantly.

### The relationship to the existing contract core

`src/airl_framework/contracts.py` already has an `Identity` class with fourteen
fields and a `correlation_key()`. It has **no production consumer** (finding
**H4**), and `_ID_RE` requires an uppercase stable identifier while the bridge
mints `SRC-ZOT-<hex>` — which happens to conform. Binding the bridge to it is the
first real test of whether the contract core is a contract or a sketch.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

1, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md) | `Signed ADR bundle` · `Rejected alternatives register` · `Reopen trigger register` · `Architecture baseline digest` |

### Full prerequisite closure

**10 of 141 packages (7%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |

### What acceptance of this package releases

- **Directly unblocked:** 15 — `WP-012` · `WP-013` · `WP-014` · `WP-015` · `WP-016` · `WP-017` · `WP-018` · `WP-019` · `WP-020` · `WP-041` · `WP-042` · `WP-049` · `WP-096` · `WP-099` · `WP-100`
- **Transitively reachable:** **129 of 141 packages (91%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **8** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **M** |
| Accountable owner | Data Platform Lead |
| Independent verifier | Security Architect |
| Gates touched | `Platform` |
| Controls | `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md)
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
| `Signed ADR bundle` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Rejected alternatives register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Reopen trigger register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Architecture baseline digest` | `WP-010` | `python3 scripts/progress.py show WP-010` |

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
- **Data Platform Lead** carries the acceptance decision; **Security Architect** must verify independently of whoever implements.
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
| WP-011-T01 | Assign the UUIDv7 and opaque-ID formats per entity type | Implementation owner | Commit / configuration / record reference |
| WP-011-T02 | Write the project → workflow → run → artifact → claim/cost correlation chain | Implementation owner | Commit / configuration / record reference |
| WP-011-T03 | Define the identity fields for human, model and service actors | Implementation owner | Commit / configuration / record reference |
| WP-011-T04 | Model external locators such as Zotero keys, DOIs and ORCIDs as aliases, never as canonical identity | Implementation owner | Commit / configuration / record reference |
| WP-011-T05 | Establish the ID minting, tombstone and merge rules | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Identifier Standard`
- `Correlation envelope`
- `ID library contract`
- `Merge/tombstone rules`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-011_identity_correlation_standard.tests.md`](wp_011_identity_correlation_standard.tests.md).

- Uniqueness and property-based tests
- A cross-service correlation fixture
- An alias-collision and merge test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-011_identity_correlation_standard.acceptance.md`](wp_011_identity_correlation_standard.acceptance.md), together with what this package still cannot establish.

- [ ] No canonical ID depends on an external key.
- [ ] Every event and artifact carries an actor and a correlation identifier.
- [ ] A merge does not break existing references.
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

A faulty ID mapping is corrected with a tombstone plus a replacement event; historical records are never overwritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
