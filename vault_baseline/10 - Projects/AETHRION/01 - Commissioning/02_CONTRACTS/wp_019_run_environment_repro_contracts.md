---
title: "WP-019 — Run, Environment and Reproduction Schemas"
aliases:
  - "WP-019"
  - "WP-019 — Run, Environment and Reproduction Schemas"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Experiment and verification runs are fully manifested with dataset, code, environment, prompt, model snapshot, seed, metric and tolerance."
source: "planning/commissioning/02_CONTRACTS/WP-019_run_environment_repro_contracts.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/g4-g7
  - aethrion/state/not-started
---

# WP-019 — Run, Environment and Reproduction Schemas

## Package card

| Field | Value |
|---|---|
| Work package | `WP-019` |
| Workstream | `02_CONTRACTS` |
| Initial effort class | **M** — medium — needs a dedicated integration window; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Hard dependencies | WP-011, WP-014, WP-018 |
| Related gates | G4–G7 |
| Related controls | CTL-DAT-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-19, ACC-20 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_019_run_environment_repro_contracts.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_019_run_environment_repro_contracts.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Experiment and verification runs are fully manifested with dataset, code, environment, prompt, model snapshot, seed, metric and tolerance. A run whose manifest is incomplete can never support a confirmatory claim.


## Analysis
### What this package actually decides

What a run has to record before its result is allowed to mean anything. The
purpose states the consequence: *a run whose manifest is incomplete can never
support a confirmatory claim.* That is a hard gate, and it is the right one —
the alternative is a result whose provenance is reconstructed afterwards, which
is reconstruction, not reproduction.

### The four verification types are four different questions (T04)

Collapsing them is the most common error in this area, and the package explicitly
separates them:

| Type | Question | What is held constant |
|---|---|---|
| **Repeatability** | Same everything, same result? | Everything, including seed and machine |
| **Reproducibility** | Same artifacts, different machine, same result? | Manifest; not hardware |
| **Robustness** | Does the conclusion survive reasonable perturbation? | The conclusion, not the number |
| **Replication** | Does an independent attempt reach the same conclusion? | The question, not the method |

They have different tolerances and different failure meanings. A run that fails
repeatability is broken; one that fails robustness may be a real but fragile
finding; one that fails replication may be a real finding about a different
population. Reporting all four as "reproduction failed" destroys that information.

The architecture already splits G7 into **G7a** deterministic reproduction and
**G7b** distributional replication for exactly this reason.

### The structural constraint this package cannot engineer around

`00_PROGRAM/01` states it against success invariant 4, and it is the most
important sentence in this package's context:

> Current-generation hosted models do not carry date-suffixed snapshot
> identifiers, so a frozen manifest cannot pin one. Deterministic reproduction
> therefore requires local open-weight models with a weight-file hash. What can be
> pinned for hosted models is a **capability fingerprint** plus full input/output
> logging.

So `RunManifest` needs two model-pinning modes, and the manifest must **record
which mode was used**, because a run pinned by capability fingerprint cannot
support an R3 deterministic-reproduction claim. If the manifest does not record
the distinction, the tolerance policy will be applied to runs that structurally
cannot meet it.

### The tolerance policy is a pre-registration, not a post-hoc judgement (T05)

A tolerance decided after seeing the reproduction result is not a tolerance. It
belongs in the manifest before the run, alongside the analysis plan reference that
T02 makes mandatory — which is the same discipline `preregistration-discipline`
and `writing-analysis-plans` encode for the research side.

### `ReproductionReport` needs a root-cause schema, not a boolean

T05 asks for tolerance **and root cause**. A failed reproduction whose report says
`false` is an alarm with no next action. The root-cause categories — environment
drift, data drift, seed handling, model change, genuine non-determinism, defect in
the original — each imply a different response, and only one of them means the
original claim was wrong.

### Baseline v1.2.0 — reproduction is three environments, not one flag

The run and reproduction contracts need to express the three-environment
separation, because a single `reproduced: true` field cannot distinguish the
cases that matter:

- **`CandidateWorkspace`** — worktree, base commit, editable, read-only and
  forbidden paths, sandbox, network and credential profile.
- **`AlgorithmUnderstandingRecord`** — the target claim interpreted into steps,
  inputs, outputs and *declared ambiguities*, frozen before code is written. It
  is what separates "the paper was misread" from "the code was wrong".
- **`ReproductionPackage`** — entrypoint, source digest, environment spec,
  dependency lock, inputs, expected outputs, comparison spec. Accepted
  reproduction is this package running in a fresh environment **with no agent
  present** — ACC-66.
- **`ReproductionRun`** and **`ClaimConsistencyReport`** — with method, data and
  result consistency as separate fields, because exit code 0 is not a
  reproduction and a right number from the wrong method is not one either.

The four reproduction levels — exact, model-snapshot, distributional, claim
robustness — are recorded per run rather than collapsed into a boolean.

### Baseline v1.3.0 — new records, and the authority typing that keeps them honest

The contract surface gains the records this baseline's capabilities need, and
one field that matters more than any of them.

**New canonical records:** `AgentCohortRecord`, `CognitiveDiversityProfile`,
`CommunicationEdgePolicy`, `BlackboardEntry`, `TypedAgentMessage`,
`CommunicationUtilityRecord`, `ContextProjectionRecord`,
`MemoryInterventionRecord`, `ResearchBudgetContract`, `TokenLedgerEntry`,
`SpecificationConformanceRecord`, `HumanPreliminaryAssessment`, `DecisionDelta`,
`ModelExecutionFingerprint`, `BenchmarkRunPolicy`, `ContaminationFinding`,
`UpstreamAssimilationRecord`.

**Explicit authority typing.** Every record carries what it may never become. The
three conversions this baseline forbids are all of the same kind, and each has
already been attempted somewhere in the field:

| Forbidden conversion | Why it is tempting |
|---|---|
| A blackboard entry into evidence | It is where the interesting sentences appear |
| A communication or search utility score into a claim confidence | It is a number, and it correlates with something |
| An event payload into gate authority | It is the fastest path and it usually works |

The rule that makes them checkable rather than remembered: **events, blackboard
entries and derived read models cannot masquerade as canonical scientific
state**, and the schema is where that is enforced.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md) | `Identifier Standard` · `Correlation envelope` · `ID library contract` · `Merge/tombstone rules` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |

### Full prerequisite closure

**16 of 160 packages (10%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 9 | `WP-012` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-017` |
| 12 | `WP-018` |

### What acceptance of this package releases

- **Directly unblocked:** 11 — `WP-020` · `WP-035` · `WP-036` · `WP-043` · `WP-081` · `WP-082` · `WP-084` · `WP-085` · `WP-144` · `WP-157` · `WP-158`
- **Transitively reachable:** **140 of 160 packages (88%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W1 — Contract spine |
| Dependency depth | level **13** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Experiment Platform Lead |
| Independent verifier | Reproducibility Engineer |
| Gates touched | `G4–G7` |
| Controls | `CTL-DAT-01` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/acc_19_clean_room_pass.md) | High | The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass. |
| [ACC-20 — Clean-Room Reproduction Failure](../12_ACCEPTANCE_SCENARIOS/acc_20_clean_room_fail.md) | Critical | G7 becomes FAIL/REVISE and the claim becomes `CHALLENGED`; an environment/data/code/stochastic/method root-cause classification is made and a controlled G4/G5 return is opened. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-011 — Identity and End-to-End Correlation Standard](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md)
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
| `Identifier Standard` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Correlation envelope` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ID library contract` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `Merge/tombstone rules` | `WP-011` | `python3 scripts/progress.py show WP-011` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Evidence contract bundle` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Claim state machine` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Review/disagreement schemas` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Decision schema fixtures` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `PublicationAssertion` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `EvidenceTag` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `FindingRecord` | `WP-018` | `python3 scripts/progress.py show WP-018` |
| `Authority typing on every scientific record` | `WP-018` | `python3 scripts/progress.py show WP-018` |

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
- **Experiment Platform Lead** carries the acceptance decision; **Reproducibility Engineer** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-019`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-019-T01 | Write the `RunManifest` input, output and lineage fields | Implementation owner | Commit / configuration / record reference |
| WP-019-T02 | Make the protocol, baseline and analysis-plan references mandatory | Implementation owner | Commit / configuration / record reference |
| WP-019-T03 | Add the `EnvironmentManifest` hardware, driver, image and SBOM fields | Implementation owner | Commit / configuration / record reference |
| WP-019-T04 | Separate repeatability, reproducibility, robustness and replication as distinct types | Implementation owner | Commit / configuration / record reference |
| WP-019-T05 | Write the `ReproductionReport` tolerance and root-cause schema | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Run schema bundle`
- `EnvironmentManifest`
- `ReproductionReport`
- `Tolerance policy examples`
- `CandidateWorkspace`
- `ReproductionPackage`
- `ClaimConsistencyReport`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-019_run_environment_repro_contracts.tests.md`](wp_019_run_environment_repro_contracts.tests.md).

- Negative tests for a missing seed, model or image hash
- A determinism fixture running the same manifest twice
- A test detecting a mislabelled reproduction type
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-019_run_environment_repro_contracts.acceptance.md`](wp_019_run_environment_repro_contracts.acceptance.md), together with what this package still cannot establish.

- [ ] A run records the version of every frozen input.
- [ ] A reproduction result carries pass/fail **and** the tolerance rationale.
- [ ] Replication is never substituted for reproduction, nor the reverse.
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

- A contract that has no consumer has never been tested, only reviewed.
- Optional fields become mandatory in practice; mark real optionality explicitly.
- Two surfaces holding the same field is a canonical-ownership defect, not a sync problem.

## Rollback / compensation

A run with an incomplete manifest stays `INVALID` or `EXPLORATORY`; it is not promoted to a publication or a critical claim.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
