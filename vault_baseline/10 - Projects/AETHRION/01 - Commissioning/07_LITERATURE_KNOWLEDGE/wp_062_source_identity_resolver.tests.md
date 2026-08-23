---
title: "WP-062 — Source Identity Resolution, Deduplication and Merge — Test Procedures"
aliases:
  - "WP-062 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.tests.md"
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

# WP-062 — Source Identity Resolution, Deduplication and Merge — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-062` |
| Work package | [`WP-062` — Source Identity Resolution, Deduplication and Merge](wp_062_source_identity_resolver.md) |
| Companion | [acceptance criteria](wp_062_source_identity_resolver.acceptance.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Knowledge Curator / Citation Auditor** — the independent verifier |
| Accountable owner | Source Resolver Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-062` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 3 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Source Resolver Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Source Resolver Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Knowledge Curator / Citation Auditor | At completion |
| `WP-017` accepted output | Source Registry and Literature Contract Schemas | Knowledge Lead | Before the first test case runs |
| `WP-050` accepted output | Initial Tool Connector Package | Tool Platform Lead | Before the first test case runs |
| `WP-058` accepted output | Untrusted Content Quarantine and Prompt-Injection Firewall | Content Security Lead | Before the first test case runs |
| `WP-061` accepted output | Canonical Source Registry Service | Knowledge Platform Lead | Before the first test case runs |

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
| C01 | `Source Resolver service` | Mandatory deliverable | *(name the test case)* |
| C02 | `Match rules/features` | Mandatory deliverable | *(name the test case)* |
| C03 | `Conflict queue` | Mandatory deliverable | *(name the test case)* |
| C04 | `Known-item/dedup test corpus` | Mandatory deliverable | *(name the test case)* |
| C05 | Write the identifier normalisation and resolver chain | WP-062-T01 | *(name the test case)* |
| C06 | Bind Crossref and provider lookups through the broker | WP-062-T02 | *(name the test case)* |
| C07 | Define exact and fuzzy candidate generation and the match features | WP-062-T03 | *(name the test case)* |
| C08 | Apply safe auto-merge thresholds through small explicit rules | WP-062-T04 | *(name the test case)* |
| C09 | Write the `ConflictCase`, curator queue and split/merge lineage | WP-062-T05 | *(name the test case)* |
| C10 | Build the duplicate metrics and the known-item test set | WP-062-T06 | *(name the test case)* |
| C11 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C12 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) — High | *(name the test case)* |
| C13 | Zotero Full Resync | [ACC-28](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) — High | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Normalisation | E1 | Feed DOI, PMID, arXiv, ISBN and URL in varied forms | All normalise to canonical form | Normalisation table |
| **TC-02** Exact resolution | E1 | Resolve by DOI | Single record, confidence 1.0 | Resolution record |
| **TC-03** Broker routing | **E2** | Confirm Crossref lookups go through the broker | No direct provider call from the resolver (WP-049) | Call trace |
| **TC-04** Candidate generation | E1 | Resolve by title/author/year | Candidates ranked with per-feature scores | Candidate list |
| **TC-05** **Explainability** | **E1** | Inspect any match decision | Names the features and the rule that decided it — no opaque score | Decision record |
| **TC-06** Auto-merge threshold | **E1** | Feed pairs above and below the threshold | Above merges; below queues | Two transcripts |
| **TC-07** **False-merge guard** | **E2** | Feed two distinct works sharing a title (`ACC-03`) | **Not merged.** Queued as a `ConflictCase` | Conflict record |
| **TC-08** Preprint/published | **E1** | Resolve a preprint and its published version | Linked as versions, **not merged into one** | Relationship record |
| **TC-09** File-hash signal | E1 | Resolve by representation hash | Matches the correct record | Resolution record |
| **TC-10** Ambiguity to human | **E1** | Feed a genuinely ambiguous pair | Reaches the curator queue with both candidates and the reason | Queue entry |
| **TC-11** Curator merge | **E1** | Merge from the queue | Lineage recorded; prior citations resolve (WP-061) | Merge record |
| **TC-12** **Split** | **E2** | Split one record into two | Prior citations resolve to a **disambiguation state**, never to an arbitrary side | Split transcript |
| **TC-13** **Known-item recall** | **E1** | Run the held-out known-item set | Precision and recall **reported as numbers**; the false-merge rate is stated | Metrics report |
| **TC-14** Threshold derivation | **E1** | Confirm the auto-merge threshold follows the measured false-merge rate | Derived, not chosen | Derivation record |
| **TC-15** Duplicate metrics | E5 | Inspect the duplicate dashboard | Queue depth, auto-merge rate and curator decisions all observable | Dashboard |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-062 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-062 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-062/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-062
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_062_source_identity_resolver.acceptance.md) reaches the decision — issuance is not acceptance.

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
