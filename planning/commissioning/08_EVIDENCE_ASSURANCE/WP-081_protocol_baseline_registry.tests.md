# WP-081 — Protocol, Analysis, Baseline and Falsification Registry — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-081` |
| Work package | [`WP-081` — Protocol, Analysis, Baseline and Falsification Registry](WP-081_protocol_baseline_registry.md) |
| Companion | [acceptance criteria](WP-081_protocol_baseline_registry.acceptance.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Statistician / Falsification Lead** — the independent verifier |
| Accountable owner | Method Office Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-081` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 1 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Method Office Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Method Office Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Statistician / Falsification Lead | At completion |
| `WP-008` accepted output | G0–G10 Gate and Assurance Policy | Research Director | Before the first test case runs |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-019` accepted output | Run, Environment and Reproduction Schemas | Experiment Platform Lead | Before the first test case runs |
| `WP-025` accepted output | PostgreSQL HA and Registry Data Foundation | Database Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-035` accepted output | G2 Protocol, G3 Literature and G4 Baseline Workflows | Scientific Workflow Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |

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
| C01 | `Method Registry` | Mandatory deliverable | *(name the test case)* |
| C02 | `Protocol validators` | Mandatory deliverable | *(name the test case)* |
| C03 | `Amendment workflow` | Mandatory deliverable | *(name the test case)* |
| C04 | `Post-hoc change detector` | Mandatory deliverable | *(name the test case)* |
| C05 | `SpecificationConformanceRecord binding` | Mandatory deliverable | *(name the test case)* |
| C06 | Establish the registry data model, API and outbox events | WP-081-T01 | *(name the test case)* |
| C07 | Write validation for variables, outcomes, controls, sample and stop rules | WP-081-T02 | *(name the test case)* |
| C08 | Make the baseline, null, counter-test and leakage fields mandatory | WP-081-T03 | *(name the test case)* |
| C09 | Apply the freeze/signature and amendment/supersession lifecycle | WP-081-T04 | *(name the test case)* |
| C10 | Add run and claim linkage plus a post-hoc change detector | WP-081-T05 | *(name the test case)* |
| C11 | Bind the review and approval workflow API | WP-081-T06 | *(name the test case)* |
| C12 | Negative Research Result | [ACC-39](../12_ACCEPTANCE_SCENARIOS/ACC-39_negative_result.md) — Medium | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Registry schema | E0 | Inspect the four artifact types | All present with owner, hash, gate reference and lifecycle | Registry |
| **TC-02** Variable validation | **E2** | Submit a protocol with an undefined outcome variable | Refused | Refusal transcript |
| **TC-03** **Mandatory counter-test** | **E2** | Submit with no `FalsificationPlan` | **Refused** — the G4 blocker is a schema requirement, not a review question | Refusal transcript |
| **TC-04** **Mandatory leakage field** | **E2** | Submit with the leakage assessment unset | Refused | Refusal transcript |
| **TC-05** Mandatory null/baseline | **E2** | Submit with no baseline or null specified | Refused | Refusal transcript |
| **TC-06** **Falsifiable stop rule** | **E2** | Submit a stop rule with no observable and threshold | Refused | Refusal transcript |
| **TC-07** Freeze and signature | **E1** | Freeze a protocol | Hashed and signed; the digest is recorded | Manifest |
| **TC-08** In-place edit | **E2** | Edit a frozen artifact | Refused | Refusal transcript |
| **TC-09** Amendment before data | **E1** | Amend with no run recorded | Accepted; versioned; timestamped | Amendment record |
| **TC-10** **Amendment after data** | **E2** | Amend after a run exists | **Refused as a correction**; permitted only as a **new, declared exploratory study** | Refusal transcript |
| **TC-11** **Post-hoc detector** | **E2** | Attempt to backdate an amendment | The detector compares amendment time to first run time and **flags it** | Detection record |
| **TC-12** Detector liveness | **E2** | Run the detector suite with the seeded post-hoc change removed | The suite **fails** rather than reporting clean | Failure transcript |
| **TC-13** G2b separate freeze | **E1** | Freeze the analysis plan separately from the protocol | Two artifacts, two digests, two gate records | Two manifests |
| **TC-14** Analysis plan bypass | **E2** | Attempt G4 with a frozen protocol and no analysis plan | Refused | Refusal transcript |
| **TC-15** Run linkage | **E1** | Link a run to its protocol | The run names the frozen digest, not the artifact identifier alone | Run record |
| **TC-16** Claim linkage | **E1** | Trace a confirmatory claim to its analysis plan | Resolves in one query | Query transcript |
| **TC-17** Supersession | **E1** | Supersede a protocol | Prior version stays resolvable; runs against it keep their reference | Version chain |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-081 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-081 --gate G2,G4 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-081/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-081
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-081_protocol_baseline_registry.acceptance.md) reaches the decision — issuance is not acceptance.

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
