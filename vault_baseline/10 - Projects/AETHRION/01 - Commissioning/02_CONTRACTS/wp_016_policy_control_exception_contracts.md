---
title: "WP-016 — PolicyDecision, Control and Exception Schemas"
aliases:
  - "WP-016"
  - "WP-016 — PolicyDecision, Control and Exception Schemas"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Every authorisation, routing and gate decision becomes an auditable record carrying its inputs, bundle version, rule ID, explanation and any linked exception."
source: "planning/commissioning/02_CONTRACTS/WP-016_policy_control_exception_contracts.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/s
  - aethrion/gate/g0-g10
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-016 — PolicyDecision, Control and Exception Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-016` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **S** — small — one owner, one review cycle; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Policy Platform Lead |
| Independent verifier | Internal Audit |
| Hard dependencies | WP-006, WP-009, WP-011 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-GOV-03 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_016_policy_control_exception_contracts.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_016_policy_control_exception_contracts.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every authorisation, routing and gate decision becomes an auditable record carrying its inputs, bundle version, rule ID, explanation and any linked exception.


## Analysis
### What this package actually decides

That a denial is explainable. Every authorisation, routing and gate decision
becomes a record carrying its **inputs, bundle version, rule ID and
explanation** — and the explanation is the field that makes the rest usable.

`PR-02` is why: *policy becomes combinatorial*, early signal *unexplainable
decisions*, rated critical. The failure is not that the policy is wrong. It is
that nobody can tell whether it is wrong, so it gets overridden — and an
overridden policy is worse than no policy, because the override is now the real
rule and it is undocumented.

### The input hash is the part that makes a decision reproducible (T04)

A `PolicyDecision` that records only its output is an assertion. One that records
the **hash of its inputs** plus the bundle version can be replayed: feed the same
inputs to the same bundle and the same decision must come out. That turns policy
from a service into a function, and it is what allows a decision taken six months
ago to be audited without reconstructing the world it was taken in.

### Default deny, and an anomaly is a denial

ADR-003 sets both. The second is the one that gets softened in implementation:
when the policy engine cannot evaluate — a missing input, a timeout, an
unparseable bundle — the tempting behaviour is to warn and continue, because
failing closed on an infrastructure fault is disruptive.

That is precisely the case an attacker creates. **An anomaly is a denial, not a
warning**, and this package has to encode it in the contract so that a downstream
implementation cannot quietly choose otherwise.

### Exceptions are where policy regimes decay (T03)

`ExceptionRecord` needs scope, approver and expiry — and, from WP-009, a **removal
criterion**, or renewal becomes a formality. The contract-level requirement is
that an expired exception is refused **at the point of use**, not merely displayed
as expired. An exception that has expired in a dashboard and still works in the
engine is the worst of both: it looks controlled and is not.

### Re-evaluation triggers (T05) are what keep a decision from going stale

A decision is taken against a state of the world. When that state changes — the
bundle is updated, the risk class is raised, the model snapshot moves, the
reviewer's independence profile changes — the decision must be re-evaluated rather
than inherited. Without triggers, an approval granted under one condition silently
authorises a different one, which is the same defect WP-004 fixes for human
decisions.

### The adoption boundary

`AETHRION_COMPONENT_REUSE.md` adopts **Cedar** as the policy decision point.
Adopted, not invented — this package defines the *record*, not the language. The
`authority_boundary` on that adoption is what stops Cedar's semantics from
becoming the canonical semantics.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md) | `Control Catalog` · `ExceptionPolicy` · `NonWaivableBlocker registry` · `Control-test mapping` |
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

- **Directly unblocked:** 13 — `WP-018` · `WP-020` · `WP-033` · `WP-038` · `WP-041` · `WP-042` · `WP-045` · `WP-049` · `WP-055` · `WP-056` · `WP-099` · `WP-100` · `WP-131`
- **Transitively reachable:** **123 of 141 packages (87%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **9** of 55 |
| On the documented critical path | no |
| Effort class | **S** |
| Accountable owner | Policy Platform Lead |
| Independent verifier | Internal Audit |
| Gates touched | `G0–G10` · `Platform` |
| Controls | `CTL-GOV-03` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
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
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Control Catalog` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `ExceptionPolicy` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `NonWaivableBlocker registry` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Control-test mapping` | `WP-009` | `python3 scripts/progress.py show WP-009` |
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

- **Effort class `S`** — small — one owner, one review cycle.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Policy Platform Lead** carries the acceptance decision; **Internal Audit** must verify independently of whoever implements.
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
| WP-016-T01 | Write the `PolicyDecision` allow/deny/obligations fields | Implementation owner | Commit / configuration / record reference |
| WP-016-T02 | Add the `ControlRecord` owner, evidence and frequency fields | Implementation owner | Commit / configuration / record reference |
| WP-016-T03 | Define the `ExceptionRecord` scope, approver and expiry schema | Implementation owner | Commit / configuration / record reference |
| WP-016-T04 | Fix the format of the policy explanation and the input hash | Implementation owner | Commit / configuration / record reference |
| WP-016-T05 | Define the re-evaluation triggers | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `PolicyDecision schema`
- `ControlRecord schema`
- `ExceptionRecord schema`
- `Example decision fixtures`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-016_policy_control_exception_contracts.tests.md`](wp_016_policy_control_exception_contracts.tests.md).

- A negative test for a missing bundle digest or rule ID
- Validation of expired exceptions
- An input-hash determinism test
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-016_policy_control_exception_contracts.acceptance.md`](wp_016_policy_control_exception_contracts.acceptance.md), together with what this package still cannot establish.

- [ ] Every decision carries an explainable rule ID and a bundle digest.
- [ ] An exception cannot be used outside its declared scope.
- [ ] An `UNKNOWN` policy result never resolves to allow.
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

A policy record is never edited; a superseding decision is written and the affected tasks are re-evaluated.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
