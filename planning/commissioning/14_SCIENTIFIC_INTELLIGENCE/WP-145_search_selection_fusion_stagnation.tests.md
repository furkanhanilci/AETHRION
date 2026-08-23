# WP-145 — Search Selection, Cross-Branch Fusion and Stagnation Control — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-145` |
| Work package | [`WP-145` — Search Selection, Cross-Branch Fusion and Stagnation Control](WP-145_search_selection_fusion_stagnation.md) |
| Companion | [acceptance criteria](WP-145_search_selection_fusion_stagnation.acceptance.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **FinOps Lead / Assurance Lead** — the independent verifier |
| Accountable owner | Experiment Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-145` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 4 acceptance scenario(s) · effort class L |
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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | FinOps Lead / Assurance Lead | At completion |
| `WP-083` accepted output | ExperimentBatch and Staged Execution | Scientific Engineering Lead | Before the first test case runs |
| `WP-100` accepted output | Cost Ledger, Budget Envelopes and FinOps | FinOps Lead | Before the first test case runs |
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
| C01 | `Selection mechanism specification` | Mandatory deliverable | *(name the test case)* |
| C02 | `SearchPolicyConfig` | Mandatory deliverable | *(name the test case)* |
| C03 | `FusionProposal` | Mandatory deliverable | *(name the test case)* |
| C04 | `StagnationDetector` | Mandatory deliverable | *(name the test case)* |
| C05 | `ResearchCampaignGovernor` | Mandatory deliverable | *(name the test case)* |
| C06 | `CampaignStopRecord` | Mandatory deliverable | *(name the test case)* |
| C07 | Write the selection mechanism specification and its fixtures before implementing | WP-145-T01 | *(name the test case)* |
| C08 | Implement the selector with metric-direction, tie and missing-value handling | WP-145-T02 | *(name the test case)* |
| C09 | Define `SearchPolicyConfig` and the early, mid and late phase profiles | WP-145-T03 | *(name the test case)* |
| C10 | Implement `FusionProposal` with named mechanism inheritance and compatibility checks | WP-145-T04 | *(name the test case)* |
| C11 | Implement the stagnation detector and its configured actions | WP-145-T05 | *(name the test case)* |
| C12 | Implement the campaign governor against `ResearchBudgetContract` | WP-145-T06 | *(name the test case)* |
| C13 | Implement reserved budgets that exploration cannot consume | WP-145-T07 | *(name the test case)* |
| C14 | Budget Hard Stop | [ACC-09](../12_ACCEPTANCE_SCENARIOS/ACC-09_budget_hard_stop.md) — Critical | *(name the test case)* |
| C15 | Cross-Branch Fusion Lineage | [ACC-58](../12_ACCEPTANCE_SCENARIOS/ACC-58_cross_branch_fusion_lineage.md) — High | *(name the test case)* |
| C16 | Discovery Search Stagnation | [ACC-59](../12_ACCEPTANCE_SCENARIOS/ACC-59_discovery_search_stagnation.md) — High | *(name the test case)* |
| C17 | Reserved Assurance Budget Is Unreachable | [ACC-101](../12_ACCEPTANCE_SCENARIOS/ACC-101_budget_hard_stop_reserved_assurance.md) — Critical | *(name the test case)* |

**17 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-144 supplies a persisted search graph; WP-100 supplies a cost ledger so budget stops are real rather than simulated; a fixed graph fixture with known metrics exists for the selection cases.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `SearchPolicyConfig`, `FusionProposal` and `ResearchBudgetContract` against their schemas | All three validate; at least one stop condition is required and a configuration with none is refused | Validator output |
| 2 | **E1** | **Fixed-graph selection.** Run the selector against the fixture with `direction: MAXIMIZE` | The expected node is selected, and the selection trace names the exploit and explore terms separately | Selection trace |
| 3 | **E1** | **Direction.** Run the same fixture with `direction: MINIMIZE` | The expected node under minimisation is selected. Metric direction is honoured, not assumed | Selection trace |
| 4 | E1 | Run the fixture with two nodes at identical metrics, and again with a node whose metric is missing | Ties resolve deterministically by the stated rule; a missing metric does not become zero | Two traces |
| 5 | **E1** | **Interior nodes remain eligible.** Confirm a previously expanded non-leaf node can be selected again | It is eligible, and the trace shows why | Selection trace |
| 6 | **E1** | **Determinism.** Run the selector twice on the same snapshot and configuration | Identical decisions. Arithmetic that varies between runs cannot be replayed or audited | Two traces |
| 7 | **E2** | **Priority is not confidence.** Attempt to write a normalised selection reward into a `VerifiedValue` or a claim assessment | Refused by schema and by policy | Refusal transcript |
| 8 | E1 | Propose a fusion naming which mechanism comes from which parent, with an expected interaction and a falsification condition | Accepted; the proposal records all four | `FusionProposal` |
| 9 | **E2** | **Incompatible fusion.** Propose a fusion of two mechanisms the compatibility rules forbid | A policy check is raised rather than a silently combined candidate | Check output |
| 10 | **E1** | **Stagnation boundary.** Run a plateau fixture and observe the detector one iteration **before** the configured window, and at it | Silent before; fires at the boundary — ACC-59 | Two detector outputs |
| 11 | E1 | Confirm the configured action on stagnation is the one in `SearchPolicyConfig` | The recorded policy decides, not a model's preference | Campaign record |
| 12 | **E2** | **Budget boundary.** Drive a campaign to each cap in turn — cost, rounds, experiments, compute, convergence patience | Each stops at its boundary and the `CampaignStopRecord` names which fired | Five stop records |
| 13 | **E2** | **A stop is not an acceptance.** Attempt to satisfy a gate with a `STOPPED_BY_BUDGET` campaign | Refused — ACC-09 | Refusal transcript |
| 14 | **E2** | **Reserved budget.** Attempt to spend the VERIFY, FULL or G7 reproduction reserve on exploration | Refused; the reserve is unreachable from the exploration path | Refusal transcript |
| 15 | **E4** | **Phase policy is recorded.** Run early, mid and late phases and restore the campaign | The phase configuration in force at each point is recoverable with its results | Campaign export |
| 16 | E3 | Independent review of one campaign's allocation record | The reviewer can say why compute went where it went, without asking the producer | `ReviewRecord` |

Case 13 is the one that matters outside this package. Every other case makes the
search well-behaved; this one stops a campaign that merely ran out of money from
being read as a campaign that concluded something.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-145   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-145 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-145/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-145
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-145_search_selection_fusion_stagnation.acceptance.md) reaches the decision — issuance is not acceptance.

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
