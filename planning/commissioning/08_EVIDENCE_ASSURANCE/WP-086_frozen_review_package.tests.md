# WP-086 — Frozen and Blind Review Package Builder — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-086` |
| Work package | [`WP-086` — Frozen and Blind Review Package Builder](WP-086_frozen_review_package.md) |
| Companion | [acceptance criteria](WP-086_frozen_review_package.acceptance.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Privacy/Security / Blind Reviewer** — the independent verifier |
| Accountable owner | Assurance Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-086` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Assurance Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Assurance Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Privacy/Security / Blind Reviewer | At completion |
| `WP-007` accepted output | IndependenceProfile and Separation-of-Duties Policy | Assurance Lead | Before the first test case runs |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-018` accepted output | Claim, Evidence, Review and Decision Schemas | Evidence Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-075` accepted output | Canonical Claim/Evidence Ledger Service | Evidence Platform Lead | Before the first test case runs |
| `WP-077` accepted output | Claim State, Dependency and Assessment Engine | Evidence Platform Lead | Before the first test case runs |
| `WP-080` accepted output | Claim–Citation Entailment, Scope and Locator Audit | Citation Audit Lead | Before the first test case runs |
| `WP-081` accepted output | Protocol, Analysis, Baseline and Falsification Registry | Method Office Lead | Before the first test case runs |
| `WP-082` accepted output | Run Registry and MLflow Lineage Integration | Experiment Platform Lead | Before the first test case runs |

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
| C01 | `Review Package Builder` | Mandatory deliverable | *(name the test case)* |
| C02 | `Blind/redaction rules` | Mandatory deliverable | *(name the test case)* |
| C03 | `Package manifests` | Mandatory deliverable | *(name the test case)* |
| C04 | `Leak detection tests` | Mandatory deliverable | *(name the test case)* |
| C05 | Define review package profiles per artifact type | WP-086-T01 | *(name the test case)* |
| C06 | Write frozen target, hash and manifest assembly | WP-086-T02 | *(name the test case)* |
| C07 | Add producer identity/model/trace redaction and a leak detector | WP-086-T03 | *(name the test case)* |
| C08 | Apply minimum-context and relevant-excerpt selection | WP-086-T04 | *(name the test case)* |
| C09 | Establish package signature, access, expiry and one-way reviewer credentials | WP-086-T05 | *(name the test case)* |
| C10 | Write the unblinding audit and the correction delta package | WP-086-T06 | *(name the test case)* |
| C11 | Planner Self-Approval Attempt | [ACC-06](../12_ACCEPTANCE_SCENARIOS/ACC-06_plan_self_approval.md) — Critical | *(name the test case)* |
| C12 | Reviewer Order Bias | [ACC-07](../12_ACCEPTANCE_SCENARIOS/ACC-07_reviewer_order_bias.md) — High | *(name the test case)* |
| C13 | Reviewer Isolation Before Review Lock | [ACC-72](../12_ACCEPTANCE_SCENARIOS/ACC-72_reviewer_isolation_before_lock.md) — Critical | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Profiles | E0 | Inspect package profiles per artifact type | A profile per type, each naming what it includes and excludes | Profiles |
| **TC-02** Frozen target | **E1** | Assemble a package | The target is hashed and immutable; the manifest names every included item | Package manifest |
| **TC-03** **Identity redaction** | **E2** | Search the assembled package for producer identity | **None** — including in paths, metadata and timestamps | Redaction scan |
| **TC-04** **Model redaction** | **E2** | Search for the producing model's identity | None | Redaction scan |
| **TC-05** **Trace removal** | **E2** | Search for the producer's working trace | None | Redaction scan |
| **TC-06** **Persuasive reasoning** | **E2** | Search for intermediate chain-of-thought | **None.** A producer's argument persuades a reviewer rather than informing them | Redaction scan |
| **TC-07** **Leak detector fires** | **E2** | Seed a producer identifier in an unusual place and assemble | **Detected**, and the package is refused | Detection transcript |
| **TC-08** Detector liveness | **E2** | Run the detector suite with the seed removed | The suite **fails** rather than reporting clean | Failure transcript |
| **TC-09** Minimum context | **E1** | Inspect the evidence included | Only spans relevant to the claims under review; the selection rule is recorded | Selection record |
| **TC-10** Everything-included | **E2** | Attempt to assemble a package containing the full workspace | Refused — volume re-introduces the trace | Refusal transcript |
| **TC-11** Signature | **E1** | Verify the package signature | Verifies; an altered package fails | Verification · failure |
| **TC-12** One-way credential | **E2** | Use a reviewer credential to read the producer's workspace | **Denied** | Denial record |
| **TC-13** Expiry | **E2** | Use a package credential past its expiry | Refused | Refusal transcript |
| **TC-14** Diff against workspace | **E1** | Diff the package against the producer's workspace | **Zero** producer-trace artifacts | Packet diff |
| **TC-15** **Unblinding audit** | **E1** | Unblind a reviewer deliberately | Recorded, and the review's independence profile is **downgraded** accordingly | Unblinding record |
| **TC-16** Silent unblinding | **E2** | Attempt unblinding without recording | Refused | Refusal transcript |
| **TC-17** Correction delta | **E1** | Correct an artifact and request re-review | A delta package shows what changed; review scope follows the delta | Delta package |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-086 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-086 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-086/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-086
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-086_frozen_review_package.acceptance.md) reaches the decision — issuance is not acceptance.

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
