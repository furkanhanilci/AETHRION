# WP-118 — Operational Readiness, On-Call and Runbook Simulation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-118` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | SRE Lead |
| Independent verifier | Internal Audit / Service Owners |
| Hard dependencies | WP-099, WP-101, WP-114, WP-115, WP-116, WP-117 |
| Related gates | Commissioning |
| Related controls | CTL-OPS-03, CTL-GOV-01 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-118_operational_readiness.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-118_operational_readiness.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The service owner, on-call, escalation, incident command, break-glass, backup/restore, reconciliation, security and business continuity runbooks have all been **executed** in staging.


## Analysis
### What this package actually decides

That the runbooks work when executed by someone under pressure. The purpose
sentence carries the whole standard in one word: every runbook has been
**executed** in staging.

`PR-13`'s failure — *exists only on paper* — generalises past backups to every
operational procedure.

### The link checker is trivial and always skipped (T01)

A runbook whose links are dead is discovered during an incident. Checking them on a
schedule costs nothing and is exactly the sort of check that never gets written.

### The tabletop and the live simulation test different things (T03)

A tabletop tests whether people know what to do. A live simulation tests whether
the procedure survives contact with the system — and the gap between the two is
where most incident response actually fails.

### Two-person break-glass is the requirement a solo laboratory cannot meet (T04)

WP-055 already frames it. The honest outcome here is ADR-001's: **declare the gap**
with a residual-risk owner and an expiry, rather than implementing a one-person path
and calling it two-person. A break-glass requiring two approvals from the same
person is worse than one requiring one, because it looks like a control.

### The reconciliation runbooks are the ones that touch a researcher's data (T05)

Zotero, tool, event, policy and model reconciliation. The Zotero one in particular
can duplicate a library or overwrite human edits (WP-067), and it must be executed
against a library that has been edited since — not a clean fixture.

### Every gap becomes a finding

A runbook rehearsal that finds nothing has usually rehearsed a path someone already
knew.

### Baseline v1.3.0 — the slices exercise the cohort, and the regression injects faults

The vertical slices and the cutover path grow to cover what this baseline adds,
and one package changes character.

**WP-107 becomes the engineering completion slice.** Requirement and
specification → worktree → TDD → code review → CI → supply-chain attestation →
signed artifact → **eligibility to produce scientific evidence**. That last arrow
is the junction between the two disciplines, and before this baseline nothing
proved it end to end.

**The other slices exercise the collaboration plane**: a compiled cohort, sealed
initial positions, typed delta exchange over a sparse topology, an adaptive
assurance route, a fingerprinted reproduction and a firewalled benchmark run.

**The regression suite gains injections rather than cases.** Faulty agent,
malicious agent, split brain, duplicate and out-of-order events, communication
degradation under budget pressure, and benchmark contamination. These are
failures that are invisible in a healthy run and obvious only in a post-mortem,
which is why they are caused deliberately rather than waited for.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md) | `Audit Ledger` · `Hash-chain service` · `Audit export/verify tooling` · `Retention/access policy` |
| [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md) | `Service Catalog` · `SLO catalog` · `Error-budget policy` · `Alert-runbook link checker` |
| [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/WP-114_operations_dr_acceptance.md) | `Two DR drill reports` · `Restore manifests` · `Integrity query results` · `RPO/RTO scorecard` |
| [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md) | `Commissioning Dossier` · `RC evidence manifest` · `Finding/risk register snapshot` · `Readiness scorecard` |
| [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md) | `Chaos test suite/results` · `Steady-state hypotheses` · `Recovery/integrity report` · `Resilience sign-off` |
| [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/WP-117_performance_capacity.md) | `Load test suite/results` · `Capacity model` · `Bottleneck/tuning report` · `Cost/headroom forecast` |

### Full prerequisite closure

**118 of 160 packages (74%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-119` · `WP-120` · `WP-128`
- **Transitively reachable:** **12 of 160 packages (8%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W7 — Commissioning |
| Dependency depth | level **50** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | SRE Lead |
| Independent verifier | Internal Audit / Service Owners |
| Gates touched | `Commissioning` |
| Controls | `CTL-OPS-03` · `CTL-GOV-01` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-101 — Service Catalogue, SLOs and Alert/Runbook Binding](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/WP-114_operations_dr_acceptance.md), [WP-115 — Full System Regression and Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md), [WP-116 — Resilience, Chaos and Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md), [WP-117 — Performance, Capacity and Load Commissioning](../10_INTEGRATION_CUTOVER/WP-117_performance_capacity.md)
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
| `Two DR drill reports` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Restore manifests` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Integrity query results` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `RPO/RTO scorecard` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `DR sign-off` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Commissioning Dossier` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `RC evidence manifest` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Finding/risk register snapshot` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Readiness scorecard` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Board verdict` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Faulty-agent, split-brain and contamination regression` | `WP-115` | `python3 scripts/progress.py show WP-115` |
| `Chaos test suite/results` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Steady-state hypotheses` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Recovery/integrity report` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Resilience sign-off` | `WP-116` | `python3 scripts/progress.py show WP-116` |
| `Load test suite/results` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity model` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Bottleneck/tuning report` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Cost/headroom forecast` | `WP-117` | `python3 scripts/progress.py show WP-117` |
| `Capacity sign-off` | `WP-117` | `python3 scripts/progress.py show WP-117` |

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
- **SRE Lead** carries the acceptance decision; **Internal Audit / Service Owners** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-118`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-118-T01 | Complete the runbook catalogue and its freshness and link checks | Implementation owner | Commit / configuration / record reference |
| WP-118-T02 | Test the on-call rota, escalation and paging | Implementation owner | Commit / configuration / record reference |
| WP-118-T03 | Run the incident commander tabletop and a live simulation | Implementation owner | Commit / configuration / record reference |
| WP-118-T04 | Exercise the two-person break-glass and credential revocation | Implementation owner | Commit / configuration / record reference |
| WP-118-T05 | Apply the Zotero, tool, event, policy and model reconciliation runbooks | Implementation owner | Commit / configuration / record reference |
| WP-118-T06 | Complete handover, training and the readiness sign-off | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Operational Readiness Review`
- `Runbook execution records`
- `On-call simulation`
- `Training/ownership sign-offs`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-118_operational_readiness.tests.md`](WP-118_operational_readiness.tests.md).

- An after-hours page and escalation
- Reconciliation of an uncertain tool write
- A policy rollback
- A model revocation
- Security containment
- A restore invocation
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-118_operational_readiness.acceptance.md`](WP-118_operational_readiness.acceptance.md), together with what this package still cannot establish.

- [ ] Every critical service has a 24×7 owner and a runbook.
- [ ] A runbook is executed evidence, not an unread document.
- [ ] Break-glass audit and revocation both work.
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

A readiness failure blocks cutover; the date is not approved until every missing owner and runbook is resolved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
