---
title: "WP-010 — Architecture Decision and Rejected-Alternatives Baseline"
aliases:
  - "WP-010"
  - "WP-010 — Architecture Decision and Rejected-Alternatives Baseline"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "The Temporal/LangGraph/NATS, Source Registry/Zotero/Obsidian, canonical-record, trust-zone and cutover decisions are captured in an ADR baseline together with the triggers that would reopen them."
source: "planning/commissioning/01_GOVERNANCE/WP-010_adr_baseline.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/m
  - aethrion/gate/program
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-010 — Architecture Decision and Rejected-Alternatives Baseline

## Package card

| Field | Value |
|---|---|
| Work package | `WP-010` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Architecture Board |
| Hard dependencies | WP-002, WP-005, WP-006, WP-007, WP-008, WP-009 |
| Related gates | Program,Platform |
| Related controls | CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_010_adr_baseline.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_010_adr_baseline.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The Temporal/LangGraph/NATS, Source Registry/Zotero/Obsidian, canonical-record, trust-zone and cutover decisions are captured in an ADR baseline together with the triggers that would reopen them.


## Analysis

### What this package actually decides

Which decisions are closed, and **what would reopen them**. The second half is
the package's real content. An ADR that records a choice without its reopen
trigger produces a decision nobody can revisit responsibly: the alternatives are
gone, the trade-off is gone, and re-litigating it costs as much as making it did.

T03 makes the trigger mandatory for every decision. That is what turns an ADR
baseline from a historical record into a live control.

### Why the rejected alternatives are mandatory (T02)

Because the value of an ADR is almost entirely in the paths not taken. Six months
later the question is never "what did we choose" — that is visible in the code.
It is "did we consider X", and an ADR that cannot answer it will be overruled by
whoever asks, correctly, since there is no evidence the question was considered.

### The decisions this package must close

The binding set is already listed in `planning/commissioning/README.md` §2:
Temporal as the single process authority, LangGraph bounded to one task, NATS
carrying events but never gate state, the Source Registry as canonical
bibliographic owner, Zotero as read-only personal seed, Obsidian as the human
synthesis surface, the Claim/Evidence Ledger as canonical claim owner, separate
risk/execution/independence profiles, and the single-cutover rule.

Three ADRs already exist and are `ACCEPTED` — ADR-001 (solo-operator
independence), ADR-002 (bootstrap verification control), ADR-003 (trusted control
and policy). This package does not restate them; it **absorbs** them into one
baseline and reconciles them with the list above, so there is a single answer to
"what has been decided".

### The consequence links are what make an ADR enforceable

T04 requires each decision's canonical-owner and trust-boundary consequences to
be linked. "NATS never holds gate state" is a sentence; its consequence is that a
NATS consumer changing gate state is a `PR-07` violation with a named control.
Without the link, the ADR is advice; with it, the ADR has an enforcement point.

### The failure mode

An ADR baseline that grows without a reopen ever firing. That looks like
stability and is usually the opposite: it means the triggers were written so
loosely that nothing satisfies them. A trigger like "if requirements change
significantly" cannot fire. A trigger like "if a single Temporal namespace
exceeds N open workflows, or if replay determinism fails a versioning test" can.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md) | `Requirement Registry` · `NFR scorecard` · `Traceability matrix seed` · `Scope boundary record` |
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md) | `Gate Policy v1` · `Gate artifact matrix` · `Reopen/return transition table` · `Gate owner matrix` |
| [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md) | `Control Catalog` · `ExceptionPolicy` · `NonWaivableBlocker registry` · `Control-test mapping` |

### Full prerequisite closure

**9 of 141 packages (6%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-011` · `WP-012` · `WP-021` · `WP-022` · `WP-051` · `WP-130`
- **Transitively reachable:** **130 of 141 packages (92%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **7** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Chief Architect |
| Independent verifier | Architecture Board |
| Gates touched | `Program` · `Platform` |
| Controls | `CTL-GOV-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-008 — G0–G10 Gate and Assurance Policy](../01_GOVERNANCE/wp_008_gate_policy_g0_g10.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md)
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
| `Gate Policy v1` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate artifact matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Reopen/return transition table` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Gate owner matrix` | `WP-008` | `python3 scripts/progress.py show WP-008` |
| `Control Catalog` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `ExceptionPolicy` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `NonWaivableBlocker registry` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Control-test mapping` | `WP-009` | `python3 scripts/progress.py show WP-009` |

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
- **Chief Architect** carries the acceptance decision; **Architecture Board** must verify independently of whoever implements.
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
| WP-010-T01 | Separate the binding decisions into individual ADRs | Implementation owner | Commit / configuration / record reference |
| WP-010-T02 | Write the alternatives, the trade-offs and the reason each was rejected | Implementation owner | Commit / configuration / record reference |
| WP-010-T03 | Define the reopen trigger for every decision | Implementation owner | Commit / configuration / record reference |
| WP-010-T04 | Link the canonical-owner and trust-boundary consequences of each decision | Implementation owner | Commit / configuration / record reference |
| WP-010-T05 | Establish the ADR → WP → control mapping | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Signed ADR bundle`
- `Rejected alternatives register`
- `Reopen trigger register`
- `Architecture baseline digest`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-010_adr_baseline.tests.md`](wp_010_adr_baseline.tests.md).

- A sweep for mutually contradictory ADRs
- An ADR-link check for every material package
- A reopen-trigger tabletop exercise
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-010_adr_baseline.acceptance.md`](wp_010_adr_baseline.acceptance.md), together with what this package still cannot establish.

- [ ] No contradiction remains on canonical ownership or engine boundaries.
- [ ] Every binding decision carries an accountable approver.
- [ ] The baseline digest can be embedded in a release manifest.
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

If a new baseline is not accepted, the last signed ADR bundle remains in force and dependent implementation packages do not become `READY`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
