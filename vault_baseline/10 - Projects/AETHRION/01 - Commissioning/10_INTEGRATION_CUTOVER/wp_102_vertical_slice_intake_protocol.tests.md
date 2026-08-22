---
title: "WP-102 — Vertical Slice 1 — Intake through Protocol Freeze — Test Procedures"
aliases:
  - "WP-102 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-102_vertical_slice_intake_protocol.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g1
  - aethrion/gate/g2
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-102 — Vertical Slice 1 — Intake through Protocol Freeze — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-102` |
| Work package | [`WP-102` — Vertical Slice 1 — Intake through Protocol Freeze](wp_102_vertical_slice_intake_protocol.md) |
| Companion | [acceptance criteria](wp_102_vertical_slice_intake_protocol.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Assurance / Project Decision Owner** — the independent verifier |
| Accountable owner | Research Workflow Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-102` |

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
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Research Workflow Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Research Workflow Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance / Project Decision Owner | At completion |
| `WP-034` accepted output | G0 Intake and G1 Charter Workflows | Research Operations Lead | Before the first test case runs |
| `WP-035` accepted output | G2 Protocol, G3 Literature and G4 Baseline Workflows | Scientific Workflow Lead | Before the first test case runs |
| `WP-056` accepted output | OPA Policy Platform and Bundle Distribution | Policy Platform Lead | Before the first test case runs |
| `WP-091` accepted output | Lab Cockpit Information Architecture and Application Shell | Product/Experience Lead | Before the first test case runs |
| `WP-092` accepted output | Project Workspace and G0–G10 Gate Timeline | Experience Lead | Before the first test case runs |
| `WP-093` accepted output | Human Decision Queue and Evidence-Delta UI | Governance Product Lead | Before the first test case runs |
| `WP-100` accepted output | Cost Ledger, Budget Envelopes and FinOps | FinOps Lead | Before the first test case runs |
| `WP-101` accepted output | Service Catalogue, SLOs and Alert/Runbook Binding | SRE Lead | Before the first test case runs |

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
| C01 | `Vertical slice dossier` | Mandatory deliverable | *(name the test case)* |
| C02 | `R1/R3 project histories` | Mandatory deliverable | *(name the test case)* |
| C03 | `Trace/audit/decision evidence` | Mandatory deliverable | *(name the test case)* |
| C04 | `Integration findings` | Mandatory deliverable | *(name the test case)* |
| C05 | Prepare the R1 and R3 synthetic project fixtures | WP-102-T01 | *(name the test case)* |
| C06 | Start the intake from the cockpit | WP-102-T02 | *(name the test case)* |
| C07 | Verify the risk, execution and independence policy decisions | WP-102-T03 | *(name the test case)* |
| C08 | Run the charter, SLA, delegation and protocol freeze | WP-102-T04 | *(name the test case)* |
| C09 | Check the budget reservation, audit and telemetry chain | WP-102-T05 | *(name the test case)* |
| C10 | Test the revise, block and reopen paths | WP-102-T06 | *(name the test case)* |
| C11 | Planner Self-Approval Attempt | [ACC-06](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) — Critical | *(name the test case)* |
| C12 | Human Approval Forgery | [ACC-25](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) — Critical | *(name the test case)* |
| C13 | Approval, Delegation and Exception Expiry | [ACC-26](../12_ACCEPTANCE_SCENARIOS/acc_26_approval_expiry.md) — Critical | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Fixtures | E0 | Prepare realistic R1 and R3 project fixtures | Both are realistic, not minimal; their risk dimensions are documented | Fixture set |
| **TC-02** Intake from the cockpit | **E1** | Start an R1 intake through the UI | `IntakeRecord` created; correlation established (WP-096) | Intake record |
| **TC-03** Incomplete intake | **E2** | Submit with no purpose, owner or class | Refused per field (WP-034) | Three refusals |
| **TC-04** **Profile composition** | **E1** | Bind risk, execution and independence profiles at G1 | All three bind; the composed `ControlPlan` names the controls each implies | `ControlPlan` |
| **TC-05** Profile disagreement | **E2** | Construct a case where two profiles imply conflicting controls | The **stricter** applies; the conflict is recorded, not silently resolved | Conflict record |
| **TC-06** R1 charter | **E1** | Complete the R1 charter with a falsifiable outcome | G1 passes | Gate record |
| **TC-07** Untestable outcome | **E2** | Submit a charter with no falsifying observation | G1 **fails** | Gate record |
| **TC-08** **R3 blocked** | **E1** | Take the R3 project to G1 | **`BLOCKED`** with the ADR-001 declaration naming the missing external verifier | Gate record · declaration |
| **TC-09** R3 forced through | **E2** | Attempt to proceed past the R3 block | Refused | Refusal transcript |
| **TC-10** SLA and delegation | **E1** | Leave the G1 decision past its SLA | Fails closed; escalates (WP-004) | Expiry transcript |
| **TC-11** Non-delegable | **E2** | Attempt to delegate the G1 decision where non-delegable | Refused | Refusal transcript |
| **TC-12** Protocol freeze | **E1** | Freeze the protocol at G2 | Hashed, signed, gate record emitted | Manifest |
| **TC-13** **Budget reservation** | **E1** | Reach the point where compute may open | Budget is **reserved before** anything is dispatched (WP-053, WP-100) | Reservation record |
| **TC-14** Hard limit | **E2** | Reach the hard budget limit | No new work opens; the workflow **pauses without losing state** | Pause transcript |
| **TC-15** **Separate gate records** | **E1** | Close G0, G1 and G2 in one session | **Three separate records** in Temporal history | History extract |
| **TC-16** **Revise path** | **E1** | Fail G1, correct, resubmit | Both attempts recorded; the second passes | Two gate records |
| **TC-17** **Reopen path** | **E2** | Change the protocol after G2 | G2 reopens; downstream is invalidated (WP-008) | Reopen transcript |
| **TC-18** Audit chain | **E1** | Export the audit for the slice | The full chain verifies from the standalone verifier (WP-099) | Verification transcript |
| **TC-19** Telemetry chain | **E1** | Inspect the trace | One correlation identifier from cockpit command to gate record | Trace |
| **TC-20** **Findings against upstream** | **E1** | Record every defect this slice exposes | Each is filed **against the package it is in**, not against this one | Finding register |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-102 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-102 --gate G0–G10 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-102/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-102
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_102_vertical_slice_intake_protocol.acceptance.md) reaches the decision — issuance is not acceptance.

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
