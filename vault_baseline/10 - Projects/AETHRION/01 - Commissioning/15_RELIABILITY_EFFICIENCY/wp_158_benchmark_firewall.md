---
title: "WP-158 — Benchmark Firewall and External Evaluation Qualification"
aliases:
  - "WP-158"
  - "WP-158 — Benchmark Firewall and External Evaluation Qualification"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "An external benchmark runs behind a frozen firewall with audited retrieval, and a run that could have seen the answers is labelled rather than reported as clean."
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-158_benchmark_firewall.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g6
  - aethrion/gate/platform
  - aethrion/state/not-started
---

# WP-158 — Benchmark Firewall and External Evaluation Qualification

## Package card

| Field | Value |
|---|---|
| Work package | `WP-158` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Eval Office |
| Independent verifier | Assurance Lead / Research Director |
| Hard dependencies | WP-043, WP-057, WP-115, WP-149 |
| Related gates | G6,Platform |
| Related controls | CTL-SEC-04, CTL-EPI-04 |
| Related acceptance scenarios | ACC-118 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_158_benchmark_firewall.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_158_benchmark_firewall.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

An external benchmark runs behind a frozen firewall with audited retrieval, and a run that could have seen the answers is labelled rather than reported as clean.


## Analysis

### What this package actually decides

How to run an external benchmark so that its score means something, and what is
reported when it does not.

This architecture leans on external benchmarks — they are one of only two doors
external truth comes through. A score is worth having only if the system could
not have seen the answers.

### Search-time contamination is the new failure

Training-data contamination is known and partly addressable by using recent
benchmarks. **Search-time contamination is not**: the agent retrieves the answer
during the run — from a leaderboard, a paper, an issue thread — and reported work
puts the resulting inflation at several points.

Nothing about the model is contaminated. The measurement is. So the firewall is
about the run:

| Frozen before the run | Why |
|---|---|
| Dataset manifest digest | The task set cannot drift between runs |
| Network mode and allowed domains | Retrieval scope is a decision, not an accident |
| Known benchmark identifiers | The scanner knows what to look for |
| Evaluator isolation mode | The grader is unreachable — `ADR-007` |
| Contamination policy | The response to a hit is decided before there is a hit |

### Labelled, not silently rerun

Where benchmark material appears in the search log, the run is `CONTAMINATED` or
`REVIEW_REQUIRED` and its score is **never reported as a clean score** — ACC-118.

It is also not quietly rerun until it comes back clean. That is the same
selective-reporting failure the architecture refuses everywhere else, and it is
more tempting here because the fix looks like diligence.

### The baseline the efficiency claim needs

WP-149 and WP-150 claim the optimised cohort is cheaper without being worse. That
needs something to be cheaper **than**, and the baseline is the **naive fully
connected cohort** — not a single agent.

Comparing to one agent measures the cost of having a cohort at all, which
`ADR-011` decided on epistemic grounds and is not up for re-litigation on cost.
Both arms run under the same firewall, the same manifest and the same budget, and
the result is reported as a frontier rather than a number.

### What a false positive costs

The scanner will flag legitimate papers that discuss the benchmark.
`REVIEW_REQUIRED` exists so a human sorts those — a pipeline that guesses would
either suppress good runs or wave through bad ones, and both destroy the number's
meaning in different directions.

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
| [WP-043 — Role-Based Model and Skill Evaluation, and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md) | `Eval dataset manifests` · `Role eval harness` · `Grader/rubric bundle` · `Contamination controls` |
| [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/wp_057_egress_proxy_dlp.md) | `Egress proxy` · `Allowlist registry` · `DLP pipeline` · `Egress audit/alerts` |
| [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md) | `Commissioning Dossier` · `RC evidence manifest` · `Finding/risk register snapshot` · `Readiness scorecard` |
| [WP-149 — Sparse Communication Topology and the Scientific Blackboard](../15_RELIABILITY_EFFICIENCY/wp_149_sparse_topology_and_blackboard.md) | `BlackboardEntry` · `TypedAgentMessage` · `CommunicationGraph` · `CommunicationEdgePolicy` |

### Full prerequisite closure

**120 of 160 packages (75%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 39 | `WP-089` · `WP-149` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` · `WP-102` · `WP-107` |
| 42 | `WP-104` |
| 43 | `WP-105` |
| 44 | `WP-106` |
| 45 | `WP-108` |
| 46 | `WP-109` |
| 47 | `WP-110` · `WP-111` · `WP-112` · `WP-113` · `WP-114` |
| 48 | `WP-115` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | unassigned |
| Dependency depth | level **49** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Eval Office |
| Independent verifier | Assurance Lead / Research Director |
| Gates touched | `G6` · `Platform` |
| Controls | `CTL-SEC-04` · `CTL-EPI-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-118 — Search-Time Benchmark Contamination](../12_ACCEPTANCE_SCENARIOS/acc_118_benchmark_search_time_contamination.md) | Critical | The run is labelled `CONTAMINATED` or `REVIEW_REQUIRED` and its score is never reported as a clean score. A run with no benchmark material in its log is reported clean, and a contaminated run is not silently rerun. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-043 — Role-Based Model and **Skill** Evaluation, and Golden Set Management](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md), [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/wp_057_egress_proxy_dlp.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-149 — Sparse Communication Topology and the Scientific Blackboard](wp_149_sparse_topology_and_blackboard.md)
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
| `Eval dataset manifests` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Role eval harness` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Grader/rubric bundle` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Contamination controls` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Eval scorecard` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Cross-model × cross-harness compliance matrix` | `WP-043` | `python3 scripts/progress.py show WP-043` |
| `Egress proxy` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Allowlist registry` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `DLP pipeline` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Egress audit/alerts` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Exception runbook` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Commissioning Dossier` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `RC evidence manifest` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Finding/risk register snapshot` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Readiness scorecard` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Board verdict` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Faulty-agent, split-brain and contamination regression` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `BlackboardEntry` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `TypedAgentMessage` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `CommunicationGraph` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `CommunicationEdgePolicy` | `WP-149` | `python3 scripts/progress.py show WP-149` |
| `Naive fully-connected baseline harness` | `WP-149` | `python3 scripts/progress.py show WP-149` |

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
- **Eval Office** carries the acceptance decision; **Assurance Lead / Research Director** must verify independently of whoever implements.
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
| WP-158-T01 | Define `BenchmarkRunPolicy` and freeze it before execution | Implementation owner | Commit / configuration / record reference |
| WP-158-T02 | Implement network mode and allowed-domain enforcement per run | Implementation owner | Commit / configuration / record reference |
| WP-158-T03 | Implement the retrieval audit log and the contamination scanner | Implementation owner | Commit / configuration / record reference |
| WP-158-T04 | Define `ContaminationFinding` and the CONTAMINATED / REVIEW_REQUIRED labels | Implementation owner | Commit / configuration / record reference |
| WP-158-T05 | Enforce evaluator, rubric and gold-answer isolation from the agent environment | Implementation owner | Commit / configuration / record reference |
| WP-158-T06 | Build the fully-connected baseline arm and the frontier report | Implementation owner | Commit / configuration / record reference |
| WP-158-T07 | Bind labelled results into the release dossier | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `BenchmarkRunPolicy`
- `Contamination scanner and audit log`
- `ContaminationFinding`
- `Baseline arm and frontier report`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-158_benchmark_firewall.tests.md`](wp_158_benchmark_firewall.tests.md).

- A run whose search log contains benchmark material must be labelled, not scored clean
- Gold answers, rubrics, hidden tests and grader prompts must be unreachable from the agent
- A frozen benchmark policy must not be modifiable mid-run
- A contaminated run must not be silently rerun to obtain a clean score
- The efficiency comparison must run against the fully-connected baseline, not a single agent
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-158_benchmark_firewall.acceptance.md`](wp_158_benchmark_firewall.acceptance.md), together with what this package still cannot establish.

- [ ] A benchmark score is reported with the conditions it was produced under, or not at all.
- [ ] Evaluator material is unreachable from the agent environment under the supported threat model.
- [ ] The efficiency claim is measured against the naive fully-connected cohort.
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

A benchmark policy is frozen per run and immutable: a changed policy produces a new run, and a labelled result keeps its label permanently rather than being superseded by a cleaner rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
