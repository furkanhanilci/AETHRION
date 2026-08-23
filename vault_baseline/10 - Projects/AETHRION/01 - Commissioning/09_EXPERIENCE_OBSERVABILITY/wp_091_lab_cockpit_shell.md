---
title: "WP-091 — Lab Cockpit Information Architecture and Application Shell"
aliases:
  - "WP-091"
  - "WP-091 — Lab Cockpit Information Architecture and Application Shell"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A human gains a secure cockpit that shows portfolio, project, gate, task, evidence, review, decision, cost and incident state under one correlation — without becoming a second copy of canonical state."
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g0-g10
  - aethrion/state/not-started
---

# WP-091 — Lab Cockpit Information Architecture and Application Shell

## Package card

| Field | Value |
|---|---|
| Work package | `WP-091` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Product/Experience Lead |
| Independent verifier | Accessibility Reviewer / Governance |
| Hard dependencies | WP-002, WP-012, WP-013, WP-020, WP-025, WP-030, WP-032, WP-033, WP-055 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-OBS-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_091_lab_cockpit_shell.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_091_lab_cockpit_shell.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A human gains a secure cockpit that shows portfolio, project, gate, task, evidence, review, decision, cost and incident state under one correlation — without becoming a second copy of canonical state.


## Analysis
### What this package actually decides

That the cockpit is a **view**, never a second copy of state. The purpose sentence
puts the constraint in the goal, and it is the discipline that keeps a UI from
becoming an authority: everything shown is read from a canonical API or a declared
read model, and every command goes back through Temporal.

`00_PROGRAM/01`'s ownership table lists the cockpit as a *view/derivative* of five
different canonical owners. A cockpit that caches and edits has become a sixth.

### The freshness indicator is the honesty control (T05)

A read model lags. A cockpit that shows a lagging projection without saying so
presents stale state with the confidence of current state — and a human decides
against it.

Showing the projection lag next to the data is cheap, and it is the difference
between a dashboard and an instrument.

### The BFF aggregates; it does not decide (T04)

A backend-for-frontend that computes a status the canonical services do not have
has invented state. Aggregation is joining what exists; anything else belongs in a
service with an owner.

### Accessibility is a real requirement here, not a checkbox (T06)

The cockpit is where a human makes decisions under time pressure, and
`00_PROGRAM/08` models human attention as the binding constraint. An interface that
is hard to read wastes the scarcest resource in the system — and the colour rules
that apply to the figures apply here too: **colour never carries a distinction
alone**.

### Deep links make evidence reachable in one hop (T03)

A decision-maker who has to navigate four screens to see the evidence delta will
stop looking. Every object addressable by a stable URL is what makes WP-093's
evidence-delta view usable at all.

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

9, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md) | `Requirement Registry` · `NFR scorecard` · `Traceability matrix seed` · `Scope boundary record` |
| [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md) | `Canonical Ownership Matrix` · `Field Authority Table` · `Sync direction map` · `Conflict ownership matrix` |
| [WP-013 — Project, Task, Role and Skill Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md) | `ProjectContract schemas` · `TaskContract schema` · `RoleContract schema` · `AgentResult schema` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md) | `PostgreSQL clusters` · `DB role matrix` · `Migration pipeline` · `Backup/restore configuration` |
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md) | `ProjectWorkflow implementation` · `State transition table` · `Workflow API` · `Replay fixtures` |
| [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md) | `Gate Service` · `GateRecord persistence` · `Verdict rule tests` · `Gate explanation format` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |

### Full prerequisite closure

**43 of 160 packages (27%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-055` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-092` · `WP-093` · `WP-094` · `WP-095` · `WP-102`
- **Transitively reachable:** **34 of 160 packages (21%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **25** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Product/Experience Lead |
| Independent verifier | Accessibility Reviewer / Governance |
| Gates touched | `G0–G10` |
| Controls | `CTL-GOV-01` · `CTL-OBS-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md), [WP-012 — Canonical Ownership and Field-Level Authority Matrix](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-013 — Project, Task and Role Contract Schemas](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA and Registry Data Foundation](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-032 — ProjectLifecycle Workflow Skeleton](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-033 — Gate Service and GateRecord Evaluation](../04_CONTROL_EVENT/wp_033_gate_service_records.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md)
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
| `Requirement Registry` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `NFR scorecard` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Traceability matrix seed` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Scope boundary record` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Canonical Ownership Matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Field Authority Table` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Sync direction map` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `Conflict ownership matrix` | `WP-012` | `python3 scripts/progress.py show WP-012` |
| `ProjectContract schemas` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `TaskContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `RoleContract schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `AgentResult schema` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Contract examples` | `WP-013` | `python3 scripts/progress.py show WP-013` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `PostgreSQL clusters` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB role matrix` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Migration pipeline` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Backup/restore configuration` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `DB SLO dashboard` | `WP-025` | `python3 scripts/progress.py show WP-025` |
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Destructive projection rebuild proof` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `ProjectWorkflow implementation` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `State transition table` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Workflow API` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Replay fixtures` | `WP-032` | `python3 scripts/progress.py show WP-032` |
| `Gate Service` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `GateRecord persistence` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Verdict rule tests` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `Gate explanation format` | `WP-033` | `python3 scripts/progress.py show WP-033` |
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |

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
- **Product/Experience Lead** carries the acceptance decision; **Accessibility Reviewer / Governance** must verify independently of whoever implements.
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
| WP-091-T01 | Write the persona, task and information architecture | Implementation owner | Commit / configuration / record reference |
| WP-091-T02 | Bind OIDC, MFA, RBAC and session security | Implementation owner | Commit / configuration / record reference |
| WP-091-T03 | Establish the project/gate timeline shell and the deep-link standard | Implementation owner | Commit / configuration / record reference |
| WP-091-T04 | Write the canonical API aggregation and read-model BFF | Implementation owner | Commit / configuration / record reference |
| WP-091-T05 | Add a state freshness and projection-lag indicator | Implementation owner | Commit / configuration / record reference |
| WP-091-T06 | Apply the accessibility, i18n, error, empty and loading patterns | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Cockpit application shell`
- `Navigation/IA`
- `BFF/read APIs`
- `RBAC matrix`
- `Accessibility baseline`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-091_lab_cockpit_shell.tests.md`](wp_091_lab_cockpit_shell.tests.md).

- A role-based view and access negative test
- The stale-projection banner
- Keyboard and screen-reader flows
- Deep navigation through canonical links
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-091_lab_cockpit_shell.acceptance.md`](wp_091_lab_cockpit_shell.acceptance.md), together with what this package still cannot establish.

- [ ] The UI never owns gate state.
- [ ] Every critical decision surface shows an evidence summary and a freshness indicator.
- [ ] No unauthorised D2+ field reaches the browser.
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

A UI release is reverted by feature flag or canary; canonical workflows are unaffected.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
