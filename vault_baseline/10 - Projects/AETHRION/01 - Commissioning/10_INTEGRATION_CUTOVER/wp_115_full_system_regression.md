---
title: "WP-115 — Full System Regression and Commissioning Dossier"
aliases:
  - "WP-115"
  - "WP-115 — Full System Regression and Commissioning Dossier"
type: work-package
category: commissioning
status: NOT_STARTED
summary: "The PREGOLIVE scenarios plus the contract, replay, attack, restore and capacity evidence are consolidated for one release candidate into a single signed Commissioning Dossier."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
---

# WP-115 — Full System Regression and Commissioning Dossier

## Package card

| Field | Value |
|---|---|
| Work package | `WP-115` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Commissioning Board |
| Hard dependencies | WP-110, WP-111, WP-112, WP-113, WP-114 |
| Related gates | Commissioning |
| Related controls | All controls |
| Related acceptance scenarios | every scenario whose `Acceptance phase` is `PRE_GO_LIVE` (ACC-01 – ACC-51 excluding the Day-2 set) |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_115_full_system_regression.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_115_full_system_regression.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The `PRE_GO_LIVE` scenarios plus the contract, replay, attack, restore and capacity evidence are consolidated for one release candidate into a single signed Commissioning Dossier.


## Analysis
### What this package actually decides

Whether everything passed **on the same thing**. The Commissioning Dossier's value
is not that it collects results; it is that it proves every result came from one
release candidate.

`00_PROGRAM/06` lists what is not evidence, and the second entry is *test outputs
from different revisions mixed together.*

### The count is 51 and the purpose sentence says forty-six

`12_ACCEPTANCE_SCENARIOS/` holds ACC-01 through ACC-51. The task list here says
"the forty-six scenarios", which predates ACC-47–51. **The dossier must consolidate
all `PRE_GO_LIVE` scenarios**, which is currently all 51.

### The open-findings sweep is the step that decides the verdict (T04)

`00_PROGRAM/10`: open critical findings = 0; open high findings = 0 or a
time-boxed, waivable residual risk accepted by the Commissioning Board. And
`00_PROGRAM/07`: security, identity, evidence, reproduction and data blockers are
**not waivable at all**.

An expiry sweep belongs here too — an accepted residual risk whose expiry has passed
is an open finding again.

### `BLOCKED` is a legitimate verdict and this package must be able to reach it (T06)

A board review that can only produce `READY` is a formality. Given the current
state — no package accepted, R3 blocked under ADR-001, no scenario ever run — the
honest first verdict is `BLOCKED`, and the dossier's value is that it says exactly
why.

### The readiness scorecard has to include the uncomfortable numbers (T05)

KPIs and SLOs, yes. Also: the number of scenarios that passed by witnessed manual
step rather than automation, the number skipped, the flake rate, and the fraction of
sources the monitoring actually covers.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

5, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-110 — Research and Literature Acceptance Package](../10_INTEGRATION_CUTOVER/wp_110_research_acceptance.md) | `ACC-01–08 results` · `Research acceptance dossier` · `Finding/disposition records` · `Owner sign-off` |
| [WP-111 — Reliability, Event and FinOps Acceptance Package](../10_INTEGRATION_CUTOVER/wp_111_reliability_finops_acceptance.md) | `Reliability/FinOps scenario results` · `Fault injection report` · `SLO/cost evidence` · `Owner sign-off` |
| [WP-112 — Security and Privacy Acceptance Package](../10_INTEGRATION_CUTOVER/wp_112_security_privacy_acceptance.md) | `Security scenario results` · `Red-team report` · `Forensic evidence` · `Security acceptance statement` |
| [WP-113 — Evidence, Reproduction and Publication Acceptance Package](../10_INTEGRATION_CUTOVER/wp_113_evidence_repro_acceptance.md) | `Evidence/repro scenario results` · `Reproduction certificates` · `Lineage/integrity reports` · `Assurance sign-off` |
| [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md) | `Two DR drill reports` · `Restore manifests` · `Integrity query results` · `RPO/RTO scorecard` |

### Full prerequisite closure

**114 of 141 packages (81%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-116` · `WP-117` · `WP-118` · `WP-119` · `WP-120` · `WP-130`
- **Transitively reachable:** **15 of 141 packages (11%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **48** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Commissioning Board |
| Gates touched | `Commissioning` |
| Controls | `All controls` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-01 — Human Seed Literature](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) | Critical | The source resolves to a single `SourceRecord`/representation, enters the G3 candidate and set chain, and **no field in personal Zotero is modified**. |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-110 — Research and Literature Acceptance Package](../10_INTEGRATION_CUTOVER/wp_110_research_acceptance.md), [WP-111 — Reliability, Event and FinOps Acceptance Package](../10_INTEGRATION_CUTOVER/wp_111_reliability_finops_acceptance.md), [WP-112 — Security and Privacy Acceptance Package](../10_INTEGRATION_CUTOVER/wp_112_security_privacy_acceptance.md), [WP-113 — Evidence, Reproduction and Publication Acceptance Package](../10_INTEGRATION_CUTOVER/wp_113_evidence_repro_acceptance.md), [WP-114 — Operations, DR and Restore Acceptance Package](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md)
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
| `ACC-01–08 results` | `WP-110` | `python3 scripts/progress.py show WP-110` |
| `Research acceptance dossier` | `WP-110` | `python3 scripts/progress.py show WP-110` |
| `Finding/disposition records` | `WP-110` | `python3 scripts/progress.py show WP-110` |
| `Owner sign-off` | `WP-110` | `python3 scripts/progress.py show WP-110` |
| `Reliability/FinOps scenario results` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `Fault injection report` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `SLO/cost evidence` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `Owner sign-off` | `WP-111` | `python3 scripts/progress.py show WP-111` |
| `Security scenario results` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Red-team report` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Forensic evidence` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Security acceptance statement` | `WP-112` | `python3 scripts/progress.py show WP-112` |
| `Evidence/repro scenario results` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Reproduction certificates` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Lineage/integrity reports` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Assurance sign-off` | `WP-113` | `python3 scripts/progress.py show WP-113` |
| `Two DR drill reports` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Restore manifests` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `Integrity query results` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `RPO/RTO scorecard` | `WP-114` | `python3 scripts/progress.py show WP-114` |
| `DR sign-off` | `WP-114` | `python3 scripts/progress.py show WP-114` |

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
- **Platform Assurance Lead** carries the acceptance decision; **Commissioning Board** must verify independently of whoever implements.
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
| WP-115-T01 | Freeze the RC digest and every bundle version | Implementation owner | Commit / configuration / record reference |
| WP-115-T02 | Verify that every `PRE_GO_LIVE` scenario result comes from the same RC | Implementation owner | Commit / configuration / record reference |
| WP-115-T03 | Consolidate the contract, replay, security, reproduction, DR, cost and trace evidence manifests | Implementation owner | Commit / configuration / record reference |
| WP-115-T04 | Sweep for open findings, risks, exceptions and expiries | Implementation owner | Commit / configuration / record reference |
| WP-115-T05 | Produce the KPI, SLO, capacity and owner readiness scorecard | Implementation owner | Commit / configuration / record reference |
| WP-115-T06 | Hold the independent board review and record the BLOCKED/READY verdict | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Commissioning Dossier`
- `RC evidence manifest`
- `Finding/risk register snapshot`
- `Readiness scorecard`
- `Board verdict`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-115_full_system_regression.tests.md`](wp_115_full_system_regression.tests.md).

- Consistency of the RC and bundle versions
- Evidence link, hash and signature verification
- An open-critical query returning zero
- An expired exception and profile scan
- Completeness of all scenarios
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-115_full_system_regression.acceptance.md`](wp_115_full_system_regression.acceptance.md), together with what this package still cannot establish.

- [ ] Every `PRE_GO_LIVE` scenario PASSes.
- [ ] Open critical findings = 0.
- [ ] Required high findings = 0, or an explicitly permitted residual risk.
- [ ] The dossier is independently verified and signed.
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

Without a READY verdict the RC is not promoted; a correction produces a new RC digest and the affected plus baseline regression is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
