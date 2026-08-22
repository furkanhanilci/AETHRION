---
title: "WP-073 — Obsidian Vault, Human/Generated Zones and Templates"
aliases:
  - "WP-073"
  - "WP-073 — Obsidian Vault, Human/Generated Zones and Templates"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Obsidian carries human synthesis across project, source, concept, claim, decision and result notes, with stable AIRL identifiers, Git history and protected human/generated blocks."
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-073_obsidian_vault_model.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/m
  - aethrion/gate/g3
  - aethrion/gate/g8
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-073 — Obsidian Vault, Human/Generated Zones and Templates

## Package card

| Field | Value |
|---|---|
| Work package | `WP-073` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Knowledge Lead |
| Independent verifier | Knowledge Curator / Governance |
| Hard dependencies | WP-012, WP-017, WP-022, WP-061, WP-072 |
| Related gates | G3,G8,G10 |
| Related controls | CTL-OPS-03 |
| Related acceptance scenarios | ACC-22 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_073_obsidian_vault_model.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_073_obsidian_vault_model.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Obsidian carries human synthesis across project, source, concept, claim, decision and result notes, with stable AIRL identifiers, Git history and protected human/generated blocks.


## Analysis
### What this package actually decides

That the researcher's thinking has a home the system cannot overwrite. Obsidian is
the **human knowledge workspace**; the repository is the authority. The vault's own
landing page states the boundary:

> Obsidian is the human knowledge workspace. Zotero is the human bibliographic
> workspace. Neither is a scientific authority: claims, evidence, runs, reviews and
> decisions are governed in the repository, and what appears here under a
> *Generated view* banner is a projection of it.

### The fenced-block semantics are the whole safety property (T04)

A note has human paragraphs and generated blocks in the same file. Without an
explicit fence, a projection either overwrites the human's text or refuses to write
at all — and both make the vault less useful.

The running system solves the coarse version of this today: `obsidian.py` deletes
only files listed in its own manifest, so a human note in the generated folder
survives, and `tests/test_obsidian.py` proves it. This package takes the same
guarantee **inside** a file.

### The AIRL ID is canonical; the citation key is an alias (T06)

Better BibTeX keys are stable until someone renames a field. Binding a note to
`airl_id` and treating the citation key as an alias means a Zotero rename does not
orphan a year of notes — the same argument WP-011 makes about DOIs.

### Property standard, not convention (T01)

The vault already has a controlled vocabulary and a linter: `_meta/taxonomy.md`
holds 131 tags and `scripts/check_vault.py` runs in the verification bundle,
checking that every page carries the frontmatter its queries need and every tag is
in the vocabulary.

That linter exists because a vault without one accumulates `#claim` and `#claims`
as two ideas. This package extends the standard to the human areas that the
mirrors do not generate.

### Git history is the vault's audit trail (T05)

Obsidian has no version control of its own. The Git history is what makes a human
note's evolution reconstructable, and it is what a G6 reviewer needs when asking
*what did the researcher believe, and when*.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md) | `Repository skeleton` · `CODEOWNERS` · `Dependency rules` · `Developer guide` |
| [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md) | `Source Registry service` · `Database migrations` · `API/OpenAPI` · `Outbox events` |
| [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md) | `LiteratureSetManifest` · `Signed frozen package` · `Portable exports` · `Zotero frozen view` |

### Full prerequisite closure

**63 of 141 packages (45%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` |
| 28 | `WP-062` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-071` |
| 32 | `WP-072` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-074` · `WP-125`
- **Transitively reachable:** **25 of 141 packages (18%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **33** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Knowledge Lead |
| Independent verifier | Knowledge Curator / Governance |
| Gates touched | `G3` · `G8` · `G10` |
| Controls | `CTL-OPS-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-22 — Obsidian Human Edit Preservation](../12_ACCEPTANCE_SCENARIOS/acc_22_obsidian_human_edit.md) | High | The human field is preserved byte- and semantically; only the generated zone updates, and an unexpected conflict opens a curator case instead of an automatic overwrite. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md), [WP-061 — Canonical Source Registry Service](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md)
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
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Repository skeleton` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CODEOWNERS` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Dependency rules` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Developer guide` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Source Registry service` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Database migrations` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `API/OpenAPI` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Outbox events` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `Service runbook` | `WP-061` | `python3 scripts/progress.py show WP-061` |
| `LiteratureSetManifest` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Signed frozen package` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Portable exports` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Zotero frozen view` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Freeze/diff report` | `WP-072` | `python3 scripts/progress.py show WP-072` |

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
- **Knowledge Lead** carries the acceptance decision; **Knowledge Curator / Governance** must verify independently of whoever implements.
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
| WP-073-T01 | Establish the vault, directory, tag and property standard | Implementation owner | Commit / configuration / record reference |
| WP-073-T02 | Write the project, source, concept, claim, decision and result templates | Implementation owner | Commit / configuration / record reference |
| WP-073-T03 | Add the `source_registry_id`, `claim_id` and `run_id` link fields | Implementation owner | Commit / configuration / record reference |
| WP-073-T04 | Apply human-authored versus generated fenced-block semantics | Implementation owner | Commit / configuration / record reference |
| WP-073-T05 | Establish the Git branch, review, merge and backup rules | Implementation owner | Commit / configuration / record reference |
| WP-073-T06 | Make the Better BibTeX key an alias and the AIRL ID canonical | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Obsidian vault baseline`
- `Note templates`
- `Zone/merge policy`
- `Git workflow`
- `User guide`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-073_obsidian_vault_model.tests.md`](wp_073_obsidian_vault_model.tests.md).

- Template and schema lint
- Preservation of a human edit across a generated refresh
- Alias and canonical ID link resolution
- Git restore
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-073_obsidian_vault_model.acceptance.md`](wp_073_obsidian_vault_model.acceptance.md), together with what this package still cannot establish.

- [ ] Obsidian never substitutes for the Source Registry or the Claim Ledger.
- [ ] Free human synthesis is preserved unchanged.
- [ ] Every generated block carries provenance and a timestamp.
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

A corrupted generated block is rebuilt from the canonical record; human Git history is restored from version control.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
