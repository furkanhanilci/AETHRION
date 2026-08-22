# WP-008 — G0–G10 Gate and Assurance Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-008` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Safety Owner |
| Hard dependencies | WP-004, WP-005, WP-007 |
| Related gates | G0–G10 |
| Related controls | CTL-GOV-01, CTL-EPI-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-008_gate_policy_g0_g10.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-008_gate_policy_g0_g10.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Each gate's invariant purpose, entry and exit artifacts, hard blockers, risk-based depth, reopen behaviour and escalation path are closed out in a single policy baseline.


## Analysis

### What this package actually decides

What a gate is permitted to let through. Eleven gates, each with an invariant
purpose, entry and exit artifacts, hard blockers and a reopen rule — and the
decision that carries the package is **which blockers can never be waived**.

A gate with a waiver path for every blocker is a checkpoint. A gate with a
non-waivable list is a control. The distance between them is this package.

### The rule about depth versus identity

`00_PROGRAM/01` states it: *risk changes only gate depth. Gate identity and the
requirement to produce a `GateRecord` never change.* This is subtler than it
looks. It means a low-risk project does not **skip** G6; it passes a shallower
G6 that still produces a record. The record is what makes the shallow path
auditable later, and what makes it possible to ask, after a failure, whether the
depth was chosen correctly.

T03 encodes the corollary: gates may close in one session, but they must still
produce **separate records**. A single combined record for G2 through G4 destroys
the ability to say which gate the error passed.

### Reopen rules are the package's least obvious deliverable

T04 defines reopen behaviour for protocol, literature, run, review and
reproduction changes. Without this, `VERIFIED` becomes terminal — and the
architecture's stated property is precisely that it is **not**: the loop closes,
and a retracted source must reach every dependent claim.

A gate model without reopen rules produces a system that can only ever move
forward, which is the same system with the evidence chain removed.

### G10 supersession is where the loop actually closes

T06 is small in the task list and large in consequence. Supersession is how a
claim stops being current without being deleted, and `ImpactCase` is how an
external change reaches the claims that depended on it. If this is under-specified
here, G10 becomes a monitoring dashboard rather than a gate, and the retraction
scenario (`ACC-04`) has nothing to bind to.

### The failure mode

Gate theatre: every gate produces a record, every record says pass, and no gate
has ever blocked anything. The counter-control is that the package must
demonstrate each **hard blocker actually blocking** — not that the gate can run,
but that it can refuse.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md) | `Decision policy` · `SLA/escalation table` · `Delegation matrix` · `Decision rationale rubric` |
| [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md) | `RiskProfile schema semantics` · `AssuranceClass decision tables` · `Promotion rules` · `Worked examples` |
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |

### Full prerequisite closure

**6 of 141 packages (4%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` |
| 4 | `WP-004` · `WP-007` |

### What acceptance of this package releases

- **Directly unblocked:** 9 — `WP-009` · `WP-010` · `WP-032` · `WP-033` · `WP-035` · `WP-036` · `WP-037` · `WP-081` · `WP-092`
- **Transitively reachable:** **132 of 141 packages (94%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **5** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Research Director |
| Independent verifier | Assurance Lead / Safety Owner |
| Gates touched | `G0–G10` |
| Controls | `CTL-GOV-01` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-004 — Human Decision, SLA, Delegation and Escalation Policy](../01_GOVERNANCE/WP-004_human_decision_sla_delegation.md), [WP-005 — Research Risk and Assurance Profile](../01_GOVERNANCE/WP-005_risk_assurance_profile.md), [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md)
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
| `Decision policy` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `SLA/escalation table` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Delegation matrix` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `Decision rationale rubric` | `WP-004` | `python3 scripts/progress.py show WP-004` |
| `RiskProfile schema semantics` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `AssuranceClass decision tables` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Promotion rules` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `Worked examples` | `WP-005` | `python3 scripts/progress.py show WP-005` |
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |

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
- **Research Director** carries the acceptance decision; **Assurance Lead / Safety Owner** must verify independently of whoever implements.
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
| WP-008-T01 | Write the entry/exit conditions and `GateRecord` fields for G0–G10 | Implementation owner | Commit / configuration / record reference |
| WP-008-T02 | Bind the R1/R2/R3 assurance overlays to each gate | Implementation owner | Commit / configuration / record reference |
| WP-008-T03 | Define the rule that gates may close in one session but must still produce separate records | Implementation owner | Commit / configuration / record reference |
| WP-008-T04 | Write the reopen rules for protocol, literature, run, review and reproduction changes | Implementation owner | Commit / configuration / record reference |
| WP-008-T05 | Map the non-waivable blockers and the residual-risk acceptance boundary | Implementation owner | Commit / configuration / record reference |
| WP-008-T06 | Define G10 supersession and impact behaviour | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Gate Policy v1`
- `Gate artifact matrix`
- `Reopen/return transition table`
- `Gate owner matrix`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-008_gate_policy_g0_g10.tests.md`](WP-008_gate_policy_g0_g10.tests.md).

- A happy-path state walkthrough
- At least one hard-fail test per gate
- A test of risk-based depth and of separate `GateRecord` emission
- A G7 fail → `CHALLENGED` return-path test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-008_gate_policy_g0_g10.acceptance.md`](WP-008_gate_policy_g0_g10.acceptance.md), together with what this package still cannot establish.

- [ ] All eleven gates have an owner, entry/exit artifacts, acceptance criteria and blockers.
- [ ] A low risk class reduces depth but never removes a gate.
- [ ] A critical blocker cannot be passed by human override.
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

A new gate policy is never applied directly to open workflows; it is promoted through an impact scan and a versioned transition.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
