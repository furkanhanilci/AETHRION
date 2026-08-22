# WP-012 — Canonical Ownership and Field-Level Authority Matrix — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-012` |
| Work package | [`WP-012` — Canonical Ownership and Field-Level Authority Matrix](WP-012_canonical_field_authority.md) |
| Companion | [acceptance criteria](WP-012_canonical_field_authority.acceptance.md) |
| Workstream | `02_CONTRACTS` |
| Approval authority | **Internal Audit / Knowledge Lead** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-012` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 3 acceptance scenario(s) |
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
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Internal Audit / Knowledge Lead | At completion |
| `WP-010` accepted output | Architecture Decision and Rejected-Alternatives Baseline | Chief Architect | Before the first test case runs |
| `WP-011` accepted output | Identity and End-to-End Correlation Standard | Data Platform Lead | Before the first test case runs |

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
| C01 | `Canonical Ownership Matrix` | Mandatory deliverable | *(name the test case)* |
| C02 | `Field Authority Table` | Mandatory deliverable | *(name the test case)* |
| C03 | `Sync direction map` | Mandatory deliverable | *(name the test case)* |
| C04 | `Conflict ownership matrix` | Mandatory deliverable | *(name the test case)* |
| C05 | Assign the canonical record for every bounded context | WP-012-T01 | *(name the test case)* |
| C06 | Define human versus agent field authority across the Source Registry and Zotero | WP-012-T02 | *(name the test case)* |
| C07 | Write the authority rules for the human and generated blocks in Obsidian | WP-012-T03 | *(name the test case)* |
| C08 | Add the rebuild rule for derived graphs and indexes | WP-012-T04 | *(name the test case)* |
| C09 | Assign owners for conflict, merge, tombstone and reconciliation cases | WP-012-T05 | *(name the test case)* |
| C10 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/ACC-03_duplicate_collision.md) — High | *(name the test case)* |
| C11 | Derived Graph Corruption and Rebuild | [ACC-21](../12_ACCEPTANCE_SCENARIOS/ACC-21_graph_corruption.md) — High | *(name the test case)* |
| C12 | Obsidian Human Edit Preservation | [ACC-22](../12_ACCEPTANCE_SCENARIOS/ACC-22_obsidian_human_edit.md) — High | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-011 is `ACCEPTED`; both surfaces of at least one real pair
(Zotero ↔ registry) are reachable in a test environment.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate the Canonical Ownership Matrix: every bounded context names exactly one canonical record | Zero contexts with two; zero with none | Matrix |
| 2 | **E0** | **Field granularity test.** Confirm authority is assigned per field, not per record | At least one record demonstrably has two field authorities; a record-level matrix fails here | Field Authority Table |
| 3 | E0 | Confirm every field that appears on two surfaces has a sync direction and a conflict rule | Zero fields with a direction and no conflict rule | Sync direction map |
| 4 | **E2** | **Write-authority test.** Attempt an agent write to a human-authority Zotero field | Rejected. The rejection names the field and its authority | Rejection transcript |
| 5 | **E2** | **Generated-zone test.** Place a human note inside the generated Obsidian area, then project | The note survives; only manifest-listed files are removed | Projection transcript |
| 6 | **E2** | **Conflict test.** Change the same field on both surfaces between syncs | The conflict rule fires; the loser is preserved as a conflict record rather than overwritten | Conflict record |
| 7 | **E2** | **Deletion-authority test.** Delete a source in Zotero | The registry applies the assigned rule — tombstone, or retain-with-flag — and does **not** silently keep it as current. This is where finding **H2** is closed | Reconciliation transcript |
| 8 | **E1** | **Rebuild test.** Delete every derived graph and index and rebuild from canonical records | The rebuild is byte-equivalent for all derived state. Anything that cannot be rebuilt is **canonical** and the matrix is corrected | Rebuild diff |
| 9 | E1 | Confirm the reconciliation job reports divergence rather than silently repairing it | Divergence produces a record with an owner | Reconciliation report |
| 10 | E1 | Confirm every conflict class has a named owner | Zero unowned conflict classes | Conflict ownership matrix |
| 11 | E3 | Independent review looking for a field that appears on two surfaces and is absent from the matrix | Any found is a finding | `ReviewRecord` |

Step 8 is the falsification test for the whole matrix, and it is the one most
likely to be skipped because it is expensive. It is also the only step that can
prove the matrix wrong rather than merely consistent.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-012 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-012 --gate Platform \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-012/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-012
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-012_canonical_field_authority.acceptance.md) reaches the decision — issuance is not acceptance.

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
