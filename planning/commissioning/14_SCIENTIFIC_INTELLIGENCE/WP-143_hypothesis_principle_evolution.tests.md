# WP-143 — Hypothesis and Principle Evolution and Proximity Graph — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-143` |
| Work package | [`WP-143` — Hypothesis and Principle Evolution and Proximity Graph](WP-143_hypothesis_principle_evolution.md) |
| Companion | [acceptance criteria](WP-143_hypothesis_principle_evolution.acceptance.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Methodologist / Knowledge Lead** — the independent verifier |
| Accountable owner | Evidence Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-143` |

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
| Target revision | The single commit every result is bound to | Evidence Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Evidence Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Methodologist / Knowledge Lead | At completion |
| `WP-018` accepted output | Claim, Evidence, Review and Decision Schemas | Evidence Platform Lead | Before the first test case runs |
| `WP-020` accepted output | Schema Registry, Compatibility and Contract SDK | Platform Architecture Lead | Before the first test case runs |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-035` accepted output | G2 Protocol, G3 Literature and G4 Baseline Workflows | Scientific Workflow Lead | Before the first test case runs |
| `WP-142` accepted output | Study Mode, Bottleneck and Idea Card Model | Research Director | Before the first test case runs |

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
| C01 | `HypothesisVersion` | Mandatory deliverable | *(name the test case)* |
| C02 | `PrincipleVersion` | Mandatory deliverable | *(name the test case)* |
| C03 | `AssumptionVersion` | Mandatory deliverable | *(name the test case)* |
| C04 | `HypothesisSimilarityEdge projection` | Mandatory deliverable | *(name the test case)* |
| C05 | `Evolution operator vocabulary` | Mandatory deliverable | *(name the test case)* |
| C06 | `Anomaly to principle challenge procedure` | Mandatory deliverable | *(name the test case)* |
| C07 | Define `HypothesisVersion` with parent, operator and immutability rules | WP-143-T01 | *(name the test case)* |
| C08 | Define the evolution operator vocabulary and its review requirements | WP-143-T02 | *(name the test case)* |
| C09 | Define `PrincipleVersion` with its distinct status vocabulary | WP-143-T03 | *(name the test case)* |
| C10 | Define `AssumptionVersion` and its links to protocol and analysis plan | WP-143-T04 | *(name the test case)* |
| C11 | Build the `HypothesisSimilarityEdge` projection and its rebuild path | WP-143-T05 | *(name the test case)* |
| C12 | Type `SearchPriorityScore` so it cannot be written to a claim assessment | WP-143-T06 | *(name the test case)* |
| C13 | Implement the anomaly-to-principle-challenge flow with its review gate | WP-143-T07 | *(name the test case)* |
| C14 | Hypothesis In-Place Mutation Attempt | [ACC-57](../12_ACCEPTANCE_SCENARIOS/ACC-57_hypothesis_in_place_mutation.md) — High | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-018 and WP-020 are `ACCEPTED`; WP-142 supplies at least one promoted `IdeaCard`; a derived-graph projection exists so the proximity read model can be dropped and rebuilt.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `HypothesisVersion`, `PrincipleVersion` and `AssumptionVersion` against their schemas | All three validate; the parent and operator fields are required on any non-initial version | Validator output |
| 2 | E0 | Confirm `PrincipleVersion` uses a **different status vocabulary** from `ClaimVersion` | The two vocabularies are disjoint; no value appears in both | Schema diff |
| 3 | **E2** | **In-place mutation.** Attempt a field-level edit of `HYP-001` v1 through the API | Refused with a conflict; a successor version is required — ACC-57 | Refusal transcript |
| 4 | **E2** | **Store-level mutation.** Attempt the same edit directly against the underlying store | Refused. An invariant enforced only at the API is not an invariant | Refusal transcript |
| 5 | E1 | Create v2 through the evolution path with operator `ADDRESS_COUNTEREVIDENCE` | v2 names v1 as parent and records the operator; v1's digest is unchanged | Both versions |
| 6 | E1 | Exercise each evolution operator once: refine scope, combine, split, narrow, generalise | Each produces a successor; `GENERALIZE` additionally requires the review its assurance class specifies | Transcript per operator |
| 7 | **E2** | **Priority is not confidence.** Attempt to write a tournament rank into a `ClaimAssessment` | Refused by schema and by policy — the two are separately typed | Refusal transcript |
| 8 | E1 | Record an anomaly that challenges a principle | The principle moves to `CHALLENGED`; the prior version is retained in full | Principle history |
| 9 | **E2** | **Anomaly cannot overwrite.** Attempt to have the anomaly edit the principle in place | Refused; a challenge creates a successor | Refusal transcript |
| 10 | **E1** | **Deterministic rebuild.** Drop the proximity projection and rebuild it from canonical records twice | Both rebuilds are byte-identical; the projection holds no state of its own | Two rebuild digests |
| 11 | E1 | Reconstruct a multi-generation hypothesis family from canonical records alone | Every version, parent, operator, evidence link and principle link resolves; no history is missing | Reconstruction report |
| 12 | E1 | Break an assumption and trace which hypotheses and protocols depended on it | The dependent set is returned by query, not by recollection | Query output |
| 13 | E3 | Independent review of one hypothesis family's evolution chain | The reviewer can say which changes were scope refinements and which were responses to evidence, from the record | `ReviewRecord` |

Cases 3 and 4 exist as a pair on purpose. An invariant that holds at the API and
not at the store is a convention with a nicer error message, and the second case
is the one that finds out.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-143   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-143 --gate G2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-143/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-143
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-143_hypothesis_principle_evolution.acceptance.md) reaches the decision — issuance is not acceptance.

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
