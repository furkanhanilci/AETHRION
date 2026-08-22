---
title: "WP-067 — Zotero Two-Way Sync and Reconciliation — Test Procedures"
aliases:
  - "WP-067 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.tests.md"
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

# WP-067 — Zotero Two-Way Sync and Reconciliation — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-067` |
| Work package | [`WP-067` — Zotero Two-Way Sync and Reconciliation](wp_067_zotero_sync_reconciliation.md) |
| Companion | [acceptance criteria](wp_067_zotero_sync_reconciliation.acceptance.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Knowledge Curator / SRE** — the independent verifier |
| Accountable owner | Knowledge Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-067` |

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
| Target revision | The single commit every result is bound to | Knowledge Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Knowledge Curator / SRE | At completion |
| `WP-061` accepted output | Canonical Source Registry Service | Knowledge Platform Lead | Before the first test case runs |
| `WP-062` accepted output | Source Identity Resolution, Deduplication and Merge | Source Resolver Lead | Before the first test case runs |
| `WP-064` accepted output | Zotero Library, Collection and Permission Model | Knowledge Lead | Before the first test case runs |
| `WP-065` accepted output | Personal Zotero Seed Ingest Pipeline | Knowledge Platform Lead | Before the first test case runs |
| `WP-066` accepted output | Agent Candidate and Used-Source Write-Back | Knowledge Platform Lead | Before the first test case runs |

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
| C01 | `Sync engine` | Mandatory deliverable | *(name the test case)* |
| C02 | `Reconciliation queue` | Mandatory deliverable | *(name the test case)* |
| C03 | `Full-resync runbook` | Mandatory deliverable | *(name the test case)* |
| C04 | `Conflict metrics/dashboard` | Mandatory deliverable | *(name the test case)* |
| C05 | Establish the per-library and per-item version and `since` checkpoint store | WP-067-T01 | *(name the test case)* |
| C06 | Write the field-level three-way merge classes | WP-067-T02 | *(name the test case)* |
| C07 | Raise a `ConflictCase` for 412, deletion, permission and duplicate situations | WP-067-T03 | *(name the test case)* |
| C08 | Bind the manual reconciliation UI/API and the curator SLA | WP-067-T04 | *(name the test case)* |
| C09 | Write the full-resync plus dedup/rebind procedure | WP-067-T05 | *(name the test case)* |
| C10 | Establish sync lag, error and overwrite-detector telemetry | WP-067-T06 | *(name the test case)* |
| C11 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) — High | *(name the test case)* |
| C12 | Zotero Full Resync | [ACC-28](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) — High | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Checkpoint store | E0 | Inspect per-library and per-item versions | All recorded; the `since` token resumes correctly | Checkpoint state |
| **TC-02** No-change sync | **E1** | Sync twice with no changes | The second reads nothing and writes nothing | Request log |
| **TC-03** Human-only edit | **E1** | Edit a human-authority field, then sync | The human value survives; nothing is overwritten | Field comparison |
| **TC-04** Agent-only edit | **E1** | Change an agent-authority field, then sync | Written; the human's fields untouched | Field comparison |
| **TC-05** **Disjoint fields** | **E1** | Edit the abstract by hand and the DOI by agent | **Both survive** — field-level merge, not item-level | Merged item |
| **TC-06** Same field | **E2** | Both edit the same field | A `ConflictCase` opens; **neither value is discarded** | Conflict record |
| **TC-07** 412 handling | **E2** | Force a version conflict on write | Re-read, merge, and conflict if unsafe — **never a blind retry** | Handling transcript |
| **TC-08** Deletion upstream | **E2** | Delete an item a claim cites | `ConflictCase`; the citation still resolves; nothing is silently dropped | Conflict record |
| **TC-09** Permission change | **E2** | Remove read access to a synced item | Distinguished from deletion; reported | State record |
| **TC-10** Duplicate appearance | **E2** | Create a Zotero duplicate of a bound source | `ConflictCase` via the resolver (WP-062); no auto-merge | Conflict record |
| **TC-11** Curator resolution | **E1** | Resolve a conflict from the queue | Applied with the curator as actor; the losing value is retained in the record | Resolution record |
| **TC-12** Curator SLA | **E2** | Let a conflict pass its SLA | Escalation fires; the case is never silently aged | Escalation record |
| **TC-13** **Lost checkpoint** | **E2** | Delete the checkpoint store and recover | Full resync **plus dedup and rebind**: no duplicates, no human edits overwritten | Recovery report |
| **TC-14** **Overwrite detector** | **E2** | Force a path that overwrites a human value | **Detected and alerted**; the prior value is recoverable from the receipt | Alert · recovery |
| **TC-15** Detector liveness | **E2** | Run the detector suite with the seeded overwrite removed | The suite **fails** rather than reporting clean | Failure transcript |
| **TC-16** Telemetry | E5 | Inspect sync lag, error rate and conflict depth | All three observable | Dashboard |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-067 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-067 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-067/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-067
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_067_zotero_sync_reconciliation.acceptance.md) reaches the decision — issuance is not acceptance.

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
