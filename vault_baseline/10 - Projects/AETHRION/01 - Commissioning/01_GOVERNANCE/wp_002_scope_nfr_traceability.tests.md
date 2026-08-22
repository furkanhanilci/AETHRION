---
title: "WP-002 — Scope, NFRs and Requirement Traceability — Test Procedures"
aliases:
  - "WP-002 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/01_GOVERNANCE/WP-002_scope_nfr_traceability.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/01-governance
  - aethrion/wave/w0
  - aethrion/effort/s
  - aethrion/gate/program
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-002 — Scope, NFRs and Requirement Traceability — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-002` |
| Work package | [`WP-002` — Scope, NFRs and Requirement Traceability](wp_002_scope_nfr_traceability.md) |
| Companion | [acceptance criteria](wp_002_scope_nfr_traceability.acceptance.md) |
| Workstream | `01_GOVERNANCE` |
| Approval authority | **Assurance Lead** — the independent verifier |
| Accountable owner | Chief Architect |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-002` |

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
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Chief Architect | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Chief Architect | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead | At completion |
| `WP-001` accepted output | Commissioning Charter and Programme Authority | Executive Sponsor | Before the first test case runs |

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
| C01 | `Requirement Registry` | Mandatory deliverable | *(name the test case)* |
| C02 | `NFR scorecard` | Mandatory deliverable | *(name the test case)* |
| C03 | `Traceability matrix seed` | Mandatory deliverable | *(name the test case)* |
| C04 | `Scope boundary record` | Mandatory deliverable | *(name the test case)* |
| C05 | Extract the functional capability list with `REQ` identifiers | WP-002-T01 | *(name the test case)* |
| C06 | Assign a target, a measurement method and a test owner to every NFR | WP-002-T02 | *(name the test case)* |
| C07 | Separate out the areas that need a domain-specific profile from the generic core | WP-002-T03 | *(name the test case)* |
| C08 | Define the REQ → WP → TST/ACC traceability schema | WP-002-T04 | *(name the test case)* |
| C09 | Record the out-of-scope items and the rules for handling future requests | WP-002-T05 | *(name the test case)* |

**9 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-001 is `ACCEPTED`; the capability list is drafted; the
`REQ` identifier scheme is chosen.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate every `REQ` entry against the requirement schema | Identifier, statement, target, measurement method, test owner and verification type all present | Schema validation output |
| 2 | E0 | Confirm identifier uniqueness and format across the whole register | Zero duplicates; every `REQ-*` matches the scheme | Register lint output |
| 3 | **E1** | **Testability screen.** For each requirement, state the observation that would falsify it | Every requirement has one. Any that does not is **reclassified as a preference** and moved to the preference register | Testability screen table |
| 4 | E1 | Confirm each NFR target names a number and a unit | Zero adjectival targets | NFR table |
| 5 | E1 | Confirm each NFR names how it is measured and by whom | Zero targets with an unassigned measurement | NFR table |
| 6 | E0 | Resolve `REQ → WP` in both directions | Every `REQ` maps to at least one package; every package maps to at least one `REQ`; unmapped entries in either direction are listed, not hidden | Traceability report |
| 7 | E0 | Resolve `REQ → TST/ACC` | Every `REQ` names the test or acceptance scenario that demonstrates it; the 39 packages currently bound to no scenario are surfaced here | Traceability report |
| 8 | **E2** | **Negative traceability test.** Introduce a synthetic `REQ` with no package and a synthetic package with no `REQ` | The traceability check **fails** and names both | Failing check transcript |
| 9 | E1 | Confirm the go-live dossier query `REQ → WP → TST/ACC → Evidence → Decision` executes end-to-end on at least one real requirement | The chain returns every hop with no manual joining | Query transcript |
| 10 | E1 | Confirm the out-of-scope register states, for each entry, **why** it is out of scope and what would bring it back | No bare exclusions | Out-of-scope register |
| 11 | E3 | Independent review of the testability screen specifically | The reviewer re-runs step 3 on a sample and disputes any requirement they cannot falsify | `ReviewRecord` with sample size and disputed entries |
| 12 | E1 | Confirm the future-request handling rule distinguishes a **correction** from an **addition** | The rule matches §7.4: a correction keeps the finish line, an addition moves it and goes to V2 | Change-handling clause |

Step 3 is the package. Steps 8 and 11 exist because a traceability matrix that
has never been observed to fail, and a testability screen nobody has challenged,
are both decoration.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-002 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-002 --gate Program \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-002/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-002
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_002_scope_nfr_traceability.acceptance.md) reaches the decision — issuance is not acceptance.

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
