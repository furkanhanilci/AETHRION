# WP-130 — Architecture and Platform Continuous Assurance

## Package card

| Field | Value |
|---|---|
| Work package | `WP-130` |
| Workstream | `11_DAY2_OPERATIONS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect / Platform Assurance Lead |
| Independent verifier | Architecture Board / Internal Audit |
| Hard dependencies | WP-010, WP-030, WP-040, WP-060, WP-109, WP-115, WP-121, WP-123, WP-124, WP-125, WP-126, WP-127, WP-128, WP-129 |
| Related gates | G0–G10, Platform, Day-2 |
| Related controls | All controls |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-130_architecture_continuous_assurance.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-130_architecture_continuous_assurance.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Architectural invariants, canonical ownership, contract compatibility, workflow replay, derived rebuild, the golden research path and control effectiveness are re-verified on a schedule. The platform is held to the same evidentiary standard it imposes on the research it hosts.


## Analysis
### What this package actually decides

That the platform is held to its own standard. The purpose sentence states it
plainly and it is the most self-aware line in the plan: *the platform is held to
the same evidentiary standard it imposes on the research it hosts.*

A system that demands preregistration, independent review and reproduction from
research, while accepting its own architecture on assertion, has an exemption it did
not earn.

### Architecture drift is the failure this catches (T01)

Invariants erode by accretion. A cache that quietly becomes canonical, a consumer
that starts writing gate state, a projection that stops rebuilding, a contract with
no consumer. Each is a small, locally reasonable change, and each breaks a stated
invariant.

This repository already carries an instance: `dependency-rules.txt` states the
target direction and records that it is **not yet machine-enforced**, with finding
**H4** as the known violation.

### The golden-path synthetic runs are the strongest signal here (T03)

A synthetic research project and a synthetic engineering change, run end to end on
a schedule. If either stops working, something broke that no unit test covers —
and it is the closest thing the system has to a continuous integration test of
itself.

### The derived-rebuild sample is the falsification test, repeated (T04)

`00_PROGRAM/01` invariant 6. WP-030 and `ACC-21` establish it once; running a sample
monthly is what catches the day something stopped being derivable.

### Contract compatibility across adapters (T02)

Schema, adapter and policy compatibility. A provider changes a response shape, an
adapter absorbs it, and the canonical contract silently no longer matches what is
stored.

### This package is the one that would catch what this repository has already found

Stale counts, an unenforced dependency rule, a projection that churned, a test suite
that mutated production state, a monitor covering less than half its sources. Every
one of those was found by looking rather than by a check — and this package is where
that looking becomes scheduled.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

14, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md) | `Signed ADR bundle` · `Rejected alternatives register` · `Reopen trigger register` · `Architecture baseline digest` |
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/WP-040_workflow_replay_failure_suite.md) | `Replay test suite` · `Golden histories` · `Fault-injection harness` · `Workflow compatibility report` |
| [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md) | `Agentic attack suite` · `Malicious fixture corpus` · `Red-team report template` · `Security regression schedule` |
| [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md) | `Acceptance Registry` · `Scenario runner` · `Fixture catalog` · `Evidence capture/signing` |
| [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md) | `Commissioning Dossier` · `RC evidence manifest` · `Finding/risk register snapshot` · `Readiness scorecard` |
| [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md) | `Hypercare log` · `Incident/finding summary` · `Production KPI baseline` · `Day-2 handoff` |
| [WP-123 — Control Effectiveness and Policy Regression Rhythm](../11_DAY2_OPERATIONS/WP-123_control_effectiveness.md) | `Control effectiveness reports` · `Policy regression results` · `Exception audit` · `Control improvement backlog` |
| [WP-124 — Model Requalification, Drift and Ejection Rhythm](../11_DAY2_OPERATIONS/WP-124_model_requalification_drift.md) | `Requalification reports` · `CapabilityProfile decisions` · `Drift/ejection events` · `ImpactCase results` |
| [WP-125 — Literature, Zotero and Obsidian Curation Rhythm](../11_DAY2_OPERATIONS/WP-125_literature_knowledge_curation.md) | `Curation calendar` · `Queue/SLA reports` · `Library quality scorecard` · `Knowledge integrity report` |
| [WP-126 — Reviewer, Judge and Reproducer Calibration](../11_DAY2_OPERATIONS/WP-126_assurance_calibration.md) | `Calibration reports` · `Reviewer capability decisions` · `Bias/quality dashboard` · `Improvement actions` |
| [WP-127 — FinOps, Capacity and Portfolio Review Rhythm](../11_DAY2_OPERATIONS/WP-127_finops_portfolio.md) | `Monthly FinOps report` · `Invoice cases` · `Portfolio decision records` · `Capacity forecast` |
| [WP-128 — Incident, Postmortem and Learning Closure](../11_DAY2_OPERATIONS/WP-128_incident_learning.md) | `IncidentRecords` · `Forensic packages` · `Postmortems` · `Learning/action register` |
| [WP-129 — Quarterly DR, Supply-Chain and Audit Drill](../11_DAY2_OPERATIONS/WP-129_quarterly_dr_supply_chain.md) | `Quarterly drill dossier` · `Restore/replay evidence` · `Supply-chain/audit results` · `Improvement backlog` |

### Full prerequisite closure

**128 of 141 packages (91%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
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
| 54 | `WP-123` · `WP-124` · `WP-125` · `WP-126` · `WP-127` · `WP-128` · `WP-129` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W9 — Day-2 |
| Dependency depth | level **55** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Chief Architect / Platform Assurance Lead |
| Independent verifier | Architecture Board / Internal Audit |
| Gates touched | `G0–G10` · `Platform` · `Day-2` |
| Controls | `All controls` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md), [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/WP-040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-109 — Forty Acceptance Scenario Registry and Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md), [WP-121 — Hypercare, Stabilisation and Programme Closure](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.md), [WP-123 — Control Effectiveness and Policy Regression Rhythm](../11_DAY2_OPERATIONS/WP-123_control_effectiveness.md), [WP-124 — Model Requalification, Drift and Ejection Rhythm](../11_DAY2_OPERATIONS/WP-124_model_requalification_drift.md), [WP-125 — Literature, Zotero and Obsidian Curation Rhythm](../11_DAY2_OPERATIONS/WP-125_literature_knowledge_curation.md), [WP-126 — Reviewer, Judge and Reproducer Calibration](../11_DAY2_OPERATIONS/WP-126_assurance_calibration.md), [WP-127 — FinOps, Capacity and Portfolio Review Rhythm](../11_DAY2_OPERATIONS/WP-127_finops_portfolio.md), [WP-128 — Incident, Postmortem and Learning Closure](../11_DAY2_OPERATIONS/WP-128_incident_learning.md), [WP-129 — Quarterly DR, Supply-Chain and Audit Drill](../11_DAY2_OPERATIONS/WP-129_quarterly_dr_supply_chain.md)
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
| `Signed ADR bundle` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Rejected alternatives register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Reopen trigger register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Architecture baseline digest` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Replay test suite` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Golden histories` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Fault-injection harness` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Workflow compatibility report` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Agentic attack suite` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Malicious fixture corpus` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Red-team report template` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Security regression schedule` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Acceptance Registry` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Scenario runner` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Fixture catalog` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Evidence capture/signing` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Result dashboard` | `WP-109` | `python3 scripts/progress.py show WP-109` |
| `Commissioning Dossier` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `RC evidence manifest` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Finding/risk register snapshot` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Readiness scorecard` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Board verdict` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Hypercare log` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Incident/finding summary` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Production KPI baseline` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Day-2 handoff` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Program closure report` | `WP-121` | `python3 scripts/progress.py show WP-121` |
| `Control effectiveness reports` | `WP-123` | `python3 scripts/progress.py show WP-123` |
| `Policy regression results` | `WP-123` | `python3 scripts/progress.py show WP-123` |
| `Exception audit` | `WP-123` | `python3 scripts/progress.py show WP-123` |
| `Control improvement backlog` | `WP-123` | `python3 scripts/progress.py show WP-123` |
| `Requalification reports` | `WP-124` | `python3 scripts/progress.py show WP-124` |
| `CapabilityProfile decisions` | `WP-124` | `python3 scripts/progress.py show WP-124` |
| `Drift/ejection events` | `WP-124` | `python3 scripts/progress.py show WP-124` |
| `ImpactCase results` | `WP-124` | `python3 scripts/progress.py show WP-124` |
| `Curation calendar` | `WP-125` | `python3 scripts/progress.py show WP-125` |
| `Queue/SLA reports` | `WP-125` | `python3 scripts/progress.py show WP-125` |
| `Library quality scorecard` | `WP-125` | `python3 scripts/progress.py show WP-125` |
| `Knowledge integrity report` | `WP-125` | `python3 scripts/progress.py show WP-125` |
| `Calibration reports` | `WP-126` | `python3 scripts/progress.py show WP-126` |
| `Reviewer capability decisions` | `WP-126` | `python3 scripts/progress.py show WP-126` |
| `Bias/quality dashboard` | `WP-126` | `python3 scripts/progress.py show WP-126` |
| `Improvement actions` | `WP-126` | `python3 scripts/progress.py show WP-126` |
| `Monthly FinOps report` | `WP-127` | `python3 scripts/progress.py show WP-127` |
| `Invoice cases` | `WP-127` | `python3 scripts/progress.py show WP-127` |
| `Portfolio decision records` | `WP-127` | `python3 scripts/progress.py show WP-127` |
| `Capacity forecast` | `WP-127` | `python3 scripts/progress.py show WP-127` |
| `Optimization backlog` | `WP-127` | `python3 scripts/progress.py show WP-127` |
| `IncidentRecords` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Forensic packages` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Postmortems` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Learning/action register` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Closure evidence` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Quarterly drill dossier` | `WP-129` | `python3 scripts/progress.py show WP-129` |
| `Restore/replay evidence` | `WP-129` | `python3 scripts/progress.py show WP-129` |
| `Supply-chain/audit results` | `WP-129` | `python3 scripts/progress.py show WP-129` |
| `Improvement backlog` | `WP-129` | `python3 scripts/progress.py show WP-129` |

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
- **Chief Architect / Platform Assurance Lead** carries the acceptance decision; **Architecture Board / Internal Audit** must verify independently of whoever implements.
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
| WP-130-T01 | Run the monthly architecture drift and canonical-owner scan | Implementation owner | Commit / configuration / record reference |
| WP-130-T02 | Run the schema, adapter and policy compatibility suite | Implementation owner | Commit / configuration / record reference |
| WP-130-T03 | Execute the golden-path synthetic research and engineering runs | Implementation owner | Commit / configuration / record reference |
| WP-130-T04 | Run a derived graph, index and Obsidian rebuild sample | Implementation owner | Commit / configuration / record reference |
| WP-130-T05 | Review the platform chaos, replay and backup evidence | Implementation owner | Commit / configuration / record reference |
| WP-130-T06 | Produce the ADR reopen triggers, service retirement and technical-debt decisions | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Continuous Assurance report`
- `Architecture drift findings`
- `Golden-path results`
- `ADR/retirement decisions`
- `Assurance backlog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-130_architecture_continuous_assurance.tests.md`](WP-130_architecture_continuous_assurance.tests.md).

- Canonical dual-write drift detection
- Workflow replay regression
- Graph rebuild
- A golden G0–G10 run
- The two-failure policy/control reopen trigger
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-130_architecture_continuous_assurance.acceptance.md`](WP-130_architecture_continuous_assurance.acceptance.md), together with what this package still cannot establish.

- [ ] The platform is verified by its own research assurance system.
- [ ] A material control failure occurring twice reopens the corresponding ADR.
- [ ] The target architecture does not drift silently into a product dependency.
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

If the drift is critical the affected release, route or control is paused; the last validated baseline is restored and an impact scan is performed.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
