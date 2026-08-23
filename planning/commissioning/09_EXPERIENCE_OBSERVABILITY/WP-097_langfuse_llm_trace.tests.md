# WP-097 — Langfuse Model/Agent Tracing and Prompt Governance — Test Procedures

## Document identity

<!-- generated:identity — produced by scripts/make_package_companions.py; do not edit inside this block -->

| Field | Value |
|---|---|
| Unique identifier | `TP-WP-097` |
| Work package | [`WP-097` — Langfuse Model/Agent Tracing and Prompt Governance](WP-097_langfuse_llm_trace.md) |
| Companion | [acceptance criteria](WP-097_langfuse_llm_trace.acceptance.md) |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| Approval authority | **Privacy/Security / Eval Office** — the independent verifier |
| Accountable owner | AI Observability Lead |
| Status at baseline | `NOT_STARTED` |
| Change history | `git log --follow` on this file; the plan seal covers its bytes |
| Document standard | Structured on the information items of ISO/IEC/IEEE 29119-3:2021 §5.2, §7.4 and §8 |
| Live state | `python3 scripts/progress.py show WP-097` |

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
| **E5** Operations | Are failure, restore and observability correct? | no | no platform or day-2 gate |

**Applicable layers: E0 · E1 · E2 · E3.** A layer marked *no* is not a waiver: it means this package cannot produce that evidence, and a claim that needs it must be earned by a package that can.

<!-- /generated:strategy -->

## Test environment requirements — §8.6

<!-- generated:environment — produced by scripts/make_package_companions.py; do not edit inside this block -->

ISO/IEC/IEEE 29119-3 §8.6 requires each environment item to name a description, a responsibility and the period it is needed for. An item without a named responsibility is an item nobody will have provisioned on the day the tests run.

| Item | Description | Responsibility | Period needed |
|---|---|---|---|
| Target revision | The single commit every result is bound to | AI Observability Lead | For the whole test run; results from two revisions are not evidence |
| Environment manifest | Hardware, image digest, SBOM — captured, not described | AI Observability Lead | Captured at the start of the run |
| Isolated workspace | A worktree or container separate from the producer's | Implementation owner | For the whole run |
| Evidence sink | Somewhere `EvidenceManifest` can be issued and verified | Privacy/Security / Eval Office | At completion |
| `WP-006` accepted output | ExecutionProfile and Route Policy | Platform Security Lead | Before the first test case runs |
| `WP-013` accepted output | Project, Task, Role and Skill Contract Schemas | Control Plane Lead | Before the first test case runs |
| `WP-020` accepted output | Schema Registry, Compatibility and Contract SDK | Platform Architecture Lead | Before the first test case runs |
| `WP-025` accepted output | PostgreSQL HA and Registry Data Foundation | Database Platform Lead | Before the first test case runs |
| `WP-026` accepted output | Content-Addressed Object Store and WORM | Data Platform Lead | Before the first test case runs |
| `WP-041` accepted output | LiteLLM Model Gateway Foundation | Model Platform Lead | Before the first test case runs |
| `WP-046` accepted output | LangGraph Bounded Cognition Runtime | Agent Platform Lead | Before the first test case runs |
| `WP-047` accepted output | Role and Skill Registries, and the Task Compiler | Agent Platform Lead | Before the first test case runs |
| `WP-055` accepted output | SPIFFE/SPIRE Workload Identity and Vault | Identity Platform Lead | Before the first test case runs |
| `WP-056` accepted output | Policy Decision Point and Bundle Distribution | Policy Platform Lead | Before the first test case runs |
| `WP-057` accepted output | Default-Deny Egress Proxy, DLP and Allowlist | Network Security Lead | Before the first test case runs |
| `WP-096` accepted output | OpenTelemetry End-to-End Correlation Spine | Observability Lead | Before the first test case runs |

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
| C01 | `Langfuse platform` | Mandatory deliverable | *(name the test case)* |
| C02 | `Prompt registry` | Mandatory deliverable | *(name the test case)* |
| C03 | `Trace/redaction policy` | Mandatory deliverable | *(name the test case)* |
| C04 | `Retention/export runbook` | Mandatory deliverable | *(name the test case)* |
| C05 | `Trace quality dashboard` | Mandatory deliverable | *(name the test case)* |
| C06 | Deploy Langfuse with project structure, RBAC and data routing | WP-097-T01 | *(name the test case)* |
| C07 | Apply the trace hierarchy and the AIRL correlation mapping | WP-097-T02 | *(name the test case)* |
| C08 | Bind the prompt and template version registry | WP-097-T03 | *(name the test case)* |
| C09 | Add input, output and tool-schema redaction and minimisation | WP-097-T04 | *(name the test case)* |
| C10 | Apply the no-chain-of-thought and rationale-summary policy | WP-097-T05 | *(name the test case)* |
| C11 | Establish evaluation feedback, cost, export, retention and backup | WP-097-T06 | *(name the test case)* |
| C12 | Secret in Prompt or Trace | [ACC-32](../12_ACCEPTANCE_SCENARIOS/ACC-32_secret_in_trace.md) — Critical | *(name the test case)* |

**12 coverage items.** Every one must appear in the *Covered by* column of at least one test case below before this package can reach `TECH_COMPLETE`.

<!-- /generated:coverage -->

## Test cases

| Case | Layer | Steps | Expected result | Evidence |
|---|---|---|---|---|
| **TC-01** Deployment | E0 | Inspect projects, RBAC and data routing | Project structure and role separation present | Configuration |
| **TC-02** Correlation mapping | **E1** | Inspect a trace | Maps to the AIRL project, workflow, run and task (WP-096) | Trace |
| **TC-03** Trace hierarchy | **E1** | Inspect an agent task | Task → node → model call → tool call nesting is correct | Trace |
| **TC-04** **Prompt version** | **E1** | Inspect a model call | Names the registered prompt and template **version** | Trace |
| **TC-05** Unregistered prompt | **E2** | Call with a prompt not in the registry | Refused, or flagged as unpinnable | Refusal · flag |
| **TC-06** **No chain-of-thought requested** | **E2** | Inspect every model request | **None requests private reasoning** | Request audit |
| **TC-07** **No chain-of-thought stored** | **E2** | Search the trace store for reasoning content | **None** | Store audit |
| **TC-08** Rationale summary | **E1** | Inspect a completed call | A stated rationale summary is present and reviewable | Trace |
| **TC-09** **Redaction at ingestion** | **E2** | Send a prompt containing a secret and personal data | Neither **lands** in the store — redacted before write, not on read | Store inspection |
| **TC-10** Redaction on read only | **E2** | Configure read-time redaction instead | Refused — the unredacted value would still be stored | Refusal transcript |
| **TC-11** Data-class routing | **E2** | Trace a D3 task | Routed to D3 retention; not in the general project | Routing record |
| **TC-12** Tool schema redaction | **E2** | Trace a tool call with sensitive arguments | Arguments redacted per the schema's declaration | Trace |
| **TC-13** Cost and tokens | **E1** | Inspect a call | Token counts, latency and cost recorded and correlated (WP-100) | Trace |
| **TC-14** **Golden-set isolation** | **E2** | From the trace store identity, read the evaluation golden set | **Denied** (`PR-15`) | Denial record |
| **TC-15** Retention | **E2** | Age a trace past its data-class retention | Removed without human action | Expiry record |
| **TC-16** Export and backup | **E1** | Export and restore | Traces round-trip; correlation survives | Export diff |

## How to execute

### Before the first case

```bash
cd /home/otonom/Desktop/FH/AETHRION
git rev-parse HEAD                     # the target revision every result binds to
python3 scripts/progress.py show WP-097 # dependencies and their states
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
python3 scripts/evidence_manifest.py issue --package WP-097 --gate G5 \
    --subject <each artifact the run produced> \
    --check "<what was verified, in one sentence>"
python3 scripts/evidence_manifest.py verify \
    --manifest delivery/WP-097/evidence.dsse.json --tamper-demo
```

The manifest is issued **last**, because it covers digests: anything that changes
afterwards fails verification, which is the control working rather than a defect.

### Handing over

```bash
python3 scripts/progress.py tech-complete WP-097
```

`TECH_COMPLETE` is where the producer stops. The verifier named on the
[acceptance criteria](WP-097_langfuse_llm_trace.acceptance.md) reaches the decision — issuance is not acceptance.

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
