# WP-098 — Grafana and the Six Operational Graphs

## Package card

| Field | Value |
|---|---|
| Work package | `WP-098` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Observability Lead |
| Independent verifier | Service Owners / FinOps / Assurance |
| Hard dependencies | WP-030, WP-096, WP-097 |
| Related gates | G0–G10,Platform |
| Related controls | CTL-OBS-01, CTL-OBS-02 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-098_grafana_six_graphs.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-098_grafana_six_graphs.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Correlated dashboards and alerts are built for the execution, workflow, experiment, knowledge/evidence, service/SLO and cost graphs.


## Analysis
### What this package actually decides

Which six questions the laboratory can answer at a glance, and — more usefully —
which signals it watches for its own failure modes.

Execution, workflow, experiment, knowledge/evidence, service/SLO, cost. Six graphs
because the system has six ways of going wrong, and a single dashboard that mixes
them tells nobody anything.

### The dashboards that matter are the ones nobody thinks to build

Four signals from `00_PROGRAM/07` and `00_PROGRAM/08` belong on these boards and
are routinely absent from real systems:

- **Median decision time falling while volume rises** — `PR-11`'s rubber-stamping
  signature. Counter-intuitive, and the reason it must be a chart rather than a
  number.
- **Assurance queue wait** — `PR-04`'s earliest observable signal, visible here
  long before it becomes a bypass request.
- **G10 reversal rate** — the outcome measure for decision quality.
- **Acceptance despite adversarial rejection** — the rate at which a falsification
  was produced and the decision proceeded anyway.

### Alerts without owners and runbooks are noise (T07)

An alert routed to nobody is a notification. `00_PROGRAM/09` and WP-101 both
require an owner; the link checker is what stops a runbook link rotting into a 404
discovered during an incident.

### The integrity dashboard is the one that would have caught this repository's own defects (T05)

Projection lag, orphaned anchors, unmonitored source fraction, queue depths,
overwrite-detector firings. Each of those has a real analogue in the running slice
today — the 100-record cap, the DOI-less 18 of 33, the vault churn — and each was
invisible until someone looked.

### Alerts must be able to fire (T07)

The repository's own rule: a check that cannot fail proves nothing. Every alert
needs a demonstrated firing, or it is a rule nobody has confirmed is wired.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md) | `OTel platform` · `Semantic conventions` · `Instrumentation libraries` · `Trace completeness dashboard` |
| [WP-097 — Langfuse Model/Agent Tracing and Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/WP-097_langfuse_llm_trace.md) | `Langfuse platform` · `Prompt registry` · `Trace/redaction policy` · `Retention/export runbook` |

### Full prerequisite closure

**54 of 141 packages (38%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |
| 30 | `WP-096` |
| 31 | `WP-097` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-101` · `WP-117`
- **Transitively reachable:** **25 of 141 packages (18%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **32** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Observability Lead |
| Independent verifier | Service Owners / FinOps / Assurance |
| Gates touched | `G0–G10` · `Platform` |
| Controls | `CTL-OBS-01` · `CTL-OBS-02` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-096 — OpenTelemetry End-to-End Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-097 — Langfuse Model/Agent Tracing and Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/WP-097_langfuse_llm_trace.md)
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
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `OTel platform` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Semantic conventions` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Instrumentation libraries` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Trace completeness dashboard` | `WP-096` | `python3 scripts/progress.py show WP-096` |
| `Langfuse platform` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Prompt registry` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Trace/redaction policy` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Retention/export runbook` | `WP-097` | `python3 scripts/progress.py show WP-097` |
| `Trace quality dashboard` | `WP-097` | `python3 scripts/progress.py show WP-097` |

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
- **Observability Lead** carries the acceptance decision; **Service Owners / FinOps / Assurance** must verify independently of whoever implements.
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
| WP-098-T01 | Establish the metric, log and trace stores and Grafana RBAC | Implementation owner | Commit / configuration / record reference |
| WP-098-T02 | Write the workflow, gate latency and blocker dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T03 | Write the execution queue, sandbox and tool dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T04 | Write the experiment, reproduction and evaluation quality dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T05 | Write the literature, claim and impact integrity dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T06 | Write the service/SLO/incident and cost/budget dashboard | Implementation owner | Commit / configuration / record reference |
| WP-098-T07 | Add alert routing, owners and runbook links | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Grafana platform`
- `Six graph dashboards`
- `Alert rules`
- `Dashboard/alert ownership catalog`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-098_grafana_six_graphs.tests.md`](WP-098_grafana_six_graphs.tests.md).

- A synthetic SLO breach alert
- Budget 80% and 100% events
- Projection lag
- G6/G7 backlog growth
- A security deny or egress event
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-098_grafana_six_graphs.acceptance.md`](WP-098_grafana_six_graphs.acceptance.md), together with what this package still cannot establish.

- [ ] Every alert carries a named owner and a runbook.
- [ ] Dashboards support decisions and actions rather than vanity metrics.
- [ ] Sensitive labels and logs are redacted.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A faulty alert or dashboard configuration is rolled back through GitOps; alert suppression is time-bound, owned and audited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
