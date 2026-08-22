---
title: "WP-013 — Project, Task, Role and Skill Contract Schemas"
aliases:
  - "WP-013"
  - "WP-013 — Project, Task, Role and Skill Contract Schemas"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Project intent, role, risk, data, tooling, budget, acceptance and independence fields travel between the lifecycle and the agent runtime as versioned contracts, so that no provider-specific detail leaks into the canonical layer."
source: "planning/commissioning/02_CONTRACTS/WP-013_project_task_role_contracts.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/g0-g6
  - aethrion/state/not-started
---

# WP-013 — Project, Task, Role and Skill Contract Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-013` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Control Plane Lead |
| Independent verifier | Governance Lead |
| Hard dependencies | WP-003, WP-004, WP-005, WP-006, WP-007, WP-011 |
| Related gates | G0–G6 |
| Related controls | CTL-GOV-01, CTL-DAT-02 |
| Related acceptance scenarios | ACC-46, ACC-48, ACC-51 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_013_project_task_role_contracts.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_013_project_task_role_contracts.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Project intent, role, risk, data, tooling, budget, acceptance and independence fields travel between the lifecycle and the agent runtime as versioned contracts, so that no provider-specific detail leaks into the canonical layer.


## Analysis

### What this package actually decides

What crosses the boundary between the lifecycle and the agent runtime — and,
more importantly, what may not. The purpose sentence carries the whole
constraint: *no provider-specific detail leaks into the canonical layer.*

That is `PR-10` — vendor lock-in — expressed as a contract rather than as a
policy. A `TaskContract` with a `temperature` field has already lost: the
canonical layer now encodes one provider's parameterisation, and swapping the
provider becomes a schema migration.

### The three sub-tasks that were added after the audit

T06, T07 and T08 are not original to the package, and each closes a specific gap:

**T06 — `skill_bundle_hash` in the evidence chain.** Skills change agent
behaviour. A result produced under one skill bundle is not comparable to one
produced under another, exactly as with a policy bundle or a model snapshot.
`00_PROGRAM/09` versions the skill bundle for this reason. Putting the hash in
`TaskContract` and into the evidence chain is what makes a run's *discipline*
reproducible, not only its inputs. Nothing else in the plan carries this.

**T07 — `work_domain`, `research_mode`, `execution_path` with fail-closed
defaults.** The classification that routes a task. Fail-closed matters for the
same reason it does in WP-005: an unclassified task must not take the permissive
path, because classification is effort and the default is where the pressure lands.

**T08 — `RoleBinding` as separation constraints rather than headcount.** This is
ADR-001's mechanism. Without it, independence is a claim about how many people
exist; with it, independence is a property of a binding that a machine can refuse.

### `AgentResult` must carry gaps and assumptions (T04)

An agent that returns only its answer has thrown away the most useful part of its
output. `AgentResult` requiring explicit `gaps` and `assumptions` fields is the
contract-level expression of this repository's central thesis: model output is a
**hypothesis**, and a hypothesis that does not state what it assumed cannot be
checked.

This is cheap to specify and easy to let rot. The field will be present and
empty. The acceptance criterion therefore has to be about non-emptiness on real
tasks, not about the field existing.

### Contract versioning is where this package fails quietly

T05's backward-compatibility rule is the difference between a contract and a
shared struct. `00_PROGRAM/09` already states the rule — a schema version is
registered, never redefined — and `src/airl_framework/contracts.py`'s
`SchemaRegistry` already refuses redefinition in-process. What does not exist is
CI enforcement: BVC-01 is written and staged at `deploy/bvc-01-verify.yml` and has
never run, and the WP-024 platform that finding **H5** names is absent.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md) | `Role Catalog` · `RACI matrix` · `Role-combination policy` · `Role assignment workflow` |
| [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md) | `Decision policy` · `SLA/escalation table` · `Delegation matrix` · `Decision rationale rubric` |
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |

### Full prerequisite closure

**11 of 141 packages (8%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

- **Directly unblocked:** 15 — `WP-020` · `WP-032` · `WP-034` · `WP-035` · `WP-038` · `WP-041` · `WP-042` · `WP-045` · `WP-046` · `WP-047` · `WP-049` · `WP-069` · `WP-091` · `WP-097` · `WP-100`
- **Transitively reachable:** **121 of 141 packages (86%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **9** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Control Plane Lead |
| Independent verifier | Governance Lead |
| Gates touched | `G0–G6` |
| Controls | `CTL-GOV-01` · `CTL-DAT-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-003 — Role Catalogue and RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md), [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
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
| `Role Catalog` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `RACI matrix` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `Role-combination policy` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `Role assignment workflow` | `WP-003` | `python3 scripts/progress.py show WP-003` |
| `Decision policy` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `SLA/escalation table` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Delegation matrix` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Decision rationale rubric` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
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
- **Control Plane Lead** carries the acceptance decision; **Governance Lead** must verify independently of whoever implements.
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
| WP-013-T01 | Define the `ProjectCharter` and `ControlPlan` contract | Implementation owner | Commit / configuration / record reference |
| WP-013-T02 | Write the `TaskContract` input, output, non-goal and acceptance fields | Implementation owner | Commit / configuration / record reference |
| WP-013-T03 | Add the `RoleContract` mandate, tool, data, risk and prohibited-action fields | Implementation owner | Commit / configuration / record reference |
| WP-013-T04 | Define the `AgentResult` format including gaps and assumptions | Implementation owner | Commit / configuration / record reference |
| WP-013-T05 | Write the backward-compatibility and contract versioning rules | Implementation owner | Commit / configuration / record reference |
| WP-013-T06 | Add the **skill binding fields** to `TaskContract` (see below) and make `skill_bundle_hash` part of the evidence chain | Implementation owner | Schema + a task record carrying a resolved bundle |
| WP-013-T07 | Add the **classification fields** `work_domain`, `research_mode` and `execution_path`, with fail-closed defaults | Implementation owner | Schema + decision-table tests |
| WP-013-T08 | Define `RoleBinding` so that a **role is a function, not a person**: separation and combination constraints instead of headcount | Implementation owner | Schema + a binding that legally combines two roles and one that cannot |

### Skill binding — the fields this package must add

A `RoleContract` says *who*; a skill says *how*. Without these fields the skill
layer cannot become a runtime obligation, and "which procedure produced this
claim?" stays unanswerable after the fact.

```yaml
TaskContract:
  work_domain:    engineering | scientific-research | mixed
  research_mode:  exploratory | replication | confirmatory   # fail-closed: confirmatory
  execution_path: spike | bounded | architectural            # fail-closed: architectural

  skills_required:        ["airl:preregistration-discipline"]   # policy-derived, not chosen
  skills_selected:        ["airl:preregistration-discipline@1.0.0"]
  skills_loaded:          ["airl:preregistration-discipline@1.0.0"]
  skill_versions:         {...}
  skill_bundle_hash:      "sha256:..."
  skill_selection_reason: "research_mode=confirmatory -> rule R-07"
  skill_policy_version:   "skill-policy@1.2.0"
```

`skills_required` is produced by policy from the classification fields;
`skills_selected` is what the compiler resolved; `skills_loaded` is what the
runtime actually loaded. **A divergence between the three is a finding, not a
detail** — it is the mechanism by which "the agent ignored the procedure"
becomes visible rather than deniable.

### `RoleBinding` — role is a function, not a person

```yaml
RoleBinding:
  role_id: statistical_methods_owner
  role_type: governance_function
  actor:
    human: <identity>            # optional
    model_profile: <profile>     # optional
    mechanical: <service>        # optional
  separation:
    must_be_independent_from: [experiment_analyst]
    can_combine_with:         [scientific_owner]
    cannot_combine_with:      [final_independent_verifier]
```

This does **not** resolve finding C2 — who may verify in a small organisation
remains a decision. It gives that decision a form: independence expressed as
**separation constraints** rather than as headcount, so a one-person operation
can be modelled honestly instead of being declared impossible.

## Mandatory deliverables

- `ProjectContract schemas`
- `TaskContract schema`
- `RoleContract schema`
- `AgentResult schema`
- `Contract examples`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-013_project_task_role_contracts.tests.md`](wp_013_project_task_role_contracts.tests.md).

- Positive and negative schema fixtures
- Unknown-field and version-compatibility tests
- Forbidden-tool and missing-acceptance tests
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-013_project_task_role_contracts.acceptance.md`](wp_013_project_task_role_contracts.acceptance.md), together with what this package still cannot establish.

- [ ] No runtime- or provider-specific field leaks into a canonical contract.
- [ ] Every task carries an owner, a budget, acceptance criteria and an allowed scope.
- [ ] Gaps and assumptions are visible as self-declarations and are never counted as a pass.
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

An incompatible contract is rejected; the adapter continues to support the previous contract version through an explicit converter.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
