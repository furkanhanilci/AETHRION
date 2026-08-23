---
title: "WP-023 — Git, Worktree and Protected-Path Policy"
aliases:
  - "WP-023"
  - "WP-023 — Git, Worktree and Protected-Path Policy"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Human and agent changes proceed on separate branches and worktrees, within a permitted file scope and pinned to a fixed target commit."
source: "planning/commissioning/03_FOUNDATION/WP-023_git_worktree_branch_policy.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/s
  - aethrion/gate/g5
  - aethrion/gate/engineering
  - aethrion/state/not-started
---

# WP-023 — Git, Worktree and Protected-Path Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-023` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Engineering Lead |
| Independent verifier | Security Reviewer |
| Hard dependencies | WP-022 |
| Related gates | G5,Engineering |
| Related controls | CTL-GOV-02, CTL-SUP-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_023_git_worktree_branch_policy.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_023_git_worktree_branch_policy.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Human and agent changes proceed on separate branches and worktrees, within a permitted file scope and pinned to a fixed target commit.


## Analysis
### What this package actually decides

That an agent's write surface is bounded before the agent runs, not judged
afterwards. A worktree pinned to a fixed commit with an allowed-path manifest is
the difference between reviewing *what an agent changed* and reviewing *what an
agent was able to change*.

### Why the pinned target commit is the important half

An agent that works against a moving branch produces a diff nobody can reproduce:
the base changed underneath it. Pinning gives the review a fixed question — *is
this diff, against this commit, correct?* — and it is also what makes the
freeze-commit behaviour in T04 meaningful.

### The protected-path manifest is a policy artifact (T03)

Allowed and protected paths are the file-level expression of WP-006's
`ToolEffect`. An agent whose task is to fix a test must not be able to edit the
policy bundle, and the enforcement belongs at the worktree controller rather than
in a prompt. `ADR-003`'s rule applies directly: content crosses, authority does
not — a task description asking for a wider scope does not widen it.

### Forensic retention is the part that gets dropped (T05)

An abandoned agent task leaves a worktree. Deleting it immediately is tidy and
destroys the only record of what the agent did before it was stopped — which is
exactly what an integrity investigation needs (`investigating-integrity-concerns`).
Retention with an expiry is the answer; "clean up on exit" is not.

### Signed commits (T01) are cheap and load-bearing

Attribution is the base of every later independence claim. If a commit's author
can be set freely, then "the producer did not write this" is unverifiable, and
WP-007's human dimension has nothing to stand on.

### Baseline v1.3.0 — modular monolith first, and a projection that can be destroyed

The collaboration plane, the conformance checker and the release assurance work
land as **modules**, not as services. A logical plane is an ownership boundary;
turning each into a deployment unit before there is a consumer buys operational
cost and no assurance.

Two guarantees the foundation now owes:

**Every derived projection is destroyable.** The graph, the vector index and the
search index are rebuilt from canonical stores as a routine, tested operation —
ACC-119. A rebuild path that is an emergency procedure will not work on the day
it is needed.

**Release artifacts carry provenance.** SLSA provenance, Sigstore signatures, an
SBOM and its scan result, and the upstream register accounting for every adapted
file. `ADR-019`, delivered by WP-159 and admitted against by WP-024's CI.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

1, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md) | `Repository skeleton` · `CODEOWNERS` · `Dependency rules` · `Developer guide` |

### Full prerequisite closure

**21 of 160 packages (13%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-024` · `WP-048` · `WP-107` · `WP-144` · `WP-154`
- **Transitively reachable:** **124 of 160 packages (78%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **16** of 55 |
| On the documented critical path | no |
| Effort class | **S** |
| Accountable owner | Engineering Lead |
| Independent verifier | Security Reviewer |
| Gates touched | `G5` · `Engineering` |
| Controls | `CTL-GOV-02` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-54 — Producer Attempts Evaluator Mutation](../12_ACCEPTANCE_SCENARIOS/acc_54_evaluator_mutation_attempt.md) | Critical | Every write is denied at the policy and sandbox boundary and audited. If any write nonetheless lands, the evaluator digest mismatch invalidates the run and the scenario FAILs as a critical security defect. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/wp_022_repository_topology.md)
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
| `Repository skeleton` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CODEOWNERS` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Dependency rules` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Developer guide` | `WP-022` | `python3 scripts/progress.py show WP-022` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `S`** — small — one owner, one review cycle.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Engineering Lead** carries the acceptance decision; **Security Reviewer** must verify independently of whoever implements.
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

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-011` — CORAL — isolated candidate worktrees and private grader zone | `PATTERN` | the running implementation | the contract this is held behind | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-011` | The evaluator zone holds the official metric, hidden material and answer keys. A producer has no read or write path into it under the supported threat model. | The multi-agent society framework and its shared-state model. |

### Where a plain row would mislead

- **`ASM-011`** — Upstream separates a public shared state symlinked into every worktree from a private grader area, and a 2026 security change isolates unprivileged agents from that private area even through a shell. That hardening history is itself the evidence the boundary is load-bearing.

### Unresolved before implementation

**None.** Every obligation the modes above create has been met.

**Acquisition readiness — resolved.** All 1 registered sources have met the obligations their modes create.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-023-T01 | Write the branch/commit naming and signed-commit policy | Implementation owner | Commit / configuration / record reference |
| WP-023-T02 | Define the agent task worktree lifecycle | Implementation owner | Commit / configuration / record reference |
| WP-023-T03 | Apply the allowed/protected path manifest | Implementation owner | Commit / configuration / record reference |
| WP-023-T04 | Establish freeze-commit and correction-branch behaviour | Implementation owner | Commit / configuration / record reference |
| WP-023-T05 | Add the cleanup, abandoned-task and forensic retention rules | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Git policy`
- `Worktree controller contract`
- `Protected-path rules`
- `Freeze procedure`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-023_git_worktree_branch_policy.tests.md`](wp_023_git_worktree_branch_policy.tests.md).

- A negative test with two agents in the same ownership zone
- A protected-path write denial test
- A test proving a review is invalidated when its frozen target changes
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-023_git_worktree_branch_policy.acceptance.md`](wp_023_git_worktree_branch_policy.acceptance.md), together with what this package still cannot establish.

- [ ] Every task carries a base commit and a target commit.
- [ ] An agent writes only inside its task worktree and its allowed paths.
- [ ] A correction produces a new frozen commit rather than amending the old one.
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

When a task is cancelled the worktree is quarantined; artifacts and evidence are retained and the branch is archived on the owner's decision.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
