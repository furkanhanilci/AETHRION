---
title: "WP-119 — Controlled Pilot and Cutover Rehearsal — Test Procedures"
aliases:
  - "WP-119 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-119_pilot_cutover_rehearsal.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w7
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-119 — Controlled Pilot and Cutover Rehearsal — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-119` |
| Work package | [`WP-119` — Controlled Pilot and Cutover Rehearsal](wp_119_pilot_cutover_rehearsal.md) |
| Companion | [acceptance criteria](wp_119_pilot_cutover_rehearsal.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board / Independent Observer** — the independent verifier |
| Accountable owner | Program Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-119` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Commissioning |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Program Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Program Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Commissioning Board / Independent Observer | At completion |
| `WP-115` accepted output | Full System Regression and Commissioning Dossier | Platform Assurance Lead | Before the first test case runs |
| `WP-116` accepted output | Resilience, Chaos and Failure-Injection Commissioning | SRE Lead | Before the first test case runs |
| `WP-117` accepted output | Performance, Capacity and Load Commissioning | Capacity Engineering Lead | Before the first test case runs |
| `WP-118` accepted output | Operational Readiness, On-Call and Runbook Simulation | SRE Lead | Before the first test case runs |

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
| C01 | `Pilot dossier` | Mandatory deliverable | *(name the test case)* |
| C02 | `Cutover rehearsal log` | Mandatory deliverable | *(name the test case)* |
| C03 | `Usability/ops findings` | Mandatory deliverable | *(name the test case)* |
| C04 | `Rollback proof` | Mandatory deliverable | *(name the test case)* |
| C05 | `Go/no-go recommendation` | Mandatory deliverable | *(name the test case)* |
| C06 | Define the pilot selection criteria and apply data minimisation | WP-119-T01 | *(name the test case)* |
| C07 | Run a G0–G10 pilot on production-equivalent RC, configuration and data volume | WP-119-T02 | *(name the test case)* |
| C08 | Measure the operations, decision and assurance SLAs and human usability | WP-119-T03 | *(name the test case)* |
| C09 | Rehearse the cutover runbook: freeze, migration, smoke, abort and rollback | WP-119-T04 | *(name the test case)* |
| C10 | Convert pilot feedback into a correction package | WP-119-T05 | *(name the test case)* |
| C11 | Produce the final rehearsal report and the go/no-go recommendation | WP-119-T06 | *(name the test case)* |
| C12 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C13 | Complete Project Audit Export | [ACC-40](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) — Critical | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Selection criteria | E0 | Inspect the pilot criteria | Low risk, realistic, and the data-minimisation rule stated | Criteria |
| **TC-02** **Data minimisation** | **E2** | Attempt to run the pilot on unminimised production-equivalent data | **Refused** | Refusal transcript |
| **TC-03** Production-equivalent RC | **E1** | Confirm the pilot runs on the real RC, configuration and data volume | All three equivalent; differences documented | Environment record |
| **TC-04** **Full G0–G10 pilot** | **E1** | Run the pilot project end to end | Eleven `GateRecord`s; a publication package; a G10 scan | Record set |
| **TC-05** **Operations SLA** | **E1** | Measure operational response during the pilot | Within target; recorded as numbers | SLA measurements |
| **TC-06** **Decision SLA** | **E1** | Measure human decision latency | Within target; the attention quota was not exceeded | SLA measurements |
| **TC-07** **Assurance SLA** | **E1** | Measure review and reproduction turnaround | Within target; the assurance queue did not grow without bound | SLA measurements |
| **TC-08** **Usability** | **E1** | Have a person complete the decision path under time pressure | Completed; friction points recorded | Usability record |
| **TC-09** Cutover rehearsal — freeze | **E1** | Rehearse the change freeze | Applied; the exception path works | Freeze record |
| **TC-10** Cutover rehearsal — migration | **E1** | Rehearse migration and promotion | Completes; integrity queries pass | Migration record |
| **TC-11** Cutover rehearsal — smoke | **E1** | Run the smoke and integrity tests | All pass on the promoted RC | Smoke report |
| **TC-12** **Abort rehearsal** | **E1** | **Abort the cutover midway** | The abort completes; the system returns to a known state | Abort transcript |
| **TC-13** **Rollback rehearsal** | **E1** | Roll back after promotion | Prior state restored; integrity queries pass; nothing lost | Rollback transcript |
| **TC-14** Abort thresholds | **E0** | Inspect the abort criteria | Thresholds and decision owners **explicit**, not judgement calls | Criteria |
| **TC-15** Abort authority | **E1** | Exercise the abort decision | The named holder can act without the sponsor's consent (WP-001) | Decision record |
| **TC-16** **Correction package** | **E1** | Convert pilot feedback into corrections | Each has an owner, a package reference and a re-test | Correction package |
| **TC-17** Feedback as backlog | **E2** | Attempt to close the pilot with feedback recorded only as a list | Refused | Refusal transcript |
| **TC-18** **Recommendation** | **E1** | Produce the go/no-go recommendation | Reasons recorded; **`no-go` is reachable** | Recommendation |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-119 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-119 --gate Cutover \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-119/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-119
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_119_pilot_cutover_rehearsal.acceptance.md) reaches the decision — issuance is not acceptance.

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
