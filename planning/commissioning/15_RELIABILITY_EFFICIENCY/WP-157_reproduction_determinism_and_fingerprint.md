# WP-157 — Reproduction Determinism and Model Execution Fingerprint

## Package card

| Field | Value |
|---|---|
| Work package | `WP-157` |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Reproducibility Lead |
| Independent verifier | Assurance Lead / Independent Grader |
| Hard dependencies | WP-019, WP-084, WP-085 |
| Related gates | G5,G7 |
| Related controls | CTL-DAT-01, CTL-EPI-03 |
| Related acceptance scenarios | ACC-113, ACC-114, ACC-115, ACC-116 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-157_reproduction_determinism_and_fingerprint.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-157_reproduction_determinism_and_fingerprint.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every model invocation that contributes to a result records what was actually executed, and a hosted black-box model yields a distributional reproduction claim rather than an exact one.


## Analysis

### What this package actually decides

What "reproducible" can honestly mean when part of the pipeline is a hosted model
nobody controls.

Reported work shows accuracy differences of up to fifteen percentage points
between equivalent runs against hosted APIs under nominally deterministic
settings. A reproduction claim that ignores that is measuring something other
than what it says.

### The fingerprint is what makes the claim inspectable

`ModelExecutionFingerprint` records provider, model id, snapshot or version if
exposed, API version, request parameters, seed, temperature, system prompt
digest, tool schema digest, context bundle digest, timestamp, region or endpoint
if known, retry and fallback history, and the raw response digest.

The retry and fallback history is the field most often missing and most often
decisive: a result produced after a silent failover to a different model is a
result from a different model — ACC-115.

### Five levels, because one boolean is a lie

| Level | What it claims |
|---|---|
| `EXACT` | Same weights, same environment, same outputs |
| `SNAPSHOT` | A provider-pinned snapshot, reproducible while it exists |
| `BEHAVIORAL` | Same decisions, not identical bytes |
| `DISTRIBUTIONAL` | Repeated runs, consistent within a stated interval |
| `CLAIM_ROBUSTNESS` | A different qualified implementation reaches the same conclusion |

**A hosted black-box model does not yield `EXACT`**, and asserting it is not a
conservative rounding — it is a false statement about what was verified. Where a
protocol needs a distributional claim, the number of runs and the interval are
declared in advance rather than chosen once the spread is known — ACC-116.

### Three zones, restated because leakage is subtle

Producer, fresh reproducer and independent grader stay separate in secrets, cache
and workspace. A `ReproductionPackage` must execute with **no agent context**.

The leak this package adds a test for is the quiet one: a shared cache, an
inherited credential, a warm container layer. ACC-113 and ACC-114 attack exactly
those, because none of them looks like a boundary violation in a log.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.md) | `Clean-room platform` · `Reproducer profile` · `Environment resolver` · `Isolation attestation` |
| [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md) | `Verification pipeline` · `Type-specific protocols` · `Robustness matrix` · `Reproduction certificates` |

### Full prerequisite closure

**69 of 160 packages (43%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-082` |
| 30 | `WP-067` · `WP-083` · `WP-084` |
| 31 | `WP-068` |
| 32 | `WP-076` |
| 33 | `WP-077` |
| 34 | `WP-085` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-R — Reliability and efficiency |
| Dependency depth | level **35** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Reproducibility Lead |
| Independent verifier | Assurance Lead / Independent Grader |
| Gates touched | `G5` · `G7` |
| Controls | `CTL-DAT-01` · `CTL-EPI-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-113 — Producer to Evaluator Leakage](../12_ACCEPTANCE_SCENARIOS/ACC-113_producer_evaluator_leakage.md) | Critical | Every path is closed. None of them looks like a boundary violation in a log, which is why each is tested explicitly rather than inferred from the zone configuration. |
| [ACC-114 — Reproduction Environment Lineage](../12_ACCEPTANCE_SCENARIOS/ACC-114_reproduction_in_producer_environment_hardened.md) | Critical | The first four are refused reproduced status. Only the independent environment yields reproducibility, and the classification is decided by environment digest lineage rather than by declaration. |
| [ACC-115 — Missing Model Execution Fingerprint](../12_ACCEPTANCE_SCENARIOS/ACC-115_missing_model_execution_fingerprint.md) | Critical | An invocation without a complete fingerprint fails the run. The failover appears in the fingerprint's retry and fallback history and invalidates any `EXACT` claim. |
| [ACC-116 — Distributional Reproduction for a Hosted Model](../12_ACCEPTANCE_SCENARIOS/ACC-116_distributional_hosted_model_reproduction.md) | High | `EXACT` is refused for hosted black-box execution. The distributional claim uses the pre-declared run count and interval, and choosing them after seeing the spread is refused. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-084 — Clean-Room Reproduction Environment](../08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md)
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
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `CandidateWorkspace` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionPackage` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ClaimConsistencyReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Clean-room platform` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Reproducer profile` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Environment resolver` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Isolation attestation` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Repro runbook` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Three-zone clean room profiles` | `WP-084` | `python3 scripts/progress.py show WP-084` |
| `Verification pipeline` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Type-specific protocols` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Robustness matrix` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Reproduction certificates` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Failure taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `AlgorithmUnderstandingRecord` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ReproductionPackage` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ClaimConsistencyReport` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Five-level reproduction taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |

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
- **Reproducibility Lead** carries the acceptance decision; **Assurance Lead / Independent Grader** must verify independently of whoever implements.
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

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-050` — Hosted-model nondeterminism under deterministic settings | `PATTERN` | the idea only — no code and nothing called at runtime | everything — the implementation here is this repository's own | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-050` | A reproduction level describes what the substrate can support. It is not a statement about whether the result is correct. | Nothing to take as code — the finding is the contribution. |

### Where a plain row would mislead

- **`ASM-050`** — Reports up to a 15-point maximum-minimum accuracy difference across equivalent runs against hosted APIs under presumed deterministic settings. The consequence is the five-level reproduction taxonomy: **seed and temperature are not a reproducibility proof**, a hosted black box cannot yield EXACT, and a distributional claim needs its run count and interval declared in advance — ACC-116.

### Unresolved before implementation

**None.** Every obligation the modes above create has been met.

**Acquisition readiness — resolved.** All 1 registered sources have met the obligations their modes create.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-157-T01 | Define `ModelExecutionFingerprint` and capture it on every contributing invocation | Implementation owner | Commit / configuration / record reference |
| WP-157-T02 | Record retry and fallback history as part of the fingerprint | Implementation owner | Commit / configuration / record reference |
| WP-157-T03 | Define the five reproduction levels and bind them to protocol declaration | Implementation owner | Commit / configuration / record reference |
| WP-157-T04 | Refuse EXACT for hosted black-box execution | Implementation owner | Commit / configuration / record reference |
| WP-157-T05 | Implement distributional reproduction with pre-declared run count and interval | Implementation owner | Commit / configuration / record reference |
| WP-157-T06 | Harden the three-zone separation against cache, credential and layer inheritance | Implementation owner | Commit / configuration / record reference |
| WP-157-T07 | Bind fingerprints into the reproduction package and the claim consistency report | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `ModelExecutionFingerprint`
- `Five-level reproduction taxonomy`
- `Three-zone leakage suite`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-157_reproduction_determinism_and_fingerprint.tests.md`](WP-157_reproduction_determinism_and_fingerprint.tests.md).

- A contributing model invocation without a fingerprint must fail the run
- A silent provider failover must appear in the fingerprint and invalidate an EXACT claim
- A hosted black-box execution must not be classifiable as EXACT
- A distributional claim must use a pre-declared run count and interval
- Shared cache, inherited credential and warm-layer paths between zones must each be blocked
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks


## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-157_reproduction_determinism_and_fingerprint.acceptance.md`](WP-157_reproduction_determinism_and_fingerprint.acceptance.md), together with what this package still cannot establish.

- [ ] Every model invocation contributing to a published result carries a complete fingerprint.
- [ ] The reproduction level asserted is the one the execution substrate can actually support.
- [ ] Producer, reproducer and grader share no cache, credential or workspace lineage.
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

Fingerprints are immutable and attached to their run: a re-execution produces a new run with a new fingerprint, and a claim's reproduction level is re-derived rather than edited.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
