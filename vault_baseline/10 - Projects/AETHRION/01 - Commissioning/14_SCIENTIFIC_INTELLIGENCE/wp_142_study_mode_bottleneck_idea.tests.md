---
title: "WP-142 — Study Mode, Bottleneck and Idea Card Model — Test Procedures"
aliases:
  - "WP-142 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-142_study_mode_bottleneck_idea.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g0
  - aethrion/gate/g1
  - aethrion/gate/g2
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-142 — Study Mode, Bottleneck and Idea Card Model — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-142` |
| Work package | [`WP-142` — Study Mode, Bottleneck and Idea Card Model](wp_142_study_mode_bottleneck_idea.md) |
| Companion | [acceptance criteria](wp_142_study_mode_bottleneck_idea.acceptance.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Assurance Lead / Methodologist** — the independent verifier |
| Accountable owner | Research Director |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-142` |

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
| Target revision | The single commit every result is bound to | Research Director | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Research Director | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead / Methodologist | At completion |
| `WP-005` accepted output | Research Risk and Assurance Profile | Safety & Governance Owner | Before the first test case runs |
| `WP-008` accepted output | G0–G10 Gate and Assurance Policy | Research Director | Before the first test case runs |
| `WP-013` accepted output | Project, Task, Role and Skill Contract Schemas | Control Plane Lead | Before the first test case runs |
| `WP-018` accepted output | Claim, Evidence, Review and Decision Schemas | Evidence Platform Lead | Before the first test case runs |
| `WP-034` accepted output | G0 Intake and G1 Charter Workflows | Research Operations Lead | Before the first test case runs |
| `WP-141` accepted output | Upstream Assimilation, Lineage and Characterisation Governance | Chief Architect | Before the first test case runs |

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
| C01 | `StudyModeRecord` | Mandatory deliverable | *(name the test case)* |
| C02 | `BottleneckRecord` | Mandatory deliverable | *(name the test case)* |
| C03 | `IdeaCard` | Mandatory deliverable | *(name the test case)* |
| C04 | `PriorArtCollision` | Mandatory deliverable | *(name the test case)* |
| C05 | `Gate policy bindings for G0-G2` | Mandatory deliverable | *(name the test case)* |
| C06 | `Mode change deviation procedure` | Mandatory deliverable | *(name the test case)* |
| C07 | Define `StudyModeRecord` with claim ceiling and external timestamp semantics | WP-142-T01 | *(name the test case)* |
| C08 | Define `BottleneckRecord` with mandatory evidence references and competing explanations | WP-142-T02 | *(name the test case)* |
| C09 | Define `IdeaCard` with the falsification-plan promotion rule | WP-142-T03 | *(name the test case)* |
| C10 | Define `PriorArtCollision` with per-axis overlap and materiality | WP-142-T04 | *(name the test case)* |
| C11 | Bind the records to G0, G1 and G2 gate policy | WP-142-T05 | *(name the test case)* |
| C12 | Write the mode-change deviation path and the one-way ceiling rule | WP-142-T06 | *(name the test case)* |
| C13 | Expose the records in the projection and UI schema | WP-142-T07 | *(name the test case)* |
| C14 | Confirmatory Result Without a Frozen Analysis Plan | [ACC-56](../12_ACCEPTANCE_SCENARIOS/acc_56_confirmatory_without_frozen_plan.md) — Critical | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-005 and WP-008 are `ACCEPTED`; an external time anchor is reachable (WP-139 or the WP-000 interim anchor); a seeded literature set exists so a bottleneck can carry real evidence references.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `StudyModeRecord`, `BottleneckRecord`, `IdeaCard` and `PriorArtCollision` against their schemas | All four validate; required fields are enforced | Validator output |
| 2 | E0 | Confirm study mode and assurance class are **separate fields** with separate effects | Neither is derivable from the other; a feasibility R3 project is expressible | Schema and worked example |
| 3 | **E1** | **Timestamp ordering.** Declare `CONFIRMATORY`, produce an official outcome, then seal the analysis plan | The external timestamps order plan **after** outcome and the ordering is recorded | Timestamp evidence |
| 4 | **E2** | **Confirmatory without a frozen plan.** With that ordering, register a confirmatory `ClaimVersion` | Refused, with the timestamp ordering as the stated reason — ACC-56 | Refusal transcript |
| 5 | **E2** | **One-way ceiling.** Relabel the same work exploratory by record, then attempt to relabel it confirmatory again | The downgrade succeeds and creates a successor plus a deviation record; **the upgrade is refused** | Both transcripts |
| 6 | **E2** | **Feasibility ceiling.** Attempt to emit a confirmatory publication assertion from a `FEASIBILITY` project | Refused; the claim ceiling is enforced at the gate, not by convention | Refusal transcript |
| 7 | **E2** | **Bottleneck without evidence.** Record a bottleneck whose only support is a model assertion, and mark it evidence-backed | Refused; evidence references are required for the evidence-backed status | Refusal transcript |
| 8 | E1 | Record a bottleneck carrying contradictory literature | Both the supporting and the competing explanations are retained; neither is dropped | `BottleneckRecord` |
| 9 | **E2** | **Falsification required.** Promote an `IdeaCard` with no falsification plan to hypothesis candidate | Promotion blocked — an idea that cannot say what would show it wrong is not yet a scientific idea | Refusal transcript |
| 10 | **E1** | **Prior-art positive control.** Screen an idea deliberately duplicating a known recent work | Scored **HIGH** on the matching axes, with problem, mechanism, data, evaluation and contribution reported separately | `PriorArtCollision` |
| 11 | **E1** | **Discrimination control.** Screen a genuinely novel idea through the same path | **Not** flagged HIGH. A collision detector that flags everything is not a detector | `PriorArtCollision` |
| 12 | E1 | Confirm an exploratory idea is permitted with the correct label and no falsification plan | Permitted and labelled; the rule binds promotion, not exploration | Transcript |
| 13 | E3 | Independent review of one full G0→G2 record set | The reviewer can reconstruct why this idea, from this bottleneck, under this mode, without asking the producer | `ReviewRecord` |

Case 5 is the one worth running twice. Lowering a claim ceiling and raising it
are not symmetrical operations, and a system that permits both has not
implemented a ceiling — it has implemented a label.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-142   # dependencies and their states
python3 scripts/ready_queue.py           # this package must appear under "Ready now"
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

A case in **bold** is a refusal case: it passes when the system declines to act.
Half this table is refusals, and a run in which every bold case "worked" has
tested the happy path twice.

### Capturing evidence

```bash
python3 scripts/evidence_manifest.py issue --package WP-142 --gate G1 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-142/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-142
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_142_study_mode_bottleneck_idea.acceptance.md) reaches the decision — issuance is not acceptance.

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
