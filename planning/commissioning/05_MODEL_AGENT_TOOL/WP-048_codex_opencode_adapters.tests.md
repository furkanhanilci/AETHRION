# WP-048 — Harness Runtime Adapters: Claude Code, Codex, OpenCode, Hermes and Direct Worker — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-048` |
| Work package | [`WP-048` — Harness Runtime Adapters: Claude Code, Codex, OpenCode, Hermes and Direct Worker](WP-048_codex_opencode_adapters.md) |
| Companion | [acceptance criteria](WP-048_codex_opencode_adapters.acceptance.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Security / Eval Office** — the independent verifier |
| Accountable owner | Agent Runtime Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-048` |

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
| Target revision | The single commit every result is bound to | Agent Runtime Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Agent Runtime Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Security / Eval Office | At completion |
| `WP-023` accepted output | Git, Worktree and Protected-Path Policy | Engineering Lead | Before the first test case runs |
| `WP-027` accepted output | Git, OCI Registry and Build Provenance Foundation | Supply Chain Security Lead | Before the first test case runs |
| `WP-046` accepted output | LangGraph Bounded Cognition Runtime | Agent Platform Lead | Before the first test case runs |
| `WP-047` accepted output | Role and Skill Registries, and the Task Compiler | Agent Platform Lead | Before the first test case runs |

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
| C01 | `Runtime adapter SDK` | Mandatory deliverable | *(name the test case)* |
| C02 | `Codex adapter` | Mandatory deliverable | *(name the test case)* |
| C03 | `OpenCode adapter` | Mandatory deliverable | *(name the test case)* |
| C04 | `Direct worker adapter` | Mandatory deliverable | *(name the test case)* |
| C05 | `Conformance report` | Mandatory deliverable | *(name the test case)* |
| C06 | Write the adapter interface and its lifecycle | WP-048-T01 | *(name the test case)* |
| C07 | Implement the Codex non-interactive task adapter | WP-048-T02 | *(name the test case)* |
| C08 | Implement the OpenCode headless/server adapter | WP-048-T03 | *(name the test case)* |
| C09 | Implement the direct/local queue worker adapter | WP-048-T04 | *(name the test case)* |
| C10 | Bind worktree, sandbox and tool credentials | WP-048-T05 | *(name the test case)* |
| C11 | Add structured results, tracing, cancellation and failure normalisation | WP-048-T06 | *(name the test case)* |
| C12 | Add the **Claude Code** and **Hermes Agent** adapters alongside Codex, OpenCode and the direct worker | WP-048-T20 | *(name the test case)* |
| C13 | Implement **skill discovery and loading** per harness, at the location each expects | WP-048-T21 | *(name the test case)* |
| C14 | Implement **automatic session bootstrap**: the router skill is present on the first turn without being asked for | WP-048-T22 | *(name the test case)* |
| C15 | Map **tools** per harness and reconcile names with the `ToolBundle` | WP-048-T23 | *(name the test case)* |
| C16 | Implement **compaction and restart recovery** so the loaded procedure is not silently lost | WP-048-T24 | *(name the test case)* |
| C17 | Return a **structured result** and an audit trace, including cancellation | WP-048-T25 | *(name the test case)* |
| C18 | Run the **harness acceptance suite** — the same task, the same expected skill set, every harness | WP-048-T26 | *(name the test case)* |
| C19 | Task Runs With No Skill Loaded | [ACC-46](../12_ACCEPTANCE_SCENARIOS/ACC-46_skill_not_loaded.md) — Critical | *(name the test case)* |
| C20 | Harness Starts Without the Skill Bootstrap | [ACC-47](../12_ACCEPTANCE_SCENARIOS/ACC-47_skill_bootstrap_missing.md) — Critical | *(name the test case)* |
| C21 | Non-Waivable Skill Ignored Under Pressure | [ACC-49](../12_ACCEPTANCE_SCENARIOS/ACC-49_skill_ignored_under_pressure.md) — Critical | *(name the test case)* |
| C22 | Procedure Lost to Context Compaction or Restart | [ACC-50](../12_ACCEPTANCE_SCENARIOS/ACC-50_skill_lost_on_compaction.md) — High | *(name the test case)* |

**22 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Adapter interface | E0 | Inspect each adapter | All five implement the same lifecycle | Interface report |
| **TC-02** Contract satisfaction | **E1** | Run one `TaskContract` on each harness | All five accept it unchanged | Five run records |
| **TC-03** Isolation | **E2** | From each harness, write outside the worktree | Refused on all five (WP-023) | Five refusals |
| **TC-04** Tool routing | **E2** | From each harness, call a tool directly rather than through the broker | Refused on all five | Five refusals |
| **TC-05** Tool-name reconciliation | **E1** | Invoke the same logical tool on each harness | All five resolve to the same `ToolDefinition` | Mapping report |
| **TC-06** Unmapped tool | **E2** | Expose a harness-native tool with no `ToolBundle` entry | Refused — an unmapped tool is an unpoliced one | Refusal transcript |
| **TC-07** **Skill discovery** | **E1** | Start a session on each harness | Skills load from the location that harness expects | Five load records |
| **TC-08** **Bootstrap** | **E1** | Issue the first turn on each harness with no instruction to load anything | The router skill is **already present** | Five first-turn transcripts |
| **TC-09** Bootstrap failure | **E2** | Remove the bootstrap wiring on one harness | The absence is **detected**, not silently tolerated | Detection transcript |
| **TC-10** Compaction survival | **E2** | Force compaction mid-task on each harness | The loaded procedure survives, or its loss is detected and recovered | Five transcripts |
| **TC-11** Restart recovery | **E2** | Restart the session mid-task | The procedure reloads before the next action | Five transcripts |
| **TC-12** Structured result | **E1** | Complete a task on each harness | An `AgentResult` in the canonical shape, including `gaps` and `assumptions` | Five results |
| **TC-13** Failure normalisation | **E1** | Force the same failure on each harness | Normalised to the same canonical error class | Five error records |
| **TC-14** Cancellation | **E2** | Cancel mid-task on each harness | All five stop; no effect completes afterwards | Five cancellation traces |
| **TC-15** Audit trace | **E1** | Inspect a completed task on each harness | Same trace shape, same correlation identifier | Five traces |
| **TC-16** **Harness acceptance suite** | **E1** | Run the same task with the same expected skill set on all five | Identical skill selection; differences are failures, not variation | Suite report |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-048 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-048 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-048/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-048
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-048_codex_opencode_adapters.acceptance.md) reaches the decision — issuance is not acceptance.

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
