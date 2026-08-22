# WP-095 — Claim/Evidence Explorer and Provenance Graph

## Package card

| Field | Value |
|---|---|
| Work package | `WP-095` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Evidence Product Lead |
| Independent verifier | Citation Auditor / Accessibility Reviewer |
| Hard dependencies | WP-030, WP-075, WP-076, WP-077, WP-078, WP-079, WP-080, WP-082, WP-085, WP-087, WP-088, WP-089, WP-090, WP-091 |
| Related gates | G5–G10 |
| Related controls | CTL-EPI-01 |
| Related acceptance scenarios | ACC-04, ACC-08, ACC-21, ACC-30, ACC-31 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-095_claim_evidence_explorer.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-095_claim_evidence_explorer.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A user can inspect a claim's version, certainty and conditions, evidence spans, contradictions, source trust, runs, reviews, reproductions, decisions and supersession chain.


## Analysis
### What this package actually decides

Where a person can see why the system believes something. Everything the ledger
holds becomes navigable: versions, spans, contradictions, trust, runs, reviews,
reproductions, decisions, supersession.

### The contradiction graph is the view that justifies the whole package (T03)

A knowledge base that can only display support accumulates mutually inconsistent
claims and looks healthy. Rendering `contradicts` edges as prominently as
`supports` is what makes inconsistency **visible rather than latent**, and WP-077
made it queryable for exactly this.

### The assessment vector must render as seven dimensions, not a bar (T04)

WP-077 refuses a total score; a UI that renders seven dimensions as a single
progress bar has reintroduced it. Each dimension shows separately, and the
**blocker explanation** names which one is stopping the claim.

### Evidence preview with locator state (T02)

Clicking a span should show the source text. When the anchor has degraded, the
preview must show the **state** — `RELOCATED`, `AMBIGUOUS`, `NEEDS_REANCHOR`,
`ORPHANED` — rather than an empty box or, worse, nearby text that looks right.

An `ORPHANED` span rendered as blank is indistinguishable from a claim with no
evidence.

### Supersession has to be walkable in both directions (T06)

*What replaced this* and *what did this replace*. A superseded claim reached from a
publication must say so at the top, not require a reader to notice a date.

### The citation audit view closes the loop to WP-080

A claim's sentences and their audit verdicts, in one place — so a reader can see
that a claim is supported *and* that the sentences asserting it were checked
against their spans.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

14, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md) | `Projection services` · `Graph/vector/search indexes` · `Rebuild jobs` · `Integrity/lag dashboard` |
| [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md) | `Claim Ledger service` · `Migrations/API` · `State transition engine` · `Lineage queries` |
| [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md) | `Anchor resolver` · `Format adapters` · `Re-anchor queue` · `Anchor regression corpus` |
| [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md) | `Claim state engine` · `Dependency validator` · `Assessment rubric` · `Impact propagation worker` |
| [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md) | `Extraction pipeline` · `Extraction schemas` · `Evidence candidate store` · `Second-pass review queue` |
| [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md) | `SourceTrustCard engine` · `Rubric profiles` · `Calibration set` · `Trust review UI contract` |
| [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md) | `Citation audit service` · `Audit rubric` · `Mechanical locator checker` · `Audit report/scorecard` |
| [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md) | `Run Registry` · `Preflight validator` · `MLflow integration` · `Run lineage queries` |
| [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md) | `Verification pipeline` · `Type-specific protocols` · `Robustness matrix` · `Reproduction certificates` |
| [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md) | `Verification Engine` · `Validator catalog` · `VerificationRecord service` · `Regression fixtures` |
| [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md) | `Review service` · `Assignment/eligibility engine` · `Review rubrics` · `ReviewRecord storage` |
| [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md) | `Disagreement service` · `Arbitration rubric` · `Disposition workflow` · `Appeal/decision integration` |
| [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md) | `Publication builder` · `RO-Crate profile` · `Signed publication package` · `Release checklist` |
| [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md) | `Cockpit application shell` · `Navigation/IA` · `BFF/read APIs` · `RBAC matrix` |

### Full prerequisite closure

**83 of 141 packages (59%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 25 | `WP-056` · `WP-091` |
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
| 40 | `WP-090` |

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-104` · `WP-105` · `WP-106` · `WP-108`
- **Transitively reachable:** **26 of 141 packages (18%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W5 — Human and visibility |
| Dependency depth | level **41** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Evidence Product Lead |
| Independent verifier | Citation Auditor / Accessibility Reviewer |
| Gates touched | `G5–G10` |
| Controls | `CTL-EPI-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-04 — Retraction Impact](../12_ACCEPTANCE_SCENARIOS/ACC-04_retraction_impact.md) | Critical | The old manifest and publication are unchanged; the claim becomes `CHALLENGED`/impact-pending, and an `ImpactCase` plus supersession or review work is opened for the correct projects and owners. |
| [ACC-08 — Strong Counter-Test](../12_ACCEPTANCE_SCENARIOS/ACC-08_strong_counter_test.md) | Critical | The majority vote does not override the test; the claim becomes `CHALLENGED`/`REJECTED`, a `DisagreementCase` opens and G6 does not pass. |
| [ACC-21 — Derived Graph Corruption and Rebuild](../12_ACCEPTANCE_SCENARIOS/ACC-21_graph_corruption.md) | High | Canonical services are unaffected; a new projection is built with the expected counts, hashes and lineage and promoted atomically. |
| [ACC-30 — Publication Completeness](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) | Critical | No publication package, signature or release is produced; G9 is FAIL/REVISE and a correction queue opens. Once the missing link is supplied, a new package version can pass. |
| [ACC-31 — Superseded Publication](../12_ACCEPTANCE_SCENARIOS/ACC-31_superseded_publication.md) | High | The old package stays reachable but is clearly marked superseded; the new package references its predecessor and the reason, and consumers receive an impact event. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-030 — Neo4j, pgvector and OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-075 — Canonical Claim/Evidence Ledger Service](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring and Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency and Assessment Engine](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-078 — Structured Evidence Extraction Pipeline](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard and Study Quality Assessment](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md), [WP-080 — Claim–Citation Entailment, Scope and Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-082 — Run Registry and MLflow Lineage Integration](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md), [WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-087 — Mechanical Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family and Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase and Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate and Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md), [WP-091 — Lab Cockpit Information Architecture and Application Shell](../09_EXPERIENCE_OBSERVABILITY/WP-091_lab_cockpit_shell.md)
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
| `Projection services` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Graph/vector/search indexes` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Rebuild jobs` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Integrity/lag dashboard` | `WP-030` | `python3 scripts/progress.py show WP-030` |
| `Claim Ledger service` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Migrations/API` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `State transition engine` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Lineage queries` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Service runbook` | `WP-075` | `python3 scripts/progress.py show WP-075` |
| `Anchor resolver` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Format adapters` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Re-anchor queue` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Anchor regression corpus` | `WP-076` | `python3 scripts/progress.py show WP-076` |
| `Claim state engine` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Dependency validator` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Assessment rubric` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Impact propagation worker` | `WP-077` | `python3 scripts/progress.py show WP-077` |
| `Extraction pipeline` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Extraction schemas` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Evidence candidate store` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Second-pass review queue` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `Quality dashboard` | `WP-078` | `python3 scripts/progress.py show WP-078` |
| `SourceTrustCard engine` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Rubric profiles` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Calibration set` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Trust review UI contract` | `WP-079` | `python3 scripts/progress.py show WP-079` |
| `Citation audit service` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit rubric` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Mechanical locator checker` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Audit report/scorecard` | `WP-080` | `python3 scripts/progress.py show WP-080` |
| `Run Registry` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Preflight validator` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `MLflow integration` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lineage queries` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Run lifecycle dashboard` | `WP-082` | `python3 scripts/progress.py show WP-082` |
| `Verification pipeline` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Type-specific protocols` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Robustness matrix` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Reproduction certificates` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Failure taxonomy` | `WP-085` | `python3 scripts/progress.py show WP-085` |
| `Verification Engine` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Validator catalog` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `VerificationRecord service` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Regression fixtures` | `WP-087` | `python3 scripts/progress.py show WP-087` |
| `Review service` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Assignment/eligibility engine` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Review rubrics` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `ReviewRecord storage` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Calibration dashboard` | `WP-088` | `python3 scripts/progress.py show WP-088` |
| `Disagreement service` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Arbitration rubric` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Disposition workflow` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Appeal/decision integration` | `WP-089` | `python3 scripts/progress.py show WP-089` |
| `Publication builder` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `RO-Crate profile` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Signed publication package` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Release checklist` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Supersession record` | `WP-090` | `python3 scripts/progress.py show WP-090` |
| `Cockpit application shell` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Navigation/IA` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `BFF/read APIs` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `RBAC matrix` | `WP-091` | `python3 scripts/progress.py show WP-091` |
| `Accessibility baseline` | `WP-091` | `python3 scripts/progress.py show WP-091` |

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
- **Evidence Product Lead** carries the acceptance decision; **Citation Auditor / Accessibility Reviewer** must verify independently of whoever implements.
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
| WP-095-T01 | Write the claim list, detail, version and diff views | Implementation owner | Commit / configuration / record reference |
| WP-095-T02 | Add the evidence-span source preview and locator state | Implementation owner | Commit / configuration / record reference |
| WP-095-T03 | Visualise the dependency, support and contradiction graph | Implementation owner | Commit / configuration / record reference |
| WP-095-T04 | Display the assessment vector and the blocker explanation | Implementation owner | Commit / configuration / record reference |
| WP-095-T05 | Bind the run, review, reproduction and decision timeline | Implementation owner | Commit / configuration / record reference |
| WP-095-T06 | Add the impact/supersession and citation audit views | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Claim Explorer`
- `Evidence preview`
- `Provenance graph`
- `Assessment/blocker panels`
- `Audit drill-down`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-095_claim_evidence_explorer.tests.md`](WP-095_claim_evidence_explorer.tests.md).

- A broken locator remaining visible
- Contradictory evidence not hidden
- A fallback query when the derived graph is corrupted
- Full lineage traversal for a critical claim
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-095_claim_evidence_explorer.acceptance.md`](WP-095_claim_evidence_explorer.acceptance.md), together with what this package still cannot establish.

- [ ] No single confidence percentage is presented.
- [ ] The graph is labelled as derived and carries canonical links.
- [ ] The full chain for a material claim is reachable in a single query.
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

- A decision surface that does not show the evidence delta invites rubber-stamping.
- Telemetry without correlation identifiers cannot answer the questions incidents raise.
- An alert nobody acknowledges is a defect in the alert, not in the responder.

## Rollback / compensation

A rollback of the graph UI or the derived projection does not affect the canonical ledger; the direct ledger fallback view is preserved.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
