---
title: "WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor — Test Procedures"
aliases:
  - "WP-106 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-106_vertical_slice_decision_publish_monitor.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-106 — Vertical Slice 5 — Human Decision, Publish and Monitor — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-106` |
| Work package | [`WP-106` — Vertical Slice 5 — Human Decision, Publish and Monitor](wp_106_vertical_slice_decision_publish_monitor.md) |
| Companion | [acceptance criteria](wp_106_vertical_slice_decision_publish_monitor.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Citation Auditor / Safety / Archivist** — the independent verifier |
| Accountable owner | Project Decision Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-106` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 6 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Project Decision Owner | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Project Decision Owner | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Citation Auditor / Safety / Archivist | At completion |
| `WP-037` accepted output | G10 Temporal Schedules and Short ImpactScan Workflows | Knowledge Monitoring Lead | Before the first test case runs |
| `WP-074` accepted output | Obsidian Projection, Link Integrity and Knowledge Write-Back | Knowledge Platform Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-080` accepted output | Claim–Citation Entailment, Scope and Locator Audit | Citation Audit Lead | Before the first test case runs |
| `WP-085` accepted output | Repeatability, Reproducibility, Robustness and Replication Pipeline | Reproducibility Lead | Before the first test case runs |
| `WP-089` accepted output | DisagreementCase and Evidence-Weighted Arbitration | Assurance Lead / Arbiter | Before the first test case runs |
| `WP-090` accepted output | PublicationPackage, RO-Crate and Provenance Export | Provenance Curator | Before the first test case runs |
| `WP-093` accepted output | Human Decision Queue and Evidence-Delta UI | Governance Product Lead | Before the first test case runs |
| `WP-095` accepted output | Claim/Evidence Explorer and Provenance Graph | Evidence Product Lead | Before the first test case runs |
| `WP-099` accepted output | WORM Audit Ledger and Independent Export | Internal Audit Platform Lead | Before the first test case runs |
| `WP-105` accepted output | Vertical Slice 4 — Blind Review, Arbitration and Clean-Room | Assurance Lead | Before the first test case runs |

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
| C01 | `Decision/publish/monitor dossier` | Mandatory deliverable | *(name the test case)* |
| C02 | `DecisionRecord` | Mandatory deliverable | *(name the test case)* |
| C03 | `PublicationPackage` | Mandatory deliverable | *(name the test case)* |
| C04 | `ImpactCase/Supersession` | Mandatory deliverable | *(name the test case)* |
| C05 | `Audit export` | Mandatory deliverable | *(name the test case)* |
| C06 | Run the evidence-delta, decision rationale and MFA update | WP-106-T01 | *(name the test case)* |
| C07 | Perform the publication completeness, licence and privacy checks | WP-106-T02 | *(name the test case)* |
| C08 | Produce the RO-Crate, signature, archive and release event | WP-106-T03 | *(name the test case)* |
| C09 | Trigger a retraction, a correction and a model drift signal | WP-106-T04 | *(name the test case)* |
| C10 | Create the `ImpactCase`, claim challenge, owner queue item and superseding package | WP-106-T05 | *(name the test case)* |
| C11 | Verify the full chain in the audit export | WP-106-T06 | *(name the test case)* |
| C12 | Retraction Impact | [ACC-04](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) — Critical | *(name the test case)* |
| C13 | Human Approval Forgery | [ACC-25](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) — Critical | *(name the test case)* |
| C14 | Publication Completeness | [ACC-30](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) — Critical | *(name the test case)* |
| C15 | Superseded Publication | [ACC-31](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) — High | *(name the test case)* |
| C16 | Model Snapshot Drift | [ACC-36](../12_ACCEPTANCE_SCENARIOS/acc_36_model_snapshot_drift.md) — Critical | *(name the test case)* |
| C17 | Complete Project Audit Export | [ACC-40](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) — Critical | *(name the test case)* |

**17 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Evidence delta** | **E1** | Present the G8 decision after evidence changed | **What changed** is shown, not the whole package | Delta view |
| **TC-02** Dissent visible | **E1** | Present a decision with a minority position and a successful counterexample | Both prominent on the surface | Screenshot |
| **TC-03** Residual risk | **E1** | Inspect the decision surface | Residual risk, owner and expiry shown | Screenshot |
| **TC-04** **Rationale required** | **E2** | Submit with no rationale | Refused | Refusal transcript |
| **TC-05** **MFA at signing** | **E2** | Sign without re-authentication | Refused | Refusal transcript |
| **TC-06** Non-delegable | **E2** | Attempt to delegate the G8 decision | Refused | Refusal transcript |
| **TC-07** Idempotent update | **E1** | Replay the decision | Applied once | Effect count |
| **TC-08** Publication completeness | **E2** | Publish with a missing reproduction certificate | Refused | Refusal transcript |
| **TC-09** Citation audit blocker | **E2** | Publish with an open blocking audit finding | Refused at G9 | Refusal transcript |
| **TC-10** Licence check | **E2** | Include redistribution-forbidden content | Refused; hash-only reference | Refusal transcript |
| **TC-11** Privacy check | **E2** | Include personal data | Refused | Refusal transcript |
| **TC-12** **Security release check** | **E2** | Include a protected locator, an internal identifier and a capability-revealing prompt | **Each refused, naming the boundary** | Three refusals |
| **TC-13** RO-Crate | **E1** | Produce the package | Conforms; readable by a tool that knows nothing of this system | Validation · read transcript |
| **TC-14** Signature and archive | **E1** | Sign, archive and emit the release event | Verifies; the archive resolves; the event is published | Verification · event |
| **TC-15** **Retraction trigger** | **E2** | Retract a cited source | `ImpactScan` runs; the published claim is reached | Impact list |
| **TC-16** **Correction trigger** | **E2** | Publish a correction to a cited source | Reached by a different path; an impact case opens | Impact record |
| **TC-17** **Model-drift trigger** | **E2** | Change the model's capability fingerprint | Requalification triggered; affected tasks assessed | Impact record |
| **TC-18** Deep derivation | **E2** | Ensure a claim three derivation hops away is included | **Appears in the impact list** | Detection transcript |
| **TC-19** Claim challenge | **E1** | Process the impact | The claim moves to `CHALLENGED`; the owner is queued with an SLA | Claim state · queue |
| **TC-20** **Superseding package** | **E1** | Publish a superseding package | **The prior version stays reachable** and the successor names it | Supersession chain |
| **TC-21** Silent withdrawal | **E2** | Attempt to withdraw the original without supersession | Refused | Refusal transcript |
| **TC-22** False positive | **E1** | Dismiss a spurious impact case | Terminal state with a reason; does not reopen next scan | Disposition record |
| **TC-23** **Standalone audit** | **E1** | Export and verify the whole slice **with no access to the running system** | Signature, chain and manifest all verify | Verification transcript |
| **TC-24** **G0→G10 completion** | **E1** | Confirm one project has traversed every gate | Eleven `GateRecord`s; the status page can stop saying otherwise | Record set |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-106 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-106 --gate G8,G9,G10 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-106/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-106
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_106_vertical_slice_decision_publish_monitor.acceptance.md) reaches the decision — issuance is not acceptance.

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
