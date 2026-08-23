---
title: "WP-159 — Supply Chain, Upstream Drift and Cross-Plane Integrity — Test Procedures"
aliases:
  - "WP-159 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/15_RELIABILITY_EFFICIENCY/WP-159_supply_chain_and_cross_plane_integrity.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/15-reliability-efficiency
  - aethrion/wave/wr
  - aethrion/effort/l
  - aethrion/gate/platform
  - aethrion/gate/g5
  - aethrion/gate/g9
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-159 — Supply Chain, Upstream Drift and Cross-Plane Integrity — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-159` |
| Work package | [`WP-159` — Supply Chain, Upstream Drift and Cross-Plane Integrity](wp_159_supply_chain_and_cross_plane_integrity.md) |
| Companion | [acceptance criteria](wp_159_supply_chain_and_cross_plane_integrity.acceptance.md) |
| Workstream | `15_RELIABILITY_EFFICIENCY` |
| Approval authority | **Chief Architect / SRE Lead** — the independent verifier |
| Accountable owner | Supply Chain Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-159` |

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
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform |

**Applicable layers: E0 · E1 · E2 · E3 · E4 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Supply Chain Security Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Supply Chain Security Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Chief Architect / SRE Lead | At completion |
| `WP-024` accepted output | CI Foundation and Deterministic Quality Gates | Engineering Productivity Lead | Before the first test case runs |
| `WP-027` accepted output | Git, OCI Registry and Build Provenance Foundation | Supply Chain Security Lead | Before the first test case runs |
| `WP-059` accepted output | Supply-Chain Admission, Sigstore and SLSA Policy | Supply Chain Security Lead | Before the first test case runs |
| `WP-141` accepted output | Upstream Assimilation, Lineage and Characterisation Governance | Chief Architect | Before the first test case runs |

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
| C01 | `SPDX/REUSE conformance` | Mandatory deliverable | *(name the test case)* |
| C02 | `OSV and Scorecard integration` | Mandatory deliverable | *(name the test case)* |
| C03 | `SLSA provenance and signature verification` | Mandatory deliverable | *(name the test case)* |
| C04 | `Split-brain injection suite` | Mandatory deliverable | *(name the test case)* |
| C05 | `Correlation chain with redaction` | Mandatory deliverable | *(name the test case)* |
| C06 | Integrate SPDX and REUSE conformance into CI | WP-159-T01 | *(name the test case)* |
| C07 | Integrate OSV-Scanner over the lockfile and images | WP-159-T02 | *(name the test case)* |
| C08 | Integrate OpenSSF Scorecard for dependency admission | WP-159-T03 | *(name the test case)* |
| C09 | Produce SLSA provenance and verify Sigstore signatures at release | WP-159-T04 | *(name the test case)* |
| C10 | Bind the upstream lineage register to admission and drift review | WP-159-T05 | *(name the test case)* |
| C11 | Implement the outbox write path and its atomicity guarantee | WP-159-T06 | *(name the test case)* |
| C12 | Build the split-brain injection suite and the projection rebuild proof | WP-159-T07 | *(name the test case)* |
| C13 | Complete the OpenTelemetry correlation chain with data-class redaction | WP-159-T08 | *(name the test case)* |
| C14 | Destructive Projection Rebuild | [ACC-119](../12_ACCEPTANCE_SCENARIOS/acc_119_derived_projection_destructive_rebuild.md) — Critical | *(name the test case)* |
| C15 | Missing Upstream Licence or Provenance | [ACC-120](../12_ACCEPTANCE_SCENARIOS/acc_120_missing_upstream_license_provenance.md) — High | *(name the test case)* |

**15 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

**Preconditions.** WP-024 supplies a CI platform that can fail a merge; WP-141 supplies the upstream register this binds to admission; canonical stores and at least one derived projection exist so the rebuild can be attempted destructively.

| # | Layer | Step | Expected result | Evidence artifact |
|---:|---|---|---|---|
| 1 | E0 | Validate `UpstreamAssimilationRecord` and confirm SPDX headers parse across the tree | All parse; REUSE conformance reported | Conformance report |
| 2 | **E2** | **Unregistered adapted file.** Introduce an adapted file with no SPDX header, register entry or pin | Admission **fails before merge** — ACC-120 | CI transcript |
| 3 | **E1** | **Discrimination control.** Introduce a correctly registered adapted file | **Passes.** A check that fails every new file has demonstrated nothing | CI transcript |
| 4 | E1 | Run OSV-Scanner over the lockfile and images | Findings reported with severity | Scan report |
| 5 | E1 | Run OpenSSF Scorecard over the dependency set | Posture reported per project | Scorecard report |
| 6 | **E1** | **Unfixable finding.** Introduce a dependency with a known vulnerability and no available fix | Becomes an owned residual risk with an expiry — not suppressed, not blocking indefinitely | Risk record |
| 7 | E1 | Produce SLSA provenance and verify Sigstore signatures for a release artifact | Both verify | Attestation + verification |
| 8 | **E2** | **Unsigned artifact.** Attempt to release an unsigned artifact | Refused | Refusal transcript |
| 9 | **E2** | **Upstream drift.** Advance an upstream past its pin and attempt an automatic update | Drift reported, review item opened, auto-update refused | Drift report |
| 10 | **E1** | **Outbox atomicity.** Kill the publisher immediately after a canonical commit | The event is published on recovery; canonical state is correct throughout | Recovery record |
| 11 | **E2** | **Duplicate and out-of-order events.** Deliver the same event twice, then out of order | No canonical state change; consumers validate identity and version — ACC-119 | State comparison |
| 12 | **E2** | **Cancelled task result.** Return a LangGraph result after its task was cancelled | Discarded; no canonical write | Rejection record |
| 13 | **E2** | **Concurrent transitions.** Attempt two gate transitions on one project simultaneously | One succeeds; the other is refused explicitly, not silently lost | Two transcripts |
| 14 | **E4** | **Destructive rebuild.** Destroy every derived projection and rebuild from canonical stores | Lossless against the pre-capture — ACC-119 | Before/after comparison |
| 15 | **E1** | **Correlation chain.** Inspect a trace spanning project, gate, task, agent, model, tool, artifact, run and claim | Complete chain; no secrets and no full sensitive prompts present | Trace sample |
| 16 | E3 | Independent review of the release dossier's provenance section | The reviewer can verify every artifact's origin without trusting this repository | `ReviewRecord` |

Cases 10 to 14 are specified as injections rather than as properties for one
reason: split brain is invisible in a healthy system and obvious only in a
post-mortem. A silent divergence is the failure, and nothing short of causing one
demonstrates that it would be caught.

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                       # the target revision every result binds to
python3 scripts/progress.py show WP-159   # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-159 --gate Platform \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-159/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-159
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_159_supply_chain_and_cross_plane_integrity.acceptance.md) reaches the decision — issuance is not acceptance.

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
