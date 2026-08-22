---
title: "WP-045 — Policy Router and Minimum-Sufficient Model Package — Test Procedures"
aliases:
  - "WP-045 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g1
  - aethrion/gate/g5
  - aethrion/gate/g6
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-045 — Policy Router and Minimum-Sufficient Model Package — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-045` |
| Work package | [`WP-045` — Policy Router and Minimum-Sufficient Model Package](wp_045_policy_router_budget.md) |
| Companion | [acceptance criteria](wp_045_policy_router_budget.acceptance.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Safety / Eval / FinOps** — the independent verifier |
| Accountable owner | Model Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-045` |

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
| Target revision | The single commit every result is bound to | Model Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Model Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Safety / Eval / FinOps | At completion |
| `WP-005` accepted output | Research Risk and Assurance Profile | Safety & Governance Owner | Before the first test case runs |
| `WP-006` accepted output | ExecutionProfile and Route Policy | Platform Security Lead | Before the first test case runs |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-013` accepted output | Project, Task, Role and Skill Contract Schemas | Control Plane Lead | Before the first test case runs |
| `WP-016` accepted output | PolicyDecision, Control and Exception Schemas | Policy Platform Lead | Before the first test case runs |
| `WP-041` accepted output | LiteLLM Model Gateway Foundation | Model Platform Lead | Before the first test case runs |
| `WP-042` accepted output | Capability Registry and Profile Lifecycle | Eval Office | Before the first test case runs |
| `WP-044` accepted output | Model Qualification and Admission Pipeline | Eval Office | Before the first test case runs |

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
| C01 | `Policy Router` | Mandatory deliverable | *(name the test case)* |
| C02 | `RouteDecision service` | Mandatory deliverable | *(name the test case)* |
| C03 | `Fan-out/budget rules` | Mandatory deliverable | *(name the test case)* |
| C04 | `Routing conformance suite` | Mandatory deliverable | *(name the test case)* |
| C05 | Bind the OPA pre-filter and the Capability Registry query | WP-045-T01 | *(name the test case)* |
| C06 | Write the quality-adjusted cost and latency selection ordering | WP-045-T02 | *(name the test case)* |
| C07 | Define the rules separating a single model from parallel or council fan-out | WP-045-T03 | *(name the test case)* |
| C08 | Apply independence-aware reviewer routing | WP-045-T04 | *(name the test case)* |
| C09 | Add fallback, retry and fan-out budget reservation | WP-045-T05 | *(name the test case)* |
| C10 | Emit the `RouteDecision` explanation and telemetry | WP-045-T06 | *(name the test case)* |
| C11 | Budget Hard Stop | [ACC-09](../12_ACCEPTANCE_SCENARIOS/acc_09_budget_hard_stop.md) — Critical | *(name the test case)* |
| C12 | Primary Model Provider Outage | [ACC-10](../12_ACCEPTANCE_SCENARIOS/acc_10_provider_outage.md) — High | *(name the test case)* |
| C13 | No Eligible Fallback | [ACC-11](../12_ACCEPTANCE_SCENARIOS/acc_11_no_eligible_fallback.md) — Critical | *(name the test case)* |
| C14 | D3 Data to a Public Provider | [ACC-18](../12_ACCEPTANCE_SCENARIOS/acc_18_d3_public_route.md) — Critical | *(name the test case)* |
| C15 | Critical Reviewer Unavailable | [ACC-38](../12_ACCEPTANCE_SCENARIOS/acc_38_reviewer_unavailable.md) — High | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Determinism | **E1** | Route the same `TaskContract` twice | Identical selection | Two records |
| **TC-02** Eligibility filter | **E1** | Route a task whose risk class no profile is admitted for | **No selection**; the task blocks rather than falling back | Block transcript |
| **TC-03** Minimum sufficient | **E1** | Route a low-risk task with a large model admitted | The **smallest** sufficient package is selected | Route record |
| **TC-04** Escalation attempt | **E2** | Request a larger model than the contract requires | Refused, or requires a recorded justification | Refusal transcript |
| **TC-05** OPA pre-filter | **E1** | Route a task violating a policy precondition | Denied before the registry is queried | Denial record |
| **TC-06** Quality-adjusted ordering | E1 | Route with two eligible candidates | Ordering follows the declared quality-adjusted cost rule, not raw cost | Ordering trace |
| **TC-07** Single vs fan-out | E1 | Route tasks at each risk class | Fan-out only where the rules require it | Route records |
| **TC-08** **Reviewer independence** | **E2** | Route a review whose only eligible reviewer collides with the producer | **Refused at routing**, naming the dimension | Refusal transcript |
| **TC-09** Gate-time recheck | **E2** | Assign a valid reviewer, grant context afterwards, reach the gate | Refused at the gate too (WP-007) | Refusal transcript |
| **TC-10** Budget reservation | **E1** | Start a five-way fan-out | The full budget is **reserved before** the first call | Reservation record |
| **TC-11** Insufficient budget | **E2** | Start a fan-out that exceeds the remaining budget | Refused before any call is made | Refusal transcript |
| **TC-12** Retry budget | **E1** | Force retries | Retries draw from the reservation; they do not extend it silently | Budget trace |
| **TC-13** Fallback eligibility | **E2** | Fail the primary with only an unadmitted fallback available | Fails closed (WP-041) | Failure transcript |
| **TC-14** Explanation | **E1** | Inspect a `RouteDecision` | Names the eligibility query, the candidate set, the ordering and the selection | Decision record |
| **TC-15** Conformance suite | **E1** | Run the routing conformance suite | Every declared rule has a passing and a failing case | Suite report |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-045 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-045 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-045/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-045
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_045_policy_router_budget.acceptance.md) reaches the decision — issuance is not acceptance.

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
