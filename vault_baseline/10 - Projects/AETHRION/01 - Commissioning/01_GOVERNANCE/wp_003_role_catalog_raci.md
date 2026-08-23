---
title: "WP-003 — Role Catalogue and RACI Baseline"
aliases:
  - "WP-003"
  - "WP-003 — Role Catalogue and RACI Baseline"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "The mandate, decision rights, forbidden actions, required artifacts and escalation boundaries of every human, service and model actor are fixed in a single catalogue."
source: "planning/commissioning/01_GOVERNANCE/WP-003_role_catalog_raci.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/m
  - aethrion/gate/g0-g10
  - aethrion/state/not-started
---

# WP-003 — Role Catalogue and RACI Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-003` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Governance Lead |
| Independent verifier | Internal Audit |
| Hard dependencies | WP-001, WP-002 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-GOV-02 |
| Related acceptance scenarios | ACC-06, ACC-38 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_003_role_catalog_raci.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_003_role_catalog_raci.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The mandate, decision rights, forbidden actions, required artifacts and escalation boundaries of every human, service and model actor are fixed in a single catalogue.


## Analysis

### What this package actually decides

What each actor is **forbidden** to do. The mandate half of a role catalogue is
the easy half and the part that gets written; the forbidden-actions half is what
makes the catalogue enforceable, because a permission system built from mandates
alone defaults to allow.

This matters more here than in a conventional programme, because the actors are
not all human. A model actor with a mandate and no forbidden list is a model
actor that will eventually do the plausible thing.

### The rule this package must encode above all others

**A role is a function, not a person.** `00_PROGRAM/01` and
`docs/architecture/AETHRION_ROLES.md` both state it, and ADR-001 depends on it:
independence is expressed as separation constraints on a `RoleBinding`, never as
headcount. Get this wrong and the entire independence argument collapses into
"we do not have enough people", which is where the audit found it (finding C2).

Sub-task T04 — role-combination rules for a small team — is therefore not a
concession to a resource constraint. It is the mechanism by which a one-person
laboratory can hold multiple roles legally, and the place where the illegal
combinations are named. The catalogue must state which pairs may never be held by
the same binding, independently of how many operators exist.

### The scale problem this package will surface

T01 maps 36 core roles. The dependency matrix assigns **74 distinct owners and
119 distinct verifiers** across the whole package registry. Those numbers cannot both be right
unless roles are functions and bindings are many-to-one — which is precisely the
rule above. This package is where that reconciliation happens, and if it does not
happen here it will happen implicitly at every gate for the rest of the programme.

### The failure mode

An escalation boundary that terminates in the same actor it escalated from. In a
small team this happens by default: every path leads back to the operator. The
catalogue must either name a genuinely external terminus for each escalation
class, or **declare** that the class has none — the same discipline ADR-001
applied to R3.

### Baseline v1.3.0 — the invariants a cost optimiser must not be able to reach

Three additions, and they share a shape: each names something that an
efficiency argument would otherwise be free to trade away.

**The cohort is not a lever.** `ADR-011` fixes that substantial scientific
execution requires at least two epistemically independent cognitive
contributions. Independence is a five-dimension profile, not a count — several
instances of one model on one context are one contribution. Governance language
here must make that an invariant rather than a default, because the pressure to
relax it will arrive as a budget conversation.

**Two disciplines, composable, neither collapsed.** `ADR-012`. A passing test is
not a confirmed hypothesis and a preregistered analysis is not correct code. The
four pairs that get conflated — TDD against preregistration, code review against
scientific review, debugging against anomaly investigation, parallel agents
against parallel analysts — stay distinct in the role, risk and control language.

**What budget may and may not degrade.** Communication verbosity degrades; the
cohort and the assurance route do not. A task that cannot afford its required
assurance is `BLOCKED`, never quietly completed more cheaply. The new
non-waivable controls follow from that: cohort integrity, assurance-route
integrity, human preliminary judgment before recommendation, and specification
conformance for confirmatory work.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/wp_001_commissioning_charter.md) | `CommissioningCharter` · `Program authority matrix` · `Initial budget envelope` · `Executive DecisionRecord` |
| [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md) | `Requirement Registry` · `NFR scorecard` · `Traceability matrix seed` · `Scope boundary record` |

### Full prerequisite closure

**2 of 160 packages (1%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-004` · `WP-007` · `WP-013` · `WP-047` · `WP-147`
- **Transitively reachable:** **154 of 160 packages (96%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **3** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Governance Lead |
| Independent verifier | Internal Audit |
| Gates touched | `G0–G10` |
| Controls | `CTL-GOV-01` · `CTL-GOV-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |
| [ACC-38 — Critical Reviewer Unavailable](../12_ACCEPTANCE_SCENARIOS/acc_38_reviewer_unavailable.md) | High | Neither the producer, a self-review, nor an ineligible fallback is used; the gate is `BLOCKED` and a human scheduling/escalation item and a capacity signal are produced. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/wp_001_commissioning_charter.md), [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md)
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
| `CommissioningCharter` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Program authority matrix` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Initial budget envelope` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Executive DecisionRecord` | `WP-001` | `python3 scripts/progress.py show WP-001` |
| `Requirement Registry` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `NFR scorecard` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Traceability matrix seed` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Scope boundary record` | `WP-002` | `python3 scripts/progress.py show WP-002` |

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
- **Governance Lead** carries the acceptance decision; **Internal Audit** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-003`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-003-T01 | Map the 36 core roles onto durable functions and duty cells | Implementation owner | Commit / configuration / record reference |
| WP-003-T02 | Write the mandate, the input/output contract and the forbidden actions for each role | Implementation owner | Commit / configuration / record reference |
| WP-003-T03 | Establish the RACI for G0–G10 and for platform release decisions | Implementation owner | Commit / configuration / record reference |
| WP-003-T04 | Define the role-combination rules that apply to a small team | Implementation owner | Commit / configuration / record reference |
| WP-003-T05 | Define `RoleContract` versioning and the assignment lifecycle | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Role Catalog`
- `RACI matrix`
- `Role-combination policy`
- `Role assignment workflow`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-003_role_catalog_raci.tests.md`](wp_003_role_catalog_raci.tests.md).

- A sweep for decisions with no accountable role
- A negative test for self-approval on the same artifact
- A small-team R1/R3 tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-003_role_catalog_raci.acceptance.md`](wp_003_role_catalog_raci.acceptance.md), together with what this package still cannot establish.

- [ ] Every material decision has exactly one accountable (A) role.
- [ ] A producer cannot review, reproduce or accept its own output.
- [ ] No permitted role combination violates the independence policy.
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

- A policy that is written but not machine-checkable is an intention, not a control.
- Role and authority documents drift silently; every change here needs a baseline bump.
- The hardest failure in this workstream is a rule that everyone agrees with and nobody can enforce.

## Rollback / compensation

Conflicting assignments are cancelled and the last signed role baseline is restored.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
