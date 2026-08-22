---
title: "WP-102 — Vertical Slice 1 — Intake through Protocol Freeze"
aliases:
  - "WP-102"
  - "WP-102 — Vertical Slice 1 — Intake through Protocol Freeze"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A realistic R1 project and a realistic R3 project travel from G0 to G2 with a complete risk/control plan, charter, protocol, human decision and audit chain."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-102_vertical_slice_intake_protocol.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g1
  - aethrion/gate/g2
  - aethrion/state/not-started
---

# WP-102 — Vertical Slice 1 — Intake through Protocol Freeze

## Package card

| Field | Value |
|---|---|
| Work package | `WP-102` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Research Workflow Lead |
| Independent verifier | Assurance / Project Decision Owner |
| Hard dependencies | WP-034, WP-035, WP-056, WP-091, WP-092, WP-093, WP-100, WP-101 |
| Related gates | G0,G1,G2 |
| Related controls | CTL-GOV-01, CTL-GOV-03 |
| Related acceptance scenarios | ACC-06, ACC-25, ACC-26 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_102_vertical_slice_intake_protocol.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_102_vertical_slice_intake_protocol.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A realistic R1 project and a realistic R3 project travel from G0 to G2 with a complete risk/control plan, charter, protocol, human decision and audit chain. This is the first slice where the design meets reality.


## Analysis
### What this package actually decides

Whether any of it works. The purpose sentence says it without decoration: *this is
the first slice where the design meets reality.*

Everything before this package is a contract, a service or a policy verified
against its own specification. This is the first time a project travels through
several of them in sequence, and it is where the seams get tested — the places
where two packages each satisfied their own criteria and disagree about the
boundary between them.

### Two projects, because R1 and R3 fail differently (T01)

An R1 project should complete. An R3 project should reach `BLOCKED` under ADR-001,
with a declaration naming the missing external verifier — and the *correct* outcome
for R3 in a solo laboratory is that it does not proceed.

A slice that only runs R1 has tested the path that works.

### The seams this slice will actually find

Three specific ones, worth naming in advance because they are where the design has
most surface:

1. **Profile binding at G1** — WP-005, WP-006 and WP-007 each produce a profile.
   Whether they compose, and what happens when they disagree, has never been run.
2. **Budget reservation before compute opens** — WP-053 reserves, WP-100 accounts,
   WP-032 pauses. Three packages, one invariant (`00_PROGRAM/01` #9).
3. **Gate record emission across a same-session close** — WP-008 requires separate
   records, WP-033 writes them, WP-032 drives them.

### Expect this package to produce findings against upstream packages

That is its function. A vertical slice whose only output is *it worked* has
probably not been run against a realistic fixture. `00_PROGRAM/06`'s finding
lifecycle applies, and the findings belong to the packages they are against — not
to this one.

### The revise, block and reopen paths are the half that gets skipped (T06)

Running a project forward through G0→G2 is the demonstration. Running it backwards
— a `REVISE` at G1, a `BLOCKED` at G2, a reopen after a protocol change — is the
test.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md) | `G0/G1 workflows` · `Intake/Charter UI API contract` · `ControlPlan generation` · `Gate fixtures` |
| [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md) | `G2–G4 workflows` · `Protocol amendment flow` · `Literature freeze integration` · `Compute-open decision` |
| [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md) | `OPA platform` · `Policy bundle v1` · `Policy test suite` · `Bundle promotion pipeline` |
| [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md) | `Cockpit application shell` · `Navigation/IA` · `BFF/read APIs` · `RBAC matrix` |
| [WP-092 — Project Workspace and G0–G10 Gate Timeline](../09_EXPERIENCE_OBSERVABILITY/wp_092_project_gate_timeline.md) | `Project Workspace` · `Gate Timeline` · `Artifact/evidence panels` · `Command/update forms` |
| [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md) | `Decision Queue UI` · `Evidence-delta component` · `Rationale forms` · `Delegation/escalation views` |
| [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md) | `Cost Ledger` · `Budget service` · `Cost adapters` · `Invoice reconciliation` |
| [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md) | `Service Catalog` · `SLO catalog` · `Error-budget policy` · `Alert-runbook link checker` |

### Full prerequisite closure

**89 of 141 packages (63%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-077` · `WP-078` · `WP-101` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-093` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-109`
- **Transitively reachable:** **22 of 141 packages (16%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **41** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Research Workflow Lead |
| Independent verifier | Assurance / Project Decision Owner |
| Gates touched | `G0` · `G1` · `G2` |
| Controls | `CTL-GOV-01` · `CTL-GOV-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-06 — Planner Self-Approval Attempt](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) | Critical | The assignment is rejected by policy; the gate becomes `BLOCKED` or waits for a suitable independent reviewer, and the violation attempt is audited. |
| [ACC-25 — Human Approval Forgery](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) | Critical | The decision is rejected; gate state does not change and a security event and audit record are produced. A valid owner with MFA and an idempotent request passes as the counter-example. |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/acc_26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-034 — G0 Intake and G1 Charter Workflows](../04_CONTROL_EVENT/wp_034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature and G4 Baseline Workflows](../04_CONTROL_EVENT/wp_035_g2_g4_workflows.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md), [WP-092 — Project Workspace and G0–G10 Gate Timeline](../09_EXPERIENCE_OBSERVABILITY/wp_092_project_gate_timeline.md), [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md), [WP-100 — Cost Ledger, Budget Envelopes and FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md)
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
| `G0/G1 workflows` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Intake/Charter UI API contract` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `ControlPlan generation` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `Gate fixtures` | `WP-034` | `python3 scripts/progress.py show WP-034` |
| `G2–G4 workflows` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Protocol amendment flow` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Literature freeze integration` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `Compute-open decision` | `WP-035` | `python3 scripts/progress.py show WP-035` |
| `OPA platform` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Cockpit application shell` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Navigation/IA` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `BFF/read APIs` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `RBAC matrix` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Accessibility baseline` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Project Workspace` | `WP-092` | `python3 scripts/progress.py show WP-092` |
| `Gate Timeline` | `WP-092` | `python3 scripts/progress.py show WP-092` |
| `Artifact/evidence panels` | `WP-092` | `python3 scripts/progress.py show WP-092` |
| `Command/update forms` | `WP-092` | `python3 scripts/progress.py show WP-092` |
| `Decision Queue UI` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence-delta component` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Rationale forms` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Delegation/escalation views` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Decision audit export` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Cost Ledger` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Budget service` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Cost adapters` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Invoice reconciliation` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `FinOps dashboard/runbook` | `WP-100` | `python3 scripts/progress.py show WP-100` |
| `Service Catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `SLO catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Error-budget policy` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Alert-runbook link checker` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Ownership dashboard` | `WP-101` | `python3 scripts/progress.py show WP-101` |

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
- **Research Workflow Lead** carries the acceptance decision; **Assurance / Project Decision Owner** must verify independently of whoever implements.
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
| WP-102-T01 | Prepare the R1 and R3 synthetic project fixtures | Implementation owner | Commit / configuration / record reference |
| WP-102-T02 | Start the intake from the cockpit | Implementation owner | Commit / configuration / record reference |
| WP-102-T03 | Verify the risk, execution and independence policy decisions | Implementation owner | Commit / configuration / record reference |
| WP-102-T04 | Run the charter, SLA, delegation and protocol freeze | Implementation owner | Commit / configuration / record reference |
| WP-102-T05 | Check the budget reservation, audit and telemetry chain | Implementation owner | Commit / configuration / record reference |
| WP-102-T06 | Test the revise, block and reopen paths | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Vertical slice dossier`
- `R1/R3 project histories`
- `Trace/audit/decision evidence`
- `Integration findings`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-102_vertical_slice_intake_protocol.tests.md`](wp_102_vertical_slice_intake_protocol.tests.md).

- Happy path for both R1 and R3
- `BLOCKED` on an unknown risk value
- An expired delegation
- A material protocol amendment
- Budget unavailable
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-102_vertical_slice_intake_protocol.acceptance.md`](wp_102_vertical_slice_intake_protocol.acceptance.md), together with what this package still cannot establish.

- [ ] Every canonical record from G0 to G2 is linked.
- [ ] R3 receives deeper assurance but uses the same gates.
- [ ] No open critical integration finding remains.
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

- Vertical slices fail at the seams; per-package green says little about the seam.
- A cutover rehearsal that differs from the real procedure has rehearsed the wrong thing.
- The rollback point must be verified by a query, not by an assertion.

## Rollback / compensation

If the slice fails, the production-like project is closed; synthetic artifacts are retained and a correction package is opened.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
