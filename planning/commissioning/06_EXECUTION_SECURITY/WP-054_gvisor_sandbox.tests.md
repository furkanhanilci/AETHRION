# WP-054 — gVisor Sandbox and Execution Cell Lifecycle — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-054` |
| Work package | [`WP-054` — gVisor Sandbox and Execution Cell Lifecycle](WP-054_gvisor_sandbox.md) |
| Companion | [acceptance criteria](WP-054_gvisor_sandbox.acceptance.md) |
| Workstream | `06_EXECUTION_SECURITY` |
| Approval authority | **Red Team / SRE** — the independent verifier |
| Accountable owner | Execution Security Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-054` |

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
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3 · E4.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | Execution Security Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | Execution Security Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Red Team / SRE | At completion |
| `WP-006` accepted output | ExecutionProfile and Route Policy | Platform Security Lead | Before the first test case runs |
| `WP-014` accepted output | Artifact, Dataset and Immutable Manifest Schemas | Data Platform Lead | Before the first test case runs |
| `WP-027` accepted output | Git, OCI Registry and Build Provenance Foundation | Supply Chain Security Lead | Before the first test case runs |
| `WP-049` accepted output | Tool Registry and Tool Broker Core | Tool Platform Lead | Before the first test case runs |
| `WP-052` accepted output | Kubernetes Cluster and Node Pool Baseline | Platform Infrastructure Lead | Before the first test case runs |
| `WP-053` accepted output | Kueue Queue, Quota and Priority Policy | Compute Platform Lead | Before the first test case runs |

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
| C01 | `Sandbox profiles` | Mandatory deliverable | *(name the test case)* |
| C02 | `Execution Cell controller` | Mandatory deliverable | *(name the test case)* |
| C03 | `SandboxAttestation` | Mandatory deliverable | *(name the test case)* |
| C04 | `Capture/destroy workflow` | Mandatory deliverable | *(name the test case)* |
| C05 | `Red-team tests` | Mandatory deliverable | *(name the test case)* |
| C06 | `Four-zone isolation profiles` | Mandatory deliverable | *(name the test case)* |
| C07 | Establish the RuntimeClass/gVisor and seccomp/capability baseline | WP-054-T01 | *(name the test case)* |
| C08 | Apply the ephemeral workspace, mount and path policy | WP-054-T02 | *(name the test case)* |
| C09 | Bind the OCI signature and SBOM attestation gate | WP-054-T03 | *(name the test case)* |
| C10 | Add CPU, memory, wall-clock and process limits | WP-054-T04 | *(name the test case)* |
| C11 | Write artifact capture, hashing, upload and teardown | WP-054-T05 | *(name the test case)* |
| C12 | Establish forensic snapshotting and escape detection | WP-054-T06 | *(name the test case)* |
| C13 | Sandbox Escape Attempt | [ACC-15](../12_ACCEPTANCE_SCENARIOS/ACC-15_sandbox_escape.md) — Critical | *(name the test case)* |
| C14 | Unsigned or Mutable Image | [ACC-17](../12_ACCEPTANCE_SCENARIOS/ACC-17_unsigned_image.md) — Critical | *(name the test case)* |

**14 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** RuntimeClass | E0 | Inspect an execution pod | Runs under the gVisor RuntimeClass with the declared seccomp profile | Pod spec |
| **TC-02** Capability drop | **E2** | Request an elevated capability | Refused | Refusal transcript |
| **TC-03** **Attestation before execution** | **E2** | Run an unsigned image | **Refused before any process starts** | Refusal transcript |
| **TC-04** Missing SBOM | **E2** | Run a signed image with no SBOM | Refused | Refusal transcript |
| **TC-05** Tag reference | **E2** | Reference the image by mutable tag | Refused; digest only | Refusal transcript |
| **TC-06** Ephemeral workspace | **E1** | Run two tasks in sequence | The second sees **nothing** from the first | Workspace inspection |
| **TC-07** Scope mount | **E2** | Read a path outside the declared mount scope | Refused | Refusal transcript |
| **TC-08** Write outside scope | **E2** | Write outside the workspace | Refused | Refusal transcript |
| **TC-09** CPU/memory limit | **E1** | Exceed each limit in turn | Terminated per policy, not throttled indefinitely | Two termination records |
| **TC-10** Wall-clock limit | **E1** | Exceed the wall-clock limit | Terminated; the run is marked, not silently truncated | Termination record |
| **TC-11** Process limit | **E2** | Fork beyond the process limit | Refused | Refusal transcript |
| **TC-12** Network isolation | **E2** | Reach any host directly | Denied; only the egress proxy path exists (WP-057) | Denial record |
| **TC-13** Artifact capture | **E1** | Produce an artifact | Hashed and uploaded; the hash is recorded before teardown | Capture record |
| **TC-14** Artifact quarantine | **E1** | Inspect where the artifact lands | The quarantine area, not the canonical store (WP-026) | Storage inspection |
| **TC-15** **Destruction on success** | **E1** | Complete a task | The cell is destroyed; no workspace remains | Teardown record |
| **TC-16** **Destruction on failure** | **E2** | Fail a task, time it out, and error its capture step | Destroyed in **all three** cases | Three teardown records |
| **TC-17** Escape detection | **E2** | Trigger the declared escape indicator | Detected, alerted, and a **forensic snapshot taken before teardown** | Snapshot · alert |
| **TC-18** Snapshot integrity | **E1** | Inspect a forensic snapshot | Sufficient to investigate: process list, filesystem diff, network attempts | Snapshot contents |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-054 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-054 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-054/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-054
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-054_gvisor_sandbox.acceptance.md) reaches the decision — issuance is not acceptance.

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
