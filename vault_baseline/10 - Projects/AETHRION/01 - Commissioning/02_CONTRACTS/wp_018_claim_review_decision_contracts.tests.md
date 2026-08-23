---
title: "WP-018 — Claim, Evidence, Review and Decision Schemas — Test Procedures"
aliases:
  - "WP-018 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/02_CONTRACTS/WP-018_claim_review_decision_contracts.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/l
  - aethrion/gate/g5-g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-018 — Claim, Evidence, Review and Decision Schemas — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-018` |
| Work package | [`WP-018` — Claim, Evidence, Review and Decision Schemas](wp_018_claim_review_decision_contracts.md) |
| Companion | [acceptance criteria](wp_018_claim_review_decision_contracts.acceptance.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Assurance Lead / Methodologist** — the independent verifier |
| Accountable owner | Evidence Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-018` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 2 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5–G10 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Evidence Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Evidence Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead / Methodologist | At completion |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |
| `WP-012` accepted output | Canonical Ownership and Field-Level Authority Matrix | Chief Architect | Before the first test case runs |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-016` accepted output | PolicyDecision, Control and Exception Schemas | Policy Platform Lead | Before the first test case runs |
| `WP-017` accepted output | Source Registry and Literature Contract Schemas | Knowledge Lead | Before the first test case runs |

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
| C01 | `Evidence contract bundle` | Mandatory deliverable | *(name the test case)* |
| C02 | `Claim state machine` | Mandatory deliverable | *(name the test case)* |
| C03 | `Review/disagreement schemas` | Mandatory deliverable | *(name the test case)* |
| C04 | `Decision schema fixtures` | Mandatory deliverable | *(name the test case)* |
| C05 | `PublicationAssertion` | Mandatory deliverable | *(name the test case)* |
| C06 | `EvidenceTag` | Mandatory deliverable | *(name the test case)* |
| C07 | `FindingRecord` | Mandatory deliverable | *(name the test case)* |
| C08 | `Authority typing on every scientific record` | Mandatory deliverable | *(name the test case)* |
| C09 | Write the `ClaimRecord` type, status and validity conditions | WP-018-T01 | *(name the test case)* |
| C10 | Define the evidence anchor as hash + structural locator + text fingerprint | WP-018-T02 | *(name the test case)* |
| C11 | Add the `ClaimDependency` supports / contradicts / derived-from relations | WP-018-T03 | *(name the test case)* |
| C12 | Write the `ReviewRecord`, `Verdict`, `Finding` and `Disposition` schemas | WP-018-T04 | *(name the test case)* |
| C13 | Complete the `DisagreementCase`, `DecisionRecord` and supersession fields | WP-018-T05 | *(name the test case)* |
| C14 | Strong Counter-Test | [ACC-08](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) — Critical | *(name the test case)* |
| C15 | Publication Completeness | [ACC-30](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) — Critical | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-014 and WP-017 are `ACCEPTED`; at least one real source
representation with extractable text is available.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate the evidence contract bundle | `ClaimRecord`, `EvidenceSpan`, `ClaimDependency`, `ReviewRecord`, `Verdict`, `Finding`, `Disposition`, `DisagreementCase`, `DecisionRecord` all validate | Schema validation output |
| 2 | **E0** | **Anchor completeness test.** Confirm an `EvidenceSpan` requires all three of hash, structural locator and text fingerprint | A span missing any one is rejected | Rejection transcript |
| 3 | E1 | Anchor a span in a real document and re-locate it | The span is found by all three mechanisms independently | Three resolution transcripts |
| 4 | **E2** | **Re-extraction test.** Re-extract the same document with a different parser | The hash breaks; the **structural locator and fingerprint still resolve**; the system reports *source representation changed*, not *evidence missing* | Degradation transcript |
| 5 | **E2** | **Re-typesetting test.** Substitute a differently paginated edition | The locator breaks; the **fingerprint still resolves**; the span is re-anchored with a recorded provenance of the re-anchoring | Re-anchor record |
| 6 | **E2** | **Unanchored-claim test.** Create a claim with no evidence span | Rejected, or created only in a state that cannot be published | Rejection transcript |
| 7 | **E2** | **Claim-edit test.** Attempt to edit a claim that a decision depends on | Rejected; a new version is required, and the dependency still names the old version | Versioning transcript |
| 8 | E1 | Record `supports`, `contradicts` and `derived-from` dependencies | All three resolve in both directions | Dependency graph query |
| 9 | **E1** | **Contradiction query test.** Introduce two claims that contradict, then query for inconsistency | The pair is returned. An inconsistency that requires a human to notice does not pass | Inconsistency query result |
| 10 | **E0** | **Finding-state test.** Confirm `Finding`'s state domain contains no value meaning "open indefinitely" | Every non-terminal state requires an owner and an expiry | State machine |
| 11 | **E2** | **Disagreement test.** Produce two conflicting verdicts on one claim | A `DisagreementCase` opens automatically; it cannot be closed without an arbiter decision | Disagreement transcript |
| 12 | **E0** | **Confidence test.** Record a confidence value with no calibration basis | Stored as `UNCALIBRATED` and **rendered as such wherever displayed**; it cannot be presented as a calibrated number | Display sample |
| 13 | **E2** | **Supersession test.** Supersede a published claim | The prior version stays reachable; the publication's lineage still resolves; downstream records are not rewritten | Supersession chain |
| 14 | E3 | Independent review of the anchor design against `anchoring-spans` and `extracting-evidence` | The contract supports what the skills require | `ReviewRecord` |

Steps 4 and 5 are the design's justification. If the three-part anchor does not
degrade gracefully under them, it is three fields rather than one mechanism.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-018 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-018 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-018/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-018
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_018_claim_review_decision_contracts.acceptance.md) reaches the decision — issuance is not acceptance.

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
