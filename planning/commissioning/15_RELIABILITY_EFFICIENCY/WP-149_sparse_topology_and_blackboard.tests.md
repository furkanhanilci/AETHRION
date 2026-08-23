# WP-149 — Sparse Communication Topology and the Scientific Blackboard — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-149` |
| Work package | [`WP-149` — Sparse Communication Topology and the Scientific Blackboard](WP-149_sparse_topology_and_blackboard.md) |
| Companion | [acceptance criteria](WP-149_sparse_topology_and_blackboard.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Research Director / Platform Assurance Lead** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-149` |

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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Research Director / Platform Assurance Lead | At completion |
| `WP-013` accepted output | Project, Task, Role and Skill Contract Schemas | Control Plane Lead | Before the first test case runs |
| `WP-015` accepted output | Event Envelope, Subject and Schema Taxonomy | Event Platform Lead | Before the first test case runs |
| `WP-046` accepted output | LangGraph Bounded Cognition Runtime | Agent Platform Lead | Before the first test case runs |
| `WP-047` accepted output | Role and Skill Registries, and the Task Compiler | Agent Platform Lead | Before the first test case runs |
| `WP-148` accepted output | Multi-Agent Collaboration Plane and Cohort Integrity | Research Director | Before the first test case runs |

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
| C01 | `BlackboardEntry` | Mandatory deliverable | *(name the test case)* |
| C02 | `TypedAgentMessage` | Mandatory deliverable | *(name the test case)* |
| C03 | `CommunicationGraph` | Mandatory deliverable | *(name the test case)* |
| C04 | `CommunicationEdgePolicy` | Mandatory deliverable | *(name the test case)* |
| C05 | `Naive fully-connected baseline harness` | Mandatory deliverable | *(name the test case)* |
| C06 | Define `BlackboardEntry` with artifact pointers, epistemic status and retention | WP-149-T01 | *(name the test case)* |
| C07 | Define the ten typed messages and their required fields | WP-149-T02 | *(name the test case)* |
| C08 | Enforce the delta-only rule and the artifact-pointer substitution | WP-149-T03 | *(name the test case)* |
| C09 | Define `CommunicationGraph` and `CommunicationEdgePolicy` | WP-149-T04 | *(name the test case)* |
| C10 | Implement topology compilation from the task and the independence profile | WP-149-T05 | *(name the test case)* |
| C11 | Implement the fully-connected control mode and the baseline harness | WP-149-T06 | *(name the test case)* |
| C12 | Prove the blackboard is deletable without canonical loss | WP-149-T07 | *(name the test case)* |
| C13 | Independent-First Embargo | [ACC-082](../12_ACCEPTANCE_SCENARIOS/ACC-082_independent_first_embargo.md) — Critical | *(name the test case)* |
| C14 | Typed Inter-Agent Message | [ACC-083](../12_ACCEPTANCE_SCENARIOS/ACC-083_typed_inter_agent_message.md) — High | *(name the test case)* |
| C15 | Delta-Only Communication | [ACC-084](../12_ACCEPTANCE_SCENARIOS/ACC-084_delta_only_communication.md) — High | *(name the test case)* |
| C16 | A Blackboard Entry Is Not Evidence | [ACC-085](../12_ACCEPTANCE_SCENARIOS/ACC-085_blackboard_entry_is_not_evidence.md) — Critical | *(name the test case)* |
| C17 | Sparse Topology Preserves Quality | [ACC-086](../12_ACCEPTANCE_SCENARIOS/ACC-086_sparse_topology_quality_preservation.md) — High | *(name the test case)* |

**17 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-148 supplies a compiled cohort; WP-015 supplies the event envelope; the artifact store accepts writes so that a pointer has something to point at.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `BlackboardEntry`, `TypedAgentMessage`, `CommunicationGraph` and `CommunicationEdgePolicy` | All four validate; message type and edge class are closed enumerations | Validator output |
| 2 | **E2** | **Untyped message.** Emit an inter-agent message with no declared type | Rejected at the contract boundary — ACC-083 | Rejection transcript |
| 3 | **E2** | **Mistyped message.** Declare `STATUS` while carrying a challenge | Rejected, or normalised only through the authorised path and audited | Rejection transcript |
| 4 | E1 | Emit a correctly typed `CHALLENGE` and track it to resolution | Trackable end to end; it appears in the convergence assessment | Challenge record |
| 5 | **E2** | **Delta-only.** Emit a message carrying a full reasoning transcript | Rejected in favour of a delta plus an artifact pointer — ACC-084 | Rejection transcript |
| 6 | E1 | Re-emit as a delta with a pointer and resolve the pointer | The full content is retrievable from the artifact store; nothing was lost | Artifact + message pair |
| 7 | **E1** | **Token effect.** Compare inter-agent token counts for the transcript and delta forms | Measurably lower for the delta form | Token ledger extract |
| 8 | **E2** | **Not evidence.** Attempt to cite a blackboard entry as evidence for a claim | Refused — ACC-085 | Refusal transcript |
| 9 | **E2** | **No promotion path.** Attempt to promote a `CONSENSUS_CANDIDATE` entry directly to a `ClaimVersion` | No such path exists; the attempt is refused | Refusal transcript |
| 10 | **E2** | **Deletability.** Capture canonical scientific state, delete the entire blackboard, re-read canonical state | Nothing canonical is lost; artifact pointers held by deleted entries still resolve — ACC-085 | Before/after comparison |
| 11 | E1 | Compile a topology from a task, its roles, its evidence dependencies and its budget | A sparse graph with per-edge policies, not fully connected | `CommunicationGraph` |
| 12 | E1 | Enable the explicit control mode and confirm the graph is fully connected | Available only in that mode, and recorded as such | Topology record |
| 13 | **E4** | **Baseline harness.** Run the same task set through the fully-connected baseline and the sparse topology | Both arms complete under the same budget and firewall; both emit the same metric schema — ACC-086 | Two run records |
| 14 | E3 | Independent review of one collaboration round's message log | The reviewer can follow every challenge to its resolution from the typed record alone | `ReviewRecord` |

Case 10 is the one that decides whether the blackboard is a projection or a
second store. It is destructive on purpose: any answer other than *nothing
canonical was lost* means the collaboration plane has quietly become authoritative.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-149   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-149 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-149/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-149
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-149_sparse_topology_and_blackboard.acceptance.md) reaches the decision — issuance is not acceptance.

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
