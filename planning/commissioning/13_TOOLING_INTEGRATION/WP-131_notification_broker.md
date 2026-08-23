# WP-131 — Notification Broker Foundation

## Package card

| Field | Value |
|---|---|
| Work package | `WP-131` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Platform Security Lead |
| Independent verifier | Safety & Governance Owner |
| Hard dependencies | WP-049 (Tool Registry/Broker), WP-016 (PolicyDecision schemas) |
| Related gates | Platform |
| Related controls | CTL-SEC-04, CTL-DAT-02 |
| Related acceptance scenarios | ACC-41, ACC-42 |
| Related skill | `notifying-humans` |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](WP-131_notification_broker.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](WP-131_notification_broker.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

A **subclass of the Tool Broker** is built so that agents can reach humans. The
agent produces a notification **intent**; only the broker performs the send.

> **Invariant:** An agent never sends a message directly. Every send passes
> through the chain identity → policy → data class → DLP → idempotency →
> transmission → `NotificationReceipt`.

Notification is a `T3` side-effect class (it mutates an external system) and
therefore requires an **explicit egress exception** against the default-deny
network policy of the `ExecutionProfile`.

The reason for the indirection is not ceremony. A message that has left the
system cannot be recalled. Every check that matters must therefore happen
*before* transmission, at a single point that can be audited — which is exactly
what a broker is.


## Analysis
### What this package actually decides

That reaching a human is a **tool call**, not a side channel. The purpose sentence
makes it a subclass of the Tool Broker deliberately: the agent produces a
`NotificationIntent`, and only the broker sends.

Everything WP-049 established applies unchanged — policy chain, idempotency,
receipts, no credential in the agent — and the reason is that notification is the
one outbound path that reaches a person directly. An agent that can message a human
without going through policy has a route to influence a decision that no gate
inspects.

### Nothing here is connected today

`AGENTS.md` §5 records the state: notification channels are **planned** —
*specified, nothing connected, nothing sends*. This package is the first that makes
any of it real, and the honest starting point is that the whole notification stack
is currently unbuilt.

### Idempotency matters more here than elsewhere (T03)

A duplicate database write is invisible. A duplicate page at 3am is a person woken
twice, and a system that does that a few times gets its alerts muted — which is the
failure mode that makes every downstream escalation useless.

### Quiet hours are a control, and they need a pierce rule (T05)

Suppressing notifications overnight is humane and is a risk. The `CRITICAL` pierce
rule (WP-134) is what stops quiet hours from becoming an outage nobody heard about.

### The receipt is what makes a notification auditable

A `NotificationReceipt` plus a `ToolReceipt`, so that *what did the system tell the
operator, and when* is answerable from the record rather than from someone's phone.

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

- Per-channel connector implementation (WP-132)
- Inbound message handling (WP-136)
- Decision authorisation (WP-135)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

2, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-049 — Tool Registry and Tool Broker Core](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md) | `Tool Registry` · `Tool Broker service` · `Invocation/Receipt persistence` · `Connector SDK` |
| [WP-016 — PolicyDecision, Control and Exception Schemas](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md) | `PolicyDecision schema` · `ControlRecord schema` · `ExceptionRecord schema` · `Example decision fixtures` |

### Full prerequisite closure

**38 of 160 packages (24%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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

### What acceptance of this package releases

- **Directly unblocked:** 7 — `WP-132` · `WP-133` · `WP-134` · `WP-135` · `WP-136` · `WP-138` · `WP-140`
- **Transitively reachable:** **8 of 160 packages (5%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **24** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Platform Security Lead |
| Independent verifier | Safety & Governance Owner |
| Gates touched | `Platform` |
| Controls | `CTL-SEC-04` · `CTL-DAT-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-41 — Outbound Notification Exceeds the Channel Data-Class Ceiling](../12_ACCEPTANCE_SCENARIOS/ACC-41_notification_data_class_ceiling.md) | Critical | The payload is refused or degraded to a signed reference with no D2 content; the agent never touches the channel credential; the decision and its rule are audited. |
| [ACC-42 — Notification Broker Unavailable During an Escalating Condition](../12_ACCEPTANCE_SCENARIOS/ACC-42_notification_broker_outage.md) | High | The intent is queued and retried, the affected workflow does not proceed as though notification had succeeded, and the liveness signal reports the degraded path. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-049 (Tool Registry/Broker), WP-016 (PolicyDecision schemas)
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Tool Registry` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool Broker service` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Invocation/Receipt persistence` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Connector SDK` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Audit events` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Capability gate` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `Tool-result reuse with recorded provenance` | `WP-049` | `python3 scripts/progress.py show WP-049` |
| `PolicyDecision schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ControlRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `ExceptionRecord schema` | `WP-016` | `python3 scripts/progress.py show WP-016` |
| `Example decision fixtures` | `WP-016` | `python3 scripts/progress.py show WP-016` |

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
- **Platform Security Lead** carries the acceptance decision; **Safety & Governance Owner** must verify independently of whoever implements.
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

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-131-T01 | Define the broker interface and the `NotificationIntent` schema | Schema file + contract test |
| WP-131-T02 | Build the policy check chain (identity, `TaskContract`, data class) | A negative test for every step of the chain |
| WP-131-T03 | Idempotency key generation and duplicate-send prevention | A second call with the same key performs no send |
| WP-131-T04 | Emit `NotificationReceipt` and `ToolReceipt` | A record for every send; a send without a record is impossible |
| WP-131-T05 | Rate limiting and quiet-hours policy | Over threshold the send is deferred, never dropped |
| WP-131-T06 | Place a transport abstraction (Apprise or equivalent) behind the interface | Changing channel does not change the broker contract |

## Mandatory deliverables

- The `NotificationBroker` service interface and implementation
- The `NotificationIntent` and `NotificationReceipt` schemas
- The policy chain and the idempotency ledger
- The egress allowlist definition
- An updated runbook and the service ownership record
- A signed `EvidenceManifest`

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-131_notification_broker.tests.md`](WP-131_notification_broker.tests.md).

- **An agent cannot send directly:** a send attempted outside the broker is rejected
- **Idempotency:** two calls with the same key → one send, two receipts sharing one `sent_id`
- **Timeout behaviour:** no blind retry when no response arrives; the state is queried instead
- **Rate limit:** over threshold the message queues rather than being silently dropped
- Negative tests for unauthorised, missing, duplicate and partial-failure inputs

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-131_notification_broker.acceptance.md`](WP-131_notification_broker.acceptance.md), together with what this package still cannot establish.

- [ ] No send originating outside the broker can succeed (static **and** runtime checks)
- [ ] Every send produces exactly one `NotificationReceipt`; there is no send without a receipt
- [ ] N calls with the same idempotency key → exactly 1 send
- [ ] Automatic re-sends after a timeout number **zero**
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

- When the broker is down, notifications are **not silently lost**; they queue and the queue depth is monitored
- Extending the egress allowlist requires Safety/Data Owner approval
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The broker is disabled; pending notifications stay in the queue and are sent in
order on re-enable. A notification that has already been sent cannot be recalled
— which is precisely why the pre-send checks are non-waivable.

## Handoff into downstream packages

WP-132 builds the channel registry, WP-133 the outbound flows, WP-134 escalation
and WP-135 decision routing on top of this broker. None of them starts without it.
