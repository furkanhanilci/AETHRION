# WP-141 — Upstream Assimilation, Lineage and Characterisation Governance

## Package card

| Field | Value |
|---|---|
| Work package | `WP-141` |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Chief Architect |
| Independent verifier | Supply Chain Security Lead / Internal Audit |
| Hard dependencies | WP-010, WP-022, WP-024, WP-059 |
| Related gates | Program,Platform |
| Related controls | CTL-SUP-01, CTL-GOV-01 |
| Related acceptance scenarios | ACC-73, ACC-74 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-141_upstream_assimilation_governance.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-141_upstream_assimilation_governance.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Taking a mechanism from someone else's work becomes a version-pinned, licence-aware, behaviour-characterised engineering process rather than an undocumented copy.


## Analysis

### What this package actually decides

Whether "adapted from upstream" is a checkable statement or a sentence in a
README. Three obligations follow from taking a mechanism, and this package makes
each of them mechanical: name the exact commit, name what was deliberately *not*
taken, and name what the mechanism may never decide.

The third is the one specific to this programme. Every other supply-chain control
in the plan asks whether a component is what it claims to be. This one asks
whether it has quietly acquired authority — because the register's governing rule
is that an adopted mechanism supplies a signal and never a verdict.

### Why a pin is not optional

A mechanism adapted against a moving `main` cannot be re-read, diffed or
re-reviewed. When upstream fixes a bug in the code this repository copied, there
is no way to discover that without a pin, and no way to decide whether the fix
matters without a characterisation suite that says what the local copy is
supposed to do.

That is why `check_upstream_lineage.py` refuses a `DIRECT_ADAPT` entry that
reaches `ADAPTING` without a pin, a file list and a suite. The rule bites at the
moment code moves, not at the moment a decision is written down.

### Direct adaptation and reimplementation are different obligations

A permissive licence makes copying legal; it does not make copying correct. Where
the upstream architecture would arrive with the code — its storage model, its
orchestrator, its own authority semantics — the mechanism is specified and
rewritten instead, and the register records that no files were taken.

The checker enforces the distinction in both directions: an entry marked
`ADAPTIVE_REIMPLEMENT` that names source files is a defect, because if files were
copied the decision was direct adaptation and a licence obligation went
unrecorded.

### Why the checker tests itself

A lineage checker that has never been observed to fail reports "no findings" and
"no detector" in identical words. `--self-test` injects a deliberate defect per
rule and fails if any rule stays silent. This is the same control-injection
discipline `scripts/monitor_sources.py` already applies to retraction
monitoring, and `00_PROGRAM/06` requires it of any check whose clean result is
used as evidence.

### Baseline v1.3.0 — the register grows, and the licence rule gets sharper

The upstream register extends to the sources this baseline draws on, and gains
one rule stated explicitly because it is the one most often got wrong:

> **A paper's mechanism may be reimplemented freely. Its source code may not be
> copied without a compatible, file-level licence.**

Those are different acts with different obligations. Reading a paper and building
the mechanism natively creates no licence obligation at all. Copying a file does,
and a repository-level licence is not a per-file licence — which is the concrete
reason the domain-skill catalogue in the register is `DEFER` rather than
imported.

Also added: SPDX and REUSE as the machine-readable form, and characterisation
**drift** as a recurring obligation rather than a one-time admission check —
`ADR-019` and WP-159.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md) | `Signed ADR bundle` · `Rejected alternatives register` · `Reopen trigger register` · `Architecture baseline digest` |
| [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/WP-022_repository_topology.md) | `Repository skeleton` · `CODEOWNERS` · `Dependency rules` · `Developer guide` |
| [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md) | `CI pipelines` · `Verification summary schema adapter` · `Test ownership registry` · `Flake policy` |
| [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md) | `Admission policies` · `Trust root management` · `CVE/exception workflow` · `Revocation/impact runbook` |

### Full prerequisite closure

**45 of 160 packages (28%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-059` |

### What acceptance of this package releases

- **Directly unblocked:** 2 — `WP-142` · `WP-159`
- **Transitively reachable:** **16 of 160 packages (10%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-S — Scientific intelligence |
| Dependency depth | level **27** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Chief Architect |
| Independent verifier | Supply Chain Security Lead / Internal Audit |
| Gates touched | `Program` · `Platform` |
| Controls | `CTL-SUP-01` · `CTL-GOV-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-73 — Upstream Assimilation Drift](../12_ACCEPTANCE_SCENARIOS/ACC-73_upstream_assimilation_drift.md) | High | The drift checker reports the divergence and opens a review item. Nothing is auto-merged, and the characterisation suite must be rerun and reviewed before the pin moves. |
| [ACC-74 — Missing Upstream Lineage or Licence](../12_ACCEPTANCE_SCENARIOS/ACC-74_missing_upstream_lineage.md) | High | Admission fails at CI before merge. A second variant, correctly registered, passes — so the check discriminates rather than blocking all new files. |
| [ACC-120 — Missing Upstream Licence or Provenance](../12_ACCEPTANCE_SCENARIOS/ACC-120_missing_upstream_license_provenance.md) | High | The unregistered file fails admission before merge. The correctly registered one passes. OSV, Scorecard, SLSA provenance and signature verification run over the release, and a dependency with no available fix becomes an owned, expiring residual risk rather than silence. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md), [WP-022 — Repository Topology and Code Ownership](../03_FOUNDATION/WP-022_repository_topology.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md)
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
| `Signed ADR bundle` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Rejected alternatives register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Reopen trigger register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Architecture baseline digest` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Repository skeleton` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CODEOWNERS` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Dependency rules` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `Developer guide` | `WP-022` | `python3 scripts/progress.py show WP-022` |
| `CI pipelines` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Verification summary schema adapter` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Test ownership registry` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Flake policy` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `SPDX/REUSE and OSV admission checks` | `WP-024` | `python3 scripts/progress.py show WP-024` |
| `Admission policies` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Trust root management` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `CVE/exception workflow` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Revocation/impact runbook` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Adapted-source admission control` | `WP-059` | `python3 scripts/progress.py show WP-059` |

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
- **Chief Architect** carries the acceptance decision; **Supply Chain Security Lead / Internal Audit** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-141`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-141-T01 | Define the `AssimilationCandidate` and `UpstreamLineage` record shapes | Implementation owner | Commit / configuration / record reference |
| WP-141-T02 | Author `provenance/upstreams.json` covering every mechanism already decided | Implementation owner | Commit / configuration / record reference |
| WP-141-T03 | Implement `check_upstream_lineage.py` with a firing control per rule | Implementation owner | Commit / configuration / record reference |
| WP-141-T04 | Bind SPDX/REUSE metadata and reconcile `NOTICE` with the register | Implementation owner | Commit / configuration / record reference |
| WP-141-T05 | Define the direct-adapt versus reimplement decision rule and its evidence | Implementation owner | Commit / configuration / record reference |
| WP-141-T06 | Define the characterisation-test convention and where suites live | Implementation owner | Commit / configuration / record reference |
| WP-141-T07 | Implement upstream drift detection and the review path that moves a pin | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `AssimilationCandidate schema`
- `UpstreamLineage register`
- `check_upstream_lineage.py`
- `SPDX/REUSE policy`
- `Characterisation test convention`
- `Upstream drift review workflow`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-141_upstream_assimilation_governance.tests.md`](WP-141_upstream_assimilation_governance.tests.md).

- A firing control for every register rule, verified by `--self-test`
- A planted unregistered adapted file must fail admission
- A planted correctly registered file must pass, so the check discriminates
- A licence outside the permissive set must block direct adaptation
- Drift against a pinned commit must open a review item and must not auto-merge
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-141_upstream_assimilation_governance.acceptance.md`](WP-141_upstream_assimilation_governance.acceptance.md), together with what this package still cannot establish.

- [ ] Every adapted file in the repository is represented in the register or carries a recorded exception.
- [ ] The checker fails on a planted missing lineage and passes on a correct one.
- [ ] No source can reach `ACCEPTED` without a characterisation suite.
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

- A search or ranking score that becomes a claim confidence is a category error. It has to be refused by a schema, not remembered by a convention.
- A mechanism adapted without a characterisation test cannot be told apart from a mechanism that was misunderstood.
- Cognition that is permitted to recommend will be read as authority unless a field — not a paragraph — says it is not.

## Rollback / compensation

The register is versioned; reverting an assimilation decision restores the previous entry as a successor rather than deleting the history of the decision.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
