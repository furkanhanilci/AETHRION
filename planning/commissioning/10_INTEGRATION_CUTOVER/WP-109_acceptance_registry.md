# WP-109 — Acceptance Scenario Registry and Harness

## Package card

| Field | Value |
|---|---|
| Work package | `WP-109` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Commissioning Board |
| Hard dependencies | WP-002, WP-009, WP-020, WP-024, WP-040, WP-060, WP-090, WP-099, WP-102, WP-103, WP-104, WP-105, WP-106, WP-107, WP-108 |
| Related gates | Commissioning |
| Related controls | CTL-OPS-02, CTL-SEC-04 |
| Related acceptance scenarios | Assigned during the relevant vertical slice and commissioning |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-109_acceptance_registry.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-109_acceptance_registry.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

ACC-01 to ACC-40 become runnable — automatically or with a witnessed manual step — in a versioned test registry carrying Given/When/Then, fixtures, expected events and invariants, evidence, owner, severity and cleanup.


## Analysis
### What this package actually decides

That an acceptance scenario is a **program**, not a paragraph. Fifty-one scenarios
currently exist as Given/When/Then prose; this package turns them into a versioned
registry with fixtures, assertions, evidence capture and cleanup.

### The count is 51, and the package card says 40

`planning/commissioning/12_ACCEPTANCE_SCENARIOS/` holds **ACC-01 through ACC-51**.
The purpose sentence here says ACC-01 to ACC-40, which predates ACC-41–46 (skill
governance) and ACC-47–51. **The registry must cover all 51**, and the discrepancy
is a correction this package carries rather than a scope question.

### Every scenario is `PRE_GO_LIVE` and that is a finding

All 51 carry `PRE_GO_LIVE`. The go-live checklist (`00_PROGRAM/10`) also requires
that *every `DAY2_CONTINUOUS` scenario is armed and scheduled* — and **no scenario
carries that phase**, so the condition is vacuously satisfied.

Either the Day-2 scenarios were never written, or the phase is unused. This package
surfaces it; resolving it is a plan change.

### The witness protocol is what makes a manual step evidence (T05)

Some scenarios need a human — a DR drill, a decision, a physical check. A manual
step with no witness record is an assertion. The protocol needs the witness's
identity, what they observed, and a timestamp, or the scenario cannot be counted.

### Skip and waiver rules must be narrow (T06)

`00_PROGRAM/05`: *a `SKIPPED` scenario on a critical package does not count as a
pass.* And `00_PROGRAM/07`: a Critical scenario can never be counted as PASS through
a SKIP or a waiver. Thirty-three of the 51 are Critical.

### Flakiness is a finding, not a retry setting (T06)

A scenario that passes on retry has told you something. Recording the flake rate and
treating a flaky critical scenario as a finding is what stops retries from becoming
a way to pass.

### Baseline v1.2.0 — the registry is count-neutral by construction

This package was titled *Forty Acceptance Scenario Registry and Harness* while the
plan held fifty-one scenarios, and now holds eighty. The number in the title was
wrong twice for the same reason, and the second time it was wrong in a document
whose job is to know how many scenarios there are.

The title is now count-neutral, and the harness derives its scenario set from the
scenario files rather than from a list. Any number written into prose here is a
number that will be stale again.

The registry must also carry the two `DAY2_CONTINUOUS` scenarios distinctly:
armed at cutover, not passed before it. `validate_commissioning_plan.py` rule 6
already refuses a `PRE_GO_LIVE` scenario that depends on a Day-2 package, and the
harness must not quietly re-create that cycle by treating every scenario as a
go-live precondition.

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

15, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md) | `Requirement Registry` · `NFR scorecard` · `Traceability matrix seed` · `Scope boundary record` |
| [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/WP-009_control_exception_catalog.md) | `Control Catalog` · `ExceptionPolicy` · `NonWaivableBlocker registry` · `Control-test mapping` |
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md) | `CI pipelines` · `Verification summary schema adapter` · `Test ownership registry` · `Flake policy` |
| [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/WP-040_workflow_replay_failure_suite.md) | `Replay test suite` · `Golden histories` · `Fault-injection harness` · `Workflow compatibility report` |
| [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md) | `Agentic attack suite` · `Malicious fixture corpus` · `Red-team report template` · `Security regression schedule` |
| [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md) | `Publication builder` · `RO-Crate profile` · `Signed publication package` · `Release checklist` |
| [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md) | `Audit Ledger` · `Hash-chain service` · `Audit export/verify tooling` · `Retention/access policy` |
| [WP-102 — Vertical Slice 1 — Intake through Protocol Freeze](../10_INTEGRATION_CUTOVER/WP-102_vertical_slice_intake_protocol.md) | `Vertical slice dossier` · `R1/R3 project histories` · `Trace/audit/decision evidence` · `Integration findings` |
| [WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze](../10_INTEGRATION_CUTOVER/WP-103_vertical_slice_literature.md) | `Literature vertical dossier` · `Frozen LiteratureSetManifest` · `Zotero SyncReceipts` · `Coverage/screening report` |
| [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_vertical_slice_run_claim.md) | `Run/claim vertical dossier` · `Run manifests/artifacts` · `Claim/Evidence records` · `Cost/trace/audit evidence` |
| [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/WP-105_vertical_slice_review_repro.md) | `Review/repro vertical dossier` · `ReviewRecords/DisagreementCase` · `ReproductionReport` · `Gate histories` |
| [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.md) | `Decision/publish/monitor dossier` · `DecisionRecord` · `PublicationPackage` · `ImpactCase/Supersession` |
| [WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release](../10_INTEGRATION_CUTOVER/WP-107_engineering_vertical_slice.md) | `Engineering vertical dossier` · `Frozen review packets` · `Validated findings` · `Signed OCI/release` |
| [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.md) | `Impact vertical dossier` · `ImpactCase set` · `Affected-object accuracy report` · `Supersession/re-evaluation records` |

### Full prerequisite closure

**108 of 160 packages (68%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 6 — `WP-110` · `WP-111` · `WP-112` · `WP-113` · `WP-114` · `WP-130`
- **Transitively reachable:** **24 of 160 packages (15%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W6 — Vertical integration |
| Dependency depth | level **46** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Platform Assurance Lead |
| Independent verifier | Commissioning Board |
| Gates touched | `Commissioning` |
| Controls | `CTL-OPS-02` · `CTL-SEC-04` |

### Acceptance scenarios that exercise this package

**None.** No acceptance scenario names this package.

> `00_PROGRAM/11_scope_coverage_matrix.md` states the rule this trips: *a row with a primary package but no acceptance column is a capability nobody will ever be asked to demonstrate.* This package can reach `ACCEPTED` on its own tests, but it cannot reach `COMMISSIONED` through a scenario, because there is none to pass.

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-002 — Scope, NFRs and Requirement Traceability](../01_GOVERNANCE/WP-002_scope_nfr_traceability.md), [WP-009 — Control Catalogue, Exceptions and Non-Waivable Blockers](../01_GOVERNANCE/WP-009_control_exception_catalog.md), [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-040 — Workflow Replay, Versioning and Failure Test Suite](../04_CONTROL_EVENT/WP-040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite and Red-Team Acceptance](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md), [WP-099 — WORM Audit Ledger and Independent Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-102 — Vertical Slice 1 — Intake through Protocol Freeze](../10_INTEGRATION_CUTOVER/WP-102_vertical_slice_intake_protocol.md), [WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze](../10_INTEGRATION_CUTOVER/WP-103_vertical_slice_literature.md), [WP-104 — Vertical Slice 3 — Baseline through Run to Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_vertical_slice_run_claim.md), [WP-105 — Vertical Slice 4 — Blind Review, Arbitration and Clean-Room](../10_INTEGRATION_CUTOVER/WP-105_vertical_slice_review_repro.md), [WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor](../10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.md), [WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release](../10_INTEGRATION_CUTOVER/WP-107_engineering_vertical_slice.md), [WP-108 — Retraction, Drift and Supersession Vertical Slice](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.md)
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
| `Requirement Registry` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `NFR scorecard` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Traceability matrix seed` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Scope boundary record` | `WP-002` | `python3 scripts/progress.py show WP-002` |
| `Control Catalog` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `ExceptionPolicy` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `NonWaivableBlocker registry` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Control-test mapping` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Non-waivable additions for the epistemic layer` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Non-waivable additions for the reliability layer` | `WP-009` | `python3 scripts/progress.py show WP-009` |
| `Schema Registry v1` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Generated SDKs` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Compatibility CI` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Contract fixture catalog` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `Deprecation policy` | `WP-020` | `python3 scripts/progress.py show WP-020` |
| `CI pipelines` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Verification summary schema adapter` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Test ownership registry` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Flake policy` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `SPDX/REUSE and OSV admission checks` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Replay test suite` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Golden histories` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Fault-injection harness` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Workflow compatibility report` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Split-brain injection suite` | `WP-040` | `python3 scripts/progress.py show WP-040` |
| `Agentic attack suite` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Malicious fixture corpus` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Red-team report template` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Security regression schedule` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `ASB and WASP external regression` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Memory poisoning and evaluator exfiltration fixtures` | `WP-060` | `python3 scripts/progress.py show WP-060` |
| `Publication builder` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `RO-Crate profile` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Signed publication package` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Release checklist` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Supersession record` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Publication compiler` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Assertion and value binding checks` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Audit Ledger` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Hash-chain service` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Audit export/verify tooling` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Retention/access policy` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Integrity dashboard` | `WP-099` | `python3 scripts/progress.py show WP-099` |
| `Vertical slice dossier` | `WP-102` | `python3 scripts/progress.py show WP-102` |
| `R1/R3 project histories` | `WP-102` | `python3 scripts/progress.py show WP-102` |
| `Trace/audit/decision evidence` | `WP-102` | `python3 scripts/progress.py show WP-102` |
| `Integration findings` | `WP-102` | `python3 scripts/progress.py show WP-102` |
| `Literature vertical dossier` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Frozen LiteratureSetManifest` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Zotero SyncReceipts` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Coverage/screening report` | `WP-103` | `python3 scripts/progress.py show WP-103` |
| `Run/claim vertical dossier` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Run manifests/artifacts` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Claim/Evidence records` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Cost/trace/audit evidence` | `WP-104` | `python3 scripts/progress.py show WP-104` |
| `Review/repro vertical dossier` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `ReviewRecords/DisagreementCase` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `ReproductionReport` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `Gate histories` | `WP-105` | `python3 scripts/progress.py show WP-105` |
| `Decision/publish/monitor dossier` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `DecisionRecord` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `PublicationPackage` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `ImpactCase/Supersession` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `Audit export` | `WP-106` | `python3 scripts/progress.py show WP-106` |
| `Engineering vertical dossier` | `WP-107` | `python3 scripts/progress.py show WP-107` |
| `Frozen review packets` | `WP-107` | `python3 scripts/progress.py show WP-107` |
| `Validated findings` | `WP-107` | `python3 scripts/progress.py show WP-107` |
| `Signed OCI/release` | `WP-107` | `python3 scripts/progress.py show WP-107` |
| `Merge DecisionRecord` | `WP-107` | `python3 scripts/progress.py show WP-107` |
| `Engineering completion slice with attestation and eligibility` | `WP-107` | `python3 scripts/progress.py show WP-107` |
| `Impact vertical dossier` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `ImpactCase set` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Affected-object accuracy report` | `WP-108` | `python3 scripts/progress.py show WP-108` |
| `Supersession/re-evaluation records` | `WP-108` | `python3 scripts/progress.py show WP-108` |

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
| WP-109-T01 | Transfer the 40 scenarios into a machine-readable registry | Implementation owner | Commit / configuration / record reference |
| WP-109-T02 | Write the fixture, environment and data-seeding standard | Implementation owner | Commit / configuration / record reference |
| WP-109-T03 | Add the expected canonical, event, audit and policy assertions | Implementation owner | Commit / configuration / record reference |
| WP-109-T04 | Build the test runner, evidence capture and result signing | Implementation owner | Commit / configuration / record reference |
| WP-109-T05 | Write the witness protocol for manual human and DR steps | Implementation owner | Commit / configuration / record reference |
| WP-109-T06 | Add the retry, flakiness, skip/waiver and cleanup rules | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Acceptance Registry`
- `Scenario runner`
- `Fixture catalog`
- `Evidence capture/signing`
- `Result dashboard`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-109_acceptance_registry.tests.md`](WP-109_acceptance_registry.tests.md).

- Registry schema validation
- A known-pass and a known-fail scenario
- Enforcement of the same release-candidate digest
- A critical `SKIP` never counting as a pass
- Cleanup isolation between scenarios
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-109_acceptance_registry.acceptance.md`](WP-109_acceptance_registry.acceptance.md), together with what this package still cannot establish.

- [ ] Every scenario carries an owner and an immutable result.
- [ ] All results come from the same release candidate, policy and schema bundle.
- [ ] A critical scenario can never be skipped or waived.
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

Harness releases are verified with a canary fixture; results from a broken harness are `INVALIDATED` and every affected scenario is rerun.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
