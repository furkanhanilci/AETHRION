# WP-146 — Epistemic Memory Taxonomy and Retention — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-146` |
| Work package | [`WP-146` — Epistemic Memory Taxonomy and Retention](WP-146_epistemic_memory_taxonomy.md) |
| Companion | [acceptance criteria](WP-146_epistemic_memory_taxonomy.acceptance.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Archivist / Internal Audit** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-146` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Knowledge Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Archivist / Internal Audit | At completion |
| `WP-012` accepted output | Canonical Ownership and Field-Level Authority Matrix | Chief Architect | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-144` accepted output | Discovery Search Graph and Candidate Lifecycle | Experiment Platform Lead | Before the first test case runs |

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
| C01 | `Six memory type contracts` | Mandatory deliverable | *(name the test case)* |
| C02 | `FindingRecord` | Mandatory deliverable | *(name the test case)* |
| C03 | `FailedApproach` | Mandatory deliverable | *(name the test case)* |
| C04 | `NegativeResult` | Mandatory deliverable | *(name the test case)* |
| C05 | `MethodExperience` | Mandatory deliverable | *(name the test case)* |
| C06 | `MemoryQuery policy` | Mandatory deliverable | *(name the test case)* |
| C07 | `Retention and revalidation jobs` | Mandatory deliverable | *(name the test case)* |
| C08 | Define the six memory type contracts and their authority matrix rows | WP-146-T01 | *(name the test case)* |
| C09 | Define `FindingRecord`, `FailedApproach` and `NegativeResult` | WP-146-T02 | *(name the test case)* |
| C10 | Define `MethodExperience` with freshness, decay and revalidation | WP-146-T03 | *(name the test case)* |
| C11 | Define `SearchExperience` and its separation from the evidence store | WP-146-T04 | *(name the test case)* |
| C12 | Implement the typed `MemoryQuery` API and its role-aware policy | WP-146-T05 | *(name the test case)* |
| C13 | Implement retention and decay jobs with immutable-class exclusion reporting | WP-146-T06 | *(name the test case)* |
| C14 | Implement the G10 impact path across findings, principles and procedures | WP-146-T07 | *(name the test case)* |
| C15 | Failed Experiment Must Be Recorded | [ACC-63](../12_ACCEPTANCE_SCENARIOS/ACC-63_failed_experiment_recorded.md) — High | *(name the test case)* |
| C16 | EvidenceGap Lifecycle | [ACC-70](../12_ACCEPTANCE_SCENARIOS/ACC-70_evidence_gap_lifecycle.md) — High | *(name the test case)* |
| C17 | Epistemic Memory Retention Violation | [ACC-79](../12_ACCEPTANCE_SCENARIOS/ACC-79_memory_retention_violation.md) — High | *(name the test case)* |
| C18 | A Refuted Memory Does Not Re-Enter Reasoning | [ACC-096](../12_ACCEPTANCE_SCENARIOS/ACC-096_refuted_memory_mask.md) — High | *(name the test case)* |
| C19 | Memory Poisoning Attempt | [ACC-098](../12_ACCEPTANCE_SCENARIOS/ACC-098_memory_poisoning_attempt.md) — Critical | *(name the test case)* |

**19 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-026 supplies immutable storage so evidence immutability is real rather than asserted; WP-075 and WP-077 supply the claim and finding chain; a blind review round exists so reviewer isolation can be exercised against a live packet.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate all six memory contracts and confirm the authority matrix names an owner, a reader set and a writer set for each | Six contracts, six complete matrix rows | Validator output |
| 2 | E0 | Confirm exactly one store — Evidence — carries the may-support-a-claim property | One store, not two, and the property is a field rather than a convention | Matrix extract |
| 3 | **E2** | **Evidence does not decay.** Run the procedural-memory decay job against a mixed set containing evidence artifacts and human intervention records | Both immutable classes are excluded, and the job **reports what it excluded and why** — ACC-79 | Exclusion report |
| 4 | **E1** | **Planted controls.** Seed one evidence artifact that must survive and one stale procedure that must expire, then run the same job | The evidence control survives with an unchanged digest **and** the stale procedure expires. A job that touches nothing passes neither half | Before/after digests |
| 5 | **E2** | **Stale procedure is not evidence.** Attempt to cite a `MethodExperience` entry in support of a claim | Refused; only the evidence store may support a claim | Refusal transcript |
| 6 | **E2** | **Reviewer isolation.** From a blind reviewer context, query the producer's search-experience and procedural memory | Denied and audited — ACC-72 | Denial transcript |
| 7 | E1 | Confirm the same reviewer can reach everything the frozen packet does include | Isolation bounds the reviewer's reach without disabling the review | Access transcript |
| 8 | E1 | Record a `FailedApproach` and retrieve it after the campaign closes | Retrievable, with its context, failure class and retry conditions intact | Retrieval output |
| 9 | **E1** | **Distinct contexts are not suppressed.** Retrieve a failed approach for a scientifically different context | The earlier failure is surfaced as context and does **not** block the new attempt | Retrieval output |
| 10 | **E2** | **Retraction cascade.** Retract a source and trace the impact through evidence, findings, claims and principles | Dependent records are flagged; **no raw artifact is deleted** and the historical result stays discoverable | Impact scan |
| 11 | **E2** | **Human audit immutability.** Attempt to edit a `HumanInterventionRecord` | Refused | Refusal transcript |
| 12 | **E1** | **Typed query.** Issue a `MemoryQuery` naming two stores, and separately one that names none | The typed query returns only the named stores; the untyped query is **refused**, not silently widened | Two query results |
| 13 | **E4** | **Rebuild.** Drop the derived retrieval indexes and rebuild them from the canonical stores | Lossless — ACC-71 | Rebuild diff |
| 14 | E3 | Independent review of the retention policy against the authority matrix | The reviewer confirms no job has a path to an immutable class | `ReviewRecord` |

Case 4 is the pair that makes case 3 meaningful. A retention job that excludes
everything and a retention job that is correctly bounded produce the same log,
and only the stale-procedure half tells them apart.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-146   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-146 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-146/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-146
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-146_epistemic_memory_taxonomy.acceptance.md) reaches the decision — issuance is not acceptance.

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
