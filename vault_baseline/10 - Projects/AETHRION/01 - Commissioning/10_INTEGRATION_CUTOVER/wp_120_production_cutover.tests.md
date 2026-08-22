---
title: "WP-120 — Production Cutover and Go-Live Decision — Test Procedures"
aliases:
  - "WP-120 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-120_production_cutover.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w8
  - aethrion/effort/l
  - aethrion/gate/cutover
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-120 — Production Cutover and Go-Live Decision — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-120` |
| Work package | [`WP-120` — Production Cutover and Go-Live Decision](wp_120_production_cutover.md) |
| Companion | [acceptance criteria](wp_120_production_cutover.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Commissioning Board / Internal Audit** — the independent verifier |
| Accountable owner | Executive Sponsor / Program Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-120` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 2 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Cutover |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Executive Sponsor / Program Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Executive Sponsor / Program Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Commissioning Board / Internal Audit | At completion |
| `WP-115` accepted output | Full System Regression and Commissioning Dossier | Platform Assurance Lead | Before the first test case runs |
| `WP-116` accepted output | Resilience, Chaos and Failure-Injection Commissioning | SRE Lead | Before the first test case runs |
| `WP-117` accepted output | Performance, Capacity and Load Commissioning | Capacity Engineering Lead | Before the first test case runs |
| `WP-118` accepted output | Operational Readiness, On-Call and Runbook Simulation | SRE Lead | Before the first test case runs |
| `WP-119` accepted output | Controlled Pilot and Cutover Rehearsal | Program Lead | Before the first test case runs |

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
| C01 | `Cutover execution log` | Mandatory deliverable | *(name the test case)* |
| C02 | `Go-Live DecisionRecord` | Mandatory deliverable | *(name the test case)* |
| C03 | `Production release manifest` | Mandatory deliverable | *(name the test case)* |
| C04 | `Smoke/integrity results` | Mandatory deliverable | *(name the test case)* |
| C05 | `Audit snapshot` | Mandatory deliverable | *(name the test case)* |
| C06 | Freeze the final RC, policy, schema, model, tool and infrastructure digests | WP-120-T01 | *(name the test case)* |
| C07 | Take the pre-cutover backup and restore point and run the owner check | WP-120-T02 | *(name the test case)* |
| C08 | Apply the IaC/GitOps deployment and migration steps | WP-120-T03 | *(name the test case)* |
| C09 | Run the service, contract, security and integrity smoke tests | WP-120-T04 | *(name the test case)* |
| C10 | Enable traffic, user access and monitoring in a controlled sequence | WP-120-T05 | *(name the test case)* |
| C11 | Record the go / no-go / abort decision with its evidence | WP-120-T06 | *(name the test case)* |
| C12 | Take the post-cutover audit snapshot | WP-120-T07 | *(name the test case)* |
| C13 | Human Seed Literature | [ACC-01](../12_ACCEPTANCE_SCENARIOS/acc_01_human_seed_literature.md) — Critical | *(name the test case)* |
| C14 | Complete Project Audit Export | [ACC-40](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) — Critical | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** **Entry conditions** | **E2** | Attempt cutover with any go-live entry condition unmet | **Refused**, naming the condition | One refusal per unmet condition |
| **TC-02** Open critical | **E2** | Attempt with an open Critical finding | Refused | Refusal transcript |
| **TC-03** Expired residual | **E2** | Attempt with a residual-risk acceptance past its expiry | Refused — an expired acceptance is an open finding | Refusal transcript |
| **TC-04** Two rehearsals | **E2** | Attempt with only one restore rehearsal | Refused | Refusal transcript |
| **TC-05** **Digest freeze** | **E1** | Freeze RC, policy, schema, model, tool and infrastructure digests | All six recorded; the set is signed | Freeze record |
| **TC-06** Unfrozen component | **E2** | Attempt with any component referenced by tag | Refused (WP-027) | Refusal transcript |
| **TC-07** **Verified restore point** | **E1** | Take the pre-cutover backup and **verify it** | Restore point verified, not merely taken; owner check complete | Verification record |
| **TC-08** Unverified restore point | **E2** | Proceed with an unverified backup | **Refused** — `PR-13` at the worst possible moment | Refusal transcript |
| **TC-09** Deployment | **E1** | Apply IaC/GitOps deployment and migrations | Applied; a second apply is a no-op | Deployment record |
| **TC-10** Migration rollback ready | **E1** | Confirm each migration has a rehearsed rollback | All do | Migration report |
| **TC-11** Service smoke | **E1** | Run the service smoke tests | All pass on the promoted RC | Smoke report |
| **TC-12** Contract smoke | **E1** | Run contract tests | Every producer/consumer pair green | Contract report |
| **TC-13** Security smoke | **E1** | Run the security smoke set | Fail-closed behaviours confirmed on the live configuration | Security report |
| **TC-14** **Integrity smoke** | **E1** | Run the integrity queries | Referential closure holds post-migration | Integrity report |
| **TC-15** **Sequenced enablement** | **E1** | Enable traffic, access and monitoring in the declared order | Each step observed before the next; **each reversible** | Enablement log |
| **TC-16** Reverse a step | **E1** | Reverse one enablement step | Reverses cleanly | Reversal transcript |
| **TC-17** **Abort available** | **E1** | Confirm abort is available at each stage | Available throughout, including after promotion | Abort readiness record |
| **TC-18** Abort exercised | **E1** | Exercise abort at a declared threshold in the rehearsal environment | Returns to the verified restore point | Abort transcript |
| **TC-19** Abort authority | **E2** | Attempt abort by an unauthorised actor, and delegate it | Both refused (WP-001, WP-004) | Two refusals |
| **TC-20** **Go-Live `DecisionRecord`** | **E1** | Record the decision | Names the actor, the evidence, the residual risks with owners and expiries, and **what was not authorised** | `DecisionRecord` |
| **TC-21** No-go reachable | **E1** | Confirm `no-go` and `abort` are recordable outcomes | Both supported | Decision options |
| **TC-22** **Post-cutover snapshot** | **E1** | Take the audit snapshot | Hash-chained; verifies standalone; becomes the baseline for later checks | Snapshot |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-120 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-120 --gate Cutover \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-120/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-120
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_120_production_cutover.acceptance.md) reaches the decision — issuance is not acceptance.

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
