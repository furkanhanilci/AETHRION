---
title: "WP-000 — Interim Evidence Policy and Attestation Bootstrap — Test Procedures"
aliases:
  - "WP-000 tests"
type: test-procedure
category: commissioning
status: TECH_COMPLETE
source: "planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/wb
  - aethrion/effort/s
  - aethrion/gate/program
  - aethrion/state/tech-complete
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-000 — Interim Evidence Policy and Attestation Bootstrap — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-000` |
| Work package | [`WP-000` — Interim Evidence Policy and Attestation Bootstrap](wp_000_interim_evidence_policy.md) |
| Companion | [acceptance criteria](wp_000_interim_evidence_policy.acceptance.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Assurance Lead** — the independent verifier |
| Accountable owner | Project Decision Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-000` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 1 acceptance scenario(s) |
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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead | At completion |

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
| C01 | Fix the `EvidenceManifest` predicate schema and its versioning rule | WP-000-T01 | *(name the test case)* |
| C02 | Implement manifest generation, DSSE signing and log submission | WP-000-T02 | *(name the test case)* |
| C03 | Implement verification: signature, inclusion proof, digest match | WP-000-T03 | *(name the test case)* |
| C04 | Implement the **interim** external time anchor here — no dependency on WP-139 — and record the anchor reference | WP-000-T04 | *(name the test case)* |
| C05 | Write the interim independence and verifier arrangement, with its expiry | WP-000-T05 | *(name the test case)* |
| C06 | Write the WP-026 migration and retirement procedure for this policy | WP-000-T06 | *(name the test case)* |
| C07 | Planner Self-Approval Attempt | [ACC-06](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) — Critical | *(name the test case)* |

**7 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

Each step names the evidence layer it belongs to (`00_PROGRAM/06`), the command
that produces the result, and the artifact the result is recorded as. A step
whose expected result cannot be produced is a stop condition.

**Preconditions.** A signing key exists at `delivery/_keys/`; the repository is at
a known revision; `cryptography` is importable.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate a manifest against the `EvidenceManifest` predicate schema | Every mandatory field present; `attestation_profile` states `airl-interim-v0.1` | Schema validation output |
| 2 | E0 | Confirm the DSSE envelope structure: `payloadType`, base64 `payload`, `signatures[]` | Envelope parses as DSSE; `payloadType` is `application/vnd.in-toto+json` | Parsed envelope |
| 3 | E1 | Issue a manifest over a known subject set — `evidence_manifest.py issue --package WP-000 --subject …` | Envelope written; subject count equals the number of `--subject` arguments | `evidence.dsse.json` |
| 4 | E1 | Verify it — `evidence_manifest.py verify --manifest …` | `signature OK`; every subject digest `OK`; anchor `OK` | Verification transcript |
| 5 | **E2** | **Tamper the payload** and re-verify | Verification **fails**; the failure names the signature, not the digest | Rejection transcript |
| 6 | **E2** | **Tamper a covered file** and re-verify | Verification **fails**; the failure names that subject by path | Rejection transcript |
| 7 | **E2** | **Forge a signature** with a different key and re-verify | Verification **fails** | Rejection transcript |
| 8 | E1 | Confirm the anchor binds the envelope digest to a clock **and** a commit | `anchor.json` carries the envelope digest, a timestamp and `git rev-parse HEAD` | `evidence.anchor.json` |
| 9 | E1 | Re-verify after the repository moves to a new commit without reissuing | Subject digests still `OK`; the anchor's commit reference is now historical, and this is reported rather than silently accepted | Verification transcript |
| 10 | E0 | Confirm the manifest's own `limitations` list is present and non-empty | It names, at minimum: no transparency log, no keyless identity, no external timestamp authority | Manifest body |
| 11 | E3 | A verifier who did not issue the manifest re-runs steps 4–7 from a clean checkout | Identical results, obtained without access to the issuer's working tree | `VerificationRecord` |
| 12 | E1 | Execute the retirement procedure on paper against WP-026 and WP-139 | Each interim property has a named successor and a migration step | Retirement procedure document |

Steps 5, 6 and 7 are the point of this package. A verification routine that has
never been observed to fail proves nothing about the cases it claims to detect;
the tamper cases are therefore mandatory, not illustrative.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-000 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-000 --gate Program \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-000/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-000
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_000_interim_evidence_policy.acceptance.md) reaches the decision — issuance is not acceptance.

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
