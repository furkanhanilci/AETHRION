---
title: "WP-121 — Hypercare, Stabilisation and Programme Closure — Test Procedures"
aliases:
  - "WP-121 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilization.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w8
  - aethrion/effort/m
  - aethrion/gate/cutover
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-121 — Hypercare, Stabilisation and Programme Closure — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-121` |
| Work package | [`WP-121` — Hypercare, Stabilisation and Programme Closure](wp_121_hypercare_stabilization.md) |
| Companion | [acceptance criteria](wp_121_hypercare_stabilization.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Executive Sponsor / Assurance** — the independent verifier |
| Accountable owner | SRE Lead / Program Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-121` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | no | no scenario and not L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Cutover / Day-2 |

**Applicable layers: E0 · E1 · E2 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | SRE Lead / Program Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | SRE Lead / Program Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Executive Sponsor / Assurance | At completion |
| `WP-120` accepted output | Production Cutover and Go-Live Decision | Executive Sponsor / Program Lead | Before the first test case runs |

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
| C01 | `Hypercare log` | Mandatory deliverable | *(name the test case)* |
| C02 | `Incident/finding summary` | Mandatory deliverable | *(name the test case)* |
| C03 | `Production KPI baseline` | Mandatory deliverable | *(name the test case)* |
| C04 | `Day-2 handoff` | Mandatory deliverable | *(name the test case)* |
| C05 | `Program closure report` | Mandatory deliverable | *(name the test case)* |
| C06 | Establish the hypercare command centre, rota and decision cadence | WP-121-T01 | *(name the test case)* |
| C07 | Monitor the critical journeys, synthetic tests, queues, cost, security and evidence dashboards | WP-121-T02 | *(name the test case)* |
| C08 | Operate incident, finding, change-freeze and rollback authority | WP-121-T03 | *(name the test case)* |
| C09 | Run user support, feedback and knowledge capture | WP-121-T04 | *(name the test case)* |
| C10 | Verify the SLO, error budget and quality KPI baseline | WP-121-T05 | *(name the test case)* |
| C11 | Sign the exit review and the Day-2 owner handoff | WP-121-T06 | *(name the test case)* |

**11 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Exit criteria fixed first** | **E0** | Inspect the criteria before hypercare begins | Observables and thresholds declared in advance | Criteria |
| **TC-02** Undefined exit | **E2** | Attempt to begin hypercare with no exit criteria | **Refused** — otherwise hypercare ends when everyone is tired | Refusal transcript |
| **TC-03** Command centre | **E1** | Establish the rota and decision cadence | Every hour covered; the cadence is scheduled | Rota · calendar |
| **TC-04** Critical journeys | **E1** | Monitor the declared critical journeys | Each observed continuously with synthetic checks | Monitoring record |
| **TC-05** Synthetic tests | **E1** | Run the golden-path synthetic research and engineering runs | Both complete on schedule | Synthetic results |
| **TC-06** Synthetic failure | **E2** | Fail a synthetic run | Alerts within the declared window | Alert record |
| **TC-07** Queue and cost watch | **E1** | Observe queues, budget and assurance wait | All within thresholds, or an action is recorded | Dashboard snapshots |
| **TC-08** Evidence dashboard | **E1** | Observe the integrity dashboard | Projection lag, orphaned anchors and coverage fraction all watched | Dashboard snapshot |
| **TC-09** Incident handling | **E1** | Run an incident to closure | Contain → recover → learn → close; each step recorded | Incident record |
| **TC-10** **Rollback as normal** | **E1** | Exercise rollback authority during hypercare | Executed as a normal response, **not as an incident escalation** | Rollback record |
| **TC-11** Change freeze | **E1** | Apply and lift a change freeze | Both recorded with authority and reason | Freeze record |
| **TC-12** Reconciliation | **E1** | Run each reconciliation runbook once | All complete; divergences recorded | Reconciliation reports |
| **TC-13** User support | **E1** | Handle real user feedback | Each item triaged with an owner and a disposition | Support log |
| **TC-14** **Knowledge capture** | **E1** | Capture what the operators learned | Written into runbooks and the vault **before the rota disperses** | Knowledge records |
| **TC-15** Uncaptured learning | **E2** | Attempt exit with open knowledge items | Refused — the difference between an organisation that learned and a person who did | Refusal transcript |
| **TC-16** **SLO baseline** | **E1** | Establish the SLO and error-budget baseline | Measured over the declared window, not asserted | Baseline record |
| **TC-17** **Quality KPI baseline** | **E1** | Establish the anti-metric baseline | **G10 reversal rate, acceptance-despite-adversarial-rejection and decision-time distribution** all measured | Baseline record |
| **TC-18** Degenerate baseline | **E2** | Detect a baseline drawn from too few observations | Flagged — a baseline established badly makes drift undetectable for a year | Flag record |
| **TC-19** **Exit review** | **E1** | Hold the exit review against the criteria | Verdict recorded; **extending hypercare is a reachable outcome** | Exit record |
| **TC-20** **Named handoff** | **E1** | Hand off to Day-2 | A **named owner** accepts; open items transfer with owners and expiries | Handoff record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-121 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-121 --gate Cutover,Day-2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-121/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-121
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_121_hypercare_stabilization.acceptance.md) reaches the decision — issuance is not acceptance.

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
