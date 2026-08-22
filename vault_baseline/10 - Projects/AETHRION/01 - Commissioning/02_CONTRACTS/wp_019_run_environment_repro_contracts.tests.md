---
title: "WP-019 — Run, Environment and Reproduction Schemas — Test Procedures"
aliases:
  - "WP-019 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/02_CONTRACTS/WP-019_run_environment_repro_contracts.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/g4-g7
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-019 — Run, Environment and Reproduction Schemas — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-019` |
| Work package | [`WP-019` — Run, Environment and Reproduction Schemas](wp_019_run_environment_repro_contracts.md) |
| Companion | [acceptance criteria](wp_019_run_environment_repro_contracts.acceptance.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Reproducibility Engineer** — the independent verifier |
| Accountable owner | Experiment Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-019` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 2 acceptance scenario(s) |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Experiment Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Experiment Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Reproducibility Engineer | At completion |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-018` accepted output | Claim, Evidence, Review and Decision Schemas | Evidence Platform Lead | Before the first test case runs |

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
| C01 | `Run schema bundle` | Mandatory deliverable | *(name the test case)* |
| C02 | `EnvironmentManifest` | Mandatory deliverable | *(name the test case)* |
| C03 | `ReproductionReport` | Mandatory deliverable | *(name the test case)* |
| C04 | `Tolerance policy examples` | Mandatory deliverable | *(name the test case)* |
| C05 | Write the `RunManifest` input, output and lineage fields | WP-019-T01 | *(name the test case)* |
| C06 | Make the protocol, baseline and analysis-plan references mandatory | WP-019-T02 | *(name the test case)* |
| C07 | Add the `EnvironmentManifest` hardware, driver, image and SBOM fields | WP-019-T03 | *(name the test case)* |
| C08 | Separate repeatability, reproducibility, robustness and replication as distinct types | WP-019-T04 | *(name the test case)* |
| C09 | Write the `ReproductionReport` tolerance and root-cause schema | WP-019-T05 | *(name the test case)* |
| C10 | Clean-Room Reproduction Pass | [ACC-19](../12_ACCEPTANCE_SCENARIOS/acc_19_clean_room_pass.md) — High | *(name the test case)* |
| C11 | Clean-Room Reproduction Failure | [ACC-20](../12_ACCEPTANCE_SCENARIOS/acc_20_clean_room_fail.md) — Critical | *(name the test case)* |

**11 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-014 is `ACCEPTED`; two distinct execution environments are
available; at least one local open-weight model is reachable for the
deterministic path.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `RunManifest`, `EnvironmentManifest`, `ReproductionReport` | All validate; protocol, baseline and analysis-plan references are **mandatory** on `RunManifest` | Schema validation output |
| 2 | **E2** | **Incomplete-manifest test.** Attempt a confirmatory claim from a run with a missing field | **Rejected.** The rejection names the missing field | Rejection transcript |
| 3 | **E0** | **Model-pinning mode test.** Confirm the manifest records *which* pinning mode was used — weight-file hash or capability fingerprint | Two modes, mutually exclusive, mandatory | Schema |
| 4 | **E2** | **R3 eligibility test.** Attempt an R3 deterministic-reproduction claim from a run pinned only by capability fingerprint | **Refused**, naming the structural constraint rather than a tolerance failure | Refusal transcript |
| 5 | E1 | Run the same job twice on the same machine (**repeatability**) | Identical within the repeatability tolerance | Repeatability report |
| 6 | E1 | Run from the manifest on a **different** machine (**reproducibility**) | Within the reproducibility tolerance; environment differences are enumerated | Reproducibility report |
| 7 | E1 | Perturb an analysis choice within its declared degrees of freedom (**robustness**) | The **conclusion** is assessed, not the number | Robustness report |
| 8 | E1 | Attempt the question by an independently chosen method (**replication**) | Reported as replication, with its own tolerance | Replication report |
| 9 | **E0** | **Type-separation test.** Confirm the four types cannot be reported under one field | A `ReproductionReport` naming no type is rejected | Rejection transcript |
| 10 | **E2** | **Post-hoc tolerance test.** Attempt to set or widen a tolerance after seeing the result | **Rejected.** The tolerance is part of the frozen manifest | Rejection transcript |
| 11 | E1 | Confirm `EnvironmentManifest` pins hardware, driver, image digest and SBOM | All four present; the image is a digest, never a tag | Environment record |
| 12 | **E1** | **Root-cause test.** Force one failure of each root-cause category and confirm the report classifies it | Six categories exercised; each classified correctly | Six reproduction reports |
| 13 | **E2** | **Clean-room test.** Reproduce from the manifest alone, with no access to the original workspace | Succeeds, or fails with a named missing input — never succeeds by accident | Clean-room transcript |
| 14 | E3 | Independent review of the tolerance policy examples for a tolerance wide enough to be unfalsifiable | Any found is a finding | `ReviewRecord` |

Step 13 is the real test of the manifest. Anything the reproducer needed and had
to ask for is a field the manifest is missing.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-019 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-019 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-019/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-019
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_019_run_environment_repro_contracts.acceptance.md) reaches the decision — issuance is not acceptance.

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
