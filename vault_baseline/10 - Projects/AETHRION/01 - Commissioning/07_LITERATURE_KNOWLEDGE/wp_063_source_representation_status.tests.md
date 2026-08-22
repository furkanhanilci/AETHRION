---
title: "WP-063 — Source Representation, Licence and Status Monitoring — Test Procedures"
aliases:
  - "WP-063 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-063 — Source Representation, Licence and Status Monitoring — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-063` |
| Work package | [`WP-063` — Source Representation, Licence and Status Monitoring](wp_063_source_representation_status.md) |
| Companion | [acceptance criteria](wp_063_source_representation_status.acceptance.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Archivist / Safety / Citation Auditor** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-063` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 1 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Knowledge Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Archivist / Safety / Citation Auditor | At completion |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-017` accepted output | Source Registry and Literature Contract Schemas | Knowledge Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-037` accepted output | G10 Temporal Schedules and Short ImpactScan Workflows | Knowledge Monitoring Lead | Before the first test case runs |
| `WP-050` accepted output | Initial Tool Connector Package | Tool Platform Lead | Before the first test case runs |
| `WP-058` accepted output | Untrusted Content Quarantine and Prompt-Injection Firewall | Content Security Lead | Before the first test case runs |
| `WP-061` accepted output | Canonical Source Registry Service | Knowledge Platform Lead | Before the first test case runs |
| `WP-062` accepted output | Source Identity Resolution, Deduplication and Merge | Source Resolver Lead | Before the first test case runs |

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
| C01 | `Representation ingest service` | Mandatory deliverable | *(name the test case)* |
| C02 | `License/status policy` | Mandatory deliverable | *(name the test case)* |
| C03 | `Status monitor` | Mandatory deliverable | *(name the test case)* |
| C04 | `Format locator metadata` | Mandatory deliverable | *(name the test case)* |
| C05 | `Retention mapping` | Mandatory deliverable | *(name the test case)* |
| C06 | Write representation ingest with hash, licence and access metadata | WP-063-T01 | *(name the test case)* |
| C07 | Produce the format-specific structural locator map | WP-063-T02 | *(name the test case)* |
| C08 | Establish the version, correction and preprint → published relationships | WP-063-T03 | *(name the test case)* |
| C09 | Bind the Crossref, Crossmark, retraction and status feed adapters | WP-063-T04 | *(name the test case)* |
| C10 | Add the periodic status Schedule and its event emission | WP-063-T05 | *(name the test case)* |
| C11 | Define behaviour for unavailable old representations and their retention | WP-063-T06 | *(name the test case)* |
| C12 | Retraction Impact | [ACC-04](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) — Critical | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Representation ingest | E1 | Ingest a PDF | Hash, format, licence, parser, access metadata all recorded | Representation record |
| **TC-02** Two representations | **E1** | Ingest a publisher PDF and an arXiv preprint of one work | Both bind to one `SourceRecord`, each with its own hash and licence | Two records |
| **TC-03** Licence refusal | **E2** | Ingest a representation whose licence forbids retention | Hash-only fallback; bytes not retained (`PR-14`) | Fallback record |
| **TC-04** PDF locator | **E1** | Resolve a structural locator in a PDF | Page and position resolve to the expected span | Resolution transcript |
| **TC-05** HTML locator | **E1** | Resolve a locator in HTML | Selector path resolves | Resolution transcript |
| **TC-06** Dataset locator | **E1** | Resolve a locator in tabular data | Row/column resolves | Resolution transcript |
| **TC-07** Generic locator | **E2** | Attempt a format-agnostic locator | Refused — a locator that resolves in no format precisely is not a locator | Refusal transcript |
| **TC-08** Version relationship | **E1** | Link a preprint to its published version | Related as versions; both remain citable | Relationship record |
| **TC-09** Correction | **E1** | Ingest a correction to an existing representation | Linked; the original stays resolvable | Correction record |
| **TC-10** **Retraction detection** | **E1** | Run the status sweep against a known-retracted DOI | Detected; `RetractionStatus` written | Status record |
| **TC-11** **Positive control** | **E2** | Run the sweep with the known-retracted control removed from the feed | The sweep **fails**, not reports clean | Failure transcript |
| **TC-12** **Impact emission** | **E1** | Set a retraction status | An `ImpactScan` is triggered (WP-037) and dependent claims are reachable | Impact list |
| **TC-13** **DOI-less coverage** | **E1** | Run the sweep over the full registry | The report **states the monitored fraction** and names the unmonitored sources | Coverage report |
| **TC-14** Schedule | E1 | Confirm the status Schedule runs | Short-lived runs; a missed run alerts (`PR-20`) | Schedule record |
| **TC-15** Unavailable representation | **E1** | Make a representation unfetchable | Marked unavailable; the **hash is retained** so a span's provenance survives | Availability record |
| **TC-16** Span against unavailable bytes | **E1** | Resolve an evidence span whose representation is gone | Reports *representation unavailable*, distinctly from *evidence not found* | Resolution transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-063 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-063 --gate G3,G10 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-063/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-063
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_063_source_representation_status.acceptance.md) reaches the decision — issuance is not acceptance.

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
