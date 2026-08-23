# WP-051 — Four Trust Zones and Network Segmentation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-051` |
| Workstream | `06_EXECUTION_SECURITY` |
| Initial effort class | **L** — large — split into sub-deliveries if it cannot be reviewed in one pass; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Security Architecture Lead |
| Independent verifier | Independent Security Reviewer / SRE |
| Hard dependencies | WP-006, WP-010, WP-021 |
| Related gates | Platform |
| Related controls | CTL-SEC-01, CTL-SEC-02 |
| Related acceptance scenarios | ACC-05, ACC-16 |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-051_trust_zone_network.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-051_trust_zone_network.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Zone 0 governance, Zone 1 control plane, Zone 2 execution and Zone 3 untrusted content are separated by explicit identity, default-deny networking and audited gateways.


## Analysis
### What this package actually decides

Where the four zones actually begin and end. `00_PROGRAM/01` names them — Zone 0
governance, Zone 1 control plane, Zone 2 execution fabric, Zone 3 untrusted
content — and states the rule: *zone transitions cannot occur without explicit
identity, policy, schema and audit.*

A zone is a diagram until a packet is dropped. This package is where the drop
happens.

### Default deny is the only defensible default (T04)

Allowlists are maintained; denylists are outrun. `ADR-003` puts it more sharply
still: **an anomaly is a denial, not a warning.** A network policy that logs and
forwards on an unmatched rule has inverted its own purpose at exactly the moment
it mattered.

DNS is part of this and is routinely forgotten: an execution pod that can resolve
arbitrary names has an exfiltration channel that no HTTP proxy sees.

### The quarantine↔parser gateway is the most dangerous crossing (T03)

Zone 3 content has to be parsed to be useful, and parsing is where untrusted bytes
meet a decoder. That crossing gets its own gateway because it is the one an
attacker controls the input to — WP-058 does the parsing, this package makes sure
it happens on the correct side of a boundary.

### Separating admin, audit and export paths (T05)

Three flows that look similar and must not share a route. The audit path must
survive an incident on the admin path; the export path carries data out and is the
one an exfiltration attempt will prefer. Collapsing them means an attacker who
reaches one reaches all three.

### The threat tests are the deliverable (T06)

A zone model with no attempted crossings is an assertion. Each declared boundary
needs a test that tries to cross it and is refused — which is `PR-06` and
`00_PROGRAM/07`'s rule that identity and data-routing failures cannot be waived.

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

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |
| [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md) | `Signed ADR bundle` · `Rejected alternatives register` · `Reopen trigger register` · `Architecture baseline digest` |
| [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md) | `Environment topology` · `Account/network IaC` · `Access baseline` · `Environment promotion policy` |

### Full prerequisite closure

**21 of 160 packages (13%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 15 | `WP-021` |

### What acceptance of this package releases

- **Directly unblocked:** 5 — `WP-052` · `WP-055` · `WP-057` · `WP-058` · `WP-060`
- **Transitively reachable:** **103 of 160 packages (64%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W2 — Platform backbone |
| Dependency depth | level **16** of 55 |
| On the documented critical path | **yes** — `02_wave_and_dependency_map.md` names it |
| Effort class | **L** |
| Accountable owner | Security Architecture Lead |
| Independent verifier | Independent Security Reviewer / SRE |
| Gates touched | `Platform` |
| Controls | `CTL-SEC-01` · `CTL-SEC-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-05 — Prompt-Injection PDF](../12_ACCEPTANCE_SCENARIOS/ACC-05_prompt_injection_pdf.md) | Critical | The content stays untrusted quoted data; extraction continues read-only, no tool, secret or write call occurs, and security event and scan evidence is produced. |
| [ACC-16 — Egress Exfiltration Attempt](../12_ACCEPTANCE_SCENARIOS/ACC-16_egress_exfiltration.md) | Critical | The traffic is denied, the canary never leaves, the credential lease is revoked and a security incident and audit record are created. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md), [WP-010 — Architecture Decision and Rejected-Alternatives Baseline](../01_GOVERNANCE/WP-010_adr_baseline.md), [WP-021 — Development, Staging and Production Environment Baseline](../03_FOUNDATION/WP-021_environment_account_network_baseline.md)
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
| `ExecutionProfile semantics` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Route/control decision tables` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Enforcement map` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Negative examples` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Producer and evaluator zone profiles` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `MutationPolicy` | `WP-006` | `python3 scripts/progress.py show WP-006` |
| `Signed ADR bundle` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Rejected alternatives register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Reopen trigger register` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Architecture baseline digest` | `WP-010` | `python3 scripts/progress.py show WP-010` |
| `Environment topology` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Account/network IaC` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Access baseline` | `WP-021` | `python3 scripts/progress.py show WP-021` |
| `Environment promotion policy` | `WP-021` | `python3 scripts/progress.py show WP-021` |

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
- **Security Architecture Lead** carries the acceptance decision; **Independent Security Reviewer / SRE** must verify independently of whoever implements.
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

### No registered source names this package

Neither register binds an upstream mechanism or a runtime component to `WP-051`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Responsible | Completion evidence |
|---|---|---|---|
| WP-051-T01 | Produce the zone, asset and data-flow inventory | Implementation owner | Commit / configuration / record reference |
| WP-051-T02 | Apply NetworkPolicies, firewalls and security groups through IaC | Implementation owner | Commit / configuration / record reference |
| WP-051-T03 | Define the control↔execution and quarantine↔parser gateways | Implementation owner | Commit / configuration / record reference |
| WP-051-T04 | Establish default-deny ingress/egress and DNS policy | Implementation owner | Commit / configuration / record reference |
| WP-051-T05 | Separate the admin, audit and export paths | Implementation owner | Commit / configuration / record reference |
| WP-051-T06 | Write the trust-boundary threat tests | Implementation owner | Commit / configuration / record reference |

## Mandatory deliverables

- `Trust zone diagram/data flows`
- `Network IaC`
- `Boundary policy`
- `Threat-test suite`
- An updated runbook or operations note, plus the service/contract ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-051_trust_zone_network.tests.md`](WP-051_trust_zone_network.tests.md).

- Denial of direct Zone 3 → Zone 1 access
- Denial of unknown egress from execution
- Denial of execution credentials against the control database
- A read-only audit export path
- At least one negative test for unauthorised, missing, stale, duplicate and partial-failure inputs
- Producer/consumer contract compatibility tests on every affected interface
- Telemetry correlation and audit-record integrity checks

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-051_trust_zone_network.acceptance.md`](WP-051_trust_zone_network.acceptance.md), together with what this package still cannot establish.

- [ ] No zone transition occurs without identity, policy, schema validation and audit.
- [ ] Untrusted content never reaches a control prompt or command channel.
- [ ] Network drift raises an alert.
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

A wrong network release is reverted through GitOps rollback; a fail-closed outage is preferred over an unsafe transition.

Immutable artifacts, reviews and decision history are **not** deleted during a rollback; the new state is expressed through a supersession or invalidation record.

## Handoff into downstream packages

On acceptance, the version and digest of every delivered artifact is written to the Package Registry, the dependency event is published, and every `READY` candidate blocked on this package is re-evaluated. A downstream package consumes **only** the contracts and evidence references listed above; it does not bind to internal implementation details.
