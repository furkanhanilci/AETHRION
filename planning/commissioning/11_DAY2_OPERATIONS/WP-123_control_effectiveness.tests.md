# WP-123 — Control Effectiveness and Policy Regression Rhythm — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-123` |
| Work package | [`WP-123` — Control Effectiveness and Policy Regression Rhythm](WP-123_control_effectiveness.md) |
| Companion | [acceptance criteria](WP-123_control_effectiveness.acceptance.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Internal Audit / Red Team** — the independent verifier |
| Accountable owner | Safety & Governance Owner |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-123` |

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
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Day-2 |

**Applicable layers: E0 · E1 · E2 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Safety & Governance Owner | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Safety & Governance Owner | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Internal Audit / Red Team | At completion |
| `WP-009` accepted output | Control Catalogue, Exceptions and Non-Waivable Blockers | Safety & Governance Owner | Before the first test case runs |
| `WP-056` accepted output | OPA Policy Platform and Bundle Distribution | Policy Platform Lead | Before the first test case runs |
| `WP-060` accepted output | Agentic Security Attack Suite and Red-Team Acceptance | Red Team Lead | Before the first test case runs |
| `WP-112` accepted output | Security and Privacy Acceptance Package | Safety & Governance Owner | Before the first test case runs |
| `WP-121` accepted output | Hypercare, Stabilisation and Programme Closure | SRE Lead / Program Lead | Before the first test case runs |

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
| C01 | `Control effectiveness reports` | Mandatory deliverable | *(name the test case)* |
| C02 | `Policy regression results` | Mandatory deliverable | *(name the test case)* |
| C03 | `Exception audit` | Mandatory deliverable | *(name the test case)* |
| C04 | `Control improvement backlog` | Mandatory deliverable | *(name the test case)* |
| C05 | Apply the control test calendar and its sampling rates | WP-123-T01 | *(name the test case)* |
| C06 | Run the OPA, identity, data, tool and supply-chain negative regressions | WP-123-T02 | *(name the test case)* |
| C07 | Audit exception expiry, usage and residual risk | WP-123-T03 | *(name the test case)* |
| C08 | Review control coverage, gaps and false positives | WP-123-T04 | *(name the test case)* |
| C09 | Trigger an ADR or policy reopen after two material failures | WP-123-T05 | *(name the test case)* |

**9 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Test calendar | E0 | Inspect the calendar | Every control has a test date and a sampling rate | Calendar |
| **TC-02** Untested control | **E2** | Detect a control with no scheduled test | Flagged; treated as **failing** until tested (WP-009) | Flag record |
| **TC-03** **OPA negative regression** | **E2** | Run the policy refusal cases | Every declared denial still denies | Regression report |
| **TC-04** Silent policy regression | **E2** | Change a bundle so one denial stops firing | **Detected by the regression**, not in production | Detection record |
| **TC-05** Identity regression | **E2** | Run identity refusal cases | Unattested workloads, expired leases and cross-account attempts all still refused | Regression report |
| **TC-06** Data-class regression | **E2** | Run data-class refusal cases | D3 routing, ceiling breaches and trace leaks all still refused | Regression report |
| **TC-07** Tool-scope regression | **E2** | Run broker refusal cases | Out-of-scope tools, unsigned definitions and confused-deputy attempts all still refused | Regression report |
| **TC-08** Supply-chain regression | **E2** | Run admission refusal cases | Unsigned, unapproved builder and CVE-threshold cases all still refused | Regression report |
| **TC-09** **Exception usage audit** | **E1** | Audit the exception register | Which were used, how often, and by whom | Usage report |
| **TC-10** **Expired exceptions** | **E2** | Detect exceptions past expiry | Found and **auto-revoked**; any that were still working is a finding | Finding record |
| **TC-11** **Quiet renewal** | **E2** | Detect a renewal with no restated removal criterion | Flagged — a register of quiet renewals is a second, undocumented policy | Flag record |
| **TC-12** Residual risk accumulation | **E1** | Sum accepted residual risks | Trend reported; growth raised to governance | Residual report |
| **TC-13** **Coverage review** | **E1** | Compare controls against the threat-to-control map | Gaps named with owners | Coverage report |
| **TC-14** **False-positive rate** | **E1** | Measure per control | Reported as a number; a high rate triggers **control tuning, not user training** | FP report |
| **TC-15** **Two material failures** | **E2** | Fail one control materially twice | **An ADR or policy reopen is triggered**, not a third remediation | Reopen record |
| **TC-16** Closure discipline | **E2** | Attempt to close a risk on *mitigation applied* | **Refused** — closure needs an effectiveness test, evidence, an owner and a re-evaluation date | Refusal transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-123 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-123 --gate Day-2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-123/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-123
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-123_control_effectiveness.acceptance.md) reaches the decision — issuance is not acceptance.

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
