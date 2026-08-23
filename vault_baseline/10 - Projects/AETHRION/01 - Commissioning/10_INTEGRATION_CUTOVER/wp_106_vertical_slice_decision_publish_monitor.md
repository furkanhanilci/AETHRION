---
title: "WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor"
aliases:
  - "WP-106"
  - "WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "A human G8 decision is taken with residual risk and dissent visible, a signed G9 package is published, and the G10 retraction/supersession impact flow runs."
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor

## Package card

| Field | Value |
|---|---|
| Work package | `WP-106` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Project Decision Owner |
| Independent verifier | Citation Auditor / Safety / Archivist |
| Hard dependencies | WP-037, WP-074, WP-077, WP-080, WP-085, WP-089, WP-090, WP-093, WP-095, WP-099, WP-105 |
| Related gates | G8,G9,G10 |
| Related controls | CTL-GOV-01, CTL-EPI-01, CTL-LIT-02 |
| Related acceptance scenarios | ACC-04, ACC-25, ACC-30, ACC-31, ACC-36, ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_106_vertical_slice_decision_publish_monitor.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_106_vertical_slice_decision_publish_monitor.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A human G8 decision is taken with residual risk and dissent visible, a signed G9 package is published, and the G10 retraction/supersession impact flow runs.


## Analysis
### What this package actually decides

Whether the loop closes. A decision is taken, a package is published, a source is
retracted, and the retraction reaches the published claim.

`AGENTS.md` §4.1 names the two properties that matter more than the chain itself:
it is **traversable in both directions**, and **`VERIFIED` is explicitly not a
permanent state**. This slice is where both are demonstrated for the first time,
and completing it is what lets `docs/STATUS.md` stop printing *no research question
has travelled G0 → G10*.

### The G8 decision must be a real decision (T01)

Evidence delta visible, dissent visible, residual risk visible, rationale required,
MFA at signing. If the decision in this slice is a click, the slice has demonstrated
the mechanism and not the control — and `PR-11` is the failure it is meant to
address.

### Publication runs three release checks, and the third is the one to watch (T02)

Licence, privacy, **security release**. A research laboratory is practised at the
first two. The third — does publishing reveal a protected locator, an internal
identifier, a capability-exposing prompt — is the one that gets waved through.

### G10 must run on three different trigger types (T04)

Retraction, correction, model drift. Each reaches the impact machinery by a
different path, and a slice that only tests retraction has tested the case everyone
designs for.

### The superseding package is the closing move (T05)

A published claim is challenged, a new package supersedes it, and **the prior
version stays reachable**. Nothing is withdrawn silently — which is what makes
publication compatible with a loop that reopens.

### The audit export is the acceptance test (T06)

Every step of this slice, verifiable from the standalone verifier with no access to
the running system. If the chain cannot be checked from outside, the system's
central claim is unverified by anyone but itself.

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

11, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/wp_037_g10_impactscan.md) | `ImpactScan workflow` · `Schedule registry` · `ImpactCase service contract` · `Supersession trigger` |
| [WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/wp_074_obsidian_projection_sync.md) | `Obsidian projection service` · `Link checker` · `Human-preservation diff` · `Concept graph projection` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md) | `Citation audit service` · `Audit rubric` · `Mechanical locator checker` · `Audit report/scorecard` |
| [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md) | `Verification pipeline` · `Type-specific protocols` · `Robustness matrix` · `Reproduction certificates` |
| [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md) | `Disagreement service` · `Arbitration rubric` · `Disposition workflow` · `Appeal/decision integration` |
| [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md) | `Publication builder` · `RO-Crate profile` · `Signed publication package` · `Release checklist` |
| [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md) | `Decision Queue UI` · `Evidence-delta component` · `Rationale forms` · `Delegation/escalation views` |
| [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md) | `Claim Explorer` · `Evidence preview` · `Provenance graph` · `Assessment/blocker panels` |
| [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md) | `Audit Ledger` · `Hash-chain service` · `Audit export/verify tooling` · `Retention/access policy` |
| [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/wp_105_vertical_slice_review_repro.md) | `Review/repro vertical dossier` · `ReviewRecords/DisagreementCase` · `ReproductionReport` · `Gate histories` |

### Full prerequisite closure

**94 of 160 packages (59%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` · `WP-091` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` · `WP-096` |
| 31 | `WP-068` · `WP-071` · `WP-097` · `WP-099` · `WP-100` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-073` · `WP-077` · `WP-078` |
| 34 | `WP-074` · `WP-079` · `WP-085` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-090` · `WP-093` |
| 41 | `WP-095` |
| 42 | `WP-104` |
| 43 | `WP-105` |

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-108` · `WP-109` · `WP-110`
- **Transitively reachable:** **26 of 160 packages (16%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **44** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Project Decision Owner |
| Independent verifier | Citation Auditor / Safety / Archivist |
| Gates touched | `G8` · `G9` · `G10` |
| Controls | `CTL-GOV-01` · `CTL-EPI-01` · `CTL-LIT-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-25 — Human Approval Forgery](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) | Critical | The decision is rejected; gate state does not change and a security event and audit record are produced. A valid owner with MFA and an idempotent request passes as the counter-example. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |
| [ACC-36 — Model Snapshot Drift](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) | Critical | The profile moves to suspension or requalification, the router cache is invalidated and an `ImpactScan` opens for open tasks, runs and claims; there is no unsafe fallback. |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-037 — G10 Temporal Schedules and Short ImpactScan Workflows](../04_CONTROL_EVENT/wp_037_g10_impactscan.md), [WP-074 — Obsidian Projection, Link Integrity and Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/wp_074_obsidian_projection_sync.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md), [WP-095 — Claim/Evidence Explorer and Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/wp_105_vertical_slice_review_repro.md)
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
| `Obsidian projection service` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Link checker` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Human-preservation diff` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Concept graph projection` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Rebuild runbook` | `WP-074` | `python3 scripts/progress.py show WP-074` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Citation audit service` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit rubric` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Mechanical locator checker` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit report/scorecard` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Decomposed citation audit with per-question verification class` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Verification pipeline` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Type-specific protocols` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Robustness matrix` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Reproduction certificates` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Failure taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `AlgorithmUnderstandingRecord` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ReproductionPackage` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ClaimConsistencyReport` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Five-level reproduction taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Disagreement service` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Arbitration rubric` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Disposition workflow` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Appeal/decision integration` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Publication builder` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `RO-Crate profile` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Signed publication package` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Release checklist` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Supersession record` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Publication compiler` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Assertion and value binding checks` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Decision Queue UI` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence-delta component` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Rationale forms` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Delegation/escalation views` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Decision audit export` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `HumanAttentionScore` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence delta view` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Human preliminary flow` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Friction symmetry measurement` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Claim Explorer` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Evidence preview` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Provenance graph` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Assessment/blocker panels` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Audit drill-down` | `WP-095` | `python3 scripts/progress.py show WP-095` |
| `Audit Ledger` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Hash-chain service` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Audit export/verify tooling` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Retention/access policy` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Integrity dashboard` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Review/repro vertical dossier` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `ReviewRecords/DisagreementCase` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `ReproductionReport` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `Gate histories` | `WP-105` | `python3 scripts/progress.py show WP-105` |

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
- **Project Decision Owner** carries the acceptance decision; **Citation Auditor / Safety / Archivist** must verify independently of whoever implements.
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
| WP-106-T01 | Run the evidence-delta, decision rationale and MFA update | Implementation owner | Commit / configuration / record reference |
| WP-106-T02 | Perform the publication completeness, licence and privacy checks | Implementation owner | Commit / configuration / record reference |
| WP-106-T03 | Produce the RO-Crate, signature, archive and release event | Implementation owner | Commit / configuration / record reference |
| WP-106-T04 | Trigger a retraction, a correction and a model drift signal | Implementation owner | Commit / configuration / record reference |
| WP-106-T05 | Create the `ImpactCase`, claim challenge, owner queue item and superseding package | Implementation owner | Commit / configuration / record reference |
| WP-106-T06 | Verify the full chain in the audit export | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Decision/publish/monitor dossier`
- `DecisionRecord`
- `PublicationPackage`
- `ImpactCase/Supersession`
- `Audit export`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-106_vertical_slice_decision_publish_monitor.tests.md`](wp_106_vertical_slice_decision_publish_monitor.tests.md).

- G9 failing on a missing locator
- Denial of a forged decision
- Retraction impact propagation
- An old link surviving a superseded publication
- Full-chain audit verification
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-106_vertical_slice_decision_publish_monitor.acceptance.md`](wp_106_vertical_slice_decision_publish_monitor.acceptance.md), together with what this package still cannot establish.

- [ ] A release happens only through a named human decision.
- [ ] An older publication stays reachable and is visibly superseded.
- [ ] G10 never silently mutates a claim.
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

A pre-release rollback invalidates the draft; after release, only a superseding publication and an impact workflow are permitted.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
