# WP-126 — Reviewer, Judge and Reproducer Calibration — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-126` |
| Work package | [`WP-126` — Reviewer, Judge and Reproducer Calibration](WP-126_assurance_calibration.md) |
| Companion | [acceptance criteria](WP-126_assurance_calibration.acceptance.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Eval Office / Independent Human Reviewer** — the independent verifier |
| Accountable owner | Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-126` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 3 acceptance scenario(s) |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G7 |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Day-2 |

**Applicable layers: E0 · E1 · E2 · E3 · E4 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Assurance Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Assurance Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Eval Office / Independent Human Reviewer | At completion |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-043` accepted output | Role-Based Model and Skill Evaluation, and Golden Set Management | Eval Office | Before the first test case runs |
| `WP-085` accepted output | Repeatability, Reproducibility, Robustness and Replication Pipeline | Reproducibility Lead | Before the first test case runs |
| `WP-086` accepted output | Frozen and Blind Review Package Builder | Assurance Platform Lead | Before the first test case runs |
| `WP-087` accepted output | Mechanical Verification Engine | Verification Engineering Lead | Before the first test case runs |
| `WP-088` accepted output | Blind, Cross-Family and Adversarial Review | Assurance Lead | Before the first test case runs |
| `WP-089` accepted output | DisagreementCase and Evidence-Weighted Arbitration | Assurance Lead / Arbiter | Before the first test case runs |
| `WP-113` accepted output | Evidence, Reproduction and Publication Acceptance Package | Assurance Lead | Before the first test case runs |
| `WP-121` accepted output | Hypercare, Stabilisation and Programme Closure | SRE Lead / Program Lead | Before the first test case runs |

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
| C01 | `Calibration reports` | Mandatory deliverable | *(name the test case)* |
| C02 | `Reviewer capability decisions` | Mandatory deliverable | *(name the test case)* |
| C03 | `Bias/quality dashboard` | Mandatory deliverable | *(name the test case)* |
| C04 | `Improvement actions` | Mandatory deliverable | *(name the test case)* |
| C05 | Run the calibration set and hidden counter-tests periodically | WP-126-T01 | *(name the test case)* |
| C06 | Audit order swaps and blind/unblind leakage | WP-126-T02 | *(name the test case)* |
| C07 | Compute validated precision and recall, disagreement rates and triage time | WP-126-T03 | *(name the test case)* |
| C08 | Establish reviewer and reproducer profile expiry and suspension | WP-126-T04 | *(name the test case)* |
| C09 | Correct rubrics, training and bundles, then requalify | WP-126-T05 | *(name the test case)* |
| C10 | Reviewer Order Bias | [ACC-07](../12_ACCEPTANCE_SCENARIOS/ACC-07_reviewer_order_bias.md) — High | *(name the test case)* |
| C11 | Strong Counter-Test | [ACC-08](../12_ACCEPTANCE_SCENARIOS/ACC-08_strong_counter_test.md) — Critical | *(name the test case)* |
| C12 | Critical Reviewer Unavailable | [ACC-38](../12_ACCEPTANCE_SCENARIOS/ACC-38_reviewer_unavailable.md) — High | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Calibration set | E0 | Inspect the calibration set | Known-outcome items, held out, refreshed on a schedule | Set manifest |
| **TC-02** **Hidden counter-tests** | **E1** | Inject known defects reviewers were not told about | **Recall measured**, not only precision | Recall report |
| **TC-03** Counter-test leakage | **E2** | Detect a counter-test that became known | Retired and replaced; the affected measurements are marked | Retirement record |
| **TC-04** **Validated precision** | **E1** | Measure per reviewer | Findings that **survived arbitration and reproduction** — not raw finding count | Precision report |
| **TC-05** Noise detection | **E2** | Detect a reviewer whose findings rarely survive | Flagged — noise consumes the scarcest resource in the system | Flag record |
| **TC-06** Silent reviewer | **E2** | Detect a reviewer who never finds anything | Flagged | Flag record |
| **TC-07** **Order bias** | **E1** | Present the same package in two finding orders | Verdicts compared; **order effect measured as a number** | Bias report |
| **TC-08** **Identity bias** | **E2** | Present packages with and without inferable producer identity | Verdict difference measured | Bias report |
| **TC-09** **Verbosity bias** | **E2** | Present the same substance at two lengths and confidence levels | Verdict difference measured — the bias most specific to model reviewers | Bias report |
| **TC-10** **Blind leakage audit** | **E2** | Test whether verdicts correlate with producer identity | No correlation, or a **leak is found and traced** | Leakage report |
| **TC-11** **Pairwise error correlation** | **E1** | Measure across the reviewer pool | **Reported as a number per pair** — this is `PR-16` and the go-live condition | Correlation matrix |
| **TC-12** Correlated pair | **E2** | Detect two reviewers whose errors correlate above threshold | They **cannot both satisfy an independence requirement** | Constraint record |
| **TC-13** Disagreement rate | **E1** | Measure reviewer disagreement | Reported; a rate near zero is **investigated**, not celebrated | Disagreement report |
| **TC-14** Triage time | **E1** | Measure time to first verdict | Reported; correlated with precision | Timing report |
| **TC-15** **Reproducer consistency** | **E1** | Have two reproducers verify the same claim | Agreement measured; disagreements itemised | Consistency report |
| **TC-16** **Profile expiry** | **E2** | Pass a reviewer profile's expiry | **Ineligible until requalified** | Expiry transcript |
| **TC-17** Suspension | **E1** | Suspend a reviewer on measured degradation | Recorded with evidence; open assignments reassigned | Suspension record |
| **TC-18** **Rubric correction** | **E1** | Correct a rubric after a measured bias | Requalification required against the corrected rubric | Requalification record |
| **TC-19** Escaped defects | **E1** | Track defects that passed review and were found later | Attributed back to the reviewing profile | Escape report |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-126 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-126 --gate G6,G7,Day-2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-126/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-126
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-126_assurance_calibration.acceptance.md) reaches the decision — issuance is not acceptance.

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
