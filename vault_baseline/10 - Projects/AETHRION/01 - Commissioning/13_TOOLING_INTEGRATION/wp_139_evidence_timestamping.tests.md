---
title: "WP-139 — Evidence Timestamping and Independent Seal — Test Procedures"
aliases:
  - "WP-139 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-139_evidence_timestamping.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/s
  - aethrion/gate/g2
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-139 — Evidence Timestamping and Independent Seal — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-139` |
| Work package | [`WP-139` — Evidence Timestamping and Independent Seal](wp_139_evidence_timestamping.md) |
| Companion | [acceptance criteria](wp_139_evidence_timestamping.acceptance.md) |
| Workstream | `13_TOOLING_INTEGRATION` |
| Approval authority | **Research Integrity Officer** — the independent verifier |
| Accountable owner | Data Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-139` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Data Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Data Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Research Integrity Officer | At completion |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |

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
| C01 | Submit the `EvidenceManifest` hash to OpenTimestamps | WP-139-T01 | *(name the test case)* |
| C02 | Secondary RFC 3161 TSA stamp | WP-139-T02 | *(name the test case)* |
| C03 | Bind the stamp files to the manifest and the object store | WP-139-T03 | *(name the test case)* |
| C04 | Verification command and runbook | WP-139-T04 | *(name the test case)* |
| C05 | Automatic stamping when the G2 analysis plan is locked | WP-139-T05 | *(name the test case)* |
| C06 | Track stamp latency and maturation | WP-139-T06 | *(name the test case)* |
| C07 | Artifact Overwrite Attempt | [ACC-23](../12_ACCEPTANCE_SCENARIOS/acc_23_artifact_overwrite.md) — Critical | *(name the test case)* |
| C08 | Complete Project Audit Export | [ACC-40](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) — Critical | *(name the test case)* |

**8 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **OTS submission** | **E1** | Submit an `EvidenceManifest` hash to OpenTimestamps | Stamp file produced and stored | Stamp file |
| **TC-02** OTS confirmation | **E1** | Wait for confirmation and upgrade the stamp | Upgraded; the attestation resolves to a block | Upgraded stamp |
| **TC-03** **RFC 3161 stamp** | **E1** | Obtain a TSA timestamp | Token produced; the TSA certificate chain verifies | Token |
| **TC-04** Two anchors | **E0** | Inspect a stamped manifest | **Both** anchors present, with their differing trust assumptions recorded | Manifest |
| **TC-05** Single anchor | **E2** | Attempt to stamp with only one | Permitted only with a recorded reason — the two have disjoint failure modes | Decision record |
| **TC-06** **Binding** | **E1** | Inspect the binding | Stamps bound to the manifest digest **and** stored in the object store (WP-026) | Binding record |
| **TC-07** Wrong-digest stamp | **E2** | Bind a stamp for a different digest | Refused | Refusal transcript |
| **TC-08** **Standalone verification** | **E1** | Verify with the manifest, the stamps and **no access to this system** | Both anchors verify | Verification transcript |
| **TC-09** Altered manifest | **E2** | Alter the manifest and verify | **Fails** | Failure transcript |
| **TC-10** Backdating attempt | **E2** | Attempt to produce a stamp claiming an earlier time | **Impossible** for OTS; refused for the TSA path | Transcript |
| **TC-11** **G2 automatic stamping** | **E1** | Lock a G2 analysis plan | **Stamped automatically**; the stamp is bound before any run | Stamp record |
| **TC-12** Unstamped analysis plan | **E2** | Attempt a confirmatory run against an unstamped locked plan | Refused, or the claim is marked as internally-timestamped only | Refusal · marking |
| **TC-13** Runbook | **E1** | Follow the verification runbook as an outside reader | The command works with only the manifest and the stamp | Runbook transcript |
| **TC-14** OTS unavailable | **E2** | Make the calendar unreachable | Recorded as **unstamped**, never as stamped; retried | Failure record |
| **TC-15** TSA unavailable | **E2** | Make the TSA unreachable | Same | Failure record |
| **TC-16** **Interim retirement** | **E1** | Confirm the interim anchor is superseded | `airl-interim-v0.1`'s *external timestamp authority* limitation is **removed from new manifests** | Profile diff |
| **TC-17** Historical manifests | **E1** | Stamp existing manifests retroactively | Stamped **at today's time**, and the record says so — a retroactive stamp proves existence now, not then | Stamp record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-139 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-139 --gate G9,G10 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-139/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-139
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_139_evidence_timestamping.acceptance.md) reaches the decision — issuance is not acceptance.

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
