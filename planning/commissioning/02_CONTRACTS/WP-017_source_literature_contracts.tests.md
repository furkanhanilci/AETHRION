# WP-017 — Source Registry and Literature Contract Schemas — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-017` |
| Work package | [`WP-017` — Source Registry and Literature Contract Schemas](WP-017_source_literature_contracts.md) |
| Companion | [acceptance criteria](WP-017_source_literature_contracts.acceptance.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Citation Auditor / Data Architect** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-017` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | no | no scenario and not L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Knowledge Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Citation Auditor / Data Architect | At completion |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |
| `WP-012` accepted output | Canonical Ownership and Field-Level Authority Matrix | Chief Architect | Before the first test case runs |
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
| C01 | `Literature schema bundle` | Mandatory deliverable | *(name the test case)* |
| C02 | `Status lifecycle` | Mandatory deliverable | *(name the test case)* |
| C03 | `Sample manifests` | Mandatory deliverable | *(name the test case)* |
| C04 | `Zotero binding contract` | Mandatory deliverable | *(name the test case)* |
| C05 | Write the `SourceRecord` identifier and merge-lineage fields | WP-017-T01 | *(name the test case)* |
| C06 | Add the `SourceRepresentation` hash, format, licence and locator fields | WP-017-T02 | *(name the test case)* |
| C07 | Define `SourceTrustCard` and `RetractionStatus` | WP-017-T03 | *(name the test case)* |
| C08 | Write the `SearchProtocol`, `ScreeningDecision` and `LiteratureSetManifest` schemas | WP-017-T04 | *(name the test case)* |
| C09 | Add the `ZoteroBinding`, `SyncReceipt` and `AnnotationObservation` schemas | WP-017-T05 | *(name the test case)* |

**9 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-011 and WP-012 are `ACCEPTED`; a Zotero library and the V0
registry are reachable; Crossref is reachable for status checks.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate the whole literature schema bundle | `SourceRecord`, `SourceRepresentation`, `SourceTrustCard`, `RetractionStatus`, `SearchProtocol`, `ScreeningDecision`, `LiteratureSetManifest`, `ZoteroBinding`, `SyncReceipt`, `AnnotationObservation` all validate | Schema validation output |
| 2 | **E0** | **Work/representation separation test.** Confirm no field of `SourceRecord` describes a specific file | A representation's hash, format and locator cannot appear on the record | Schema review |
| 3 | E1 | Register one work with two representations — a publisher PDF and an arXiv preprint | Both bind to one `SourceRecord`; each carries its own hash and licence | Two representation records |
| 4 | **E2** | **Anchor test.** Anchor a claim to a `SourceRecord` rather than to a representation | Rejected — an evidence anchor requires a representation, because a page number without a file is not a locator | Rejection transcript |
| 5 | **E2** | **Licence test.** Attempt to store a representation whose licence forbids retention | Refused, and the hash-only fallback is used instead (`PR-14`) | Refusal transcript |
| 6 | E1 | Run a `SearchProtocol` and record `ScreeningDecision`s | Every included and excluded source carries a decision with a stated basis; the counts reconcile | Screening log |
| 7 | **E2** | **Frozen-set test.** Freeze a `LiteratureSetManifest`, then change the underlying registry | The manifest still resolves to what it recorded; it does not follow the registry | Frozen manifest resolution |
| 8 | **E2** | **Retraction test.** Set `RetractionStatus` on a source inside a frozen set | The status is visible **through** the frozen manifest; the set is not silently mutated. Every dependent claim is reachable | Impact list |
| 9 | E1 | Confirm `monitor_sources.py`'s sweep writes into `RetractionStatus` | The G10 measurement's `claim_impact_analysis` stops reading "not implemented" | Measurement file diff |
| 10 | **E2** | **Zotero write test.** Attempt any non-`GET` operation against the personal library through the contract path | **Refused structurally.** A `MockTransport` raising on non-`GET`, driven through the whole sync, closes finding **H3** | Refusal transcript · new test |
| 11 | E1 | Confirm `SyncReceipt` records what was read, when, and what changed | A sync with no changes still produces a receipt saying so | Receipt sample |
| 12 | E1 | Confirm `AnnotationObservation` cannot be promoted to a claim without passing through the claim contract | No direct path exists | Schema review |
| 13 | **E2** | **Merge-lineage test.** Merge two `SourceRecord`s | Lineage names both; every prior citation resolves; **finding L2's collision case has a defined outcome** | Merge record |
| 14 | E3 | Independent review of the trust card fields against `screening-sources` and `curating-zotero` | The contract supports what the skills require, or the difference is recorded | `ReviewRecord` |

Step 10 is the one this repository has owed since the first audit. It is cheap,
it closes a High finding, and it is the strongest security claim in the system.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-017 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-017 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-017/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-017
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-017_source_literature_contracts.acceptance.md) reaches the decision — issuance is not acceptance.

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
