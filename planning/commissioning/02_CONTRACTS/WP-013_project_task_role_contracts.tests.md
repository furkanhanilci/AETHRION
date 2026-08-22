# WP-013 — Project, Task, Role and Skill Contract Schemas — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-013` |
| Work package | [`WP-013` — Project, Task, Role and Skill Contract Schemas](WP-013_project_task_role_contracts.md) |
| Companion | [acceptance criteria](WP-013_project_task_role_contracts.acceptance.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Governance Lead** — the independent verifier |
| Accountable owner | Control Plane Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-013` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | no | no scenario and not L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Control Plane Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Control Plane Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Governance Lead | At completion |
| `WP-003` accepted output | Role Catalogue and RACI Baseline | Governance Lead | Before the first test case runs |
| `WP-004` accepted output | Human Decision, SLA, Delegation and Escalation Policy | Project Decision Owner | Before the first test case runs |
| `WP-005` accepted output | Research Risk and Assurance Profile | Safety & Governance Owner | Before the first test case runs |
| `WP-006` accepted output | ExecutionProfile and Route Policy | Platform Security Lead | Before the first test case runs |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |

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
| C01 | `ProjectContract schemas` | Mandatory deliverable | *(name the test case)* |
| C02 | `TaskContract schema` | Mandatory deliverable | *(name the test case)* |
| C03 | `RoleContract schema` | Mandatory deliverable | *(name the test case)* |
| C04 | `AgentResult schema` | Mandatory deliverable | *(name the test case)* |
| C05 | `Contract examples` | Mandatory deliverable | *(name the test case)* |
| C06 | Define the `ProjectCharter` and `ControlPlan` contract | WP-013-T01 | *(name the test case)* |
| C07 | Write the `TaskContract` input, output, non-goal and acceptance fields | WP-013-T02 | *(name the test case)* |
| C08 | Add the `RoleContract` mandate, tool, data, risk and prohibited-action fields | WP-013-T03 | *(name the test case)* |
| C09 | Define the `AgentResult` format including gaps and assumptions | WP-013-T04 | *(name the test case)* |
| C10 | Write the backward-compatibility and contract versioning rules | WP-013-T05 | *(name the test case)* |
| C11 | Add the **skill binding fields** to `TaskContract` (see below) and make `skill_bundle_hash` part of the evidence chain | WP-013-T06 | *(name the test case)* |
| C12 | Add the **classification fields** `work_domain`, `research_mode` and `execution_path`, with fail-closed defaults | WP-013-T07 | *(name the test case)* |
| C13 | Define `RoleBinding` so that a **role is a function, not a person**: separation and combination constraints instead of headcount | WP-013-T08 | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-011 and WP-007 are `ACCEPTED`; a task can be dispatched to
a stub agent runtime.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `ProjectCharter`, `ControlPlan`, `TaskContract`, `RoleContract`, `AgentResult` against their schemas | All five validate; every mandatory field is present | Schema validation output |
| 2 | **E0** | **Provider-leak test.** Scan every canonical contract for provider-specific field names | Zero. `temperature`, `top_p`, `system`, model-vendor names and SDK types must not appear | Leak scan report |
| 3 | E0 | Confirm `TaskContract` carries `skill_bundle_hash`, `work_domain`, `research_mode` and `execution_path` | All four present and mandatory | Schema |
| 4 | **E2** | **Fail-closed classification test.** Dispatch a task with `work_domain` unset | Rejected, or defaulted to the **most restrictive** path and flagged — never the permissive one | Rejection transcript |
| 5 | **E2** | **Skill-bundle test.** Run the same task under two skill bundles | The two results carry **different** `skill_bundle_hash` values, and the evidence chain distinguishes them | Two evidence records |
| 6 | **E2** | **Comparability test.** Attempt to compare two results produced under different skill bundles as if equivalent | Refused, or flagged as non-comparable | Refusal transcript |
| 7 | **E1** | **`AgentResult` completeness test.** Run ten real tasks and inspect `gaps` and `assumptions` | Non-empty on tasks where gaps genuinely exist. **A field that is always empty has not been implemented, only declared** | Ten results with the non-empty rate |
| 8 | **E2** | **`RoleBinding` separation test.** Bind producer and verifier to one actor | Rejected by the separation constraint, not by a headcount check | Rejection transcript |
| 9 | E1 | Confirm a `RoleBinding` legally holds several roles when no separation constraint is violated | Accepted, and the held set is recorded | Binding record |
| 10 | **E2** | **Compatibility test.** Publish a v1 contract, add an optional field as v1.1, then change a field type as v2 | v1.1 accepted as compatible; v2 refused for existing v1 consumers | Compatibility transcript |
| 11 | **E2** | **Redefinition test.** Republish v1 with different content | Rejected — a registered version is never redefined | Rejection transcript |
| 12 | E1 | Confirm the contract examples in the deliverable set validate against their own schemas | Zero examples that fail their schema | Fixture run |
| 13 | E3 | Independent review for provider leakage the scan cannot see — a field that is generic in name and provider-shaped in semantics | Any found is a finding | `ReviewRecord` |

Step 7 is the one that distinguishes this package from a schema exercise. Steps 2
and 13 together are the vendor-lock-in control, and only the second can catch a
`max_tokens` renamed to `output_budget`.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-013 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-013 --gate G0–G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-013/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-013
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-013_project_task_role_contracts.acceptance.md) reaches the decision — issuance is not acceptance.

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
