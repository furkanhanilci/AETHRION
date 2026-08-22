# WP-010 — Architecture Decision and Rejected-Alternatives Baseline — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-010` |
| Work package | [`WP-010` — Architecture Decision and Rejected-Alternatives Baseline](WP-010_adr_baseline.md) |
| Companion | [acceptance criteria](WP-010_adr_baseline.acceptance.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Architecture Board** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-010` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | no | no scenario and not L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform |

**Applicable layers: E0 · E1 · E2 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Chief Architect | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Chief Architect | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Architecture Board | At completion |
| `WP-002` accepted output | Scope, NFRs and Requirement Traceability | Chief Architect | Before the first test case runs |
| `WP-005` accepted output | Research Risk and Assurance Profile | Safety & Governance Owner | Before the first test case runs |
| `WP-006` accepted output | ExecutionProfile and Route Policy | Platform Security Lead | Before the first test case runs |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-008` accepted output | G0–G10 Gate and Assurance Policy | Research Director | Before the first test case runs |
| `WP-009` accepted output | Control Catalogue, Exceptions and Non-Waivable Blockers | Safety & Governance Owner | Before the first test case runs |

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
| C01 | `Signed ADR bundle` | Mandatory deliverable | *(name the test case)* |
| C02 | `Rejected alternatives register` | Mandatory deliverable | *(name the test case)* |
| C03 | `Reopen trigger register` | Mandatory deliverable | *(name the test case)* |
| C04 | `Architecture baseline digest` | Mandatory deliverable | *(name the test case)* |
| C05 | Separate the binding decisions into individual ADRs | WP-010-T01 | *(name the test case)* |
| C06 | Write the alternatives, the trade-offs and the reason each was rejected | WP-010-T02 | *(name the test case)* |
| C07 | Define the reopen trigger for every decision | WP-010-T03 | *(name the test case)* |
| C08 | Link the canonical-owner and trust-boundary consequences of each decision | WP-010-T04 | *(name the test case)* |
| C09 | Establish the ADR → WP → control mapping | WP-010-T05 | *(name the test case)* |

**9 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-002 is `ACCEPTED`; the existing ADR-001/002/003 are
available; the binding-decision list from the plan README is available.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate every ADR against the ADR schema | Context, decision, alternatives with rejection reasons, consequences, status, reopen trigger present | Schema validation output |
| 2 | **E0** | **Completeness test.** Check every binding decision in the plan README §2 has an ADR | Zero binding decisions without one; any gap is listed | Coverage report |
| 3 | **E0** | **Alternatives test.** Confirm no ADR has an empty alternatives section | Every ADR names at least one rejected alternative **and why** it was rejected | Lint output |
| 4 | **E0** | **Reopen-trigger test.** Confirm every trigger names an observable and a threshold | Zero triggers phrased as "if circumstances change" | Trigger lint output |
| 5 | **E2** | **Trigger firing test.** For a sample of ADRs, construct the condition each trigger describes | Each trigger is shown to be **reachable** — a trigger nothing can satisfy is a finding | Transcript per sampled ADR |
| 6 | E0 | Resolve ADR → WP → control for every decision | Every ADR maps to the packages that implement it and the controls that enforce it | Mapping report |
| 7 | E0 | Confirm each ADR links its canonical-owner and trust-boundary consequences | Zero ADRs with consequences stated only in prose | Consequence links |
| 8 | E1 | Reconcile ADR-001, ADR-002 and ADR-003 into the baseline | One answer per question; contradictions with the README §2 list are resolved, not both retained | Reconciliation record |
| 9 | **E2** | **Self-contradiction test.** Run `check_doc_consistency.py`'s decision-record check | No ADR whose status is `ACCEPTED` still describes its own decision as unmade | Check transcript |
| 10 | E1 | Confirm superseded ADRs are marked superseded, not deleted, and name their successor | Supersession chain resolves | ADR index |
| 11 | E3 | Independent review of the alternatives sections | The reviewer names at least one alternative that should have been considered and was not | `ReviewRecord` |

Steps 3, 4 and 5 are where this package either earns its place or becomes a
filing system. A baseline of ADRs whose triggers cannot fire is a baseline that
will be silently outgrown.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-010 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-010 --gate Program \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-010/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-010
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-010_adr_baseline.acceptance.md) reaches the decision — issuance is not acceptance.

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
