---
title: "WP-022 — Repository Topology and Code Ownership"
aliases:
  - "WP-022"
  - "WP-022 — Repository Topology and Code Ownership"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Boundaries and owners for the control plane, services, schemas, policy, IaC, workflows, agents, tests and docs are made explicit in the repository structure."
source: "planning/commissioning/03_FOUNDATION/WP-022_repository_topology.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/m
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-022 — Repository Topology and Code Ownership

## Package card

| Field | Value |
|---|---|
| Work package | `WP-022` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Platform Lead / Security |
| Hard dependencies | WP-010, WP-020 |
| Related gates | Platform |
| Related controls | CTL-SUP-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_022_repository_topology.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_022_repository_topology.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Boundaries and owners for the control plane, services, schemas, policy, IaC, workflows, agents, tests and docs are made explicit in the repository structure.


## Analysis
### What this package actually decides

Which direction dependencies are allowed to point. The directory layout is the
visible part; the dependency rule is the load-bearing one, because a layout with
no enforced direction becomes a graph within one refactor.

### This repository already has the artifact and the violation

`dependency-rules.txt` exists at the root, states the target direction, and says
plainly what is not true yet:

> **NOT YET MACHINE-ENFORCED.** See `docs/review/` finding C3.
> Known violation (finding H4): `src/airl_bridge` does NOT import
> `src/airl_framework` at all — the contract core has zero production consumers.
> The rule above states the TARGET, not the current state.

That is an unusually honest artifact and it is also the package's brief: turn a
declared direction into a check. `import-linter` or `tach` wired into CI is named
as the target, and CI is WP-024 — so this package's enforcement half depends on
the package after it.

### CODEOWNERS is a real constraint, not a review convenience (T03)

The repository's own `CODEOWNERS` says it: *a path with no owner has no
accountable reviewer and cannot reach `ACCEPTED`*. That makes ownership coverage
an acceptance criterion rather than a nicety, and it makes an unowned path a
blocker rather than a gap.

### The monorepo decision needs an ADR because it is reopenable (T01)

T01 asks for the decision *with an ADR*, and WP-010's rule applies: the ADR needs
a reopen trigger naming an observable. "If the repository gets too large" cannot
fire. "If CI wall-clock for an unrelated change exceeds N minutes" can.

### Generated areas must be separated structurally (T05)

This repository has already learned the cost of not doing it: `docs/STATUS.md`,
`docs/READY.md`, the figures, the workstream indexes, the vault mirrors and now
the package companions are all generated, and each one that was ever hand-edited
was silently reverted on the next run. Separating generated, migration and
fixture areas is what lets a check say *you edited an output* instead of a human
noticing later.

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
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |

### Full prerequisite closure

**20 of 141 packages (14%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-023` · `WP-024` · `WP-027` · `WP-073` · `WP-101`
- **Transitively reachable:** **106 of 141 packages (75%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **15** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Chief Architect |
| Independent verifier | Platform Lead / Security |
| Gates touched | `Platform` |
| Controls | `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md)
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
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |

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
- **Chief Architect** carries the acceptance decision; **Platform Lead / Security** must verify independently of whoever implements.
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
| WP-022-T01 | Close the monorepo versus polyrepo decision with an ADR | Implementation owner | Commit / configuration / record reference |
| WP-022-T02 | Create the service and bounded-context directories | Implementation owner | Commit / configuration / record reference |
| WP-022-T03 | Define CODEOWNERS and the protected paths | Implementation owner | Commit / configuration / record reference |
| WP-022-T04 | Write the shared-library and dependency-direction rules | Implementation owner | Commit / configuration / record reference |
| WP-022-T05 | Separate the generated-code, migration and test-fixture areas | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Repository skeleton`
- `CODEOWNERS`
- `Dependency rules`
- `Developer guide`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-022_repository_topology.tests.md`](wp_022_repository_topology.tests.md).

- An architecture dependency lint
- A protected-path approval test
- A build-graph smoke test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-022_repository_topology.acceptance.md`](wp_022_repository_topology.acceptance.md), together with what this package still cannot establish.

- [ ] The canonical schema, policy and IaC owners are distinct.
- [ ] No circular dependency exists between bounded contexts.
- [ ] A standard scaffold exists for creating a new service.
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

- Infrastructure built by hand once is infrastructure that cannot be rebuilt under pressure.
- A backup that has never been restored is not a backup.
- Environment parity erodes from the staging side first, and quietly.

## Rollback / compensation

A wrong topology is reversed on a migration branch; repository history is never rewritten.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
