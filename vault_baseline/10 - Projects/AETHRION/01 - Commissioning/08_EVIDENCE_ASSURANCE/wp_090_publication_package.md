---
title: "WP-090 — PublicationPackage, RO-Crate and Provenance Export"
aliases:
  - "WP-090"
  - "WP-090 — PublicationPackage, RO-Crate and Provenance Export"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Approved claims, limitations, source sets, protocols, runs, code/data/environment, reviews, reproductions and the DecisionRecord become a portable, signed and supersedable publication package."
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-090_publication_package.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g9
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-090 — PublicationPackage, RO-Crate and Provenance Export

## Package card

| Field | Value |
|---|---|
| Work package | `WP-090` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Provenance Curator |
| Independent verifier | Citation Auditor / Safety / Archivist |
| Hard dependencies | WP-014, WP-018, WP-026, WP-072, WP-075, WP-077, WP-080, WP-081, WP-082, WP-085, WP-087, WP-088, WP-089 |
| Related gates | G9,G10 |
| Related controls | CTL-EPI-01, CTL-DAT-03, CTL-SUP-01 |
| Related acceptance scenarios | ACC-30, ACC-31, ACC-40 |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **Quarto/Pandoc authoring stack (provisional) · CSL · JATS · MECA · veraPDF**

The publication package is produced by an adopted authoring stack rather than a bespoke renderer: Quarto orchestrates, Pandoc's AST carries transformations, CSL supplies citation styles, JATS and MECA are interchange and submission exports, and veraPDF validates the rendered artifact when PDF/A or PDF/UA is requested. **A renderer exiting zero decides nothing** — publication remains a G9 human decision, and the authoring backend is provisional until the bake-off in `skills/authoring-research-documents/references/authoring-backend-bakeoff.md` is run.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md` §9.1.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_090_publication_package.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_090_publication_package.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Approved claims, limitations, source sets, protocols, runs, code/data/environment, reviews, reproductions and the `DecisionRecord` become a portable, signed and supersedable publication package.


## Analysis
### What this package actually decides

What leaves the laboratory. A `PublicationPackage` carries the claims, their
lineage, the sources, the protocols, the runs, the code, the data, the environment,
the reviews, the reproductions and the `DecisionRecord` — as one portable, signed,
supersedable object.

### RO-Crate because the format should outlive the system (T01)

`AETHRION_COMPONENT_REUSE.md` adopts **Workflow Run RO-Crate**. The reason is
specific: a package readable only by the system that produced it is not a
publication, and a laboratory that closes leaves its results unreadable.

Adopted, not invented — this package writes a profile, not a format.

### Supersession is what makes publication compatible with the loop (T06)

`AGENTS.md` §4.1: `VERIFIED` is explicitly not a permanent state, and the loop
closes. A publication that cannot be superseded forces the choice between a
permanent record and a correctable one — and `ACC-04`'s retraction impact scenario
needs the second.

The prior version stays reachable. Nothing is withdrawn silently.

### The release checks are three separate gates, not one review (T05)

- **Licence** — may this source's content be redistributed at all? (`PR-14`)
- **Privacy** — does the package contain personal data?
- **Security release** — does publishing reveal something the trust boundary
  protected: a dataset locator, an internal identifier, a prompt exposing an
  unpublished capability?

The third is the one that gets skipped, and it is the one a research laboratory is
least practised at.

### The narrative must materialise from the ledger, not beside it (T02)

If the prose is written independently and links are added afterwards, the links are
decoration. Materialising the claim narrative **from** the ledger means a sentence
without a claim cannot appear, which is what `evidence-before-claim` requires and
what WP-080's audit checks.

### The landing metadata is what makes the package findable and citable (T06)

A DOI, a persistent identifier, and an access statement. WP-138/WP-139 own the
deposit and the timestamp; this package produces what they deposit.

### Baseline v1.2.0 — the compiler's job is to refuse

The publication package becomes a **compiler over canonical state**. The document
is a projection of the claim, evidence and value graph; a language model may draft
wording and is never the source of what the document asserts.

Four refusals, each with a scenario:

| Refusal | Test |
|---|---|
| A factual sentence with no `ClaimVersion` | ACC-52 |
| A number the `VerifiedValue` registry does not carry | ACC-53 |
| A real citation that does not support the sentence | ACC-76 |
| A V2 verdict with no current qualification | ACC-61 |

The check must **discriminate**: structural and editorial text carries a
`text_role` and passes, and a declared rounding of a registered value passes and
records its display transform. A compiler that blocks all prose has demonstrated
nothing except that it can block.

Method sections are rendered from the executed protocol, code and configuration.
Hand-editing the prose invalidates the method–code alignment result, which was
about a specific pair of texts.

The scope verifier proposes a bounded restatement and does not apply one. A system
that silently rewrites its own claims to make them pass has replaced one integrity
problem with a worse one.

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

13, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md) | `Evidence contract bundle` · `Claim state machine` · `Review/disagreement schemas` · `Decision schema fixtures` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md) | `LiteratureSetManifest` · `Signed frozen package` · `Portable exports` · `Zotero frozen view` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md) | `Citation audit service` · `Audit rubric` · `Mechanical locator checker` · `Audit report/scorecard` |
| [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md) | `Method Registry` · `Protocol validators` · `Amendment workflow` · `Post-hoc change detector` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md) | `Verification pipeline` · `Type-specific protocols` · `Robustness matrix` · `Reproduction certificates` |
| [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md) | `Verification Engine` · `Validator catalog` · `VerificationRecord service` · `Regression fixtures` |
| [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md) | `Review service` · `Assignment/eligibility engine` · `Review rubrics` · `ReviewRecord storage` |
| [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md) | `Disagreement service` · `Arbitration rubric` · `Disposition workflow` · `Appeal/decision integration` |

### Full prerequisite closure

**81 of 160 packages (51%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 26 | `WP-057` · `WP-059` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` · `WP-083` · `WP-084` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` · `WP-085` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-095` · `WP-106` · `WP-107` · `WP-108` · `WP-109` · `WP-113` · `WP-138`
- **Transitively reachable:** **29 of 160 packages (18%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W4 — Knowledge and evidence |
| Dependency depth | level **40** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Provenance Curator |
| Independent verifier | Citation Auditor / Safety / Archivist |
| Gates touched | `G9` · `G10` |
| Controls | `CTL-EPI-01` · `CTL-DAT-03` · `CTL-SUP-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |
| [ACC-40 — Complete Project Audit Export](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) | Critical | The signed export verifies with complete correlation and hash chain; a missing or tampered fixture fails verification and raises an incident. |
| [ACC-52 — Claimless Publication Assertion](../12_ACCEPTANCE_SCENARIOS/acc_52_claimless_publication_assertion.md) | Critical | The build fails; the sentence's location and the missing relation are reported; no signed `PublicationPackage` is produced. Prose whose `text_role` declares it structural or editorial is not affected. |
| [ACC-53 — Unverified Numeric Result](../12_ACCEPTANCE_SCENARIOS/acc_53_unverified_numeric_result.md) | Critical | The build fails regardless of the quality of the surrounding prose; the report lists the value refs that were permitted and the one that was not. A declared rounding or display transform of a registered value passes. |
| [ACC-76 — Unsupported Publication Sentence](../12_ACCEPTANCE_SCENARIOS/acc_76_unsupported_publication_sentence.md) | Critical | The reference-existence check passes at V0, and the entailment and scope checks fail at V2. Publication is blocked. A control sentence whose citation genuinely supports it passes both. |
| [ACC-105 — A Claim Without a Complete Evidence Chain](../12_ACCEPTANCE_SCENARIOS/acc_105_claim_without_evidence_chain.md) | Critical | The break is found and named at the failing link, and publication is blocked. A complete chain passes, so the audit discriminates rather than blocking every claim. |
| [ACC-106 — A Number Without a VerifiedValue](../12_ACCEPTANCE_SCENARIOS/acc_106_numeric_value_without_verifiedvalue.md) | Critical | The build fails and names the ungrounded figure. A registered value passes, and a declared rounding of a registered value passes and records its display transform. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review and Decision Schemas](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-072 — LiteratureSetManifest Freeze and Human-Readable Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline and Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md)
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
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `LiteratureSetManifest` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Signed frozen package` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Portable exports` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Zotero frozen view` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Freeze/diff report` | `WP-072` | `python3 scripts/progress.py show WP-072` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
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
| `Verification pipeline` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Type-specific protocols` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Robustness matrix` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Reproduction certificates` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Failure taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `AlgorithmUnderstandingRecord` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ReproductionPackage` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `ClaimConsistencyReport` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Five-level reproduction taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Verification Engine` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Validator catalog` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerificationRecord service` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Regression fixtures` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `V0-V3 verification routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerifierQualificationRecord` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Positive and negative control suite` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Adaptive assurance routing` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Abstention verdicts` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Review service` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Assignment/eligibility engine` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Review rubrics` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `ReviewRecord storage` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Calibration dashboard` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Disagreement service` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Arbitration rubric` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Disposition workflow` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Appeal/decision integration` | `WP-089` | `python3 scripts/progress.py show WP-089` |

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
- **Provenance Curator** carries the acceptance decision; **Citation Auditor / Safety / Archivist** must verify independently of whoever implements.
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
| `ASM-033` — CiTO — Citation Typing Ontology | `STANDARD` | the running implementation | the contract this is held behind | **1** |
| `ASM-034` — Nanopublications — claim-level machine-readable publication | `DEFER` | nothing — recorded so it is not re-examined from scratch | everything — the implementation here is this repository's own | none |
| `CMP-022` — Workflow Run RO-Crate | `STANDARD` | The crate format and its PROV mapping. | Which run facts must be present for a run to be re-executable by someone who was not there. | none |
| `CMP-027` — Pandoc | `DEPENDENCY` | The document AST, citeproc, reference templates and Lua filter execution. | Every AIRL transformation, expressed as an AST filter. | **2** |
| `CMP-028` — Quarto | `DEPENDENCY` | Manuscript orchestration, cross references, multi-format render, JATS output and MECA bundling. | The publication package contract and what a rendered artifact must contain. | **2** |
| `CMP-029` — MyST | `OPTIONAL_BACKEND` | The authoring and render stack. | The publication package contract, as for Quarto. | **1** |
| `CMP-030` — CSL | `STANDARD` | Citation style definitions and their rendering. | Which style a venue requires; nothing more. | none |
| `CMP-031` — veraPDF | `DEPENDENCY` | PDF/A and PDF/UA validation. | The accessibility contract the rendered artifact must satisfy. | **2** |
| `CMP-035` — Manubot | `PATTERN` | the idea only — no code and nothing called at runtime | Manuscript-as-code discipline: continuous rebuild and citation by identifier. | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-001` | A CoE Audit result is a VerificationResult, never a GateRecord verdict. The audit reports; the gate policy decides. | The producer architecture, the provider assumptions, and any notion that the audit score is itself a decision. |
| `ASM-033` | A citation type describes the intent of a link. It does not establish that the link is correct — that is the V2 entailment verifier's job. | The full ontology surface; only the relations EvidenceTag actually needs. |
| `ASM-034` | An export projection of accepted claims. Publishing one does not accept a claim; a DecisionRecord does. | Nothing yet — deferred. |
| `CMP-022` | A crate records what ran. It does not assert that the result supports a claim; that binding is the `EvidenceManifest`'s. | Any AETHRION-specific run format that would fork the standard. |
| `CMP-027` | A renderer formats what the compiler decided; it never changes what a document asserts. **AIRL transformations are AST filters, never regexes over a manuscript.** | Any transformation that edits rendered output after the fact. |
| `CMP-028` | As for Pandoc: rendering never changes an assertion. | Quarto's computation cache as a source of results. |
| `CMP-029` | As for Quarto. | Any stack-specific syntax in canonical content. |
| `CMP-030` | A citation style is presentation. It never changes which source supports a claim. | An AIRL-invented citation style — AETHRION does not invent one. |
| `CMP-031` | A validator reports conformance to a format profile. It does not assess whether the document is readable by a person, and a pass is not an accessibility claim. | A validator pass as evidence that WCAG 2.2 is met. |
| `CMP-035` | A build discipline says nothing about what the manuscript may claim. | Manubot as a second render engine — taken as discipline, not as an engine. |

### Where a plain row would mislead

- **`ASM-001`** — Two public versions of this work report different evaluation corpus sizes. Any number quoted from it must carry the version it came from — the same rule this architecture applies to SourceRepresentation.
- **`ASM-033`** — Not in the source brief; added here. EvidenceTag.support_relation was about to be an invented three-value enum (SUPPORTS / CHALLENGES / CONTEXTUALIZES). CiTO already provides the published vocabulary for exactly this — cito:supports, cito:disagreesWith, cito:usesMethodIn and the rest — and AETHRION's own rule is not to invent an identifier scheme where one is maintained by people closer to the problem. Binding the enum to CiTO IRIs costs nothing now and makes an EvidenceTag exportable to anyone who reads SPAR.
- **`ASM-034`** — Not in the source brief; added here as a deferred candidate. Its structure — assertion, provenance, publication info as one citable unit — is close to an exact match for ClaimVersion plus EvidenceTag plus DecisionRecord, so the publication compiler should be built so that this projection is later addable without reshaping the claim model. Deferred because a projection nobody consumes is cost without benefit until the compiler exists.

### Unresolved before implementation

Each item below is an obligation its mode creates, quoted from the rule that creates it. None can be met from a session with no network access, and none may be assumed satisfied.

**`ASM-001` — ScientistOne / Science One Framework — Chain-of-Evidence** · `ADAPTIVE_REIMPLEMENT` · status `PROPOSED`

- a written mechanism specification — inputs, outputs, state, transitions, invariants, failure conditions and forbidden behaviour — before implementation

**`ASM-033` — CiTO — Citation Typing Ontology** · `STANDARD` · status `PROPOSED`

- a conformance suite against the published specification

**`CMP-027` — Pandoc** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**`CMP-028` — Quarto** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**`CMP-029` — MyST** · `OPTIONAL_BACKEND` · status `PROPOSED`

- the backend itself — still unchosen, which is the correct state until the qualification runs, and a stop condition for anyone about to pick one

**`CMP-031` — veraPDF** · `DEPENDENCY` · status `PROPOSED`

- a version or image-digest policy and an upgrade path
- what happens when it is unavailable, slow or wrong

**Acquisition readiness — 9 obligations open across 6 of 10 sources.** `00_PROGRAM/05_definition_of_ready_and_done.md` requires the acquisition surface of a package to be classified and its obligations resolved before the package is `READY`; `scripts/ready_queue.py` holds it back until they are.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-090-T01 | Write the `PublicationPackage` and RO-Crate profile and manifest | Implementation owner | Commit / configuration / record reference |
| WP-090-T02 | Build the claim narrative → ledger link materialiser | Implementation owner | Commit / configuration / record reference |
| WP-090-T03 | Bind the CSL citation, locator and audit results | Implementation owner | Commit / configuration / record reference |
| WP-090-T04 | Add the code, data, environment, run and reproduction artifact references | Implementation owner | Commit / configuration / record reference |
| WP-090-T05 | Apply the licence, privacy, redaction and release checks | Implementation owner | Commit / configuration / record reference |
| WP-090-T06 | Produce signature, archive, access, supersession and public landing metadata | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Publication builder`
- `RO-Crate profile`
- `Signed publication package`
- `Release checklist`
- `Supersession record`
- `Publication compiler`
- `Assertion and value binding checks`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-090_publication_package.tests.md`](wp_090_publication_package.tests.md).

- Failure when a critical claim has no locator
- Redaction of restricted data
- Package hash and signature verification
- An old link remaining accessible after supersession
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-090_publication_package.acceptance.md`](wp_090_publication_package.acceptance.md), together with what this package still cannot establish.

- [ ] The narrative cannot change the certainty or limitations recorded in the ledger.
- [ ] The package carries complete lineage and its `DecisionRecord`.
- [ ] An older package is never deleted; it receives a supersession link.
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

A pre-release fault marks the draft package `INVALIDATED`; a post-publication correction requires a new version, a supersession and an `ImpactCase`.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
