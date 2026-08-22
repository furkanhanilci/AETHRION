---
title: "WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows"
aliases:
  - "WP-035"
  - "WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Method, literature set, baseline, falsification plan, stop rules and the decision to open compute are frozen as versioned artifacts behind gates."
source: "planning/commissioning/04_CONTROL_EVENT/WP-035_g2_g4_workflows.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/04-control-event
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g2
  - aethrion/gate/g3
  - aethrion/gate/g4
  - aethrion/state/not-started
---

# WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows

## Package card

| Field | Value |
|---|---|
| Work package | `WP-035` |
| Workstream | `04_CONTROL_EVENT` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Scientific Workflow Lead |
| Independent verifier | Methodologist / Evidence Lead / Falsification Lead |
| Hard dependencies | WP-008, WP-013, WP-017, WP-019, WP-032, WP-033, WP-034 |
| Related gates | G2,G3,G4 |
| Related controls | CTL-EPI-02, CTL-LIT-01, CTL-CST-01 |
| Related acceptance scenarios | ACC-01, ACC-39 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_035_g2_g4_workflows.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_035_g2_g4_workflows.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Method, literature set, baseline, falsification plan, stop rules and the decision to open compute are frozen as versioned artifacts behind gates.


## Analysis
### What this package actually decides

That method is fixed before results are seen. Everything the programme claims
about confirmatory research rests on this one property, and it is the property
that cannot be added afterwards: a protocol frozen after the first look is not a
protocol.

`preregistration-discipline` and `writing-analysis-plans` are the skills; this
package is the workflow that makes them binding.

### Amendment is the honest half (T01)

Protocols do change, and forbidding it produces either paralysis or quiet
deviation. The rule is that an amendment is **versioned and recorded before the
data is seen** — the amendment's timestamp relative to the run is the whole
control. An amendment applied after the result is not an amendment, it is a
different study.

### `LiteratureSetManifest` freeze is what makes a claim's evidence base fixed (T03)

An unfrozen literature set follows the registry. The claim then rests on whatever
the set contained when someone last looked, which is unrecoverable. Freezing
converts it into a citable object — and WP-017's retraction status must be visible
*through* the frozen set without mutating it.

### Leakage and contamination checks belong before compute opens (T05)

`PR-15` names eval contamination. The check is cheap at G4 and impossible
afterwards: once the golden set has appeared in a prompt, no amount of later
analysis separates a real result from a memorised one.

### The falsification plan is what distinguishes this from a demonstration (T04)

`00_PROGRAM/01`'s G4 blocker is *leakage, or no counter-test*. A study designed
only to confirm will confirm. The `FalsificationPlan` names in advance what
observation would overturn the hypothesis — and `ACC-08`, the strong counter-test,
is what checks that the plan was real.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

7, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md) | `Gate Policy v1` · `Gate artifact matrix` · `Reopen/return transition table` · `Gate owner matrix` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md) | `Gate Service` · `GateRecord persistence` · `Verdict rule tests` · `Gate explanation format` |
| [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md) | `G0/G1 workflows` · `Intake/Charter UI API contract` · `ControlPlan generation` · `Gate fixtures` |

### Full prerequisite closure

**32 of 141 packages (23%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-023` · `WP-025` · `WP-026` |
| 17 | `WP-024` · `WP-028` |
| 18 | `WP-027` |
| 19 | `WP-031` |
| 20 | `WP-032` |
| 21 | `WP-033` |
| 22 | `WP-034` |

### What acceptance of this package releases

- **Directly unblocked:** 9 — `WP-036` · `WP-040` · `WP-069` · `WP-081` · `WP-083` · `WP-092` · `WP-102` · `WP-103` · `WP-104`
- **Transitively reachable:** **61 of 141 packages (43%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W3 — Control and runtime |
| Dependency depth | level **23** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Scientific Workflow Lead |
| Independent verifier | Methodologist / Evidence Lead / Falsification Lead |
| Gates touched | `G2` · `G3` · `G4` |
| Controls | `CTL-EPI-02` · `CTL-LIT-01` · `CTL-CST-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-39 — Negative Research Result](../12_ACCEPTANCE_SCENARIOS/acc_39_negative_result.md) | Medium | The result is neither lost nor reframed as a success; a negative run and claim artifact, the limitations and a stop/pivot/continue `DecisionRecord` are produced. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/wp_019_run_environment_repro_contracts.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md)
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
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
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
- **Scientific Workflow Lead** carries the acceptance decision; **Methodologist / Evidence Lead / Falsification Lead** must verify independently of whoever implements.
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
| WP-035-T01 | Write the protocol authoring, review and amendment workflow | Implementation owner | Commit / configuration / record reference |
| WP-035-T02 | Bind the `LiteratureCampaign` child and task contracts | Implementation owner | Commit / configuration / record reference |
| WP-035-T03 | Add the `LiteratureSetManifest` freeze activity | Implementation owner | Commit / configuration / record reference |
| WP-035-T04 | Establish baseline and `FalsificationPlan` validation | Implementation owner | Commit / configuration / record reference |
| WP-035-T05 | Add the leakage/contamination and budget-readiness checks | Implementation owner | Commit / configuration / record reference |
| WP-035-T06 | Apply the G2–G4 revise and reopen transitions | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `G2–G4 workflows`
- `Protocol amendment flow`
- `Literature freeze integration`
- `Compute-open decision`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-035_g2_g4_workflows.tests.md`](wp_035_g2_g4_workflows.tests.md).

- A version test on a material protocol change
- A test proving a literature-set change forces a new synthesis
- Denial of a post-result baseline mutation
- A hard fail on identified leakage risk
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-035_g2_g4_workflows.acceptance.md`](wp_035_g2_g4_workflows.acceptance.md), together with what this package still cannot establish.

- [ ] No expensive execution opens before G4 passes.
- [ ] Protocol and baseline carry a frozen hash.
- [ ] A newly added source never silently alters an existing manifest.
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

- Any consumer that can change gate state creates dual authority over the workflow.
- At-least-once delivery means every consumer must be idempotent, without exception.
- A workflow change that breaks open executions is a data incident, not a deploy.

## Rollback / compensation

A G2/G3/G4 revise opens a new artifact version; the relationships of previously frozen sets and runs are preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
