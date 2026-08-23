# WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall

## Package card

| Field | Value |
|---|---|
| Work package | `WP-058` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Content Security Lead |
| Independent verifier | Red Team / Knowledge Lead |
| Hard dependencies | WP-014, WP-017, WP-026, WP-049, WP-050, WP-051, WP-054, WP-056, WP-057 |
| Related gates | G3,G5 |
| Related controls | CTL-SEC-01, CTL-LIT-01 |
| Related acceptance scenarios | ACC-05 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-058_content_quarantine_firewall.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-058_content_quarantine_firewall.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Web, PDF, repository and tool output passes through quarantine, malware/MIME/licence/size scanning, isolated parsing, instruction tagging and read-only extraction — with no active content ever executed.


## Analysis
### What this package actually decides

That untrusted content is never executed and never instructs. This is ADR-003's
data plane implemented as a pipeline: quarantine, scan, parse in isolation,
separate the channels, tag the instruction-shaped parts, and hand back **read-only
text with provenance**.

### `ACC-05` is the scenario, and it is already reachable in the running system

The Bridge's MCP server says so in its own docstring:

> `get_source` returns the Zotero abstract as raw text. An abstract originating in
> a malicious PDF can carry injected instructions — this is scenario **ACC-05**
> reaching the MCP surface. The blast radius is small while every tool is
> read-only, and it grows the moment Hermes has a tool that writes. The cheap
> mitigation is to wrap external content in an explicit boundary marker such as
> `<untrusted-source-content>`; **it is not implemented yet.**

That is an accurate description of a live gap, in a system with five read-only
tools. This package is what closes it before the tool set grows.

### Channel separation is the structural control (T04)

Text, metadata, links, scripts and instruction-shaped segments are **different
channels**. A parser that returns one blob has already merged the thing the model
should read with the thing an attacker wrote — and no downstream prompt discipline
reliably unmerges them.

### Tagging is a mitigation; the boundary is the scope (T05)

Marking instruction-like segments as untrusted quoted data reduces the chance a
model acts on them. It does **not** make it safe, and ADR-003 says why: control
flow comes only from trusted intent. The actual guarantee is that the agent's
`TaskContract` fixes its authority and nothing it reads can widen it (WP-046,
WP-049).

### The parser runs in a cell for a specific reason (T03)

PDF and HTML parsers are large C libraries with a long CVE history, fed by
attacker-controlled bytes. Running them inside WP-054's ephemeral sandbox means a
parser exploit lands somewhere that is destroyed on exit.

### T0/T1 read-only extraction profile (T06)

The extraction step has no reason to write anything or reach anything. Giving it
the narrowest possible `ToolEffect` means a compromised extractor has nothing to
do with its compromise.

### Baseline v1.3.0 — four zones, a capability gate, and a benchmark firewall

The isolation story gains a fourth zone and two new attack surfaces.

**Four zones, not three.** Producer, evaluator, reproducer and independent
grader, separated in secrets, cache and workspace. The leakage paths that matter
are the quiet ones — a shared cache, an inherited credential, a warm container
layer — and none of them looks like a boundary violation in a log. Each is tested
explicitly rather than inferred from the zone configuration (ACC-113).

**Security is a capability, not a prompt.** *Prompt says safe* is not security;
*the capability is unavailable unless policy grants it* is. External content —
PDF, web page, tool result, reviewer comment — is quarantined into a data object,
and the agent's tool intent passes a policy gate before any credential is
injected (ACC-117).

**A benchmark firewall.** An evaluation run freezes its dataset manifest, network
mode, allowed domains, known identifiers and evaluator isolation before it
starts, and audits every retrieval. Gold answers, private rubrics, hidden tests
and grader prompts are unreachable from the agent environment (ACC-118).

The attack suite gains ASB and WASP as external regressions, alongside internal
fixtures for source-PDF injection, malicious citation text, tool-result
injection, memory poisoning and credential exfiltration.

## Out of scope

- The internal implementation of any dependent package
- Production cutover and final operational approval

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

9, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md) | `ArtifactRecord schema` · `DatasetManifest schema` · `Environment reference schema` · `Immutability lifecycle` |
| [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md) | `Literature schema bundle` · `Status lifecycle` · `Sample manifests` · `Zotero binding contract` |
| [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md) | `Object storage IaC` · `Object address service` · `Retention matrix` · `Integrity scan job` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md) | `Versioned connectors` · `Connector permission profiles` · `Connector contract tests` · `Compensation/reconciliation playbooks` |
| [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md) | `Trust zone diagram/data flows` · `Network IaC` · `Boundary policy` · `Threat-test suite` |
| [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md) | `Sandbox profiles` · `Execution Cell controller` · `SandboxAttestation` · `Capture/destroy workflow` |
| [WP-056 — Policy Decision Point and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md) | `Policy decision point` · `PolicyDecision interface conformance suite` · `Policy bundle v1` · `Policy test suite` |
| [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md) | `Egress proxy` · `Allowlist registry` · `DLP pipeline` · `Egress audit/alerts` |

### Full prerequisite closure

**46 of 160 packages (29%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

| Level | Packages |
|---:|---|
| 1 | `WP-001` |
| 2 | `WP-002` |
| 3 | `WP-003` · `WP-005` · `WP-006` |
| 4 | `WP-004` · `WP-007` |
| 5 | `WP-008` |
| 6 | `WP-009` |
| 7 | `WP-010` |
| 8 | `WP-011` |
| 9 | `WP-012` · `WP-013` · `WP-016` |
| 10 | `WP-014` |
| 11 | `WP-015` · `WP-017` |
| 12 | `WP-018` |
| 13 | `WP-019` |
| 14 | `WP-020` |
| 15 | `WP-021` · `WP-022` |
| 16 | `WP-023` · `WP-025` · `WP-026` · `WP-051` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` |
| 25 | `WP-056` |
| 26 | `WP-057` |

### What acceptance of this package releases

- **Directly unblocked:** 8 — `WP-060` · `WP-062` · `WP-063` · `WP-068` · `WP-076` · `WP-078` · `WP-103` · `WP-136`
- **Transitively reachable:** **72 of 160 packages (45%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **27** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Content Security Lead |
| Independent verifier | Red Team / Knowledge Lead |
| Gates touched | `G3` · `G5` |
| Controls | `CTL-SEC-01` · `CTL-LIT-01` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-05 — Prompt-Injection PDF](../12_ACCEPTANCE_SCENARIOS/ACC-05_prompt_injection_pdf.md) | Critical | The content stays untrusted quoted data; extraction continues read-only, no tool, secret or write call occurs, and security event and scan evidence is produced. |
| [ACC-44 — Inbound Content Attempts to Act as an Instruction](../12_ACCEPTANCE_SCENARIOS/ACC-44_inbound_message_is_not_an_instruction.md) | Critical | No decision record is created, no tool is invoked from the content, the material is labelled untrusted in context, and an authenticated structured `CommandIntent` through the proper path still succeeds. |
| [ACC-098 — Memory Poisoning Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-098_memory_poisoning_attempt.md) | Critical | The content is stored in a typed store whose authority field forbids claim support. It cannot be retrieved as evidence, cannot support a claim, and a lesson derived from a failed approach is not an accepted fact. |
| [ACC-117 — Prompt Injection Meets a Capability Gate](../12_ACCEPTANCE_SCENARIOS/ACC-117_prompt_injection_capability_gate.md) | Critical | The action is unavailable because policy did not grant the capability, not because a detector recognised the text. Content crosses the boundary; authority does not. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-014 — Artifact, Dataset and Immutable Manifest Schemas](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry and Literature Contract Schemas](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store and WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — Initial Tool Connector Package](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md), [WP-054 — gVisor Sandbox and Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-057 — Default-Deny Egress Proxy, DLP and Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `ArtifactRecord schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `DatasetManifest schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Environment reference schema` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Immutability lifecycle` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Ordered parent lineage` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Digest normalisation and migration` | `WP-014` | `python3 scripts/progress.py show WP-014` |
| `Literature schema bundle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Status lifecycle` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Sample manifests` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Zotero binding contract` | `WP-017` | `python3 scripts/progress.py show WP-017` |
| `Object storage IaC` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Object address service` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Retention matrix` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Integrity scan job` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Restore procedure` | `WP-026` | `python3 scripts/progress.py show WP-026` |
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Versioned connectors` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector permission profiles` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Connector contract tests` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Compensation/reconciliation playbooks` | `WP-050` | `python3 scripts/progress.py show WP-050` |
| `Trust zone diagram/data flows` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Network IaC` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Boundary policy` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Threat-test suite` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Sandbox profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Execution Cell controller` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `SandboxAttestation` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Capture/destroy workflow` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Red-team tests` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Four-zone isolation profiles` | `WP-054` | `python3 scripts/progress.py show WP-054` |
| `Policy decision point` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `PolicyDecision interface conformance suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Egress proxy` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Allowlist registry` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `DLP pipeline` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Egress audit/alerts` | `WP-057` | `python3 scripts/progress.py show WP-057` |
| `Exception runbook` | `WP-057` | `python3 scripts/progress.py show WP-057` |

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `L`** — large — split into sub-packages if the estimate exceeds the wave.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Content Security Lead** carries the acceptance decision; **Red Team / Knowledge Lead** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation acquisition and assimilation

<!-- generated:implementation-sources — produced by scripts/expand_acquisition.py; do not edit inside this block -->

**What is already solved elsewhere, and on what terms.** Before the first task starts, an implementer has to know which parts of this package are called at runtime, which are copied and refactored, which are reimplemented from a specification, and which have no upstream at all. Those decisions are recorded in [`provenance/upstreams.json`](../../../provenance/upstreams.json) — mechanisms assimilated into this repository's own code — and in [`provenance/components.json`](../../../provenance/components.json) — components adopted at runtime. This block is derived from both, so a decision and the place it is used cannot drift apart.

### Acquisition map

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| `ASM-047` — Agent Security Bench — attack and defence surface for tool-using agents | `BENCHMARK` | a measurement of this system — nothing enters it | the contract this is held behind | none |
| `CMP-034` — CaMeL | `PATTERN` | the idea only — no code and nothing called at runtime | The trusted-control / untrusted-data architecture and the capability gate that enforces it. | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-047` | Measures the security boundary. Never part of the running system, and a passing score is not a security property. | Any runtime dependency. |
| `CMP-034` | Control flow comes from trusted intent. Untrusted content may supply values; it can never create actions or expand permissions. Content crosses the boundary, authority does not. | Prompt-layer injection detection as a security boundary — a detector is defence in depth, not a boundary. |

### Where a plain row would mislead

- **`ASM-047`** — Ten scenarios, over 400 tools, 27 attack and defence methods across 13 model backbones, with a highest average attack success rate of 84.3% and defences reported as of limited effectiveness. That last finding is the architectural argument for ADR-003 and the capability gate: **if defences at the prompt layer are weak, the boundary has to be that the capability is unavailable** — ACC-117.
- **`CMP-034`** — WP-136 changes character: from *prompt-injection detection* to **trusted control / untrusted data architecture**.

### Unresolved before implementation

**None.** Every obligation the modes above create has been met.

**Acquisition readiness — resolved.** All 2 registered sources have met the obligations their modes create.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-058-T01 | Establish the quarantine bucket and the ingest gateway | Implementation owner | Commit / configuration / record reference |
| WP-058-T02 | Apply MIME, malware, archive-bomb, size and licence scanning | Implementation owner | Commit / configuration / record reference |
| WP-058-T03 | Run the PDF/HTML/OCR parser inside an isolated cell | Implementation owner | Commit / configuration / record reference |
| WP-058-T04 | Separate the text, metadata, link, script and instruction channels | Implementation owner | Commit / configuration / record reference |
| WP-058-T05 | Tag instruction-like segments as untrusted quoted data | Implementation owner | Commit / configuration / record reference |
| WP-058-T06 | Restrict the extraction tool profile to T0/T1 read-only | Implementation owner | Commit / configuration / record reference |
| WP-058-T07 | Add security events and quarantine disposition | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Content firewall`
- `Parser workers`
- `ContentSafetyRecord`
- `Injection detector`
- `Quarantine UI/API`
- `Capability gate for untrusted content`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-058_content_quarantine_firewall.tests.md`](WP-058_content_quarantine_firewall.tests.md).

- A PDF carrying a tool-command injection
- Malware and archive bombs
- Parser crash containment
- Denial of write and tool access from extraction
- Curator disposition of a false positive
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-058_content_quarantine_firewall.acceptance.md`](WP-058_content_quarantine_firewall.acceptance.md), together with what this package still cannot establish.

- [ ] External content can never become a workflow command.
- [ ] Extraction receives no secret, no write access and no unrestricted network.
- [ ] Every span carries the source representation hash and the parser version.
- [ ] All mandatory tests passed **on the same target revision**.
- [ ] No open Critical or High findings; no non-waivable blocker remains.
- [ ] The independent verifier has accepted the evidence package.
- [ ] Rollback/compensation behaviour has been exercised and audited.
- [ ] The related dashboard, alert, audit query or integrity query has produced working evidence.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- If a contract or canonical ownership question is unresolved, implementation **stops** and the question escalates to the Architecture Board.
- Identity, data routing, artifact integrity, independence and critical evidence problems **cannot** be passed by waiver.
- If a temporary manual control is required, its owner, scope, expiry, compensating control and removal package are recorded.
- A "package complete" statement is **not** acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

### Workstream-specific hazards

- A control not exercised by a negative test is an assumption.
- Default-allow egress anywhere in the chain nullifies every other isolation control.
- Sandbox escape is tested by attempting it, not by reading the configuration.

## Rollback / compensation

Suspicious content stays in quarantine; the parser or detector is rolled back and the content is reprocessed as a new version.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
