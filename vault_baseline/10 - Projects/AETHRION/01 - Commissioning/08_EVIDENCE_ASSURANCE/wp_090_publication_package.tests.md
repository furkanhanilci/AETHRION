---
title: "WP-090 — PublicationPackage, RO-Crate and Provenance Export — Test Procedures"
aliases:
  - "WP-090 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-090_publication_package.tests.md"
generated: false
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
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-090 — PublicationPackage, RO-Crate and Provenance Export — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-090` |
| Work package | [`WP-090` — PublicationPackage, RO-Crate and Provenance Export](wp_090_publication_package.md) |
| Companion | [acceptance criteria](wp_090_publication_package.acceptance.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Citation Auditor / Safety / Archivist** — the independent verifier |
| Accountable owner | Provenance Curator |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-090` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 8 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Provenance Curator | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Provenance Curator | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Citation Auditor / Safety / Archivist | At completion |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-018` accepted output | Claim, Evidence, Review and Decision Schemas | Evidence Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-072` accepted output | LiteratureSetManifest Freeze and Human-Readable Archive | Evidence Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-080` accepted output | Claim–Citation Entailment, Scope and Locator Audit | Citation Audit Lead | Before the first test case runs |
| `WP-081` accepted output | Protocol, Analysis, Baseline and Falsification Registry | Method Office Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |
| `WP-085` accepted output | Repeatability, Reproducibility, Robustness and Replication Pipeline | Reproducibility Lead | Before the first test case runs |
| `WP-087` accepted output | Mechanical Verification Engine | Verification Engineering Lead | Before the first test case runs |
| `WP-088` accepted output | Blind, Cross-Family and Adversarial Review | Assurance Lead | Before the first test case runs |
| `WP-089` accepted output | DisagreementCase and Evidence-Weighted Arbitration | Assurance Lead / Arbiter | Before the first test case runs |

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
| C01 | `Publication builder` | Mandatory deliverable | *(name the test case)* |
| C02 | `RO-Crate profile` | Mandatory deliverable | *(name the test case)* |
| C03 | `Signed publication package` | Mandatory deliverable | *(name the test case)* |
| C04 | `Release checklist` | Mandatory deliverable | *(name the test case)* |
| C05 | `Supersession record` | Mandatory deliverable | *(name the test case)* |
| C06 | `Publication compiler` | Mandatory deliverable | *(name the test case)* |
| C07 | `Assertion and value binding checks` | Mandatory deliverable | *(name the test case)* |
| C08 | Write the `PublicationPackage` and RO-Crate profile and manifest | WP-090-T01 | *(name the test case)* |
| C09 | Build the claim narrative → ledger link materialiser | WP-090-T02 | *(name the test case)* |
| C10 | Bind the CSL citation, locator and audit results | WP-090-T03 | *(name the test case)* |
| C11 | Add the code, data, environment, run and reproduction artifact references | WP-090-T04 | *(name the test case)* |
| C12 | Apply the licence, privacy, redaction and release checks | WP-090-T05 | *(name the test case)* |
| C13 | Produce signature, archive, access, supersession and public landing metadata | WP-090-T06 | *(name the test case)* |
| C14 | Publication Completeness | [ACC-30](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) — Critical | *(name the test case)* |
| C15 | Superseded Publication | [ACC-31](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) — High | *(name the test case)* |
| C16 | Complete Project Audit Export | [ACC-40](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) — Critical | *(name the test case)* |
| C17 | Claimless Publication Assertion | [ACC-52](../12_ACCEPTANCE_SCENARIOS/acc_52_claimless_publication_assertion.md) — Critical | *(name the test case)* |
| C18 | Unverified Numeric Result | [ACC-53](../12_ACCEPTANCE_SCENARIOS/acc_53_unverified_numeric_result.md) — Critical | *(name the test case)* |
| C19 | Unsupported Publication Sentence | [ACC-76](../12_ACCEPTANCE_SCENARIOS/acc_76_unsupported_publication_sentence.md) — Critical | *(name the test case)* |
| C20 | A Claim Without a Complete Evidence Chain | [ACC-105](../12_ACCEPTANCE_SCENARIOS/acc_105_claim_without_evidence_chain.md) — Critical | *(name the test case)* |
| C21 | A Number Without a VerifiedValue | [ACC-106](../12_ACCEPTANCE_SCENARIOS/acc_106_numeric_value_without_verifiedvalue.md) — Critical | *(name the test case)* |

**21 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** RO-Crate profile | E0 | Validate the package against the profile | Conforms; readable by a standard RO-Crate reader | Validation output |
| **TC-02** External readability | **E1** | Open the package with a tool that knows nothing of this system | Claims, sources and runs are navigable | Read transcript |
| **TC-03** **Narrative materialisation** | **E1** | Generate the narrative | Every sentence resolves to a claim in the ledger | Materialisation report |
| **TC-04** Unlinked sentence | **E2** | Add a material sentence with no claim behind it | **Refused** | Refusal transcript |
| **TC-05** Citation rendering | **E1** | Render citations | CSL output; every citation resolves to a source and a locator | Bibliography |
| **TC-06** Citation audit binding | **E2** | Attempt to publish with an open blocking `CitationAudit` finding | **Refused at G9** (WP-080) | Refusal transcript |
| **TC-07** Artifact references | **E1** | Inspect code, data, environment, run and reproduction references | All resolve by digest, not by tag or path | Reference report |
| **TC-08** Missing reproduction | **E2** | Publish an R3 claim with no reproduction certificate | Refused (WP-085) | Refusal transcript |
| **TC-09** **Licence check** | **E2** | Include content whose licence forbids redistribution | Refused; hash-only reference used instead | Refusal transcript |
| **TC-10** **Privacy check** | **E2** | Include personal data | Refused | Refusal transcript |
| **TC-11** **Security release check** | **E2** | Include a protected dataset locator, an internal identifier and a capability-revealing prompt | Each refused, naming the boundary | Three refusals |
| **TC-12** Redaction record | **E1** | Redact a section | The redaction is recorded; the package states that redaction occurred | Redaction record |
| **TC-13** Signature | **E1** | Sign and verify | Verifies; an altered package fails | Verification · failure |
| **TC-14** **Supersession** | **E1** | Supersede a published package | Prior version **reachable**; the successor names it; nothing withdrawn silently | Supersession chain |
| **TC-15** Retraction impact (`ACC-04`) | **E2** | Retract a source cited by a published package | The package is reached; an impact case opens; the claim's state moves | Impact record |
| **TC-16** Landing metadata | **E1** | Inspect the package | Persistent identifier, access statement and licence present | Metadata |
| **TC-17** `DecisionRecord` | **E1** | Inspect the decision | Names the actor, the evidence seen and what was **not** authorised | `DecisionRecord` |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-090 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-090 --gate G9 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-090/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-090
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_090_publication_package.acceptance.md) reaches the decision — issuance is not acceptance.

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
