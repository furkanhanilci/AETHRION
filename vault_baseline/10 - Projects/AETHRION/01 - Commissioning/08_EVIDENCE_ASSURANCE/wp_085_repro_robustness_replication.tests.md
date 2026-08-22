---
title: "WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline — Test Procedures"
aliases:
  - "WP-085 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g7
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-085 — Repeatability, Reproducibility, Robustness and Replication Pipeline — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-085` |
| Work package | [`WP-085` — Repeatability, Reproducibility, Robustness and Replication Pipeline](wp_085_repro_robustness_replication.md) |
| Companion | [acceptance criteria](wp_085_repro_robustness_replication.acceptance.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Assurance Lead / Statistician** — the independent verifier |
| Accountable owner | Reproducibility Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-085` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G7 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Reproducibility Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Reproducibility Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead / Statistician | At completion |
| `WP-005` accepted output | Research Risk and Assurance Profile | Safety & Governance Owner | Before the first test case runs |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-019` accepted output | Run, Environment and Reproduction Schemas | Experiment Platform Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-081` accepted output | Protocol, Analysis, Baseline and Falsification Registry | Method Office Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |
| `WP-083` accepted output | ExperimentBatch and Staged Execution | Scientific Engineering Lead | Before the first test case runs |
| `WP-084` accepted output | Clean-Room Reproduction Environment | Reproducibility Lead | Before the first test case runs |

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
| C01 | `Verification pipeline` | Mandatory deliverable | *(name the test case)* |
| C02 | `Type-specific protocols` | Mandatory deliverable | *(name the test case)* |
| C03 | `Robustness matrix` | Mandatory deliverable | *(name the test case)* |
| C04 | `Reproduction certificates` | Mandatory deliverable | *(name the test case)* |
| C05 | `Failure taxonomy` | Mandatory deliverable | *(name the test case)* |
| C06 | Write the verification type selector and its policy | WP-085-T01 | *(name the test case)* |
| C07 | Establish the same-code, same-environment repeatability job | WP-085-T02 | *(name the test case)* |
| C08 | Establish the independent-environment reproducibility job | WP-085-T03 | *(name the test case)* |
| C09 | Apply the seed, parameter and data-slice robustness matrix | WP-085-T04 | *(name the test case)* |
| C10 | Write the independent data/method replication request lifecycle | WP-085-T05 | *(name the test case)* |
| C11 | Produce tolerance, pre-registration, root-cause, disposition and certificate records | WP-085-T06 | *(name the test case)* |
| C12 | Clean-Room Reproduction Pass | [ACC-19](../12_ACCEPTANCE_SCENARIOS/acc_19_clean_room_pass.md) — High | *(name the test case)* |
| C13 | Clean-Room Reproduction Failure | [ACC-20](../12_ACCEPTANCE_SCENARIOS/acc_20_clean_room_fail.md) — Critical | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Type selector | **E1** | Select verification types for R1, R2 and R3 claims | The minimum required combination differs per class, per policy | Three selections |
| **TC-02** Type substitution | **E2** | Attempt to satisfy a required reproducibility with a repeatability run | **Refused** | Refusal transcript |
| **TC-03** **Repeatability** | **E1** | Re-run same code, same environment | Within the repeatability tolerance | Repeatability certificate |
| **TC-04** **Reproducibility** | **E1** | Run from the manifest in the clean room (WP-084) | Within tolerance; environment differences enumerated | Reproducibility certificate |
| **TC-05** **Robustness** | **E1** | Vary seeds, parameters and data slices per the declared matrix | The **conclusion** is assessed, not the point estimate | Robustness certificate |
| **TC-06** **Replication** | **E1** | Independent data or method attempt | Reported as replication with its own tolerance | Replication certificate |
| **TC-07** **G7a structural refusal** | **E2** | Request deterministic reproduction of a hosted-model run | **Refused naming the structural constraint**, not reported as a tolerance failure | Refusal transcript |
| **TC-08** Open-weight path | **E1** | Reproduce a local open-weight run by weight-file hash | Deterministic reproduction succeeds | Certificate |
| **TC-09** Independence | **E2** | Assign a reproducer who produced the original | Refused (WP-007) | Refusal transcript |
| **TC-10** Independence at gate | **E2** | Grant the reproducer context after assignment | Refused at the gate | Refusal transcript |
| **TC-11** **Pre-registered tolerance** | **E2** | Widen a tolerance after seeing the result | **Refused** | Refusal transcript |
| **TC-12** Tolerance absent | **E2** | Run a verification with no declared tolerance | Refused | Refusal transcript |
| **TC-13** **Root cause — six categories** | **E1** | Force one failure of each category | Each classified correctly; **only *defect in the original* implies the claim was wrong** | Six reports |
| **TC-14** Boolean report | **E2** | Emit a reproduction report with no root cause | Refused | Refusal transcript |
| **TC-15** Failed reproduction | **E2** | Fail a confirmatory reproduction | The claim is marked **`CHALLENGED`** (WP-077, invariant 4) | Claim state |
| **TC-16** Certificate | **E1** | Complete each type | A certificate naming the type, tolerance, environment, independence profile and outcome | Four certificates |
| **TC-17** Disposition | **E1** | Disposition a failed verification | Terminal state with an owner and a reason | Disposition record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-085 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-085 --gate G7 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-085/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-085
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_085_repro_robustness_replication.acceptance.md) reaches the decision — issuance is not acceptance.

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
