# WP-036 — G5 Execute through G9 Publish Workflows — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-036` |
| Work package | [`WP-036` — G5 Execute through G9 Publish Workflows](WP-036_g5_g9_workflows.md) |
| Companion | [acceptance criteria](WP-036_g5_g9_workflows.acceptance.md) |
| Workstream | `04_CONTROL_EVENT` |
| Approval authority | **Assurance Lead / Decision Owner** — the independent verifier |
| Accountable owner | Workflow Engineering Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-036` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5–G9 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Workflow Engineering Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Workflow Engineering Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead / Decision Owner | At completion |
| `WP-004` accepted output | Human Decision, SLA, Delegation and Escalation Policy | Project Decision Owner | Before the first test case runs |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-008` accepted output | G0–G10 Gate and Assurance Policy | Research Director | Before the first test case runs |
| `WP-019` accepted output | Run, Environment and Reproduction Schemas | Experiment Platform Lead | Before the first test case runs |
| `WP-032` accepted output | ProjectLifecycle Workflow Skeleton | Workflow Engineering Lead | Before the first test case runs |
| `WP-033` accepted output | Gate Service and GateRecord Evaluation | Control Plane Lead | Before the first test case runs |
| `WP-035` accepted output | G2 Protocol, G3 Literature and G4 Baseline Workflows | Scientific Workflow Lead | Before the first test case runs |

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
| C01 | `G5–G9 workflows` | Mandatory deliverable | *(name the test case)* |
| C02 | `Review/repro integration contracts` | Mandatory deliverable | *(name the test case)* |
| C03 | `Decision update flow` | Mandatory deliverable | *(name the test case)* |
| C04 | `Publication transition` | Mandatory deliverable | *(name the test case)* |
| C05 | Write the G5 `RunBatch` dispatch, checkpoint and stop flow | WP-036-T01 | *(name the test case)* |
| C06 | Bind the G6 frozen review package and its dispositions | WP-036-T02 | *(name the test case)* |
| C07 | Establish the G7 reproduction request, result and reopen flow | WP-036-T03 | *(name the test case)* |
| C08 | Apply the G8 evidence-delta human decision update | WP-036-T04 | *(name the test case)* |
| C09 | Bind the G9 citation, provenance and security release checklist | WP-036-T05 | *(name the test case)* |
| C10 | Add cancellation, compensation and supersession | WP-036-T06 | *(name the test case)* |
| C11 | Strong Counter-Test | [ACC-08](../12_ACCEPTANCE_SCENARIOS/ACC-08_strong_counter_test.md) — Critical | *(name the test case)* |
| C12 | Clean-Room Reproduction Pass | [ACC-19](../12_ACCEPTANCE_SCENARIOS/ACC-19_clean_room_pass.md) — High | *(name the test case)* |
| C13 | Clean-Room Reproduction Failure | [ACC-20](../12_ACCEPTANCE_SCENARIOS/ACC-20_clean_room_fail.md) — Critical | *(name the test case)* |
| C14 | Publication Completeness | [ACC-30](../12_ACCEPTANCE_SCENARIOS/ACC-30_publication_completeness.md) — Critical | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Run dispatch | E1 | Dispatch a `RunBatch` against a frozen protocol | Runs execute; each carries a complete `RunManifest` | Batch record |
| **TC-02** Mid-run parameter change | **E2** | Change a threshold during a batch | **The batch stops.** It is not adjusted and continued | Stop transcript |
| **TC-03** Checkpoint and resume | E1 | Kill a batch mid-flight and resume | Resumes from checkpoint; no duplicate runs | Resume transcript |
| **TC-04** Stop rule | **E1** | Trigger a declared stop rule | The batch stops and records which rule fired | Stop record |
| **TC-05** Incomplete manifest | **E2** | Attempt to freeze a claim from a run with a missing manifest field | Refused, naming the field | Refusal transcript |
| **TC-06** Frozen review package | **E1** | Assemble a G6 package and diff it against the producer's workspace | **Zero producer-trace artifacts** | Packet diff |
| **TC-07** Reviewer independence | **E2** | Assign a reviewer who has seen the trace | Refused at the gate, re-evaluated at gate time (WP-007) | Refusal transcript |
| **TC-08** G7a reproduction | E1 | Reproduce deterministically from the manifest | Within the declared tolerance, or `CHALLENGED` | Reproduction report |
| **TC-09** G7b replication | E1 | Replicate distributionally | Reported **as replication**, with its own tolerance | Replication report |
| **TC-10** Type collapse | **E2** | Attempt to report both under one verdict | Refused | Refusal transcript |
| **TC-11** G8 evidence delta | **E1** | Change evidence behind an approved claim and re-present | The decision surface shows **what changed**, and the standing approval is invalidated | Delta record |
| **TC-12** G8 non-delegable | **E2** | Attempt to delegate the G8 decision | Refused | Refusal transcript |
| **TC-13** G9 citation audit | **E2** | Publish with an unresolvable citation | Refused | Refusal transcript |
| **TC-14** G9 security release | **E2** | Publish content exposing a protected locator | Refused, naming the boundary | Refusal transcript |
| **TC-15** Supersession | E1 | Supersede a published claim | Prior version reachable; lineage intact; nothing rewritten | Supersession chain |
| **TC-16** Cancellation | E1 | Cancel mid-G5 with an open external effect | Compensation runs (WP-038); leases revoked | Compensation trace |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-036 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-036 --gate G5–G9 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-036/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-036
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-036_g5_g9_workflows.acceptance.md) reaches the decision — issuance is not acceptance.

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
