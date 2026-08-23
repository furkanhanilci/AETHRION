---
title: "WP-135 — Decision Routing and Signed Deep Links"
aliases:
  - "WP-135"
  - "WP-135 — Decision Routing and Signed Deep Links"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Events requiring a human decision are announced by notification, but the decision itself is taken on an authenticated surface."
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-135_decision_routing_signed_deeplink.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/m
  - aethrion/gate/g1
  - aethrion/gate/g4
  - aethrion/gate/g8
  - aethrion/gate/g9
  - aethrion/state/not-started
---

# WP-135 — Decision Routing and Signed Deep Links

## Package card

| Field | Value |
|---|---|
| Work package | `WP-135` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Governance Lead |
| Independent verifier | Platform Security Lead |
| Hard dependencies | WP-131, WP-132, WP-055 (SPIFFE/Vault identity), WP-093 (Decision Queue UI) |
| Related gates | G1, G4, G8, G9 |
| Related controls | CTL-GOV-01, CTL-SEC-04 |
| Related acceptance scenarios | ACC-25, ACC-26 |
| Related skill | `routing-decision-requests` |
| Status at baseline | `NOT_STARTED` |

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_135_decision_routing_signed_deeplink.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_135_decision_routing_signed_deeplink.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Events requiring a human decision are **announced** by notification, but the
decision itself is taken on an authenticated surface.

> **Invariant:** Messaging is a **notification channel**, not an authorisation
> channel. No decision can be given by a chat reply.

The reasoning: Telegram, Discord, WhatsApp and email accounts can be
compromised, impersonated or forwarded. A `DecisionRecord` is a signed, binding
record; anchoring the end of the evidence chain to a chat message reduces the
entire chain to the security of that channel. This is the preventive side of
the **ACC-25 (Human Approval Forgery)** scenario.

A chat reply **can**: acknowledge receipt, request more information, request an
SLA extension. It **cannot**: approve, reject, or trigger a destructive action.


## Analysis
### What this package actually decides

That a notification **announces** a decision and never carries it. The purpose
sentence draws the line, and T02 states the property that enforces it: the link
carries **surface access, never authority**.

This is ADR-003's rule applied to the human channel. A chat message is untrusted
content in both directions — it can be forwarded, spoofed, quoted and replayed —
and a system that accepts an approval from one has moved its most consequential
control onto its least controlled surface.

### Rejecting approvals from chat is the whole package (T04)

`PR-11` is rubber-stamping; this is the mechanism that makes it maximally easy. A
one-tap approve in a messaging app has no evidence delta, no dissent view, no
rationale field and no MFA — every control WP-093 built, absent.

The correct behaviour is refusal, not a degraded decision path.

### Single-use, time-limited, user-bound (T01, T03)

Three properties, and the third is the one usually missed. A forwarded link that
works has turned a personal authorisation into a bearer token — and forwarding is
exactly what people do with a link they cannot open.

### The attention quota reaches into this package (T05)

`00_PROGRAM/08` makes human decision capacity a hard quota. A notification system
that can generate unlimited decision requests will exhaust it, so the quota is
applied **before** the announcement is sent rather than at the decision surface.

### Nothing sends today

`AGENTS.md` §5 again: specified, nothing connected. This package's controls are
currently a design.

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

- The decision surface UI itself (WP-093)
- The content and rubric of the decision (the relevant gate package)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

4, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-131 — Notification Broker Foundation](../13_TOOLING_INTEGRATION/wp_131_notification_broker.md) | — |
| [WP-132 — Channel Registry and Data-Class Ceiling](../13_TOOLING_INTEGRATION/wp_132_channel_registry_data_class_ceiling.md) | — |
| [WP-055 — SPIFFE/SPIRE Workload Identity and Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md) | `SPIRE/Vault deployments` · `Identity registry mapping` · `Lease policies` · `Break-glass procedure` |
| [WP-093 — Human Decision Queue and Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md) | `Decision Queue UI` · `Evidence-delta component` · `Rationale forms` · `Delegation/escalation views` |

### Full prerequisite closure

**82 of 160 packages (51%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 18 | `WP-027` · `WP-030` · `WP-042` |
| 19 | `WP-031` · `WP-043` · `WP-052` |
| 20 | `WP-032` · `WP-044` · `WP-053` |
| 21 | `WP-033` · `WP-037` · `WP-045` |
| 22 | `WP-034` · `WP-038` · `WP-046` |
| 23 | `WP-035` · `WP-047` · `WP-049` |
| 24 | `WP-050` · `WP-054` · `WP-055` · `WP-131` |
| 25 | `WP-056` · `WP-091` · `WP-132` |
| 26 | `WP-057` · `WP-061` |
| 27 | `WP-058` · `WP-064` · `WP-075` |
| 28 | `WP-062` · `WP-081` |
| 29 | `WP-063` · `WP-065` · `WP-066` · `WP-069` · `WP-082` |
| 30 | `WP-067` · `WP-070` |
| 31 | `WP-068` · `WP-071` |
| 32 | `WP-072` · `WP-076` |
| 33 | `WP-077` · `WP-078` |
| 34 | `WP-079` |
| 35 | `WP-080` |
| 36 | `WP-086` |
| 37 | `WP-087` |
| 38 | `WP-088` |
| 39 | `WP-089` |
| 40 | `WP-093` |

### What acceptance of this package releases

**Nothing.** No package names this one as a hard dependency, so accepting it unblocks no other work. That is normal for a terminal package and is worth knowing before it is prioritised over one that unblocks many.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **41** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Governance Lead |
| Independent verifier | Platform Security Lead |
| Gates touched | `G1` · `G4` · `G8` · `G9` |
| Controls | `CTL-GOV-01` · `CTL-SEC-04` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-25 — Human Approval Forgery](../12_ACCEPTANCE_SCENARIOS/acc_25_human_approval_forgery.md) | Critical | The decision is rejected; gate state does not change and a security event and audit record are produced. A valid owner with MFA and an idempotent request passes as the counter-example. |
| [ACC-26 — Approval, Delegation and Exception Expiry](../12_ACCEPTANCE_SCENARIOS/acc_26_approval_expiry.md) | Critical | The authority is auto-revoked; new operations are denied and running tasks pause or are contained according to policy. There is no automatic extension or re-approval. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-131, WP-132, WP-055 (SPIFFE/Vault identity), WP-093 (Decision Queue UI)
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
| `SPIRE/Vault deployments` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity registry mapping` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Lease policies` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Break-glass procedure` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Identity audit dashboard` | `WP-055` | `python3 scripts/progress.py show WP-055` |
| `Decision Queue UI` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence-delta component` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Rationale forms` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Delegation/escalation views` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Decision audit export` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `HumanAttentionScore` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Evidence delta view` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Human preliminary flow` | `WP-093` | `python3 scripts/progress.py show WP-093` |
| `Friction symmetry measurement` | `WP-093` | `python3 scripts/progress.py show WP-093` |

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
- **Governance Lead** carries the acceptance decision; **Platform Security Lead** must verify independently of whoever implements.
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
| `ASM-065` — Buzz — workflow approval action as a human decision | `DEFER` | nothing — recorded so it is not re-examined from scratch | everything — the implementation here is this repository's own | none |
| — | `BUILD_NATIVE` | Everything not listed above: the contracts, the authority boundaries and the integration this package specifies | All of it | — |

### What each source may never decide

An adopted mechanism supplies a signal, never a verdict. The recurring failure of adoption is not a component behaving badly but a component quietly acquiring authority, which is why every register entry states this before it is taken.

| Source | May never decide | Deliberately not taken |
|---|---|---|
| `ASM-065` | Not adopted for authority. A backend approval may become an interaction surface that presents a decision and collects a human action; the canonical decision is still written through the Decision Service as a signed `DecisionRecord` with its preliminary-assessment rules and assurance context. **A Buzz approval cannot move G8 or G9.** | The approval action as the decision itself. At the reviewed baseline its implementation is not sufficient for scientific authority, and adopting it as UX while implying it is authority is exactly how a gate quietly stops being one. |

### Where a plain row would mislead

- **`ASM-065`** — Deferred rather than rejected: the UX is worth having later, under WP-093's queue and WP-135's signed deep links.

### Unresolved before implementation

**None.** Every obligation the modes above create has been met.

**Acquisition readiness — resolved.** All 1 registered sources have met the obligations their modes create.

<!-- /generated:implementation-sources -->

## Implementation tasks

| Sub-task | Work to be done | Completion evidence |
|---|---|---|
| WP-135-T01 | Generate signed, time-limited, single-use deep links | The link is invalid after expiry |
| WP-135-T02 | Enforce that the link carries **surface access**, never authority | A link alone cannot produce a decision |
| WP-135-T03 | User-bound verification (a forwarded link is invalid) | A link opened under a different identity is rejected |
| WP-135-T04 | Reject approval/rejection attempts arriving from a chat channel | The attempt is logged and rejected |
| WP-135-T05 | Apply the human attention-budget quota | When the quota is exhausted the queue waits; no auto-approve |
| WP-135-T06 | Decision telemetry (duration, sections opened, reversal rate) | Measurements flow to Metascience |

## Mandatory deliverables

- The signed deep-link generator and validator
- The authenticated decision-surface link
- Chat-channel approval rejection
- The attention-budget quota
- Decision telemetry

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-135_decision_routing_signed_deeplink.tests.md`](wp_135_decision_routing_signed_deeplink.tests.md).

- **Approval from chat:** an "I approve" message on a channel produces no decision
- **Link lifetime:** the link is invalid after its TTL
- **Single use:** a second use is rejected
- **Forwarding:** a link opened under another identity is rejected
- **Quota:** when the weekly quota is exhausted, new decision requests wait; there is no auto-approve

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-135_decision_routing_signed_deeplink.acceptance.md`](wp_135_decision_routing_signed_deeplink.acceptance.md), together with what this package still cannot establish.

- [ ] No `DecisionRecord` can originate from a messaging channel
- [ ] Deep links are time-limited, single-use and user-bound
- [ ] When the quota is exhausted the system **waits**; there is no express-review mode
- [ ] The decision-time distribution and the G10 reversal rate are measured
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

- The quota limits the laboratory's throughput. **This is a design choice, not a defect.**
- Link leakage: TTLs are kept short and links are revoked after use
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

If the deep-link mechanism is disabled, decisions are taken only on the surface
itself and notifications degrade to contentless triggers. The decision flow does
not stop.

## Handoff into downstream packages

WP-136 inherits the rule for rejecting approval attempts arriving on inbound channels.
