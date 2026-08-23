# WP-151 — Memory Masking and Proactive Intervention — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-151` |
| Work package | [`WP-151` — Memory Masking and Proactive Intervention](WP-151_memory_masking_and_intervention.md) |
| Companion | [acceptance criteria](WP-151_memory_masking_and_intervention.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Assurance Lead / Archivist** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-151` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 3 acceptance scenario(s) |
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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead / Archivist | At completion |
| `WP-146` accepted output | Epistemic Memory Taxonomy and Retention | Knowledge Lead | Before the first test case runs |
| `WP-150` accepted output | Communication Governor, Edge Utility and Context Projection | Chief Architect | Before the first test case runs |

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
| C01 | `MemoryMask policy` | Mandatory deliverable | *(name the test case)* |
| C02 | `MemoryInterventionRecord` | Mandatory deliverable | *(name the test case)* |
| C03 | `Memory poisoning fixture suite` | Mandatory deliverable | *(name the test case)* |
| C04 | Define `MemoryMask` policy and its seven evaluation dimensions | WP-151-T01 | *(name the test case)* |
| C05 | Implement exclusion of refuted, superseded and stale items from reasoning context | WP-151-T02 | *(name the test case)* |
| C06 | Preserve full visibility of excluded items to failure-history queries | WP-151-T03 | *(name the test case)* |
| C07 | Define `MemoryInterventionRecord` and the reminder emission rule | WP-151-T04 | *(name the test case)* |
| C08 | Bind the mask to the context projection of WP-150 | WP-151-T05 | *(name the test case)* |
| C09 | Build the memory-poisoning fixture suite | WP-151-T06 | *(name the test case)* |
| C10 | A Refuted Memory Does Not Re-Enter Reasoning | [ACC-096](../12_ACCEPTANCE_SCENARIOS/ACC-096_refuted_memory_mask.md) — High | *(name the test case)* |
| C11 | Proactive Reminder of a Frozen Constraint | [ACC-097](../12_ACCEPTANCE_SCENARIOS/ACC-097_proactive_frozen_constraint_reminder.md) — High | *(name the test case)* |
| C12 | Memory Poisoning Attempt | [ACC-098](../12_ACCEPTANCE_SCENARIOS/ACC-098_memory_poisoning_attempt.md) — Critical | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-146 supplies the six typed stores; WP-150 supplies the context projection this mask filters; a frozen analysis plan with an explicit stopping rule exists so a material reminder has something to be material about.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate the `MemoryMask` policy and `MemoryInterventionRecord` | Both validate; the seven mask dimensions are required | Validator output |
| 2 | E1 | Seed refuted, superseded, stale and current items in one store | All four stored with distinct epistemic status | Store contents |
| 3 | **E2** | **Refuted excluded.** Assemble a reasoning context over that store | No refuted, superseded or stale item appears — ACC-096 | `ContextProjectionRecord` |
| 4 | **E1** | **Discrimination control.** Confirm the current items do appear | Present. A mask that empties the context is not a mask | Projection contents |
| 5 | **E1** | **History remains queryable.** Run a failure-history query over the same store | All three excluded items are returned | Query result |
| 6 | E1 | Compare stored items before and after masking | Nothing deleted, nothing re-labelled — the mask is a read policy | Before/after digests |
| 7 | **E2** | **Stale is not evidence.** Attempt to cite a `MethodExperience` entry in support of a claim | Refused | Refusal transcript |
| 8 | **E1** | **Material reminder.** Drive an agent toward a step that violates the frozen stopping rule | A reminder fires carrying canonical artifact references — ACC-097 | `MemoryInterventionRecord` |
| 9 | **E1** | **Selective, not per-turn.** Run an ordinary step with no constraint at stake | No reminder fires | Step record |
| 10 | **E2** | **Reminder creates nothing.** Inspect canonical state after the reminder | No `ClaimVersion` and no new assertion was created | State comparison |
| 11 | **E2** | **Poisoning.** Pass crafted untrusted content through quarantine and attempt retrieval as evidence | Lands in a store whose authority forbids claim support; unretrievable as evidence — ACC-098 | Denial transcript |
| 12 | **E2** | **Derived lesson is not fact.** Attempt to support a claim with a lesson from a `FailedApproach` | Refused | Refusal transcript |
| 13 | E3 | Independent review of one masked projection against the unmasked store | The reviewer can say what was withheld and why | `ReviewRecord` |

Cases 3 and 5 are a pair and neither is sufficient alone. Excluding a refuted item
from reasoning is only correct if the same item is still answerable to *what did
we already try* — otherwise the mask has destroyed the failure record WP-146
exists to keep.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-151   # dependencies and their states
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

A case in **bold** is a refusal or an injection: it passes when the system
declines to act, or when a deliberately caused fault is caught. Most of this
table is one or the other, because a reliability package that only exercises the
happy path has tested the thing that was never in doubt.

### Capturing evidence

```bash
python3 scripts/evidence_manifest.py issue --package WP-151 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-151/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-151
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-151_memory_masking_and_intervention.acceptance.md) reaches the decision — issuance is not acceptance.

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
