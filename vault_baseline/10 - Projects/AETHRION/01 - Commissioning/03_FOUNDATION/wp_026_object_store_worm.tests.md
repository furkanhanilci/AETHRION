---
title: "WP-026 — Content-Addressed Object Store and WORM — Test Procedures"
aliases:
  - "WP-026 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/03_FOUNDATION/WP-026_object_store_worm.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/03-foundation
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/g3-g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-026 — Content-Addressed Object Store and WORM — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-026` |
| Work package | [`WP-026` — Content-Addressed Object Store and WORM](wp_026_object_store_worm.md) |
| Companion | [acceptance criteria](wp_026_object_store_worm.acceptance.md) |
| Workstream | `03_FOUNDATION` |
| Approval authority | **Archivist / Security** — the independent verifier |
| Accountable owner | Data Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-026` |

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
| Target revision | The single commit every result is bound to | Data Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Data Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Archivist / Security | At completion |
| `WP-021` accepted output | Development, Staging and Production Environment Baseline | Platform Lead | Before the first test case runs |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |

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
| C01 | `Object storage IaC` | Mandatory deliverable | *(name the test case)* |
| C02 | `Object address service` | Mandatory deliverable | *(name the test case)* |
| C03 | `Retention matrix` | Mandatory deliverable | *(name the test case)* |
| C04 | `Integrity scan job` | Mandatory deliverable | *(name the test case)* |
| C05 | `Restore procedure` | Mandatory deliverable | *(name the test case)* |
| C06 | Establish the bucket/namespace layout and the data-class separation | WP-026-T01 | *(name the test case)* |
| C07 | Apply content-addressed keys and multipart hash verification | WP-026-T02 | *(name the test case)* |
| C08 | Enable object lock/WORM and the retention policy | WP-026-T03 | *(name the test case)* |
| C09 | Bind the encryption keys and access logging | WP-026-T04 | *(name the test case)* |
| C10 | Separate the quarantine, canonical and publication areas | WP-026-T05 | *(name the test case)* |
| C11 | Set up replication, restore and a bit-rot scan | WP-026-T06 | *(name the test case)* |
| C12 | Artifact Overwrite Attempt | [ACC-23](../12_ACCEPTANCE_SCENARIOS/acc_23_artifact_overwrite.md) — Critical | *(name the test case)* |
| C13 | Regional / Management Plane DR | [ACC-27](../12_ACCEPTANCE_SCENARIOS/acc_27_regional_dr.md) — Critical | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Layout | E0 | Inspect bucket/namespace layout | Quarantine, canonical and publication are separate, with data-class separation | Layout export |
| **TC-02** Content addressing | E1 | Store an object and read back its key | The key is the content hash in the format WP-014 fixed | Key record |
| **TC-03** Multipart hash | E1 | Store a large object via multipart | The verified hash equals the whole-object hash | Hash comparison |
| **TC-04** Overwrite | **E2** | Write different bytes to an existing key | **Refused at the storage layer**, not by the application | Storage refusal |
| **TC-05** Delete under lock | **E2** | Delete a locked object | Refused | Storage refusal |
| **TC-06** Retention expiry | **E2** | Expire retention on an object under legal hold and delete | Refused; hold overrides retention | Refusal transcript |
| **TC-07** Root credential | **E2** | Attempt deletion with the highest available credential | Still refused — object lock is not a permission | Refusal transcript |
| **TC-08** Quarantine boundary | **E2** | Attempt to read a quarantined object from a canonical-plane identity | Denied | Denial record |
| **TC-09** Promotion out of quarantine | E1 | Promote after scanning | The object moves with a recorded decision and a new canonical key | Promotion record |
| **TC-10** Encryption and access log | E1 | Store, read, inspect logs | Encrypted at rest; every access logged with an identity | Log sample |
| **TC-11** Replication | E1 | Store, then read from the replica | Byte-identical | Replica read |
| **TC-12** Bit-rot scan | **E1** | Corrupt a replica object out of band and run the scan | The scan **detects and reports** it | Scan report |
| **TC-13** Restore | E1 | Restore the store and verify a known digest set | All digests match | Restore transcript |
| **TC-14** **WP-000 retirement** | E1 | Migrate a WP-000 interim manifest into this store and verify it | It verifies; the migration path is exercised, not described | Migration record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-026 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-026 --gate Platform \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-026/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-026
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_026_object_store_worm.acceptance.md) reaches the decision — issuance is not acceptance.

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
