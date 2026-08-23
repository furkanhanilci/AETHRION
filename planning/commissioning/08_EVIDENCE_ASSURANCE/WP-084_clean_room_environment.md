# WP-084 — Clean-Room Reproduction Environment

## Package card

| Field | Value |
|---|---|
| Work package | `WP-084` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Reproducibility Lead |
| Independent verifier | Security / Independent SRE |
| Hard dependencies | WP-007, WP-014, WP-019, WP-026, WP-027, WP-052, WP-053, WP-054, WP-055, WP-059, WP-082 |
| Related gates | G7 |
| Related controls | CTL-GOV-02, CTL-EPI-03, CTL-SEC-04 |
| Related acceptance scenarios | ACC-19, ACC-20 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-084_clean_room_environment.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-084_clean_room_environment.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

The reproducer runs in a clean environment built from the frozen manifest, isolated from the producer's workspace, credentials, caches and intermediate traces.


## Analysis
### What this package actually decides

That the reproducer starts from nothing. `00_PROGRAM/01` invariant 3 and the G7
blocker together require it: a clean-room run that succeeds because a cached
artifact happened to be present has not reproduced anything.

### Blocking the producer's cache is harder than blocking their workspace (T03)

A workspace is a directory. A cache is a package index, a model download, a
container layer, a resolved dependency lockfile, a browser profile — and each of
them can carry the exact bytes that make an unreproducible run appear
reproducible.

The clean room needs its own everything, and the test that matters is the one
where a **deliberately missing input** causes a failure rather than a silent
success.

### Offline by default, with a declared exception path (T05)

A reproduction that fetches from the network is reproducing against the network's
current state. Offline is the honest default; where a fetch is genuinely required,
it goes through a pinned, verified path and the fetch is part of the manifest.

### Hardware tolerance is a real and often-ignored variable (T04)

Floating-point results differ across GPU architectures. A tolerance that assumes
identical hardware will report a spurious failure on different hardware, and one
that is loose enough to absorb hardware differences may absorb a real one. Both
have to be declared, and the environment captured, so the reproduction report can
say which applies.

### Forensic retention before destruction (T06)

Same rule as WP-054: an environment destroyed on failure leaves nothing to
diagnose. The snapshot is taken when the reproduction fails, before teardown.

### Baseline v1.2.0 — three zones, and the isolation that has to be per candidate

The clean room becomes three zones with three identities: the **producer**
workspace, the **evaluator** zone holding the official evaluator and hidden
material, and the **grader** environment where outputs are compared. No shared
mutable state between any pair.

Isolation is **per candidate**, not per campaign. Each candidate gets its own
worktree and commit lineage under its own `MutationPolicy`, so a diff is
attributable and a parallel population cannot contaminate itself.

A boundary breach **invalidates the run** rather than lowering its score. A
candidate that reached the evaluator zone produced a result of unknown
provenance, and scoring it low would record it as a bad result rather than as no
result. ACC-54, ACC-55; ADR-007.

### Baseline v1.3.0 — the assurance layer stops using one word for two things

Three changes, and the first is a vocabulary correction with real consequences.

**"Mechanical verifier" is retired as a broad term.** It becomes V0 deterministic
· V1 computational · V2 qualified semantic · V3 human (`ADR-008`), and the class
is assigned by the verifier service from the procedure that actually ran — never
by the caller. The reason is that the gate rule *a mechanical check cannot be
overridden by a model* is correct for V0 and V1 and absurd at V2, where it says a
model's judgement cannot be overridden by a model.

**Assurance becomes routed** (`ADR-015`): by consequence and uncertainty rather
than uniformly, with a cascade to a stronger independent verifier or to a human,
and with `ABSTAIN` as a valid verdict that escalates. A route cannot be lowered
because the queue is long or the budget is tight.

**Three hard bindings** into the evidence and publication path:

- **Specification conformance** — the frozen method and the running code are
  compared, and an unapproved `SCIENTIFIC_MAJOR` deviation cannot carry a
  confirmatory package forward (`ADR-018`, ACC-104).
- **Model execution fingerprint** — every invocation contributing to a result
  records what actually executed, retry and fallback history included, and a
  hosted black-box model does not yield an `EXACT` reproduction claim
  (ACC-115, ACC-116).
- **Publication compiler** — no prose without a claim, no number without a
  `VerifiedValue`, and a complete evidence chain checked link by link
  (ACC-105, ACC-106).

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

11, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md) | `IndependenceProfile rubric` · `Eligibility matrix` · `Conflict-of-interest declaration` · `Violation response` |
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md) | `Run schema bundle` · `EnvironmentManifest` · `ReproductionReport` · `Tolerance policy examples` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md) | `Kubernetes clusters` · `Node pool catalog` · `Namespace/security baseline` · `Upgrade/restore runbook` |
| [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md) | `Kueue configuration` · `Quota/priority policy` · `Budget admission adapter` · `Queue dashboard` |
| [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md) | `Sandbox profiles` · `Execution Cell controller` · `SandboxAttestation` · `Capture/destroy workflow` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |
| [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md) | `Admission policies` · `Trust root management` · `CVE/exception workflow` · `Revocation/impact runbook` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |

### Full prerequisite closure

**53 of 160 packages (33%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 21 | `WP-033` · `WP-045` |
| 22 | `WP-034` · `WP-046` |
| 23 | `WP-035` · `WP-049` |
| 24 | `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-059` · `WP-061` |
| 27 | `WP-075` |
| 28 | `WP-081` |
| 29 | `WP-082` |

### What acceptance of this package releases

- **Directly unblocked:** 3 — `WP-085` · `WP-105` · `WP-157`
- **Transitively reachable:** **32 of 160 packages (20%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **30** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Reproducibility Lead |
| Independent verifier | Security / Independent SRE |
| Gates touched | `G7` |
| Controls | `CTL-GOV-02` · `CTL-EPI-03` · `CTL-SEC-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-19 — Clean-Room Reproduction Pass](../12_ACCEPTANCE_SCENARIOS/ACC-19_clean_room_pass.md) | High | The result falls within tolerance; a `ReproductionReport`, certificate and independence attestation are produced, and G7 can pass. |
| [ACC-20 — Clean-Room Reproduction Failure](../12_ACCEPTANCE_SCENARIOS/ACC-20_clean_room_fail.md) | Critical | G7 becomes FAIL/REVISE and the claim becomes `CHALLENGED`; an environment/data/code/stochastic/method root-cause classification is made and a controlled G4/G5 return is opened. |
| [ACC-54 — Producer Attempts Evaluator Mutation](../12_ACCEPTANCE_SCENARIOS/ACC-54_evaluator_mutation_attempt.md) | Critical | Every write is denied at the policy and sandbox boundary and audited. If any write nonetheless lands, the evaluator digest mismatch invalidates the run and the scenario FAILs as a critical security defect. |
| [ACC-55 — Hidden Evaluation Data Access Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-55_hidden_evaluation_data_access.md) | Critical | Access is denied under the supported threat model, no hidden content appears in any candidate artifact, log or trace, and each attempt raises a security finding. |
| [ACC-65 — Reproduction in the Producer Environment](../12_ACCEPTANCE_SCENARIOS/ACC-65_reproduction_in_producer_environment.md) | Critical | The `IndependenceProfile` detects the shared environment lineage and refuses to award reproduced status. A run may still be executed and recorded, but it is classified as repeatability, not reproducibility. |
| [ACC-113 — Producer to Evaluator Leakage](../12_ACCEPTANCE_SCENARIOS/ACC-113_producer_evaluator_leakage.md) | Critical | Every path is closed. None of them looks like a boundary violation in a log, which is why each is tested explicitly rather than inferred from the zone configuration. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-007 — IndependenceProfile and Separation-of-Duties Policy](../01_GOVERNANCE/WP-007_independence_profile.md), [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-019 — Run, Environment and Reproduction Schemas](../02_CONTRACTS/WP-019_run_environment_repro_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-052 — Kubernetes Cluster and Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Quota and Priority Policy](../06_EXECUTION_SECURITY/WP-053_kueue_quota.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-059 — Supply-Chain Admission, Sigstore and SLSA Policy](../06_EXECUTION_SECURITY/WP-059_supply_chain_admission.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
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
| `IndependenceProfile rubric` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Eligibility matrix` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Conflict-of-interest declaration` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Violation response` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Evaluator and memory-context independence constraints` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `Cohort independence dimensions` | `WP-007` | `python3 scripts/progress.py show WP-007` |
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Run schema bundle` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `EnvironmentManifest` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Tolerance policy examples` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `CandidateWorkspace` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ReproductionPackage` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `ClaimConsistencyReport` | `WP-019` | `python3 scripts/progress.py show WP-019` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `OCI registry` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Build/promotion pipeline` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `SBOM/provenance artifacts` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Signature policy seed` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Kubernetes clusters` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Node pool catalog` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Namespace/security baseline` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Upgrade/restore runbook` | `WP-052` | `python3 scripts/progress.py show WP-052` |
| `Kueue configuration` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Quota/priority policy` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Budget admission adapter` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Queue dashboard` | `WP-053` | `python3 scripts/progress.py show WP-053` |
| `Sandbox profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Execution Cell controller` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `SandboxAttestation` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Capture/destroy workflow` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Red-team tests` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Four-zone isolation profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Admission policies` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Trust root management` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `CVE/exception workflow` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Revocation/impact runbook` | `WP-059` | `python3 scripts/progress.py show WP-059` |
| `Adapted-source admission control` | `WP-059` | `python3 scripts/progress.py show WP-059` |
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
- **Reproducibility Lead** carries the acceptance decision; **Security / Independent SRE** must verify independently of whoever implements.
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
| WP-084-T01 | Establish the dedicated reproduction queue, nodes, namespace and identity | Implementation owner | Commit / configuration / record reference |
| WP-084-T02 | Write the frozen package resolver and the image/data/code fetch verification | Implementation owner | Commit / configuration / record reference |
| WP-084-T03 | Block access to the producer's cache, workspace and credentials | Implementation owner | Commit / configuration / record reference |
| WP-084-T04 | Apply seed and hardware tolerance and capture the environment | Implementation owner | Commit / configuration / record reference |
| WP-084-T05 | Bind the network/offline policy and output capture | Implementation owner | Commit / configuration / record reference |
| WP-084-T06 | Write environment destruction and forensic retention | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Clean-room platform`
- `Reproducer profile`
- `Environment resolver`
- `Isolation attestation`
- `Repro runbook`
- `Three-zone clean room profiles`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-084_clean_room_environment.tests.md`](WP-084_clean_room_environment.tests.md).

- Denial of access to producer credentials and caches
- Building the environment from the manifest alone
- Tolerance across different hardware
- Hash failure on a tampered artifact
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-084_clean_room_environment.acceptance.md`](WP-084_clean_room_environment.acceptance.md), together with what this package still cannot establish.

- [ ] The reproducer never sees the producer's intermediate output.
- [ ] Every input is resolved from a frozen digest.
- [ ] The clean-room attestation is attached to the report.
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

- Independence asserted in a record but not enforced by the router is decorative.
- A review that sees the producer's conclusion first is anchored, not independent.
- Reproduction that reuses the producer's environment reproduces the environment, not the result.

## Rollback / compensation

A suspect reproduction cell is contained; the run is re-planned in a fresh clean cell with independent credentials.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
