---
title: "WP-006 — ExecutionProfile and Route Policy"
aliases:
  - "WP-006"
  - "WP-006 — ExecutionProfile and Route Policy"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "DataClass, CodeTrust, ToolEffect and network/credential scope act as separate axes that jointly produce the sandbox, route, approval and isolation controls."
source: "planning/commissioning/01_GOVERNANCE/WP-006_execution_profile.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/m
  - aethrion/gate/g1
  - aethrion/gate/g5
  - aethrion/state/not-started
---

# WP-006 — ExecutionProfile and Route Policy

## Package card

| Field | Value |
|---|---|
| Work package | `WP-006` |
| Workstream | `01_GOVERNANCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Security Lead |
| Independent verifier | Safety Owner / SRE |
| Hard dependencies | WP-002 |
| Related gates | G1,G5 |
| Related controls | CTL-DAT-02, CTL-SEC-04 |
| Related acceptance scenarios | ACC-15, ACC-18 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_006_execution_profile.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_006_execution_profile.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

`DataClass`, `CodeTrust`, `ToolEffect` and network/credential scope act as **separate axes** that jointly produce the sandbox, route, approval and isolation controls. Collapsing them into one score is the failure this package exists to prevent.


## Analysis

### What this package actually decides

Which sandbox a piece of work runs in — and it decides it from **four independent
axes**, not from data sensitivity alone. The purpose statement names the failure
it prevents: *collapsing them into one score is the failure this package exists
to prevent.*

The reason is concrete. Public data (`D0`) processed by untrusted code (`C3`) with
a tool that writes externally (`T5`) over unrestricted egress is a maximum-risk
execution and a data-class-only policy would place it at minimum. The axes are
independent because the threats are independent.

### The dominance rule is the whole enforcement model

T04's dominance rule says the strictest requirement across the four axes wins,
and the minimum execution tier is derived from that maximum. This is the same
asymmetry as WP-005's max/precedence, applied to execution rather than assurance,
and it is what makes the profile safe to compute automatically.

### Why enforcement points are a deliverable, not an implementation detail

T05 maps enforcement across the model router, the broker, Kueue and the sandbox.
A profile computed and then enforced nowhere is a label. Worse, it is a label that
makes the system *look* controlled — which is why the enforcement-point map is
mandatory output of this package and not of the packages that build those four
components. Those packages consume the map; they do not define it.

### Relationship to ADR-003

ADR-003 draws the trust boundary: content crosses, authority does not. `CodeTrust`
and `ToolEffect` are how that boundary becomes computable. Untrusted content
arriving with an instruction cannot raise its own `ToolEffect`, because the
profile is computed from the declared task, not from the content. This package
must state that explicitly — the profile is an input to execution, never an output
of it.

### The failure mode

Profile inflation. Every task eventually requests the most permissive profile that
works, because the permissive one always works. The counter-control is that
lowering restriction requires an approval that is recorded and expires, while
raising it requires none — and that the default for an unclassified task is the
**most** restrictive tier, not the most convenient.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

1, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md) | `Requirement Registry` · `NFR scorecard` · `Traceability matrix seed` · `Scope boundary record` |

### Full prerequisite closure

**2 of 141 packages (1%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |

### What acceptance of this package releases

- **Directly unblocked:** 17 — `WP-009` · `WP-010` · `WP-013` · `WP-016` · `WP-021` · `WP-034` · `WP-041` · `WP-042` · `WP-045` · `WP-049` · `WP-051` · `WP-053` · `WP-054` · `WP-056` · `WP-057` · `WP-097` · `WP-132`
- **Transitively reachable:** **132 of 141 packages (94%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W0 — Programme lock |
| Dependency depth | level **3** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **M** |
| Accountable owner | Platform Security Lead |
| Independent verifier | Safety Owner / SRE |
| Gates touched | `G1` · `G5` |
| Controls | `CTL-DAT-02` · `CTL-SEC-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-15 — Sandbox Escape Attempt](../12_ACCEPTANCE_SCENARIOS/acc_15_sandbox_escape.md) | Critical | Every escape path is denied or contained; no credential or host data leaks, the cell is stopped and a forensic `SecurityEvent` is produced. |
| [ACC-18 — D3 Data to a Public Provider](../12_ACCEPTANCE_SCENARIOS/acc_18_d3_public_route.md) | Critical | No public provider call is made; a secure or local eligible route is chosen if one exists, otherwise the task is `BLOCKED`, and an audit record is written. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md)
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
- **Platform Security Lead** carries the acceptance decision; **Safety Owner / SRE** must verify independently of whoever implements.
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
| WP-006-T01 | Define the D0–D4 `DataClass` rubric | Implementation owner | Commit / configuration / record reference |
| WP-006-T02 | Write the C0–C3 `CodeTrust` and T0–T5 `ToolEffect` rubrics | Implementation owner | Commit / configuration / record reference |
| WP-006-T03 | Define the network and credential scope levels | Implementation owner | Commit / configuration / record reference |
| WP-006-T04 | Write the dominance rule and the minimum execution tier rule | Implementation owner | Commit / configuration / record reference |
| WP-006-T05 | Map the enforcement points across the model router, the broker, Kueue and the sandbox | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ExecutionProfile semantics`
- `Route/control decision tables`
- `Enforcement map`
- `Negative examples`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-006_execution_profile.tests.md`](wp_006_execution_profile.tests.md).

- A D0 + untrusted-code hardened-sandbox test
- A D4 + signed-code isolated-route test
- A negative test proving T4/T5 remain human-only
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks



## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-006_execution_profile.acceptance.md`](wp_006_execution_profile.acceptance.md), together with what this package still cannot establish.

- [ ] Data class is never equated with sandbox tier.
- [ ] The highest required control cannot be lowered by a permissive value on another axis.
- [ ] Every routing decision carries an explainable policy rule ID.
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

Policy changes are validated in shadow mode; on a wrong route, profiles are revoked and affected workloads are paused rather than allowed to continue.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
