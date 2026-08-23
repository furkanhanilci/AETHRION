---
title: "WP-130 — Architecture and Platform Continuous Assurance — Test Procedures"
aliases:
  - "WP-130 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/11_DAY2_OPERATIONS/WP-130_architecture_continuous_assurance.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/11-day2-operations
  - aethrion/wave/w9
  - aethrion/effort/m
  - aethrion/gate/g0-g10
  - aethrion/gate/platform
  - aethrion/gate/day-2
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-130 — Architecture and Platform Continuous Assurance — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-130` |
| Work package | [`WP-130` — Architecture and Platform Continuous Assurance](wp_130_architecture_continuous_assurance.md) |
| Companion | [acceptance criteria](wp_130_architecture_continuous_assurance.acceptance.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Architecture Board / Internal Audit** — the independent verifier |
| Accountable owner | Chief Architect / Platform Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-130` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 2 acceptance scenario(s) |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform / Day-2 |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Chief Architect / Platform Assurance Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Chief Architect / Platform Assurance Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Architecture Board / Internal Audit | At completion |
| `WP-010` accepted output | Architecture Decision and Rejected-Alternatives Baseline | Chief Architect | Before the first test case runs |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-040` accepted output | Workflow Replay, Versioning and Failure Test Suite | Platform Assurance Lead | Before the first test case runs |
| `WP-060` accepted output | Agentic Security Attack Suite and Red-Team Acceptance | Red Team Lead | Before the first test case runs |
| `WP-109` accepted output | Acceptance Scenario Registry and Harness | Platform Assurance Lead | Before the first test case runs |
| `WP-115` accepted output | Full System Regression and Commissioning Dossier | Platform Assurance Lead | Before the first test case runs |
| `WP-121` accepted output | Hypercare, Stabilisation and Programme Closure | SRE Lead / Program Lead | Before the first test case runs |
| `WP-123` accepted output | Control Effectiveness and Policy Regression Rhythm | Safety & Governance Owner | Before the first test case runs |
| `WP-124` accepted output | Model Requalification, Drift and Ejection Rhythm | Eval Office | Before the first test case runs |
| `WP-125` accepted output | Literature, Zotero and Obsidian Curation Rhythm | Knowledge Lead | Before the first test case runs |
| `WP-126` accepted output | Reviewer, Judge and Reproducer Calibration | Assurance Lead | Before the first test case runs |
| `WP-127` accepted output | FinOps, Capacity and Portfolio Review Rhythm | FinOps Lead / Research Director | Before the first test case runs |
| `WP-128` accepted output | Incident, Postmortem and Learning Closure | Incident Commander / SRE Lead | Before the first test case runs |
| `WP-129` accepted output | Quarterly DR, Supply-Chain and Audit Drill | SRE Lead / Supply Chain Security | Before the first test case runs |

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
| C01 | `Continuous Assurance report` | Mandatory deliverable | *(name the test case)* |
| C02 | `Architecture drift findings` | Mandatory deliverable | *(name the test case)* |
| C03 | `Golden-path results` | Mandatory deliverable | *(name the test case)* |
| C04 | `ADR/retirement decisions` | Mandatory deliverable | *(name the test case)* |
| C05 | `Assurance backlog` | Mandatory deliverable | *(name the test case)* |
| C06 | `MAS efficiency and Pareto frontier assurance` | Mandatory deliverable | *(name the test case)* |
| C07 | Run the monthly architecture drift and canonical-owner scan | WP-130-T01 | *(name the test case)* |
| C08 | Run the schema, adapter and policy compatibility suite | WP-130-T02 | *(name the test case)* |
| C09 | Execute the golden-path synthetic research and engineering runs | WP-130-T03 | *(name the test case)* |
| C10 | Run a derived graph, index and Obsidian rebuild sample | WP-130-T04 | *(name the test case)* |
| C11 | Review the platform chaos, replay and backup evidence | WP-130-T05 | *(name the test case)* |
| C12 | Produce the ADR reopen triggers, service retirement and technical-debt decisions | WP-130-T06 | *(name the test case)* |
| C13 | Upstream Assimilation Drift | [ACC-73](../12_ACCEPTANCE_SCENARIOS/acc_73_upstream_assimilation_drift.md) — High | *(name the test case)* |
| C14 | Governed Versus Ungoverned Research Harness | [ACC-80](../12_ACCEPTANCE_SCENARIOS/acc_80_governed_versus_ungoverned_harness.md) — Medium | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Architecture drift scan** | **E1** | Run the monthly scan | Every stated invariant checked; deviations listed | Drift report |
| **TC-02** Canonical-owner scan | **E2** | Detect a derivative holding state nothing else has | **Reclassified as canonical**; WP-012's matrix corrected | Correction record |
| **TC-03** Gate-state writer | **E2** | Detect any consumer writing gate state | Flagged as a `PR-07` violation | Flag record |
| **TC-04** **Dependency direction** | **E2** | Run the import linter over the tree | Every declared rule holds; a violation **fails**, not warns | Linter output |
| **TC-05** **Contract with no consumer** | **E2** | Detect a published contract nothing consumes | Flagged — *bind it or delete it* (finding **H4**'s rule) | Flag record |
| **TC-06** Schema compatibility | **E1** | Run the compatibility suite | Every producer/consumer pair green | Suite report |
| **TC-07** **Adapter drift** | **E2** | Change a provider response shape behind an adapter | **Detected** — the canonical contract must not silently diverge from what is stored | Detection record |
| **TC-08** Policy compatibility | **E1** | Run the policy suite against current bundles | All pass; coverage reported | Policy report |
| **TC-09** **Golden research path** | **E1** | Run the synthetic research project end to end | Completes G0–G10 | Run record |
| **TC-10** Golden path failure | **E2** | Break a step | The synthetic run **fails and alerts** — the closest thing to CI for the system itself | Alert record |
| **TC-11** **Golden engineering path** | **E1** | Run the synthetic engineering change | Completes through review, verification and signed release | Run record |
| **TC-12** **Derived rebuild sample** | **E1** | Rebuild a sample of graph, index and Obsidian projections | All byte-equivalent from canonical records — invariant 6 | Rebuild diff |
| **TC-13** Rebuild failure | **E2** | Detect anything that no longer rebuilds | Reclassified as canonical; the matrix corrected | Correction record |
| **TC-14** **Declared-count audit** | **E2** | Check every number a document states about the repository | Each is derived, or **flagged as unverifiable** | Count audit |
| **TC-15** Unregistered count | **E2** | Detect a stated number with no derivation rule | Flagged — the failure class is that checks cover the numbers someone registered | Flag record |
| **TC-16** **Test isolation audit** | **E2** | Verify no test mutates production state | Any that does is a finding | Isolation report |
| **TC-17** **Monitoring coverage** | **E1** | Report the fraction of sources actually monitored | Stated as a number, with the unmonitored set named | Coverage report |
| **TC-18** Platform chaos and replay | **E1** | Review the period's chaos, replay and backup evidence | All present and current; gaps named | Evidence review |
| **TC-19** **Platform evidence standard** | **E2** | Attempt to accept a platform invariant on assertion | **Refused** — the platform meets the standard it imposes | Refusal transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-130 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-130 --gate Day-2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-130/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-130
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_130_architecture_continuous_assurance.acceptance.md) reaches the decision — issuance is not acceptance.

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
