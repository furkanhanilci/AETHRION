---
title: "WP-108 — Retraction, Drift and Supersession Vertical Slice — Test Procedures"
aliases:
  - "WP-108 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-108_retraction_drift_vertical_slice.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-108 — Retraction, Drift and Supersession Vertical Slice — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-108` |
| Work package | [`WP-108` — Retraction, Drift and Supersession Vertical Slice](wp_108_retraction_drift_vertical_slice.md) |
| Companion | [acceptance criteria](wp_108_retraction_drift_vertical_slice.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Assurance / Eval Office / Decision Owner** — the independent verifier |
| Accountable owner | Knowledge Monitoring Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-108` |

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
| Target revision | The single commit every result is bound to | Knowledge Monitoring Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Monitoring Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance / Eval Office / Decision Owner | At completion |
| `WP-037` accepted output | G10 Temporal Schedules and Short ImpactScan Workflows | Knowledge Monitoring Lead | Before the first test case runs |
| `WP-042` accepted output | Capability Registry and Profile Lifecycle | Eval Office | Before the first test case runs |
| `WP-044` accepted output | Model Qualification and Admission Pipeline | Eval Office | Before the first test case runs |
| `WP-063` accepted output | Source Representation, Licence and Status Monitoring | Knowledge Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-090` accepted output | PublicationPackage, RO-Crate and Provenance Export | Provenance Curator | Before the first test case runs |
| `WP-095` accepted output | Claim/Evidence Explorer and Provenance Graph | Evidence Product Lead | Before the first test case runs |
| `WP-106` accepted output | Vertical Slice 5 — Human Decision, Publish and Monitor | Project Decision Owner | Before the first test case runs |

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
| C01 | `Impact vertical dossier` | Mandatory deliverable | *(name the test case)* |
| C02 | `ImpactCase set` | Mandatory deliverable | *(name the test case)* |
| C03 | `Affected-object accuracy report` | Mandatory deliverable | *(name the test case)* |
| C04 | `Supersession/re-evaluation records` | Mandatory deliverable | *(name the test case)* |
| C05 | Produce the retraction, correction, model, data, policy and incident fixtures | WP-108-T01 | *(name the test case)* |
| C06 | Run the schedule/event → `ImpactScan` and the graph query | WP-108-T02 | *(name the test case)* |
| C07 | Compare the computed affected claim/task/project/publication set against the expected set | WP-108-T03 | *(name the test case)* |
| C08 | Apply priority, SLA, owner and the provisional/challenged state | WP-108-T04 | *(name the test case)* |
| C09 | Perform re-review, reproduction, republication or a no-impact disposition | WP-108-T05 | *(name the test case)* |
| C10 | Test false-positive handling and duplicate-trigger idempotency | WP-108-T06 | *(name the test case)* |
| C11 | Retraction Impact | [ACC-04](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) — Critical | *(name the test case)* |
| C12 | Superseded Publication | [ACC-31](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) — High | *(name the test case)* |
| C13 | Model Snapshot Drift | [ACC-36](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) — Critical | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Fixtures | E0 | Prepare all six trigger fixtures | Retraction, correction, model, data, policy, incident | Fixture set |
| **TC-02** **Expected sets** | **E0** | Compute the expected affected set for each fixture, by hand | Six expected sets, each derived independently of the system | Expected-set document |
| **TC-03** **Retraction** | **E1** | Fire the retraction | Computed set **equals** the expected set | Comparison |
| **TC-04** **Correction** | **E1** | Fire the correction | Equals expected | Comparison |
| **TC-05** **Model revocation** | **E1** | Revoke a model snapshot | Equals expected, **including open tasks** — invariant 7 | Comparison |
| **TC-06** **Dataset change** | **E1** | Change a monitored dataset | Equals expected | Comparison |
| **TC-07** **Policy change** | **E1** | Publish a new policy bundle | Affected decisions re-evaluated; equals expected | Comparison |
| **TC-08** **Incident** | **E1** | Raise an incident signal | Equals expected | Comparison |
| **TC-09** Under-inclusion | **E2** | Seed a claim four derivation hops from the source | **Present in the computed set** | Detection transcript |
| **TC-10** Over-inclusion | **E2** | Seed an unrelated claim sharing a keyword | **Absent** from the computed set | Absence proof |
| **TC-11** Publication reach | **E1** | Retract a source cited by a published package | The **publication** is in the set, not only the claim | Impact list |
| **TC-12** **Coverage fraction** | **E1** | Run over the full registry | The report **states the monitorable fraction** and names what is outside it | Coverage report |
| **TC-13** Priority and SLA | **E1** | Open cases of differing severity | Each carries priority, SLA and owner | Case records |
| **TC-14** SLA breach | **E2** | Let a Critical case pass its SLA | Escalates | Escalation record |
| **TC-15** Claim state | **E1** | Process a retraction impact | The claim moves to `CHALLENGED`, not silently downgraded | Claim state |
| **TC-16** **Duplicate trigger** | **E2** | Fire the same retraction from two sources | **One case**, not two | Case count |
| **TC-17** Re-fire after dismissal | **E2** | Dismiss a case, then re-run the scan | **Does not reopen** — a dismissal is not a snooze | Scan output |
| **TC-18** Re-review path | **E1** | Resolve by re-review | Review runs; the disposition cites it | Disposition record |
| **TC-19** Reproduction path | **E1** | Resolve by re-reproduction | Certificate produced; claim state follows | Certificate |
| **TC-20** Republication path | **E1** | Resolve by superseding the publication | Prior version reachable | Supersession chain |
| **TC-21** **No-impact disposition** | **E1** | Resolve a case as no impact | Terminal state **with a reason** | Disposition record |
| **TC-22** Missed scan | **E2** | Suppress a scheduled scan | Alert fires (`PR-20`) | Alert record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-108 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-108 --gate G10 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-108/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-108
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_108_retraction_drift_vertical_slice.acceptance.md) reaches the decision — issuance is not acceptance.

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
