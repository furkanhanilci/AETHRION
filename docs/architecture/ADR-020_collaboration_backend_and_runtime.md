# ADR-020 — The Collaboration Backend and the Agent Runtime Are Not the Architecture

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | Where collaboration transport and agent-runtime hosting sit relative to scientific authority, and what neither of them may ever decide |
| Sibling documents | `ADR-003` (trusted control and policy) · `ADR-004` (mechanism assimilation) · `ADR-011` (multi-agent execution invariant) · `ADR-012` (dual disciplines) · `ADR-013` (blackboard and sparse communication) · WP-047 · WP-048 · WP-148–150 · WP-154 · WP-159 |
| Status | **ACCEPTED — 2026-08-24.** Boundary decided; no backend is integrated, no runtime is qualified, and no adapter exists |
| Date | 2026-08-24 |

**In one paragraph.** A large part of what the collaboration plane needs is not
scientific: identities, rooms, message transport, presence, process attachment,
a human-and-agent workspace. Building that here would consume most of the
collaboration budget and differentiate nothing. Something that already does it
well is therefore worth adopting — and the moment such a thing is adopted, the
question stops being *does it work* and becomes *what has it quietly been given
authority over*. This record fixes that boundary before any code moves: AETHRION
owns scientific semantics, cohort compilation, communication policy, evidence and
human decision; a collaboration backend carries messages; a runtime executes
cognition; and neither of them may decide anything.

---

## 1. The decision

> **Collaboration transport and agent-runtime hosting are accessed through
> AETHRION-owned contracts and are replaceable behind them.** A
> `CollaborationBackend` carries what the Task Compiler decided; an
> `AgentRuntime` executes a cognitive function that was chosen before the runtime
> was. Neither owns canonical scientific state, gate authority, role semantics or
> human decision. **Buzz is the first backend candidate and Hermes the preferred
> runtime profile; both are named, neither is assumed.**

The test that decides whether an integration is correct is stated once and is not
negotiable:

> **If the backend disappears, which truths disappear?** Rooms, presence, message
> history projection and operational coordination are acceptable losses. Gate
> state, claims, evidence spans, verified values, protocol freeze, human
> decisions, experiment lineage, reproduction records, publication assertions and
> accepted engineering artifacts are not. If any of those depends on backend
> state, the integration is architecturally wrong — not fragile, wrong.

---

## 2. The mistake this record exists to refuse

The failure mode is a single sentence:

```text
AETHRION = Buzz + some scientific prompts
```

It is attractive because it is nearly true at the level of *mechanics*. A
collaboration substrate can host agents, route messages, attach runtimes, manage
workspaces and show a human what happened. Almost everything in the paragraph
above is genuinely solved.

What it does not contain is the entire reason this system exists: which evidence,
having passed which control, licenses which claim. A backend that hosts a cohort
has no opinion about whether the cohort was epistemically sufficient. A runtime
that reports `completed` has no opinion about whether the work is acceptable. A
room full of agreeing agents is not a finding, and five identities on one model
and one context are **one** contribution — `ADR-011`, unchanged by anything here.

So the relationship is the other way round.

```text
AETHRION   scientific authority · cohort semantics · communication policy
           evidence · assurance · human decision
    │
    │ compiles what collaboration must happen
    ▼
CollaborationBackend contract          ← AETHRION owns this
    │
    ▼
Buzz            first candidate — not yet qualified, and replaceable
    │
    ▼
AgentRuntime contract                  ← AETHRION owns this too
    │
    ▼
Hermes · Codex · Claude Code · Buzz Agent · future runtimes
    │
    ▼
AETHRION skills + Superpowers discipline
    │
    ▼
ToolIntent → Tool Broker → PolicyDecision → Execution Broker
```

Two contracts, both AETHRION's, with the adopted thing sitting *under* each.

---

## 3. Five concerns, five owners

The architecture stops using "agent framework" as though one component owns every
layer, because that phrase is what lets a transport acquire authority.

| Concern | Owner | Examples |
|---|---|---|
| Scientific authority and lifecycle | **AETHRION** | gates, `ClaimVersion`, `DecisionRecord`, protocol freeze |
| Collaboration substrate | **backend** (Buzz first) | identities, rooms, messages, presence, runtime attachment |
| Runtime / harness | **runtime** (Hermes, Codex, Claude Code, Buzz Agent) | the local agent loop, model interaction, tool-call formatting |
| Cognitive and task orchestration | **AETHRION** Task Compiler, with LangGraph where the profile needs it | cognitive-function decomposition, bounded reasoning |
| Engineering discipline | **Superpowers** plus AETHRION's shared family | planning, worktrees, TDD, review, verification |

The sentence worth remembering:

> The backend says **where and who** collaborates. The runtime says **how** an
> actor executes. Superpowers says **how software work is conducted**. AETHRION
> says **what any of it is worth**.

---

## 4. Role is not cognitive function is not model is not runtime is not identity

This is the conflation the adoption invites, and it is worth naming all five
levels because collapsing any adjacent pair breaks something different.

| Level | What it is | What breaks if it is collapsed into the next |
|---|---|---|
| `RoleContract` / `RoleBinding` | governance authority — who may decide what | a backend identity starts implying authority it was never granted |
| Cognitive function | the epistemic job — `Statistician`, `Adversarial Reviewer` | independence stops being measurable, because the profile has nothing to measure |
| Model profile | the admitted model and its snapshot | requalification silently stops applying |
| Runtime profile | the harness executing the loop | "we used Hermes" starts being offered as a description of the method |
| Backend identity | the operational actor in a room | attribution is mistaken for authorisation |

**`Hermes` is not a role.** `Statistician` is a cognitive function, and it may run
on any qualified runtime without its scientific meaning changing. The Task
Compiler emits cognitive functions, capability requirements, independence
constraints and context requirements — never `"a Hermes agent"` — and a separate
runtime selector maps those requirements onto a qualified profile afterwards.

The order matters more than the mapping: **choose the cognitive function first,
the runtime second.** Selecting a runtime first and then inventing roles that fit
it is how a cohort comes to be shaped by a harness.

---

## 5. What a backend may never decide

`ADR-003` already says content crosses the trust boundary and authority does not.
A collaboration backend is where that rule meets a concrete temptation, because
the backend is fast, present and full of text that looks like instructions.

- **A message is not an instruction, and messaging is not authorisation.** A
  receiving actor still acts under its `RoleContract`, its policy and its current
  task. A message from another agent carries no privilege merely because the
  sender holds an agent identity.
- **Backend text is untrusted data.** It sits on the data-plane side of `ADR-003`
  unless a trusted control component produced it under a typed contract.
- **An operational identity is not a `RoleBinding`.** Cryptographic identity
  supports attribution. It does not establish that an actor currently holds a
  governance role, and attribution and authorisation are different questions.
- **There is no shortcut into the evidence chain.** `backend message →
  EvidenceSpan` does not exist. An agent reporting external evidence produces a
  typed message carrying a *pointer*, which enters through source ingestion and
  `SourceRepresentation` like everything else. An agent reporting a result does
  not thereby produce a `RawEvaluatorArtifact`.
- **An approval is not a decision.** A backend may present a decision card and
  collect a human action; the canonical decision is written through the Decision
  Service as a signed `DecisionRecord`. **A backend approval cannot move G8 or
  G9.**
- **A room is not the blackboard.** `BlackboardEntry` is an AETHRION projection
  over canonical artifact pointers. A room can be destroyed and rebuilt from
  AETHRION state; the reverse is not true and must never become true.

---

## 6. Convenience is the attack surface, and round zero is where it shows

The backend makes one thing very easy: put every actor in one room. That single
convenience would silently undo `ADR-011` §4 and `ADR-013` at once — round-zero
independence, the sealed `InitialPositionArtifact`, the sparse topology and the
delta-only discipline all assume that an actor **cannot** see what it has not been
given.

So topology is compiled, not emergent:

```text
actor A → actor B : CHALLENGE, REQUEST
actor B → actor A : EVIDENCE, CORRECTION
actor C → synthesis : SEALED_POSITION, and only after embargo release
```

The adapter's job is to realise that graph. **If the backend cannot enforce the
required isolation, that is a backend capability failure and the task does not
run** — it is never a reason to relax the graph. A fully connected room remains
legal in exactly one situation: as the explicit benchmark control arm that
`ADR-013` requires optimisation to be measured against.

The same rule governs context. **Room history is not a `ContextProjection`.** The
Context Projector assembles the role contract, the task contract, admissible
evidence, the compiled skill bundle, the peer deltas the current round permits and
the memory that survives masking. Appending a channel transcript would violate
the cost discipline and the independence discipline in one move.

---

## 7. Bootstrap is a profile, not a stage that ends by itself

A backend plus a runtime plus worktrees is enough to do real work *before* the
Tool Broker, the Execution Broker and the policy set exist. That is genuinely
useful, and it is exactly how a temporary shortcut fossilises.

Everything that trades a control for progress is therefore named, scoped and
given an owner:

| Bootstrap shortcut | Permanent replacement |
|---|---|
| backend or manifest coordination of package steps | Task Compiler under Temporal-controlled process |
| direct agent shell in a worktree | `ToolIntent` → Tool Broker → `PolicyDecision` → Execution Broker |
| a room used as a coordination scratchpad | `BlackboardEntry` semantics with a backend projection |
| a flat roster manifest | `AgentCohortRecord` + `CollaborationDeploymentPlan` |
| runtime-native retries | the failure taxonomy and AETHRION execution policy |
| review conducted in chat | canonical `ReviewRecord` and `DecisionRecord` |

A shortcut used under `BOOTSTRAP_EXECUTION_PROFILE` is **retired**, not
reclassified as production-ready because it kept working.

---

## 8. Consequences

- **Two contracts are added to the plan as refinements, not additions.** WP-148
  already had to deliver a collaboration plane; naming the boundary it is
  delivered behind is *how*, not *what*. `CollaborationBackendProfile`,
  `CollaborationDeploymentPlan` and `AgentRuntimeProfile` are specified in
  WP-047, WP-048 and WP-148 and the finish line does not move.
- **The Task Compiler gains a refusal set.** No qualified runtime, a backend that
  cannot enforce round-zero isolation, a skill bundle that cannot be materialised,
  an impossible verifier independence, or a budget that would only fit by
  dropping required cohort or assurance — each is a compile-time refusal rather
  than a warning.
- **Nothing is adopted without an authority boundary.** Buzz, `buzz-acp`, Hermes,
  Buzz Agent and the alternative harnesses are registered in
  `provenance/components.json`; the mechanisms taken from the same project are
  registered separately in `provenance/upstreams.json`. The registers are
  projected into the packages that execute them.
- **A prototype upstream is pinned or it is not used.** Buzz was prototype-grade
  and moving at review, so a floating `main` is not an acceptable dependency:
  WP-159 tracks the backend, the ACP surface, the runtime profiles and any
  adapted source, and an upgrade that fails characterisation is quarantined.
- **This record decides a boundary and nothing else.** No backend is integrated,
  no runtime is qualified, no adapter exists, and no characterisation suite has
  been written. Everything above is `SPECIFIED`.

---

## 9. What this record deliberately leaves open

- the production pin, deployment topology and whether the first backend stays the
  only one;
- how far Hermes is preferred once cost and capability data exist per role;
- the runtime selection algorithm beyond a deterministic first policy;
- Persona Pack packaging depth, and signed identity/delegation protocols, both of
  which are recorded as `PATTERN` or `DEFER` rather than adopted;
- every user-interface question, which stays out of V1 — `docs/V2_CANDIDATES.md`.

---

## 10. Decision

**Accepted.** Collaboration transport and runtime hosting are adopted behind
AETHRION-owned contracts, with the authority boundary stated before any code
moves. Buzz is the first backend candidate and Hermes the preferred runtime
profile; both are replaceable, and the architecture is only correct while
removing either one loses no scientific truth.

## Provenance

Prepared from the Buzz/ACP/Hermes architecture delta reviewed against AETHRION
`c750946d0ee08e58e3090f979630743aafcf9696` and a Buzz baseline of
`0720f5380ce8a6c050afac159f8462c06cd51ab5`.

**The licence was read at the source on 2026-08-24**, from a session with network
access. The `LICENSE` file at the pinned tree is the unmodified Apache License
2.0 — nine numbered sections, the standard appendix, no non-commercial clause, no
field-of-use restriction and no added term — under `Copyright 2026 Block, Inc.`
The delta's reported baseline commit was verified to exist, and the crates it
described (`buzz-acp`, `buzz-agent`, `buzz-persona`, `buzz-relay`,
`buzz-workflow`) were confirmed present.

Between the decision and that reading, the Harbor Orchestra manifest was
registered as `PATTERN` rather than the `DIRECT_ADAPT` the delta proposed,
because `check_upstream_lineage.py` R7 refuses a direct adaptation under an
unverified licence. The refusal held for exactly as long as it should have, and
`ASM-060` now carries the verified licence, the pin and a named file list. **It
is still `PROPOSED`**: no characterisation suite exists, and R5 refuses
`ADAPTING` until one does.

One fact from that reading belongs in the decision rather than only in the
register. **The pinned tree is 465 commits ahead of `v0.5.2`**, the latest
release tag — it was the tip of `main` when read. The mechanism analysis was
performed against that tree, which is why it is the pin; it also means the
reviewed behaviour is unreleased development code, and choosing a production pin
is a separate decision under WP-159.
