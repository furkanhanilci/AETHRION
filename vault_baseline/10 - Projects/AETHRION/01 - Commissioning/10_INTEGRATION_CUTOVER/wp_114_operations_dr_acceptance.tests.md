---
title: "WP-114 — Operations, DR and Restore Acceptance Package — Test Procedures"
aliases:
  - "WP-114 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/10_INTEGRATION_CUTOVER/WP-114_operations_dr_acceptance.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/10-integration-cutover
  - aethrion/wave/w6
  - aethrion/effort/l
  - aethrion/gate/commissioning
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-114 — Operations, DR and Restore Acceptance Package — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-114` |
| Work package | [`WP-114` — Operations, DR and Restore Acceptance Package](wp_114_operations_dr_acceptance.md) |
| Companion | [acceptance criteria](wp_114_operations_dr_acceptance.acceptance.md) |
| Workstream | `10_INTEGRATION_CUTOVER` |
| Approval authority | **Independent DR Witness / Internal Audit** — the independent verifier |
| Accountable owner | SRE Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-114` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Commissioning |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | SRE Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | SRE Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Independent DR Witness / Internal Audit | At completion |
| `WP-025` accepted output | PostgreSQL HA and Registry Data Foundation | Database Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-028` accepted output | NATS JetStream and Transactional Outbox Foundation | Event Platform Lead | Before the first test case runs |
| `WP-030` accepted output | Neo4j, pgvector and OpenSearch Derived Read Models | Knowledge Data Lead | Before the first test case runs |
| `WP-031` accepted output | Temporal Platform, Namespaces and HA | Control Plane Lead | Before the first test case runs |
| `WP-052` accepted output | Kubernetes Cluster and Node Pool Baseline | Platform Infrastructure Lead | Before the first test case runs |
| `WP-099` accepted output | WORM Audit Ledger and Independent Export | Internal Audit Platform Lead | Before the first test case runs |
| `WP-101` accepted output | Service Catalogue, SLOs and Alert/Runbook Binding | SRE Lead | Before the first test case runs |
| `WP-109` accepted output | Forty Acceptance Scenario Registry and Harness | Platform Assurance Lead | Before the first test case runs |

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
| C01 | `Two DR drill reports` | Mandatory deliverable | *(name the test case)* |
| C02 | `Restore manifests` | Mandatory deliverable | *(name the test case)* |
| C03 | `Integrity query results` | Mandatory deliverable | *(name the test case)* |
| C04 | `RPO/RTO scorecard` | Mandatory deliverable | *(name the test case)* |
| C05 | `DR sign-off` | Mandatory deliverable | *(name the test case)* |
| C06 | Plan DR-1 component restore and DR-2 regional/management-plane restore | WP-114-T01 | *(name the test case)* |
| C07 | Restore PostgreSQL PITR, objects, NATS, Temporal, registries, audit and projections | WP-114-T02 | *(name the test case)* |
| C08 | Perform a Zotero full resync and a graph and vault rebuild | WP-114-T03 | *(name the test case)* |
| C09 | Run the workflow, run, claim, source and artifact integrity queries | WP-114-T04 | *(name the test case)* |
| C10 | Measure the on-call, incident, communication and decision timeline | WP-114-T05 | *(name the test case)* |
| C11 | Produce the DR dossier, its gaps and the sign-off | WP-114-T06 | *(name the test case)* |
| C12 | Derived Graph Corruption and Rebuild | [ACC-21](../12_ACCEPTANCE_SCENARIOS/acc_21_graph_corruption.md) — High | *(name the test case)* |
| C13 | Regional / Management Plane DR | [ACC-27](../12_ACCEPTANCE_SCENARIOS/acc_27_regional_dr.md) — Critical | *(name the test case)* |
| C14 | Zotero Full Resync | [ACC-28](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) — High | *(name the test case)* |
| C15 | Complete Project Audit Export | [ACC-40](../12_ACCEPTANCE_SCENARIOS/acc_40_audit_export.md) — Critical | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Drill plan | E0 | Plan DR-1 and DR-2 | Two **distinct** scopes: component, and region/management plane | Plan |
| **TC-02** **Independent operator** | **E1** | Have someone other than the runbook author run each drill | Both run by an independent operator; the runbook is what is tested | Operator record |
| **TC-03** **PostgreSQL PITR** | **E1** | Restore to a point in time | Restored; **integrity queries pass** | Restore transcript · queries |
| **TC-04** Service-start-only | **E2** | Accept a restore on services starting alone | **Refused** as evidence — the queries are the test | Refusal transcript |
| **TC-05** Object store | **E1** | Restore objects and verify a known digest set | All digests match | Digest report |
| **TC-06** NATS and Temporal | **E1** | Restore the backbone and control plane | Open workflows resume; no execution lost | Recovery record |
| **TC-07** Registries | **E1** | Restore source, run, claim and capability registries | All resolve; cross-registry references hold | Integrity report |
| **TC-08** Audit | **E1** | Restore the audit store | The **hash chain verifies across the restore boundary** | Verification output |
| **TC-09** Projections | **E1** | Rebuild derived graph, vector and search | Byte-equivalent to canonical (`ACC-21`) | Rebuild diff |
| **TC-10** **Zotero full resync** | **E1** | Resync after restore against a library edited since | **No duplicates; no human edit overwritten** (WP-067) | Resync report |
| **TC-11** Resync without rebind | **E2** | Resync with dedup/rebind disabled | Duplicates appear — **demonstrating why the procedure includes it** | Contrast record |
| **TC-12** Vault rebuild | **E1** | Rebuild the Obsidian projection | Generated areas return; **human notes survive** | Projection diff |
| **TC-13** **RPO measurement** | **E1** | Measure workflow-state loss | **RPO 0**, recorded as a number | Measurement |
| **TC-14** **RTO measurement** | **E1** | Time each drill end to end | Within the declared target; recorded | Timing |
| **TC-15** **Human timeline** | **E1** | Measure detection → on-call → incident command → decision | Each interval recorded; the decision authority was reachable | Timeline |
| **TC-16** Communication | **E1** | Execute the communication plan | Stakeholders reached; the record is complete | Communication log |
| **TC-17** **Gaps recorded** | **E1** | Capture every runbook gap found | Each becomes a finding with an owner — **a drill that finds nothing is suspect** | Gap register |
| **TC-18** Dossier and sign-off | **E1** | Produce the DR dossier | Both drills, measurements, gaps and sign-off present | Dossier |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-114 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-114 --gate Commissioning \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-114/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-114
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_114_operations_dr_acceptance.acceptance.md) reaches the decision — issuance is not acceptance.

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
