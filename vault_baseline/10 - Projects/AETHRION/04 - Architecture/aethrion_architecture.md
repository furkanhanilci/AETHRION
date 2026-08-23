---
title: "AETHRION — Architecture Reference"
cssclasses:
  - aethrion-reference
type: reference
category: architecture
summary: "AETHRION — Agentic Intelligence Research Layer is an evidence-centred research operating system: AI agents perform bounded research tasks, deterministic systems verify whatever can be verified mechanically, independent assurance challenges what survives, humans retain scientific decision authority,"
source: "docs/architecture/AETHRION_ARCHITECTURE.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
---

> [!info] Generated view
> This note is generated from `docs/architecture/AETHRION_ARCHITECTURE.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

<p align="center">
  <img src="../assets/branding/aethrion-logo.png" alt="AETHRION" width="110">
</p>

# AETHRION — Architecture Reference

| Field | Value |
|---|---|
| Document type | Architecture reference — the single explanatory entry point |
| Audience | A human or a model arriving with no prior context |
| Naming | **AETHRION — Agentic Intelligence Research Layer.** `AIRL` is the abbreviation of the descriptor and survives as a technical term; see `../branding.md` |
| Sibling documents | `../branding.md` (naming) · `AETHRION_COMPONENT_REUSE.md` (what is adopted) · `AETHRION_ROLES.md` (role definitions and authority flows) · `AETHRION_IDEAL_STRUCTURE.md` (proposed additions) · `AETHRION_SKILL_LAYER.md` (how agents work) · `AETHRION_ROLE_MODEL_ASSIGNMENT.md` (who executes what) · `AETHRION_EXTERNAL_STANDARDS.md` (what is adopted rather than invented) |
| Date | 2026-08-22 |
| Status | Describes the **target architecture** and, in §10, exactly how much of it exists |

**In one paragraph.** AETHRION — Agentic Intelligence Research Layer is an evidence-centred research operating system: AI agents perform bounded research tasks, deterministic systems verify whatever can be verified mechanically, independent assurance challenges what survives, humans retain scientific decision authority, and every material claim stays traceable from source span and experiment through to publication and later revision. This document is the explanatory entry point to that design — the principle, the evidence chain, the planes, the G0–G10 lifecycle, the role and skill layers, and how evidence is signed. §10 states how much of it exists, and the answer is: one vertical slice.

> **Read §10 before believing §§2–9.** This document describes a design. One
> vertical slice of it runs. The distance between the two is the most important
> fact about this repository, and it is stated in one place so that no section
> above can be mistaken for a status report.

---

## 1. What AETHRION is

A normal AI research assistant is a pipeline from a question to an answer:

```mermaid
flowchart LR
    U["Human question"] --> L["LLM"] --> S["Search + summarise"] --> A["Answer"]
    style A fill:#FBEFD6,stroke:#E69F00,color:#000
```

Whatever comes out is trusted because a capable model produced it. AETHRION
starts from the opposite assumption: **a fluent, confident, well-cited, entirely
wrong result is the normal failure mode of a capable model**, and no amount of
model capability detects it from the inside.

So AETHRION is not an assistant. It is a **laboratory**: a system in which model
output is a *hypothesis* that must survive mechanical verification, independent
review, and a human decision before it is allowed to become a claim — and where
every claim stays traceable to the exact sentence in the exact source it came
from, and stays revisable after publication.

> **AETHRION is an evidence-centred research operating system in which AI agents
> perform bounded research tasks, deterministic systems verify what can be
> verified mechanically, independent assurance challenges the results, humans
> retain scientific decision authority, and every material claim remains
> traceable from source and experiment to publication and subsequent revision.**

---

## 2. The one principle everything else follows from

> **Agents produce · machines verify · humans decide.**

These three roles are never allowed to blur into one another.

```mermaid
flowchart TD
    A["AGENT<br/>produces<br/><i>'I think this is right'</i>"]
    M["MACHINE<br/>verifies what is verifiable<br/>hashes · statistics · entailment · independence"]
    H["HUMAN<br/>decides<br/><i>'I accept this claim on this evidence'</i>"]

    A -->|"not sufficient on its own"| M
    M -->|"passes only what survives"| H
    H -->|"decision recorded, never delegated"| R["DecisionRecord"]

    M -.->|"fails → back with a finding, never a waiver"| A

    style A fill:#DDEAF4,stroke:#0072B2,color:#000
    style M fill:#E0F3EC,stroke:#009E73,color:#000
    style H fill:#F7E2D6,stroke:#D55E00,color:#000
    style R fill:#F5E4EE,stroke:#CC79A7,color:#000
```

The failure mode this defends against is the ordinary multi-agent pattern:

```
Agent A produces  →  Agent B reads it  →  Agent B says "looks good"  →  accepted
```

AETHRION does not count that as verification. Two models from the same family
share training lineage and therefore share errors; agreement between them is
correlation, not confirmation. This is why **independence must be measured**
(§7.3) rather than asserted.

### 2.1 The assignment principle — verification asymmetry

For every step there is exactly one question:

```mermaid
flowchart TD
    Q{"Can this step be<br/>verified mechanically?"}
    Q -->|Yes| M["The mechanical check runs FIRST<br/><b>and the model cannot override it</b>"]
    Q -->|No| P["A model may produce —<br/>but its output must be <b>falsifiable</b>"]
    P --> F{"Can the output be reduced to<br/>something a machine can check?"}
    F -->|No| S["It is a <b>suggestion</b>, not evidence"]
    F -->|Yes| M

    style M fill:#E0F3EC,stroke:#009E73,color:#000
    style S fill:#FBEFD6,stroke:#E69F00,color:#000
```

**A model is a hypothesis generator, not a verifier.**

---

## 3. The evidence chain

Nothing becomes knowledge by being asserted. It becomes knowledge by surviving a
chain in which **every link is addressable**:

![The evidence chain and how much of it exists](figures/aethrion_evidence_chain.svg)

*Figure 2 — The chain, its revision loop, and the attestation that makes a link
admissible. Solid nodes are implemented; hollow dashed nodes are designed and not
built. Nine of the ten links are hollow.*

```mermaid
flowchart LR
    S["Source<br/><i>the paper</i>"] --> SR["SourceRepresentation<br/><i>parsed, hashed</i>"]
    SR --> ES["EvidenceSpan<br/><i>the exact sentence</i>"]
    ES --> C["ClaimVersion<br/><i>what we assert</i>"]
    C --> R["ExperimentRun<br/><i>what we ran</i>"]
    R --> RV["Review<br/><i>who challenged it</i>"]
    RV --> RP["Reproduction<br/><i>does it hold again</i>"]
    RP --> D["DecisionRecord<br/><i>a human accepted it</i>"]
    D --> P["Publication"]
    P --> MO["Monitoring<br/><i>does it still hold</i>"]
    MO -.->|"supersede / revise / retract"| C

    style ES fill:#E0F3EC,stroke:#009E73,color:#000
    style D fill:#F7E2D6,stroke:#D55E00,color:#000
    style MO fill:#F5E4EE,stroke:#CC79A7,color:#000
```

Two properties matter more than the chain itself:

1. **It is traversable in both directions.** From a published sentence you can
   reach the source span; from a retracted source you can reach every claim that
   depended on it. This is what makes G10 possible at all.
2. **The loop closes.** A claim is never permanently true. Monitoring feeds back
   into the claim, and `VERIFIED` is explicitly *not* an irreversible state.

### 3.1 Where a number comes from

The chain above is drawn at the level of *kinds of thing*. Two of its links are
where a research system is most easily fooled, and both were under-specified
until `ADR-007` and `ADR-009`.

The first is a **number**. A result in a paper is normally a string somebody
typed, and a string is exactly as convincing whether it was measured or invented.
So a number is a record with a lineage:

```mermaid
flowchart LR
    CC["candidate<br/><i>producer zone</i>"] -->|signed commit| EV["frozen evaluator<br/><i>evaluator zone</i>"]
    EV --> RAW["RawEvaluatorArtifact<br/><i>immutable, stored before<br/>any agent reads it</i>"]
    RAW --> VV["VerifiedValue<br/><i>metric, aggregation, seeds,<br/>uncertainty, scope</i>"]
    VV --> PA["PublicationAssertion"]

    style RAW fill:#F7E2D6,stroke:#D55E00,color:#000
    style VV fill:#F7E2D6,stroke:#D55E00,color:#000
```

Two properties carry it. The producer has **no read or write path** into the
evaluator zone — not to the evaluator source, not to hidden material, not to the
official metric. And the evaluator's raw output is stored **before any agent
interprets it**, so what persists is bytes rather than an interested party's
paraphrase.

A boundary breach invalidates the run rather than lowering its score: a candidate
that reached the evaluator zone produced a result of unknown provenance, and
scoring it low would record it as a bad result rather than as no result.

*See also Figure 10 —* [`aethrion_discovery.svg`](figures/aethrion_discovery.svg).

### 3.2 Where a sentence comes from

The second is a **sentence**. The natural way to produce a paper from a research
system is to hand a model the results and ask it to write; that produces good
prose and an unfalsifiable document, in which a fabricated number sits beside a
measured one in the same typeface.

So the document is a **projection** of canonical state, and the compiler's job is
to refuse:

| Refusal | Test |
|---|---|
| A factual sentence with no `ClaimVersion` | ACC-52 |
| A number the `VerifiedValue` registry does not carry | ACC-53 |
| A real citation that does not support the sentence | ACC-76 |
| A V2 verdict from a verifier with no current qualification | ACC-61 |

Structural and editorial text carries a `text_role` and passes, so the check
discriminates rather than blocking all prose. An `EvidenceTag` binds an
assertion to its evidence with a support relation drawn from **CiTO**, rather
than an enum invented here.

### 3.3 What is remembered, and where

The chain says what becomes knowledge. A separate question is what the system
*remembers* along the way, and the default answer — one long-term store,
retrieved by similarity — is wrong here for a reason unrelated to retrieval
quality: a raw evaluator output, a failed experiment, a debugging lesson and a
working scientific principle do not have the same standing.

There are **six** memories: Evidence · Finding · Search Experience · Procedural ·
Principle · Human Intervention. **Only Evidence may support a claim.** Evidence
never decays, because a claim anchored to a retracted source has to stay
traversable *after* the retraction. Procedural memory must decay, because "this
library needs that flag" is true about a version on a date and goes stale
silently.

Memory is also an independence question: a reviewer able to query the producer's
search experience inherits the producer's dead ends, and the review is anchored
while the record still says independent. `ADR-005`; Figure 11 —
[`aethrion_memory.svg`](figures/aethrion_memory.svg).

---

## 4. The plane architecture

Six planes, plus a seventh that has been proposed but not accepted:

```mermaid
flowchart TD
    subgraph EXP["EXPERIENCE PLANE"]
        E1["Human intent · approvals · decision queue<br/>Obsidian vault · cockpit · dashboards"]
    end
    subgraph CTL["CONTROL PLANE"]
        C1["Temporal — G0–G10 lifecycle · gates<br/>retry · timeout · compensation"]
    end
    subgraph EVT["EVENT PLANE"]
        V1["NATS JetStream — post-commit events<br/>integration · fan-out · replay"]
    end
    subgraph COG["COGNITION PLANE"]
        G1["LangGraph — bounded agent reasoning<br/>inside a single task, never across gates"]
    end
    subgraph EXE["EXECUTION PLANE"]
        X1["Sandbox · Tool Broker · Execution Broker<br/>credentials never reach the agent"]
    end
    subgraph EVD["EVIDENCE & OPERATIONS PLANE"]
        D1["Sources · claims · runs · manifests<br/>ledgers · object store · audit"]
    end
    subgraph MET["METASCIENCE PLANE — proposed, not accepted"]
        M1["Agreement · calibration · gate yield<br/>control injection · claim survival"]
    end

    EXP --> CTL --> COG --> EXE --> EVD
    CTL --> EVT
    EVT -.-> EXP
    EVD -.-> MET
    MET -.->|"measures the laboratory itself"| CTL

    style MET fill:#FBEFD6,stroke:#E69F00,color:#000
    style EVD fill:#E0F3EC,stroke:#009E73,color:#000
```

Cross-cutting through all of them: **policy, security, identity, model routing,
assurance**.

> **These are logical planes, not deployment units.** Seven planes do not imply
> seven services, seven databases or seven clusters. The Metascience plane may
> begin as a handful of scheduled queries over the evidence store; the Cognition
> plane may be a library inside a worker. The planes fix *ownership and
> direction of authority* — what may decide what — and deployment topology is
> chosen separately, per component, against real operational need.

### 4.1 Two separations that carry the design

**Temporal is the process authority. LangGraph is not.**

```mermaid
flowchart TD
    T["TEMPORAL<br/>owns the research lifecycle<br/>durable, months-long, replayable"]
    T --> G0["G0"] --> G1["G1"] --> G2["G2"] --> G3["G3"] --> G4["G4"] --> G5["G5"]
    G5 --> G6["G6 Review"]
    G6 --> LG["LangGraph task<br/>reason → retrieve → tool → output<br/><i>minutes, bounded, disposable</i>"]
    LG --> G6
    G6 --> G7["G7"] --> G8["G8"] --> G9["G9"] --> G10["G10"]

    style T fill:#DDEAF4,stroke:#0072B2,color:#000
    style LG fill:#F5E4EE,stroke:#CC79A7,color:#000
```

A research project lives for months and must survive process restarts, model
changes and human absence. An agent graph is the wrong place to keep that state.
Conversely, Temporal is the wrong place to do reasoning. **LangGraph is not a
workflow engine; Temporal is not a reasoning engine.**

**NATS carries events. It does not carry authority.**

```mermaid
flowchart LR
    G3["G3 literature frozen"] --> TC["Temporal state commit<br/><b>canonical</b>"]
    TC --> EV["LITERATURE_SET_FROZEN<br/>event on JetStream"]
    EV --> O1["Obsidian updater"]
    EV --> O2["Dashboards"]
    EV --> O3["Graph index"]
    EV --> O4["Audit pipeline"]

    style TC fill:#DDEAF4,stroke:#0072B2,color:#000
```

If the entire event stream were deleted, gate state would still be recoverable
from Temporal. A consumer may miss an event; it may never *decide* anything.

### 4.1.1 The collaboration plane — how a cohort works without talking itself broke

Substantial scientific execution runs as a **cohort**, not a single actor
(`ADR-011`). That is an epistemic decision rather than a capability one: this
system is built against *plausibility*, and a second independent look is the only
mechanism that sees what the first could not. It is also expensive, and the
plane exists to make it affordable without making it pointless.

**Independence is a profile, not a count.**

| Dimension | The question |
|---|---|
| Cognitive function | Different kinds of scrutiny — methodologist, statistician, skeptic? |
| Evidence exposure | Derived from the same evidence, or different subsets? |
| Peer visibility | Did the second see the first before forming a position? |
| Model profile | Different family and snapshot — necessary, not sufficient |
| Prompt perspective | Different framing, or the same framing twice? |

Several instances of one model on one context are **one** contribution. They will
agree, and the agreement carries no information — ACC-081.

**Independent-first, because order is the mechanism.** Peer output is hidden for
round zero; each actor produces an `InitialPositionArtifact`; the artifacts are
sealed; only then are material differences exposed. Anchoring is an effect rather
than a preference, and a sealed first position is the only thing that later
distinguishes independent agreement from deference — ACC-082.

**Convergence is not a vote.** A cohort converges when no material
methodological challenge is unresolved, no critical evidence contradiction is
open, and every protocol blocker is closed or explicitly escalated. Four actors
agreeing does not close a skeptic's unanswered objection — ACC-090.

#### What the cohort says to itself

```mermaid
flowchart LR
    A["agent"] -->|"typed delta<br/><i>+ artifact pointer</i>"| BB["Scientific Blackboard<br/><i>a projection</i>"]
    BB --> B["agent"]
    A -.->|"full content"| AR["Artifact store<br/><i>canonical</i>"]
    BB -.->|"pointer resolves"| AR
    BB -->|"delete the blackboard"| X["no canonical<br/>science is lost"]

    style AR fill:#F7E2D6,stroke:#D55E00,color:#000
    style X fill:#E0F3EC,stroke:#009E73,color:#000
```

Ten message types — `PROPOSAL`, `CHALLENGE`, `EVIDENCE`, `REQUEST`,
`CORRECTION`, `DISAGREEMENT`, `CONSENSUS_CANDIDATE`, `ABSTAIN`, `STATUS`,
`BLOCKER` — because a type can be tracked to resolution and a tone cannot. A
message carries a **delta and a pointer**, never a transcript: the token saving
is the obvious reason, and the other one is that a transcript passed between
agents is a channel through which one agent's error becomes another's premise.

The topology is compiled per task and is **fully connected only in an explicit
control mode** — which exists because that is the baseline the optimisation is
measured against. Comparing to a single agent would measure the cost of having a
cohort at all, a decision already taken on other grounds.

**Two things a governor may never silence:** a `BLOCKER`, and any non-waivable
safety message. A low-utility edge carrying a blocker is still carrying a
blocker — ACC-088. And a low-calibration sender is not silenced either; its
message changes priority and corroboration requirement, because silencing an
actor for having been wrong is how a cohort stops being able to surprise itself.

**Optimisation is anchored.** Accepted only when quality stays within a declared
tolerance *and* coordination cost falls meaningfully; a regression rolls the
topology back automatically — ACC-086, ACC-087. `ADR-013`; WP-148 to WP-150.

### 4.1.2 What degrades when the budget runs low

Not the cohort, and not the assurance route. Communication verbosity, in a
declared order:

```
structured full → compressed → pointer-only → silence unless material
```

A task that cannot afford its required assurance becomes `BLOCKED_BUDGET` or
requests a scope reduction — it does not proceed more cheaply (ACC-099,
ACC-101). Every token carries one of seven categories, so **coordination overhead
is a derived ratio rather than an estimate**: a single cost total says a campaign
was expensive, and the categories say whether it was expensive because it did
science or because it held a meeting. `ADR-011` §5; WP-153.

### 4.2 The separation that cuts across every plane

The planes answer *where* a thing runs. [ADR-003](adr_003_trusted_control_and_policy.md)
answers a question no plane diagram can: **whose words are allowed to change what
the system does.**

![The trust boundary, with one injected instruction followed to the point where it is denied](figures/aethrion_trust.svg)

*Figure 7 — The control plane holds the goal, the plan and every privilege. The
data plane holds everything an outsider can write, including whatever a PDF hides
in white-on-white. Content crosses the boundary; authority does not. Generated by
`scripts/fig_trust.py`.*

```mermaid
flowchart TD
    subgraph TRUST["TRUSTED CONTROL PLANE — may act"]
        T1["Task and plan"]
        T2["Tool broker · credentials · write paths"]
    end
    subgraph DATA["UNTRUSTED DATA PLANE — may only be read"]
        U1["Paper full text · tool and API output<br/>web pages · reviewer comments"]
    end
    U1 -->|"content crosses:<br/>quoted, attributed, <b>never obeyed</b>"| T1
    T1 --> PDP{"policy decision point<br/>permit or forbid?"}
    PDP -->|"permit"| ACT["Tool call executes;<br/>the decision is recorded with the run"]
    PDP -->|"forbid — and forbid is the default"| DENY["Denied.<br/>An anomaly is a denial, not a warning"]
    style TRUST fill:#DDEAF4,stroke:#0072B2,color:#000
    style DATA fill:#FBEFD6,stroke:#E69F00,color:#000
    style PDP fill:#F5E4EE,stroke:#CC79A7,color:#000
    style DENY fill:#F7E2D6,stroke:#D55E00,color:#000
```

A retrieved sentence may change what the agent *knows*. It may never change what
the agent is *allowed to do*, because the request it would provoke is evaluated
against policy that no retrieved text can author. This is the CaMeL pattern,
adopted as a `PATTERN` rather than reimplemented, with the policy-engine
`DEPENDENCY` and AgentDojo named as the `BENCHMARK` that would falsify it.

**Nothing here has been exercised.** No policy set is authored in this
repository and no adversarial benchmark has been run against it, so the cut in
Figure 7 is a decision on paper. It is a *testable* decision — which is the whole
reason a benchmark was named alongside it — and it has not been tested.

---

## 5. The G0–G10 research lifecycle

The spine of the system. Each gate has a frozen output — an artefact that, once
produced, does not change without a recorded supersession.

![The AETHRION research lifecycle](figures/aethrion_lifecycle.svg)

*Figure 1 — Eleven gates on the vertical axis, three actor classes on the
horizontal. Reading down is time; reading across is who may act. **G5 is drawn
as two lanes** because one label could not carry it: bounded discovery cognition
runs in `G5·D`, and nothing model-produced becomes evaluator truth in `G5·E`.
The hatched cells at `G5·E` and `G7a` are the design, not an omission. Generated
by `scripts/fig_lifecycle.py`; see `docs/figures/README.md` for the
specification.*

```mermaid
flowchart TD
    G0["<b>G0 Intake</b><br/>IntakeRecord<br/><i>is this new? who owns it?</i>"]
    G1["<b>G1 Charter</b><br/>ProjectCharter · ControlPlan<br/><i>the human writes the decision question</i>"]
    G2["<b>G2 Protocol</b><br/>ProtocolManifest<br/><i>method frozen before results exist</i>"]
    G2B["<b>G2b Analysis Plan</b><br/>AnalysisPlanManifest<br/><i>how the result will be judged</i>"]
    IPA["<b>In-Principle Acceptance</b><br/><i>accepted on method, not on outcome</i>"]
    G3["<b>G3 Literature</b><br/>LiteratureSetManifest<br/><i>frozen, hashed, PRISMA-reported</i>"]
    G4["<b>G4 Baseline</b><br/>BaselineBundle · FalsificationPlan<br/><i>what would prove this wrong?</i>"]
    G5D["<b>G5·D Discovery</b><br/>SearchNode · candidate workspace<br/><i>bounded model cognition runs here</i>"]
    G5E["<b>G5·E Execute</b><br/>ExperimentRun · RawEvaluatorArtifact<br/><b>no evaluator authority</b>"]
    G6["<b>G6 Assurance</b><br/>mechanical → blind → adversarial → disagreement"]
    G7A["<b>G7a Reproduction</b><br/>same manifest, same seed<br/><b>deterministic, no model</b>"]
    G7B["<b>G7b Replication</b><br/>different implementation<br/><i>distribution test</i>"]
    G8["<b>G8 Decision</b><br/>DecisionRecord<br/><b>HUMAN ONLY, under quota</b>"]
    G9["<b>G9 Publish</b><br/>PublicationPackage<br/><i>claim binding V0 · scope V2</i>"]
    G10["<b>G10 Monitor</b><br/>retraction · citation · CVE · conflict<br/><i>a living review</i>"]

    G0 --> G1 --> G2 --> MODE{"research_mode?"}
    MODE -->|exploratory| G3
    MODE -->|replication| RC["Locked replication contract"] --> G3
    MODE -->|confirmatory| G2B --> IPA --> G3
    G3 --> G4 --> G5D --> G5E --> G6
    G6 --> G7A --> G7B --> G8 --> G9 --> G10
    G10 -.->|"material signal"| G2
    G6 -.->|"three failed explanations → ProtocolChallenge"| G2

    style G5D fill:#DCE9F7,stroke:#0072B2,color:#000
    style G5E fill:#E0F3EC,stroke:#009E73,color:#000
    style G7A fill:#E0F3EC,stroke:#009E73,color:#000
    style G8 fill:#F7E2D6,stroke:#D55E00,color:#000
    style IPA fill:#FBEFD6,stroke:#E69F00,color:#000
```

### 5.1 What each gate is defending against

| Gate | Frozen output | The failure it exists to prevent |
|---|---|---|
| **G0** Intake | `IntakeRecord` | Redoing work that already exists; unowned work |
| **G1** Charter | `ProjectCharter`, `ControlPlan` | A model inventing its own research objective |
| **G2** Protocol | `ProtocolManifest` | Changing the method after seeing the result |
| **G2b** Analysis Plan | `AnalysisPlanManifest` | Choosing the analysis that gives the nicest answer |
| **G3** Literature | `LiteratureSetManifest` | An evidence base that cannot be re-derived |
| **G4** Baseline | `BaselineBundle`, `FalsificationPlan` | Only asking how to confirm, never how to refute |
| **G5** Execute | `ExperimentRun` | Model bias entering the measurement itself |
| **G6** Assurance | `ReviewRecord` | "Looks good" counted as independent review |
| **G7a** Reproduction | reproduction result | A result nobody can obtain twice |
| **G7b** Replication | distribution comparison | Confusing "same numbers" with "same conclusion" |
| **G8** Decision | `DecisionRecord` | A model deciding what the laboratory believes |
| **G9** Publish | `PublicationPackage` | A sentence claiming more than its evidence supports |
| **G10** Monitor | supersession records | Treating a published claim as permanently true |

> **G2b and in-principle acceptance are conditional, not universal.** Forcing
> Registered Report ceremony onto exploratory work produces bureaucracy without
> epistemic gain, and pushes people to mislabel confirmatory work as exploratory
> to escape it — the opposite of the intent. The router sits immediately after
> G2:
>
> | `research_mode` | Analysis plan | In-principle acceptance |
> |---|---|---|
> | `exploratory` | recommended | **not required** — but the claim may never be labelled confirmatory |
> | `replication` | required | a locked replication contract, naming the target claim and the agreement criterion |
> | `confirmatory` | **required and locked** | **required** |
>
> The classification itself is fail-closed: absent or ambiguous, it resolves to
> `confirmatory`, which is the heaviest path.

### 5.1.1 Inside G4 and G5 — the discovery search graph

Where G5 runs computational discovery, it is not an agent loop with a transcript.
It is a typed candidate graph in which two distinctions are load-bearing:

- **`DEBUG` is a different node state from `IMPROVE`.** A candidate that failed
  to compile has said nothing about the hypothesis. Recorded as "tried a
  different approach", an implementation defect becomes evidence about a
  scientific question, and the record cannot be told from one where the idea
  genuinely failed. ACC-64 makes the conversion impossible.
- **`PRIMARY_PARENT` is a different edge from `REFERENCE`.** One is the ancestry
  and credit path that reproduction depends on; the other lets a branch read a
  sibling without changing its ancestry.

Everything the graph computes is a **priority for spending compute**. Writing a
selection score, a normalised rank or a tournament position into a
`ClaimVersion`, a `VerifiedValue` or a `GateRecord` is refused by schema and by
policy. A campaign that stops on budget produces a `CampaignStopRecord` that
satisfies no gate — running out of money demonstrates nothing.

`ADR-006`; WP-144 and WP-145.

### 5.2 In-principle acceptance — why it is in the flow

Without it, publication bias survives every other control:

```mermaid
flowchart LR
    A["G2 protocol frozen"] --> B["G5 negative result"] --> C{"G8 human"}
    C -->|"'I don't like this,<br/>let's not publish'"| D["Publication bias<br/>intact"]
    style D fill:#F7E2D6,stroke:#D55E00,color:#000
```

The fix is a commitment made **before** the result exists: *if the protocol is
executed as written, the outcome is accepted regardless of its direction.* This
is Registered Reports discipline, and it is the point where AETHRION stops being
a research assistant and becomes a scientific instrument.

### 5.3 G6 in detail — the heaviest gate

```mermaid
flowchart TD
    IN["Result + evidence"] --> M["<b>G6-0 Mechanical</b><br/>hashes · manifests · statcheck · GRIM/GRIMMER<br/>citation entailment · schema · artifact integrity"]
    M -->|"fails"| BACK["Returned with a finding<br/><i>no model can waive this</i>"]
    M -->|"passes"| B["<b>G6-1 Blind review</b><br/>ReviewPacket built by a <b>program</b><br/>reviewer never sees producer reasoning"]
    B --> A["<b>G6-2 Adversarial</b><br/>ACH matrix — which hypotheses does<br/>this evidence <b>eliminate</b>?"]
    A --> D{"<b>G6-3 Disagreement</b>"}
    D -->|"converges"| OUT["Verdict + ProducerResponse"]
    D -->|"does not converge"| AR["Delphi / IDEA rounds → arbiter<br/><i>bounded: round limit + breaker</i>"]
    AR --> OUT

    style M fill:#E0F3EC,stroke:#009E73,color:#000
    style BACK fill:#F7E2D6,stroke:#D55E00,color:#000
```

Three details carry most of the weight:

- **The `ReviewPacket` is built by a deterministic program, not a prompt.** Only
  then can "what exactly did the reviewer see?" be answered afterwards.
- **The adversarial reviewer is scored on the quality of its refutation**, not on
  approval speed. A reviewer rewarded for agreeing is a rubber stamp with a
  model behind it.
- **Disagreement is bounded.** Rounds are counted, a breaker exists, and open
  findings cannot disappear silently — they are closed by a `ProducerResponse`
  carrying `ACCEPTED` / `DISPUTED` / `CLARIFICATION_NEEDED`.

---

## 6. Who executes what

Two questions live here and they are different: **which durable function is
accountable** (the role catalogue) and **which kind of actor executes a given
step** (mechanical, model or human). The full tables live in
`AETHRION_ROLE_MODEL_ASSIGNMENT.md`; this section gives the shape of both.

### 6.0 The fourteen durable functions

![Role authority and separation constraints](figures/aethrion_roles.svg)

*Figure 3 — Authority tiers, actor composition per role, and the constraint
resolution that lets one operator hold several roles. Full definitions, including
what each role may never do, are in [`AETHRION_ROLES.md`](aethrion_roles.md).*

```mermaid
flowchart TD
    subgraph AUTH["👤 HUMAN AUTHORITY — never a model"]
        A1["Project Decision Owner — signs G8 · G9"]
        A2["Safety / Data Owner — data class · blocks all"]
        A3["Research Integrity Officer — integrity judgement · blocks all"]
        A4["Assurance Lead — reviewer assignment · blocks G6 · G7"]
    end
    subgraph OWN["👤 + 🤖 OWNERSHIP — human decides, model drafts"]
        B1["Scientific Owner — the decision question · G2"]
        B2["Statistical Methods Owner — locks the analysis plan"]
        B3["Evidence Lead — freezes the literature set · G3"]
        B4["Engineering Owner — approves code · G4 · G5"]
    end
    subgraph PROD["🤖 + 👤 PRODUCTION — model produces, human approves"]
        C1["Research Software Engineer — reproducibility · G7"]
        C2["Data Steward — datasets · identifiers"]
        C3["Red Team Lead — pre-mortem · control injection"]
    end
    subgraph MECHR["⚙️ + 🤖 MECHANICAL-FIRST"]
        D1["Scientific Editor — scope conformance · G9"]
        D2["Knowledge Steward — contradiction sweeps · G0"]
        D3["Metascience Lead — measures, <b>blocks nothing</b>"]
    end
    AUTH -.->|"authority downward"| OWN -.-> PROD -.-> MECHR
    MECHR -.->|"findings upward — never waivers"| AUTH

    style AUTH fill:#F7E2D6,stroke:#D55E00,color:#000
    style OWN fill:#FBEFD6,stroke:#E69F00,color:#000
    style PROD fill:#DDEAF4,stroke:#0072B2,color:#000
    style MECHR fill:#E0F3EC,stroke:#009E73,color:#000
```

**The Metascience Lead blocks nothing by design.** A function that both measures
the laboratory and can veto its work stops measuring honestly — it acquires an
interest in the numbers.

### 6.0.1 How any gate resolves

```mermaid
flowchart TD
    IN["Gate entry"] --> MECHQ{"Is there a mechanical<br/>check for this step?"}
    MECHQ -->|Yes| RUN["⚙️ Run it FIRST"]
    RUN --> PASS{"Passed?"}
    PASS -->|No| BLOCK["Blocked with a finding<br/><b>no model may waive it</b>"]
    PASS -->|Yes| MODELN
    MECHQ -->|No| MODELN["🤖 Model produces<br/>output must be falsifiable"]
    MODELN --> AUTHQ{"Does the gate carry<br/>decision authority?"}
    AUTHQ -->|"G8 · G9 · freeze · lock · sign"| HUMANN["👤 Human decides<br/>recorded, never delegated"]
    AUTHQ -->|No| REC["Gate record produced"]
    HUMANN --> REC

    style RUN fill:#E0F3EC,stroke:#009E73,color:#000
    style BLOCK fill:#F7E2D6,stroke:#D55E00,color:#000
    style MODELN fill:#DDEAF4,stroke:#0072B2,color:#000
    style HUMANN fill:#F7E2D6,stroke:#D55E00,color:#000
```

### 6.0.2 Actor classes

```mermaid
flowchart LR
    subgraph MECH["⚙️ Mechanical — cannot be overridden by a model"]
        ME["duplicate search · policy engine<br/>GROBID · hashing · statcheck<br/>ReviewPacketBuilder · reproduction<br/>scope conformance"]
    end
    subgraph MODEL["🤖 Model — produces, never decides"]
        MO["triage · drafts · query plans<br/>screening · pre-mortem<br/>review · adversarial refutation"]
    end
    subgraph HUMAN["👤 Human — authority"]
        HU["the decision question · signatures<br/>freeze · lock · data class<br/><b>G8 and G9</b>"]
    end
    MECH --> MODEL --> HUMAN

    style MECH fill:#E0F3EC,stroke:#009E73,color:#000
    style MODEL fill:#DDEAF4,stroke:#0072B2,color:#000
    style HUMAN fill:#F7E2D6,stroke:#D55E00,color:#000
```

### 6.1 A role is a function, not a person

The role catalogue names fourteen durable functions. It does **not** require
fourteen people, and reading it that way is what makes the organisation look
impossible in a small operation.

```yaml
RoleBinding:
  role_id: statistical_methods_owner
  role_type: governance_function
  actor:
    human: <identity>          # any of these may be empty
    model_profile: <profile>
    mechanical: <service>
  separation:
    must_be_independent_from: [experiment_analyst]
    can_combine_with:         [scientific_owner]
    cannot_combine_with:      [final_independent_verifier]
```

```mermaid
flowchart TD
    R["RoleBinding<br/>role_id: statistical_methods_owner"]
    R --> ACT["actor<br/>human · model_profile · mechanical<br/><i>any may be empty</i>"]
    R --> SEP["separation"]
    SEP --> S1["must_be_independent_from:<br/>experiment_analyst"]
    SEP --> S2["can_combine_with:<br/>scientific_owner ✅"]
    SEP --> S3["cannot_combine_with:<br/>final_independent_verifier ❌"]
    S1 --> ENG["Constraint engine<br/>admits or refuses the binding"]
    S2 --> ENG
    S3 --> ENG
    ENG --> OK["One person, several roles —<br/>legally, and provably"]

    style ENG fill:#E0F3EC,stroke:#009E73,color:#000
    style S2 fill:#E0F3EC,stroke:#009E73,color:#000
    style S3 fill:#F7E2D6,stroke:#D55E00,color:#000
```

Independence is then expressed as **separation constraints**, not headcount: one
person may legally hold several roles, and the constraint engine states exactly
which combinations destroy independence and which do not. The binding is
enforced at compile time by WP-013 and WP-047, not asserted in prose.

> This does not resolve finding **C2** — who may act as the final independent
> verifier when there is one person — but it gives that decision a form. The
> question stops being "where do I find 73 owners?" and becomes "which
> combinations am I willing to declare independent, and which must remain
> mechanical or external?"

**Three invariants that are not negotiable:**

1. **No agentic methodological discretion during a frozen G5 execution.** The
   subject of an experiment may perfectly well *be* a model — a frozen model
   under test, a preregistered inference pipeline, an RL policy. What is
   forbidden is a research agent changing a threshold, a metric, a stopping
   point or a sample mid-run because the result looks wrong. The model may be
   the instrument; it may not be the methodologist.
2. **The same at G7a**, and more strictly: reproduction runs the frozen manifest
   and reports what happened. It reproduces or it does not.
3. **At G8 a model produces a recommendation, never a decision.**

Effort and reviewer count are bound to the assurance class:

| Assurance | Producer effort | Reviewer effort | Adversarial | Reviewer quota | Model policy |
|---|---|---|---|---|---|
| **R1** | `medium` | `high` | — | 1, any family | hosted OK |
| **R2** | `high` | `high` | `xhigh` | 2, **different family** | hosted + full I/O logging |
| **R3** | `xhigh` | `xhigh` | `max` | 3, **different family** | **local open-weight mandatory** |

R3 requires a local model because a hosted model has no pinnable snapshot, and
without one, G7a is structurally impossible. That is a constraint, not a
preference.

---

## 7. The skill layer — how an agent knows *how* to work

A `RoleContract` says **who** an agent is: its purpose, its allowed tools, its
data classes, its budget, its success criteria. Every one of those is a
*boundary*. None of them says **which procedure to follow**. That gap was
previously filled by the prompt — an unversioned, untested, unauditable layer.

Skills close it, and they come in **two families with one shared core**:

```mermaid
flowchart TD
    R["<b>using-aethrion</b><br/>router — classify first"]
    R --> Q{"What kind of task?"}

    Q -->|"building AETHRION"| ENG["<b>ENGINEERING · 11</b><br/>vendored from obra/superpowers<br/>test-driven-development<br/>systematic-debugging · writing-plans<br/>using-git-worktrees · code review<br/>subagent-driven-development"]
    Q -->|"doing research"| SCI["<b>SCIENTIFIC · 28</b><br/>AIRL-native<br/>preregistration-discipline<br/>searching-literature · extracting-evidence<br/>blind/adversarial review · metascience"]
    Q -->|"always"| SH["<b>SHARED · 10</b><br/>verification-before-completion<br/>independence-discipline<br/>evidence-before-claim · scope-discipline"]

    ENG --> TC["TaskContract<br/>skills_loaded[] + skill_bundle_hash"]
    SCI --> TC
    SH --> TC
    TC --> EV["→ enters the evidence chain"]

    style ENG fill:#DDEAF4,stroke:#0072B2,color:#000
    style SCI fill:#E0F3EC,stroke:#009E73,color:#000
    style SH fill:#F5E4EE,stroke:#CC79A7,color:#000
```

> **Research adaptations extend their engineering counterparts; they never
> replace them.** `preregistration-discipline` is what test-driven development
> becomes when the artefact is a claim rather than a function — but building the
> Claim Ledger is still test-driven-development work. AETHRION is simultaneously a
> laboratory and a software platform, and it needs both disciplines at once.

The mapping is a translation of the same epistemic rule into two domains:

| Software engineering | Scientific research | The shared rule |
|---|---|---|
| Test before code | Preregistration before result | You do not get to decide the criterion after seeing the outcome |
| Bug root-cause tracing | Anomaly root-cause tracing | Three failed explanations means the architecture is wrong, not the fix |
| Fresh-context implementer | Fresh-context analyst | Whoever produced it cannot be the one who checks it |
| Reviewer sees the diff, not the reasoning | Reviewer sees the packet, not the trace | Information asymmetry is what makes review independent |
| Verification before "done" | Verification before "claimed" | Memory is not evidence |

### 7.1 Two classification axes, not one

```
research_mode:   exploratory | replication | confirmatory     ← what the claim may assert
execution_path:  spike       | bounded     | architectural     ← how heavy the execution is
```

They are orthogonal: a confirmatory study can be a bounded task, and an
exploratory one can force an architectural change. Both are classified, and
**when in doubt the heavier value is taken on each axis** — the fall-through
default is fail-closed, never the lightest path.

### 7.2 The format is the bootstrap

Skills conform to the **Agent Skills open standard** (`agentskills.io`), which
Claude Code, Codex, OpenCode, Cursor, Copilot, Gemini CLI and Hermes Agent all
implement. A skill that does not load governs nothing, so conformance is checked
mechanically by `scripts/validate_skills.py`, and provenance
(`airl.derived_from`, `airl.upstream_commit`) is checked with it.

> **Format compatibility is not behavioural compatibility.** Conformance makes
> the registry *loadable* by those harnesses. Whether a given harness loads the
> right skill at the right moment — and keeps it across compaction — is
> established by the acceptance suite in WP-048 (ACC-42, ACC-44, ACC-45), and it
> is **not** established today. Only the Claude Code path is wired
> (`.claude/skills`), and even there no behavioural test has been run.

### 7.3 Independence is measured, not assumed

```mermaid
flowchart LR
    A["Different tier,<br/>same family<br/>Sonnet ↔ Opus"] --> L["LOW<br/>shared lineage,<br/>correlated errors"]
    B["Different provider<br/>family"] --> M["MEDIUM<br/>different pipeline,<br/>overlapping corpus"]
    C["Model judgement ↔<br/><b>mechanical verification</b>"] --> H["HIGH<br/>the only genuinely<br/>independent axis"]

    style L fill:#F7E2D6,stroke:#D55E00,color:#000
    style M fill:#FBEFD6,stroke:#E69F00,color:#000
    style H fill:#E0F3EC,stroke:#009E73,color:#000
```

The family rule — *at R2/R3 the reviewer must come from a different provider
family* — is a **proxy**. What is permanent is the measured pairwise error
correlation ρ; when the calibration set exists, the measurement replaces the
proxy. A laboratory that never measures its own independence assumption is
producing the repetition of an assumption and calling it verification.

---

## 8. How evidence is signed — and how that unlocks the programme

Every Definition of Done requires a signed `EvidenceManifest` in an immutable
store. The store was scheduled far downstream, which produced a deadlock: nothing
could be accepted until it existed, and it could not be built without accepting
something first.

The resolution is to **delegate immutability to standards that already exist**
rather than to build it first:

```mermaid
flowchart TD
    A["Work package artefacts<br/>tests · environment · schema + policy versions"] --> B["<b>in-toto Statement</b><br/>subject = artefact digest<br/>predicate = EvidenceManifest"]
    B --> C["<b>DSSE envelope</b>"]
    C --> D["<b>Sigstore</b> keyless signature<br/>short-lived OIDC-bound cert"]
    D --> E["<b>Rekor transparency log</b><br/>append-only · inclusion proof"]
    E --> F["<b>OpenTimestamps</b> anchor<br/>WP-139 · hash-only"]
    F --> G["Verifier accepts<br/>→ package may reach ACCEPTED"]
    E -.->|"when WP-026 lands"| H["WORM object store<br/><i>log entry remains as<br/>an independent witness</i>"]

    style E fill:#E0F3EC,stroke:#009E73,color:#000
    style G fill:#F7E2D6,stroke:#D55E00,color:#000
```

> **Rekor is a tamper-evident transparency record for signed metadata — not an
> artifact store.** It holds the attestation and its inclusion proof. The
> artifacts themselves, the Sigstore bundle, the certificate chain and the
> verification material still need durable storage, which is what WP-026
> eventually provides. **WP-000 defers WP-026; it does not cancel it.**

The same machinery signs model weights: `sigstore/model-transparency` and the
OpenSSF Model Signing spec give the R3 requirement — a hashed, signed local
open-weight model — an off-the-shelf implementation.

> **What this does not solve.** Immutability was only half of the blocker. The
> other half is *who the independent verifier is* in a one-person operation. No
> standard answers that; it is a scope decision that remains open. See
> `AETHRION_EXTERNAL_STANDARDS.md` §3.2.

---

## 9. What actually runs today — Literature Bridge V0

One vertical slice exists and works: **Zotero → canonical registry → Obsidian →
agent**, read-only end to end.

```mermaid
flowchart TD
    Z["<b>Zotero local API</b><br/>127.0.0.1:23119<br/><i>bibliographic authority</i>"]
    Z -->|"READ ONLY<br/>no key · no write · no delete · no merge"| SV["<b>airl_bridge.service</b><br/>FastAPI · systemd user unit"]
    SV --> DB["<b>SQLite canonical registry</b><br/>stable AIRL source identity<br/>idempotent upsert"]
    DB --> OB["<b>Obsidian projection</b><br/>70 - Literature Sets/Zotero Sources<br/>atomic write · manifest-owned deletion"]
    DB --> MCP["<b>Hermes MCP server</b><br/>5 tools, read-only"]
    T["<b>sync timer</b><br/>every 30 min"] -.-> SV
    MCP --> AG["Hermes / any MCP agent"]
    OB --> HU["Human synthesis<br/>20 - Source Notes"]

    style Z fill:#FBEFD6,stroke:#E69F00,color:#000
    style DB fill:#E0F3EC,stroke:#009E73,color:#000
    style MCP fill:#DDEAF4,stroke:#0072B2,color:#000
```

### 9.1 The design decisions inside it

**Zotero is never touched.** No API key is stored, no write path exists. An
agent silently mutating a human's bibliographic workspace is the failure mode
being designed out, and it stays out until a group library and an audit policy
exist.

**SQLite is not a cache — it is the identity boundary.** A Zotero representation
is not an AIRL source. The registry assigns AIRL's own stable identity, so the
rest of the system never depends on another tool's key space.

**Generated and human-authored content cannot collide.**

```mermaid
flowchart LR
    subgraph GEN["GENERATED — the bridge owns these"]
        G["70 - Literature Sets/Zotero Sources/<br/>01 - Commissioning · 02 - Reviews<br/>04 - Architecture · 07 - Skills"]
    end
    subgraph HUM["HUMAN — never overwritten"]
        H["20 - Source Notes · 30 - Concepts<br/>40 - Claims · 50 - Decisions<br/>80 - Daily"]
    end
    GEN -.->|"manifest-owned deletion:<br/>only files it created"| GEN
    HUM -.->|"untouched"| HUM

    style GEN fill:#DDEAF4,stroke:#0072B2,color:#000
    style HUM fill:#E0F3EC,stroke:#009E73,color:#000
```

The bridge deletes only files recorded in its own projection manifest. A
markdown file a human drops into the generated folder is not "stale" — it is
simply not the bridge's.

**The agent's blast radius is bounded.** The MCP server exposes exactly five
read-only tools:

| Exposed | Deliberately absent |
|---|---|
| `bridge_status` · `search_sources` · `get_source` · `list_categories` · `list_possible_duplicates` | `sync` · any write · delete · merge · any Zotero mutation |

Even a fully compromised agent can read the catalogue and nothing else.

### 9.2 The known hazard in it

`get_source` returns an abstract as raw text. A PDF or abstract can contain
`IGNORE ALL PREVIOUS INSTRUCTIONS…`, so untrusted source content reaches an
agent's context — recorded as risk **ACC-05**, and currently bounded only by the
absence of any write capability. The moment a write-capable tool broker exists,
this becomes a real exposure, and the untrusted-content boundary must be enforced
before that, not after.

### 9.3 Modules

| Module | Responsibility |
|---|---|
| `zotero.py` | Read-only Zotero local API client |
| `database.py` · `models.py` | Canonical registry, schema, idempotent upsert |
| `service.py` | Sync orchestration, staleness, projection lifecycle |
| `obsidian.py` | Atomic projection writer, manifest-owned deletion, path-traversal defence |
| `catalog.py` | Category taxonomy and duplicate heuristics |
| `mcp_server.py` | The five read-only MCP tools |
| `main.py` · `cli.py` · `config.py` | FastAPI app, operator CLI, settings |
| `airl_framework/contracts.py` | Shared identity/manifest/event contracts — **no production consumer yet** |

---

## 10. Target versus reality

This is the section that governs how every other section should be read.

```mermaid
flowchart LR
    subgraph WORKING["RUNNING — verified locally"]
        W["Zotero read-only client<br/>SQLite source registry<br/>Obsidian projection<br/>Hermes MCP · 5 tools<br/>systemd units · 149 tests<br/>plan seal · 20 status checks<br/>signed evidence manifest<br/>17 generated figures"]
    end
    subgraph WRITTEN["WRITTEN — never executed"]
        S["52 skills, none behaviour-tested<br/>148 package documents<br/>80 acceptance scenarios<br/>role→model assignment rules<br/>4 authoring profiles"]
    end
    subgraph DESIGNED["DESIGNED — no code"]
        D["Temporal · LangGraph · NATS<br/>Tool Broker · Execution Broker<br/>Claim/Evidence Ledger · Run Registry<br/>Model Gateway · G0–G10 engine<br/>review pipeline · policy set<br/>metascience plane<br/>discovery graph · evaluator zone<br/>six memories · publication compiler"]
    end
    WORKING -->|"one work package<br/>of 148"| WRITTEN
    WRITTEN -->|"the distance is<br/><b>much larger</b> than the<br/>page count implies"| DESIGNED
    style WORKING fill:#E0F3EC,stroke:#009E73,color:#000
    style WRITTEN fill:#F5E4EE,stroke:#CC79A7,color:#000
    style DESIGNED fill:#FBEFD6,stroke:#E69F00,color:#000
```

| Component | Status |
|---|---|
| Zotero Bridge · Source Registry · Obsidian projection · Hermes MCP | **Working V0** |
| Plan seal, mirror generators, skill validator, figure generators | **Working** |
| Evidence issuance and verification (WP-000 tooling) | **Working** — `TECH_COMPLETE`, not `ACCEPTED` |
| Shared contract core | Prototype — **zero production consumers**, hash format conflicts with the bridge |
| Skill registry — 52 skills | Format-conformant and loadable; **behaviour untested** |
| Document authoring subsystem — router, 12 modules, 4 profiles | Written; one specimen **authored and resolution-checked**, **never rendered** — no toolchain is installed |
| G0–G10 contracts, roles, gates | Designed |
| Temporal · LangGraph · NATS · brokers · ledgers · Model Gateway | Planned |
| Policy set, ADR-003 enforcement | Decided; the engine is deferred to the ADR-010 bake-off and **no policy set is authored** |
| Metascience plane · role→model assignment | Proposal |
| Production | **No** |

### 10.1 The programme, and how far it has run

![The commissioning programme: eleven waves against the one package that has produced anything](figures/aethrion_waves.svg)

*Figure 6 — Waves are dependency order, not dates; the plan has none, and drawing
time it does not have would be an invention. The package counts are counted from
the plan directory at generation time, so the figure cannot disagree with the
plan it describes. Generated by `scripts/fig_waves.py`.*

Between W7 and W8 sits the only irreversible step in the programme: every
`PRE_GO_LIVE` acceptance scenario passes on one release candidate, and a human
signs. Baseline v1.0.1 exists because an earlier draft made a Day-2 rhythm a
precondition of the go-live that precedes it — a cycle that would have made the
gate unreachable in principle rather than merely unreached in practice.

### 10.2 The blockers, in order

Two of the five original blockers are now closed by **decisions** rather than by
code. That is progress of a specific and limited kind: a decision removes an
unknown, it does not remove work.

| # | Blocker | State |
|---|---|---|
| **C1** | Evidence bootstrap deadlock | **Closed.** WP-000 executed; issuance and verification run, tamper is rejected |
| **C2** | What "independent verifier" means for a one-person organisation | **Closed by [ADR-001](adr_001_solo_operator_independence.md).** R1 solo, R2 declared-partial, R3 `BLOCKED` — enforced, not argued |
| **H1** | Zotero ingest capped at 100 records, no pagination | Open — **fix M9 first**, or pagination turns a masked truncation into active data loss |
| **H2** | No deletion reconciliation, no tombstones | Open |
| **H3** | Read-only boundary has no behavioural test | Open |
| **H4** | Contract core has no consumers | Open |
| **H5** | No continuous integration | **Staged, not active** — the workflow exists at `deploy/bvc-01-verify.yml` and has never run; see [ADR-002](adr_002_bootstrap_verification_control.md) |

The two closures do not change the shape of the distance. What changed is that
the remaining blockers are now all **implementation**, and none of them is
waiting on a question nobody has answered.

---

## 10.3 What this system builds, and what it stands on

![The target stack, with adoption type and build status](figures/aethrion_stack.svg)

*Figure 4 — Adoption type is a visual channel rather than a caption: a
dependency, a standard, a pattern and a benchmark create different obligations.
Solid borders mark what is implemented.*

> **AETHRION should not invent its own PDF parser, screening engine, policy
> language, sandbox, experiment tracker or scholarly identifier.** A gate backed
> by a component its community maintains and tests is **stronger** than the same
> gate backed by code written here for the first time — the point of adoption is
> strength, not economy.

The register — every component, its adoption type, its priority and what it
changes about a work package — is
[`AETHRION_COMPONENT_REUSE.md`](aethrion_component_reuse.md). Security
architecture and policy evaluation are decided in
[`ADR-003`](adr_003_trusted_control_and_policy.md).

## 11. Where everything lives

Three surfaces, and only one of them is authoritative.

![Repository, vault and the outside world, with direction on every edge](figures/aethrion_topology.svg)

*Figure 9 — Every arrow points one way, and that is the design rather than a
simplification of it. A two-way sync between a repository and a note vault would
create a second place to be wrong in. Generated by `scripts/fig_topology.py`.*

The diagram below expands the same topology into the concrete directories.

```mermaid
flowchart TD
    subgraph REPO["Repository — canonical"]
        P["planning/commissioning/<br/><i>hash-sealed plan</i>"]
        DOC["docs/architecture · docs/review"]
        SK["skills/ — 52"]
        SRC["src/ · scripts/ · tests/"]
    end
    subgraph VAULT["Obsidian vault — generated views"]
        V1["01 - Commissioning"]
        V2["02 - Reviews"]
        V4["04 - Architecture"]
        V7["07 - Skills"]
        V3["70 - Literature Sets/Zotero Sources"]
    end
    subgraph HUMAN["Obsidian vault — human-authored"]
        H1["20 - Source Notes · 30 - Concepts<br/>40 - Claims · 50 - Decisions · 80 - Daily"]
    end
    P -->|"mirror_plan.py"| V1
    DOC -->|"mirror_vault.py"| V2 & V4
    SK -->|"mirror_vault.py"| V7
    SRC -->|"airl-bridge sync"| V3
    VAULT -->|"rsync"| BASE["vault_baseline/ — versioned snapshot"]

    style REPO fill:#E0F3EC,stroke:#009E73,color:#000
    style VAULT fill:#DDEAF4,stroke:#0072B2,color:#000
    style HUMAN fill:#F5E4EE,stroke:#CC79A7,color:#000
```

**Never edit a generated area.** Change the canonical file, regenerate, re-sync.
The plan seal does not cover the mirror, so drift there is invisible unless
`--check` is run. The mirror overwrites rather than merges, so the failure mode
of editing the vault is **losing that edit**, not corrupting the source — a
deliberately cheap failure.

### 11.1 How the corpus checks itself

The machine half of "agents produce, machines verify, humans decide" is not an
aspiration in this repository; it is ten checks that run on one command and
refuse to pass on a warning.

![What each check proves, and what it cannot see](figures/aethrion_verification.svg)

*Figure 8 — Each row states the claim the check earns and, beside it, the claim
it does not. The blind-spot column is why the figure exists: a bundle that
reports only green teaches its reader to trust it for things it never examined.
Generated by `scripts/fig_verification.py`.*

Two properties make this more than a test suite. **Truth is derived, never
transcribed** — counts, inventories and status come from the repository at check
time, so a document cannot quietly disagree with the thing it describes. And
**there is no advisory tier**: a warning is a failure, because a warning nobody
must act on is a warning nobody acts on.

The limit is stated plainly in the figure. All of this is internal consistency,
and every one of its guarantees would still hold for a corpus describing a system
that does not work. External truth enters through two doors only: reference
verification against Crossref, OpenAlex and arXiv, and the benchmarks named in
[`AETHRION_COMPONENT_REUSE.md`](aethrion_component_reuse.md) — none of which has
been run.

---

### 11.2 Human notification channels — PLANNED, with skills already written

The invariant "messaging is not an authorisation channel" implies a channel
layer, and the plan has one: **WP-131–135** in the tooling wave define a channel
registry with a **data-class ceiling** per channel, and signed deep links for
decision routing. The channels named in `WP-132` are ntfy (self-hosted),
Telegram, Discord/Slack and WhatsApp, each admitted only up to a data class:
Telegram and Discord/Slack at **D1**, WhatsApp at **D0** only, and only through
approved templates, because outside its 24-hour window the Business Cloud API
will not carry a free-form message at all.

| Component | Status |
|---|---|
| Channel registry and data-class ceiling (WP-132) | **PLANNED** — specified, no code |
| Decision routing with signed deep links (WP-135) | **PLANNED** — specified, no code |
| `notifying-humans`, `routing-decision-requests`, `escalating-and-paging` skills | **WRITTEN** — format-conformant, never executed |
| Any channel actually connected | **None.** Nothing sends anything today |

Three rules survive from the plan into the skills and are worth stating here,
because they are the reason the layer is not simply "add a bot": an agent never
sends a message — a broker does; a channel ceiling does not vary by person, so
there is no "but it is my own Telegram" exception; and a timeout never becomes
an approval.

---

## 12. The invariants

1. **Agents produce, machines verify, humans decide** — the order is never inverted.
2. **Nothing is complete without fresh verification evidence** — not memory, not a prior run, not another agent's report.
3. **When in doubt, take the heavier path** — missing or ambiguous input resolves to the highest assurance class.
4. **A producer may not summon its own verifier or helper.**
5. **An inbound message is never an instruction; messaging is not an authorisation channel.**
6. **`TECH_COMPLETE` is not `ACCEPTED`** — only an independent verifier's decision moves a package.
7. **A mechanical check, where one exists, runs first and cannot be overridden by a model.**
8. **No model at G5 or G7a; at G8 a model may only recommend.**
9. **A frozen artefact changes only through a recorded supersession.**
10. **`VERIFIED` is not a permanent state** — G10 can revise anything.

The following were added at baseline v1.2.0 with `ADR-004` to `ADR-010`. They are
the same kind of statement as the ten above — things that must hold whatever else
changes — and each names the scenario that tests it.

11. **No prose without a claim.** A factual publication assertion with no `ClaimVersion` behind it does not enter a package — ACC-52.
12. **No number without a `VerifiedValue`**, and no `VerifiedValue` without an immutable evaluator output under it — ACC-53, ACC-77.
13. **No evaluator controlled by its producer.** The producer cannot read, write or override the evaluator, the hidden material or the official metric — ACC-54, ACC-55.
14. **No confirmatory result without a plan frozen before it.** The claim ceiling lowers by record and never rises on the same data — ACC-56.
15. **No reproduction in the producer's environment** — ACC-65.
16. **No qualifying verdict from an unqualified verifier**, and "mechanical" means V0 and V1 only — ACC-61, ACC-62.
17. **No failed experiment without a recorded outcome**, and an implementation failure never refutes a hypothesis — ACC-63, ACC-64.
18. **No hypothesis or principle mutated in place** — a change is a new version naming its parent and its operator — ACC-57.
19. **No human intervention without an audit record**, and no timeout, learned preference or inbound message creates an approval — ACC-68, ACC-69.
20. **No adapted mechanism without lineage** — a pinned commit, a licence read at the source, a characterisation suite, and a statement of what it may never decide — ACC-73, ACC-74.

The following were added at baseline v1.3.0 with `ADR-011` to `ADR-019`. Where
the previous ten constrain what may be **believed**, these constrain **how the
work is carried out**.

21. **Substantial scientific execution stays multi-agent**, and independence is a profile rather than a count. Optimisation targets the conversation, the context and the assurance route — never the cohort — ACC-081.
22. **Peer output is embargoed until initial positions are sealed** — ACC-082.
23. **A majority cannot close a material challenge** — ACC-090.
24. **The blackboard is deletable.** Exchange is typed and delta-only, no entry is evidence, and none may be promoted to a claim — ACC-085.
25. **Budget degrades verbosity, never the cohort and never assurance** — ACC-099, ACC-101.
26. **A verifier may abstain, and abstention escalates.** No route is lowered by queue length or budget — ACC-108, ACC-109.
27. **The human judges before the machine recommends**, through every interface, and correcting costs no more than approving — ACC-110, ACC-112.
28. **The frozen specification and the running code must still agree** — ACC-104.
29. **Every contributing model invocation carries an execution fingerprint**, and a hosted black box does not yield an `EXACT` reproduction claim — ACC-115, ACC-116.
30. **A benchmark score carries the conditions it was produced under** — ACC-118.
31. **One canonical owner per kind of state**, and every projection rebuilds losslessly — ACC-119.
32. **`UNKNOWN` is a legitimate failure classification** — ACC-094.

> **These are constraints on what may be believed, not on what may be tried.**
> Every one of them permits the work and refuses the *record* of the work when
> the record would claim more than the work established. The v1.3.0 additions
> extend that: they permit the work and refuse the *shortcut* — the cheaper
> cohort, the skipped assurance, the recommendation shown first.

---

## 13. Where to go next

| Question | File |
|---|---|
| What is the state, what is next? | `03 - Implementation/session_handover_*` then the Cockpit |
| What happened, with evidence? | `implementation_log.md` |
| What is actually broken? | `docs/review/FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md` |
| What should be added to the architecture? | `AETHRION_IDEAL_STRUCTURE.md` |
| How do agents work? | `AETHRION_SKILL_LAYER.md` — **§14 first** — and `skills/` |
| Who executes what? | `AETHRION_ROLE_MODEL_ASSIGNMENT.md` |
| What is adopted rather than invented? | `AETHRION_EXTERNAL_STANDARDS.md` |
| Which mechanism was taken from which project, and what may it never decide? | `../../provenance/README.md` · `AETHRION_COMPONENT_REUSE.md` §9.2 · `ADR-004` |
| Where does a published number come from? | `ADR-007` · Figure 10 |
| What does "verify" mean here? | `ADR-008` · Figure 12 |
| What is remembered, and which store may support a claim? | `ADR-005` · Figure 11 |
| How does a cohort collaborate, and why is it not a cost lever? | `ADR-011` · `ADR-013` · §4.1.1 |
| Who owns which truth, and what happens when a projection disagrees? | `ADR-014` |
| When does each verification class run, and what if the verifier cannot tell? | `ADR-015` |
| Why does the human see the evidence before the recommendation? | `ADR-016` |
| What makes a benchmark score mean anything? | `ADR-017` |
| The plan itself | `planning/commissioning/` — canonical, hash-sealed |
