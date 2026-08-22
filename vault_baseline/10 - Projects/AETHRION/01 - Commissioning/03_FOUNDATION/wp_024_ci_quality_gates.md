---
title: "WP-024 — CI Foundation and Deterministic Quality Gates"
aliases:
  - "WP-024"
  - "WP-024 — CI Foundation and Deterministic Quality Gates"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Format, lint, type, unit, integration, schema, policy, security and build checks produce a standard interface and machine-readable evidence output."
source: "planning/commissioning/03_FOUNDATION/WP-024_ci_quality_gates.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/m
  - aethrion/gate/g5-g9
  - aethrion/gate/engineering
  - aethrion/state/not-started
---

# WP-024 — CI Foundation and Deterministic Quality Gates

## Package card

| Field | Value |
|---|---|
| Work package | `WP-024` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Engineering Productivity Lead |
| Independent verifier | Mechanical Verifier |
| Hard dependencies | WP-020, WP-022, WP-023 |
| Related gates | G5–G9,Engineering |
| Related controls | CTL-SUP-01, CTL-OPS-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_024_ci_quality_gates.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_024_ci_quality_gates.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Format, lint, type, unit, integration, schema, policy, security and build checks produce a standard interface and machine-readable evidence output.


## Analysis
### What this package actually decides

Whether any check in this programme is binding. Every other package's acceptance
criteria assume something fails a build; this is the package that makes a build
exist. Until it does, every check in the repository runs *because someone
remembered*, and `README.md` says exactly that: **the guarantee is "someone ran
this", not "this cannot regress".**

### This is finding H5, and the distinction that matters

`deploy/bvc-01-verify.yml` is written, sits outside `.github/workflows/` because
the committing token lacks the `workflow` scope, and **has never run**.
`deploy/README.md` is explicit that BVC-01 is a *temporary control with an owner,
an expiry and WP-024 as its retirement package*, and that it does **not** close
H5. H5 is the absence of this package, not the absence of that file.

So this package has two jobs and they are different sizes: activating BVC-01 is a
credential; building the WP-024 platform is the work.

### Machine-readable evidence is the deliverable, not the log (T03)

A CI job that prints results and exits is a signal. A CI job that emits a
`verification-summary.json` bound to a target revision is **evidence**, and
`00_PROGRAM/06`'s evidence manifest has a field waiting for it. The difference
decides whether an acceptance package can be assembled mechanically or has to be
transcribed by hand — and a transcribed result is one nobody can re-derive.

### Flaky-test quarantine needs an owner SLA or it becomes a graveyard (T05)

Quarantine without a clearing deadline is how a suite loses coverage silently:
tests move out and never move back, and the suite keeps reporting green over a
shrinking surface. The SLA — and the count of quarantined tests as a published
number — is what keeps that visible.

### The fail-fast split is a capacity decision (T04)

Cheap checks first is the same rule `00_PROGRAM/06` applies to evidence layers.
It matters here because the expensive resource is the developer's attention
between push and feedback, and a suite that takes twenty minutes to tell you
about a formatting error trains people to stop watching it.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md) | `Repository skeleton` · `CODEOWNERS` · `Dependency rules` · `Developer guide` |
| [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md) | `Git policy` · `Worktree controller contract` · `Protected-path rules` · `Freeze procedure` |

### Full prerequisite closure

**22 of 141 packages (16%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 15 | `WP-022` |
| 16 | `WP-023` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-027` · `WP-040` · `WP-087` · `WP-107` · `WP-109`
- **Transitively reachable:** **104 of 141 packages (74%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **17** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Engineering Productivity Lead |
| Independent verifier | Mechanical Verifier |
| Gates touched | `G5–G9` · `Engineering` |
| Controls | `CTL-SUP-01` · `CTL-OPS-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md), [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md)
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
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Repository skeleton` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CODEOWNERS` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Dependency rules` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Developer guide` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Git policy` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Worktree controller contract` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Protected-path rules` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Freeze procedure` | `WP-023` | `python3 scripts/progress.py show WP-023` |

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
- **Engineering Productivity Lead** carries the acceptance decision; **Mechanical Verifier** must verify independently of whoever implements.
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
| WP-024-T01 | Define the CI job taxonomy and pin the target revision | Implementation owner | Commit / configuration / record reference |
| WP-024-T02 | Add the schema, policy and architecture linters | Implementation owner | Commit / configuration / record reference |
| WP-024-T03 | Emit test results as machine-readable artifacts | Implementation owner | Commit / configuration / record reference |
| WP-024-T04 | Establish the split between fail-fast checks and the full suite | Implementation owner | Commit / configuration / record reference |
| WP-024-T05 | Define flaky-test quarantine and the owner SLA for clearing it | Implementation owner | Commit / configuration / record reference |
| WP-024-T06 | Trigger signed build provenance | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `CI pipelines`
- `Verification summary schema adapter`
- `Test ownership registry`
- `Flake policy`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-024_ci_quality_gates.tests.md`](wp_024_ci_quality_gates.tests.md).

- A known-fail fixture that must stop CI
- A negative test mixing artifacts from different commits
- A retry and flaky-classification test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-024_ci_quality_gates.acceptance.md`](wp_024_ci_quality_gates.acceptance.md), together with what this package still cannot establish.

- [ ] A failing required check cannot be bypassed.
- [ ] Evidence carries the target commit and the environment.
- [ ] Deleting or weakening a test requires owner review.
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

A faulty pipeline returns to its previous signed version; required checks are never switched off to unblock a merge.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
