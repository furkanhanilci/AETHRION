# WP-015 — Event Envelope, Subject and Schema Taxonomy — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-015` |
| Work package | [`WP-015` — Event Envelope, Subject and Schema Taxonomy](WP-015_event_envelope_taxonomy.md) |
| Companion | [acceptance criteria](WP-015_event_envelope_taxonomy.acceptance.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Control Plane Lead / Security** — the independent verifier |
| Accountable owner | Event Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-015` |

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
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Event Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Event Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Control Plane Lead / Security | At completion |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |
| `WP-012` accepted output | Canonical Ownership and Field-Level Authority Matrix | Chief Architect | Before the first test case runs |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |

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
| C01 | `EventEnvelope schema` | Mandatory deliverable | *(name the test case)* |
| C02 | `Event Catalog seed` | Mandatory deliverable | *(name the test case)* |
| C03 | `Subject/retention table` | Mandatory deliverable | *(name the test case)* |
| C04 | `Consumer contract` | Mandatory deliverable | *(name the test case)* |
| C05 | Fix the `EventEnvelope` fields | WP-015-T01 | *(name the test case)* |
| C06 | Establish the workflow, artifact, evidence, security, cost and telemetry subject taxonomy | WP-015-T02 | *(name the test case)* |
| C07 | Write the rule separating an inline payload from an encrypted reference | WP-015-T03 | *(name the test case)* |
| C08 | Add the at-least-once delivery and idempotent-consumer expectation | WP-015-T04 | *(name the test case)* |
| C09 | Define schema evolution and `replay_mode` semantics | WP-015-T05 | *(name the test case)* |
| C10 | Duplicate Event Delivery | [ACC-12](../12_ACCEPTANCE_SCENARIOS/ACC-12_duplicate_event.md) — Critical | *(name the test case)* |
| C11 | DLQ Repair and Corrected Replay | [ACC-34](../12_ACCEPTANCE_SCENARIOS/ACC-34_dlq_repair.md) — High | *(name the test case)* |

**11 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-011, WP-012, WP-014 are `ACCEPTED`; a NATS JetStream
instance and at least one consumer are reachable in a test environment.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `EventEnvelope` against its schema | Event, causation, correlation and idempotency identifiers all mandatory | Schema validation output |
| 2 | E0 | Confirm the subject taxonomy covers workflow, artifact, evidence, security, cost and telemetry, and that **every subject has a retention value** | Six domains; zero subjects without retention | Subject/retention table |
| 3 | **E2** | **Gate-authority test.** Have a consumer attempt to change gate state on receiving an event | **Rejected.** Gate transitions come only from Temporal. This is `PR-07` | Rejection transcript |
| 4 | **E2** | **Data-class test.** Publish an event with a D3 payload inline | Rejected at publish, not at consume | Rejection transcript |
| 5 | **E2** | **PII test.** Publish an event whose body contains a detectable PII pattern | Rejected; the detector is defence in depth and the schema rule is the boundary | Rejection transcript |
| 6 | **E2** | **Duplicate-delivery test (`ACC-12`).** Deliver the same event twice | **Exactly one** business effect; the duplicate is acknowledged and audited; the side effect does not repeat | Effect count · audit record |
| 7 | **E2** | **Replay test.** Replay a historical event with `replay_mode` set | The consumer performs no external side effect; state is reconciled | Replay transcript |
| 8 | **E2** | **Replay-without-flag test.** Replay the same event with `replay_mode` unset | The consumer treats it as live — demonstrating the flag is load-bearing rather than decorative | Contrast transcript |
| 9 | **E2** | **Schema-evolution test.** Publish a major-version envelope to a consumer pinned to the previous major | Rejected or routed to an adapter; never silently consumed | Compatibility transcript |
| 10 | **E2** | **DLQ repair test (`ACC-34`).** Poison an event, route to DLQ, correct and replay | No consumer loop; the corrected event names what it replaces; original causation is preserved; processed exactly once | DLQ repair transcript |
| 11 | E1 | Confirm every event resolves to its correlation chain (WP-011) | One query returns the originating project, workflow and run | Chain query |
| 12 | E1 | Confirm retention is enforced per subject, not globally | Two subjects with different retentions both behave correctly | Retention observation |
| 13 | E3 | Independent review of the subject taxonomy for a subject whose retention conflicts with its data class | Any found is a finding | `ReviewRecord` |

Step 8 is the unusual one and it is deliberate: it tests that the *absence* of the
flag changes behaviour. A flag that makes no difference when omitted has not been
implemented.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-015 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-015 --gate Platform \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-015/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-015
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-015_event_envelope_taxonomy.acceptance.md) reaches the decision — issuance is not acceptance.

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
