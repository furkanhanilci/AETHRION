---
title: "WP-079 — SourceTrustCard and Study Quality Assessment — Test Procedures"
aliases:
  - "WP-079 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/m
  - aethrion/gate/g3
  - aethrion/gate/g6
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-079 — SourceTrustCard and Study Quality Assessment — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-079` |
| Work package | [`WP-079` — SourceTrustCard and Study Quality Assessment](wp_079_source_trust_cards.md) |
| Companion | [acceptance criteria](wp_079_source_trust_cards.acceptance.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Independent Domain/Statistician Reviewer** — the independent verifier |
| Accountable owner | Methodologist |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-079` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** |  |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Methodologist | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Methodologist | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Independent Domain/Statistician Reviewer | At completion |
| `WP-005` accepted output | Research Risk and Assurance Profile | Safety & Governance Owner | Before the first test case runs |
| `WP-017` accepted output | Source Registry and Literature Contract Schemas | Knowledge Lead | Before the first test case runs |
| `WP-063` accepted output | Source Representation, Licence and Status Monitoring | Knowledge Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |
| `WP-076` accepted output | Evidence Span Anchoring and Re-anchoring | Evidence Engineering Lead | Before the first test case runs |
| `WP-078` accepted output | Structured Evidence Extraction Pipeline | Evidence Lead | Before the first test case runs |

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
| C01 | `SourceTrustCard engine` | Mandatory deliverable | *(name the test case)* |
| C02 | `Rubric profiles` | Mandatory deliverable | *(name the test case)* |
| C03 | `Calibration set` | Mandatory deliverable | *(name the test case)* |
| C04 | `Trust review UI contract` | Mandatory deliverable | *(name the test case)* |
| C05 | Define rubrics and profiles per source type | WP-079-T01 | *(name the test case)* |
| C06 | Bind the automatic status, licence and provenance fields | WP-079-T02 | *(name the test case)* |
| C07 | Assess method, bias, precision and applicability as separate dimensions | WP-079-T03 | *(name the test case)* |
| C08 | Write the human/agent assessment and disagreement semantics | WP-079-T04 | *(name the test case)* |
| C09 | Add expiry, new-version and retraction impact rules | WP-079-T05 | *(name the test case)* |
| C10 | Prepare the calibration sample and the reviewer guide | WP-079-T06 | *(name the test case)* |

**10 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Rubrics per type | E0 | Inspect rubrics | A rubric exists per source type; each level has a written anchor | Rubric set |
| **TC-02** **No total score** | **E0** | Inspect a completed card | Dimensions reported **separately**; no weighted total exists anywhere | Trust card |
| **TC-03** Automatic fields | **E1** | Create a card | Status, licence and provenance populate automatically from the registry | Card |
| **TC-04** **Fact/judgement separation** | **E0** | Inspect the card layout | Automatic facts and assessed judgements are **visibly distinguished** | Card |
| **TC-05** Method dimension | **E1** | Assess a well-designed study | High on method, independent of the other three | Card |
| **TC-06** Applicability | **E1** | Assess a large trial in a different population | **High method, low applicability** — the two do not collapse | Card |
| **TC-07** Precision | **E1** | Assess a small precise study | Low precision, high directness | Card |
| **TC-08** Masking attempt | **E2** | Attempt to advance a claim on a source disqualified on one dimension | Blocked on that dimension (WP-077) | Blocker record |
| **TC-09** Human/agent assessment | **E1** | Produce an agent assessment and a human assessment | Both recorded, **attributed**, and comparable | Two assessments |
| **TC-10** Disagreement | **E2** | Produce conflicting assessments | A disagreement opens; neither value is discarded | Disagreement record |
| **TC-11** **Expiry** | **E2** | Age a card past its expiry | Reads **`unassessed`**, not its last value | Card state |
| **TC-12** New version | **E2** | Ingest a new version of the source | The card is invalidated and re-queued | Invalidation record |
| **TC-13** Retraction | **E2** | Retract the source | The card reflects it immediately; dependent claims are reached (WP-037) | Impact record |
| **TC-14** **Calibration** | **E1** | Have two assessors apply the rubric to the same sample | **Agreement reported as a measured number**; disagreements itemised | Agreement report |
| **TC-15** Degenerate rubric | **E2** | Detect a dimension where all sources score identically | Flagged — a dimension with no variance is not discriminating | Flag record |
| **TC-16** Reviewer guide | E0 | Inspect the guide | Each dimension has worked examples at each level | Guide |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-079 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-079 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-079/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-079
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_079_source_trust_cards.acceptance.md) reaches the decision — issuance is not acceptance.

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
