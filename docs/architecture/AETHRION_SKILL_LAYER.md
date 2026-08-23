# AETHRION Skill Layer — Full `obra/superpowers` Integration Report

| Field | Value |
|---|---|
| Document type | Architectural contribution — operational layer design |
| Source | `github.com/obra/superpowers` (14 skills, all read) |
| Target | `AIRL-OS-Architecture.md` v1.0 — *historical name; current identity **AETHRION**, current reference [`AETHRION_ARCHITECTURE.md`](AETHRION_ARCHITECTURE.md)* |
| Sibling documents | `AETHRION_ARCHITECTURE.md` (system overview + diagrams) · `AETHRION_IDEAL_STRUCTURE.md` (roles, review mechanisms, metascience) · `AETHRION_EXTERNAL_STANDARDS.md` (what is adopted) |
| Date | 2026-08-23 |
| Status | Proposal — awaiting a human decision, **except Sections 14, 15 and 16, which are decided** |

**In one paragraph.** A `RoleContract` says who an agent is; nothing said how it works, and that gap was filled by the prompt — an unversioned, untested, unauditable layer. This report analyses `obra/superpowers` and derives the skill layer that closes it. Sections 2–13 record the original analysis; **§14 is the decided correction**: research skills extend their engineering counterparts rather than replacing them, both families live in one registry in the Agent Skills open format, and provenance to upstream is pinned per skill.

> **Read Section 14 first.** It overrules the "convert each engineering skill into
> a research skill" reading that runs through Sections 2–13, and fixes the format
> the skills are written in. **Section 15** records the 2026-08-23 overlap audit
> against a second upstream methodology, and the one gap it found.

---

## 0. The diagnosis in one sentence

> **AETHRION uses `RoleContract` to define *who* an agent is.
> It defines *how the agent works* nowhere.**
>
> Superpowers solves exactly that missing half — and solves it with a method
> that has been validated experimentally rather than asserted.

Look at your current `RoleContract`:

```yaml
RoleContract:
  role: "Evidence Extractor"
  purpose: "Determine which evidence supports which claim, from which source"
  inputs: [claim_candidates, source_candidates]
  outputs: [evidence_spans]
  tools_allowed: [pdf_annotate, text_similarity, citation_parse]
  data_classes_read: [D0, D1, D2]
  independence_requirements: [...]
  budget: {...}
  success_criteria: [span_coverage >= 0.95, false_positive_rate <= 0.05]
```

Everything here is a **boundary**: who, what may be read, how much may be spent,
what must be produced. The one thing missing is **procedure**. Nowhere is it
written *which steps* the Evidence Extractor takes, *in what order*, with *which
verifications*. That gap is currently filled by the prompt — that is, by a layer
that is unversioned, untested and unauditable.

Superpowers' answer: **the Skill.**

---

## 1. Conceptual placement: where the Skill layer sits

```
┌─────────────────────────────────────────────────────────────┐
│ RoleContract Registry        ← WHO (identity, authority,    │  EXISTS ✅
│                                 budget)                      │
├─────────────────────────────────────────────────────────────┤
│ ►► SKILL REGISTRY ◄◄         ← HOW (procedure, trigger,     │  MISSING ⚠️
│                                 iron law, verification)      │
├─────────────────────────────────────────────────────────────┤
│ Task Compiler                ← BINDING (role + skill +      │  EXISTS ✅
│                                 project)                     │
├─────────────────────────────────────────────────────────────┤
│ TaskContract                 ← THE EXECUTABLE TASK           │  EXISTS ✅
├─────────────────────────────────────────────────────────────┤
│ LangGraph Runtime            ← EXECUTION                     │  EXISTS ✅
└─────────────────────────────────────────────────────────────┘
```

**What a skill is:** a versioned, tested unit of behaviour containing its trigger
conditions, its procedure, its iron law, its verification steps and *the known
evasion rationalisations*.

**Why it must not be embedded inside `RoleContract`:**
- One skill is used by **many roles** (`verification-before-completion` by everyone).
- One role uses **many skills** (Evidence Extractor: `extracting-evidence` +
  `anchoring-spans` + `verification-before-completion`).
- Skills load **by trigger**, not by role ("when you see an unexplained anomaly,
  load `investigating-anomalies`").
- Skills are **versioned and tested independently**.

**And it adds fields to `TaskContract`:**

```yaml
TaskContract:
  # ... existing fields ...
  skills_loaded:                                    # ← NEW
    - "airl:extracting-evidence@2.1.0"
    - "airl:anchoring-spans@1.4.0"
    - "airl:verification-before-completion@3.0.0"
  skill_bundle_hash: "sha256:..."                   # ← NEW, auditable
```

This puts the question "under which rules did this agent operate?" **into the
evidence chain**. Today that information is stored nowhere — once a claim is
produced, you cannot determine retrospectively which procedure the producing
agent followed.

---

## 2. Superpowers' real contribution: how skills are *written*

The skill catalogue matters less than people assume. **The real contribution is
the meta-method.**

### 2.1 The Iron Law: "NO SKILL WITHOUT A FAILING TEST FIRST"

In Superpowers, a skill is produced like this:

```
RED:      Run the baseline scenario WITHOUT the skill.
          Record how the agent fails and WHICH RATIONALISATIONS IT PRODUCES,
          VERBATIM.

GREEN:    Write the minimum skill that closes THOSE SPECIFIC failures.
          Test again — does it comply?

REFACTOR: Find the new evasion rationalisations, close them explicitly,
          test again.

No exceptions: "a simple addition", "an update", "a small untested fix" —
untested work is deleted and started again.
```

**Why this is critical for AETHRION:**

You have a `non-waivable blocker` list. But you have **no defence against the
rationalisations an agent will produce while trying to get around it.** Writing
"non-waivable" does not mean a model will not cross it — a model can always
produce a plausible-sounding justification:

> *"Reproduction is technically impossible in this case because the environment
> changed; however, since the results are consistent, the evidence can be
> considered sufficient."*

Superpowers' answer: **the rationalisation table.** The evasions the agent
actually produced during baseline testing, verbatim, each with an explicit
counter-ruling.

### 2.2 A rationalisation table adapted to AETHRION

For the `preregistration-discipline` skill:

| Rationalisation the agent produced | Ruling |
|---|---|
| "The analysis plan is already implied by the protocol" | **NO.** Implication ≠ a lock. `AnalysisPlanManifest` is a separate hash. Without it, no `confirmatory` claim may be produced. |
| "I couldn't know which test was appropriate without seeing the result" | **Correct — and that is exactly why it is `exploratory`.** Label it and continue. |
| "This is only a small covariate addition" | **There is no such thing as a small change.** Every post-plan change is `exploratory`. |
| "The preliminary analysis was exploratory; the main analysis follows the plan" | **If the exploratory data came from the same data as the main analysis, it is not independent.** Both are `exploratory`. |
| "There is time pressure; the plan can be written afterwards" | **Time pressure is not a justification.** G5 does not start before the plan is locked. |

This table is **not invented** — it is compiled from the rationalisations agents
actually produced in the baseline test. It is the only mechanism that converts
"non-waivable" from a declaration into an enforceable rule.

### 2.3 Trigger discipline — a subtle but critical finding

A failure mode Superpowers discovered experimentally:

> **If the `description` field summarises the procedure, the agent follows the
> summary instead of reading the skill.**
>
> A real case: a description reading "code review between tasks" caused the agent
> to perform **one** review — when the skill's flowchart required **two**.

**Rule:** `description` states **only the trigger condition**, never the procedure.

- ✅ `"Use when tests have race conditions, timing dependencies, or pass/fail inconsistently"`
- ❌ `"Use for TDD — write test first, watch it fail, write minimal code, refactor"`

**Applying this directly to AETHRION:** your `RoleContract.purpose` field currently
summarises a procedure:

```yaml
purpose: "Determine which evidence supports which claim, from which source"
```

That is a procedure description. An agent can read it and skip the skill. It
should be split:

```yaml
role: "Evidence Extractor"
triggers: "When a SourceRepresentation exists for a ClaimCandidate that has
           no EvidenceSpan yet"
skills: ["extracting-evidence@2.1.0", "anchoring-spans@1.4.0"]
```

### 2.4 Token budget — and a finding

Superpowers' limits: getting-started `<150 words`, frequently-loaded `<200 words`,
others `<500 words`.

**Finding:** the 130 WP files under `planning/commissioning/` averaged **677
words**, of which **59.2% was template repeated verbatim across 130 files**
(measured). In other words:

> **Your commissioning plan is not agent-consumable.** It is a good human
> document and a poor agent context — every load carries ~400 words of template
> noise and the density of real instruction is low.

In a laboratory operated by models, that requires a **machine-consumable
projection**: for each WP, a template-free skill or task-brief under 500 words
containing the trigger, the iron law and the verification step.

Superpowers already has the answer: `scripts/task-brief` — it extracts the plan
**mechanically** rather than summarising it with a prompt. That is the same
principle as your own `ReviewPacketBuilder` argument: **a program, not a prompt.**

---

## 3. Skill anatomy — the AETHRION adaptation

To Superpowers' `SKILL.md` schema, I add the fields AETHRION needs (**bold** items
are added):

```markdown
---
name: extracting-evidence
version: 2.1.0
description: Use when a ClaimCandidate exists without a linked EvidenceSpan
             and at least one SourceRepresentation is available
                                          # TRIGGER ONLY — no procedure

gates: [G3, G6]                           # ← ADDED: bound gates
roles: [Evidence Extractor]               # ← ADDED: bound roles
assurance_classes: [R1, R2, R3]           # ← ADDED: where it is mandatory
non_waivable: false                       # ← ADDED
data_class_ceiling: D2                    # ← ADDED
requires_skills:                          # ← ADDED: composition
  - anchoring-spans
  - verification-before-completion
emits:                                    # ← ADDED: canonical output
  - EvidenceSpan
  - ToolReceipt
mechanical_checks:                        # ← ADDED: needing no model judgement
  - span_resolves_in_representation
  - quote_exact_match
tested_against: baselines/extracting-evidence/  # ← ADDED: the RED scenarios
---

# Extracting Evidence

## General principle
[1–2 sentences]

## When to use it / when not to
[symptom list]

## Iron law
[if any — one sentence, no exceptions]

## Procedure
[steps, with a verification at each step]

## Mechanical verification
[checks that run without model judgement]

## Rationalisation table
| Rationalisation | Ruling |

## Red flags
[signs that this skill is being skipped]
```

**Directory layout:**

```
skills/
  <skill-name>/
    SKILL.md              # mandatory, <500 words
    procedure.md          # heavy reference of 100+ lines (optional)
    checks/               # mechanical check scripts
    baselines/            # RED scenarios — the skill's own tests
```

**Composition rule** (taken verbatim from Superpowers): **reference** a dependent
skill, do not embed it.
- ✅ `**REQUIRED BACKGROUND:** you must have understood the airl:anchoring-spans skill`
- ❌ `@skills/anchoring-spans/SKILL.md` — burns the context immediately

---

## 4. The AETHRION Skill Catalogue

All 14 Superpowers skills plus additions specific to the research domain.
**A) Meta**, **B) Discipline**, **C) Process**, **D) Review**, **E) Research**,
**F) Metascience**, **G) Communication**.

### A. Meta skills

| Skill | Superpowers counterpart | Job |
|---|---|---|
| `using-aethrion` | `using-superpowers` | Entry point; which skill applies in which situation |
| `writing-skills` | `writing-skills` | Skill-writing discipline — **RED/GREEN/REFACTOR and a rationalisation table are mandatory** |

### B. Discipline skills (iron-law — tested under pressure)

| Skill | Iron law | Superpowers source |
|---|---|---|
| **`preregistration-discipline`** | **NO CONFIRMATORY CLAIM WITHOUT A LOCKED PREREGISTRATION.** Any result computed before the plan is locked is relabelled `exploratory` — no exceptions. | `test-driven-development` (direct adaptation) |
| **`verification-before-completion`** | **NO COMPLETION CLAIM WITHOUT FRESH VERIFICATION EVIDENCE.** Evidence quoted from memory, from a previous run or from an agent's report is not evidence. | `verification-before-completion` (one-to-one) |
| **`evidence-before-claim`** | **EVERY ASSERTION MUST RESOLVE TO AN `EvidenceSpan`.** A sentence that cannot be resolved cannot be published. | *(new — research-specific)* |
| **`scope-discipline`** | **THE TEXT MAY NOT EXCEED `ClaimVersion.scope_qualification`.** Checked mechanically. | *(new)* |
| **`independence-discipline`** | **A PRODUCER MAY NOT SUMMON ITS OWN VERIFIER OR ITS OWN HELPER.** | `subagent-driven-development` ("the implementer never dispatches subagents") |

The one-to-one translation of `verification-before-completion` into AETHRION:

```
1. IDENTIFY the command that will prove the claim
2. RUN it FRESH (not from memory)
3. READ the full output — exit code, error count
4. VERIFY that the output genuinely supports the claim
5. REPORT the evidence ATTACHED to the claim

Forbidden phrases (before verification):
  "should work", "probably correct", "it appears", "Great!", "Perfect!"
  and trusting an agent's report without independent verification
```

This is the **operational** form of your `TECH_COMPLETE ≠ ACCEPTED` distinction.
The distinction exists conceptually ✅ — but no rule enforces it.

### C. Process skills

| Skill | Superpowers counterpart | What it does in AETHRION |
|---|---|---|
| `framing-research` | `brainstorming` | **Classify first:** `Spike / Bounded / Architectural` → the AIRL equivalent `Exploratory / Replication / Confirmatory`. **"When in doubt, choose the heavier one."** The approval gate never disappears; only its ceremony shrinks. |
| `writing-protocols` | `writing-plans` | Authoring `ProtocolManifest`: **placeholders forbidden** ("TBD", "handle the edge cases", "similar to Task N"), exact values and a verification at every step, type consistency, a self-review checklist |
| `writing-analysis-plans` | *(new)* | `AnalysisPlanManifest` — **a lock separate from the protocol** |
| `executing-experiments` | `executing-plans` | Batch execution plus checkpoints |
| `agent-driven-research` | `subagent-driven-development` | **The centre of this document** — Section 5 |
| `dispatching-parallel-analysts` | `dispatching-parallel-agents` | Multi-analyst fan-out discipline — Section 6 |
| `using-isolated-environments` | `using-git-worktrees` | An isolated workspace plus **clean baseline verification**; "do not fight the harness" |
| `finishing-a-project` | `finishing-a-development-branch` | A closing checklist plus **a menu for the human** — Section 7 |

### D. Review skills

| Skill | Superpowers counterpart | Note |
|---|---|---|
| `requesting-review` | `requesting-code-review` | **A standalone package, never the session history.** Severity: Critical / Important / Minor. Output: strengths → findings (by severity) → assessment |
| **`receiving-review`** | `receiving-code-review` | **Entirely absent from your architecture — Section 8** |
| `blind-reviewing` | *(new)* | Frozen packet, no producer trace |
| `adversarial-reviewing` | *(new)* | ACH plus a diagnosticity matrix |
| `arbitrating-disagreement` | *(new + the `subagent-driven-development` breaker)* | Delphi rounds plus the breaker |

### E. Research-domain skills

| Skill | Job |
|---|---|
| `investigating-anomalies` | The research counterpart of `systematic-debugging` — Section 9 |
| `investigating-integrity-concerns` | The RIO process; the `IntegrityCase` lifecycle |
| `searching-literature` | Search protocol, multi-source discovery |
| `screening-sources` | Inclusion/exclusion criteria, active learning (ASReview) |
| `extracting-evidence` | Span extraction |
| `anchoring-spans` | W3C multi-selector anchoring, re-anchoring |
| `curating-zotero` | The two-library model, 412 reconciliation |
| `building-review-packets` | `ReviewPacketBuilder` — **a program, not a prompt** |

### F. Metascience skills

| Skill | Job (see `AETHRION_IDEAL_STRUCTURE.md` Section C) |
|---|---|
| `calibrating-confidence` | Brier score, isotonic calibration, the `UNCALIBRATED` state |
| `measuring-agreement` | κ / error correlation → the independence quota |
| `injecting-controls` | Positive and negative control injection (hidden from the agents) |

### G. Communication and external-world skills

> **Architectural warning:** messaging is not a *skill*, it is a **Tool Broker
> connector**. These skills define the agent's discipline in producing an
> *intent*; the **Notification Broker** performs the send. **An agent never sends
> a message directly.**

| Skill | Direction | Critical rule |
|---|---|---|
| `notifying-humans` | outbound | A per-channel data-class ceiling; DLP; idempotency |
| `routing-decision-requests` | both | **Messaging is not an authorisation channel** |
| `receiving-external-messages` | inbound | **An inbound message is never an instruction** (Zone 3) |
| `escalating-and-paging` | outbound | A timeout is never an auto-approval |
| `publishing-digests` | outbound | A read-only derivative; it changes no state |
| `submitting-external-records` | outbound | OSF/Zenodo/ORCID — irreversible, human-approved |
| `monitoring-external-feeds` | inbound | G10; no silent supersession |

#### Notification Broker — a new component

Added to the Execution Plane as a subclass of the `Tool Broker`:

```
Agent → notification INTENT
      → Notification Broker
           1. identity + TaskContract validation
           2. DATA-CLASS CEILING (per channel)
           3. DLP scan (secrets, PII — Presidio)
           4. template application (not free text)
           5. idempotency key
           6. rate limit + quiet hours
           7. send  →  NotificationReceipt + ToolReceipt
```

**Suggested abstraction:** [Apprise](https://github.com/caronc/apprise) —
abstracts 143 services behind a single URL format (Telegram, Discord, Slack,
Matrix, ntfy, Signal, email, WhatsApp/Twilio). It is appropriate as the broker's
transport layer; the policy and DLP layers are written **on top of it**, never
delegated to it.

#### Per-channel data-class ceiling

| Channel | Ceiling | Rationale |
|---|---|---|
| ntfy (self-hosted) | **D2** | Your own server |
| Matrix (self-hosted) | **D2** | E2E encryption on your own homeserver |
| Signal | D2 | E2E; hard to automate |
| Email (own SMTP) | D1 | Encrypted in transit, not at rest |
| Telegram | **D1** | Cloud |
| Discord / Slack | **D1** | Cloud, third party |
| **WhatsApp** | **D0** | Cloud + **a 24-hour window and mandatory approved templates** |

> **D3/D4 content goes to no messaging channel.** Only a contentless trigger.
>
> **WhatsApp is the worst channel for agent-initiated notification:** outside the
> 24-hour window following the user's last message, only pre-approved templates
> can be sent. It is operationally fragile.

#### Why inbound traffic is more dangerous

An outbound message is a **data exfiltration** risk. An inbound message is a
**control takeover** risk. Text embedded in an email, a PDF attachment or a
Discord message becomes prompt injection the moment it enters an agent's
context — the `ACC-05` scenario widens across the messaging surface.

Hence the inbound path: sender verification → attachment scanning →
`<untrusted-external-content>` tagging → **no instruction extraction**.

#### The approval flow — the preventive side of `ACC-25`

```
DecisionRequest → notification + a SIGNED, TIME-LIMITED, SINGLE-USE deep link
                → the human opens the link
                → the decision is made on an AUTHENTICATED surface
                → the DecisionRecord is signed
```

A chat reply: acknowledgement ✅, request for more information ✅,
**approval/rejection ❌**.

---

## 5. `agent-driven-research` — the central skill

Superpowers' `subagent-driven-development` skill closes your largest operational
gap. Four mechanics:

### 5.1 Information asymmetry — at the file level

| | Producer sees | Reviewer sees |
|---|---|---|
| Task brief / ProtocolManifest | ✅ | ✅ |
| The **interfaces** of previous tasks | ✅ | — |
| Global constraints (**verbatim** from the spec) | ✅ | ✅ |
| The producer's report | writes it | ✅ |
| The produced artifact / diff | produces it | ✅ |
| **The producer's internal reasoning** | — | ❌ **never** |
| Session history | ❌ | ❌ |

**Your `ReviewPacket.excluded_from_packet` list already agrees ✅.**
Two rules need adding:

1. **"No context pasting"** — no inline text is passed to the reviewer, only a
   **file path plus a hash**. That is what makes `evidence_packet_hash` genuinely
   auditable.
2. **Global constraints are copied mechanically from the spec**, never summarised.

### 5.2 A bounded escalation ladder plus "the breaker"

Superpowers' disagreement resolution — **which you do not have**:

```
Rounds 1–3:  Return to the SAME producer. Its context is preserved.
             Open findings are relayed VERBATIM (never summarised).
             The correction report is APPENDED to the SAME report file
             (persistent memory).
             Only the changed part is re-reviewed (FIX_BASE → HEAD).

Rounds 4–5:  A FRESH producer on a MORE CAPABLE model.
             Framed explicitly: "A previous producer attempted this N times;
             it is now yours."

Still open at the end of round 5 → THE BREAKER:
             Dispatch STOPS.
             A human rules on every open finding ONE BY ONE.
             Every ruling is written into the ledger.
             ►► SILENT DISCARD IS FORBIDDEN ◄◄
```

**What is missing from your `DisagreementCase`:**
- No round limit
- No model-tier escalation
- No "findings are relayed verbatim" rule
- **And most importantly: no guarantee that open findings do not silently vanish**

Your finding lifecycle in the evidence and acceptance strategy
(`REPORTED → … → CLOSED`) is correct — but it is **not bound to a round-based
escalation**, and it does not force the question "what happened to this finding?"
at every round.

**To add:**

```yaml
DisagreementCase:
  # ... existing fields ...
  round: 3                          # ← NEW
  max_rounds: 5                     # ← NEW
  escalation_tier: "fresh_producer_higher_model"   # ← NEW
  finding_ledger:                   # ← NEW — one row per finding
    - finding_id: "F-012"
      status: "OPEN"                # OPEN | RESOLVED | PARKED
      rounds_seen: [1, 2, 3]
      # MANDATORY when PARKED:
      parked_rationale: null
      parked_owner: null
      parked_expiry: null
  breaker_invoked: false            # ← NEW
```

**Rule:** a `DisagreementCase` may close only when every row in `finding_ledger`
is `RESOLVED` or `PARKED` (with a rationale, an owner and an expiry). Closing
with a status-less finding is **forbidden**.

### 5.3 Dispatch uniqueness

| Rule | AETHRION counterpart |
|---|---|
| A **fresh** subagent per task | Context Isolation ✅ (exists) |
| A **single** implementation dispatch per task (no parallel producers — collisions) | ⚠️ missing |
| Small, same-shaped jobs are **batched into one dispatch** | ⚠️ missing |
| **A producer never calls a subagent** | ❌ **missing — critical** |

### 5.4 Ledger-based recovery

If context runs out: `progress.md` supplies the completed work and the Git
commits. **Deterministic recovery.**

Your `implementation_log.md` agrees in spirit ✅ but is **free text** — an agent
cannot parse it reliably.

**To add:** `progress.jsonl` (append-only, machine-readable):
```json
{"step_id":"S-041","wp_ids":["WP-011"],"status":"TECH_COMPLETE",
 "target_sha":"6c849bd","evidence_manifest":"delivery/WP-011/em.json",
 "skills":["airl:writing-protocols@1.2.0"],"ts":"2026-08-22T00:05:00+03:00"}
```

---

## 6. `dispatching-parallel-analysts` — multi-analyst discipline

Superpowers' fan-out rules are the operational counterpart of the
**multi-analyst** proposal in `AETHRION_IDEAL_STRUCTURE.md` Section B3:

| Superpowers rule | AETHRION application |
|---|---|
| Fan out only over **independent** problem areas | Are the analysis paths genuinely independent? If they are causally linked, do not parallelise |
| Each agent gets a **narrow scope** and a **self-contained** prompt | Each analyst gets the same `AnalysisPlanManifest`, a different model family, and **cannot see the others** |
| The "do not modify other code" constraint | "Do not see or use another analyst's output" |
| **Collision checking** when merging results | The **distribution** of results — convergence or divergence |
| A full test suite plus spot checks | If the spread is wide → `claim.confidence` DROPS and `scope_qualification` becomes mandatory |

**And read in reverse — this is a metascience signal:**

> Independent analysts **converging too quickly** is also an alarm. Genuinely
> independent judges do not produce κ ≈ 1.0. Either the task is trivial, or the
> independence is not real.

---

## 7. `finishing-a-project` — closing discipline

Superpowers' branch-closing skill adapts directly to G8/G9:

```
1. Run the full verification suite → IF ANY OF IT IS RED, STOP
2. Capture the environment state (which target, which environment)
3. Verify the base reference (which manifest it derives from)
4. PRESENT A MENU TO THE HUMAN
5. Apply the selection
6. Clean up
```

**Two rules to take verbatim:**

1. **"Tests are non-negotiable."** If verification is red, the menu is **never
   shown**. Your G8 has this (the non-waivable blocker) ✅ but it is not
   formulated as a *closing checklist*.

2. **Full-word confirmation:**
   > *"Even phrases like 'Yeah, get rid of it' don't authorize deletion; only the
   > typed word `discard` does."*

   The AETHRION counterpart — **full-word confirmation is mandatory for
   destructive operations:**
   - Retracting a claim → `RETRACT`
   - Superseding a publication → `SUPERSEDE`
   - Abandoning a project → `ABANDON`
   - Unfreezing a literature set → `UNFREEZE`

   "OK remove it" and "sure, cancel it" are **not authorisation**. This is the
   preventive side of your `ACC-25 Human Approval Forgery` scenario.

---

## 8. `receiving-review` — the link entirely missing from your architecture

**Finding:** your architecture has `ReviewVerdict` and `DisagreementCase`, but the
**producer's response to a review is not modelled at all**.

The concrete gap:

```
Blind Reviewer A: CONDITIONAL_PASS
  conditions:
    - "Qualify the claim as 'under the synchronous assumption'"
    - "Add a test for the asynchronous case"

→ Then what happens?
   Did the producer accept the conditions?
   Did it dispute them?
   Who VERIFIED that the conditions were met?
   If they were not met, can the claim still proceed to G8?

   The architecture answers NONE of these questions.
```

Superpowers' `receiving-code-review` skill solves exactly this.

### 8.1 The response frame

```
Read → Understand → VERIFY → Evaluate → Respond → Implement
```

> *"Verify before implementing. Ask before assuming.
> Technical correctness over social comfort."*

### 8.2 Disagreement is legitimate (and encouraged)

The producer **should** push back when:
- The feedback breaks existing working behaviour
- The reviewer lacks full context
- It is a YAGNI violation
- It contradicts an architectural decision
- It is technically incorrect

> *"Use technical reasoning, not defensiveness. Reference working tests/code."*

**Why this is critical in an AI laboratory:** models are **sycophantic**. They
agree where they should object. If the producer's right to object is not defined
explicitly, the review process becomes approval theatre — the reviewer says
something, the producer agrees, and nobody learns anything. That is the
agent-side equivalent of `PR-11` rubber-stamping.

### 8.3 Forbidden: performative agreement

> *"Never give performative responses like 'Great point!' or 'You're absolutely
> right!' — actions demonstrate comprehension instead."*

This is a direct LLM failure mode and must be forbidden in `ReviewVerdict`
responses.

### 8.4 STOP on ambiguity

> *"If any item is unclear: STOP — do not implement anything yet."*

The order: **resolve every ambiguity first** → blocking problems → simple fixes →
complex fixes → test each separately → regression check.

### 8.5 The object to add

```yaml
ProducerResponse:                          # ← NEW CANONICAL OBJECT
  response_id: "resp-2026-08-001"
  verdict_id: "verdict-2026-08-reviewer-a-001"
  responder: "<producer role/model profile>"
  response_date: "..."

  per_condition:
    - condition_id: "C-01"
      stance: "ACCEPTED"          # ACCEPTED | DISPUTED | CLARIFICATION_NEEDED
      action_taken: "claim-v3 produced; scope qualified as 'synchronous'"
      evidence_ref: "claim-v3-2026-08-001"
      verified_by: "mechanical:scope-conformance"     # WHO verified it
    - condition_id: "C-02"
      stance: "DISPUTED"
      technical_rationale: "The asynchronous test is outside the G2 protocol
                            scope; widening the scope requires a new
                            ProtocolManifest"
      escalated_to: "DisagreementCase disagree-2026-08-001"

  # MANDATORY INTEGRITY RULE:
  # Every condition must carry a stance.
  # Proceeding to G8 with an unanswered condition is FORBIDDEN.
```

**And the gate rule:** if `ReviewVerdict.decision == CONDITIONAL_PASS`, then
before G8 every `condition` must be either `ACCEPTED` **and independently
verified**, or `DISPUTED` **and bound to a DisagreementCase**.

This single addition closes the largest hole currently open in your review
process.

---

## 9. `investigating-anomalies` — the research counterpart of `systematic-debugging`

Superpowers' four-phase root-cause analysis adapts directly to experimental
anomalies.

**Iron law:** *"NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST"*

The AETHRION counterpart: **AN ANOMALY MAY NOT BE "FIXED" OR EXCLUDED BEFORE ITS
ROOT CAUSE IS UNDERSTOOD.**

This bears directly on your `ProtocolManifest.exclusion_rules`: *"Outliers > 3σ
from median excluded"* — an exclusion rule applied before the root cause is
understood is not data cleaning, it is **result shaping**.

| Phase | Superpowers (code) | AETHRION (research) |
|---|---|---|
| **1. Root cause** | Read the error message fully, reproduce it consistently, check recent changes, add logging at the boundaries, trace the data flow backwards | **Reproduce** the anomaly, check the execution context (seed, environment, versions), add measurement at the pipeline boundaries, trace the data back to its source |
| **2. Pattern analysis** | Find similar working code, read the reference **fully**, list every difference | Find **working** runs of the same condition, list every difference (seed, node, version, data slice) |
| **3. Hypothesis** | "X is the root cause because Y". Test with the **smallest** change. If it fails, form a **new hypothesis** — do not stack fixes | The same. And the hypothesis must be **pre-registered**; anomaly investigation runs under the `exploratory` label |
| **4. Implementation** | Failing test first, then **one** fix, then a regression check | A **separate verification run** for the anomaly; it is never mixed into the main result set |

### 9.1 The three-fix rule — the most valuable piece

> *"If three or more fixes fail, stop and question the architecture itself rather
> than continuing to patch."*

**The AETHRION counterpart:**

> **If three attempts to explain an anomaly have failed, stop. What is in
> question is not the implementation — it is the `ProtocolManifest`.**
>
> → Open a `ProtocolChallenge` → evaluate a return to G2.

And Superpowers' second signal:

> *"Watch for patterns where each fix reveals new problems in different areas —
> this signals fundamental design issues."*

In research this is a **very familiar** pattern: if each fix produces a new
anomaly, the problem is not in the measurement — it is in the model or the
protocol.

**You currently have no `ProtocolChallenge` object.** After G2, the only way to
question the protocol is `material_changes` → a new `ProtocolManifest` version —
but nothing **triggers** that. The three-fix rule is the trigger.

---

## 10. `preregistration-discipline` — the research counterpart of TDD

Superpowers' hardest skill is TDD. Its AETHRION counterpart is this one, and it
sits **at the centre of your laboratory's scientific integrity**.

| TDD | Preregistration discipline |
|---|---|
| **RED:** write the failing test first | **FREEZE:** lock the `AnalysisPlanManifest` first — what each result will mean is written in advance |
| Watch the test fail **for the expected reason** | Verify that the falsification plan and stop rules are **genuinely discriminating** (severity) |
| **GREEN:** the minimum code to pass | **EXECUTE:** follow the plan **exactly** |
| **REFACTOR:** clean up while the tests are green | **REPORT:** deviations from the plan are reported **explicitly** |
| **Iron law:** code written before the test is **deleted** | **Iron law:** a result computed before the plan cannot be `confirmatory` — it is relabelled `exploratory` |
| "Keeping it for reference" is forbidden | "The preliminary analysis was exploratory" is forbidden as a justification |
| Writing the test afterwards and pretending it came first is forbidden | Writing the plan afterwards and presenting it as a preregistration is forbidden (HARKing) |

**The critical difference, and why it must be even harder here:** in code, work
written before the test *can be deleted*. In research, **you cannot un-see a
result.** So on the research side the penalty is not deletion but **permanent
relabelling**: that analysis can never be `confirmatory`, ever.

Combined with **in-principle acceptance** (`AETHRION_IDEAL_STRUCTURE.md`
Section B1), this closes publication bias.

**Verification checklist** (in Superpowers' format):

```
Before the work is complete:
  □ Every confirmatory claim has a locked AnalysisPlanManifest
  □ The plan hash was recorded BEFORE the result was produced (timestamp evidence)
  □ The falsification test was assessed for severity
  □ Every deviation from the plan is listed in the report
  □ Every analysis outside the preregistration is labelled `exploratory`
  □ Results did not influence the writing of the plan (evidence of blind analysis,
    if applied)

Cannot tick them all? Preregistration discipline has been skipped.
This claim cannot be `confirmatory`.
```

---

## 11. Integration map — summary

> **Superseded in part by Section 14.** Every row below that reads *"Add as
> `<research-skill>`"* is to be read as *"add the research skill **alongside**
> the engineering one"*, never as a replacement.

| Superpowers | Status in AETHRION | Action |
|---|---|---|
| The skill concept + `SKILL.md` + trigger discovery | ❌ absent | **Build the Skill Registry** |
| `writing-skills` (TDD for skills, rationalisation tables) | ❌ absent | **Highest meta-value — build it** |
| Iron law + evasion closure | ⚠️ "non-waivable" exists, no defence | **Add rationalisation tables** |
| Trigger ≠ procedure summary | ❌ `RoleContract.purpose` summarises a procedure | **Split out a `triggers` field** |
| Token budget | ❌ WP files 59% template, 677 words | **Produce a machine-consumable projection** |
| `test-driven-development` | ❌ | **Add as `preregistration-discipline`** |
| `verification-before-completion` | ⚠️ exists conceptually | **Add as an operational rule** |
| `brainstorming` (classification + approval gate) | ⚠️ RiskProfile exists, no "choose the heavier one" | **Add the fail-closed default** |
| `writing-plans` (placeholder ban, self-review) | ⚠️ ProtocolManifest exists | **Add the placeholder ban and self-review** |
| `subagent-driven-development` — information asymmetry | ✅ ReviewPacket | **Add "no context pasting" and hashes** |
| `subagent-driven-development` — a producer cannot call a subagent | ❌ **absent** | **The 8th independence dimension — critical** |
| `subagent-driven-development` — escalation + breaker | ❌ absent | **Add round/ledger/breaker to `DisagreementCase`** |
| `requesting-code-review` | ✅ exists | Clarify the severity tiers |
| `receiving-code-review` | ❌ **entirely absent** | **The `ProducerResponse` object — critical** |
| `systematic-debugging` + the three-fix rule | ❌ absent | **`investigating-anomalies` + `ProtocolChallenge`** |
| `dispatching-parallel-agents` | ❌ absent | **Multi-analyst discipline** |
| `using-git-worktrees` + clean baseline | ⚠️ the runtime dimension exists | **Add baseline verification** |
| `finishing-a-development-branch` | ⚠️ G8/G9 exist | **Closing checklist + full-word confirmation** |
| Ledger-based recovery | ⚠️ free-text log | **`progress.jsonl`** |

---

## 12. Implementation order

### Phase S0 — Skill infrastructure *(code, ~1 week)*

| # | Work |
|---|---|
| S0.1 | The `skills/` directory structure + the `SKILL.md` schema (Section 3) |
| S0.2 | Skill loader + version resolution + `skill_bundle_hash` |
| S0.3 | `skills_loaded` and `skill_bundle_hash` fields on `TaskContract` |
| S0.4 | The `writing-skills` skill — **this must be the first skill written** (the meta-rule) |
| S0.5 | Baseline test-run infrastructure (the RED scenarios) |

### Phase S1 — Discipline skills *(highest return)*

| # | Skill | Gap it closes |
|---|---|---|
| S1.1 | `verification-before-completion` | The operational form of the `TECH_COMPLETE` declaration |
| S1.2 | `preregistration-discipline` | HARKing, publication bias |
| S1.3 | `independence-discipline` | **A producer calling its own subagent** |
| S1.4 | `evidence-before-claim` + `scope-discipline` | Overgeneralisation |

For each: **the baseline test first** (RED), then the skill (GREEN), then the
rationalisation table (REFACTOR).

### Phase S2 — Process and review skills

| # | Work |
|---|---|
| S2.1 | `receiving-review` + **the `ProducerResponse` canonical object** |
| S2.2 | `agent-driven-research` + round/ledger/breaker on `DisagreementCase` |
| S2.3 | `investigating-anomalies` + `ProtocolChallenge` |
| S2.4 | `framing-research` + fail-closed classification |
| S2.5 | `writing-protocols` + `writing-analysis-plans` |
| S2.6 | `finishing-a-project` + full-word confirmation |

### Phase S3 — Research and metascience skills

| # | Work |
|---|---|
| S3.1 | `building-review-packets` (as a program) |
| S3.2 | `dispatching-parallel-analysts` |
| S3.3 | `searching-literature`, `screening-sources`, `extracting-evidence`, `anchoring-spans`, `curating-zotero` |
| S3.4 | `calibrating-confidence`, `measuring-agreement`, `injecting-controls` |

### Phase S4 — The communication layer

| # | Work | Note |
|---|---|---|
| S4.1 | **Notification Broker** — a Tool Broker subclass; policy + DLP + idempotency | Transport: Apprise |
| S4.2 | The channel registry + the **data-class ceiling** table, enforced in code | D3/D4 → contentless trigger |
| S4.3 | `notifying-humans`, `escalating-and-paging`, `publishing-digests` | outbound |
| S4.4 | **Signed, time-limited, single-use deep links** + an authenticated decision surface | `routing-decision-requests` |
| S4.5 | The quarantine chain: sender verification → attachment scanning → `<untrusted-external-content>` | `receiving-external-messages` |
| S4.6 | G10 feed connections (Crossref / Retraction Watch / CVE / registries) | `monitoring-external-feeds` |
| S4.7 | OSF preregistration + Zenodo DOI + ORCID | `submitting-external-records` |

**The order matters:** no channel is connected before S4.1–S4.2 (broker plus
ceiling) is complete. Connecting a channel first and adding the policy afterwards
makes a data-class violation permanent.

**Suggested first channels:** ntfy (self-hosted) plus Telegram. Reason: ntfy can
carry up to D2 and runs on your own server; the Telegram bot API is the
lowest-friction interactive channel. WhatsApp is left **for last**.

### Phase S5 — Plan projection

| # | Work |
|---|---|
| S5.1 | A 130-WP → machine-consumable task-brief generator (**mechanical, not a prompt**) |
| S5.2 | The `progress.jsonl` append-only ledger |
| S5.3 | The WP ↔ skill mapping (which skills execute which WP) |
| S5.4 | New WPs: the Notification Broker, the Metascience plane, the added roles |

---

## 13. The five most critical conclusions

1. **`ProducerResponse` does not exist.** Nothing verifies whether the conditions
   of a `CONDITIONAL_PASS` verdict were met. The review process is currently
   **open-ended**. *(Section 8)*

2. **A producer calling its own helper is not forbidden.** Without that
   prohibition, the other seven dimensions of the IndependenceMatrix are void.
   *(Section 5.3)*

3. **"Non-waivable" is a declaration, not a defence.** A model can always produce
   a plausible evasion. Without rationalisation tables, non-waivable rules are
   brittle. *(Section 2.2)*

4. **Disagreement resolution has no round limit and no breaker.** Open findings
   can vanish silently. *(Section 5.2)*

5. **The commissioning plan is not agent-consumable.** 59% template, no triggers,
   no iron laws. The plan of a laboratory to be operated by models must be
   loadable into a model. *(Section 2.4)*

---

## 14. Correction, 2026-08-22 — two skill families, one open format

> **Decision taken.** Sections 2–13 above treat every Superpowers skill as
> something to be *converted* into a research skill. Section 11 states this
> literally: `test-driven-development` → *"Add as `preregistration-discipline`"*.
> **That is now overruled.** The research adaptations **extend** their engineering
> counterparts; they do not replace them.

### 14.1 Why the replacement reading was wrong

AETHRION does two different jobs, and only one of them is research.

| Job | Who does it | Discipline needed |
|---|---|---|
| **Building AETHRION** — Temporal workflows, the Tool Broker, the Source Registry, the Claim Ledger, harness adapters | agents working in this repository, today | **engineering**: TDD, systematic debugging, worktrees, code review |
| **Doing research through AETHRION** — protocol, evidence, claim, review, publication | agents working inside a runtime that does not exist yet | **scientific**: preregistration, evidence anchoring, blind review |

The evidence that the replacement reading was wrong was visible in the
repository at the time this correction was written: **all 12 engineering skills
were absent from `skills/`**, while AETHRION was itself being built by agents. The
laboratory had written down how to conduct research and thrown away how to build
the laboratory.

> **State after implementation.** 11 upstream engineering skills are vendored
> verbatim; 3 upstream procedures (`using-superpowers`, `writing-skills`,
> `verification-before-completion`) are represented by AIRL router/shared
> adaptations; the registry holds **52 conformant skills**. The paragraphs below
> describe the situation this decision responded to, not the situation today.

### 14.2 The principle

> **Engineering skills govern how AETHRION software is built. Scientific skills
> govern how research is conducted through AETHRION. Shared discipline skills
> govern both. Research adaptations extend, rather than replace, their
> engineering counterparts.**

One task may draw on both families. Building the Claim Ledger is engineering work
(`test-driven-development`) that also carries evidence obligations
(`evidence-before-claim`, `independence-discipline`).

### 14.3 The families are not symmetric in urgency

| | Engineering family | Research family |
|---|---|---|
| Consumer today | **yes** — this repository, this session | none |
| Waiting on | nothing | the Task Compiler and LangGraph runtime (WP-046/047, unbuilt) |
| Can be baseline-tested | now | only once a runtime can load it |

`writing-skills` states the iron law *"no skill without a failing baseline test
first."* The engineering family is currently **the only family that law can be
applied to.** The research family stays written-but-untested — deliberately, and
recorded as such, not by omission.

### 14.4 Two classification axes, not one

Section 2 folds Superpowers' execution-complexity classes into the research
classes. They are orthogonal, and a confirmatory study can be a bounded task:

```yaml
research_mode:  exploratory | replication | confirmatory   # what the claim may assert
execution_path: spike | bounded | architectural            # how heavy the execution is
```

Both are classified; when in doubt, the heavier value is taken on **each** axis
(see `AETHRION_IDEAL_STRUCTURE.md` E4).

### 14.5 Conform to the Agent Skills open format

`SKILL.md` is no longer a Superpowers convention — it is an **open standard**
(`agentskills.io`, opened by Anthropic in December 2025) implemented by Claude
Code, Codex, OpenCode, Cursor, Copilot **and Hermes Agent** — that is, by every
harness AETHRION targets, including the one in use today.

**Consequence for WP-048:** per-harness bootstrap adapters are largely
unnecessary. Conformance to the format *is* the bootstrap.

At the time of this decision all 38 skills were **non-conformant**. The spec
permits exactly six top-level frontmatter fields — `name`, `description`,
`license`, `compatibility`, `metadata`, `allowed-tools` — and every other key
belongs under `metadata` as a string map. The files then declared `version`,
`gates`, `roles`, `assurance_classes`, `emits`, `mechanical_checks`,
`non_waivable`, `requires_skills`, `data_class_ceiling` and `tool_effect` at the
top level. **All 52 skills now conform**, and `scripts/validate_skills.py`
keeps them that way.

The required shape:

```yaml
---
name: preregistration-discipline
description: Use when any analysis is about to run, when a confirmatory claim is
  being drafted, or when analysis choices are being changed after seeing results
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"          # engineering | scientific-research | shared
  airl.origin: "airl-native"                  # airl-native | superpowers | upstream
  airl.derived_from: "superpowers:test-driven-development"
  airl.upstream_commit: "<sha>"
  airl.gates: "G2,G4,G5,G6"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "writing-analysis-plans"
  airl.emits: "AnalysisPlanManifest,ClaimVersion"
  airl.mechanical_checks: "plan_hash_precedes_result_timestamp"
---
```

Nothing is lost: `skill_bundle_hash` still hashes the file, and the AIRL fields
stay machine-readable under a namespaced prefix. What is gained is that the same
directory loads unmodified in every harness, and `skills-ref validate` becomes a
mechanical check that CI can run.

**The `derived_from` / `upstream_commit` pair answers a question that has no
answer today:** when `obra/superpowers` changes, which AIRL skills must be
re-examined?

### 14.5.1 The reporting family, added 2026-08-22

Three skills carry document production, and they compose rather than nest:
**`authoring-research-documents`** conducts the pipeline and loads twelve
reference modules on demand; **`reporting-results`** owns what a result permits
you to say; **`producing-figures`** owns figures, with its long-form methodology
in a reference module. The router skill stays at 131 lines precisely because the
handbook lives beside it rather than inside it — which is the progressive
disclosure the Agent Skills format is built for.

### 14.6 What follows from this decision

| # | Work | State |
|---|---|---|
| 1 | Migrate all skills to spec-conformant frontmatter; enforce it mechanically | ✅ **done** — 52/52, `scripts/validate_skills.py` |
| 2 | Add the engineering family — installed from upstream with a pinned commit, **not** re-authored as AIRL prose | ✅ **done** — 11 vendored @ `b36e0829` |
| 3 | `using-aethrion` becomes the router: family first, then `research_mode` × `execution_path` | ✅ **done** |
| 4 | Skill binding into `TaskContract` | 📐 **specified** in WP-013; not built |
| 5 | Reflect the skill layer into the sealed commissioning plan | ✅ **bound in baseline v1.0** — WP-013/043/047/048 and ACC-41–46; re-sealed at 202 files |
| 6 | Behaviour-test the skills — RED baselines, pressure, triggers, compaction | ❌ **not started**; WP-043 owns it |

---

## Closing

Superpowers is a coding methodology. But the problem it solves is **the same** as
yours: *how do you trust the work an agent produced?*

And its answer points the same way as your architecture's: **information
asymmetry, independent review, mechanical verification, human authority.** That
two designs arrived independently at the same conclusions — the gate ceremony
flexes while the record does not; fresh context; a timeout is not an
auto-approval — is evidence that your architecture is on the right axis.

---

## 15. Overlap audit, 2026-08-23 — a second methodology, and one real gap

### Why the audit happened

`obra/superpowers` is a **software engineering** methodology, and §14 records how
this registry took its discipline and layered research semantics on top. In 2026
a second upstream appeared that solves the nearer problem directly:
**K-Dense Science Superpowers**, MIT-licensed, sixteen skills, adapting the same
architecture to computational science with **pre-registration in place of
test-driven development** — the same substitution `preregistration-discipline`
makes here, arrived at independently.

Two paths were open. Import it as a parallel family, which produces two skills
for every procedure and a router that has to choose between them. Or audit
skill-by-skill and keep one local skill per procedure. **The second, and the
audit is below** so the conclusion is checkable rather than asserted.

### The mapping

| Upstream skill | Local counterpart | Verdict |
|---|---|---|
| `framing-research-questions` | `framing-research` | covered |
| `surveying-prior-work` | `searching-literature` + `screening-sources` | covered, and split finer here |
| `establishing-feasibility-first` | — | **gap** — see below |
| `designing-the-analysis` | `writing-analysis-plans` | covered |
| `preregistering-analysis` | `preregistration-discipline` | covered; the local iron law is stricter |
| `subagent-driven-analysis` | `agent-driven-research` | covered |
| `executing-analysis` | `executing-experiments` | covered |
| `dispatching-parallel-investigations` | `dispatching-parallel-analysts` | covered |
| `investigating-anomalous-results` | `investigating-anomalies` | covered |
| `verifying-results-before-claiming` | `verification-before-completion` + `evidence-before-claim` | covered, and split finer here |
| `requesting-red-team-review` | `requesting-review` + `adversarial-reviewing` | covered, and split finer here |
| `receiving-critical-review` | `receiving-review` | covered |
| `setting-up-reproducible-analysis` | `using-isolated-environments` | covered |
| `reporting-and-archiving-findings` | `reporting-results` + `finishing-a-project` | covered, and split finer here |
| `writing-science-skills` | `writing-skills` | covered |
| `using-science-superpowers` | `using-aethrion` | covered |

**Fifteen of sixteen already had a counterpart.** That is the audit's main
result, and it is worth stating plainly because the opposite result was the
expected one: two projects solving the same problem converged on nearly the same
procedure list.

### The gap: feasibility as its own mode

`establishing-feasibility-first` had no counterpart, and the reason it matters
is not that a procedure was missing. It is that **feasibility was being treated
here as a kind of exploratory work**, and the two have different claim ceilings.

A feasibility run answers *does this execute*. It routinely also produces a
number — real, yours, and predicted by nothing. The most common way a research
record goes wrong is that this number is written up afterwards as though it had
been. Exploratory work can be reported as exploratory; feasibility work
producing a headline result is a category error that only becomes visible if the
mode was named beforehand.

### What was done, and what was deliberately not

**Not done: a fifty-third skill.** Skill count is not a success metric, and the
first question for any new procedure is whether an existing skill can absorb it.
This one could.

**Done:** `framing-research` now classifies on two axes rather than one —
assurance class (*how much scrutiny*) and study mode (*what may be claimed*) —
with `FEASIBILITY` as its own mode, a `StudyModeRecord` emitted before the first
result exists, and the rule that the claim ceiling moves one way only.
`preregistration-discipline` carries the matching rule at the other end: a
feasibility outcome may inform a confirmatory protocol and can never be the
outcome that protocol confirms. WP-142 makes it a contract; ACC-56 tests it.

### What the audit did *not* do, and why

**No local skill was relabelled as derived from this upstream.** These skills
were written independently, and `ADR-004` forbids claiming a derivation without
a pinned commit — there is no network access in this environment to pin one, and
inventing a digest to satisfy a metadata field is exactly the failure the field
exists to prevent. `airl.derived_from` therefore still names only
`obra/superpowers`, which is genuinely where the eleven vendored skills came
from and where the pin is real.

**The domain catalogue was not imported.** The same organisation publishes 161
scientific skills across eighteen domains. Its repository licence is MIT while
each skill declares its own licence in its `SKILL.md`, so a repository-level
assumption would be wrong per file. It is recorded as `DEFER` in
`provenance/upstreams.json`: importing a bioinformatics skill before there is a
bioinformatics project adds surface without adding capability, and when one is
imported the licence in that skill's own file governs.

### What this audit does not establish

That any of these skills works. Fifteen counterparts existing is a statement
about coverage, not about behaviour — **none of the 52 has a behaviour
baseline**, which is WP-043's job and is not started. An audit that finds good
coverage of untested procedures has found good coverage of untested procedures.

---

## 16. Two disciplines, composable — the decision, 2026-08-23

`ADR-012`. Section 15's audit answered *does the scientific family duplicate an
upstream methodology*. This section answers a question that arrives immediately
afterwards and has the opposite shape: **now that the scientific mechanisms are
very visible, should the eleven engineering skills be folded into them?**

No. And the reason is not symmetry or attribution — it is that most of what this
system will actually produce is **code**.

### 16.1 Where the science's failure modes actually live

Evaluators, preprocessing, simulation harnesses, reproduction packages, analysis
scripts. Every one is a place where an ordinary software defect becomes a
scientific error with a plausible number attached, and none of them is caught by
a scientific procedure. A p-value computed correctly from a wrongly filtered
dataframe is a correct computation of the wrong thing.

The engineering discipline is not supporting work around the science. It is where
a large fraction of the science's failure modes live.

### 16.2 The four pairs that get conflated

| Engineering | Scientific | Why the substitution fails |
|---|---|---|
| `test-driven-development` | `preregistration-discipline` | Both commit before seeing an outcome, and that is where the resemblance stops. A test fixes what the code must **do**; a preregistration fixes what a result will **mean**. Passing tests on an analysis reshaped after seeing the data is a correct implementation of a compromised study |
| `requesting-code-review` | `requesting-review` · `adversarial-reviewing` | Code review asks *is this correct and maintainable*. Scientific review asks *does the evidence support the claim, and what would show it does not*. A reviewer who approved the diff has said nothing about the inference |
| `systematic-debugging` | `investigating-anomalies` | Debugging assumes the system is wrong and the expectation is right. Anomaly investigation cannot assume that — **the surprising result may be the finding**, and treating every anomaly as a bug is how a discovery gets fixed |
| `dispatching-parallel-agents` | `dispatching-parallel-analysts` | One decomposes work that has a right answer and merges. The other runs independent analyses *because* the answer is unknown, and its output is a spread rather than a merge |

### 16.3 What a coding-science task compiles to

Both families, in one `TaskContract`, with neither aliasing the other:

```
preregistration-discipline · writing-analysis-plans · executing-experiments
evidence-before-claim · scope-discipline                    ← scientific
using-git-worktrees · test-driven-development
systematic-debugging · requesting-code-review               ← engineering
verification-before-completion · independence-discipline    ← shared
```

The junction between the two loops is the only interesting part: a code artifact
becomes **eligible to produce scientific evidence** when the engineering loop has
closed on it — specification, worktree, RED, implementation, GREEN, review, CI,
attestation, signed artifact. Before that it is a draft, and a result from a
draft is a result from unknown code. WP-107 proves that arrow end to end; WP-154
adds the check that afterwards keeps the frozen specification and the running
code in agreement (`ADR-018`).

### 16.4 What this section does not establish

That either family works. The engineering eleven are vendored at a pinned commit
and are not rewritten here; the scientific thirty-one were audited for coverage
in §15. **Neither has an execution baseline** — routing is measured since v1.3.1
by `scripts/check_skill_baseline.py`, but whether loading a skill changes what an
agent does is still unmeasured, and that is WP-043's job, extended by
WP-154 to cover engineering discipline under deadline pressure, and it has not
started. Coverage of untested procedures is still coverage of untested
procedures.
