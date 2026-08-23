---
title: "WP-157 — Reproduction Determinism and Model Execution Fingerprint — Test Procedures"
aliases:
  - "WP-157 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-157_reproduction_determinism_and_fingerprint.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/g7
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-157 — Reproduction Determinism and Model Execution Fingerprint — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-157` |
| Work package | [`WP-157` — Reproduction Determinism and Model Execution Fingerprint](wp_157_reproduction_determinism_and_fingerprint.md) |
| Companion | [acceptance criteria](wp_157_reproduction_determinism_and_fingerprint.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Assurance Lead / Independent Grader** — the independent verifier |
| Accountable owner | Reproducibility Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-157` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 / G7 |
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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead / Independent Grader | At completion |
| `WP-019` accepted output | Run, Environment and Reproduction Schemas | Experiment Platform Lead | Before the first test case runs |
| `WP-084` accepted output | Clean-Room Reproduction Environment | Reproducibility Lead | Before the first test case runs |
| `WP-085` accepted output | Repeatability, Reproducibility, Robustness and Replication Pipeline | Reproducibility Lead | Before the first test case runs |

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
| C01 | `ModelExecutionFingerprint` | Mandatory deliverable | *(name the test case)* |
| C02 | `Five-level reproduction taxonomy` | Mandatory deliverable | *(name the test case)* |
| C03 | `Three-zone leakage suite` | Mandatory deliverable | *(name the test case)* |
| C04 | Define `ModelExecutionFingerprint` and capture it on every contributing invocation | WP-157-T01 | *(name the test case)* |
| C05 | Record retry and fallback history as part of the fingerprint | WP-157-T02 | *(name the test case)* |
| C06 | Define the five reproduction levels and bind them to protocol declaration | WP-157-T03 | *(name the test case)* |
| C07 | Refuse EXACT for hosted black-box execution | WP-157-T04 | *(name the test case)* |
| C08 | Implement distributional reproduction with pre-declared run count and interval | WP-157-T05 | *(name the test case)* |
| C09 | Harden the three-zone separation against cache, credential and layer inheritance | WP-157-T06 | *(name the test case)* |
| C10 | Bind fingerprints into the reproduction package and the claim consistency report | WP-157-T07 | *(name the test case)* |
| C11 | Producer to Evaluator Leakage | [ACC-113](../12_ACCEPTANCE_SCENARIOS/acc_113_producer_evaluator_leakage.md) — Critical | *(name the test case)* |
| C12 | Reproduction Environment Lineage | [ACC-114](../12_ACCEPTANCE_SCENARIOS/acc_114_reproduction_in_producer_environment_hardened.md) — Critical | *(name the test case)* |
| C13 | Missing Model Execution Fingerprint | [ACC-115](../12_ACCEPTANCE_SCENARIOS/acc_115_missing_model_execution_fingerprint.md) — Critical | *(name the test case)* |
| C14 | Distributional Reproduction for a Hosted Model | [ACC-116](../12_ACCEPTANCE_SCENARIOS/acc_116_distributional_hosted_model_reproduction.md) — High | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-084 supplies the three zones; WP-085 supplies the reproduction pipeline; a hosted model endpoint and a locally-controlled one are both reachable so the level taxonomy can be exercised at both ends.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `ModelExecutionFingerprint` and the five-level reproduction taxonomy | Both validate; retry and fallback history are required fields | Validator output |
| 2 | **E2** | **No fingerprint, no run.** Execute a contributing invocation with fingerprint capture disabled | The run fails rather than recording an incomplete result — ACC-115 | Failure transcript |
| 3 | **E1** | **Failover is visible.** Force a silent provider failover mid-run | It appears in the retry and fallback history | Fingerprint |
| 4 | **E2** | **Failover invalidates exact.** Attempt to assert `EXACT` for that run | Refused | Refusal transcript |
| 5 | **E2** | **Hosted black box.** Attempt `EXACT` against a hosted black-box model | Refused; the reason names the substrate — ACC-116 | Refusal transcript |
| 6 | E1 | Assert `SNAPSHOT` against a provider-pinned snapshot | Permitted while the snapshot exists | Reproduction record |
| 7 | **E1** | **Distributional.** Execute the pre-declared number of runs and compute the distribution | Within the declared interval; the claim is `DISTRIBUTIONAL` | Run set + summary |
| 8 | **E2** | **No post-hoc widening.** Attempt to widen the interval after seeing the spread | Refused and recorded as an attempt | Refusal transcript |
| 9 | **E2** | **No post-hoc runs.** Attempt to add runs after seeing the spread | Refused | Refusal transcript |
| 10 | **E2** | **Cache leakage.** Attempt producer-to-evaluator access through a shared cache | Denied — ACC-113 | Denial transcript |
| 11 | **E2** | **Credential leakage.** Attempt it through an inherited credential | Denied | Denial transcript |
| 12 | **E2** | **Layer leakage.** Attempt it through a warm container layer | Denied | Denial transcript |
| 13 | **E1** | **Canary sweep.** Scan every producer artifact, log and trace for the evaluator canary | Zero occurrences | Scan report |
| 14 | **E2** | **Lineage decides.** Attempt reproduction in five environments of decreasing producer lineage | Only the genuinely independent one yields reproducibility — ACC-114 | Five status records |
| 15 | **E4** | **Agentless execution.** Run the reproduction package with no agent context available | Executes and produces comparison artifacts | Run record |
| 16 | E3 | Independent grading of the reproduction in a third environment | The grader shares no workspace, cache or credential with either other zone | Grader record |

Cases 10 to 12 are the ones that matter and the ones a zone diagram will not
catch. None of a shared cache, an inherited credential or a warm layer looks like
a boundary violation in a log, which is why each is attempted explicitly rather
than inferred from the configuration.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-157   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-157 --gate G7 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-157/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-157
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_157_reproduction_determinism_and_fingerprint.acceptance.md) reaches the decision — issuance is not acceptance.

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
