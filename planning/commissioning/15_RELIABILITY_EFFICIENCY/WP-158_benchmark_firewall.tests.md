# WP-158 — Benchmark Firewall and External Evaluation Qualification — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-158` |
| Work package | [`WP-158` — Benchmark Firewall and External Evaluation Qualification](WP-158_benchmark_firewall.md) |
| Companion | [acceptance criteria](WP-158_benchmark_firewall.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Assurance Lead / Research Director** — the independent verifier |
| Accountable owner | Eval Office |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-158` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 1 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | no | no execution or reproduction gate |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform |

**Applicable layers: E0 · E1 · E2 · E3 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Eval Office | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Eval Office | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Assurance Lead / Research Director | At completion |
| `WP-043` accepted output | Role-Based Model and Skill Evaluation, and Golden Set Management | Eval Office | Before the first test case runs |
| `WP-057` accepted output | Default-Deny Egress Proxy, DLP and Allowlist | Network Security Lead | Before the first test case runs |
| `WP-115` accepted output | Full System Regression and Commissioning Dossier | Platform Assurance Lead | Before the first test case runs |
| `WP-149` accepted output | Sparse Communication Topology and the Scientific Blackboard | Chief Architect | Before the first test case runs |

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
| C01 | `BenchmarkRunPolicy` | Mandatory deliverable | *(name the test case)* |
| C02 | `Contamination scanner and audit log` | Mandatory deliverable | *(name the test case)* |
| C03 | `ContaminationFinding` | Mandatory deliverable | *(name the test case)* |
| C04 | `Baseline arm and frontier report` | Mandatory deliverable | *(name the test case)* |
| C05 | Define `BenchmarkRunPolicy` and freeze it before execution | WP-158-T01 | *(name the test case)* |
| C06 | Implement network mode and allowed-domain enforcement per run | WP-158-T02 | *(name the test case)* |
| C07 | Implement the retrieval audit log and the contamination scanner | WP-158-T03 | *(name the test case)* |
| C08 | Define `ContaminationFinding` and the CONTAMINATED / REVIEW_REQUIRED labels | WP-158-T04 | *(name the test case)* |
| C09 | Enforce evaluator, rubric and gold-answer isolation from the agent environment | WP-158-T05 | *(name the test case)* |
| C10 | Build the fully-connected baseline arm and the frontier report | WP-158-T06 | *(name the test case)* |
| C11 | Bind labelled results into the release dossier | WP-158-T07 | *(name the test case)* |
| C12 | Search-Time Benchmark Contamination | [ACC-118](../12_ACCEPTANCE_SCENARIOS/ACC-118_benchmark_search_time_contamination.md) — Critical | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-057 supplies egress control so a network mode can actually be enforced; WP-149 supplies the fully-connected baseline arm; at least one external benchmark and its dataset manifest are obtainable.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `BenchmarkRunPolicy` and `ContaminationFinding` | Both validate; the policy fields are required before a run may start | Validator output |
| 2 | **E2** | **Frozen before start.** Attempt to modify the benchmark policy mid-run | Refused | Refusal transcript |
| 3 | E1 | Freeze dataset manifest digest, network mode, allowed domains, known identifiers and evaluator isolation | All five recorded before execution | Policy record |
| 4 | **E2** | **Evaluator isolation.** Attempt to reach gold answers, the private rubric, hidden tests and the grader prompt from the agent environment | All four unreachable | Four denial transcripts |
| 5 | **E1** | **Contaminated run.** Execute with benchmark material reachable through retrieval | Labelled `CONTAMINATED` or `REVIEW_REQUIRED` — ACC-118 | Run label |
| 6 | **E2** | **Not scored clean.** Attempt to report the contaminated run's score as clean | Refused; the label travels with the score | Refusal transcript |
| 7 | **E2** | **No silent rerun.** Attempt to rerun and report a clean score from the retry | Refused and recorded as an attempt | Refusal transcript |
| 8 | **E1** | **Clean run.** Execute under restricted retrieval with no benchmark material reachable | Reported clean — the scanner discriminates | Run label |
| 9 | **E1** | **False positive path.** Retrieve a legitimate paper that discusses the benchmark | `REVIEW_REQUIRED`, routed to a human rather than auto-judged | Finding |
| 10 | E1 | Read the full retrieval audit log for both runs | Complete; every retrieval recorded | Audit log |
| 11 | **E4** | **Baseline arm.** Run the fully-connected cohort under the same policy, manifest and budget | Completes; emits the same metric schema — ACC-086 | Run record |
| 12 | E1 | Compute and publish the quality/cost frontier for both arms | A frontier, not a headline number | Frontier report |
| 13 | **E2** | **Not a single agent.** Attempt to substitute a single-agent arm for the baseline | Refused; the baseline is the fully-connected cohort | Refusal transcript |
| 14 | E1 | Bind both labelled results into the release dossier | Labels present in the dossier | Dossier extract |
| 15 | E3 | Independent review of one benchmark run's policy, log and label | The reviewer can say what the score is a measurement of | `ReviewRecord` |

Cases 5 and 8 are the pair that gives the scanner meaning, and case 9 is the one
that keeps it usable. A scanner with no false-positive path either suppresses good
runs or waves through bad ones, and `REVIEW_REQUIRED` is where a human absorbs the
ambiguity instead of the pipeline guessing.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-158   # dependencies and their states
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

A case in **bold** is a refusal or an injection: it passes when the system
declines to act, or when a deliberately caused fault is caught. Most of this
table is one or the other, because a reliability package that only exercises the
happy path has tested the thing that was never in doubt.

### Capturing evidence

```bash
python3 scripts/evidence_manifest.py issue --package WP-158 --gate G6 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-158/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-158
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-158_benchmark_firewall.acceptance.md) reaches the decision — issuance is not acceptance.

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
