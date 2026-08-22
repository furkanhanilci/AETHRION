---
title: "WP-098 — Grafana and the Six Operational Graphs — Test Procedures"
aliases:
  - "WP-098 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-098_grafana_six_graphs.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g0-g10
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-098 — Grafana and the Six Operational Graphs — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-098` |
| Work package | [`WP-098` — Grafana and the Six Operational Graphs](wp_098_grafana_six_graphs.md) |
| Companion | [acceptance criteria](wp_098_grafana_six_graphs.acceptance.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Service Owners / FinOps / Assurance** — the independent verifier |
| Accountable owner | Observability Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-098` |

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
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Observability Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Observability Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Service Owners / FinOps / Assurance | At completion |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-096` accepted output | OpenTelemetry End-to-End Correlation Spine | Observability Lead | Before the first test case runs |
| `WP-097` accepted output | Langfuse Model/Agent Tracing and Prompt Governance | AI Observability Lead | Before the first test case runs |

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
| C01 | `Grafana platform` | Mandatory deliverable | *(name the test case)* |
| C02 | `Six graph dashboards` | Mandatory deliverable | *(name the test case)* |
| C03 | `Alert rules` | Mandatory deliverable | *(name the test case)* |
| C04 | `Dashboard/alert ownership catalog` | Mandatory deliverable | *(name the test case)* |
| C05 | Establish the metric, log and trace stores and Grafana RBAC | WP-098-T01 | *(name the test case)* |
| C06 | Write the workflow, gate latency and blocker dashboard | WP-098-T02 | *(name the test case)* |
| C07 | Write the execution queue, sandbox and tool dashboard | WP-098-T03 | *(name the test case)* |
| C08 | Write the experiment, reproduction and evaluation quality dashboard | WP-098-T04 | *(name the test case)* |
| C09 | Write the literature, claim and impact integrity dashboard | WP-098-T05 | *(name the test case)* |
| C10 | Write the service/SLO/incident and cost/budget dashboard | WP-098-T06 | *(name the test case)* |
| C11 | Add alert routing, owners and runbook links | WP-098-T07 | *(name the test case)* |

**11 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Stores and RBAC | E0 | Inspect metric, log and trace stores | All three present with role separation | Configuration |
| **TC-02** Workflow graph | **E1** | Open the workflow dashboard | Gate latency, blocker counts and reopen rate visible | Screenshot |
| **TC-03** Execution graph | **E1** | Open the execution dashboard | Queue wait, sandbox utilisation, tool error rate visible | Screenshot |
| **TC-04** Experiment graph | **E1** | Open the experiment dashboard | Run outcomes, reproduction results and eval quality visible | Screenshot |
| **TC-05** **Integrity graph** | **E1** | Open the knowledge/evidence dashboard | Projection lag, orphaned anchors, **unmonitored source fraction**, queue depths and overwrite-detector firings all visible | Screenshot |
| **TC-06** Service graph | **E1** | Open the SLO dashboard | Per-service SLI, error budget and incident state visible | Screenshot |
| **TC-07** Cost graph | **E1** | Open the cost dashboard | Spend by project, run, role and outcome; forecast against envelope | Screenshot |
| **TC-08** **Rubber-stamp signal** | **E1** | Plot decision time against decision volume | **Both on one chart** — the failure signature is falling time with rising volume | Screenshot |
| **TC-09** **Assurance wait** | **E1** | Plot assurance queue wait | Visible with its threshold (`PR-04`) | Screenshot |
| **TC-10** **Reversal rate** | **E1** | Plot the G10 reversal rate | Visible over time | Screenshot |
| **TC-11** **Adversarial override** | **E1** | Plot acceptance despite adversarial rejection | Visible over time | Screenshot |
| **TC-12** Correlation | **E1** | Click through from a chart to a trace | Resolves via the correlation identifier (WP-096) | Transcript |
| **TC-13** **Alert owner** | **E2** | Define an alert with no owner | **Refused** | Refusal transcript |
| **TC-14** **Runbook link** | **E2** | Point an alert at a dead runbook link | Detected by the link checker | Detection record |
| **TC-15** **Every alert fires once** | **E1** | Trigger each declared alert | **Each is demonstrated firing** to its owner | Firing record per alert |
| **TC-16** Silent alert | **E2** | Include an alert whose condition is unreachable | Flagged — a rule that cannot fire is not an alert | Flag record |
| **TC-17** Data-class separation | **E2** | View a D3 dashboard with a D0 identity | Denied | Denial record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-098 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-098 --gate Platform \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-098/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-098
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_098_grafana_six_graphs.acceptance.md) reaches the decision — issuance is not acceptance.

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
