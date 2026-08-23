---
title: "WP-136 — Inbound Content Quarantine and Channel Allowlist"
aliases:
  - "WP-136"
  - "WP-136 — Inbound Content Quarantine and Channel Allowlist"
cssclasses:
  - aethrion-work-package
type: work-package
category: commissioning
status: NOT_STARTED
summary: "Every inbound message, email, webhook and external document is treated as Zone 3."
source: "planning/commissioning/13_TOOLING_INTEGRATION/WP-136_inbound_content_quarantine.md"
generated: true
provenance: mirror_plan.py
tags:
  - aethrion/commissioning
  - aethrion/work-package
  - aethrion/workstream/13-tooling-integration
  - aethrion/wave/wt
  - aethrion/effort/m
  - aethrion/gate/g0
  - aethrion/gate/g3
  - aethrion/gate/g10
  - aethrion/state/not-started
---

# WP-136 — Inbound Content Quarantine and Channel Allowlist

## Package card

| Field | Value |
|---|---|
| Work package | `WP-136` |
| Workstream | `13_TOOLING_INTEGRATION` |
| Initial effort class | **M** — medium; a three-point (O/M/P) estimate is mandatory at refinement |
| Accountable owner | Content Security Lead |
| Independent verifier | Safety & Governance Owner |
| Hard dependencies | WP-058 (Content Quarantine Firewall), WP-131, WP-132 |
| Related gates | G0, G3, G10 |
| Related controls | CTL-SEC-02 |
| Related acceptance scenarios | ACC-05, ACC-44 |
| Related skill | `receiving-external-messages` |
| Status at baseline | `NOT_STARTED` |

## Adopted component

> **CaMeL pattern** — trusted control / untrusted data, not a detector

Control flow is derived from trusted intent; untrusted content may supply values but can never create actions or expand permissions. A detector is defence in depth, never the boundary. **AgentDojo** measures the result. See `docs/architecture/ADR-003`.

Rationale and adoption type: `docs/architecture/AETHRION_COMPONENT_REUSE.md`.

## Package documents

This package is described by three documents. They are separate because they have three readers: this card is read at refinement by someone deciding whether the package can start; the test procedures are read months later by whoever runs them; the acceptance criteria are read by an **independent verifier** who must reach a verdict without having done the work — and `00_PROGRAM/06` requires that verifier to work from a packet they can be handed.

| Document | Answers | Read by |
|---|---|---|
| **This card** | What is this, what does it depend on, what does it release? | Refinement, planning |
| [Test procedures](wp_136_inbound_content_quarantine.tests.md) | How is it tested, in what environment, with what data, and what counts as a complete run? | The implementer and the tester |
| [Acceptance criteria](wp_136_inbound_content_quarantine.acceptance.md) | What must hold for this to be `ACCEPTED`, and what does it still not establish? | The independent verifier |

## Purpose and expected outcome

Every inbound message, email, webhook and external document is treated as
**Zone 3**.

> **Invariant:** **Untrusted human-readable inbound content is never an
> instruction.** It is data, not a
> command.

Outbound traffic is a **data exfiltration** risk; inbound traffic is a **control
takeover** risk. Text embedded in an email, a PDF attachment or a chat message
becomes prompt injection the moment it enters an agent's context — the `ACC-05`
scenario extends across the messaging surface.

Quarantine order: sender verification (SPF/DKIM/DMARC, bot identity, channel
allowlist) → attachment and file scanning → tagging the content as
`<untrusted-external-content>` → entry into agent context **only** under that
tag → **no instruction extraction**.


## Analysis
### What this package actually decides

That **anything arriving from outside is Zone 3**. Messages, email, webhooks,
documents — the same treatment WP-058 gives a fetched PDF, applied to the inbound
direction.

The asymmetry this corrects is common and dangerous: systems quarantine what they
fetch and trust what arrives. An email is not more trustworthy than a web page
because someone sent it.

### `receiving-external-messages` is the skill this implements

And the rule it encodes is T05's: **the ban on instruction extraction.** Inbound
content may supply values. It may never supply actions, and no amount of apparent
authority in the message changes that — ADR-003: control flow comes only from
trusted intent.

### Sender verification narrows, it does not authorise (T02)

SPF, DKIM, DMARC and bot identity establish that a message came from where it
claims. They say nothing about whether its content should be acted on, and a system
that treats a verified sender as a trusted instruction source has re-created the
problem one layer up.

### Attachments are the highest-risk element (T03)

Macros, embedded scripts, malformed containers. They go to the same isolated parsing
WP-058 uses, and for the same reason.

### The tagging is mandatory and structural (T04)

`<untrusted-external-content>` around everything inbound, always. Not conditional on
a detector's opinion — because a detector that decides when to tag is a detector
that will eventually decide not to.

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

- Scientific assessment of the content (owned by the G0/G3 packages)

## Dependency and prerequisite analysis

<!-- generated:dependency-analysis — produced by scripts/expand_packages.py; do not edit inside this block -->

### Direct hard dependencies

3, each of which must be `ACCEPTED` — not `TECH_COMPLETE` — before this package is `READY`.

| Package | Supplies to this package |
|---|---|
| [WP-058 — Untrusted Content Quarantine and Prompt-Injection Firewall](../06_EXECUTION_SECURITY/wp_058_content_quarantine_firewall.md) | `Content firewall` · `Parser workers` · `ContentSafetyRecord` · `Injection detector` |
| [WP-131 — Notification Broker Foundation](../13_TOOLING_INTEGRATION/wp_131_notification_broker.md) | — |
| [WP-132 — Channel Registry and Data-Class Ceiling](../13_TOOLING_INTEGRATION/wp_132_channel_registry_data_class_ceiling.md) | — |

### Full prerequisite closure

**49 of 160 packages (31%)** must reach `ACCEPTED` before this one can begin — the direct list above plus everything they in turn require. This is the number that determines when the package can actually start; the direct list is only its last layer.

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
| 24 | `WP-050` · `WP-054` · `WP-055` · `WP-131` |
| 25 | `WP-056` · `WP-132` |
| 26 | `WP-057` |
| 27 | `WP-058` |

### What acceptance of this package releases

- **Directly unblocked:** 1 — `WP-137`
- **Transitively reachable:** **1 of 160 packages (1%)** cannot be accepted until this one is.

The transitive figure is the leverage number. It does not appear anywhere else in the plan, and it is the one that should drive sequencing when two packages are otherwise equally ready.

### Position in the programme

| | |
|---|---|
| Wave | W-T — Tooling |
| Dependency depth | level **28** of 55 |
| On the documented critical path | no |
| Effort class | **M** |
| Accountable owner | Content Security Lead |
| Independent verifier | Safety & Governance Owner |
| Gates touched | `G0` · `G3` · `G10` |
| Controls | `CTL-SEC-02` |

### Acceptance scenarios that exercise this package

`COMMISSIONED` requires every scenario below to pass **on the same release candidate**. A `SKIPPED` scenario on a `Critical` row does not count as a pass.

| Scenario | Severity | What it must show |
|---|---|---|
| [ACC-05 — Prompt-Injection PDF](../12_ACCEPTANCE_SCENARIOS/acc_05_prompt_injection_pdf.md) | Critical | The content stays untrusted quoted data; extraction continues read-only, no tool, secret or write call occurs, and security event and scan evidence is produced. |
| [ACC-44 — Inbound Content Attempts to Act as an Instruction](../12_ACCEPTANCE_SCENARIOS/acc_44_inbound_message_is_not_an_instruction.md) | Critical | No decision record is created, no tool is invoked from the content, the material is labelled untrusted in context, and an authenticated structured `CommandIntent` through the proper path still succeeds. |
| [ACC-117 — Prompt Injection Meets a Capability Gate](../12_ACCEPTANCE_SCENARIOS/acc_117_prompt_injection_capability_gate.md) | Critical | The action is unavailable because policy did not grant the capability, not because a detector recognised the text. Content crosses the boundary; authority does not. |

<!-- /generated:dependency-analysis -->

## Preconditions — Definition of Ready

- Dependencies accepted: WP-058 (Content Quarantine Firewall), WP-131, WP-132
- A named owner, a named implementer and a verifier independent of the producer are assigned.
- `DataClass`, `CodeTrust`, `ToolEffect` and the network/credential scope are classified.
- Test fixtures, the environment, the rollback point and the acceptance measurement method are reachable.

## Execution requirements

<!-- generated:execution-requirements — produced by scripts/expand_packages.py; do not edit inside this block -->

### Inputs that must exist before the first task starts

Each row is a deliverable of a dependency. Its **absence is a stop condition**, not a risk to manage: work started against a missing input is work that will be redone against the real one.

| Required input | Comes from | Accepted? |
|---|---|---|
| `Content firewall` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Parser workers` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `ContentSafetyRecord` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Injection detector` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Quarantine UI/API` | `WP-058` | `python3 scripts/progress.py show WP-058` |
| `Capability gate for untrusted content` | `WP-058` | `python3 scripts/progress.py show WP-058` |

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
- **Content Security Lead** carries the acceptance decision; **Safety & Governance Owner** must verify independently of whoever implements.
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
| WP-136-T01 | Channel and sender allowlist registry | A sender outside the allowlist stays in quarantine |
| WP-136-T02 | Sender verification (SPF/DKIM/DMARC, bot identity) | A forged sender is rejected |
| WP-136-T03 | Attachment and file scanning (malware, macros, embedded scripts) | A malicious attachment never enters context |
| WP-136-T04 | Mandatory `<untrusted-external-content>` tagging | Untagged external content cannot enter context |
| WP-136-T05 | Enforce the ban on instruction extraction | No task is generated from inbound text |
| WP-136-T06 | Route inbound messages to the right flow (G0 intake / note / source / feed) | Each type reaches the correct flow |
| WP-136-T07 | Separate **data** from **control** at the boundary: human-readable content can never become a command, while an authenticated, signed, structured `CommandIntent` may — subject to its own authorisation | Two negative tests and one positive test |

## Mandatory deliverables

- The channel and sender allowlist
- The sender verification chain
- The attachment scanning pipeline
- The `QuarantineRecord` schema
- Untrusted-tagging enforcement

## Test and verification plan

The outline below is the summary. The executable procedure — environment, data, coverage items, cases, execution log, incident and completion reports — is in [`WP-136_inbound_content_quarantine.tests.md`](wp_136_inbound_content_quarantine.tests.md).

- **Prompt injection:** an email and a PDF carrying embedded instructions → agent behaviour is unchanged
- **Untagged content:** untagged external content cannot enter context (negative test)
- **Forged sender:** a message failing DKIM/DMARC stays in quarantine
### Data versus control — why the invariant is worded narrowly

| Class | Example | May it cause an effect? |
|---|---|---|
| **Untrusted content** | email body, PDF text, chat message, web page, abstract | **Never.** It is quarantined data, whatever it says |
| **Authenticated command** | a signed, structured `CommandIntent` from a registered service identity | Possibly — through its own authorisation path, never by being persuasive |

Writing the invariant as "an inbound *message* is never an instruction" would
also forbid legitimate machine-to-machine automation later. The line that
matters is not inbound versus outbound; it is **persuasion versus
authentication**. A prompt-injection payload and a polite request are the same
class of object; a signed command from a known identity is a different one.

- **Approval attempt:** an "I approve" in an inbound message produces no decision
- **Unknown sender:** the content does not enter context; a summary is reported to a human

## Acceptance criteria

The programme-level conditions are below. The package-specific, measurable criteria — each with a threshold and the test case that decides it — are in [`WP-136_inbound_content_quarantine.acceptance.md`](wp_136_inbound_content_quarantine.acceptance.md), together with what this package still cannot establish.

- [ ] No external content enters any agent context without being tagged
- [ ] No code path extracts instructions from inbound text
- [ ] Sender verification cannot be skipped
- [ ] The ACC-05 scenario also passes on the messaging surface
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

- "The sender is familiar" is not a valid justification; senders can be impersonated
- PDF is the most common injection carrier; attachment scanning is non-waivable
- A "package complete" statement is not acceptance. Without a verifier decision the package can only be `TECH_COMPLETE`.

## Rollback / compensation

The inbound channel is closed; quarantined content is not deleted and remains
available for review. Quarantine records are retained for audit.

## Handoff into downstream packages

WP-137 subjects external feed content to these same quarantine rules.
