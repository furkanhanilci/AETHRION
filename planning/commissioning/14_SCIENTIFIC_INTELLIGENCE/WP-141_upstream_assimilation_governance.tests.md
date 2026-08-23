# WP-141 — Upstream Assimilation, Lineage and Characterisation Governance — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-141` |
| Work package | [`WP-141` — Upstream Assimilation, Lineage and Characterisation Governance](WP-141_upstream_assimilation_governance.md) |
| Companion | [acceptance criteria](WP-141_upstream_assimilation_governance.acceptance.md) |
| Workstream | `14_SCIENTIFIC_INTELLIGENCE` |
| Approval authority | **Supply Chain Security Lead / Internal Audit** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-141` |

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
| Target revision | The single commit every result is bound to | Chief Architect | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Chief Architect | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Supply Chain Security Lead / Internal Audit | At completion |
| `WP-010` accepted output | Architecture Decision and Rejected-Alternatives Baseline | Chief Architect | Before the first test case runs |
| `WP-022` accepted output | Repository Topology and Code Ownership | Chief Architect | Before the first test case runs |
| `WP-024` accepted output | CI Foundation and Deterministic Quality Gates | Engineering Productivity Lead | Before the first test case runs |
| `WP-059` accepted output | Supply-Chain Admission, Sigstore and SLSA Policy | Supply Chain Security Lead | Before the first test case runs |

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
| C01 | `AssimilationCandidate schema` | Mandatory deliverable | *(name the test case)* |
| C02 | `UpstreamLineage register` | Mandatory deliverable | *(name the test case)* |
| C03 | `check_upstream_lineage.py` | Mandatory deliverable | *(name the test case)* |
| C04 | `SPDX/REUSE policy` | Mandatory deliverable | *(name the test case)* |
| C05 | `Characterisation test convention` | Mandatory deliverable | *(name the test case)* |
| C06 | `Upstream drift review workflow` | Mandatory deliverable | *(name the test case)* |
| C07 | Define the `AssimilationCandidate` and `UpstreamLineage` record shapes | WP-141-T01 | *(name the test case)* |
| C08 | Author `provenance/upstreams.json` covering every mechanism already decided | WP-141-T02 | *(name the test case)* |
| C09 | Implement `check_upstream_lineage.py` with a firing control per rule | WP-141-T03 | *(name the test case)* |
| C10 | Bind SPDX/REUSE metadata and reconcile `NOTICE` with the register | WP-141-T04 | *(name the test case)* |
| C11 | Define the direct-adapt versus reimplement decision rule and its evidence | WP-141-T05 | *(name the test case)* |
| C12 | Define the characterisation-test convention and where suites live | WP-141-T06 | *(name the test case)* |
| C13 | Implement upstream drift detection and the review path that moves a pin | WP-141-T07 | *(name the test case)* |
| C14 | Upstream Assimilation Drift | [ACC-73](../12_ACCEPTANCE_SCENARIOS/ACC-73_upstream_assimilation_drift.md) — High | *(name the test case)* |
| C15 | Missing Upstream Lineage or Licence | [ACC-74](../12_ACCEPTANCE_SCENARIOS/ACC-74_missing_upstream_lineage.md) — High | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-024 is `ACCEPTED` so admission can actually fail a change; `provenance/upstreams.json` exists with at least one entry per assimilation type; a scratch branch is available for the planted-defect cases.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate the register against its own schema: every entry has an id, a name, an assimilation type, a status, a licence and an **authority boundary** | All required fields present; the type and status vocabularies are closed sets | Validator output |
| 2 | E0 | Confirm every `work_packages` reference in the register resolves to a package that exists in the plan | Zero unresolved references | Validator output |
| 3 | E0 | Confirm every `local_modules` path in the register exists on disk | Zero missing paths | Validator output |
| 4 | **E1** | **Self-test.** Run `check_upstream_lineage.py --self-test`: one deliberate defect is injected per rule | **Every rule fires.** The run reports zero silent controls and exits non-zero if any rule stays quiet | Self-test transcript |
| 5 | **E2** | **Pin required.** Move a `DIRECT_ADAPT` entry to status `ADAPTING` with `pinned_commit: null` | Refused, naming the missing pin | Refusal transcript |
| 6 | **E2** | **Characterisation required.** Move a `DIRECT_ADAPT` entry to `ADAPTING` with a pin and a file list but no characterisation suite | Refused, naming the missing suite | Refusal transcript |
| 7 | **E2** | **Licence gate.** Register a `DIRECT_ADAPT` entry under a licence outside the permissive set | Refused; the licence is named | Refusal transcript |
| 8 | **E2** | **Reimplementation carrying files.** Add `source_files` to an `ADAPTIVE_REIMPLEMENT` entry | Refused — if files moved, the decision was direct adaptation and a licence obligation went unrecorded | Refusal transcript |
| 9 | **E2** | **Branch name as a pin.** Set `pinned_commit` to `main` | Refused; a branch is not a pin | Refusal transcript |
| 10 | **E2** | **Planted unregistered file.** Introduce a file marked as adapted with no SPDX header and no register entry, and submit it | CI admission **fails before merge** — ACC-74 | CI transcript |
| 11 | **E1** | **Discrimination control.** Submit a correctly registered adapted file with a pin, a file list and a suite | **Passes.** A check that fails every new file has demonstrated nothing | CI transcript |
| 12 | E1 | Regenerate `provenance/README.md` and run the drift check | The generated index matches the register; hand-editing it fails | Drift check output |
| 13 | **E2** | **Drift.** Advance the upstream reference past a pin and run the drift checker; then attempt an automatic pin update | Divergence reported and a review item opened; the auto-update is refused — ACC-73 | Drift report |
| 14 | E3 | Independent review of the register's `authority_boundary` fields | The reviewer challenges any boundary that states a capability rather than a prohibition | `ReviewRecord` |
| 15 | E5 | Confirm the checker is in the verification bundle and that removing it makes the bundle red | The bundle reports one fewer check and fails | Bundle transcript |

Case 4 is the one that decides whether any of the others mean anything. A
lineage checker that has never been observed to fail reports "no findings" and
"no detector" in identical words, and every remaining case in this table assumes
the rules can fire.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-141   # dependencies and their states
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

A case in **bold** is a refusal case: it passes when the system declines to act.
Half this table is refusals, and a run in which every bold case "worked" has
tested the happy path twice.

### Capturing evidence

```bash
python3 scripts/evidence_manifest.py issue --package WP-141 --gate Platform \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-141/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-141
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-141_upstream_assimilation_governance.acceptance.md) reaches the decision — issuance is not acceptance.

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
