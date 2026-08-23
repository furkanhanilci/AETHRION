---
title: "WP-057 — Default-Deny Egress Proxy, DLP and Allowlist — Test Procedures"
aliases:
  - "WP-057 tests"
cssclasses:
  - aethrion-test-procedure
type: test-procedure
category: commissioning
status: NOT_STARTED
source: "planning/commissioning/06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.tests.md"
generated: false
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/06-execution-security
  - aethrion/wave/w2
  - aethrion/effort/l
  - aethrion/gate/g3
  - aethrion/gate/g5
  - aethrion/gate/platform
  - aethrion/state/not-started
  - aethrion/test-procedure
  - aethrion/authoring/authored
---

# WP-057 — Default-Deny Egress Proxy, DLP and Allowlist — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-057` |
| Work package | [`WP-057` — Default-Deny Egress Proxy, DLP and Allowlist](wp_057_egress_proxy_dlp.md) |
| Companion | [acceptance criteria](wp_057_egress_proxy_dlp.acceptance.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **Red Team / Privacy Owner** — the independent verifier |
| Accountable owner | Network Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-057` |

<!-- /generated:identity -->

## Test strategy extract — §8.2.5

<!-- generated:strategy — produced by scripts/make_package_companions.py; do not edit inside this block -->

The evidence layers this package must satisfy, derived from the gates it touches and the scenarios bound to it. `00_PROGRAM/06` fixes the order: **cheap layers run first**, because an independent reviewer's attention is the expensive resource and should not be spent on what a mechanical check would have caught.

| Layer | Question it answers | Required here | Why |
|---|---|:--:|---|
| **E0** Structural | Does the file, schema or reference exist? | **yes** | never optional — the artifact must exist and behave |
| **E1** Mechanical | Is the behaviour correct under a deterministic test? | **yes** | never optional — the artifact must exist and behave |
| **E2** Security | Is the forbidden path actually blocked? | **yes** | never optional — a control that has not been observed refusing is prose |
| **E3** Independent review | Did an actor outside the producer examine the semantics? | **yes** | bound to 5 acceptance scenario(s) · effort class L |
| **E4** Reproduction | Does the same package run again in a clean environment? | **yes** | touches G5 |
| **E5** Operations | Are failure, restore and observability correct? | **yes** | touches Platform |

**Applicable layers: E0 · E1 · E2 · E3 · E4 · E5.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Network Security Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Network Security Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Red Team / Privacy Owner | At completion |
| `WP-006` accepted output | ExecutionProfile and Route Policy | Platform Security Lead | Before the first test case runs |
| `WP-021` accepted output | Development, Staging and Production Environment Baseline | Platform Lead | Before the first test case runs |
| `WP-049` accepted output | Tool Registry and Tool Broker Core | Tool Platform Lead | Before the first test case runs |
| `WP-051` accepted output | Four Trust Zones and Network Segmentation | Security Architecture Lead | Before the first test case runs |
| `WP-055` accepted output | SPIFFE/SPIRE Workload Identity and Vault | Identity Platform Lead | Before the first test case runs |
| `WP-056` accepted output | Policy Decision Point and Bundle Distribution | Policy Platform Lead | Before the first test case runs |

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
| C01 | `Egress proxy` | Mandatory deliverable | *(name the test case)* |
| C02 | `Allowlist registry` | Mandatory deliverable | *(name the test case)* |
| C03 | `DLP pipeline` | Mandatory deliverable | *(name the test case)* |
| C04 | `Egress audit/alerts` | Mandatory deliverable | *(name the test case)* |
| C05 | `Exception runbook` | Mandatory deliverable | *(name the test case)* |
| C06 | Establish the explicit proxy, DNS policy and TLS strategy | WP-057-T01 | *(name the test case)* |
| C07 | Bind the tool/provider domain registry and the purpose allowlist | WP-057-T02 | *(name the test case)* |
| C08 | Add request/response size, MIME and method constraints | WP-057-T03 | *(name the test case)* |
| C09 | Apply the secret, PII and D3–D4 DLP detectors | WP-057-T04 | *(name the test case)* |
| C10 | Establish canary secrets and anomalous-volume alerting | WP-057-T05 | *(name the test case)* |
| C11 | Write the emergency deny/revoke and exception flow | WP-057-T06 | *(name the test case)* |
| C12 | Egress Exfiltration Attempt | [ACC-16](../12_ACCEPTANCE_SCENARIOS/acc_16_egress_exfiltration.md) — Critical | *(name the test case)* |
| C13 | D3 Data to a Public Provider | [ACC-18](../12_ACCEPTANCE_SCENARIOS/acc_18_d3_public_route.md) — Critical | *(name the test case)* |
| C14 | Secret in Prompt or Trace | [ACC-32](../12_ACCEPTANCE_SCENARIOS/acc_32_secret_in_trace.md) — Critical | *(name the test case)* |
| C15 | Hidden Evaluation Data Access Attempt | [ACC-55](../12_ACCEPTANCE_SCENARIOS/acc_55_hidden_evaluation_data_access.md) — Critical | *(name the test case)* |
| C16 | Search-Time Benchmark Contamination | [ACC-118](../12_ACCEPTANCE_SCENARIOS/acc_118_benchmark_search_time_contamination.md) — Critical | *(name the test case)* |

**16 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Explicit proxy | **E2** | Bypass the proxy from an execution pod | Denied at the network layer (WP-051) | Denial record |
| **TC-02** DNS policy | **E2** | Resolve an arbitrary name | Refused | Denial record |
| **TC-03** Domain allowlist | **E2** | Reach an unlisted domain | Denied | Denial record |
| **TC-04** Method constraint | **E2** | `POST` to a domain allowlisted for `GET` | **Denied** — an allowlist on domain alone permits exfiltration to a permitted host | Denial record |
| **TC-05** Purpose constraint | **E2** | Call an allowlisted domain for an undeclared purpose | Denied | Denial record |
| **TC-06** Data-class ceiling | **E2** | Send D3 content to a destination with a lower ceiling | Denied, naming the class and the ceiling | Denial record |
| **TC-07** Size and MIME | **E2** | Exceed the declared response size; return an unexpected MIME | Each refused | Two refusals |
| **TC-08** Secret detector | **E2** | Send a secret-shaped string within an allowed request | Blocked and alerted | Alert record |
| **TC-09** PII detector | **E2** | Send personal data within an allowed request | Blocked and alerted | Alert record |
| **TC-10** **Canary secret** | **E2** | Plant a canary and cause it to be sent | **Detected and blocked.** Proves the detector can fire | Detection transcript |
| **TC-11** Canary silence | **E2** | Run the detector suite with the canary removed | The suite **fails** rather than reporting clean | Failure transcript |
| **TC-12** Anomalous volume | **E2** | Send a large volume to an **allowed** destination over time | Alert fires against the baseline | Alert record |
| **TC-13** Full audit | **E1** | Inspect the log after a permitted request | Destination, method, purpose, class, size, identity and outcome all recorded | Log sample |
| **TC-14** **Emergency deny** | **E1** | Exercise the emergency deny path | All egress stops within the declared time; the action is audited | Deny transcript · timing |
| **TC-15** Emergency restore | **E1** | Restore from emergency deny | Service resumes; the incident record is complete | Restore transcript |
| **TC-16** Exception flow | **E2** | Request an egress exception with no approver, then with an expired one | Both refused (WP-009) | Two refusals |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-057 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-057 --gate Platform \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-057/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-057
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](wp_057_egress_proxy_dlp.acceptance.md) reaches the decision — issuance is not acceptance.

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
