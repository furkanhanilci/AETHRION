---
title: "WP-094 — Literature Workbench and Reconciliation UI — Test Procedures"
aliases:
  - "WP-094 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/09_EXPERIENCE_OBSERVABILITY/WP-094_literature_workbench.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/09-experience-observability
  - aethrion/wave/w5
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-094 — Literature Workbench and Reconciliation UI — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-094` |
| Work package | [`WP-094` — Literature Workbench and Reconciliation UI](wp_094_literature_workbench.md) |
| Companion | [acceptance criteria](wp_094_literature_workbench.acceptance.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Knowledge Curator / Citation Auditor** — the independent verifier |
| Accountable owner | Knowledge Product Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-094` |

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
| Target revision | The single commit every result is bound to | Knowledge Product Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Product Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Knowledge Curator / Citation Auditor | At completion |
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
| C01 | `Literature Workbench` | Mandatory deliverable | *(name the test case)* |
| C02 | `Resolver/reconciliation UI` | Mandatory deliverable | *(name the test case)* |
| C03 | `Screening UI` | Mandatory deliverable | *(name the test case)* |
| C04 | `Manifest freeze UI` | Mandatory deliverable | *(name the test case)* |
| C05 | `Sync health view` | Mandatory deliverable | *(name the test case)* |
| C06 | Write the campaign, query and coverage dashboard | WP-094-T01 | *(name the test case)* |
| C07 | Build the source identity, representation and trust detail views | WP-094-T02 | *(name the test case)* |
| C08 | Add the duplicate, merge and conflict reconciliation screen | WP-094-T03 | *(name the test case)* |
| C09 | Bind the screening include/exclude/disagreement queue | WP-094-T04 | *(name the test case)* |
| C10 | Write the annotation → `EvidenceCandidate` promotion view | WP-094-T05 | *(name the test case)* |
| C11 | Add Zotero sync receipts, lag and conflict views plus manifest freeze/diff | WP-094-T06 | *(name the test case)* |
| C12 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C13 | Agent-Used Source Write-Back | [ACC-02](../12_ACCEPTANCE_SCENARIOS/acc_02_agent_used_source_writeback.md) — Critical | *(name the test case)* |
| C14 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) — High | *(name the test case)* |
| C15 | Retraction Impact | [ACC-04](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) — Critical | *(name the test case)* |
| C16 | Zotero Full Resync | [ACC-28](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) — High | *(name the test case)* |

**16 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Campaign dashboard | **E1** | Open a campaign | Queries, execution log, known-item recall and saturation visible | Screenshot |
| **TC-02** **Coverage fraction** | **E1** | Inspect the status coverage panel | The **monitored fraction** and the unmonitored sources are shown | Screenshot |
| **TC-03** Clean-without-coverage | **E2** | Show *no retractions found* with no coverage stated | Refused by the view contract | Refusal transcript |
| **TC-04** Source detail | **E1** | Open a source | Identity, representations, trust card and status all resolve | Screenshot |
| **TC-05** **Reconciliation screen** | **E1** | Open a resolver conflict | Both candidates side by side, **with the match features that produced it** | Screenshot |
| **TC-06** False-merge rejection (`ACC-03`) | **E1** | Reject a tempting merge | Recorded with the curator and the reason; the pair is not re-queued identically | Decision record |
| **TC-07** Merge from screen | **E1** | Confirm a merge | Lineage recorded; prior citations resolve (WP-061) | Merge record |
| **TC-08** Screening queue | **E1** | Screen from the queue | Reason code required; the other screener's decision is **not visible** | Screening log |
| **TC-09** Disagreement routing | **E1** | Produce a screening disagreement | Routed to arbitration, not resolved by whoever looks second | Disagreement record |
| **TC-10** **Promotion view** | **E1** | Promote an annotation | Actor, reason and **locator state** captured at promotion | Promotion record |
| **TC-11** Degraded locator | **E1** | Promote a span in `NEEDS_REANCHOR` | Permitted and **visibly flagged** | Screenshot |
| **TC-12** Zotero receipts | **E1** | Inspect the sync panel | Last sync, receipts, lag and conflict count visible | Screenshot |
| **TC-13** Silent sync failure | **E2** | Fail a sync | The panel shows it; the library is **not** presented as current | Screenshot |
| **TC-14** Manifest freeze | **E1** | Freeze a set from the workbench | Manifest written and hashed (WP-072) | Manifest |
| **TC-15** Manifest diff | **E1** | Produce a new version | Added, removed and status-changed sources shown | Diff view |
| **TC-16** **Queue depth** | **E1** | Inspect every queue | Each shows its depth and its oldest item | Screenshot |
| **TC-17** Ageing item | **E2** | Let a queue item pass its SLA | Escalates; nothing ages silently | Escalation record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-094 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-094 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-094/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-094
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_094_literature_workbench.acceptance.md) reaches the decision — issuance is not acceptance.

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
