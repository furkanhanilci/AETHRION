---
title: "WP-061 — Canonical Source Registry Service — Test Procedures"
aliases:
  - "WP-061 tests"
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/07-literature-knowledge
  - aethrion/wave/w4
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-061 — Canonical Source Registry Service — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-061` |
| Work package | [`WP-061` — Canonical Source Registry Service](wp_061_source_registry_service.md) |
| Companion | [acceptance criteria](wp_061_source_registry_service.acceptance.md) |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| Approval authority | **Data Architect / Citation Auditor** — the independent verifier |
| Accountable owner | Knowledge Platform Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-061` |

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
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Knowledge Platform Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Platform Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Data Architect / Citation Auditor | At completion |
| `WP-012` accepted output | Canonical Ownership and Field-Level Authority Matrix | Chief Architect | Before the first test case runs |
| `WP-017` accepted output | Source Registry and Literature Contract Schemas | Knowledge Lead | Before the first test case runs |
| `WP-020` accepted output | Schema Registry, Compatibility and Contract SDK | Platform Architecture Lead | Before the first test case runs |
| `WP-025` accepted output | PostgreSQL HA and Registry Data Foundation | Database Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-028` accepted output | NATS JetStream and Transactional Outbox Foundation | Event Platform Lead | Before the first test case runs |
| `WP-055` accepted output | SPIFFE/SPIRE Workload Identity and Vault | Identity Platform Lead | Before the first test case runs |
| `WP-056` accepted output | OPA Policy Platform and Bundle Distribution | Policy Platform Lead | Before the first test case runs |

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
| C01 | `Source Registry service` | Mandatory deliverable | *(name the test case)* |
| C02 | `Database migrations` | Mandatory deliverable | *(name the test case)* |
| C03 | `API/OpenAPI` | Mandatory deliverable | *(name the test case)* |
| C04 | `Outbox events` | Mandatory deliverable | *(name the test case)* |
| C05 | `Service runbook` | Mandatory deliverable | *(name the test case)* |
| C06 | Migrate the `SourceRecord`, representation, trust and binding tables | WP-061-T01 | *(name the test case)* |
| C07 | Write the create, read, version, merge and tombstone APIs | WP-061-T02 | *(name the test case)* |
| C08 | Bind optimistic concurrency and outbox event emission | WP-061-T03 | *(name the test case)* |
| C09 | Apply field authority and data-class RBAC | WP-061-T04 | *(name the test case)* |
| C10 | Add search, filter, history and bulk ingest APIs | WP-061-T05 | *(name the test case)* |
| C11 | Establish backups, SLOs and the audit queries | WP-061-T06 | *(name the test case)* |
| C12 | Duplicate and Metadata Collision | [ACC-03](../12_ACCEPTANCE_SCENARIOS/acc_03_duplicate_collision.md) — High | *(name the test case)* |
| C13 | Zotero Full Resync | [ACC-28](../12_ACCEPTANCE_SCENARIOS/acc_28_zotero_full_resync.md) — High | *(name the test case)* |

**13 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Schema migration | **E1** | Migrate the V0 registry's 33 records | All present; **every prior `airl_id` still resolves** | Migration report |
| **TC-02** Identity stability | **E2** | Compare pre- and post-migration identifiers | Zero re-minted identities. A citation that resolved yesterday resolves today | Identity diff |
| **TC-03** Identity minting | **E1** | Create a new source | Minted through WP-011's standard, with the population ceiling recorded — closing **L2** | Source record |
| **TC-04** Create/read | E1 | Create and read back | Round-trips with every field | API transcript |
| **TC-05** Version | **E1** | Update a source | A new version; the prior version stays resolvable | Version chain |
| **TC-06** Merge | **E2** | Merge two records | Lineage names both; **every prior citation resolves to the survivor** | Merge lineage |
| **TC-07** **Tombstone** | **E1** | Tombstone a source removed upstream | Redirects rather than disappears; dependent claims still resolve — closing **H2**'s registry half | Tombstone record |
| **TC-08** Optimistic concurrency | **E2** | Two concurrent updates to one record | One succeeds; the other is **refused with a version conflict**, not silently overwritten | Conflict transcript |
| **TC-09** Outbox atomicity | **E1** | Update a source | The change event is written in the same transaction (WP-028) | Transaction log |
| **TC-10** Rollback | **E2** | Force a rollback after the outbox write | **No event published** | Absence proof |
| **TC-11** Field authority | **E2** | Write a human-authority field from an agent identity | Refused **at the API**, naming the field (WP-012) | Refusal transcript |
| **TC-12** Data-class RBAC | **E2** | Read a D3 field with a D0-scoped identity | Denied | Denial record |
| **TC-13** **Bulk ingest paging** | **E1** | Ingest more than 100 sources | All ingested; `Total-Results` read; **no silent truncation** — closing **H1**'s registry half | Ingest report |
| **TC-14** Search and filter | E1 | Query by identifier, DOI, title, status and project | Each returns correctly | Query transcript |
| **TC-15** History | E1 | Read a record's full history | Every version, actor and timestamp present | History output |
| **TC-16** Connection lifetime | **E1** | Run sustained load | Connections are pooled and returned; **no leak** — the V0 pattern (**M8**) is not carried forward | Pool telemetry |
| **TC-17** Restore | **E1** | Restore and run the integrity queries (WP-025) | All pass | Restore transcript |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-061 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-061 --gate G3 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-061/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-061
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_061_source_registry_service.acceptance.md) reaches the decision — issuance is not acceptance.

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
