# WP-125 — Literature, Zotero and Obsidian Curation Rhythm — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-125` |
| Work package | [`WP-125` — Literature, Zotero and Obsidian Curation Rhythm](WP-125_literature_knowledge_curation.md) |
| Companion | [acceptance criteria](WP-125_literature_knowledge_curation.acceptance.md) |
| Workstream | `11_DAY2_OPERATIONS` |
| Approval authority | **Citation Auditor / Knowledge Curator** — the independent verifier |
| Accountable owner | Knowledge Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-125` |

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
| Target revision | The single commit every result is bound to | Knowledge Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Knowledge Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Citation Auditor / Knowledge Curator | At completion |
| `WP-061` accepted output | Canonical Source Registry Service | Knowledge Platform Lead | Before the first test case runs |
| `WP-062` accepted output | Source Identity Resolution, Deduplication and Merge | Source Resolver Lead | Before the first test case runs |
| `WP-063` accepted output | Source Representation, Licence and Status Monitoring | Knowledge Lead | Before the first test case runs |
| `WP-064` accepted output | Zotero Library, Collection and Permission Model | Knowledge Lead | Before the first test case runs |
| `WP-065` accepted output | Personal Zotero Seed Ingest Pipeline | Knowledge Platform Lead | Before the first test case runs |
| `WP-066` accepted output | Agent Candidate and Used-Source Write-Back | Knowledge Platform Lead | Before the first test case runs |
| `WP-067` accepted output | Zotero Two-Way Sync and Reconciliation | Knowledge Platform Lead | Before the first test case runs |
| `WP-068` accepted output | Zotero Annotation → EvidenceCandidate Pipeline | Evidence Intake Lead | Before the first test case runs |
| `WP-069` accepted output | SearchProtocol and LiteratureCampaign Orchestration | Evidence Lead | Before the first test case runs |
| `WP-070` accepted output | Human + Agent Two-Way Literature Discovery | Evidence Lead | Before the first test case runs |
| `WP-071` accepted output | Screening, Inclusion/Exclusion and Coverage | Evidence Lead | Before the first test case runs |
| `WP-072` accepted output | LiteratureSetManifest Freeze and Human-Readable Archive | Evidence Lead | Before the first test case runs |
| `WP-073` accepted output | Obsidian Vault, Human/Generated Zones and Templates | Knowledge Lead | Before the first test case runs |
| `WP-074` accepted output | Obsidian Projection, Link Integrity and Knowledge Write-Back | Knowledge Platform Lead | Before the first test case runs |
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
| C01 | `Curation calendar` | Mandatory deliverable | *(name the test case)* |
| C02 | `Queue/SLA reports` | Mandatory deliverable | *(name the test case)* |
| C03 | `Library quality scorecard` | Mandatory deliverable | *(name the test case)* |
| C04 | `Knowledge integrity report` | Mandatory deliverable | *(name the test case)* |
| C05 | Run the daily sync/conflict/lag check and the weekly curator queue review | WP-125-T01 | *(name the test case)* |
| C06 | Track candidate TTL, used-source promotion and duplicate metrics | WP-125-T02 | *(name the test case)* |
| C07 | Run the monthly status, retraction and broken-link scan | WP-125-T03 | *(name the test case)* |
| C08 | Check the Obsidian human/generated diff and projection integrity | WP-125-T04 | *(name the test case)* |
| C09 | Perform the quarterly library, group, permission and licence review | WP-125-T05 | *(name the test case)* |

**9 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Daily sync check | **E1** | Run the daily sync, conflict and lag check | Lag within threshold; conflicts counted | Check report |
| **TC-02** **Failed sync visible** | **E2** | Fail a sync | Surfaced the same day; the library is **not presented as current** | Alert · dashboard |
| **TC-03** Weekly curator review | **E1** | Review every curator queue | Each queue's depth and oldest item recorded | Review record |
| **TC-04** Ageing queue item | **E2** | Let an item pass its SLA | Escalates | Escalation record |
| **TC-05** **Candidate TTL** | **E1** | Age an unscreened candidate past its TTL | **Expired with the expiry recorded**, so the coverage claim stays honest | Expiry record |
| **TC-06** Silent accumulation | **E2** | Detect a queue growing without bound | Raised as a finding | Finding record |
| **TC-07** Used-source promotion | **E1** | Promote sources a claim actually used | Written to `40_Used` with the claim reference (WP-066) | Promotion record |
| **TC-08** Duplicate metrics | **E1** | Track the duplicate and **false-merge rate** | Both reported as numbers | Metrics report |
| **TC-09** **Monthly status scan** | **E1** | Run the retraction and correction scan | Detections routed to `ImpactScan`; dispositions tracked | Scan report |
| **TC-10** **Positive control** | **E2** | Run the scan with the known-retracted control removed | The scan **fails**, not reports clean | Failure transcript |
| **TC-11** **Coverage fraction** | **E1** | Report scan coverage | The **monitored fraction** stated and the unmonitored sources named | Coverage report |
| **TC-12** Broken-link scan | **E1** | Run the link scan | Broken links and orphans routed to the curator queue | Lint output |
| **TC-13** **Vault integrity** | **E1** | Run `check_vault.py` | Links resolve, frontmatter present, tags in vocabulary, no orphans | Lint output |
| **TC-14** **Human/generated diff** | **E2** | Detect a human edit inside a generated zone | Reported as drift; the human's text is recoverable | Drift report |
| **TC-15** Projection integrity | **E1** | Verify projection byte-stability | Unchanged input rewrites nothing | Snapshot comparison |
| **TC-16** **Quarterly library review** | **E1** | Review group membership, permissions and licences | Each confirmed or changed **with a reason** | Review record |
| **TC-17** Licence change | **E2** | Detect a source whose licence no longer permits retention | Bytes removed; hash-only reference retained (`PR-14`) | Remediation record |
| **TC-18** Permission loss | **E2** | Detect a library the system can no longer read | Distinguished from deletion; reported | State record |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-125 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-125 --gate G3,G10,Day-2 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-125/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-125
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-125_literature_knowledge_curation.acceptance.md) reaches the decision — issuance is not acceptance.

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
