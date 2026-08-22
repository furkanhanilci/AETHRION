# WP-093 — Human Decision Queue and Evidence-Delta UI — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-093` |
| Work package | [`WP-093` — Human Decision Queue and Evidence-Delta UI](WP-093_decision_queue_ui.md) |
| Companion | [acceptance criteria](WP-093_decision_queue_ui.acceptance.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Project Decision Owner / Accessibility Reviewer** — the independent verifier |
| Accountable owner | Governance Product Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-093` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 2 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Governance Product Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Governance Product Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Project Decision Owner / Accessibility Reviewer | At completion |
| `WP-004` accepted output | Human Decision, SLA, Delegation and Escalation Policy | Project Decision Owner | Before the first test case runs |
| `WP-018` accepted output | Claim, Evidence, Review and Decision Schemas | Evidence Platform Lead | Before the first test case runs |
| `WP-038` accepted output | Human Update, Cancellation and Compensation Semantics | Control Plane Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-089` accepted output | DisagreementCase and Evidence-Weighted Arbitration | Assurance Lead / Arbiter | Before the first test case runs |
| `WP-091` accepted output | Lab Cockpit Information Architecture and Application Shell | Product/Experience Lead | Before the first test case runs |

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
| C01 | `Decision Queue UI` | Mandatory deliverable | *(name the test case)* |
| C02 | `Evidence-delta component` | Mandatory deliverable | *(name the test case)* |
| C03 | `Rationale forms` | Mandatory deliverable | *(name the test case)* |
| C04 | `Delegation/escalation views` | Mandatory deliverable | *(name the test case)* |
| C05 | `Decision audit export` | Mandatory deliverable | *(name the test case)* |
| C06 | Write the decision inbox, filters, escalation and ownership views | WP-093-T01 | *(name the test case)* |
| C07 | Design the frozen evidence snapshot, delta and dissent summary | WP-093-T02 | *(name the test case)* |
| C08 | Apply the rationale rubric and required-field validation | WP-093-T03 | *(name the test case)* |
| C09 | Add delegation scope and expiry plus the non-delegable banner | WP-093-T04 | *(name the test case)* |
| C10 | Bind MFA re-authentication, signing and update idempotency | WP-093-T05 | *(name the test case)* |
| C11 | Write the decision history, revoke and supersede views | WP-093-T06 | *(name the test case)* |
| C12 | Human Approval Forgery | [ACC-25](../12_ACCEPTANCE_SCENARIOS/ACC-25_human_approval_forgery.md) — Critical | *(name the test case)* |
| C13 | Approval, Delegation and Exception Expiry | [ACC-26](../12_ACCEPTANCE_SCENARIOS/ACC-26_approval_expiry.md) — Critical | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Inbox | **E1** | Open the decision queue | Filters, ownership, escalation state and SLA visible | Screenshot |
| **TC-02** Frozen snapshot | **E1** | Open a decision | The evidence snapshot is the one the decision binds to, marked frozen | Screenshot |
| **TC-03** **Evidence delta** | **E1** | Re-present an object whose evidence changed | **What changed** is shown, not the full package again | Delta view |
| **TC-04** Unchanged re-presentation | **E2** | Re-present an unchanged object | Marked unchanged; the standing approval is still valid (WP-004) | Screenshot |
| **TC-05** Stale approval | **E2** | Change evidence behind an approved object | The standing approval is **invalidated** and shown as such | Invalidation record |
| **TC-06** **Dissent** | **E1** | Open a decision with a minority reviewer position | Dissent is **shown on the surface**, not compressed into a summary | Screenshot |
| **TC-07** Adversarial counterexample | **E1** | Open a decision where falsification succeeded | The counterexample is prominent | Screenshot |
| **TC-08** Residual risk | **E1** | Inspect the decision surface | Residual risk, its owner and its expiry are visible | Screenshot |
| **TC-09** **Rationale required** | **E2** | Submit a decision with no rationale | **Refused** | Refusal transcript |
| **TC-10** Rubric | **E1** | Submit a rationale | Validated against the rubric's required fields | Validation record |
| **TC-11** **Non-delegable banner** | **E1** | Open a G8, publication, retraction or cutover decision | The banner states it is non-delegable **before** any attempt | Four screenshots |
| **TC-12** Delegation attempt | **E2** | Attempt to delegate one | Refused (WP-004) | Refusal transcript |
| **TC-13** Delegation scope | **E1** | Create a valid delegation | Scope and expiry shown; use outside either is refused | Delegation record |
| **TC-14** **MFA at signing** | **E2** | Sign without re-authentication | Refused | Refusal transcript |
| **TC-15** Idempotency | **E1** | Replay a submitted decision | Applied once (WP-038) | Effect count |
| **TC-16** **Defer** | **E1** | Defer a decision | A first-class outcome; the object returns to the queue with the deferral recorded | Decision record |
| **TC-17** History and revoke | **E1** | Revoke a decision | The revocation takes effect at the point of use; history is preserved | Revoke transcript |
| **TC-18** SLA expiry | **E2** | Let a material decision's SLA expire | Fails closed to *not approved*; escalation fires | Expiry transcript |
| **TC-19** **Rubber-stamp signals** | **E1** | Complete ten decisions | Decision time, sections opened, and later reversal are all emitted (WP-004) | Telemetry sample |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-093 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-093 --gate G8 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-093/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-093
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-093_decision_queue_ui.acceptance.md) reaches the decision — issuance is not acceptance.

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
