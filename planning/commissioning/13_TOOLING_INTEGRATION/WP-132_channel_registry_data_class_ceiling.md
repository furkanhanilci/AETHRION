# WP-132 — Channel Registry and Data-Class Ceiling

## Package card

| Field | Value |
|---|---|
| Work package | `WP-132` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Platform Security Lead |
| Hard dependencies | WP-131, WP-006 (ExecutionProfile) |
| Related gates | Platform |
| Related controls | CTL-DAT-02, CTL-DAT-03 |
| Related acceptance scenarios | ACC-41 |
| Related skill | `notifying-humans` |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-132_channel_registry_data_class_ceiling.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-132_channel_registry_data_class_ceiling.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every notification channel is registered with a **data-class ceiling** that is
enforced in code. The ceiling is a pre-send gate, not a recommendation.

| Channel | Ceiling | Rationale |
|---|---|---|
| ntfy (self-hosted) | **D2** | Your own server; no third-party processing |
| Matrix (self-hosted) | **D2** | End-to-end encryption on your own homeserver |
| Signal | D2 | End-to-end encrypted; hard to automate |
| Email (own SMTP) | D1 | Encrypted in transit, not at rest on the server |
| Telegram | **D1** | Cloud; readable server-side |
| Discord / Slack | **D1** | Cloud; third party |
| **WhatsApp** | **D0** | Cloud + a 24-hour window + mandatory approved templates |

> **D3/D4 content never goes to any messaging channel.** Only a contentless
> trigger may be sent: "an identified event exists — check the console."

**WhatsApp operational warning:** on the Business Cloud API, outside the
24-hour window following the user's last message, only pre-approved templates
may be sent. That makes WhatsApp the most fragile channel for agent-initiated
notification, and it is therefore scheduled last.


## Analysis
### What this package actually decides

That a channel has a **data-class ceiling enforced in code**. The purpose sentence
is emphatic — *a pre-send gate, not a recommendation* — and the reason is that a
notification is the easiest accidental exfiltration path in the system.

A person adds a helpful detail to an alert template. The detail is a source
excerpt. The channel is a third-party chat service. Nothing errors.

### Free-text sending is disabled, and that is the strongest control here (T04)

Templates only. A template's fields are known, their data classes are known, and the
ceiling can be checked before send. Free text cannot be checked at all — and a
system that allows it has a DLP scanner as its only defence, which ADR-003 already
says is defence in depth rather than a boundary.

### ntfy self-hosted first, then Telegram (T05)

The ordering matters. A self-hosted channel keeps content inside the trust boundary
while the mechanism is proven; a third-party channel is a lower ceiling
permanently. Registering the ceiling *with* the channel is what makes that
difference structural rather than a note.

### DLP is mandatory and is still not the boundary (T03)

Secrets, tokens and PII scanned before send. It catches the case where a template
field carried something the class did not predict. The **boundary** is the ceiling
plus the template; the scanner is the second layer.

### The egress host belongs in the registry (T01)

A channel's destination is an egress decision (WP-057). Registering it with the
channel is what lets the allowlist and the ceiling agree.

### Baseline v1.3.0 — the messaging layer inherits the same two refusals

Nothing changes about what these packages own. Two rules from this baseline
apply to all of them, and both are restatements of things that erode first at the
edges of a system:

**No message and no timeout becomes authority.** An inbound message is never an
instruction; a notification is never an authorisation; an expired SLA escalates
and pages and never approves.

**Alignment with the new paths.** The capability gate governs any action an
inbound message might trigger. Evidence-delta priority drives the decision
queue. The human preliminary flow means a notification announcing a decision may
not carry the recommendation. Every intervention writes an immutable audit
record atomically with the change it describes.

## Out of scope

- The internal implementation detail of the channel connectors (transport library work)
- The inbound direction (WP-136)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-131 — Notification Broker Foundation](../13_TOOLING_INTEGRATION/WP-131_notification_broker.md) | — |
| [WP-006 — ExecutionProfile and Route Policy](../01_GOVERNANCE/WP-006_execution_profile.md) | `ExecutionProfile semantics` · `Route/control decision tables` · `Enforcement map` · `Negative examples` |

### Full prerequisite closure

**39 of 160 packages (24%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 16 | `WP-023` · `WP-025` · `WP-026` |
| 17 | `WP-024` · `WP-028` · `WP-029` · `WP-041` |
| 18 | `WP-027` · `WP-042` |
| 19 | `WP-031` · `WP-043` |
| 20 | `WP-032` · `WP-044` |
| 21 | `WP-045` |
| 22 | `WP-046` |
| 23 | `WP-049` |
| 24 | `WP-131` |

### What acceptance of this package releases

- **Directly unblocked:** 4 — `WP-133` · `WP-134` · `WP-135` · `WP-136`
- **Transitively reachable:** **6 of 160 packages (4%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **25** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Safety & Governance Owner |
| Independent verifier | Platform Security Lead |
| Gates touched | `Platform` |
| Controls | `CTL-DAT-02` · `CTL-DAT-03` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-41 — Outbound Notification Exceeds the Channel Data-Class Ceiling](../12_ACCEPTANCE_SCENARIOS/ACC-41_notification_data_class_ceiling.md) | Critical | The payload is refused or degraded to a signed reference with no D2 content; the agent never touches the channel credential; the decision and its rule are audited. |
| [ACC-69 — Human Decision Timeout Must Not Auto-Approve](../12_ACCEPTANCE_SCENARIOS/ACC-69_decision_timeout_no_autoapproval.md) | Critical | The state escalates and pages; it never becomes approved. No timeout, no learned preference, no inbound message and no low attention score creates a `DecisionRecord`. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-006 (ExecutionProfile)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- The **acquisition surface is classified**: every part of this package is `DEPENDENCY`, `ADAPTER`, `OPTIONAL_BACKEND`, `STANDARD`, `BENCHMARK`, `PATTERN`, `DIRECT_ADAPT`, `ADAPTIVE_REIMPLEMENT` or `BUILD_NATIVE`, and every obligation the mode creates is resolved — see **Implementation acquisition and assimilation** above.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

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

### Classification that must be recorded before work begins

`00_PROGRAM/05_definition_of_ready_and_done.md` requires all four to be classified at refinement. They are not documentation: together they select the `ExecutionProfile`, and an unclassified package cannot be given one.

| Field | Must state | Recorded at refinement |
|---|---|---|
| `DataClass` | D0–D4 for every input and output this package touches | ☐ |
| `CodeTrust` | provenance of code this package executes | ☐ |
| `ToolEffect` | T0–T5; whether any external side effect occurs | ☐ |
| Network / credential scope | egress destinations and the identity used | ☐ |

### Capacity that must be reserved

- **Effort class `M`** — medium — a dedicated integration window.
- A three-point `O`/`M`/`P` person-day estimate, with `PERT = (O + 4M + P) / 6`, is **mandatory** before this package is `READY`. It is not recorded here because it depends on real capacity at the time of refinement.
- **Safety & Governance Owner** carries the acceptance decision; **Platform Security Lead** must verify independently of whoever implements.
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

Neither register binds an upstream mechanism or a runtime component to `WP-132`, so every deliverable below is **`BUILD_NATIVE`**.

That is a statement about the registers, not a finding that no upstream exists. If refinement identifies one, it is recorded in the register **first** and appears here on the next generation — a component named in this document without a register entry is a defect that `scripts/check_wp_implementation_sources.py` reports.

| Source | Mode | What is taken | AETHRION owns | Unresolved |
|---|---|---|---|---|
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

**Acquisition readiness — nothing to resolve.** No acquisition obligation stands between this package and `READY`.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-132-T01 | Define the `ChannelRegistry` schema (channel, ceiling, egress host, identity) | Schema + populated registry file |
| WP-132-T02 | Enforce the ceiling in code and bind it to the policy engine | An above-ceiling send is rejected in test |
| WP-132-T03 | Make DLP scanning (secrets, tokens, PII) mandatory before send | A message containing a secret is not sent |
| WP-132-T04 | Template registry — free-text sending is disabled | An untemplated send is rejected |
| WP-132-T05 | First channels: ntfy (self-hosted) + Telegram | Both channels work end to end |
| WP-132-T06 | Define the egress allowlist separately per channel | Egress to a host outside the allowlist is blocked |

## Mandatory deliverables

- The `ChannelRegistry` schema and its populated registry
- Data-class ceiling enforcement (code + tests)
- DLP scanning integration
- The message template registry
- A per-channel egress allowlist

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-132_channel_registry_data_class_ceiling.tests.md`](WP-132_channel_registry_data_class_ceiling.tests.md).

- **Ceiling enforcement:** content at ceiling+1 for each channel → send rejected
- **D3/D4:** no content reaches any channel; only a contentless trigger is produced
- **DLP:** sample messages carrying API keys, tokens and PII are caught
- **Templates:** free-text sending is rejected
- **Egress:** a request to a host outside the allowlist is blocked

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-132_channel_registry_data_class_ceiling.acceptance.md`](WP-132_channel_registry_data_class_ceiling.acceptance.md), together with what this package still cannot establish.

- [ ] The per-channel ceiling is defined **in code** and enforced by tests, not only documented
- [ ] D3/D4 content cannot leave through any channel (negative test)
- [ ] There is no code path that skips DLP scanning
- [ ] WhatsApp is reachable only at D0 and only through approved templates
- [ ] All mandatory tests passed on the same target revision.
- [ ] No open Critical or High findings.
- [ ] The independent verifier has accepted the evidence package.

## Acceptance evidence package

- Test results captured on the same target revision/digest
- An `EvidenceManifest` recording the environment, schema, policy and dependency versions
- The independent verifier's `ReviewRecord` or `VerificationRecord`
- The rollback/compensation trial and its result reference
- The list of open findings and residual risks with owners and expiry dates

## Risks and control points

- A channel ceiling does not vary by person; there is no "but it's my own Telegram" exception
- Adding a new channel requires Safety/Data Owner approval and a new ceiling entry
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The channel is removed from the registry; pending messages for that channel are
not dropped — they stay queued and are **not** rerouted to another channel,
because rerouting could breach a ceiling.

## Handoff into downstream packages

WP-133 and WP-134 use the channels in this registry. A channel that is not
registered cannot be used.
