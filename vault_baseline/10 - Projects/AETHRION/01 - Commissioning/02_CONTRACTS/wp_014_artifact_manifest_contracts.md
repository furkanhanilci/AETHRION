---
title: "WP-014 — Artifact, Dataset and Immutable Manifest Schemas"
aliases:
  - "WP-014"
  - "WP-014 — Artifact, Dataset and Immutable Manifest Schemas"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Code, data, environment, document and publication artifacts are defined as immutable objects carrying a content hash, lineage, retention, licence and validity state."
source: "planning/commissioning/02_CONTRACTS/WP-014_artifact_manifest_contracts.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/g3-g9
  - aethrion/state/not-started
---

# WP-014 — Artifact, Dataset and Immutable Manifest Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-014` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Data Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Hard dependencies | WP-011, WP-012 |
| Related gates | G3–G9 |
| Related controls | CTL-DAT-01, CTL-SUP-01 |
| Related acceptance scenarios | ACC-23 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_014_artifact_manifest_contracts.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_014_artifact_manifest_contracts.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Code, data, environment, document and publication artifacts are defined as immutable objects carrying a content hash, lineage, retention, licence and validity state.


## Analysis

### What this package actually decides

That bytes are never overwritten. T04 states it as a replacement: **new version
and `INVALIDATED` semantics in place of overwrite.** Everything else in the
package follows — the content address, the lineage, the retention, the legal hold
— because each of them only means something if the bytes they describe cannot
change under them.

`PR-08` is the failure: *different bytes at the same URI.* Rated critical, and
correctly: an artifact that changed silently invalidates every claim that cited
it and every run that consumed it, with no signal that anything happened.

### The conflict this package must resolve, today

`src/airl_framework/contracts.py`'s `ArtifactManifest` requires a **bare
64-character** lowercase digest. `src/airl_bridge` produces `"sha256:<hex>"`.
The contract and the only real data in the system disagree — finding **H4**, and
the module's own docstring says so: *the contract is violated by the only data
that exists.*

This is not a formatting quibble. A content address with an implicit algorithm is
a content address that cannot be migrated when the algorithm changes, and one with
an explicit prefix cannot be compared to one without. The package must pick, and
picking means one of the two existing implementations changes.

The prefixed form is the better choice — it is what SWHID, OCI and sigstore all
do, and `AETHRION_COMPONENT_REUSE.md` adopts all three — but that is an argument
to be recorded in the package, not assumed here.

### `INVALIDATED` is a state, not a deletion

An artifact that turns out to be wrong is not removed; it is marked, and the
things that depended on it are reachable. This is the same property the gate model
needs for G10 supersession, and it is why `00_PROGRAM/01` invariant 6 requires
derived state to be rebuildable while artifacts are not.

The subtlety: `INVALIDATED` must propagate as a **query result**, not as a
rewrite. Marking an artifact invalid and then updating every downstream record is
a rewrite of history. Marking it invalid and letting downstream queries see the
state is the loop closing.

### Legal hold and retention are not the same control

T05 groups them, and they must not collapse. Retention says when something *may*
be deleted; legal hold says it **may not be**, overriding retention. A system that
implements retention alone will eventually delete something under hold, and the
failure is discovered by a lawyer rather than by a check.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |

### Full prerequisite closure

**12 of 141 packages (9%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 19 — `WP-015` · `WP-017` · `WP-018` · `WP-019` · `WP-020` · `WP-026` · `WP-043` · `WP-054` · `WP-058` · `WP-063` · `WP-072` · `WP-076` · `WP-081` · `WP-082` · `WP-084` · `WP-086` · `WP-090` · `WP-138` · `WP-139`
- **Transitively reachable:** **125 of 141 packages (89%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **10** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Data Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Gates touched | `G3–G9` |
| Controls | `CTL-DAT-01` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-23 — Artifact Overwrite Attempt](../12_ACCEPTANCE_SCENARIOS/acc_23_artifact_overwrite.md) | Critical | The overwrite is rejected; the new bytes can only be written as a new content address and version, and existing references are unchanged. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md)
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
- **Data Platform Lead** carries the acceptance decision; **Reproducibility Engineer** must verify independently of whoever implements.
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
| WP-014-T01 | Write the `ArtifactRecord` and `ContentAddress` schema | Implementation owner | Commit / configuration / record reference |
| WP-014-T02 | Add the split, lineage and licence fields to `DatasetManifest` | Implementation owner | Commit / configuration / record reference |
| WP-014-T03 | Define the environment, OCI and SBOM references | Implementation owner | Commit / configuration / record reference |
| WP-014-T04 | Write new-version and `INVALIDATED` semantics in place of overwrite | Implementation owner | Commit / configuration / record reference |
| WP-014-T05 | Add object-lock, retention and legal-hold metadata | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ArtifactRecord schema`
- `DatasetManifest schema`
- `Environment reference schema`
- `Immutability lifecycle`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-014_artifact_manifest_contracts.tests.md`](wp_014_artifact_manifest_contracts.tests.md).

- A negative test writing different bytes to the same URI
- Hash verification and lineage traversal tests
- A historical-reference test against an invalidated artifact
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-014_artifact_manifest_contracts.acceptance.md`](wp_014_artifact_manifest_contracts.acceptance.md), together with what this package still cannot establish.

- [ ] No artifact is accepted without a hash over its bytes.
- [ ] Every mutation produces a new version.
- [ ] If licence or retention metadata is missing, external use is `BLOCKED`.
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

A corrupted object is restored to a new key and the old record is marked `INVALIDATED`; the hash history is preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
