# WP-111 — Reliability, Event and FinOps Acceptance Package — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-111` |
| Work package | [`WP-111` — Reliability, Event and FinOps Acceptance Package](WP-111_reliability_finops_acceptance.md) |
| Companion | [acceptance criteria](WP-111_reliability_finops_acceptance.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **FinOps / Control Plane Reviewer** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-111` |

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
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Commissioning |

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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | FinOps / Control Plane Reviewer | At completion |
| `WP-040` accepted output | Workflow Replay, Versioning and Failure Test Suite | Platform Assurance Lead | Before the first test case runs |
| `WP-053` accepted output | Kueue Queue, Quota and Priority Policy | Compute Platform Lead | Before the first test case runs |
| `WP-083` accepted output | ExperimentBatch and Staged Execution | Scientific Engineering Lead | Before the first test case runs |
| `WP-100` accepted output | Cost Ledger, Budget Envelopes and FinOps | FinOps Lead | Before the first test case runs |
| `WP-109` accepted output | Acceptance Scenario Registry and Harness | Platform Assurance Lead | Before the first test case runs |

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
| C01 | `Reliability/FinOps scenario results` | Mandatory deliverable | *(name the test case)* |
| C02 | `Fault injection report` | Mandatory deliverable | *(name the test case)* |
| C03 | `SLO/cost evidence` | Mandatory deliverable | *(name the test case)* |
| C04 | `Owner sign-off` | Mandatory deliverable | *(name the test case)* |
| C05 | Run the ACC-09–14 and ACC-29/33/34/35 fixtures | WP-111-T01 | *(name the test case)* |
| C06 | Inject budget, provider, worker, event and queue faults | WP-111-T02 | *(name the test case)* |
| C07 | Verify the state RPO, duplicate-effect, DLQ and cost ledger assertions | WP-111-T03 | *(name the test case)* |
| C08 | Measure the runbook and alert response | WP-111-T04 | *(name the test case)* |
| C09 | Produce the reliability/FinOps dossier and sign-off | WP-111-T05 | *(name the test case)* |
| C10 | Budget Hard Stop | [ACC-09](../12_ACCEPTANCE_SCENARIOS/ACC-09_budget_hard_stop.md) — Critical | *(name the test case)* |
| C11 | Provider Invoice Variance | [ACC-29](../12_ACCEPTANCE_SCENARIOS/ACC-29_invoice_variance.md) — Medium | *(name the test case)* |
| C12 | Kueue Preemption | [ACC-33](../12_ACCEPTANCE_SCENARIOS/ACC-33_kueue_preemption.md) — High | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Fixtures and RC | E0 | Reset fixtures; bind to one release candidate | One digest across all scenarios | RC binding |
| **TC-02** **Budget hard stop** (`ACC-09`) | **E2** | Drive spend to the hard limit | **No new expensive work opens**; the workflow pauses **without losing state** | Pause transcript |
| **TC-03** Budget resume | **E1** | Raise the envelope and resume | Continues from where it paused; no work repeated | Resume transcript |
| **TC-04** **Provider outage** (`ACC-10`/`11`) | **E2** | Remove a model provider | Fails over to an **admitted** profile or **fails closed** — never silently to an unqualified model | Failover record |
| **TC-05** Provider partial | **E2** | Return malformed provider responses | Retried, then failed cleanly; no partial output treated as complete | Transcript |
| **TC-06** **Duplicate event** (`ACC-12`) | **E2** | Deliver one event twice | **Exactly one** business effect; the duplicate acknowledged and audited | Effect count |
| **TC-07** **Worker loss** (`ACC-13`) | **E2** | Kill workers mid-activity | Activities retry elsewhere; no duplicate external effect | Recovery trace |
| **TC-08** **Workflow deployment** (`ACC-14`) | **E2** | Deploy changed workflow code against open executions | Executions continue via version markers; **no nondeterminism error** | Replay transcript |
| **TC-09** **Preemption** (`ACC-33`) | **E1** | Preempt a checkpointing workload | Checkpoint written; resumed; no item runs twice | Resume transcript |
| **TC-10** Preemption without checkpoint | **E2** | Preempt a workload declaring none | **Refused** | Refusal transcript |
| **TC-11** **DLQ repair** (`ACC-34`) | **E2** | Poison, route to DLQ, correct and replay | No consumer loop; causation preserved; processed once | Repair transcript |
| **TC-12** **Partial tool failure** (`ACC-35`) | **E2** | Have a tool succeed externally and fail to return | Reconciliation runs; the effect is **recorded as uncertain with an owner** if it cannot be resolved | Reconciliation record |
| **TC-13** Partial failure double-effect | **E2** | Retry after a partial failure | The idempotency key prevents a second effect | Effect count |
| **TC-14** **RPO measurement** | **E1** | Kill the primary mid-write and recover | **Workflow-state RPO measured as 0**; the number is recorded | Measurement |
| **TC-15** State integrity | **E1** | Run the integrity queries after every fault | Referential closure holds throughout | Integrity reports |
| **TC-16** **Invoice variance** (`ACC-29`) | **E1** | Reconcile a provider invoice against the ledger | Variance computed; a case opens above threshold **with an owner** | Variance case |
| **TC-17** Unowned variance | **E2** | Leave a variance unassigned | Refused | Refusal transcript |
| **TC-18** **Alert response** | **E1** | Trigger each declared alert in these scenarios | Each reaches its owner; **response time measured** | Response log |
| **TC-19** **Runbook execution** | **E1** | Execute the relevant runbooks under fault | Each completes; gaps recorded | Runbook reports |
| **TC-20** Dossier and sign-off | **E1** | Produce the reliability/FinOps dossier | Every result, evidence and residual risk present; owner sign-off | Dossier |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-111 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-111 --gate Commissioning \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-111/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-111
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-111_reliability_finops_acceptance.acceptance.md) reaches the decision — issuance is not acceptance.

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
