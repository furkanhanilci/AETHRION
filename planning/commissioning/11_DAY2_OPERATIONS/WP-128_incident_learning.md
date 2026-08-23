# WP-128 — Incident, Postmortem and Learning Closure

## Package card

| Field | Value |
|---|---|
| Work package | `WP-128` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Incident Commander / SRE Lead |
| Independent verifier | Safety / Assurance / Service Owner |
| Hard dependencies | WP-037, WP-060, WP-099, WP-101, WP-116, WP-118, WP-121 |
| Related gates | G10,Day-2 |
| Related controls | CTL-OPS-03, CTL-MOD-02, CTL-LIT-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-128_incident_learning.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-128_incident_learning.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Security, data, reliability, cost and epistemic incidents are run through a contain → recover → learn → close lifecycle that ends in a control, evaluation or runbook change.


## Analysis
### What this package actually decides

That an incident ends in a **change**. Contain → recover → learn → close, and the
close is conditional: `00_PROGRAM/06`'s finding lifecycle requires every finding to
reach a terminal state, and T05 requires every action to bind to a work package,
control, evaluation, runbook or `ImpactCase`.

An incident that closes with a postmortem and no bound action has produced a
document.

### Epistemic incidents are in scope and that is unusual (purpose sentence)

Security, data, reliability, cost — and **epistemic**. A published claim that turns
out to be wrong, a fabricated citation, a review that missed something material.
Most incident processes have no category for these, and this system's central risk
is exactly that class.

`investigating-integrity-concerns` is the skill; this is the process.

### Containment before analysis, always (T02)

Credential revocation, pausing workflows, stopping publication. The instinct to
understand first is what turns a contained incident into an ongoing one.

### Canonical integrity analysis is specific to this system (T03)

After any incident, the question *is the canonical record still correct* has to be
answered by the integrity queries rather than assumed. An incident that corrupted a
projection is recoverable; one that corrupted the ledger is not, and the two look
similar at first.

### Blameless, and the timeline is the artifact (T04)

The decision timeline — what was known when, who decided what — is what makes a
postmortem useful and is the first thing lost to memory.

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

8, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md) | `ImpactScan workflow` · `Schedule registry` · `ImpactCase service contract` · `Supersession trigger` |
| [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md) | `Agentic attack suite` · `Malicious fixture corpus` · `Red-team report template` · `Security regression schedule` |
| [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md) | `Audit Ledger` · `Hash-chain service` · `Audit export/verify tooling` · `Retention/access policy` |
| [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md) | `Service Catalog` · `SLO catalog` · `Error-budget policy` · `Alert-runbook link checker` |
| [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md) | `Chaos test suite/results` · `Steady-state hypotheses` · `Recovery/integrity report` · `Resilience sign-off` |
| [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operational_readiness.md) | `Operational Readiness Review` · `Runbook execution records` · `On-call simulation` · `Training/ownership sign-offs` |
| [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md) | `Hypercare log` · `Incident/finding summary` · `Production KPI baseline` · `Day-2 handoff` |
| [WP-152 — Failure Taxonomy, Attribution and Resilience Controls](../15_RELIABILITY_EFFICIENCY/WP-152_failure_taxonomy_and_resilience.md) | `Extended FailureAssessment taxonomy` · `Attribution pipeline` · `Challenger and Inspector functions` · `Faulty-agent fixture suite` |

### Full prerequisite closure

**127 of 160 packages (79%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 27 | `WP-058` · `WP-064` · `WP-075` · `WP-141` |
| 28 | `WP-060` · `WP-062` · `WP-081` · `WP-142` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` · `WP-154` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` · `WP-147` |
| 38 | `WP-088` · `WP-148` |
| 39 | `WP-089` · `WP-152` |
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
| Accountable owner | Incident Commander / SRE Lead |
| Independent verifier | Safety / Assurance / Service Owner |
| Gates touched | `G10` · `Day-2` |
| Controls | `CTL-OPS-03` · `CTL-MOD-02` · `CTL-LIT-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md), [WP-118 — Operational Readiness, On-Call and Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operational_readiness.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md)
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
| `ImpactScan workflow` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Schedule registry` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `ImpactCase service contract` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Supersession trigger` | `WP-037` | `python3 scripts/progress.py show WP-037` |
| `Agentic attack suite` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Malicious fixture corpus` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Red-team report template` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Security regression schedule` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `ASB and WASP external regression` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Memory poisoning and evaluator exfiltration fixtures` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Audit Ledger` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Hash-chain service` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Audit export/verify tooling` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Retention/access policy` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Integrity dashboard` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Service Catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `SLO catalog` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Error-budget policy` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Alert-runbook link checker` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Ownership dashboard` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Coordination overhead and Pareto SLOs` | `WP-101` | `python3 scripts/progress.py show WP-101` |
| `Chaos test suite/results` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Steady-state hypotheses` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Recovery/integrity report` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Resilience sign-off` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Operational Readiness Review` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Runbook execution records` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `On-call simulation` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Training/ownership sign-offs` | `WP-118` | `python3 scripts/progress.py show WP-118` |
| `Hypercare log` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Incident/finding summary` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Production KPI baseline` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Day-2 handoff` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Program closure report` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Extended FailureAssessment taxonomy` | `WP-152` | `python3 scripts/progress.py show WP-152` |
| `Attribution pipeline` | `WP-152` | `python3 scripts/progress.py show WP-152` |
| `Challenger and Inspector functions` | `WP-152` | `python3 scripts/progress.py show WP-152` |
| `Faulty-agent fixture suite` | `WP-152` | `python3 scripts/progress.py show WP-152` |

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
- **Incident Commander / SRE Lead** carries the acceptance decision; **Safety / Assurance / Service Owner** must verify independently of whoever implements.
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
| WP-128-T01 | Operate severity classification and the `IncidentWorkflow` | Implementation owner | Commit / configuration / record reference |
| WP-128-T02 | Perform containment, credential revocation, pausing and communication | Implementation owner | Commit / configuration / record reference |
| WP-128-T03 | Run forensic, audit and canonical integrity analysis and root-cause analysis | Implementation owner | Commit / configuration / record reference |
| WP-128-T04 | Write the blameless postmortem and the decision timeline | Implementation owner | Commit / configuration / record reference |
| WP-128-T05 | Bind each action to a WP, control, evaluation, runbook or `ImpactCase` | Implementation owner | Commit / configuration / record reference |
| WP-128-T06 | Verify effectiveness and take the closure decision | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `IncidentRecords`
- `Forensic packages`
- `Postmortems`
- `Learning/action register`
- `Closure evidence`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-128_incident_learning.tests.md`](WP-128_incident_learning.tests.md).

- Security containment
- Duplicate effect and data integrity
- An escaped epistemic claim
- Re-testing action effectiveness
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-128_incident_learning.acceptance.md`](WP-128_incident_learning.acceptance.md), together with what this package still cannot establish.

- [ ] A material incident is never closed by a document alone.
- [ ] Every action carries an owner, a date and evidence.
- [ ] Affected claims, projects, models and controls receive an impact scan.
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

If the recovery proves wrong the incident is reopened; evidence and postmortems remain versioned rather than edited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
