# WP-092 — Project Workspace and G0–G10 Gate Timeline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-092` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experience Lead |
| Independent verifier | Research Operations / Assurance |
| Hard dependencies | WP-008, WP-032, WP-033, WP-034, WP-035, WP-036, WP-037, WP-091 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-OPS-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-092_project_gate_timeline.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-092_project_gate_timeline.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every project gains a working surface that explains its current gate, frozen versions, blockers, budget, owner, residual risk, reopen history and next action.


## Analysis
### What this package actually decides

How a project explains itself. The gate timeline is the surface where the whole
lifecycle becomes legible: which gate, which frozen versions, which blockers, whose
decision, and **what happens next**.

### The blocker explanation is the most-used view in the system (T04)

`BLOCKED`, `REVISE`, `DISAGREEMENT` — three states a person encounters when they
wanted to proceed, and the moment where an unexplained system gets routed around.
`PR-02`'s early signal is *unexplainable decisions*, and WP-033 already requires
the verdict to name every failed check.

This is where that explanation reaches a human, and the test is the same as
WP-016's: can someone who did not write the policy state why it blocked?

### `GateRecord` diffs are what make a reopen comprehensible (T02, T05)

A gate that reopened and passed again looks identical to one that passed first
time, unless the diff is shown. The diff is what tells a reader that the protocol
changed, that the literature set moved, or that a reproduction failed and was
re-run.

### Frozen versions must be shown as versions, not as current (T01)

A project at G5 is running against a frozen protocol, a frozen literature set and a
frozen analysis plan. Showing the *current* protocol next to the run is how a
reader concludes the run used something it did not.

### Commands bind to the Temporal API (T06)

Every authorised action on this screen is an Update on the workflow, authenticated
and idempotent (WP-038). A command surface that writes state directly has made the
cockpit an authority.

### Residual risk belongs on the project page

`00_PROGRAM/05` allows accepted Medium/Low risks with a named owner and an expiry.
If they are not visible on the project's own surface, they accumulate — and an
expired accepted risk that nobody saw is an open finding.

### Baseline v1.3.0 — showing the cost of collaboration, and the shape of a decision

The experience and observability layer gains three things it could not
previously display, because they did not exist to be displayed.

**Collaboration cost.** Coordination overhead ratio, redundant message rate,
useful challenge rate, rounds, and the token ledger's seven categories. A single
cost total says a campaign was expensive; the categories say whether it was
expensive because it did science or because it held a meeting.

**The human decision surface, reordered.** Evidence first, recommendation second,
and a `DecisionDelta` when the second changes the first (`ADR-016`). The queue
uses evidence-delta priority — what changed since the last decision, not the full
state every time. **Attention priority orders and never authorises**, and no
timeout or learned preference produces an approval.

**Verifier abstention, surfaced.** An `ABSTAIN` is an escalation signal and has to
look like one in the interface. A surface that renders it as a soft pass has
undone `ADR-015`.

New SLOs: coordination overhead, challenge rate, contamination and security
findings, and the quality/cost Pareto frontier.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md) | `Gate Policy v1` · `Gate artifact matrix` · `Reopen/return transition table` · `Gate owner matrix` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md) | `Gate Service` · `GateRecord persistence` · `Verdict rule tests` · `Gate explanation format` |
| [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md) | `G0/G1 workflows` · `Intake/Charter UI API contract` · `ControlPlan generation` · `Gate fixtures` |
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-036 — G5 Execute through G9 Publish Workflows](../04_CONTROL_EVENT/WP-036_g5_g9_workflows.md) | `G5–G9 workflows` · `Review/repro integration contracts` · `Decision update flow` · `Publication transition` |
| [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md) | `ImpactScan workflow` · `Schedule registry` · `ImpactCase service contract` · `Supersession trigger` |
| [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md) | `Cockpit application shell` · `Navigation/IA` · `BFF/read APIs` · `RBAC matrix` |

### Full prerequisite closure

**48 of 160 packages (30%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-036` · `WP-055` |
| 25 | `WP-091` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-102`
- **Transitively reachable:** **26 of 160 packages (16%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **26** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Experience Lead |
| Independent verifier | Research Operations / Assurance |
| Gates touched | `G0–G10` |
| Controls | `CTL-GOV-01` · `CTL-OPS-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/WP-033_gate_service_records.md), [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-036 — G5 Execute through G9 Publish Workflows](../04_CONTROL_EVENT/WP-036_g5_g9_workflows.md), [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md)
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
| `Gate Policy v1` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate artifact matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Reopen/return transition table` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate owner matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Gate Service` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `GateRecord persistence` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Verdict rule tests` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Gate explanation format` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `G0/G1 workflows` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Intake/Charter UI API contract` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `ControlPlan generation` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Gate fixtures` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `G5–G9 workflows` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Review/repro integration contracts` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Decision update flow` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Publication transition` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `Gate consumption of collaboration and assurance policies` | `WP-036` | `python3 scripts/progress.py show WP-036` |
| `ImpactScan workflow` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Schedule registry` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `ImpactCase service contract` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Supersession trigger` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Cockpit application shell` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Navigation/IA` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `BFF/read APIs` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `RBAC matrix` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Accessibility baseline` | `WP-091` | `python3 scripts/progress.py show WP-091` |

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
- **Experience Lead** carries the acceptance decision; **Research Operations / Assurance** must verify independently of whoever implements.
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
| WP-092-T01 | Write the project overview, charter and control profile views | Implementation owner | Commit / configuration / record reference |
| WP-092-T02 | Display the G0–G10 timeline and `GateRecord` diffs | Implementation owner | Commit / configuration / record reference |
| WP-092-T03 | Bind the artifact, manifest, review, reproduction and decision panels | Implementation owner | Commit / configuration / record reference |
| WP-092-T04 | Design the `BLOCKED` / `REVISE` / `DISAGREEMENT` explanation surface | Implementation owner | Commit / configuration / record reference |
| WP-092-T05 | Add reopen, supersession and history comparison | Implementation owner | Commit / configuration / record reference |
| WP-092-T06 | Bind the authorised command and update forms to the Temporal API | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Project Workspace`
- `Gate Timeline`
- `Artifact/evidence panels`
- `Command/update forms`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-092_project_gate_timeline.tests.md`](WP-092_project_gate_timeline.tests.md).

- Visualisation of a G7 failure as a controlled return
- Risk depth shown alongside separate `GateRecord`s
- Denial of an unauthorised transition
- Projection lag versus a live canonical query
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-092_project_gate_timeline.acceptance.md`](WP-092_project_gate_timeline.acceptance.md), together with what this package still cannot establish.

- [ ] A user can see **why** they are blocked, with the rule and the evidence.
- [ ] There is no free-form state mutation from the UI.
- [ ] Older versions and decision history remain reachable.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A frontend rollback loses no state; a faulty command is rejected server-side by policy regardless of client version.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
