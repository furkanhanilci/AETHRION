---
title: "WP-083 — ExperimentBatch and Staged Execution — Test Procedures"
aliases:
  - "WP-083 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-083_experiment_batch.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-083 — ExperimentBatch and Staged Execution — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-083` |
| Work package | [`WP-083` — ExperimentBatch and Staged Execution](wp_083_experiment_batch.md) |
| Companion | [acceptance criteria](wp_083_experiment_batch.acceptance.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Methodologist / FinOps / SRE** — the independent verifier |
| Accountable owner | Scientific Engineering Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-083` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 3 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Scientific Engineering Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Scientific Engineering Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Methodologist / FinOps / SRE | At completion |
| `WP-032` accepted output | ProjectLifecycle Workflow Skeleton | Workflow Engineering Lead | Before the first test case runs |
| `WP-035` accepted output | G2 Protocol, G3 Literature and G4 Baseline Workflows | Scientific Workflow Lead | Before the first test case runs |
| `WP-045` accepted output | Policy Router and Minimum-Sufficient Model Package | Model Platform Lead | Before the first test case runs |
| `WP-053` accepted output | Kueue Queue, Quota and Priority Policy | Compute Platform Lead | Before the first test case runs |
| `WP-054` accepted output | gVisor Sandbox and Execution Cell Lifecycle | Execution Security Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |

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
| C01 | `ExperimentBatch workflow` | Mandatory deliverable | *(name the test case)* |
| C02 | `Staging policy` | Mandatory deliverable | *(name the test case)* |
| C03 | `Parameter manifest` | Mandatory deliverable | *(name the test case)* |
| C04 | `Checkpoint/recovery logic` | Mandatory deliverable | *(name the test case)* |
| C05 | `Batch report` | Mandatory deliverable | *(name the test case)* |
| C06 | Write the `ExperimentBatch` workflow and the batch/item state model | WP-083-T01 | *(name the test case)* |
| C07 | Establish the staged compute promotion checks | WP-083-T02 | *(name the test case)* |
| C08 | Apply the parameter/seed matrix and fan-out caps | WP-083-T03 | *(name the test case)* |
| C09 | Add checkpointing, preemption, resume and partial-result behaviour | WP-083-T04 | *(name the test case)* |
| C10 | Bind budget reservation, release and cost attribution | WP-083-T05 | *(name the test case)* |
| C11 | Implement the stop / pivot / negative-result decision | WP-083-T06 | *(name the test case)* |
| C12 | Budget Hard Stop | [ACC-09](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) — Critical | *(name the test case)* |
| C13 | Kueue Preemption | [ACC-33](../12_ACCEPTANCE_SCENARIOS/acc_33_kueue_preemption.md) — High | *(name the test case)* |
| C14 | Negative Research Result | [ACC-39](../12_ACCEPTANCE_SCENARIOS/acc_39_negative_result.md) — Medium | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Batch state model | E0 | Inspect batch and item states | Both modelled; item failure does not silently fail the batch | State machine |
| **TC-02** Stage order | **E1** | Run a batch | Smoke → baseline → sweep → full, in order | Batch trace |
| **TC-03** Stage skip | **E2** | Attempt to launch a full run without smoke and baseline | **Refused** | Refusal transcript |
| **TC-04** Smoke failure | **E1** | Fail the smoke stage | The batch stops; no compute is spent on later stages | Stop record |
| **TC-05** Baseline failure | **E1** | Have the baseline show the effect in the control | The batch **stops and reports it** rather than proceeding | Stop record |
| **TC-06** **Fan-out cap** | **E2** | Submit a matrix exceeding the declared cap | Refused **before dispatch** | Refusal transcript |
| **TC-07** Budget reservation | **E1** | Launch a batch | The full budget is reserved up front (WP-053) | Reservation record |
| **TC-08** Budget exhaustion | **E1** | Exhaust the reservation mid-batch | The batch pauses **without losing state**; nothing is silently truncated | Pause transcript |
| **TC-09** Checkpoint | **E1** | Checkpoint and resume | Resumes from the checkpoint; no item runs twice | Resume transcript |
| **TC-10** Preemption | **E1** | Preempt mid-batch (WP-053) | Checkpoint written; work resumes | Resume transcript |
| **TC-11** **Partial results** | **E1** | Stop a batch part-way | Results marked **partial** with the completed fraction recorded | Result record |
| **TC-12** Partial as complete | **E2** | Attempt to report partial results as a complete batch | Refused | Refusal transcript |
| **TC-13** **Mid-batch parameter change** | **E2** | Change a threshold during execution | **The batch stops.** It is not adjusted and continued | Stop transcript |
| **TC-14** Stop rule | **E1** | Trigger a declared stop rule | The batch stops; the rule that fired is recorded | Stop record |
| **TC-15** **Negative completion** | **E1** | Complete a batch whose result does not support the hypothesis | A **legitimate completion**, recorded as a negative result (WP-082) | Batch record |
| **TC-16** Pivot | **E1** | Trigger a pivot condition | Recorded as a pivot with its reason; the original batch closes cleanly | Pivot record |
| **TC-17** Cost attribution | **E1** | Inspect a completed batch | Cost attributed per item and per stage | Cost record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-083 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-083 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-083/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-083
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_083_experiment_batch.acceptance.md) reaches the decision — issuance is not acceptance.

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
