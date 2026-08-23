---
title: "WP-075 — Canonical Claim/Evidence Ledger Service — Test Procedures"
aliases:
  - "WP-075 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/08-evidence-assurance
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g5-g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-075 — Canonical Claim/Evidence Ledger Service — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-075` |
| Work package | [`WP-075` — Canonical Claim/Evidence Ledger Service](wp_075_claim_evidence_ledger.md) |
| Companion | [acceptance criteria](wp_075_claim_evidence_ledger.acceptance.md) |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| Approval authority | **Data Architect / Assurance Lead** — the independent verifier |
| Accountable owner | Evidence Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-075` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 8 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5–G10 |
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Evidence Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Evidence Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Data Architect / Assurance Lead | At completion |
| `WP-018` accepted output | Claim, Evidence, Review and Decision Schemas | Evidence Platform Lead | Before the first test case runs |
| `WP-020` accepted output | Schema Registry, Compatibility and Contract SDK | Platform Architecture Lead | Before the first test case runs |
| `WP-025` accepted output | PostgreSQL HA and Registry Data Foundation | Database Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-028` accepted output | NATS JetStream and Transactional Outbox Foundation | Event Platform Lead | Before the first test case runs |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-055` accepted output | SPIFFE/SPIRE Workload Identity and Vault | Identity Platform Lead | Before the first test case runs |
| `WP-056` accepted output | Policy Decision Point and Bundle Distribution | Policy Platform Lead | Before the first test case runs |
| `WP-061` accepted output | Canonical Source Registry Service | Knowledge Platform Lead | Before the first test case runs |

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
| C01 | `Claim Ledger service` | Mandatory deliverable | *(name the test case)* |
| C02 | `Migrations/API` | Mandatory deliverable | *(name the test case)* |
| C03 | `State transition engine` | Mandatory deliverable | *(name the test case)* |
| C04 | `Lineage queries` | Mandatory deliverable | *(name the test case)* |
| C05 | `Service runbook` | Mandatory deliverable | *(name the test case)* |
| C06 | Migrate the claim, evidence, dependency and assessment tables | WP-075-T01 | *(name the test case)* |
| C07 | Write the version, create, challenge and supersede APIs | WP-075-T02 | *(name the test case)* |
| C08 | Bind optimistic locking, actor, policy and outbox events | WP-075-T03 | *(name the test case)* |
| C09 | Apply field-level and data-class RBAC plus access logging | WP-075-T04 | *(name the test case)* |
| C10 | Add the lineage and impact query APIs | WP-075-T05 | *(name the test case)* |
| C11 | Establish backup, integrity checks and the WORM audit export | WP-075-T06 | *(name the test case)* |
| C12 | Retraction Impact | [ACC-04](../12_ACCEPTANCE_SCENARIOS/acc_04_retraction_impact.md) — Critical | *(name the test case)* |
| C13 | Strong Counter-Test | [ACC-08](../12_ACCEPTANCE_SCENARIOS/acc_08_strong_counter_test.md) — Critical | *(name the test case)* |
| C14 | Publication Completeness | [ACC-30](../12_ACCEPTANCE_SCENARIOS/acc_30_publication_completeness.md) — Critical | *(name the test case)* |
| C15 | Superseded Publication | [ACC-31](../12_ACCEPTANCE_SCENARIOS/acc_31_superseded_publication.md) — High | *(name the test case)* |
| C16 | EvidenceGap Lifecycle | [ACC-70](../12_ACCEPTANCE_SCENARIOS/acc_70_evidence_gap_lifecycle.md) — High | *(name the test case)* |
| C17 | Raw Evidence Versus Interpretation | [ACC-78](../12_ACCEPTANCE_SCENARIOS/acc_78_raw_evidence_versus_interpretation.md) — Critical | *(name the test case)* |
| C18 | A Blackboard Entry Is Not Evidence | [ACC-085](../12_ACCEPTANCE_SCENARIOS/acc_085_blackboard_entry_is_not_evidence.md) — Critical | *(name the test case)* |
| C19 | A Claim Without a Complete Evidence Chain | [ACC-105](../12_ACCEPTANCE_SCENARIOS/acc_105_claim_without_evidence_chain.md) — Critical | *(name the test case)* |

**19 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Schema | E0 | Inspect the ledger | Claim, evidence span, dependency, assessment, review link, decision, supersession all present | Schema |
| **TC-02** Create and version | **E1** | Create a claim, then change it | A **new version**; the prior version stays resolvable | Version chain |
| **TC-03** Mutation | **E2** | Attempt an in-place edit of a claim a decision depends on | **Refused** | Refusal transcript |
| **TC-04** Challenge | **E1** | Challenge a supported claim | State moves; the evidence for the challenge is linked | Challenge record |
| **TC-05** Supersede | **E1** | Supersede a published claim | Prior version reachable; publication lineage intact | Supersession chain |
| **TC-06** Optimistic locking | **E2** | Two concurrent writes to one claim | One succeeds; the other gets a version conflict | Conflict transcript |
| **TC-07** Outbox atomicity | **E1** | Change a claim | The event is written in the same transaction | Transaction log |
| **TC-08** Field RBAC | **E2** | Read the producer identity from a reviewer identity | **Denied** — this is what makes blind review enforceable | Denial record |
| **TC-09** Access log | **E1** | Read a claim | Actor, fields and time recorded | Access log |
| **TC-10** Unblinding detection | **E2** | Have a reviewer identity read a producer-identifying field | Denied **and** logged as an attempt | Alert record |
| **TC-11** **Forward lineage** | **E1** | From a claim, resolve source representation, span, run, review and decision | **One query**, every hop — invariant 1 | Query transcript |
| **TC-12** **Impact query** | **E1** | From a retracted source, resolve affected claims | Direct **and derived**, transitively | Impact list |
| **TC-13** Deep derivation | **E2** | Plant a claim four derivation hops from the source | It appears in the impact list | Detection transcript |
| **TC-14** Cycle safety | **E2** | Create a dependency cycle | Refused, or the impact query terminates and reports the cycle | Transcript |
| **TC-15** Integrity check | **E1** | Run the ledger integrity queries | Referential closure holds; no orphan span, no claim with a missing version | Integrity report |
| **TC-16** WORM export | **E2** | Export, then attempt to alter the export | Refused | Refusal transcript |
| **TC-17** Restore | **E1** | Restore and re-run the integrity queries | All pass | Restore transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-075 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-075 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-075/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-075
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_075_claim_evidence_ledger.acceptance.md) reaches the decision — issuance is not acceptance.

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
