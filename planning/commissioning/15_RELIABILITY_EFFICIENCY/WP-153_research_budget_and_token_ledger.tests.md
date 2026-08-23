# WP-153 — Research Budget, Token Ledger and Efficiency Control — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-153` |
| Work package | [`WP-153` — Research Budget, Token Ledger and Efficiency Control](WP-153_research_budget_and_token_ledger.md) |
| Companion | [acceptance criteria](WP-153_research_budget_and_token_ledger.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Research Director / SRE Lead** — the independent verifier |
| Accountable owner | FinOps Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-153` |

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
| Target revision | The single commit every result is bound to | FinOps Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | FinOps Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Research Director / SRE Lead | At completion |
| `WP-100` accepted output | Cost Ledger, Budget Envelopes and FinOps | FinOps Lead | Before the first test case runs |
| `WP-145` accepted output | Search Selection, Cross-Branch Fusion and Stagnation Control | Experiment Platform Lead | Before the first test case runs |
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
| C01 | `ResearchBudgetContract` | Mandatory deliverable | *(name the test case)* |
| C02 | `TokenLedgerEntry` | Mandatory deliverable | *(name the test case)* |
| C03 | `Communication degradation ladder` | Mandatory deliverable | *(name the test case)* |
| C04 | `Tool-result reuse` | Mandatory deliverable | *(name the test case)* |
| C05 | `Pareto frontier report` | Mandatory deliverable | *(name the test case)* |
| C06 | Define `ResearchBudgetContract` across the nine dimensions | WP-153-T01 | *(name the test case)* |
| C07 | Define `TokenLedgerEntry` and its seven categories | WP-153-T02 | *(name the test case)* |
| C08 | Implement the communication degradation ladder | WP-153-T03 | *(name the test case)* |
| C09 | Place cohort, assurance route and non-waivable controls outside degradation | WP-153-T04 | *(name the test case)* |
| C10 | Implement `BLOCKED_BUDGET` and the scope-reduction request path | WP-153-T05 | *(name the test case)* |
| C11 | Implement deterministic tool-result reuse with recorded provenance | WP-153-T06 | *(name the test case)* |
| C12 | Emit the quality/cost frontier for the release dossier | WP-153-T07 | *(name the test case)* |
| C13 | Budget Degrades Communication, Not the Cohort | [ACC-099](../12_ACCEPTANCE_SCENARIOS/ACC-099_communication_budget_degradation.md) — Critical | *(name the test case)* |
| C14 | Token Ledger Classification | [ACC-100](../12_ACCEPTANCE_SCENARIOS/ACC-100_token_ledger_classification.md) — High | *(name the test case)* |
| C15 | Reserved Assurance Budget Is Unreachable | [ACC-101](../12_ACCEPTANCE_SCENARIOS/ACC-101_budget_hard_stop_reserved_assurance.md) — Critical | *(name the test case)* |
| C16 | Deterministic Tool-Result Reuse | [ACC-102](../12_ACCEPTANCE_SCENARIOS/ACC-102_tool_result_reuse.md) — Medium | *(name the test case)* |

**16 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-100 supplies the cost ledger; WP-150 supplies the communication policy this degrades; WP-145 supplies the campaign governor this generalises; a campaign with a declared assurance route is available.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `ResearchBudgetContract` across its nine dimensions and `TokenLedgerEntry` across its seven categories | Both validate; a contract with no stop condition is refused | Validator output |
| 2 | **E1** | **Categorisation.** Run a campaign exercising all seven token categories | Every entry categorised; categories sum to the provider total with no remainder — ACC-100 | Ledger extract |
| 3 | **E1** | **Derived ratio.** Compute coordination overhead from the ledger | Derivable, and agrees with an independent count of inter-agent messages | Two independent counts |
| 4 | **E1** | **Degradation ladder.** Drive spend through each communication threshold | Structured → compressed → pointer-only → silence-unless-material, in order — ACC-099 | Policy per threshold |
| 5 | **E2** | **Cohort is outside.** Confirm cohort size through every threshold | Unchanged. Budget pressure never reduces the cohort | Cohort records |
| 6 | **E2** | **Assurance is outside.** Confirm the assurance route through every threshold | Unchanged. No required verification is skipped for budget | Route records |
| 7 | **E2** | **Terminal state.** Drive spend to exhaustion | `BLOCKED_BUDGET` or a scope-reduction request — never a cheaper completion | Stop record |
| 8 | **E2** | **Reserves.** Attempt to consume the verification, reproduction and assurance reserves from exploration | Each unreachable from the exploration path — ACC-101 | Three refusal transcripts |
| 9 | E1 | Run the reserved assurance and reproduction work after the exploration stop | Affordable; the reserve did its job | Run records |
| 10 | **E2** | **A stop is not an acceptance.** Attempt to satisfy a gate with a stopped campaign | Refused | Refusal transcript |
| 11 | **E1** | **Tool reuse.** Call a deterministic tool twice with identical inputs inside the freshness window | Second call served from the record and **marked reused** — ACC-102 | Two invocation records |
| 12 | **E2** | **Freshness boundary.** Call again across a declared freshness boundary | Re-executes | Invocation record |
| 13 | **E2** | **Non-deterministic tools.** Attempt reuse for a non-deterministic tool | Never reused | Refusal transcript |
| 14 | E1 | Produce the quality/cost frontier for the campaign | Both axes reported; neither direction accepted silently | Frontier report |
| 15 | E3 | Independent review of one campaign's ledger and stop record | The reviewer can say where the money went and why the campaign ended | `ReviewRecord` |

Cases 5 and 6 are the reason this package exists. Every other budget mechanism
here is ordinary FinOps; these two are what stop a cost optimiser from buying its
savings out of the assurance budget, which is the cheapest saving available and
the most expensive one to discover later.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-153   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-153 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-153/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-153
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-153_research_budget_and_token_ledger.acceptance.md) reaches the decision — issuance is not acceptance.

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
