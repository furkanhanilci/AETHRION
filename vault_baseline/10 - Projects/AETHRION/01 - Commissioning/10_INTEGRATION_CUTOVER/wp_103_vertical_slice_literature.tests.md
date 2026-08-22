---
title: "WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze — Test Procedures"
aliases:
  - "WP-103 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-103_vertical_slice_literature.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-103 — Vertical Slice 2 — Two-Way Literature and Set Freeze — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-103` |
| Work package | [`WP-103` — Vertical Slice 2 — Two-Way Literature and Set Freeze](wp_103_vertical_slice_literature.md) |
| Companion | [acceptance criteria](wp_103_vertical_slice_literature.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Citation Auditor / Security** — the independent verifier |
| Accountable owner | Evidence Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-103` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 5 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Evidence Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Evidence Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Citation Auditor / Security | At completion |
| `WP-035` accepted output | G2 Protocol, G3 Literature and G4 Baseline Workflows | Scientific Workflow Lead | Before the first test case runs |
| `WP-058` accepted output | Untrusted Content Quarantine and Prompt-Injection Firewall | Content Security Lead | Before the first test case runs |
| `WP-061` accepted output | Canonical Source Registry Service | Knowledge Platform Lead | Before the first test case runs |
| `WP-062` accepted output | Source Identity Resolution, Deduplication and Merge | Source Resolver Lead | Before the first test case runs |
| `WP-063` accepted output | Source Representation, Licence and Status Monitoring | Knowledge Lead | Before the first test case runs |
| `WP-064` accepted output | Zotero Library, Collection and Permission Model | Knowledge Lead | Before the first test case runs |
| `WP-065` accepted output | Personal Zotero Seed Ingest Pipeline | Knowledge Platform Lead | Before the first test case runs |
| `WP-066` accepted output | Agent Candidate and Used-Source Write-Back | Knowledge Platform Lead | Before the first test case runs |
| `WP-067` accepted output | Zotero Two-Way Sync and Reconciliation | Knowledge Platform Lead | Before the first test case runs |
| `WP-068` accepted output | Zotero Annotation → EvidenceCandidate Pipeline | Evidence Intake Lead | Before the first test case runs |
| `WP-069` accepted output | SearchProtocol and LiteratureCampaign Orchestration | Evidence Lead | Before the first test case runs |
| `WP-070` accepted output | Human + Agent Two-Way Literature Discovery | Evidence Lead | Before the first test case runs |
| `WP-071` accepted output | Screening, Inclusion/Exclusion and Coverage | Evidence Lead | Before the first test case runs |
| `WP-072` accepted output | LiteratureSetManifest Freeze and Human-Readable Archive | Evidence Lead | Before the first test case runs |
| `WP-094` accepted output | Literature Workbench and Reconciliation UI | Knowledge Product Lead | Before the first test case runs |
| `WP-099` accepted output | WORM Audit Ledger and Independent Export | Internal Audit Platform Lead | Before the first test case runs |

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
| C01 | `Literature vertical dossier` | Mandatory deliverable | *(name the test case)* |
| C02 | `Frozen LiteratureSetManifest` | Mandatory deliverable | *(name the test case)* |
| C03 | `Zotero SyncReceipts` | Mandatory deliverable | *(name the test case)* |
| C04 | `Coverage/screening report` | Mandatory deliverable | *(name the test case)* |
| C05 | Ingest the personal seed fixture | WP-103-T01 | *(name the test case)* |
| C06 | Run the agent literature campaign, snowball and counter-evidence search | WP-103-T02 | *(name the test case)* |
| C07 | Test duplicates, conflicts, 412 responses and human-field preservation | WP-103-T03 | *(name the test case)* |
| C08 | Complete the screening, disagreement, trust and status flow | WP-103-T04 | *(name the test case)* |
| C09 | Prepare an annotation for candidate → span promotion | WP-103-T05 | *(name the test case)* |
| C10 | Verify the manifest, exports, Zotero frozen view and audit trail | WP-103-T06 | *(name the test case)* |
| C11 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C12 | Agent-Used Source Write-Back | [ACC-02](../12_ACCEPTANCE_SCENARIOS/acc_02_agent_used_source_writeback.md) — Critical | *(name the test case)* |
| C13 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) — High | *(name the test case)* |
| C14 | Prompt-Injection PDF | [ACC-05](../12_ACCEPTANCE_SCENARIOS/acc_05_prompt_injection_pdf.md) — Critical | *(name the test case)* |
| C15 | Zotero Full Resync | [ACC-28](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) — High | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Seed ingest | **E1** | Ingest the personal seed fixture | Sources resolve into the registry; correlation established | Ingest report |
| **TC-02** **Read-only boundary** | **E2** | Drive the whole sync with a transport that raises on any non-`GET` | **Passes** — finding **H3** closed behaviourally | Transport test |
| **TC-03** **Above the cap** | **E1** | Ingest a fixture library of more than 100 items | All ingested; **no silent truncation**; the run is not `SUCCEEDED` if partial | Ingest report |
| **TC-04** **M9 precondition** | **E2** | Confirm the projection cap is removed before paging is enabled | Enforced; the ordering is not merely documented | Gate record |
| **TC-05** Agent campaign | **E1** | Run keyword, citation, snowball and semantic scouts | Candidates produced with strategy and branch recorded | Candidate set |
| **TC-06** **Counter-evidence branch** | **E1** | Run the disconfirming search | Candidates produced; **closing without it is refused** | Refusal · counter set |
| **TC-07** Cross-strategy merge | **E1** | Merge overlapping candidates | Through the resolver at the conservative threshold | Merge record |
| **TC-08** **Duplicate fixture** (`ACC-03`) | **E2** | Introduce two distinct works sharing a title | **Not merged**; queued as a conflict | Conflict record |
| **TC-09** **412 fixture** | **E2** | Have a human edit land between agent read and write | 412; **the human's edit survives**; no blind retry | 412 transcript |
| **TC-10** **Human-field preservation** | **E2** | Attempt an agent write to a human-authority field | Refused — invariant 5 | Refusal transcript |
| **TC-11** **Deletion fixture** | **E1** | Remove a seed source upstream | Reconciled per field authority; **not left silently current** — finding **H2** | Reconciliation record |
| **TC-12** Collection membership | **E2** | Update collection membership with a human-added item present | Read → merge → conditional write; the human's item survives | Membership diff |
| **TC-13** Screening | **E1** | Screen to inclusion with reason codes | Blind assignment; codes required; PRISMA numbers reconcile | Screening log · flow |
| **TC-14** Screening disagreement | **E2** | Produce a conflict | `DisagreementCase`; **not resolved by majority** | Disagreement record |
| **TC-15** Trust cards | **E1** | Assess included sources | Dimensions separate; facts distinguished from judgements | Trust cards |
| **TC-16** **Annotation promotion** | **E1** | Promote an annotation to an `EvidenceCandidate` | Actor, reason and locator state recorded; **the observation alone never cites** | Promotion record |
| **TC-17** Direct citation attempt | **E2** | Cite an `AnnotationObservation` in a claim | Refused | Refusal transcript |
| **TC-18** **Manifest freeze** | **E1** | Freeze the G3 set | Immutable, hashed, signed; included **and excluded** with reason codes | Manifest |
| **TC-19** Retraction through freeze | **E2** | Retract an included source | Visible through the frozen set; the set is not mutated | Status resolution |
| **TC-20** Exports and frozen view | **E1** | Export CSL-JSON/BibTeX/RIS and sync `90_Frozen_View` | All round-trip; the Zotero view is marked a mirror | Exports · collection |
| **TC-21** Audit trail | **E1** | Export the audit | Full chain verifies standalone | Verification transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-103 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-103 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-103/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-103
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_103_vertical_slice_literature.acceptance.md) reaches the decision — issuance is not acceptance.

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
