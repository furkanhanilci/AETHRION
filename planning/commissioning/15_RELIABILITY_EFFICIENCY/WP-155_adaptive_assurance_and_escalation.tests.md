# WP-155 — Adaptive Assurance, Verifier Qualification and Escalation — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-155` |
| Work package | [`WP-155` — Adaptive Assurance, Verifier Qualification and Escalation](WP-155_adaptive_assurance_and_escalation.md) |
| Companion | [acceptance criteria](WP-155_adaptive_assurance_and_escalation.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Eval Office / Internal Audit** — the independent verifier |
| Accountable owner | Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-155` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 4 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G7 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Assurance Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Assurance Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Eval Office / Internal Audit | At completion |
| `WP-043` accepted output | Role-Based Model and Skill Evaluation, and Golden Set Management | Eval Office | Before the first test case runs |
| `WP-044` accepted output | Model Qualification and Admission Pipeline | Eval Office | Before the first test case runs |
| `WP-087` accepted output | Mechanical Verification Engine | Verification Engineering Lead | Before the first test case runs |

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
| C01 | `Assurance router` | Mandatory deliverable | *(name the test case)* |
| C02 | `Cascade and escalation path` | Mandatory deliverable | *(name the test case)* |
| C03 | `Abstention verdicts` | Mandatory deliverable | *(name the test case)* |
| C04 | `Extended VerifierQualificationRecord` | Mandatory deliverable | *(name the test case)* |
| C05 | Implement the assurance router and its five routing inputs | WP-155-T01 | *(name the test case)* |
| C06 | Implement the V0 → V1 → V2 → V3 cascade with independence-aware verifier selection | WP-155-T02 | *(name the test case)* |
| C07 | Add `ABSTAIN` and `INSUFFICIENT_CONFIDENCE` as first-class verdicts | WP-155-T03 | *(name the test case)* |
| C08 | Make abstention rate a tracked qualification metric | WP-155-T04 | *(name the test case)* |
| C09 | Extend `VerifierQualificationRecord` with fingerprint, coverage and human agreement | WP-155-T05 | *(name the test case)* |
| C10 | Prevent consequence-based downgrade and budget-based route reduction | WP-155-T06 | *(name the test case)* |
| C11 | Build the ambiguous fixture set that a calibrated verifier must abstain on | WP-155-T07 | *(name the test case)* |
| C12 | Inspector Reviews High-Consequence Output | [ACC-092](../12_ACCEPTANCE_SCENARIOS/ACC-092_inspector_high_consequence_review.md) — High | *(name the test case)* |
| C13 | Expired Verifier Qualification | [ACC-107](../12_ACCEPTANCE_SCENARIOS/ACC-107_expired_verifier_qualification.md) — Critical | *(name the test case)* |
| C14 | Escalation Is Not Selective Enforcement | [ACC-108](../12_ACCEPTANCE_SCENARIOS/ACC-108_selective_verifier_escalation.md) — Critical | *(name the test case)* |
| C15 | Verifier Abstention Is a Valid Result | [ACC-109](../12_ACCEPTANCE_SCENARIOS/ACC-109_verifier_abstention_is_valid.md) — High | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-087 supplies the V0–V3 engine this routes between; WP-126 supplies qualification records; a labelled calibration set including genuinely ambiguous cases exists before any verifier is qualified.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate the extended `VerifierQualificationRecord` including fingerprint, coverage, human agreement and abstention rate | Validates; the qualification key carries all five components | Validator output |
| 2 | E1 | Route a claim through V0 and confirm V0 always runs first | V0 precedes every other class | Routing trace |
| 3 | **E2** | **V0/V1 remain absolute.** Fail a V0 check and attempt to proceed on a V2 pass | Refused; deterministic failure is non-waivable | Refusal transcript |
| 4 | E1 | Route claims of differing consequence and read the class assigned to each | Higher consequence reaches deeper classes | Routing traces |
| 5 | **E2** | **Expired qualification.** Request a required verification from a verifier past its `valid_until` | `INCONCLUSIVE`; gate blocked — ACC-107 | Gate state |
| 6 | **E2** | **Threshold change.** Request one from a verifier whose threshold moved after measurement | `INCONCLUSIVE`; the qualification is invalid independently of the expiry date | Gate state |
| 7 | **E1** | **Current qualification.** Request one from a verifier with a current, matching qualification | **Satisfies the requirement.** The rule discriminates | Verification result |
| 8 | E1 | Confirm advisory verdicts from unqualified verifiers are retained and labelled | Retained, labelled, and satisfying nothing | Verification records |
| 9 | **E1** | **Abstention.** Present a genuinely ambiguous case from the calibration set | `ABSTAIN`, escalating rather than passing or failing — ACC-109 | Verification result |
| 10 | **E1** | **Abstention discriminates.** Present unambiguous positive and negative cases | Both yield verdicts — the verifier is not abstaining everywhere | Two results |
| 11 | **E1** | **Abstention is qualified.** Qualify a verifier that never abstains on the ambiguous set | Fails qualification; abstention rate is a recorded metric | Qualification record |
| 12 | **E2** | **No selective enforcement.** Attempt to lower a high-consequence route because the human queue is long | Refused and audited — ACC-108 | Refusal transcript |
| 13 | **E2** | **No budget downgrade.** Attempt to lower a route because of budget pressure | Refused; the task blocks instead | Refusal transcript |
| 14 | E1 | Confirm low-consequence claims route cheaply | They do — routing is adaptive rather than maximal everywhere | Routing traces |
| 15 | E3 | Independent review of the routing decisions for one gate round | The reviewer can say why each claim went where it went | `ReviewRecord` |

Cases 9 and 10 are a pair. A verifier that abstains on the ambiguous case and
also abstains on everything else has coverage rather than calibration, and only
running both tells them apart.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-155   # dependencies and their states
python3 scripts/ready_queue.py           # this package must appear under "Ready now"
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

A case in **bold** is a refusal or an injection: it passes when the system
declines to act, or when a deliberately caused fault is caught. Most of this
table is one or the other, because a reliability package that only exercises the
happy path has tested the thing that was never in doubt.

### Capturing evidence

```bash
python3 scripts/evidence_manifest.py issue --package WP-155 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-155/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-155
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-155_adaptive_assurance_and_escalation.acceptance.md) reaches the decision — issuance is not acceptance.

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
