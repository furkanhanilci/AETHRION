# WP-057 — Default-Deny Egress Proxy, DLP and Allowlist

## Package card

| Field | Value |
|---|---|
| Work package | `WP-057` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Network Security Lead |
| Independent verifier | Red Team / Privacy Owner |
| Hard dependencies | WP-006, WP-021, WP-049, WP-051, WP-055, WP-056 |
| Related gates | G3,G5,Platform |
| Related controls | CTL-SEC-02, CTL-OBS-02 |
| Related acceptance scenarios | ACC-16, ACC-18, ACC-32 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-057_egress_proxy_dlp.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-057_egress_proxy_dlp.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

All outbound traffic from execution and services passes through a domain/IP/method/purpose/data-class allowlist, secret and PII detectors, and full audit.


## Analysis
### What this package actually decides

What may leave. Every other control in the security workstream limits what can be
reached or what can be run; this one limits what can go **out**, and it is the
last boundary before data is gone.

### The allowlist has five dimensions, not one (T02, T03)

Domain, IP, method, purpose, data class. A proxy that allowlists domains alone
permits a `POST` of a D3 dataset to an approved documentation host — which is an
exfiltration through a permitted destination, and the most likely shape of a real
incident.

### DLP detectors are defence in depth, never the boundary (T04)

ADR-003 is explicit and the rule generalises: a detector is defence in depth,
never the boundary. The **boundary** is the data class attached to the request and
the ceiling attached to the destination. Detectors catch the case where the class
was wrong — they do not replace it.

A package that relies on regexes to stop exfiltration has inverted its own design.

### Canary secrets are what make the control testable (T05)

A secret that exists only to be detected if it ever leaves. Without one, "no
secret has leaked" is indistinguishable from "the detector does not work" — and
`monitor_sources.py` already applies this discipline in this repository: it
carries a known-retracted positive control and **fails if the control stays
silent**.

The same rule belongs here.

### Anomalous volume is the signal for the case the allowlist permits (T05)

Slow exfiltration through an approved destination defeats every categorical
control. Volume against a baseline is the only thing that sees it.

### The emergency deny path needs to be exercised, not documented (T06)

An emergency control first used during an emergency is a control being tested
during an incident.

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

6, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md) | `Trust zone diagram/data flows` · `Network IaC` · `Boundary policy` · `Threat-test suite` |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |
| [WP-056 — Policy Decision Point and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md) | `Policy decision point` · `PolicyDecision interface conformance suite` · `Policy bundle v1` · `Policy test suite` |

### Full prerequisite closure

**42 of 160 packages (26%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-055` |
| 25 | `WP-056` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-058` · `WP-060` · `WP-096` · `WP-097` · `WP-158`
- **Transitively reachable:** **82 of 160 packages (51%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **26** of 55 |
| On the documented critical path | no |
| Effort class | **L** |
| Accountable owner | Network Security Lead |
| Independent verifier | Red Team / Privacy Owner |
| Gates touched | `G3` · `G5` · `Platform` |
| Controls | `CTL-SEC-02` · `CTL-OBS-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-16 — Egress Exfiltration Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-16_egress_exfiltration.md) | Critical | The traffic is denied, the canary never leaves, the credential lease is revoked and a security incident and audit record are created. |
| [ACC-18 — D3 Data to a Public Provider](../12_ACCEPTANCE_SCENARIOS/ACC-18_d3_public_route.md) | Critical | No public provider call is made; a secure or local eligible route is chosen if one exists, otherwise the task is `BLOCKED`, and an audit record is written. |
| [ACC-32 — Secret in Prompt or Trace](../12_ACCEPTANCE_SCENARIOS/ACC-32_secret_in_trace.md) | Critical | The secret never appears in raw telemetry, events or the UI; redaction or quarantine occurs, a security event is raised and the credential is revoked. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md), [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-051 — Four Trust Zones and Network Segmentation](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md), [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform and Bundle Distribution](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md)
- A named owner, a named implementer, and a verifier **independent of the producer** are assigned.
- Affected canonical records, interfaces and ADRs have been linked during refinement.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.
- An O/M/P person-day estimate is recorded and real capacity is reserved against it.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Producer and evaluator zone profiles` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `MutationPolicy` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Environment topology` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Account/network IaC` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Access baseline` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Environment promotion policy` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Trust zone diagram/data flows` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Network IaC` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Boundary policy` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `Threat-test suite` | `WP-051` | `python3 scripts/progress.py show WP-051` |
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Policy decision point` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `PolicyDecision interface conformance suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy bundle v1` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Policy test suite` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Bundle promotion pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |
| `Decision log pipeline` | `WP-056` | `python3 scripts/progress.py show WP-056` |

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
- **Network Security Lead** carries the acceptance decision; **Red Team / Privacy Owner** must verify independently of whoever implements.
- One owner holds at most two `IN_PROGRESS` packages. At least 25% of assurance capacity stays reserved for correction and re-verification.

### Evidence that must be producible before starting

A package whose evidence cannot be produced is not `READY`, however complete its design is. Confirm each is reachable:

- The target revision can be pinned, and every test result bound to it.
- An environment manifest can be captured for the environment the tests run in.
- The rollback or compensation path named in this document can actually be exercised.
- A signed `EvidenceManifest` can be issued — today via the interim profile `airl-interim-v0.1` (`scripts/evidence_manifest.py`), which is **tamper-evident and not externally witnessed**.
- The verifier can reach the evidence **without** seeing the producer's working trace.

<!-- /generated:execution-requirements -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-057-T01 | Establish the explicit proxy, DNS policy and TLS strategy | Implementation owner | Commit / configuration / record reference |
| WP-057-T02 | Bind the tool/provider domain registry and the purpose allowlist | Implementation owner | Commit / configuration / record reference |
| WP-057-T03 | Add request/response size, MIME and method constraints | Implementation owner | Commit / configuration / record reference |
| WP-057-T04 | Apply the secret, PII and D3–D4 DLP detectors | Implementation owner | Commit / configuration / record reference |
| WP-057-T05 | Establish canary secrets and anomalous-volume alerting | Implementation owner | Commit / configuration / record reference |
| WP-057-T06 | Write the emergency deny/revoke and exception flow | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Egress proxy`
- `Allowlist registry`
- `DLP pipeline`
- `Egress audit/alerts`
- `Exception runbook`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-057_egress_proxy_dlp.tests.md`](WP-057_egress_proxy_dlp.tests.md).

- Denial of an unknown domain
- Denial of a canary-secret exfiltration attempt
- Denial of a D3 payload to a public endpoint
- Denial of DNS bypass and raw-IP access
- A permitted connector passing cleanly
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-057_egress_proxy_dlp.acceptance.md`](WP-057_egress_proxy_dlp.acceptance.md), together with what this package still cannot establish.

- [ ] No direct internet route exists.
- [ ] A DLP denial can revoke a lease and raise an incident.
- [ ] Sensitive bodies are masked in logs.
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

A false-positive allowlist change is handled through a time-bound exception; a proxy outage fails closed, or falls back to a policy-defined local-only route.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
