---
title: "WP-109 — Forty Acceptance Scenario Registry and Harness — Test Procedures"
aliases:
  - "WP-109 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-109 — Forty Acceptance Scenario Registry and Harness — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-109` |
| Work package | [`WP-109` — Forty Acceptance Scenario Registry and Harness](wp_109_acceptance_registry.md) |
| Companion | [acceptance criteria](wp_109_acceptance_registry.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board** — the independent verifier |
| Accountable owner | Platform Assurance Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-109` |

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
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Commissioning |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Platform Assurance Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Platform Assurance Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Commissioning Board | At completion |
| `WP-002` accepted output | Scope, NFRs and Requirement Traceability | Chief Architect | Before the first test case runs |
| `WP-009` accepted output | Control Catalogue, Exceptions and Non-Waivable Blockers | Safety & Governance Owner | Before the first test case runs |
| `WP-020` accepted output | Schema Registry, Compatibility and Contract SDK | Platform Architecture Lead | Before the first test case runs |
| `WP-024` accepted output | CI Foundation and Deterministic Quality Gates | Engineering Productivity Lead | Before the first test case runs |
| `WP-040` accepted output | Workflow Replay, Versioning and Failure Test Suite | Platform Assurance Lead | Before the first test case runs |
| `WP-060` accepted output | Agentic Security Attack Suite and Red-Team Acceptance | Red Team Lead | Before the first test case runs |
| `WP-090` accepted output | PublicationPackage, RO-Crate and Provenance Export | Provenance Curator | Before the first test case runs |
| `WP-099` accepted output | WORM Audit Ledger and Independent Export | Internal Audit Platform Lead | Before the first test case runs |
| `WP-102` accepted output | Vertical Slice 1 — Intake through Protocol Freeze | Research Workflow Lead | Before the first test case runs |
| `WP-103` accepted output | Vertical Slice 2 — Two-Way Literature and Set Freeze | Evidence Lead | Before the first test case runs |
| `WP-104` accepted output | Vertical Slice 3 — Baseline through Run to Claim/Evidence | Scientific Engineering Lead | Before the first test case runs |
| `WP-105` accepted output | Vertical Slice 4 — Blind Review, Arbitration and Clean-Room | Assurance Lead | Before the first test case runs |
| `WP-106` accepted output | Vertical Slice 5 — Human Decision, Publish and Monitor | Project Decision Owner | Before the first test case runs |
| `WP-107` accepted output | Engineering Vertical Slice — Spec, Worktree, Signed Release | Engineering Lead | Before the first test case runs |
| `WP-108` accepted output | Retraction, Drift and Supersession Vertical Slice | Knowledge Monitoring Lead | Before the first test case runs |

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
| C01 | `Acceptance Registry` | Mandatory deliverable | *(name the test case)* |
| C02 | `Scenario runner` | Mandatory deliverable | *(name the test case)* |
| C03 | `Fixture catalog` | Mandatory deliverable | *(name the test case)* |
| C04 | `Evidence capture/signing` | Mandatory deliverable | *(name the test case)* |
| C05 | `Result dashboard` | Mandatory deliverable | *(name the test case)* |
| C06 | Transfer the 40 scenarios into a machine-readable registry | WP-109-T01 | *(name the test case)* |
| C07 | Write the fixture, environment and data-seeding standard | WP-109-T02 | *(name the test case)* |
| C08 | Add the expected canonical, event, audit and policy assertions | WP-109-T03 | *(name the test case)* |
| C09 | Build the test runner, evidence capture and result signing | WP-109-T04 | *(name the test case)* |
| C10 | Write the witness protocol for manual human and DR steps | WP-109-T05 | *(name the test case)* |
| C11 | Add the retry, flakiness, skip/waiver and cleanup rules | WP-109-T06 | *(name the test case)* |

**11 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Full coverage** | **E0** | Compare the registry against the scenario directory | **All 51** present — not 40 | Coverage report |
| **TC-02** Machine-readable | **E0** | Inspect a registry entry | Given/When/Then, fixtures, expected events, invariants, evidence, owner, severity and cleanup all structured | Registry entry |
| **TC-03** Missing field | **E2** | Register a scenario with no owner or severity | Refused | Refusal transcript |
| **TC-04** **Phase audit** | **E0** | Inspect the phase distribution | All 51 are `PRE_GO_LIVE`; **the absence of any `DAY2_CONTINUOUS` scenario is reported as a finding** | Phase report · finding |
| **TC-05** Fixture standard | **E1** | Seed a scenario's fixtures | Deterministic; regenerated from a committed source | Fixture run |
| **TC-06** Fixture isolation | **E2** | Run two scenarios in sequence | The second sees nothing from the first | Isolation transcript |
| **TC-07** Canonical assertions | **E1** | Run a scenario | Registry, ledger, gate and audit assertions all evaluated | Assertion output |
| **TC-08** Event assertions | **E1** | Assert expected events | Emitted events compared against expected, including absence | Assertion output |
| **TC-09** Policy assertions | **E1** | Assert a policy decision | Decision, rule and explanation all checked | Assertion output |
| **TC-10** **Runner** | **E1** | Execute a scenario end to end | Result produced with captured evidence and a signature | Signed result |
| **TC-11** Evidence capture | **E1** | Inspect a result | Every assertion's observed value captured, not summarised | Evidence bundle |
| **TC-12** **Witness protocol** | **E1** | Run a manual scenario step | Witness identity, observation and timestamp recorded | Witness record |
| **TC-13** Unwitnessed manual step | **E2** | Complete a manual step with no witness | **Not counted as a pass** | Refusal transcript |
| **TC-14** **Critical skip** | **E2** | Attempt to SKIP a Critical scenario | **Refused** — a Critical scenario cannot pass through a SKIP or a waiver | Refusal transcript |
| **TC-15** Non-critical skip | **E1** | SKIP a Medium scenario with a reason | Permitted, recorded, and **reported separately from passes** | Skip record |
| **TC-16** **Flakiness** | **E2** | Make a scenario pass only on retry | The flake is **recorded as a finding**, not absorbed by the retry setting | Finding record |
| **TC-17** Retry limit | **E1** | Exceed the retry limit | Fails; the attempts are recorded | Result |
| **TC-18** Cleanup | **E1** | Complete a scenario | Fixtures and state torn down; the next run starts clean | Cleanup record |
| **TC-19** Cleanup failure | **E2** | Fail a cleanup | Reported; the following scenario is **blocked** rather than run dirty | Block record |
| **TC-20** Versioning | **E1** | Change a scenario | The registry versions it; prior results name the version they ran against | Version chain |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-109 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-109 --gate Commissioning \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-109/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-109
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_109_acceptance_registry.acceptance.md) reaches the decision — issuance is not acceptance.

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
