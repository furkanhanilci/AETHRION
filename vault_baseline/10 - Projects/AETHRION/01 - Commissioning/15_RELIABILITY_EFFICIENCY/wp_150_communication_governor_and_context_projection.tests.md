---
title: "WP-150 — Communication Governor, Edge Utility and Context Projection — Test Procedures"
aliases:
  - "WP-150 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-150_communication_governor_and_context_projection.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-150 — Communication Governor, Edge Utility and Context Projection — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-150` |
| Work package | [`WP-150` — Communication Governor, Edge Utility and Context Projection](wp_150_communication_governor_and_context_projection.md) |
| Companion | [acceptance criteria](wp_150_communication_governor_and_context_projection.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **FinOps Lead / Assurance Lead** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-150` |

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
| Target revision | The single commit every result is bound to | Chief Architect | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Chief Architect | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | FinOps Lead / Assurance Lead | At completion |
| `WP-096` accepted output | OpenTelemetry End-to-End Correlation Spine | Observability Lead | Before the first test case runs |
| `WP-100` accepted output | Cost Ledger, Budget Envelopes and FinOps | FinOps Lead | Before the first test case runs |
| `WP-149` accepted output | Sparse Communication Topology and the Scientific Blackboard | Chief Architect | Before the first test case runs |

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
| C01 | `CommunicationValue` | Mandatory deliverable | *(name the test case)* |
| C02 | `CommunicationUtilityRecord` | Mandatory deliverable | *(name the test case)* |
| C03 | `ContextProjectionRecord` | Mandatory deliverable | *(name the test case)* |
| C04 | `Quality guard and rollback` | Mandatory deliverable | *(name the test case)* |
| C05 | Define `CommunicationValue` and its deterministic first implementation | WP-150-T01 | *(name the test case)* |
| C06 | Define `CommunicationUtilityRecord` and its per-edge history | WP-150-T02 | *(name the test case)* |
| C07 | Implement the five governor decisions and the blocker exemption | WP-150-T03 | *(name the test case)* |
| C08 | Define `ContextProjectionRecord` and the per-invocation assembly | WP-150-T04 | *(name the test case)* |
| C09 | Implement the quality guard and the topology rollback path | WP-150-T05 | *(name the test case)* |
| C10 | Emit coordination overhead, redundancy and useful-challenge metrics | WP-150-T06 | *(name the test case)* |
| C11 | Implement the delivery adapter: `CommunicationDecision` → backend action → delivery evidence | WP-150-T08 | *(name the test case)* |
| C12 | Bind every delivered message to its AETHRION message id and the policy decision that authorised it | WP-150-T09 | *(name the test case)* |
| C13 | Implement delivery failure handling — timeout, duplicate, reconnect — as classified collaboration events rather than silent omission | WP-150-T10 | *(name the test case)* |
| C14 | Delta-Only Communication | [ACC-084](../12_ACCEPTANCE_SCENARIOS/acc_084_delta_only_communication.md) — High | *(name the test case)* |
| C15 | Sparse Topology Preserves Quality | [ACC-086](../12_ACCEPTANCE_SCENARIOS/acc_086_sparse_topology_quality_preservation.md) — High | *(name the test case)* |
| C16 | Communication Optimisation Rollback | [ACC-087](../12_ACCEPTANCE_SCENARIOS/acc_087_communication_optimization_rollback.md) — High | *(name the test case)* |
| C17 | Strategic Silence Never Silences a Blocker | [ACC-088](../12_ACCEPTANCE_SCENARIOS/acc_088_strategic_silence_never_silences_a_blocker.md) — Critical | *(name the test case)* |
| C18 | Budget Degrades Communication, Not the Cohort | [ACC-099](../12_ACCEPTANCE_SCENARIOS/acc_099_communication_budget_degradation.md) — Critical | *(name the test case)* |

**18 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-149 supplies a compiled topology and a runnable fully-connected baseline; WP-100 supplies a cost ledger; a quality tolerance is declared before any optimisation runs.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `CommunicationValue`, `CommunicationUtilityRecord` and `ContextProjectionRecord` | All three validate | Validator output |
| 2 | E1 | Compute a communication value deterministically for a fixed message and history | Repeatable; the same inputs give the same value | Two value traces |
| 3 | E1 | Exercise all five governor decisions on graded inputs | `SEND_FULL_STRUCTURED`, `SEND_COMPRESSED`, `SEND_POINTER_ONLY`, `DEFER` and `SILENCE` are each reachable | Decision trace per case |
| 4 | **E2** | **Blocker exemption.** Drive an edge's utility to the bottom and send a `BLOCKER` on it | Delivered regardless of utility — ACC-088 | Delivery record |
| 5 | **E2** | **Safety exemption.** Send a non-waivable safety message on the same edge | Delivered regardless of utility | Delivery record |
| 6 | **E2** | **Threshold cannot suppress.** Attempt to configure a threshold that would silence a blocker | Configuration refused | Refusal transcript |
| 7 | **E1** | **Low calibration is not silence.** Send a material finding from a low-calibration sender | Priority and corroboration requirement change; the message is **not** deleted | Routing record |
| 8 | **E2** | **Forbidden conversion.** Attempt to write a communication utility score into a claim assessment | Refused by schema and by policy | Refusal transcript |
| 9 | E1 | Assemble a context projection for an invocation and inspect its contents | Role contract, task contract, skills, canonical state, admissible evidence, targeted deltas — not the whole project history | `ContextProjectionRecord` |
| 10 | **E2** | **Projection respects independence.** Assemble a reviewer projection under blind policy | The producer's search and procedural memory are absent | Projection contents |
| 11 | **E1** | **Quality guard.** Prune a load-bearing edge and let the guard measure the result | Regression detected against the **declared** tolerance, not a post-hoc one — ACC-087 | Guard measurement |
| 12 | **E1** | **Rollback.** Observe what follows the regression | Topology rolls back automatically, without human intervention; the campaign continues | Rollback record |
| 13 | E1 | Confirm the regression measurement is retained after rollback | Retained, not discarded | Metascience record |
| 14 | **E4** | **Frontier.** Run optimised and baseline arms and compute coordination overhead for both | Cost falls measurably; quality delta within tolerance; both reported as a frontier — ACC-086 | Frontier report |
| 15 | E3 | Independent review of one optimisation decision and its evidence | The reviewer can say why each edge was pruned and what the guard measured | `ReviewRecord` |

Cases 11 and 12 are the package's whole safety argument. An optimiser without an
armed guard and an automatic rollback is a mechanism for degrading quality in
exchange for a number that looks better.
| 16 | **E2** | **Silence has a floor.** Drive the budget to its degradation limit, then emit a blocker message | Delivered. `SILENCE` never applies to a blocker or safety message, whatever the budget state | Delivery record |
| 17 | **E1** | **The backend does not re-decide.** Hand the adapter a `SEND_COMPRESSED` decision and observe the delivered payload | Delivered as decided. The backend executes a communication action and never recomputes communication value | Decision/delivery pair |
| 18 | **E2** | **History is not context.** Build a `ContextProjection` for an actor in a busy room | Reproducible from canonical state, evidence, skills and permitted peer deltas alone. Channel history is not an input | Projection digest |
| 19 | **E1** | **Rollback over a live backend.** Trigger a quality regression and roll topology back while rooms exist | Previous topology restored; existing rooms do not prevent or distort it | Topology history |


## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-150   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-150 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-150/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-150
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_150_communication_governor_and_context_projection.acceptance.md) reaches the decision — issuance is not acceptance.

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
