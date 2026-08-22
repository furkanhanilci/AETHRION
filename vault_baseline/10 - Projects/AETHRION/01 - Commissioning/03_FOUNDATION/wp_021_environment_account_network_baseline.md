---
title: "WP-021 — Development, Staging and Production Environment Baseline"
aliases:
  - "WP-021"
  - "WP-021 — Development, Staging and Production Environment Baseline"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Accounts and subscriptions, regions, VPC and network layout, DNS, encryption, administrative access and the environment promotion boundaries are separated in a production-ready configuration."
source: "planning/commissioning/03_FOUNDATION/WP-021_environment_account_network_baseline.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-021 — Development, Staging and Production Environment Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-021` |
| Workstream | `03_FOUNDATION` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Lead |
| Independent verifier | Security Architect / SRE |
| Hard dependencies | WP-001, WP-006, WP-010, WP-020 |
| Related gates | Platform |
| Related controls | CTL-DAT-02, CTL-SEC-02 |
| Related acceptance scenarios | ACC-18, ACC-27 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_021_environment_account_network_baseline.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_021_environment_account_network_baseline.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Accounts and subscriptions, regions, VPC and network layout, DNS, encryption, administrative access and the environment promotion boundaries are separated in a production-ready configuration.


## Analysis
### What this package actually decides

Where the blast radius of a mistake stops. Three accounts with three trust
boundaries is not administrative tidiness — it is the only control that makes a
production incident survivable when the same operator holds every role.

For a solo laboratory this matters more, not less. ADR-001 already concedes that
personnel separation is unavailable; **environment separation is the substitute
that can still be enforced mechanically**, because an account boundary does not
care who is typing.

### Break-glass is the sub-task that decides the package (T04)

Every access model has a path that bypasses it. The question is whether that path
is *designed* or *discovered*. A designed break-glass has MFA, a time limit, an
automatic incident, and a reconciliation afterwards; a discovered one is a
long-lived administrative credential someone kept because deployments were
failing at 2am.

`00_PROGRAM/09` already states the rule — a break-glass change opens an incident
and a reconciliation — so this package's job is to make the path *exist* on those
terms rather than to forbid it.

### Promotion is a direction, not a permission (T05)

dev → staging → prod. The rule that carries weight is the negative one: nothing
moves backwards, and production data never seeds a lower environment. Seed data
flowing down is how production personal data ends up in a dev database that
nobody classified, and it is the most common route to `PR-14` and to a privacy
finding that no code review would have caught.

### The residency and key model is a data-class decision (T03)

Region choice looks like an infrastructure preference until a D3 artifact lands
in the wrong one. Keys, regions and data classes are decided together here so
that WP-006's `ExecutionProfile` has somewhere real to point.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/wp_001_commissioning_charter.md) | `CommissioningCharter` · `Program authority matrix` · `Initial budget envelope` · `Executive DecisionRecord` |
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
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

- **Directly unblocked:** 13 — `WP-025` · `WP-026` · `WP-027` · `WP-028` · `WP-029` · `WP-031` · `WP-041` · `WP-051` · `WP-052` · `WP-055` · `WP-056` · `WP-057` · `WP-096`
- **Transitively reachable:** **116 of 141 packages (82%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **15** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Platform Lead |
| Independent verifier | Security Architect / SRE |
| Gates touched | `Platform` |
| Controls | `CTL-DAT-02` · `CTL-SEC-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-18 — D3 Data to a Public Provider](../12_ACCEPTANCE_SCENARIOS/acc_18_d3_public_route.md) | Critical | No public provider call is made; a secure or local eligible route is chosen if one exists, otherwise the task is `BLOCKED`, and an audit record is written. |
| [ACC-27 — Regional / Management Plane DR](../12_ACCEPTANCE_SCENARIOS/acc_27_regional_dr.md) | Critical | Temporal workflow state holds at RPO = 0, canonical registries, artifacts and audit records are intact, service returns within the RTO target, and derived views are rebuilt. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/wp_001_commissioning_charter.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md)
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
| `CommissioningCharter` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Program authority matrix` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Initial budget envelope` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Executive DecisionRecord` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
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

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Platform Lead** carries the acceptance decision; **Security Architect / SRE** must verify independently of whoever implements.
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
| WP-021-T01 | Separate the dev, staging and production accounts and their trust boundaries | Implementation owner | Commit / configuration / record reference |
| WP-021-T02 | Design the management, data and execution network segments | Implementation owner | Commit / configuration / record reference |
| WP-021-T03 | Establish the region, data-residency and encryption-key model | Implementation owner | Commit / configuration / record reference |
| WP-021-T04 | Restrict administrative and break-glass access behind MFA | Implementation owner | Commit / configuration / record reference |
| WP-021-T05 | Write the environment promotion and seed-data rules | Implementation owner | Commit / configuration / record reference |
| WP-021-T06 | Review the baseline IaC plan | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Environment topology`
- `Account/network IaC`
- `Access baseline`
- `Environment promotion policy`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-021_environment_account_network_baseline.tests.md`](wp_021_environment_account_network_baseline.tests.md).

- A cross-environment access negative test
- An encryption and key-ownership verification
- A production-route and break-glass tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-021_environment_account_network_baseline.acceptance.md`](wp_021_environment_account_network_baseline.acceptance.md), together with what this package still cannot establish.

- [ ] No production credential exists in any lower environment.
- [ ] The D3/D4 region and network policy is enforceable, not merely stated.
- [ ] The whole environment can be rebuilt from IaC.
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

On an IaC apply failure, roll back or destroy within the transaction scope; no manual intervention is performed against a shared production resource.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
