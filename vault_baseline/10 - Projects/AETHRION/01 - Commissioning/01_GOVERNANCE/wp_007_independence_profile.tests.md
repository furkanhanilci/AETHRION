---
title: "WP-007 — IndependenceProfile and Separation-of-Duties Policy — Test Procedures"
aliases:
  - "WP-007 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/01_GOVERNANCE/WP-007_independence_profile.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/m
  - aethrion/gate/g6
  - aethrion/gate/g7
  - aethrion/gate/g8
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-007 — IndependenceProfile and Separation-of-Duties Policy — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-007` |
| Work package | [`WP-007` — IndependenceProfile and Separation-of-Duties Policy](wp_007_independence_profile.md) |
| Companion | [acceptance criteria](wp_007_independence_profile.acceptance.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Internal Audit / Safety Owner** — the independent verifier |
| Accountable owner | Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-007` |

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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Internal Audit / Safety Owner | At completion |
| `WP-003` accepted output | Role Catalogue and RACI Baseline | Governance Lead | Before the first test case runs |
| `WP-005` accepted output | Research Risk and Assurance Profile | Safety & Governance Owner | Before the first test case runs |

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
| C01 | `IndependenceProfile rubric` | Mandatory deliverable | *(name the test case)* |
| C02 | `Eligibility matrix` | Mandatory deliverable | *(name the test case)* |
| C03 | `Conflict-of-interest declaration` | Mandatory deliverable | *(name the test case)* |
| C04 | `Violation response` | Mandatory deliverable | *(name the test case)* |
| C05 | Define the seven independence dimensions | WP-007-T01 | *(name the test case)* |
| C06 | Write the minimum required sets for R1, R2 and R3 | WP-007-T02 | *(name the test case)* |
| C07 | Identify the non-compensable dimensions and their blocker rules | WP-007-T03 | *(name the test case)* |
| C08 | Define the frozen-package and context-contamination controls | WP-007-T04 | *(name the test case)* |
| C09 | Design re-evaluation at assignment time and again at gate time | WP-007-T05 | *(name the test case)* |
| C10 | Planner Self-Approval Attempt | [ACC-06](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) — Critical | *(name the test case)* |
| C11 | Critical Reviewer Unavailable | [ACC-38](../12_ACCEPTANCE_SCENARIOS/acc_38_reviewer_unavailable.md) — High | *(name the test case)* |

**11 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-003 and WP-005 are `ACCEPTED`; ADR-001 is in force; a
frozen review packet can be constructed.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate the `IndependenceProfile` schema across all seven dimensions | Each dimension has a defined value domain and an evidence source | Schema validation output |
| 2 | E0 | Confirm the minimum required set for R1, R2 and R3 is stated per dimension | Three complete sets; none defined as "as much as practical" | Requirement matrix |
| 3 | E0 | Confirm the non-compensable list is a **list**, and each entry names its blocker | Non-empty; each entry maps to a hard refusal | Non-compensable list |
| 4 | **E2** | **Same-human test.** Assign producer and reviewer to one actor at R2 | Rejected, naming the human dimension | Rejection transcript |
| 5 | **E2** | **Same-model-family test.** Assign reviewer from the producer's model family at R3 | Rejected, naming the model-family dimension | Rejection transcript |
| 6 | **E2** | **Context-contamination test.** Give the reviewer access to the producer's working trace, then request a verdict | Rejected before the verdict is accepted, not after | Rejection transcript |
| 7 | **E2** | **Credential and data-path tests.** Share a credential, then share a data path | Each rejected separately and distinguishably | Transcript per dimension |
| 8 | **E2** | **Economic-interest test.** Assign a reviewer with a declared interest in the outcome | Rejected as non-compensable regardless of the other six being satisfied | Rejection transcript |
| 9 | **E2** | **Gate-time re-evaluation test.** Assign a valid reviewer, then grant them context **after** assignment, then reach the gate | The gate re-evaluates and **refuses**. Assignment-time validity does not survive | Re-evaluation transcript |
| 10 | E1 | Confirm the frozen-packet control: the reviewer's packet contains no producer trace | Packet diff against the producer's workspace shows zero trace artifacts | Frozen packet manifest |
| 11 | E1 | Confirm R3 with a solo operator produces `BLOCKED` under ADR-001, with the declaration attached | Blocked, and the declaration names the missing external verifier | Blocking transcript |
| 12 | E1 | Confirm an R2 assignment records its **declared partial** profile, naming which dimensions are unmet | The record states what is absent, not only what is present | `IndependenceProfile` record |
| 13 | E3 | Independent review of the non-compensable list | The reviewer proposes at least one dimension that should be non-compensable and is not | `ReviewRecord` |

Step 9 is the test that distinguishes a real implementation from a plausible one.
Steps 4–8 will pass in most designs; assignment-time-only checking passes 4–8 and
fails 9.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-007 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-007 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-007/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-007
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_007_independence_profile.acceptance.md) reaches the decision — issuance is not acceptance.

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
