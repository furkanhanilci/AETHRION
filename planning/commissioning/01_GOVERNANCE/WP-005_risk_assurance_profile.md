# WP-005 — Research Risk and Assurance Profile

## Package card

| Field | Value |
|---|---|
| Work package | `WP-005` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Research Director / Assurance Lead |
| Hard dependencies | WP-001, WP-002 |
| Related gates | G0,G1 |
| Related controls | CTL-GOV-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-005_risk_assurance_profile.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-005_risk_assurance_profile.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The materiality, uncertainty, exposure and safety/ethics/regulation dimensions produce an R1/R2/R3 assurance class through small decision tables rather than a combinatorial cross-product.


## Analysis

### What this package actually decides

How much assurance a piece of work has to survive, from four inputs rather than
one. The design choice that carries the package is stated in its own purpose:
**small decision tables rather than a combinatorial cross-product**.

That is a real engineering decision with a named failure on the other side of it.
`PR-02` — policy becomes combinatorial — is the register's second entry and is
rated critical, because a policy nobody can explain is a policy that gets
overridden. Four dimensions at four levels is 256 cells; four tables with
precedence rules is four things a human can hold in mind.

### Why max/precedence rather than a score

A weighted score lets a high materiality be cancelled by a low exposure. That is
arithmetically reasonable and epistemically wrong: a claim that could change a
clinical decision does not become safe because it is cheap to run. Sub-task T02's
max/precedence rule encodes the asymmetry — the highest dimension wins, and
**hard-promotion** rules exist for cases where a single dimension alone forces R3
regardless of the others.

### `UNKNOWN` is the load-bearing value

T03 makes an unknown dimension fail closed. This is the difference between a
classifier and a control. Most real work arrives partially classified, and a
system that treats missing as low will classify most of its work as low — not
because the work is low risk, but because classification is effort. Fail-closed
inverts that incentive: the cheapest path becomes classifying honestly.

### Where this package's output is consumed

R1/R2/R3 is not an annotation. ADR-001 binds it directly to what is legal for a
solo operator: R1 solo, R2 solo under a declared partial-independence profile,
**R3 `BLOCKED`**. So this package decides, in practice, which work the laboratory
may do at all in its current configuration. A rubric that classifies too much as
R3 stops the lab; one that classifies too little makes ADR-001's protection
vacuous. That trade-off is the thing to get right, and it cannot be gotten right
without measuring — which is why WP-007 and the metascience gap sit beside it.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/WP-001_commissioning_charter.md) | `CommissioningCharter` · `Program authority matrix` · `Initial budget envelope` · `Executive DecisionRecord` |
| [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md) | `Requirement Registry` · `NFR scorecard` · `Traceability matrix seed` · `Scope boundary record` |

### Full prerequisite closure

**2 of 141 packages (1%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |

### What acceptance of this package releases

- **Directly unblocked:** 12 — `WP-007` · `WP-008` · `WP-009` · `WP-010` · `WP-013` · `WP-034` · `WP-042` · `WP-045` · `WP-056` · `WP-077` · `WP-079` · `WP-085`
- **Transitively reachable:** **134 of 141 packages (95%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **3** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **M** |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Research Director / Assurance Lead |
| Gates touched | `G0` · `G1` |
| Controls | `CTL-GOV-03` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-001 — Commissioning Charter and Programme Authority](../01_GOVERNANCE/WP-001_commissioning_charter.md), [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md)
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
- **Safety & Governance Owner** carries the acceptance decision; **Research Director / Assurance Lead** must verify independently of whoever implements.
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
| WP-005-T01 | Define the M/U/X/S dimensions with a 0–3 rubric | Implementation owner | Commit / configuration / record reference |
| WP-005-T02 | Write the max/precedence rules and the hard-promotion rules | Implementation owner | Commit / configuration / record reference |
| WP-005-T03 | Define the fail-closed effect of an `UNKNOWN` value | Implementation owner | Commit / configuration / record reference |
| WP-005-T04 | Map R1/R2/R3 onto review, literature and reproduction depth | Implementation owner | Commit / configuration / record reference |
| WP-005-T05 | Assign the decision rights for raising and lowering a risk class | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `RiskProfile schema semantics`
- `AssuranceClass decision tables`
- `Promotion rules`
- `Worked examples`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-005_risk_assurance_profile.tests.md`](WP-005_risk_assurance_profile.tests.md).

- Boundary-value policy tests
- A consistency and calibration test applying the same case twice
- Negative tests for `UNKNOWN` handling and for class downgrade
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-005_risk_assurance_profile.acceptance.md`](WP-005_risk_assurance_profile.acceptance.md), together with what this package still cannot establish.

- [ ] The decision tables require no cross-product enumeration.
- [ ] Identical inputs produce a deterministic class.
- [ ] R3 and hard promotion cannot be compensated by any low score on another dimension.
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

A new table is evaluated in shadow mode before promotion; on failure the previous signed policy version is restored.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
