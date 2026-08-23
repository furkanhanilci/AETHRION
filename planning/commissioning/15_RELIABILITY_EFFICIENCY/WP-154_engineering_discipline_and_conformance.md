# WP-154 — Engineering Discipline and Specification Conformance

## Package card

| Field | Value |
|---|---|
| Work package | `WP-154` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Engineering Productivity Lead / Assurance Lead |
| Hard dependencies | WP-023, WP-047, WP-081, WP-107 |
| Related gates | G2,G5,Engineering |
| Related controls | CTL-SUP-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-103, ACC-104 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-154_engineering_discipline_and_conformance.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-154_engineering_discipline_and_conformance.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The software-engineering discipline is first-class beside the scientific one, and the code that ran is compared against the specification that was frozen.


## Analysis

### What this package actually decides

Two things that turn out to be the same thing: that engineering discipline is not
absorbed into scientific discipline, and that the code implementing a frozen
method is checked against it.

`ADR-012` fixes the first. `ADR-018` fixes the second. They belong in one package
because the second is only expressible if the first holds — you cannot compare a
specification to code if the specification's discipline has been folded into the
code's.

### Four pairs that are not synonyms

| Engineering | Scientific | Why substitution fails |
|---|---|---|
| `test-driven-development` | `preregistration-discipline` | A test fixes what code must do; a preregistration fixes what a result will mean |
| `requesting-code-review` | `requesting-review` | Approving the diff says nothing about the inference |
| `systematic-debugging` | `investigating-anomalies` | Debugging assumes the expectation is right; the surprising result may be the finding |
| `dispatching-parallel-agents` | `dispatching-parallel-analysts` | One decomposes work with a right answer; the other runs independent analyses because there is none |

The eleven engineering skills stay vendored at their pinned commit and are not
rewritten here.

### Why drift survives both reviews

Code review asks whether the code is correct. It is — the simplified algorithm is
implemented cleanly and its tests pass. Scientific review reads the method
section, which describes the frozen protocol, and the method is sound.

**Neither reviewer compares the two documents.** That is the gap, and closing it
needs a distinct check with a distinct record:
`SpecificationConformanceRecord`, comparing the frozen specification against the
code that actually ran.

### The severity ladder is what makes it usable

`NONE` · `ENGINEERING_ONLY` · `SCIENTIFIC_MINOR` · `SCIENTIFIC_MAJOR` ·
`UNKNOWN`.

`ENGINEERING_ONLY` is what keeps the check from becoming noise — without it every
refactor is a scientific event, the detector cries wolf, and it gets turned off.
`UNKNOWN` is what keeps it honest: method–code alignment is a **V2** judgement
and a verifier that cannot tell must say so.

An unapproved `SCIENTIFIC_MAJOR` cannot carry a confirmatory package forward. The
minimum consequence is relabelling to exploratory, or a re-freeze and re-run —
ACC-104.

### Measured in both directions

Positive fixtures the detector must catch: metric scale swap, simplified
algorithm, omitted baseline, changed seed policy, altered data split, hidden
preprocessing, removed stopping criterion.

**And a clean implementation it must pass.** A detector that flags everything is
an obstacle whose findings get dismissed by habit, which is worse than no
detector at all.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/WP-023_git_worktree_branch_policy.md) | `Git policy` · `Worktree controller contract` · `Protected-path rules` · `Freeze procedure` |
| [WP-047 — Role and Skill Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md) | `Role Bundle Registry` · `Core role bundles` · `Bundle conformance tests` · `Cohort, topology, projection and assurance-route compilation` |
| [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md) | `Method Registry` · `Protocol validators` · `Amendment workflow` · `Post-hoc change detector` |

### Full prerequisite closure

**50 of 160 packages (31%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-107`
- **Transitively reachable:** **23 of 160 packages (14%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **29** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Chief Architect |
| Independent verifier | Engineering Productivity Lead / Assurance Lead |
| Gates touched | `G2` · `G5` · `Engineering` |
| Controls | `CTL-SUP-01` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-103 — Minor Specification Drift Is Recorded](../12_ACCEPTANCE_SCENARIOS/ACC-103_scientific_minor_spec_drift.md) | High | The bounded deviation is classified `SCIENTIFIC_MINOR`, recorded and reported with the result. The refactor is `ENGINEERING_ONLY` and changes no scientific status. |
| [ACC-104 — Major Specification Drift Blocks Confirmatory Status](../12_ACCEPTANCE_SCENARIOS/ACC-104_scientific_major_spec_drift.md) | Critical | The deviation is classified `SCIENTIFIC_MAJOR`. The confirmatory package cannot proceed: the minimum consequence is relabelling to exploratory, or a re-freeze and a re-run. A clean implementation passes. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-023 — Git, Worktree and Protected-Path Policy](../03_FOUNDATION/WP-023_git_worktree_branch_policy.md), [WP-047 — Role and **Skill** Registries, and the Task Compiler](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release](../10_INTEGRATION_CUTOVER/WP-107_engineering_vertical_slice.md)
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
| `Git policy` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Worktree controller contract` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Protected-path rules` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Freeze procedure` | `WP-023` | `python3 scripts/progress.py show WP-023` |
| `Role Bundle Registry` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Core role bundles` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Bundle conformance tests` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Cohort, topology, projection and assurance-route compilation` | `WP-047` | `python3 scripts/progress.py show WP-047` |
| `Method Registry` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Protocol validators` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Amendment workflow` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Post-hoc change detector` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `SpecificationConformanceRecord binding` | `WP-081` | `python3 scripts/progress.py show WP-081` |

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
- **Chief Architect** carries the acceptance decision; **Engineering Productivity Lead / Assurance Lead** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-154`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-154-T01 | Make the engineering skill family first-class in the Task Compiler output | Implementation owner | Commit / configuration / record reference |
| WP-154-T02 | Extend WP-107's vertical slice to spec → worktree → TDD → review → attestation → eligibility | Implementation owner | Commit / configuration / record reference |
| WP-154-T03 | Define `SpecificationConformanceRecord` and its severity model | Implementation owner | Commit / configuration / record reference |
| WP-154-T04 | Implement comparison of frozen specification against executed code | Implementation owner | Commit / configuration / record reference |
| WP-154-T05 | Bind SCIENTIFIC_MAJOR to the confirmatory-status consequence | Implementation owner | Commit / configuration / record reference |
| WP-154-T06 | Build the seven positive drift fixtures and the clean negative control | Implementation owner | Commit / configuration / record reference |
| WP-154-T07 | Write behaviour baselines for the engineering skills under pressure | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Dual-discipline task compilation`
- `SpecificationConformanceRecord`
- `Drift fixture suite`
- `Extended WP-107 engineering slice`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-154_engineering_discipline_and_conformance.tests.md`](WP-154_engineering_discipline_and_conformance.tests.md).

- A coding-science task must compile both skill families without either aliasing the other
- Each of the seven planted drifts must be detected and classified
- A clean implementation must pass — the detector must discriminate
- An unapproved SCIENTIFIC_MAJOR must block confirmatory status
- An ENGINEERING_ONLY deviation must not change scientific status
- A comparison that cannot be made confidently must report UNKNOWN, not NONE
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-154_engineering_discipline_and_conformance.acceptance.md`](WP-154_engineering_discipline_and_conformance.acceptance.md), together with what this package still cannot establish.

- [ ] Engineering and scientific skills compile together without either substituting for the other.
- [ ] Seven planted drifts are caught, a clean implementation passes, and ambiguity reports UNKNOWN.
- [ ] An unapproved major deviation cannot leave a confirmatory package confirmatory.
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

- An efficiency measure that improves a cost number and quietly lowers assurance has moved the failure, not removed it. Every optimisation here is anchored to a quality guard and rolls back when it trips.
- A coordination defect is invisible in a healthy run and obvious only in a post-mortem. These packages are specified as injection suites for that reason, not as properties.
- Multi-agent cost pressure always argues for fewer agents. The cohort is fixed by ADR-011 and is not a lever any package here may pull.

## Rollback / compensation

A conformance record is immutable and bound to a code digest: re-running after a fix produces a new record, and the deviation history of a study stays readable in order.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
