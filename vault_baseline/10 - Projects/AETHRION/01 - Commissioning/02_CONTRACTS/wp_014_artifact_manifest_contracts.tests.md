---
title: "WP-014 — Artifact, Dataset and Immutable Manifest Schemas — Test Procedures"
aliases:
  - "WP-014 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/02_CONTRACTS/WP-014_artifact_manifest_contracts.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/02-contracts
  - aethrion/wave/w1
  - aethrion/effort/m
  - aethrion/gate/g3-g9
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-014 — Artifact, Dataset and Immutable Manifest Schemas — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-014` |
| Work package | [`WP-014` — Artifact, Dataset and Immutable Manifest Schemas](wp_014_artifact_manifest_contracts.md) |
| Companion | [acceptance criteria](wp_014_artifact_manifest_contracts.acceptance.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Reproducibility Engineer** — the independent verifier |
| Accountable owner | Data Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-014` |

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
| Target revision | The single commit every result is bound to | Data Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Data Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Reproducibility Engineer | At completion |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |
| `WP-012` accepted output | Canonical Ownership and Field-Level Authority Matrix | Chief Architect | Before the first test case runs |

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
| C01 | `ArtifactRecord schema` | Mandatory deliverable | *(name the test case)* |
| C02 | `DatasetManifest schema` | Mandatory deliverable | *(name the test case)* |
| C03 | `Environment reference schema` | Mandatory deliverable | *(name the test case)* |
| C04 | `Immutability lifecycle` | Mandatory deliverable | *(name the test case)* |
| C05 | Write the `ArtifactRecord` and `ContentAddress` schema | WP-014-T01 | *(name the test case)* |
| C06 | Add the split, lineage and licence fields to `DatasetManifest` | WP-014-T02 | *(name the test case)* |
| C07 | Define the environment, OCI and SBOM references | WP-014-T03 | *(name the test case)* |
| C08 | Write new-version and `INVALIDATED` semantics in place of overwrite | WP-014-T04 | *(name the test case)* |
| C09 | Add object-lock, retention and legal-hold metadata | WP-014-T05 | *(name the test case)* |
| C10 | Artifact Overwrite Attempt | [ACC-23](../12_ACCEPTANCE_SCENARIOS/acc_23_artifact_overwrite.md) — Critical | *(name the test case)* |

**10 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-011 is `ACCEPTED`; an object store with versioning is
reachable in a test environment.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `ArtifactRecord`, `ContentAddress`, `DatasetManifest`, environment reference against their schemas | All validate | Schema validation output |
| 2 | **E0** | **Digest-format decision test.** Confirm exactly one content-address format is canonical, and that the choice is recorded with its reason | One format. The existing conflict — `sha256:<hex>` in the bridge, bare hex in the contract core — is resolved, not documented | ADR or package decision record |
| 3 | E1 | Confirm both existing implementations now emit the chosen format | `src/airl_bridge` and `src/airl_framework` agree; **finding H4's digest half is closed** | Passing cross-check |
| 4 | **E2** | **Overwrite test.** Write different bytes to an existing content address | **Rejected.** The rejection names the address and the existing digest | Rejection transcript |
| 5 | **E2** | **New-version test.** Supersede an artifact | A new record is created; the prior record is retained and reachable; the lineage links the two | Version chain |
| 6 | **E2** | **Invalidation propagation test.** Mark an artifact `INVALIDATED` that three claims depend on | All three are reachable **as a query result**; no downstream record is rewritten | Impact query · unchanged downstream digests |
| 7 | **E2** | **Retention test.** Let retention expire on an artifact under legal hold | Deletion is **refused**; hold overrides retention | Refusal transcript |
| 8 | **E2** | **Object-lock test.** Attempt deletion of a locked object through the storage API directly | Refused at the storage layer, not only at the application layer | Storage refusal |
| 9 | E1 | Confirm `DatasetManifest` carries split, lineage and licence, and that a split is reproducible from the manifest | The same split is regenerated byte-identically | Split reproduction |
| 10 | E1 | Confirm the environment reference resolves to an OCI digest and an SBOM | Both resolve; neither is a tag | Environment record |
| 11 | **E2** | **Tag-instead-of-digest test.** Reference an environment by mutable tag | Rejected — a tag is not a pin | Rejection transcript |
| 12 | E1 | Confirm licence metadata is mandatory where the artifact is a source representation | Zero source artifacts with no licence field | Licence coverage report |
| 13 | E3 | Independent review of the invalidation semantics against G10 supersession (WP-008) | The two agree, or the difference is reconciled in writing | `ReviewRecord` |

Steps 4, 7 and 8 are the immutability claim. Step 6 is the one that distinguishes
a content store from an evidence store: propagation as a query, not as a rewrite.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-014 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-014 --gate G3–G9 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-014/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-014
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_014_artifact_manifest_contracts.acceptance.md) reaches the decision — issuance is not acceptance.

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
