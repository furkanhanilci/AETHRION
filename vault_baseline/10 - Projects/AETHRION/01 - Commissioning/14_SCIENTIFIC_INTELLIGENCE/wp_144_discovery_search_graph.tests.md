---
title: "WP-144 — Discovery Search Graph and Candidate Lifecycle — Test Procedures"
aliases:
  - "WP-144 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/14_SCIENTIFIC_INTELLIGENCE/WP-144_discovery_search_graph.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/14-scientific-intelligence
  - aethrion/wave/ws
  - aethrion/effort/l
  - aethrion/gate/g4
  - aethrion/gate/g5
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-144 — Discovery Search Graph and Candidate Lifecycle — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-144` |
| Work package | [`WP-144` — Discovery Search Graph and Candidate Lifecycle](wp_144_discovery_search_graph.md) |
| Companion | [acceptance criteria](wp_144_discovery_search_graph.acceptance.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Reproducibility Engineer / Chief Architect** — the independent verifier |
| Accountable owner | Experiment Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-144` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Experiment Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Experiment Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Reproducibility Engineer / Chief Architect | At completion |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-019` accepted output | Run, Environment and Reproduction Schemas | Experiment Platform Lead | Before the first test case runs |
| `WP-023` accepted output | Git, Worktree and Protected-Path Policy | Engineering Lead | Before the first test case runs |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |
| `WP-143` accepted output | Hypothesis and Principle Evolution and Proximity Graph | Evidence Platform Lead | Before the first test case runs |

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
| C01 | `SearchNode` | Mandatory deliverable | *(name the test case)* |
| C02 | `SearchEdge` | Mandatory deliverable | *(name the test case)* |
| C03 | `Candidate lifecycle state machine` | Mandatory deliverable | *(name the test case)* |
| C04 | `SearchGraph module` | Mandatory deliverable | *(name the test case)* |
| C05 | `Discovery graph projection` | Mandatory deliverable | *(name the test case)* |
| C06 | Define `SearchNode` with its state machine and artifact bindings | WP-144-T01 | *(name the test case)* |
| C07 | Define `SearchEdge` classes and the acyclicity rule on primary parents | WP-144-T02 | *(name the test case)* |
| C08 | Implement DRAFT, DEBUG, IMPROVE and FUSE transitions with policy checks | WP-144-T03 | *(name the test case)* |
| C09 | Bind candidate artifacts and workspaces to nodes | WP-144-T04 | *(name the test case)* |
| C10 | Bind node executions to the run registry and verified values | WP-144-T05 | *(name the test case)* |
| C11 | Build the derived discovery-graph projection and its rebuild | WP-144-T06 | *(name the test case)* |
| C12 | Integrate the campaign slice with the Temporal activity boundary | WP-144-T07 | *(name the test case)* |
| C13 | Cross-Branch Fusion Lineage | [ACC-58](../12_ACCEPTANCE_SCENARIOS/acc_58_cross_branch_fusion_lineage.md) — High | *(name the test case)* |
| C14 | Implementation Failure Must Not Refute a Hypothesis | [ACC-64](../12_ACCEPTANCE_SCENARIOS/acc_64_implementation_failure_not_refutation.md) — Critical | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-082 is `ACCEPTED` so runs and values can be bound; WP-023 supplies candidate worktrees; a deterministic fixture task exists so a campaign can be replayed without a model in the loop.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `SearchNode` and `SearchEdge` against their schemas | Both validate; node state and edge class are closed enumerations | Validator output |
| 2 | **E2** | **Primary-parent cycle.** Construct a cycle in the `PRIMARY_PARENT` graph | Rejected. The ancestry path reproduction depends on must stay acyclic | Refusal transcript |
| 3 | E1 | Create a `DRAFT` node that executes, then an `IMPROVE` successor | The successor is a new immutable node naming its primary parent | Both nodes |
| 4 | **E1** | **Debug preserves direction.** Create a candidate that fails to compile, repair it through `DEBUG`, and compare mechanism tags | The repaired node carries the **same** mechanism identity as its parent | Both nodes |
| 5 | **E2** | **Implementation failure is not refutation.** After exhausting `DEBUG` attempts, attempt to mark the hypothesis `REFUTED` | Refused. A `FailedApproach` with class `IMPLEMENTATION` is recorded instead — ACC-64 | Refusal transcript |
| 6 | E1 | Run a candidate that fails on a corrupted dataset and one that returns a valid preregistered null result | Classified `DATA` and `HYPOTHESIS` respectively; only the second is eligible for a `NegativeResult` | Two assessments |
| 7 | **E2** | **Reference edges do not re-parent.** Add a `REFERENCE` edge from another branch and re-read the ancestry | The primary parent is unchanged; the reference is visible and separate | Graph query |
| 8 | **E2** | **Fusion needs two.** Create a `FUSE` node with a single input | Rejected | Refusal transcript |
| 9 | **E1** | **Fusion lineage.** Create a `FUSE` node from branches A and C, execute it, export the evidence package, then rebuild the derived graph | A and C are named as inputs in the canonical graph, the export **and** the rebuild; their artifact digests are unchanged — ACC-58 | Three lineage listings |
| 10 | E1 | Confirm every executed candidate resolves to an immutable artifact, a workspace commit and an official run | No executed node lacks any of the three | Binding report |
| 11 | **E4** | **Replay.** Persist a multi-branch campaign, restore it and replay the deterministic slice | The restored graph is identical, and the replayed slice produces the same transitions | Two graph digests |
| 12 | E1 | Render the derived discovery graph and confirm it holds no state absent from the canonical store | Dropping and rebuilding loses nothing | Rebuild diff |
| 13 | E3 | Independent review of one campaign's node history | The reviewer can say, for every node, where it came from and whether the change was a repair or a scientific move | `ReviewRecord` |

Cases 4, 5 and 6 are the scientific content of this package. Everything else is
graph hygiene; these three are what stop a build log from being mistaken for a
research record.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-144   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-144 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-144/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-144
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_144_discovery_search_graph.acceptance.md) reaches the decision — issuance is not acceptance.

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
