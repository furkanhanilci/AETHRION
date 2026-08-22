---
title: "WP-044 — Model Qualification and Admission Pipeline — Test Procedures"
aliases:
  - "WP-044 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-044_model_qualification_admission.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g1
  - aethrion/gate/g5
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-044 — Model Qualification and Admission Pipeline — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-044` |
| Work package | [`WP-044` — Model Qualification and Admission Pipeline](wp_044_model_qualification_admission.md) |
| Companion | [acceptance criteria](wp_044_model_qualification_admission.acceptance.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Admission Board / Safety / FinOps** — the independent verifier |
| Accountable owner | Eval Office |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-044` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Eval Office | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Eval Office | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Admission Board / Safety / FinOps | At completion |
| `WP-041` accepted output | LiteLLM Model Gateway Foundation | Model Platform Lead | Before the first test case runs |
| `WP-042` accepted output | Capability Registry and Profile Lifecycle | Eval Office | Before the first test case runs |
| `WP-043` accepted output | Role-Based Model and Skill Evaluation, and Golden Set Management | Eval Office | Before the first test case runs |

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
| C01 | `Qualification pipeline` | Mandatory deliverable | *(name the test case)* |
| C02 | `Admission dossier` | Mandatory deliverable | *(name the test case)* |
| C03 | `CapabilityProfile update` | Mandatory deliverable | *(name the test case)* |
| C04 | `Regression schedule` | Mandatory deliverable | *(name the test case)* |
| C05 | `Ejection procedure` | Mandatory deliverable | *(name the test case)* |
| C06 | Resolve the qualification request against an immutable model snapshot | WP-044-T01 | *(name the test case)* |
| C07 | Run the role evaluation, safety, latency and cost batches | WP-044-T02 | *(name the test case)* |
| C08 | Compute the baseline comparison and the incremental value | WP-044-T03 | *(name the test case)* |
| C09 | Verify the data and provider contract and its retention terms | WP-044-T04 | *(name the test case)* |
| C10 | Write the Admission Board decision workflow and the profile expiry | WP-044-T05 | *(name the test case)* |
| C11 | Bind the regression/drift schedule to the revocation path | WP-044-T06 | *(name the test case)* |
| C12 | Primary Model Provider Outage | [ACC-10](../12_ACCEPTANCE_SCENARIOS/acc_10_provider_outage.md) — High | *(name the test case)* |
| C13 | Model Snapshot Drift | [ACC-36](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) — Critical | *(name the test case)* |
| C14 | Evaluation Set Contamination | [ACC-37](../12_ACCEPTANCE_SCENARIOS/acc_37_eval_contamination.md) — Critical | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Snapshot resolution | **E1** | Open a qualification request | It resolves to an **immutable snapshot or a recorded capability fingerprint**, never a moving alias | Request record |
| **TC-02** Alias request | **E2** | Request qualification of an alias | Refused | Refusal transcript |
| **TC-03** Role evaluation batch | E1 | Run the WP-043 sets for the target role | Scores recorded against the eval manifest version | Scorecard |
| **TC-04** Safety batch | E1 | Run the adversarial set | Results recorded; failures itemised | Safety report |
| **TC-05** Latency and cost | E1 | Measure both under representative load | Distributions, not means | Measurement |
| **TC-06** **Shadow run** | **E1** | Run in shadow alongside the incumbent on real tasks | Output recorded and **unused**; disagreement rate with the incumbent reported | Shadow report |
| **TC-07** Shadow bypass | **E2** | Attempt admission with no shadow evidence | Refused | Refusal transcript |
| **TC-08** **Incremental value** | **E1** | Compare against the incumbent baseline | Improvement stated as a number with an interval, not as "better" | Comparison |
| **TC-09** No-improvement case | **E2** | Submit a model that matches the incumbent | Not admitted — parity does not justify a switch | Decision record |
| **TC-10** Retention terms | **E2** | Qualify a provider whose retention conflicts with D3 handling | **Not admitted for D3**, whatever its quality scores | Decision record |
| **TC-11** Admission decision | E1 | Run the board workflow | Decision recorded with actor, evidence references and scope | `DecisionRecord` |
| **TC-12** Profile expiry set | **E0** | Inspect the resulting profile | Carries an expiry; an admission with none is refused | Profile |
| **TC-13** Regression schedule | E1 | Confirm a recurring regression run is scheduled | Scheduled with an owner | Schedule entry |
| **TC-14** Drift ejection | **E2** | Fail a scheduled regression | Ejection path runs; open tasks receive an impact event (WP-042) | Ejection transcript |
| **TC-15** Contamination ejection | **E2** | Detect the canary in a model's trace | Ejected regardless of scores | Ejection transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-044 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-044 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-044/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-044
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_044_model_qualification_admission.acceptance.md) reaches the decision — issuance is not acceptance.

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
