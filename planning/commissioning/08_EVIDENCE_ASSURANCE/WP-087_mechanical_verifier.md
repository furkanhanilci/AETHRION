# WP-087 — Mechanical Verification Engine

## Package card

| Field | Value |
|---|---|
| Work package | `WP-087` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Verification Engineering Lead |
| Independent verifier | Independent Test Engineer |
| Hard dependencies | WP-020, WP-024, WP-026, WP-027, WP-075, WP-076, WP-080, WP-081, WP-082, WP-086 |
| Related gates | G2–G9 |
| Related controls | CTL-EPI-01, CTL-SUP-01 |
| Related acceptance scenarios | ACC-08, ACC-17, ACC-23, ACC-30 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-087_mechanical_verifier.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-087_mechanical_verifier.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Schema, hash, test, policy, manifest, signature, locator, lineage and report-to-claim links are verified by deterministic records, independent of any LLM assertion.


## Analysis
### What this package actually decides

What can be verified **without asking a model anything**. The purpose sentence
carries the constraint: *independent of any LLM assertion.*

This is the mechanical half of `agents produce · machines verify · humans decide`,
and `docs/architecture/AETHRION_ROLE_MODEL_ASSIGNMENT.md` fixes its precedence:
**a mechanical check, where one exists, runs first and cannot be overridden by a
model.**

### Determinism is the property, not speed (T01, T02)

A validator that consults a model, a network service or the current time is not a
validator — it is a reviewer with a fast interface. The plugin contract has to make
determinism structural: same inputs, same verdict, replayable.

`00_PROGRAM/06`'s ordering follows from it: cheap deterministic layers first, so a
reviewer's attention is never spent on something a hash comparison settles.

### This repository already runs a version of this

The twelve-check bundle, `scripts/write_status.py`, the plan seal, the figure
containment check, the evidence manifest verifier. `AGENTS.md` §11 also states
their limit precisely: *all of them are internal consistency, and every one would
still hold for a corpus describing a system that does not work.*

That limit belongs in this package's own documentation, because a `VerificationRecord`
full of green mechanical checks is exactly the artifact most likely to be mistaken
for a quality result.

### The target-revision check is the one that catches mixed evidence (T04)

`00_PROGRAM/05` requires all criteria to pass **on the same target revision**, and
`00_PROGRAM/06` lists *test outputs from different revisions mixed together* as
evidence that is not accepted. A validator that confirms every result names one
revision is what enforces it.

### Structural validation of findings (T04)

A finding with no location, no severity or no reproduction step cannot be
dispositioned. Checking finding *shape* mechanically is cheap and it stops
malformed findings entering the arbitration path.

### Validator calibration and regression (T06)

A validator can drift into passing everything. Each one needs a **known-bad
fixture** it must fail — the repository's own rule, applied to the checkers
themselves.

### Baseline v1.2.0 — four classes, and what the word 'mechanical' now means

This package's title and scope change from *mechanical verification* to a
verification engine that **routes by class and records which class answered**:
V0 deterministic · V1 computational or statistical · V2 model-mediated semantic ·
V3 human judgement.

The reason is not vocabulary hygiene. The gate rule — *a mechanical check runs
first and cannot be overridden by a model* — is correct for V0 and V1 and absurd
when applied to V2, where it says a model's judgement cannot be overridden by a
model. Splitting the word repairs the rule: V0 and V1 failures are absolute; a V2
result is a finding with a measured error rate, routed to review.

**The class is assigned by the verifier service from the procedure that ran**,
never by the caller. A model-mediated result submitted as V0 is refused and
audited — ACC-62. A V2 verdict without a current `VerifierQualificationRecord`
for that task type at that threshold cannot satisfy a required verification; the
gate reports `INCONCLUSIVE` rather than passing or failing on an unmeasured
judgement — ACC-61.

Every critical verifier carries a known-positive that must fail and a
known-negative that must pass, and **the suite fails if a planted control stays
silent**. A detector reports "no findings" and "no detector" in identical words.

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

10, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md) | `Schema Registry v1` · `Generated SDKs` · `Compatibility CI` · `Contract fixture catalog` |
| [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md) | `CI pipelines` · `Verification summary schema adapter` · `Test ownership registry` · `Flake policy` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md) | `OCI registry` · `Build/promotion pipeline` · `SBOM/provenance artifacts` · `Signature policy seed` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md) | `Anchor resolver` · `Format adapters` · `Re-anchor queue` · `Anchor regression corpus` |
| [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md) | `Citation audit service` · `Audit rubric` · `Mechanical locator checker` · `Audit report/scorecard` |
| [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md) | `Method Registry` · `Protocol validators` · `Amendment workflow` · `Post-hoc change detector` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md) | `Review Package Builder` · `Blind/redaction rules` · `Package manifests` · `Leak detection tests` |

### Full prerequisite closure

**74 of 160 packages (46%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |

### What acceptance of this package releases

- **Directly unblocked:** 9 — `WP-088` · `WP-089` · `WP-090` · `WP-095` · `WP-105` · `WP-107` · `WP-113` · `WP-126` · `WP-155`
- **Transitively reachable:** **37 of 160 packages (23%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **37** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Verification Engineering Lead |
| Independent verifier | Independent Test Engineer |
| Gates touched | `G2–G9` |
| Controls | `CTL-EPI-01` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/ACC-08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-17 — Unsigned or Mutable Image](../12_ACCEPTANCE_SCENARIOS/ACC-17_unsigned_image.md) | Critical | The pod is not created; the signature, provenance and digest policy denies it and produces audit and alert records. A signed-digest counter-example passes. |
| [ACC-23 — Artifact Overwrite Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-23_artifact_overwrite.md) | Critical | The overwrite is rejected; the new bytes can only be written as a new content address and version, and existing references are unchanged. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-53 — Unverified Numeric Result](../12_ACCEPTANCE_SCENARIOS/ACC-53_unverified_numeric_result.md) | Critical | The build fails regardless of the quality of the surrounding prose; the report lists the value refs that were permitted and the one that was not. A declared rounding or display transform of a registered value passes. |
| [ACC-60 — Failed Smoke Candidate Promotion Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-60_failed_smoke_promotion.md) | Critical | Both promotions are refused. Under a CONFIRMATORY study mode the rule is non-waivable; where an exceptional path exists at all it requires an explicit authorised exception with an owner and an expiry, and it is recorded as one. |
| [ACC-61 — Unqualified Semantic Verifier](../12_ACCEPTANCE_SCENARIOS/ACC-61_unqualified_semantic_verifier.md) | Critical | The verdict is recorded as advisory and cannot satisfy the requirement; the gate blocks with `INCONCLUSIVE` rather than passing or failing the claim on an unqualified judgement. |
| [ACC-62 — Semantic Verifier Recorded as Mechanical](../12_ACCEPTANCE_SCENARIOS/ACC-62_verifier_class_misdeclaration.md) | High | It is refused. A verification class is set by the authorised verifier service from the procedure that actually ran, not by the caller, and the attempt raises an audit finding. |
| [ACC-67 — Claim–Code–Result Consistency Failure](../12_ACCEPTANCE_SCENARIOS/ACC-67_claim_code_result_consistency.md) | Critical | Both are reported `INCONSISTENT` and G7 does not pass. Exit code 0 is not a reproduction, and a matching number reached by the wrong method is not one either. |
| [ACC-76 — Unsupported Publication Sentence](../12_ACCEPTANCE_SCENARIOS/ACC-76_unsupported_publication_sentence.md) | Critical | The reference-existence check passes at V0, and the entailment and scope checks fail at V2. Publication is blocked. A control sentence whose citation genuinely supports it passes both. |
| [ACC-77 — VerifiedValue Rebinding Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-77_verified_value_rebinding.md) | Critical | Both are refused. The binding is immutable and digest-checked; a changed evaluation produces a new value, and a tampered raw artifact fails its digest. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-020 — Schema Registry, Compatibility and Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-024 — CI Foundation and Deterministic Quality Gates](../03_FOUNDATION/WP-024_ci_quality_gates.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-027 — Git, OCI Registry and Build Provenance Foundation](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-086 — Frozen and Blind Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md)
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
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `OCI registry` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Build/promotion pipeline` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `SBOM/provenance artifacts` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Signature policy seed` | `WP-027` | `python3 scripts/progress.py show WP-027` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Anchor resolver` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Format adapters` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Re-anchor queue` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Anchor regression corpus` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Citation audit service` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit rubric` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Mechanical locator checker` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit report/scorecard` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Decomposed citation audit with per-question verification class` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Method Registry` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Protocol validators` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Amendment workflow` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `Post-hoc change detector` | `WP-081` | `python3 scripts/progress.py show WP-081` |
| `SpecificationConformanceRecord binding` | `WP-081` | `python3 scripts/progress.py show WP-081` |
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
| `Review Package Builder` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Blind/redaction rules` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Package manifests` | `WP-086` | `python3 scripts/progress.py show WP-086` |
| `Leak detection tests` | `WP-086` | `python3 scripts/progress.py show WP-086` |

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
- **Verification Engineering Lead** carries the acceptance decision; **Independent Test Engineer** must verify independently of whoever implements.
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
| `ASM-001` — ScientistOne / Science One Framework — Chain-of-Evidence | `ADAPTIVE_REIMPLEMENT` | `MS-COE-001` · `MS-COE-002` · `MS-COE-003` · `MS-COE-004` · `MS-COE-005` · `MS-COE-006` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-010` — Curie — intra-agent and inter-agent rigor | `ADAPTIVE_REIMPLEMENT` | `MS-RIG-001` · `MS-RIG-002` | the local module and contract surface this becomes — **named at refinement** | **1** |
| `ASM-027` — REPRO-Bench — claim / package / recomputed-output consistency | `BENCHMARK` | a measurement of this system — nothing enters it | the contract this is held behind | none |
| `CMP-032` — statcheck · grim · pysprite | `DEPENDENCY` | The statistical consistency tests themselves. | Which forensic test runs at which gate, and what a failure means for the claim. | **2** |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-001` | A CoE Audit result is a VerificationResult, never a GateRecord verdict. The audit reports; the gate policy decides. | The producer architecture, the provider assumptions, and any notion that the audit score is itself a decision. |
| `ASM-010` | A RigorFinding blocks a transition when policy maps it to a control. It does not by itself reject a scientific claim. | The agent hierarchy and orchestrator, which would duplicate the authority Temporal already holds. |
| `ASM-027` | Measures G7; never gates it. | Any runtime dependency. |
| `CMP-032` | A forensic finding is a `VerificationResult` that opens an investigation. It is never a finding of misconduct and never a gate verdict — `investigating-integrity-concerns` governs what happens next. | A test failure as an accusation, or a test pass as evidence of integrity. |

### Where a plain row would mislead

- **`ASM-001`** — Two public versions of this work report different evaluation corpus sizes. Any number quoted from it must carry the version it came from — the same rule this architecture applies to SourceRepresentation.
- **`ASM-010`** — The rule worth taking is that agent B must not infer A succeeded from A's confident prose. Every rigor check that can be deterministic must be.
- **`ASM-027`** — The lesson encoded as ACC-67: exit code zero is not a reproduction.
- **`CMP-032`** — Validated implementations are used because the edge cases — scale granularity, rounding, integer constraints — are exactly where a fresh implementation goes wrong.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-001` — ScientistOne / Science One Framework — Chain-of-Evidence** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-010` — Curie — intra-agent and inter-agent rigor** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`CMP-032` — statcheck · grim · pysprite** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 4 obligations open across 3 of 4 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-087-T01 | Establish the validator plugin interface and registry | Implementation owner | Commit / configuration / record reference |
| WP-087-T02 | Add the schema, hash, signature, SBOM and policy validators | Implementation owner | Commit / configuration / record reference |
| WP-087-T03 | Bind the test/CI, run, manifest, locator and lineage validators | Implementation owner | Commit / configuration / record reference |
| WP-087-T04 | Write structural validation of findings and the target revision check | Implementation owner | Commit / configuration / record reference |
| WP-087-T05 | Produce the `VerificationRecord` and its evidence map | Implementation owner | Commit / configuration / record reference |
| WP-087-T06 | Establish validator versioning, calibration and regression | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Verification Engine`
- `Validator catalog`
- `VerificationRecord service`
- `Regression fixtures`
- `V0-V3 verification routing`
- `VerifierQualificationRecord`
- `Positive and negative control suite`
- `Adaptive assurance routing`
- `Abstention verdicts`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-087_mechanical_verifier.tests.md`](WP-087_mechanical_verifier.tests.md).

- Failure on a tampered hash or signature
- Failure on missing lineage or locator
- Invalidation of a finding pointing at the wrong file or symbol
- Deterministic results on the same target
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-087_mechanical_verifier.acceptance.md`](WP-087_mechanical_verifier.acceptance.md), together with what this package still cannot establish.

- [ ] A self-declaration is never counted as verification.
- [ ] Every validator records its input, output, version and artifact hash.
- [ ] A critical mechanical failure cannot be overridden by a reviewer majority.
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

A faulty validator release is revoked; affected `VerificationRecord`s are re-run and receive an impact assessment.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
