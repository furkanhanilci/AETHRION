---
title: "WP-050 — Initial Tool Connector Package — Test Procedures"
aliases:
  - "WP-050 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/05_MODEL_AGENT_TOOL/WP-050_tool_connectors.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/05-model-agent-tool
  - aethrion/wave/w3
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-050 — Initial Tool Connector Package — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-050` |
| Work package | [`WP-050` — Initial Tool Connector Package](wp_050_tool_connectors.md) |
| Companion | [acceptance criteria](wp_050_tool_connectors.acceptance.md) |
| Workstream | `05_MODEL_AGENT_TOOL` |
| Approval authority | **Security / Connector Owners** — the independent verifier |
| Accountable owner | Tool Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-050` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 4 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Tool Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Tool Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Security / Connector Owners | At completion |
| `WP-049` accepted output | Tool Registry and Tool Broker Core | Tool Platform Lead | Before the first test case runs |

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
| C01 | `Versioned connectors` | Mandatory deliverable | *(name the test case)* |
| C02 | `Connector permission profiles` | Mandatory deliverable | *(name the test case)* |
| C03 | `Connector contract tests` | Mandatory deliverable | *(name the test case)* |
| C04 | `Compensation/reconciliation playbooks` | Mandatory deliverable | *(name the test case)* |
| C05 | Implement the web read/search connector with its allowlist | WP-050-T01 | *(name the test case)* |
| C06 | Write the Crossref and status-lookup connector | WP-050-T02 | *(name the test case)* |
| C07 | Separate the Zotero read, candidate and update-proposal connectors | WP-050-T03 | *(name the test case)* |
| C08 | Add the Git branch/worktree connector | WP-050-T04 | *(name the test case)* |
| C09 | Build the object store signed-upload and reference connector | WP-050-T05 | *(name the test case)* |
| C10 | Bind the MLflow run and metric connector | WP-050-T06 | *(name the test case)* |
| C11 | Write a target resolver and compensation path for every connector | WP-050-T07 | *(name the test case)* |
| C12 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C13 | Agent-Used Source Write-Back | [ACC-02](../12_ACCEPTANCE_SCENARIOS/acc_02_agent_used_source_writeback.md) — Critical | *(name the test case)* |
| C14 | Prompt-Injection PDF | [ACC-05](../12_ACCEPTANCE_SCENARIOS/acc_05_prompt_injection_pdf.md) — Critical | *(name the test case)* |
| C15 | Tool Partial Failure | [ACC-35](../12_ACCEPTANCE_SCENARIOS/acc_35_tool_partial_failure.md) — Critical | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Web allowlist | **E2** | Fetch a host outside the allowlist | Refused at the connector **and** at the egress proxy | Two refusals |
| **TC-02** Web quarantine | **E2** | Fetch a page containing an injected instruction | Returned as quarantined data; scope unchanged (`ACC-05`) | Audit record |
| **TC-03** Crossref lookup | E1 | Resolve a DOI and a retraction status | Both resolve; provenance and retrieval date recorded | Lookup record |
| **TC-04** Crossref absence | E1 | Resolve a DOI that does not exist | Reported as *not found*, never as *clean* | Lookup record |
| **TC-05** **Zotero read-only** | **E2** | Attempt any non-`GET` through the read connector, driven through the whole sync | **Refused structurally.** This closes finding **H3** | Refusal transcript · new test |
| **TC-06** Zotero personal write | **E2** | Attempt a write to a personal library record | Refused. Invariant 5 | Refusal transcript |
| **TC-07** Zotero proposal | **E1** | Propose an update via the proposal connector (`ACC-02`) | A proposal is recorded; **nothing in Zotero changes** | Proposal record · unchanged library |
| **TC-08** Proposal application | **E1** | Have a human apply the proposal | Applied through the update connector, with the human as actor | Applied record |
| **TC-09** Connector collapse | **E2** | Attempt to apply a proposal through the read or candidate connector | Refused — proposing and applying are separate capabilities | Refusal transcript |
| **TC-10** Git scope | **E2** | Write outside the allowed path manifest (WP-023) | Refused | Refusal transcript |
| **TC-11** Object store upload | **E1** | Upload via signed URL | Content-addressed; reference returned, not bytes | Upload record |
| **TC-12** Object overwrite | **E2** | Upload different bytes to an existing address | Refused (WP-026) | Refusal transcript |
| **TC-13** MLflow reference | **E1** | Log a run and an artifact reference | Reference recorded; no copy made (WP-029) | Run record |
| **TC-14** Notification ceiling | **E2** | Send D3 content through a channel with a lower data ceiling | Refused, naming the ceiling | Refusal transcript |
| **TC-15** Compensation — reversible | **E1** | Compensate a Git branch creation | Branch removed | Compensation record |
| **TC-16** Compensation — invalidation | **E1** | Compensate an object upload | Marked `INVALIDATED`, not deleted | Artifact state |
| **TC-17** Compensation — irreversible | **E1** | Compensate a sent notification | Recorded **uncompensated with an owner**; a correction is sent | Compensation record |
| **TC-18** Contract tests | **E1** | Run the connector contract suite | Every connector passes the same broker contract | Suite report |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-050 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-050 --gate G3,G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-050/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-050
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_050_tool_connectors.acceptance.md) reaches the decision — issuance is not acceptance.

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
