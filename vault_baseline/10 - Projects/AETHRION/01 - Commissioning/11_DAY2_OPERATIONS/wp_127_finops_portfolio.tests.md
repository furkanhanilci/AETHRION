---
title: "WP-127 — FinOps, Capacity and Portfolio Review Rhythm — Test Procedures"
aliases:
  - "WP-127 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-127_finops_portfolio.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g0
  - aethrion/gate/g4
  - aethrion/gate/g8
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-127 — FinOps, Capacity and Portfolio Review Rhythm — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-127` |
| Work package | [`WP-127` — FinOps, Capacity and Portfolio Review Rhythm](wp_127_finops_portfolio.md) |
| Companion | [acceptance criteria](wp_127_finops_portfolio.acceptance.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Internal Audit / Assurance** — the independent verifier |
| Accountable owner | FinOps Lead / Research Director |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-127` |

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
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Day-2 |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | FinOps Lead / Research Director | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | FinOps Lead / Research Director | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Internal Audit / Assurance | At completion |
| `WP-100` accepted output | Cost Ledger, Budget Envelopes and FinOps | FinOps Lead | Before the first test case runs |
| `WP-117` accepted output | Performance, Capacity and Load Commissioning | Capacity Engineering Lead | Before the first test case runs |
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
| C01 | `Monthly FinOps report` | Mandatory deliverable | *(name the test case)* |
| C02 | `Invoice cases` | Mandatory deliverable | *(name the test case)* |
| C03 | `Portfolio decision records` | Mandatory deliverable | *(name the test case)* |
| C04 | `Capacity forecast` | Mandatory deliverable | *(name the test case)* |
| C05 | `Optimization backlog` | Mandatory deliverable | *(name the test case)* |
| C06 | Run the invoice, provider, compute and storage reconciliation | WP-127-T01 | *(name the test case)* |
| C07 | Produce the project and outcome budget variance and forecast | WP-127-T02 | *(name the test case)* |
| C08 | Analyse model/agent fan-out and the expected value of verification | WP-127-T03 | *(name the test case)* |
| C09 | Update the capacity, headroom and queue-wait plan | WP-127-T04 | *(name the test case)* |
| C10 | Record the stop/pivot decision for low-value, high-cost projects | WP-127-T05 | *(name the test case)* |
| C11 | Trigger the annual cost policy benchmark and reopen | WP-127-T06 | *(name the test case)* |
| C12 | Budget Hard Stop | [ACC-09](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) — Critical | *(name the test case)* |
| C13 | Provider Invoice Variance | [ACC-29](../12_ACCEPTANCE_SCENARIOS/acc_29_invoice_variance.md) — Medium | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Invoice reconciliation** | **E1** | Reconcile provider, compute and storage invoices | Variance computed against the ledger | Reconciliation report |
| **TC-02** Variance case | **E2** | Exceed the variance threshold | A case opens **with an owner** | Variance case |
| **TC-03** Unowned variance | **E2** | Leave one unassigned | Refused | Refusal transcript |
| **TC-04** Budget variance | **E1** | Compute project and outcome variance | Reported per project and per outcome class | Variance report |
| **TC-05** **Forecast** | **E1** | Produce the forecast | States its assumptions; compares against the envelope | Forecast |
| **TC-06** Assumption-free forecast | **E2** | Produce one with unstated assumptions | Refused | Refusal transcript |
| **TC-07** **Fan-out analysis** | **E1** | Analyse model and agent fan-out cost | Council review and sweeps costed separately from base work | Fan-out report |
| **TC-08** **Expected value of verification** | **E1** | Measure verification cost against defects caught | **Both reported**; the ratio stated | EV report |
| **TC-09** Naive optimisation | **E2** | Attempt to reduce assurance capacity on the EV number alone | **Refused** — `00_PROGRAM/08` protects the pool because this calculation always favours cutting it | Refusal transcript |
| **TC-10** **Quality-adjusted cost** | **E1** | Compare model profiles on production data | A cheaper model producing more rework is **exposed** | Comparison report |
| **TC-11** Feedback to routing | **E1** | Feed the numbers to WP-045's ordering | The router's quality-adjusted rule uses production data | Routing record |
| **TC-12** **Queue capacity** | **E1** | Update the capacity and queue-wait plan | Assurance wait and headroom projected | Capacity plan |
| **TC-13** **Human quota in the forecast** | **E2** | Forecast throughput growth exceeding the human decision quota | **Refused, or the growth plan is reduced** | Refusal · revised plan |
| **TC-14** **Stop decision** | **E1** | Apply the stop condition to a low-value, high-cost project | The decision is **taken and recorded** with its evidence | `DecisionRecord` |
| **TC-15** Sunk-cost pressure | **E2** | Apply the stop condition where substantial work exists | The condition still applies; sunk cost is **not** a counter-argument | Decision record |
| **TC-16** Pivot | **E1** | Apply a pivot condition | Recorded with the reason; the original project closes cleanly | Pivot record |
| **TC-17** No stop ever | **E2** | Detect a period with no stop or pivot decision across the portfolio | **Reviewed** — a portfolio where nothing is ever stopped is not being managed | Review record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-127 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-127 --gate Day-2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-127/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-127
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_127_finops_portfolio.acceptance.md) reaches the decision — issuance is not acceptance.

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
