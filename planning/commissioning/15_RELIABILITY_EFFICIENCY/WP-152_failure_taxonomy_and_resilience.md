# WP-152 — Failure Taxonomy, Attribution and Resilience Controls

## Package card

| Field | Value |
|---|---|
| Work package | `WP-152` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Incident Commander / SRE Lead |
| Independent verifier | Assurance Lead / Research Director |
| Hard dependencies | WP-082, WP-096, WP-128, WP-148 |
| Related gates | G5,G6,Platform |
| Related controls | CTL-OPS-02, CTL-EPI-03 |
| Related acceptance scenarios | ACC-091, ACC-092, ACC-094, ACC-095 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-152_failure_taxonomy_and_resilience.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-152_failure_taxonomy_and_resilience.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A multi-agent failure is classified into a typed cause and routed to the discipline that can act on it — and `UNKNOWN` is a legitimate classification rather than a gap to be filled with a guess.


## Analysis

### What this package actually decides

That a failed collaboration produces a typed, routable record rather than a
transcript somebody has to read.

The taxonomy extends WP-082's `FailureAssessment` with the classes a cohort makes
possible: `COORDINATION` and `VERIFICATION` alongside `IMPLEMENTATION`,
`METHODOLOGY`, `DATA`, `HYPOTHESIS`, `INFRASTRUCTURE`, `POLICY` and `UNKNOWN`.

### `UNKNOWN` is the honest class, and it is load-bearing

Published attribution work reports that identifying the exact failing step in a
multi-agent trace is hard — the best reported methods sit low, and confident
attribution is often wrong.

So **no attributor is treated as an oracle.** `UNKNOWN` is a valid terminal
classification that routes to human diagnosis — ACC-094. A taxonomy that forces
every failure into a named cause produces a tidy register of misattributions, and
the second-order cost is worse than the first: work gets routed to the wrong
discipline and the real cause goes unexamined.

### Routing is the point of classifying

| Class | Routed to |
|---|---|
| `IMPLEMENTATION` | engineering debugging — WP-154 |
| `METHODOLOGY` | protocol challenge — WP-081 |
| `DATA` | data steward |
| `HYPOTHESIS` | scientific discovery — only from a validly executed run |
| `INFRASTRUCTURE` | operations |
| `COORDINATION` | the collaboration plane — WP-148, WP-149 |
| `VERIFICATION` | assurance — WP-155 |
| `SECURITY` / `POLICY` | block and escalate |
| `UNKNOWN` | human diagnosis |

The `HYPOTHESIS` row carries the constraint from ACC-064: only a validly executed
run under the frozen plan can support it.

### Challenger and Inspector, and what they are not

A **Challenger** targets assumptions and contradictions in peer output. An
**Inspector** checks high-consequence messages and artifacts against
specification, evidence and policy — ACC-092.

Both improve recovery and **neither holds gate authority**. They produce findings
that route like any other finding, which is the same boundary WP-147 draws around
the scientific council: cognition that is permitted to recommend must be recorded
as recommending, in a field rather than in prose.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md) | `OTel platform` · `Semantic conventions` · `Instrumentation libraries` · `Trace completeness dashboard` |
| [WP-128 — Incident, Postmortem and Learning Closure](../11_DAY2_OPERATIONS/WP-128_incident_learning.md) | `IncidentRecords` · `Forensic packages` · `Postmortems` · `Learning/action register` |
| [WP-148 — Multi-Agent Collaboration Plane and Cohort Integrity](../15_RELIABILITY_EFFICIENCY/WP-148_multi_agent_collaboration_plane.md) | `AgentCohortRecord` · `CognitiveDiversityProfile` · `InitialPositionArtifact` · `MaterialChallenge` |

### Full prerequisite closure

**126 of 160 packages (79%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` · `WP-098` |
| 33 | `WP-073` · `WP-077` · `WP-078` · `WP-094` · `WP-101` |
| 34 | `WP-074` · `WP-079` · `WP-085` · `WP-103` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` · `WP-147` |
| 38 | `WP-088` · `WP-148` |
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
| 54 | `WP-128` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | unassigned |
| Dependency depth | level **55** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Incident Commander / SRE Lead |
| Independent verifier | Assurance Lead / Research Director |
| Gates touched | `G5` · `G6` · `Platform` |
| Controls | `CTL-OPS-02` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-091 — Faulty Agent Output Does Not Propagate](../12_ACCEPTANCE_SCENARIOS/ACC-091_faulty_agent_challenge.md) | Critical | The faulty output is challenged rather than absorbed, does not reach any canonical record, and the failure is classified and routed. The Challenger's finding does not itself close a gate. |
| [ACC-092 — Inspector Reviews High-Consequence Output](../12_ACCEPTANCE_SCENARIOS/ACC-092_inspector_high_consequence_review.md) | High | Inconsistencies are raised as findings and routed. The Inspector holds no gate authority, and a clean Inspector result does not by itself satisfy any required verification. |
| [ACC-094 — An Unattributable Failure Is `UNKNOWN`](../12_ACCEPTANCE_SCENARIOS/ACC-094_failure_cause_unknown.md) | High | The failure is classified `UNKNOWN` and routed to human diagnosis. It is not forced into a named class, and `UNKNOWN` is a terminal classification rather than a pipeline defect. |
| [ACC-095 — Failure Taxonomy Routing](../12_ACCEPTANCE_SCENARIOS/ACC-095_failure_taxonomy_routing.md) | High | Each reaches its owning discipline. A `HYPOTHESIS` class is reachable only from a validly executed run under the frozen plan — the other classes cannot produce it however the run failed. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-128 — Incident, Postmortem and Learning Closure](../11_DAY2_OPERATIONS/WP-128_incident_learning.md), [WP-148 — Multi-Agent Collaboration Plane and Cohort Integrity](WP-148_multi_agent_collaboration_plane.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Run Registry` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Preflight validator` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `MLflow integration` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lineage queries` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lifecycle dashboard` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `RawEvaluatorArtifact` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `VerifiedValue` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `PredictionRecord` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `FailureAssessment` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `ModelExecutionFingerprint` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `OTel platform` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Semantic conventions` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Instrumentation libraries` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Trace completeness dashboard` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `IncidentRecords` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Forensic packages` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Postmortems` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Learning/action register` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `Closure evidence` | `WP-128` | `python3 scripts/progress.py show WP-128` |
| `AgentCohortRecord` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `CognitiveDiversityProfile` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `InitialPositionArtifact` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `MaterialChallenge` | `WP-148` | `python3 scripts/progress.py show WP-148` |
| `ConvergenceAssessment` | `WP-148` | `python3 scripts/progress.py show WP-148` |

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
- **Incident Commander / SRE Lead** carries the acceptance decision; **Assurance Lead / Research Director** must verify independently of whoever implements.
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
| WP-152-T01 | Extend the failure taxonomy with `COORDINATION` and `VERIFICATION` | Implementation owner | Commit / configuration / record reference |
| WP-152-T02 | Implement the trace-to-candidate-cause pipeline | Implementation owner | Commit / configuration / record reference |
| WP-152-T03 | Make `UNKNOWN` a terminal class routed to human diagnosis | Implementation owner | Commit / configuration / record reference |
| WP-152-T04 | Implement routing per class to the owning discipline | Implementation owner | Commit / configuration / record reference |
| WP-152-T05 | Implement Challenger and Inspector as advisory functions with no gate authority | Implementation owner | Commit / configuration / record reference |
| WP-152-T06 | Build the faulty-agent and malicious-agent fixture suite | Implementation owner | Commit / configuration / record reference |
| WP-152-T07 | Emit failure-class distribution and attribution-confidence metrics | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Extended FailureAssessment taxonomy`
- `Attribution pipeline`
- `Challenger and Inspector functions`
- `Faulty-agent fixture suite`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-152_failure_taxonomy_and_resilience.tests.md`](WP-152_failure_taxonomy_and_resilience.tests.md).

- A failure whose cause cannot be established must classify as UNKNOWN, not guess
- Each class must route to its owning discipline, verified per class
- A faulty agent's output must not propagate into a canonical record
- A malicious agent must not be able to bind authority anywhere
- Challenger and Inspector findings must not close a gate
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-152_failure_taxonomy_and_resilience.acceptance.md`](WP-152_failure_taxonomy_and_resilience.acceptance.md), together with what this package still cannot establish.

- [ ] `UNKNOWN` is reachable, terminal, and routed rather than treated as a defect.
- [ ] Every failure class routes to a named owner, and the routing is tested per class.
- [ ] A faulty or malicious actor in the cohort cannot write canonical state or bind authority.
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

- An efficiency measure that improves a cost number and quietly lowers assurance has moved the failure, not removed it. Every optimisation here is anchored to a quality guard and rolls back when it trips.
- A coordination defect is invisible in a healthy run and obvious only in a post-mortem. These packages are specified as injection suites for that reason, not as properties.
- Multi-agent cost pressure always argues for fewer agents. The cohort is fixed by ADR-011 and is not a lever any package here may pull.

## Rollback / compensation

Failure records are immutable: a re-attribution creates a successor assessment naming the one it supersedes, so a corrected diagnosis never erases the original reading.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
