---
title: "WP-123 — Control Effectiveness and Policy Regression Rhythm"
aliases:
  - "WP-123"
  - "WP-123 — Control Effectiveness and Policy Regression Rhythm"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Policies and controls are measured for effectiveness — through scheduled negative tests, attacks, exception audits, coverage and false-positive review — not merely for existence."
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-123_control_effectiveness.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/day-2
  - aethrion/state/not-started
---

# WP-123 — Control Effectiveness and Policy Regression Rhythm

## Package card

| Field | Value |
|---|---|
| Work package | `WP-123` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Internal Audit / Red Team |
| Hard dependencies | WP-009, WP-056, WP-060, WP-112, WP-121 |
| Related gates | Day-2 |
| Related controls | All controls |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_123_control_effectiveness.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_123_control_effectiveness.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Policies and controls are measured for **effectiveness** — through scheduled negative tests, attacks, exception audits, coverage and false-positive review — not merely for existence.


## Analysis
### What this package actually decides

That a control is measured for **effectiveness**, not existence. The purpose
sentence draws the distinction, and `00_PROGRAM/07` makes it a closure rule: *a risk
does not close on "mitigation applied" — closure requires a control effectiveness
test, an evidence reference, a residual-risk owner and a re-evaluation date.*

### Negative regressions are the mechanism (T02)

A control is effective if it still refuses. Running the refusal cases on a schedule
— OPA denials, identity rejections, data-class blocks, tool scope refusals, supply
chain rejections — is what detects a control that silently stopped working after a
configuration change.

This repository already applies the rule to its own checkers: `monitor_sources.py`
fails if its positive control stays silent.

### Exception audit is where control regimes actually decay (T03)

WP-009 gives exceptions an expiry and a removal criterion. This is where the
register is audited: which exceptions were used, which expired unnoticed, which were
renewed without restating their criterion, and what residual risk has accumulated.

An exception register full of quiet renewals is a second, undocumented policy.

### False-positive review is what keeps controls trusted (T04)

A control with a high false-positive rate gets routed around. Measuring it — and
tuning the control rather than the people — is what stops that.

### Two material failures reopen a decision (T05)

The trigger is unusual and worth keeping: two material failures of the same control
means the design is wrong, not the operation. That reopens an ADR or a policy rather
than producing a third remediation.

### Baseline v1.3.0 — Day-2 measures what this baseline added

The recurring rhythms gain six subjects, each of which is a number that only
means something when tracked over time:

- **Multi-agent efficiency** — coordination overhead against the naive
  fully-connected baseline, and whether the optimisation still holds.
- **Verifier calibration** — precision, recall, **abstention rate** and error
  correlation between verifier families, requalified on a schedule.
- **Source and upstream drift** — pinned mechanisms whose upstream moved, and
  sources whose status changed.
- **Supply-chain posture** — OSV and Scorecard findings, and residual risks that
  reached their expiry.
- **Failure taxonomy distribution** — including how often attribution returned
  `UNKNOWN`, which is a system-health signal rather than a defect count.
- **The Pareto frontier** — quality against cost, so an optimisation that stopped
  paying is visible.

Incident learning consumes the typed `FailureAssessment` and retains negative
results. A failed approach that is deleted is a lesson the next campaign pays for
again.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md) | `Control Catalog` · `ExceptionPolicy` · `NonWaivableBlocker registry` · `Control-test mapping` |
| [WP-056 — Policy Decision Point and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md) | `Policy decision point` · `PolicyDecision interface conformance suite` · `Policy bundle v1` · `Policy test suite` |
| [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md) | `Agentic attack suite` · `Malicious fixture corpus` · `Red-team report template` · `Security regression schedule` |
| [WP-112 — Security and Privacy Acceptance Package](../10_INTEGRATION_CUTOVER/wp_112_security_privacy_acceptance.md) | `Security scenario results` · `Red-team report` · `Forensic evidence` · `Security acceptance statement` |
| [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md) | `Hypercare log` · `Incident/finding summary` · `Production KPI baseline` · `Day-2 handoff` |

### Full prerequisite closure

**122 of 160 packages (76%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-037` · `WP-039` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-036` · `WP-048` · `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-040` · `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` · `WP-092` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-060` · `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` · `WP-154` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |
| 47 | `WP-110` · `WP-111` · `WP-112` · `WP-113` · `WP-114` |
| 48 | `WP-115` |
| 49 | `WP-116` · `WP-117` |
| 50 | `WP-118` |
| 51 | `WP-119` |
| 52 | `WP-120` |
| 53 | `WP-121` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-130`
- **Transitively reachable:** **1 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W9 — Day-2 |
| Dependency depth | level **54** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Internal Audit / Red Team |
| Gates touched | `Day-2` |
| Controls | `All controls` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-112 — Security and Privacy Acceptance Package](../10_INTEGRATION_CUTOVER/wp_112_security_privacy_acceptance.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
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
| `Control Catalog` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `ExceptionPolicy` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `NonWaivableBlocker registry` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Control-test mapping` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Non-waivable additions for the epistemic layer` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Non-waivable additions for the reliability layer` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Policy decision point` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `PolicyDecision interface conformance suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Agentic attack suite` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Malicious fixture corpus` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Red-team report template` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Security regression schedule` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `ASB and WASP external regression` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Memory poisoning and evaluator exfiltration fixtures` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Security scenario results` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Red-team report` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Forensic evidence` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Security acceptance statement` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Hypercare log` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Incident/finding summary` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Production KPI baseline` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Day-2 handoff` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Program closure report` | `WP-121` | `python3 scripts/progress.py show WP-121` |

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
- **Safety & Governance Owner** carries the acceptance decision; **Internal Audit / Red Team** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-123`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-123-T01 | Apply the control test calendar and its sampling rates | Implementation owner | Commit / configuration / record reference |
| WP-123-T02 | Run the OPA, identity, data, tool and supply-chain negative regressions | Implementation owner | Commit / configuration / record reference |
| WP-123-T03 | Audit exception expiry, usage and residual risk | Implementation owner | Commit / configuration / record reference |
| WP-123-T04 | Review control coverage, gaps and false positives | Implementation owner | Commit / configuration / record reference |
| WP-123-T05 | Trigger an ADR or policy reopen after two material failures | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Control effectiveness reports`
- `Policy regression results`
- `Exception audit`
- `Control improvement backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-123_control_effectiveness.tests.md`](wp_123_control_effectiveness.tests.md).

- Non-waivable denial tests
- An expired exception scan
- An attack regression sample
- Decision log coverage
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-123_control_effectiveness.acceptance.md`](wp_123_control_effectiveness.acceptance.md), together with what this package still cannot establish.

- [ ] A critical control-effectiveness failure produces a same-day incident and containment.
- [ ] Exceptions never extend automatically.
- [ ] Control success is not measured by denial count alone.
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

- Day-2 controls decay fastest because nothing fails when they stop running.
- Periodic work that stops silently is indistinguishable from periodic work with nothing to do.
- Operational evidence must keep being produced after go-live, or the assurance argument expires.

## Rollback / compensation

A faulty policy bundle is rolled back; the affected decisions and tasks receive an impact scan.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
