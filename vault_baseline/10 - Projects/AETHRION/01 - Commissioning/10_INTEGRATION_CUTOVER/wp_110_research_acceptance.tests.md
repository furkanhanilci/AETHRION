---
title: "WP-110 — Research and Literature Acceptance Package — Test Procedures"
aliases:
  - "WP-110 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-110_research_acceptance.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-110 — Research and Literature Acceptance Package — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-110` |
| Work package | [`WP-110` — Research and Literature Acceptance Package](wp_110_research_acceptance.md) |
| Companion | [acceptance criteria](wp_110_research_acceptance.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Citation Auditor / Assurance** — the independent verifier |
| Accountable owner | Research Director |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-110` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Commissioning |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Research Director | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Research Director | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Citation Auditor / Assurance | At completion |
| `WP-103` accepted output | Vertical Slice 2 — Two-Way Literature and Set Freeze | Evidence Lead | Before the first test case runs |
| `WP-104` accepted output | Vertical Slice 3 — Baseline through Run to Claim/Evidence | Scientific Engineering Lead | Before the first test case runs |
| `WP-105` accepted output | Vertical Slice 4 — Blind Review, Arbitration and Clean-Room | Assurance Lead | Before the first test case runs |
| `WP-106` accepted output | Vertical Slice 5 — Human Decision, Publish and Monitor | Project Decision Owner | Before the first test case runs |
| `WP-108` accepted output | Retraction, Drift and Supersession Vertical Slice | Knowledge Monitoring Lead | Before the first test case runs |
| `WP-109` accepted output | Acceptance Scenario Registry and Harness | Platform Assurance Lead | Before the first test case runs |

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
| C01 | `ACC-01–08 results` | Mandatory deliverable | *(name the test case)* |
| C02 | `Research acceptance dossier` | Mandatory deliverable | *(name the test case)* |
| C03 | `Finding/disposition records` | Mandatory deliverable | *(name the test case)* |
| C04 | `Owner sign-off` | Mandatory deliverable | *(name the test case)* |
| C05 | Reset the ACC-01 to ACC-08 fixtures | WP-110-T01 | *(name the test case)* |
| C06 | Execute a controlled, non-parallel run on the same release candidate | WP-110-T02 | *(name the test case)* |
| C07 | Verify the expected Registry, Zotero, Ledger, Gate and Audit outcomes | WP-110-T03 | *(name the test case)* |
| C08 | Run critical-finding triage, reproduction and correction | WP-110-T04 | *(name the test case)* |
| C09 | Produce the research acceptance dossier and obtain owner sign-off | WP-110-T05 | *(name the test case)* |
| C10 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C11 | Strong Counter-Test | [ACC-08](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) — Critical | *(name the test case)* |
| C12 | Governed Versus Ungoverned Research Harness | [ACC-80](../12_ACCEPTANCE_SCENARIOS/acc_80_governed_versus_ungoverned_harness.md) — Medium | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Fixture reset | **E1** | Reset ACC-01–08 fixtures | Deterministic starting state; isolation verified | Reset record |
| **TC-02** Same RC | **E0** | Confirm every run binds to one release candidate | One digest across all eight | RC binding |
| **TC-03** Serial execution | **E1** | Run without parallelism | No shared-state interference; each result attributable | Execution log |
| **TC-04** **ACC-01 human seed** | **E1** | Run the seed scenario | Source resolves to one record; **no personal Zotero field modified** | Scenario result |
| **TC-05** **ACC-02 write-back** | **E1** | Run agent write-back | Proposal recorded; a human applies it; the agent cannot apply | Scenario result |
| **TC-06** **ACC-03 duplicate collision** | **E2** | Run the duplicate scenario | Two distinct works **not merged**; queued | Scenario result |
| **TC-07** **ACC-04 retraction impact** | **E1** | Run the retraction scenario | Every dependent claim reached, including derived ones | Scenario result |
| **TC-08** **ACC-05 prompt injection** | **E2** | Run the injection scenario through the full ingest path | Tagged untrusted, wrapped in the boundary marker, **agent scope unchanged** | Scenario result · audit |
| **TC-09** ACC-05 at the MCP surface | **E2** | Retrieve the injected abstract through the read-only MCP tools | Arrives inside the boundary marker — the gap the Bridge documents is closed | Output sample |
| **TC-10** **ACC-06 self-approval** | **E2** | Attempt producer self-approval **through every available path** | **Every path refused**, including the cockpit, the API and any delegation | One refusal per path |
| **TC-11** ACC-06 under solo operation | **E1** | Attempt the same with one operator holding several roles | Refused by separation constraint, or **`BLOCKED` with the ADR-001 declaration** | Refusal · declaration |
| **TC-12** **ACC-07 order bias** | **E1** | Run the order-bias scenario | Finding order randomised; the seed recorded; verdicts compared across orders | Scenario result |
| **TC-13** **ACC-08 counter-test** | **E1** | Run the strong counter-test | The counter-evidence branch ran; the counter-test was executed; its result **acted on** | Scenario result |
| **TC-14** ACC-08 negative outcome | **E1** | Have the counter-test disconfirm | The claim moves state; it is not quietly retained | Claim state |
| **TC-15** **Critical finding triage** | **E2** | Attempt to close a Critical finding as a probable false positive | **Refused** — a reproducer result is required | Refusal transcript |
| **TC-16** Reproduction of a finding | **E1** | Reproduce a Critical finding | Independent reproduction record | Reproduction record |
| **TC-17** Correction and retest | **E1** | Correct and re-run | Passes on the **same** RC or a new RC is declared | Retest result |
| **TC-18** Dossier | **E1** | Produce the research acceptance dossier | Every scenario's result, evidence and disposition present | Dossier |
| **TC-19** Owner sign-off | **E1** | Obtain sign-off | Named owner; MFA; residual risks listed with owners and expiries | Sign-off record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-110 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-110 --gate Commissioning \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-110/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-110
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_110_research_acceptance.acceptance.md) reaches the decision — issuance is not acceptance.

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
