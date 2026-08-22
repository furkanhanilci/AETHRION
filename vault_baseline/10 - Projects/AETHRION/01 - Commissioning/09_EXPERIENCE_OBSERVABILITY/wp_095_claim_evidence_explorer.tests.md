---
title: "WP-095 — Claim/Evidence Explorer and Provenance Graph — Test Procedures"
aliases:
  - "WP-095 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-095_claim_evidence_explorer.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g5-g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-095 — Claim/Evidence Explorer and Provenance Graph — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-095` |
| Work package | [`WP-095` — Claim/Evidence Explorer and Provenance Graph](wp_095_claim_evidence_explorer.md) |
| Companion | [acceptance criteria](wp_095_claim_evidence_explorer.acceptance.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Citation Auditor / Accessibility Reviewer** — the independent verifier |
| Accountable owner | Evidence Product Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-095` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 5 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5–G10 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Evidence Product Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Evidence Product Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Citation Auditor / Accessibility Reviewer | At completion |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |
| `WP-076` accepted output | Evidence Span Anchoring and Re-anchoring | Evidence Engineering Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-078` accepted output | Structured Evidence Extraction Pipeline | Evidence Lead | Before the first test case runs |
| `WP-079` accepted output | SourceTrustCard and Study Quality Assessment | Methodologist | Before the first test case runs |
| `WP-080` accepted output | Claim–Citation Entailment, Scope and Locator Audit | Citation Audit Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |
| `WP-085` accepted output | Repeatability, Reproducibility, Robustness and Replication Pipeline | Reproducibility Lead | Before the first test case runs |
| `WP-087` accepted output | Mechanical Verification Engine | Verification Engineering Lead | Before the first test case runs |
| `WP-088` accepted output | Blind, Cross-Family and Adversarial Review | Assurance Lead | Before the first test case runs |
| `WP-089` accepted output | DisagreementCase and Evidence-Weighted Arbitration | Assurance Lead / Arbiter | Before the first test case runs |
| `WP-090` accepted output | PublicationPackage, RO-Crate and Provenance Export | Provenance Curator | Before the first test case runs |
| `WP-091` accepted output | Lab Cockpit Information Architecture and Application Shell | Product/Experience Lead | Before the first test case runs |

### Environment readiness report — §8.8

Every row must be checked before the first test case. An unchecked row is a stop condition, not a risk to manage.

- [ ] The target revision is pinned and recorded.
- [ ] The environment manifest has been **captured** from the running environment rather than written from intention.
- [ ] The workspace is isolated from the producer's working tree.
- [ ] Every dependency listed above is `ACCEPTED` (`python3 scripts/ready_queue.py`).
- [ ] The evidence sink is reachable and a specimen manifest verifies.
- [ ] The rollback or compensation path named on the package card can actually be exercised in this environment.

<!-- /generated:environment -->

## Test data requirements — §8.5

<!-- generated:data — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.5 and §8.7. Test data is a **deliverable of this package**, not a by-product of running it: a test whose fixture cannot be regenerated cannot be re-run, and a result that cannot be re-run is an anecdote.

| Requirement | Rule |
|---|---|
| Provenance | Every fixture is either synthetic or a licensed extract with its licence recorded. Personal or production data is never a fixture |
| Data class | Every fixture carries a `DataClass`; a fixture above D2 requires the matching `ExecutionProfile` |
| Regeneration | Each fixture is regenerated from a committed script or manifest, byte-identically |
| Negative fixtures | Every schema and every control has at least one fixture that **must fail**. A test set with no failing fixture proves nothing |
| Independence | Fixtures are not shared with any evaluation golden set (`PR-15` — eval contamination) |

### Test data readiness report — §8.7

- [ ] Every fixture regenerates byte-identically from its committed source.
- [ ] Every fixture carries a `DataClass` and, above D2, an `ExecutionProfile`.
- [ ] At least one **negative** fixture exists per schema and per control.
- [ ] No fixture overlaps an evaluation golden set.
- [ ] Fixture licences permit the retention this test run requires.

<!-- /generated:data -->

## Test coverage items — §8.3.2

<!-- generated:coverage — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.3.2. A coverage item is something the tests must reach. The two sources are mechanical: every mandatory deliverable of this package, and every acceptance scenario bound to it. A coverage item with no test case is a gap, and it is listed here so the gap is visible rather than assumed away.

| # | Coverage item | Source | Covered by |
|---:|---|---|---|
| C01 | `Claim Explorer` | Mandatory deliverable | *(name the test case)* |
| C02 | `Evidence preview` | Mandatory deliverable | *(name the test case)* |
| C03 | `Provenance graph` | Mandatory deliverable | *(name the test case)* |
| C04 | `Assessment/blocker panels` | Mandatory deliverable | *(name the test case)* |
| C05 | `Audit drill-down` | Mandatory deliverable | *(name the test case)* |
| C06 | Write the claim list, detail, version and diff views | WP-095-T01 | *(name the test case)* |
| C07 | Add the evidence-span source preview and locator state | WP-095-T02 | *(name the test case)* |
| C08 | Visualise the dependency, support and contradiction graph | WP-095-T03 | *(name the test case)* |
| C09 | Display the assessment vector and the blocker explanation | WP-095-T04 | *(name the test case)* |
| C10 | Bind the run, review, reproduction and decision timeline | WP-095-T05 | *(name the test case)* |
| C11 | Add the impact/supersession and citation audit views | WP-095-T06 | *(name the test case)* |
| C12 | Retraction Impact | [ACC-04](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) — Critical | *(name the test case)* |
| C13 | Strong Counter-Test | [ACC-08](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) — Critical | *(name the test case)* |
| C14 | Derived Graph Corruption and Rebuild | [ACC-21](../12_ACCEPTANCE_SCENARIOS/acc_21_graph_corruption.md) — High | *(name the test case)* |
| C15 | Publication Completeness | [ACC-30](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) — Critical | *(name the test case)* |
| C16 | Superseded Publication | [ACC-31](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) — High | *(name the test case)* |

**16 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Claim list and detail | **E1** | Open a claim | Type, state, version, certainty and conditions visible | Screenshot |
| **TC-02** Version diff | **E1** | Compare two claim versions | The difference in assertion, evidence and state is shown | Diff view |
| **TC-03** **Evidence preview** | **E1** | Open an evidence span | The source text is shown at its locator | Screenshot |
| **TC-04** **Degraded locator** | **E1** | Open a span in each degraded state | `RELOCATED`, `AMBIGUOUS`, `NEEDS_REANCHOR` and `ORPHANED` each render **distinctly** | Four screenshots |
| **TC-05** Orphan as blank | **E2** | Render an `ORPHANED` span as an empty preview | Refused — indistinguishable from a claim with no evidence | Refusal transcript |
| **TC-06** Nearby-text substitution | **E2** | Render approximate text for an `AMBIGUOUS` span | Refused | Refusal transcript |
| **TC-07** **Contradiction graph** | **E1** | Open a claim with a `contradicts` edge | The contradiction is rendered **as prominently as support** | Screenshot |
| **TC-08** Latent inconsistency | **E1** | Query the graph for mutually contradicting claims | Returned as a list, not left for a reader to notice | Query result |
| **TC-09** **Seven dimensions** | **E1** | Open the assessment | All seven render **separately**; no single bar or score appears | Screenshot |
| **TC-10** Score rendering | **E2** | Attempt to render the vector as one total | Refused (WP-077) | Refusal transcript |
| **TC-11** Blocker explanation | **E1** | Open a blocked claim | The blocking dimension is named, with what would clear it | Screenshot |
| **TC-12** Timeline | **E1** | Inspect a claim's timeline | Runs, reviews, reproductions and decisions in order, each deep-linked | Screenshot |
| **TC-13** Source trust | **E1** | Open a cited source from a claim | The trust card renders with facts and judgements separated (WP-079) | Screenshot |
| **TC-14** **Supersession — forward** | **E1** | Open a superseded claim | It **says so at the top** and names its successor | Screenshot |
| **TC-15** Supersession — backward | **E1** | Open a superseding claim | Names what it replaced | Screenshot |
| **TC-16** Impact view | **E1** | Retract a cited source | The claim shows the impact case and its state change | Screenshot |
| **TC-17** Citation audit | **E1** | Open the audit view | Each material sentence with its verdict, span and rationale (WP-080) | Screenshot |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-095 # dependencies and their states
python3 scripts/ready_queue.py         # this package must appear under "Ready now"
```

Record the revision in the execution log header. **Results from two revisions are
not evidence** — `00_PROGRAM/05` requires all criteria to pass on the same one.

### Running a case

1. Work in an isolated workspace (`skills/using-isolated-environments`), not in
   the producer's tree.
2. Run the case exactly as written. A deviation is recorded in the completion
   report (§7.4.3), never silently absorbed.
3. Capture the **actual** result verbatim — not a summary of it (§8.9).
4. Compare against the expected result and record a verdict.
5. On any mismatch, raise an incident (§8.11) before continuing.

### Capturing evidence

```bash
python3 scripts/evidence_manifest.py issue --package WP-095 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-095/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-095
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_095_claim_evidence_explorer.acceptance.md) reaches the decision — issuance is not acceptance.

## Test execution log — §8.10

One row per executed case. The log is evidence and is written **as the run happens**, not reconstructed afterwards.

| Case | Date/time (UTC) | Executed by | Revision | Actual result | Verdict | Evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

## Incident reporting — §8.11

Any deviation between an actual and an expected result raises an incident carrying timing, originator, context, description, the originator's assessment of **severity** and **priority**, the risk, and a status. An incident is not closed by the person who raised it deciding it was probably fine: `00_PROGRAM/06` requires a reproducer result before a critical finding can be closed.

| Incident | Raised | Case | Severity | Priority | Risk | Status | Disposition |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Test completion report — §7.4

Written once, at the end of the run, and handed to the verifier with the evidence package.

- **Summary of testing performed:**
- **Deviations from this procedure** (including every skipped case and why):
- **Completion evaluation** against the exit criteria below:
- **Factors that blocked progress:**
- **Test measures** (cases executed / passed / failed / blocked; coverage items reached):
- **Residual risks**, each with an owner and an expiry:
- **Test deliverables** produced:
- **Reusable test assets:**
- **Lessons learned:**

## Exit criteria

<!-- generated:exit — produced by scripts/make_package_companions.py; do not edit inside this block -->

The run is complete when every line holds. These are conditions on the **testing**, not on the package: a complete test run that found defects is complete.

- [ ] Every coverage item above is named by at least one executed test case.
- [ ] Every executed test case has an actual result and a verdict (§8.9).
- [ ] Every case at layer **E2** has been observed to **fail** in its negative direction. A control that has only ever passed has not been tested.
- [ ] Every deviation from this procedure is recorded in the completion report (§7.4.3) — including cases that were skipped and why.
- [ ] Every incident raised has a severity, a priority and a status (§8.11).
- [ ] All results are bound to **one** target revision.
- [ ] The residual risk list is written, with an owner and an expiry for each entry (§7.4.7).

> **Not an exit condition.** That every test passed. A procedure that can only complete on success has no way to report a defect, which is the outcome it exists to produce.

<!-- /generated:exit -->
