# WP-140 — Service Liveness Monitoring and Dead-Man's Switch — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-140` |
| Work package | [`WP-140` — Service Liveness Monitoring and Dead-Man's Switch](WP-140_service_liveness_dead_mans_switch.md) |
| Companion | [acceptance criteria](WP-140_service_liveness_dead_mans_switch.acceptance.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Metascience Lead** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-140` |

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
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | SRE Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | SRE Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Metascience Lead | At completion |
| `WP-101` accepted output | Service Catalogue, SLOs and Alert/Runbook Binding | SRE Lead | Before the first test case runs |
| `WP-131` accepted output | Notification Broker Foundation | Platform Security Lead | Before the first test case runs |
| `WP-134` accepted output | Escalation and Paging | SRE Lead | Before the first test case runs |

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
| C01 | Inventory of periodic jobs and their expected intervals | WP-140-T01 | *(name the test case)* |
| C02 | Emit a success signal (heartbeat) for every job | WP-140-T02 | *(name the test case)* |
| C03 | Alarm when no signal arrives (self-hosted monitor) | WP-140-T03 | *(name the test case)* |
| C04 | Distinguish partial success: `SUCCEEDED` vs `PARTIAL` | WP-140-T04 | *(name the test case)* |
| C05 | Bind alarm escalation to the WP-134 chain | WP-140-T05 | *(name the test case)* |
| C06 | Liveness dashboard with last-run times | WP-140-T06 | *(name the test case)* |
| C07 | Notification Broker Unavailable During an Escalating Condition | [ACC-42](../12_ACCEPTANCE_SCENARIOS/ACC-42_notification_broker_outage.md) — High | *(name the test case)* |
| C08 | Escalation Timeout and Dead-Man's Switch | [ACC-43](../12_ACCEPTANCE_SCENARIOS/ACC-43_escalation_and_dead_mans_switch.md) — Critical | *(name the test case)* |

**8 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Job inventory** | **E0** | Inventory every periodic job | **Complete** — impact scans, status sweeps, control tests, calibration, drift analysis, digests, chain verification, drills | Inventory |
| **TC-02** Unregistered job | **E2** | Add a scheduled job with no registry entry | **Detected** — an unwatched periodic job is an unwatched control | Detection record |
| **TC-03** Expected interval | E0 | Inspect the registry | Every job declares its expected interval and tolerance | Registry |
| **TC-04** **Heartbeat** | **E1** | Complete a job | A success signal is emitted with the job identity and the run outcome | Heartbeat record |
| **TC-05** **Absence alarm** | **E2** | Suppress a job entirely | **Alarm fires** within the declared tolerance | Alarm record |
| **TC-06** Failure alarm | **E1** | Fail a job | Alarms — but distinguishably from absence | Two alarm records |
| **TC-07** **Monitor independence** | **E2** | Take down the infrastructure the jobs run on | The monitor **still alarms** — it is self-hosted and independent | Alarm record |
| **TC-08** Shared-fate monitor | **E2** | Attempt to run the monitor on the watched infrastructure | Refused — a monitor that goes silent with its jobs is not a monitor | Refusal transcript |
| **TC-09** **`SUCCEEDED` vs `PARTIAL`** | **E1** | Complete a job that processed only part of its input | Reported **`PARTIAL`**, never `SUCCEEDED` | Run record |
| **TC-10** Silent truncation | **E2** | Reproduce finding **H1**'s pattern — a capped read reported as complete | **Detected**: the run is `PARTIAL` and the shortfall is named | Detection record |
| **TC-11** Partial escalation | **E1** | Let a job report `PARTIAL` repeatedly | Escalates — repeated partial success is a defect, not a status | Escalation record |
| **TC-12** **Escalation binding** | **E1** | Fire an absence alarm | Escalates through WP-134's chain and **promotes if unacknowledged** | Escalation record |
| **TC-13** Alarm to nobody | **E2** | Configure an alarm with no owner | Refused | Refusal transcript |
| **TC-14** **Monitor's own liveness** | **E2** | Stop the monitor itself | Its absence is detected by an independent means — **the watcher is watched** | Detection record |
| **TC-15** Recovery | **E1** | Restore a suppressed job | The alarm clears and the recovery is recorded | Recovery record |
| **TC-16** Alarm history | **E1** | Inspect alarm history | Every absence, its duration and its resolution recorded | History |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-140 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-140 --gate Day-2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-140/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-140
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-140_service_liveness_dead_mans_switch.acceptance.md) reaches the decision — issuance is not acceptance.

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
