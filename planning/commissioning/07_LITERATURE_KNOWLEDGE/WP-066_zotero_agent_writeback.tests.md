# WP-066 — Agent Candidate and Used-Source Write-Back — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-066` |
| Work package | [`WP-066` — Agent Candidate and Used-Source Write-Back](WP-066_zotero_agent_writeback.md) |
| Companion | [acceptance criteria](WP-066_zotero_agent_writeback.acceptance.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Knowledge Curator / Security** — the independent verifier |
| Accountable owner | Knowledge Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-066` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Knowledge Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Knowledge Curator / Security | At completion |
| `WP-012` accepted output | Canonical Ownership and Field-Level Authority Matrix | Chief Architect | Before the first test case runs |
| `WP-017` accepted output | Source Registry and Literature Contract Schemas | Knowledge Lead | Before the first test case runs |
| `WP-049` accepted output | Tool Registry and Tool Broker Core | Tool Platform Lead | Before the first test case runs |
| `WP-050` accepted output | Initial Tool Connector Package | Tool Platform Lead | Before the first test case runs |
| `WP-061` accepted output | Canonical Source Registry Service | Knowledge Platform Lead | Before the first test case runs |
| `WP-062` accepted output | Source Identity Resolution, Deduplication and Merge | Source Resolver Lead | Before the first test case runs |
| `WP-064` accepted output | Zotero Library, Collection and Permission Model | Knowledge Lead | Before the first test case runs |

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
| C01 | `Zotero write-back service` | Mandatory deliverable | *(name the test case)* |
| C02 | `Field mapping` | Mandatory deliverable | *(name the test case)* |
| C03 | `Eligibility policy` | Mandatory deliverable | *(name the test case)* |
| C04 | `SyncReceipt ledger` | Mandatory deliverable | *(name the test case)* |
| C05 | `Connector tests` | Mandatory deliverable | *(name the test case)* |
| C06 | Define the write eligibility rule separating candidates from used sources | WP-066-T01 | *(name the test case)* |
| C07 | Write the `SourceRecord` → Zotero item field mapping | WP-066-T02 | *(name the test case)* |
| C08 | Apply agent-owned item and field markers | WP-066-T03 | *(name the test case)* |
| C09 | Establish the read → merge → `If-Unmodified-Since-Version` PATCH flow | WP-066-T04 | *(name the test case)* |
| C10 | Handle the full-list semantics of collection membership safely | WP-066-T05 | *(name the test case)* |
| C11 | Apply the attachment, licence and note policy | WP-066-T06 | *(name the test case)* |
| C12 | Emit `SyncReceipt` and outbox events | WP-066-T07 | *(name the test case)* |
| C13 | Agent-Used Source Write-Back | [ACC-02](../12_ACCEPTANCE_SCENARIOS/ACC-02_agent_used_source_writeback.md) — Critical | *(name the test case)* |
| C14 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/ACC-03_duplicate_collision.md) — High | *(name the test case)* |
| C15 | Tool Partial Failure | [ACC-35](../12_ACCEPTANCE_SCENARIOS/ACC-35_tool_partial_failure.md) — Critical | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Candidate write | **E1** | Write a discovered candidate | Lands in `10_Agent_Candidates` with the agent marker | Item record |
| **TC-02** Used-source write | **E1** | Write a source a claim used | Lands in `40_Used` with a reference to the claim | Item record |
| **TC-03** Eligibility refusal | **E2** | Attempt to write a source that is neither candidate nor used | Refused | Refusal transcript |
| **TC-04** Personal library | **E2** | Attempt any write to the personal library | Refused (invariant 5) | Refusal transcript |
| **TC-05** Human collection | **E2** | Attempt a write to `00_Human_Seeds` | Refused | Refusal transcript |
| **TC-06** Field mapping | E1 | Inspect a written item | `SourceRecord` fields mapped per the declared map; nothing invented | Field comparison |
| **TC-07** Human field | **E2** | Attempt to write a human-authority field on an existing item | Refused, naming the field (WP-012) | Refusal transcript |
| **TC-08** **Conditional write** | **E2** | PATCH with a stale `If-Unmodified-Since-Version` | **412; the human's edit survives** | 412 transcript · unchanged field |
| **TC-09** Blind retry | **E2** | Retry a 412 without re-reading | Refused — a retry that ignores the conflict is the overwrite | Refusal transcript |
| **TC-10** **Collection membership** | **E2** | Update collection membership while a human-added item is present | Read → merge → conditional write; **the human's item survives** | Membership before/after |
| **TC-11** Naive membership write | **E2** | Attempt a membership PATCH without reading first | **Refused by the client** — full-list semantics would delete unseen items | Refusal transcript |
| **TC-12** Agent marker | **E1** | Inspect every agent-written item and field | All carry the marker | Marker audit |
| **TC-13** Attachment policy | **E2** | Attempt to upload an attachment whose licence forbids redistribution | Refused; reference only (`PR-14`) | Refusal transcript |
| **TC-14** Note policy | **E2** | Attempt to write into a human's note | Refused | Refusal transcript |
| **TC-15** Threshold | **E2** | Exceed the declared write-rate threshold | Throttled and reported — an agent writing thousands of items is a defect, not throughput | Throttle record |
| **TC-16** `SyncReceipt` | **E1** | Complete a write | A receipt names the item, the fields, the prior version and the authority | Receipt |
| **TC-17** Reconstruction | **E1** | Rebuild the agent's library changes from receipts alone | Complete; no write exists without a receipt | Reconstruction report |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-066 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-066 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-066/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-066
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-066_zotero_agent_writeback.acceptance.md) reaches the decision — issuance is not acceptance.

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
