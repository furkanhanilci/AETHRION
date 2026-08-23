# WP-047 — Role and Skill Registries, and the Task Compiler — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-047` |
| Work package | [`WP-047` — Role and Skill Registries, and the Task Compiler](WP-047_role_bundle_registry.md) |
| Companion | [acceptance criteria](WP-047_role_bundle_registry.acceptance.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Governance / Eval Office** — the independent verifier |
| Accountable owner | Agent Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-047` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Agent Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Agent Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Governance / Eval Office | At completion |
| `WP-003` accepted output | Role Catalogue and RACI Baseline | Governance Lead | Before the first test case runs |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-013` accepted output | Project, Task, Role and Skill Contract Schemas | Control Plane Lead | Before the first test case runs |
| `WP-020` accepted output | Schema Registry, Compatibility and Contract SDK | Platform Architecture Lead | Before the first test case runs |
| `WP-042` accepted output | Capability Registry and Profile Lifecycle | Eval Office | Before the first test case runs |
| `WP-045` accepted output | Policy Router and Minimum-Sufficient Model Package | Model Platform Lead | Before the first test case runs |
| `WP-046` accepted output | LangGraph Bounded Cognition Runtime | Agent Platform Lead | Before the first test case runs |

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
| C01 | `Role Bundle Registry` | Mandatory deliverable | *(name the test case)* |
| C02 | `Core role bundles` | Mandatory deliverable | *(name the test case)* |
| C03 | `Bundle conformance tests` | Mandatory deliverable | *(name the test case)* |
| C04 | `Cohort, topology, projection and assurance-route compilation` | Mandatory deliverable | *(name the test case)* |
| C05 | Build the `RoleBundle` schema and its Git registry | WP-047-T01 | *(name the test case)* |
| C06 | Write the `RoleContract` → runtime prompt/tool/context compiler | WP-047-T02 | *(name the test case)* |
| C07 | Create the initial bundles for planner, scout, extractor, methodologist, coder, reviewer, reproducer and curator | WP-047-T03 | *(name the test case)* |
| C08 | Bind the context budget and frozen-package policy | WP-047-T04 | *(name the test case)* |
| C09 | Add bundle signature, admission and evaluation references | WP-047-T05 | *(name the test case)* |
| C10 | Establish deprecation and migration management | WP-047-T06 | *(name the test case)* |
| C11 | Build the **Skill Registry**: discovery, the Agent Skills format contract, and `scripts/validate_skills.py` as an admission gate | WP-047-T07 | *(name the test case)* |
| C12 | Implement **trigger resolution** — classification fields → `skills_required` — with a recorded `skill_selection_reason` | WP-047-T08 | *(name the test case)* |
| C13 | Implement **version and dependency resolution** across `airl.requires_skills`, including conflict refusal | WP-047-T09 | *(name the test case)* |
| C14 | Compute and record `skill_bundle_hash`; bind it into `TaskContract` and the evidence chain | WP-047-T10 | *(name the test case)* |
| C15 | Enforce the **two-family policy**: engineering, scientific-research and shared, selected from `work_domain` — never chosen freely by the agent | WP-047-T11 | *(name the test case)* |
| C16 | Track **upstream provenance**: `airl.derived_from` + `airl.upstream_commit`, and flag derived skills when upstream moves | WP-047-T12 | *(name the test case)* |

**16 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Bundle schema | E0 | Compile a `RoleBundle` | Mandate, prompt, I/O schemas, allowed tools, context budget, eval refs all present | Bundle |
| **TC-02** Compiler fidelity | **E1** | Compile the same `RoleContract` twice | Identical bundle hash | Two hashes |
| **TC-03** Unsigned bundle | **E2** | Load a bundle with no signature | Refused | Refusal transcript |
| **TC-04** Tool scope | **E2** | Have a bundle request a tool outside its allowed set | Refused at the broker, naming the bundle | Refusal transcript |
| **TC-05** Context budget | **E2** | Exceed the declared context budget | Refused or truncated per policy — never silently exceeded | Transcript |
| **TC-06** Frozen package | **E1** | Compile a reviewer bundle | Its context contains no producer trace (WP-007) | Packet diff |
| **TC-07** **Skill admission gate** | **E2** | Register a skill failing `validate_skills.py` | **Does not load.** The validator is a gate, not a report | Refusal transcript |
| **TC-08** Trigger resolution | **E1** | Dispatch a task whose classification implies one skill | The skill loads and `skill_selection_reason` is recorded | Selection record |
| **TC-09** Competing skills | **E2** | Dispatch a task matching two skills | Resolves deterministically **or refuses** — never picks silently | Transcript |
| **TC-10** No matching skill | **E2** | Dispatch an uncovered task | Detected and reported, not run bare | Transcript |
| **TC-11** Dependency resolution | **E1** | Load a skill declaring `airl.requires_skills` | Dependencies resolve; the closure is recorded | Resolution record |
| **TC-12** Version conflict | **E2** | Require two incompatible skill versions | **Refused.** No arbitrary winner | Refusal transcript |
| **TC-13** **`skill_bundle_hash`** | **E1** | Run one task under two skill bundles | Different hashes; both reach the evidence chain | Two evidence records |
| **TC-14** Comparability refusal | **E2** | Compare results across differing bundle hashes as equivalent | Refused or flagged non-comparable | Transcript |
| **TC-15** Family policy | **E2** | Have an agent request a family other than the one `work_domain` implies | **Refused.** The family is selected, not chosen | Refusal transcript |
| **TC-16** Upstream drift | **E2** | Move the pinned upstream commit | Every skill carrying `airl.derived_from` is **flagged** | Flag report |
| **TC-17** Vendored integrity | **E1** | Diff the eleven vendored skills against their pinned commit | Byte-identical, or the difference is a finding | Diff report |
| **TC-18** Deprecation | **E2** | Deprecate a bundle with a live consumer | Consumer identified before the cutoff; the cutoff refuses | Deprecation transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-047 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-047 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-047/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-047
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-047_role_bundle_registry.acceptance.md) reaches the decision — issuance is not acceptance.

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
