---
title: "WP-117 — Performance, Capacity and Load Commissioning — Test Procedures"
aliases:
  - "WP-117 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-117_performance_capacity.tests.md"
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

# WP-117 — Performance, Capacity and Load Commissioning — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-117` |
| Work package | [`WP-117` — Performance, Capacity and Load Commissioning](wp_117_performance_capacity.md) |
| Companion | [acceptance criteria](wp_117_performance_capacity.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **SRE / FinOps / Assurance** — the independent verifier |
| Accountable owner | Capacity Engineering Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-117` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Commissioning |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Capacity Engineering Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Capacity Engineering Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | SRE / FinOps / Assurance | At completion |
| `WP-053` accepted output | Kueue Queue, Quota and Priority Policy | Compute Platform Lead | Before the first test case runs |
| `WP-096` accepted output | OpenTelemetry End-to-End Correlation Spine | Observability Lead | Before the first test case runs |
| `WP-098` accepted output | Grafana and the Six Operational Graphs | Observability Lead | Before the first test case runs |
| `WP-100` accepted output | Cost Ledger, Budget Envelopes and FinOps | FinOps Lead | Before the first test case runs |
| `WP-101` accepted output | Service Catalogue, SLOs and Alert/Runbook Binding | SRE Lead | Before the first test case runs |
| `WP-115` accepted output | Full System Regression and Commissioning Dossier | Platform Assurance Lead | Before the first test case runs |

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
| C01 | `Load test suite/results` | Mandatory deliverable | *(name the test case)* |
| C02 | `Capacity model` | Mandatory deliverable | *(name the test case)* |
| C03 | `Bottleneck/tuning report` | Mandatory deliverable | *(name the test case)* |
| C04 | `Cost/headroom forecast` | Mandatory deliverable | *(name the test case)* |
| C05 | `Capacity sign-off` | Mandatory deliverable | *(name the test case)* |
| C06 | Define the workload mix, concurrency, data size and fan-out envelope | WP-117-T01 | *(name the test case)* |
| C07 | Write the service, queue and end-to-end load tests | WP-117-T02 | *(name the test case)* |
| C08 | Measure bottlenecks across the database, NATS, Temporal, models, tools and sandboxes | WP-117-T03 | *(name the test case)* |
| C09 | Tune autoscaling, connection pools, caches and backpressure | WP-117-T04 | *(name the test case)* |
| C10 | Model the assurance queue and the human SLA capacity | WP-117-T05 | *(name the test case)* |
| C11 | Produce the cost curve, headroom and capacity plan | WP-117-T06 | *(name the test case)* |

**11 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Approved envelope** | **E0** | Inspect the workload envelope | Mix, concurrency, data size and **fan-out assumption** all stated and approved | Envelope |
| **TC-02** Unapproved envelope | **E2** | Run a capacity test with no approved envelope | Results **not accepted as evidence** | Refusal transcript |
| **TC-03** Service load | **E1** | Load each tier-1 service to the envelope | SLOs met; latency distributions recorded | Load report |
| **TC-04** Queue load | **E1** | Load the intake, gate, event, model, broker, registry and experiment queues | Each meets its wait-time target | Queue report |
| **TC-05** End-to-end | **E1** | Run the full research journey at envelope concurrency | Completes within the declared end-to-end target | Journey report |
| **TC-06** **Bottleneck identification** | **E1** | Measure across database, NATS, Temporal, models, tools and sandboxes | The **binding constraint is identified and named** | Bottleneck report |
| **TC-07** **Backpressure** | **E1** | Exceed the envelope | The system **queues and signals**; it does not fail or silently degrade | Backpressure record |
| **TC-08** Silent degradation | **E2** | Detect any path that degrades quality under load | Each is a finding — degrading quality under load is the failure mode research cannot tolerate | Finding record |
| **TC-09** Autoscaling | **E1** | Apply the envelope with autoscaling | Scales within declared bounds; the capacity reserve is untouched | Scaling record |
| **TC-10** Connection pools | **E2** | Saturate pools | Queues or refuses cleanly; the database is never driven to its own limit | Pool record |
| **TC-11** **Fan-out multiplier** | **E1** | Apply the envelope with council review and a parameter sweep active | The multiplied load is within the envelope's stated fan-out assumption | Fan-out report |
| **TC-12** Fan-out cap | **E2** | Exceed the declared fan-out | Refused before dispatch (WP-045, WP-053) | Refusal transcript |
| **TC-13** **Assurance queue model** | **E1** | Model review and reproduction capacity at envelope throughput | The assurance queue **does not grow without bound** | Queue model |
| **TC-14** Assurance starvation | **E2** | Saturate with research work | Assurance is admitted from its reserve and is not preempted | Admission record |
| **TC-15** **Human SLA capacity** | **E1** | Model decision requests against the human attention quota | The quota is **not exceeded** at envelope throughput; if it is, the envelope is reduced | Capacity model |
| **TC-16** **Cost curve** | **E1** | Measure cost against throughput | The curve is produced; the envelope's cost at full load is stated | Cost curve |
| **TC-17** Headroom | **E1** | Compute headroom | Stated as a number against each binding constraint | Headroom report |
| **TC-18** Capacity plan | **E1** | Produce the plan | Names the next constraint to be hit and at what growth | Capacity plan |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-117 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-117 --gate Commissioning \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-117/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-117
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_117_performance_capacity.acceptance.md) reaches the decision — issuance is not acceptance.

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
