---
title: "WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release — Test Procedures"
aliases:
  - "WP-107 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-107_engineering_vertical_slice.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/engineering
  - aethrion/gate/g5-g9
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-107 — Engineering Vertical Slice — Spec, Worktree, Signed Release — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-107` |
| Work package | [`WP-107` — Engineering Vertical Slice — Spec, Worktree, Signed Release](wp_107_engineering_vertical_slice.md) |
| Companion | [acceptance criteria](wp_107_engineering_vertical_slice.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Independent Technical Reviewer / Reproducer** — the independent verifier |
| Accountable owner | Engineering Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-107` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 3 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5–G9 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Engineering Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Engineering Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Independent Technical Reviewer / Reproducer | At completion |
| `WP-023` accepted output | Git, Worktree and Protected-Path Policy | Engineering Lead | Before the first test case runs |
| `WP-024` accepted output | CI Foundation and Deterministic Quality Gates | Engineering Productivity Lead | Before the first test case runs |
| `WP-027` accepted output | Git, OCI Registry and Build Provenance Foundation | Supply Chain Security Lead | Before the first test case runs |
| `WP-032` accepted output | ProjectLifecycle Workflow Skeleton | Workflow Engineering Lead | Before the first test case runs |
| `WP-045` accepted output | Policy Router and Minimum-Sufficient Model Package | Model Platform Lead | Before the first test case runs |
| `WP-047` accepted output | Role and Skill Registries, and the Task Compiler | Agent Platform Lead | Before the first test case runs |
| `WP-048` accepted output | Harness Runtime Adapters: Claude Code, Codex, OpenCode, Hermes and Direct Worker | Agent Runtime Lead | Before the first test case runs |
| `WP-049` accepted output | Tool Registry and Tool Broker Core | Tool Platform Lead | Before the first test case runs |
| `WP-054` accepted output | gVisor Sandbox and Execution Cell Lifecycle | Execution Security Lead | Before the first test case runs |
| `WP-059` accepted output | Supply-Chain Admission, Sigstore and SLSA Policy | Supply Chain Security Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |
| `WP-086` accepted output | Frozen and Blind Review Package Builder | Assurance Platform Lead | Before the first test case runs |
| `WP-087` accepted output | Mechanical Verification Engine | Verification Engineering Lead | Before the first test case runs |
| `WP-089` accepted output | DisagreementCase and Evidence-Weighted Arbitration | Assurance Lead / Arbiter | Before the first test case runs |
| `WP-090` accepted output | PublicationPackage, RO-Crate and Provenance Export | Provenance Curator | Before the first test case runs |
| `WP-096` accepted output | OpenTelemetry End-to-End Correlation Spine | Observability Lead | Before the first test case runs |

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
| C01 | `Engineering vertical dossier` | Mandatory deliverable | *(name the test case)* |
| C02 | `Frozen review packets` | Mandatory deliverable | *(name the test case)* |
| C03 | `Validated findings` | Mandatory deliverable | *(name the test case)* |
| C04 | `Signed OCI/release` | Mandatory deliverable | *(name the test case)* |
| C05 | `Merge DecisionRecord` | Mandatory deliverable | *(name the test case)* |
| C06 | Create the B/C risk fixtures and the technical specification | WP-107-T01 | *(name the test case)* |
| C07 | Open the plan reality check, protected-path check and the worktree | WP-107-T02 | *(name the test case)* |
| C08 | Run the agent implementation and CI verification | WP-107-T03 | *(name the test case)* |
| C09 | Perform blind and cross-family review of the frozen diff | WP-107-T04 | *(name the test case)* |
| C10 | Apply the reproducer and correction loop to HIGH/BLOCKER findings | WP-107-T05 | *(name the test case)* |
| C11 | Re-freeze, re-review, produce a signed build and take the human merge decision | WP-107-T06 | *(name the test case)* |
| C12 | Planner Self-Approval Attempt | [ACC-06](../12_ACCEPTANCE_SCENARIOS/acc_06_plan_self_approval.md) — Critical | *(name the test case)* |
| C13 | Unsigned or Mutable Image | [ACC-17](../12_ACCEPTANCE_SCENARIOS/acc_17_unsigned_image.md) — Critical | *(name the test case)* |
| C14 | Artifact Overwrite Attempt | [ACC-23](../12_ACCEPTANCE_SCENARIOS/acc_23_artifact_overwrite.md) — Critical | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Fixtures | E0 | Prepare a B-class and a C-class change | Both realistic; risk dimensions documented | Fixtures |
| **TC-02** Specification | **E1** | Author the technical specification | Testable acceptance criteria naming a command or a threshold | Specification |
| **TC-03** Untestable spec | **E2** | Submit a spec with no measurable criterion | Refused | Refusal transcript |
| **TC-04** **Plan reality check** | **E1** | Check the plan against the repository | Every referenced symbol, file and API **resolves** | Reality-check report |
| **TC-05** Stale plan | **E2** | Reference a function that does not exist | **Caught before implementation** | Detection record |
| **TC-06** Worktree | **E1** | Open the agent worktree | Pinned to a commit; allowed-path manifest applied (WP-023) | Worktree state |
| **TC-07** **Protected path** | **E2** | Attempt a change touching a protected path | Refused at the worktree boundary | Refusal transcript |
| **TC-08** Scope escalation | **E2** | Supply a task description requesting wider paths | Manifest unchanged; the attempt audited | Audit record |
| **TC-09** Implementation | **E1** | Run the agent implementation | Diff produced within scope; `AgentResult` carries gaps and assumptions | Diff · result |
| **TC-10** **CI verification** | **E1** | Run the pipeline on the diff | All gates run; results bound to one revision | CI run |
| **TC-11** Gate failure | **E2** | Introduce a lint, type, schema and security violation | **Each fails the build** | Four failing runs |
| **TC-12** **Blind diff review** | **E1** | Freeze and dispatch the diff | Diff against the producer's workspace shows **zero trace artifacts** | Packet diff |
| **TC-13** Authorship leak | **E2** | Seed an authorship signal in commit structure or comments | **Detected by the leak detector** | Detection record |
| **TC-14** Cross-family review | **E1** | Review the C-class change across model families | Two families; verdicts sealed | `ReviewRecord`s |
| **TC-15** **Correction loop** | **E1** | Produce a HIGH finding, correct, **re-freeze**, re-review | The corrected diff is re-reviewed from a new frozen package | Loop transcript |
| **TC-16** Merge with open finding | **E2** | Attempt to merge with an open BLOCKER | **Refused** | Refusal transcript |
| **TC-17** Reproducer | **E1** | Reproduce a finding independently | Reproduction record; the finding is confirmed or dismissed with a reason | Reproduction record |
| **TC-18** Architecture gate | **E2** | Introduce a forbidden import | Refused (WP-022) | Refusal transcript |
| **TC-19** **Risk divergence** | **E1** | Compare the B and C paths | **Visibly different**: review depth, reproduction requirement and approval differ | Comparison |
| **TC-20** Signed build | **E1** | Produce the release | Digest-pinned, signed, provenance verifies (WP-027) | Provenance |
| **TC-21** **Human merge decision** | **E1** | Take the merge decision | Rationale recorded; MFA at signing; residual risk named | `DecisionRecord` |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-107 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-107 --gate G5–G9,Engineering \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-107/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-107
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_107_engineering_vertical_slice.acceptance.md) reaches the decision — issuance is not acceptance.

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
