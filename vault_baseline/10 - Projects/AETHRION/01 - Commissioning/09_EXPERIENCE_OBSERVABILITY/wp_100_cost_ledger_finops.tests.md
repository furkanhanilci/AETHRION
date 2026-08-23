---
title: "WP-100 — Cost Ledger, Budget Envelopes and FinOps — Test Procedures"
aliases:
  - "WP-100 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/gate/g8
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-100 — Cost Ledger, Budget Envelopes and FinOps — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-100` |
| Work package | [`WP-100` — Cost Ledger, Budget Envelopes and FinOps](wp_100_cost_ledger_finops.md) |
| Companion | [acceptance criteria](wp_100_cost_ledger_finops.acceptance.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Project Decision Owner / Internal Audit** — the independent verifier |
| Accountable owner | FinOps Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-100` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | FinOps Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | FinOps Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Project Decision Owner / Internal Audit | At completion |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |
| `WP-013` accepted output | Project, Task, Role and Skill Contract Schemas | Control Plane Lead | Before the first test case runs |
| `WP-015` accepted output | Event Envelope, Subject and Schema Taxonomy | Event Platform Lead | Before the first test case runs |
| `WP-016` accepted output | PolicyDecision, Control and Exception Schemas | Policy Platform Lead | Before the first test case runs |
| `WP-025` accepted output | PostgreSQL HA and Registry Data Foundation | Database Platform Lead | Before the first test case runs |
| `WP-028` accepted output | NATS JetStream and Transactional Outbox Foundation | Event Platform Lead | Before the first test case runs |
| `WP-041` accepted output | LiteLLM Model Gateway Foundation | Model Platform Lead | Before the first test case runs |
| `WP-045` accepted output | Policy Router and Minimum-Sufficient Model Package | Model Platform Lead | Before the first test case runs |
| `WP-049` accepted output | Tool Registry and Tool Broker Core | Tool Platform Lead | Before the first test case runs |
| `WP-052` accepted output | Kubernetes Cluster and Node Pool Baseline | Platform Infrastructure Lead | Before the first test case runs |
| `WP-053` accepted output | Kueue Queue, Quota and Priority Policy | Compute Platform Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |
| `WP-096` accepted output | OpenTelemetry End-to-End Correlation Spine | Observability Lead | Before the first test case runs |

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
| C01 | `Cost Ledger` | Mandatory deliverable | *(name the test case)* |
| C02 | `Budget service` | Mandatory deliverable | *(name the test case)* |
| C03 | `Cost adapters` | Mandatory deliverable | *(name the test case)* |
| C04 | `Invoice reconciliation` | Mandatory deliverable | *(name the test case)* |
| C05 | `FinOps dashboard/runbook` | Mandatory deliverable | *(name the test case)* |
| C06 | `Token ledger categories` | Mandatory deliverable | *(name the test case)* |
| C07 | Establish the `BudgetEnvelope`, C0–C4 classes and the reservation API | WP-100-T01 | *(name the test case)* |
| C08 | Ingest gateway, Kueue, tool, storage and human cost events | WP-100-T02 | *(name the test case)* |
| C09 | Write estimate → reserve → commit → release plus retry and fan-out attribution | WP-100-T03 | *(name the test case)* |
| C10 | Integrate the 80% and 100% thresholds with Temporal pause and decision flows | WP-100-T04 | *(name the test case)* |
| C11 | Add provider invoice reconciliation and variance cases | WP-100-T05 | *(name the test case)* |
| C12 | Build the quality-adjusted cost/outcome dashboard and forecast | WP-100-T06 | *(name the test case)* |
| C13 | Budget Hard Stop | [ACC-09](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) — Critical | *(name the test case)* |
| C14 | Provider Invoice Variance | [ACC-29](../12_ACCEPTANCE_SCENARIOS/acc_29_invoice_variance.md) — Medium | *(name the test case)* |
| C15 | Discovery Search Stagnation | [ACC-59](../12_ACCEPTANCE_SCENARIOS/acc_59_discovery_search_stagnation.md) — High | *(name the test case)* |
| C16 | Token Ledger Classification | [ACC-100](../12_ACCEPTANCE_SCENARIOS/acc_100_token_ledger_classification.md) — High | *(name the test case)* |

**16 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Envelope and classes | E0 | Inspect the budget model | `BudgetEnvelope` and C0–C4 classes defined | Model |
| **TC-02** **Reserve before spend** | **E1** | Dispatch work | The reservation is taken **before** the first billable call | Reservation record |
| **TC-03** Unreserved spend | **E2** | Attempt a billable call with no reservation | **Refused** | Refusal transcript |
| **TC-04** Commit and release | **E1** | Complete work under budget | Committed actual; the unused reservation is released | Ledger entries |
| **TC-05** Ingest — model | **E1** | Complete a gateway call | Cost event ingested with correlation (WP-041) | Cost event |
| **TC-06** Ingest — compute | **E1** | Complete a Kueue workload | Cost ingested | Cost event |
| **TC-07** Ingest — tool and storage | **E1** | Perform a tool call and a storage write | Both ingested | Two events |
| **TC-08** **Ingest — human triage** | **E1** | Complete a human review and a decision | **Human time is ingested as a cost** | Cost event |
| **TC-09** **Fan-out attribution** | **E1** | Run a five-way fan-out | All five attributed to one reservation; **it is not extended** | Budget trace |
| **TC-10** **Retry attribution** | **E1** | Force retries | Drawn from the reservation; a retry storm **exhausts rather than extends** | Budget trace |
| **TC-11** **80% threshold** | **E1** | Cross 80% of an envelope | Warning fires; work continues | Alert record |
| **TC-12** **100% hard stop** | **E2** | Reach the hard limit | **No new expensive work opens**; the workflow **pauses without losing state** | Pause transcript |
| **TC-13** Hard-stop bypass | **E2** | Attempt to dispatch past the hard limit | Refused | Refusal transcript |
| **TC-14** Decision integration | **E1** | Reach the hard limit on a live project | A `DecisionRequest` reaches the owner (WP-093) | Decision record |
| **TC-15** **Outcome attribution** | **E1** | Complete a claim, a reproduction and a negative result | Each carries its cost | Three records |
| **TC-16** Negative-result cost | **E1** | Inspect the cost of work producing a negative result | **Visible and not labelled waste** | Dashboard |
| **TC-17** **Invoice reconciliation** | **E1** | Reconcile a provider invoice against the ledger | Variance computed; a case opens above the threshold | Variance case |
| **TC-18** Unowned variance | **E2** | Leave a variance case unassigned | Refused; every case carries an owner | Refusal transcript |
| **TC-19** Forecast | **E1** | Inspect the forecast | Projects spend against the envelope with its assumptions stated | Forecast |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-100 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-100 --gate G5,G8 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-100/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-100
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_100_cost_ledger_finops.acceptance.md) reaches the decision — issuance is not acceptance.

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
