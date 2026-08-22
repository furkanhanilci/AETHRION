<p align="center">
  <img src="docs/assets/branding/aethrion-logo.png" alt="AETHRION" width="150">
</p>

<h1 align="center">AETHRION</h1>

<p align="center"><strong>Agentic Intelligence Research Layer</strong></p>

---

AETHRION — Agentic Intelligence Research Layer — is an evidence-centred,
auditable research system. Its central thesis: **agents produce, machines
verify, humans decide** — and those three roles are kept structurally separate.

`AIRL` is the abbreviation of the descriptor, and it survives inside the system
as a technical term: the G0–G10 control layer is the *Agentic Intelligence
Research Layer*, and the skill metadata namespace, the source-registry field and
the bridge service all carry the `airl` prefix. It is not the product name.
[`docs/branding.md`](docs/branding.md) records which is which.

**In one paragraph.** A capable model's characteristic failure is not
incompetence but plausibility: fluent, well-cited, confident output that is
wrong, and that no amount of further model capability detects from the inside.
AETHRION answers that by treating model output as a hypothesis which must survive
mechanical verification, independent review and a human decision before it
becomes a claim — with every claim traceable back to an exact source span and
forward to a signed attestation. This repository holds the target architecture
for that system, the execution discipline agents work under, and the one vertical
slice that actually runs today.

**The evidence-chain idea is not original to this project.** Google Research
published *Science One / ScientistOne* around the same principle —
**Chain-of-Evidence** — and, unlike this repository, measured it on 75 generated
papers. What differs here is scope: Science One asks whether an autonomous system
can produce verifiable papers; AETHRION asks under what governance a claim may be
believed at all, including its own. That is a broader question, harder to
demonstrate, and today **answered only on paper**. The comparison, and where
those systems are simply ahead, is in
[`AETHRION_RELATED_SYSTEMS.md`](docs/architecture/AETHRION_RELATED_SYSTEMS.md).

**A plan is not evidence of implementation**; the table below separates the two,
and every document here is written under [`docs/DOCUMENT_STANDARD.md`](docs/DOCUMENT_STANDARD.md),
whose central rule is that distance from working software is stated rather than
implied.

| Area | Status | Location |
|---|---|---|
| Literature bridge V0 | ✅ **Working**, locally accepted | `src/airl_bridge/` |
| Zotero → Obsidian projection | ✅ Working, read-only at the Zotero boundary | `src/airl_bridge/obsidian.py` |
| Hermes MCP access | ✅ Working, five read-only tools | `src/airl_bridge/mcp_server.py` |
| Shared contract core | ⚠️ `TECH_COMPLETE` — no production consumer | `src/airl_framework/` |
| Skill registry (52 skills, two families) | ✅ Format-conformant · ⚠️ wired for Claude Code only · 📐 behaviour **not yet tested** | `skills/` |
| Obsidian information architecture | ✅ V0 ready | `vault_baseline/` |
| Target architecture and skill layer | 📐 Designed, awaiting decision | `docs/architecture/` |
| Commissioning programme — **baseline v1.0.2** | ⬜ Planned, not started; 141 package documents, 51 scenarios | `planning/commissioning/` |
| Interim evidence policy (WP-000) | ✅ `TECH_COMPLETE` — tooling implemented, specimen issued and verified | `scripts/evidence_manifest.py` · `delivery/WP-000/` |
| Verification on push (BVC-01) | 📐 Decided and written, **not yet active** — needs a workflow-scoped token | `deploy/bvc-01-verify.yml` |
| Document production (authoring + figures + reporting) | 📐 Skill and reference modules written; resolution checks run · **no renderer installed** | `skills/authoring-research-documents/` |
| Reference verification (CoE Audit check 1) | ✅ **Working and measured** — 81.8% of the registry corroborated | `scripts/verify_references.py` |
| Source monitoring (first slice of G10) | ✅ **Working** — positive control fires; 18 of 33 sources carry no DOI | `scripts/monitor_sources.py` |

## Layout

```
src/          Bridge component and the shared contract core
tests/        Test suite
skills/       52 skills — HOW agents work; engineering + scientific + shared
planning/     WP-000, WP-001..140, ACC-01..51 (hash-sealed canonical plan, baseline v1.0.2)
docs/         Architecture, review, branding and operations documents
docs/assets/  Branding assets — the logo, and the rules that keep it canonical
schemas/      Shared contract schemas
delivery/     Per-package evidence packages — signed manifests and anchors
deploy/       systemd unit files
scripts/      Acceptance, smoke, skill-validation, figure and mirror generation
docs/figures/ Publication figures — generated, never hand-edited
vault_baseline/  Versioned copy of the Obsidian vault
```

Three surfaces exist, and only one of them is authoritative:

![Repository, vault and the outside world, with direction on every edge](docs/figures/aethrion_topology.svg)

*Figure 9 — Everything is authored in the repository. The Obsidian vault is
produced from it and never edited back; the mirror overwrites, so the failure
mode of editing the vault is losing that edit, not corrupting the source.
External bibliographic services are read at verification time and their answers
are recorded, never assumed. Generated by `scripts/fig_topology.py`.*

## Where to start

| Question | Document |
|---|---|
| **What is this system?** — explained and diagrammed | [`docs/architecture/AETHRION_ARCHITECTURE.md`](docs/architecture/AETHRION_ARCHITECTURE.md) |
| What actually exists today? | [`docs/review/2026-08-22_remediation_verification.md`](docs/review/2026-08-22_remediation_verification.md) — current state against the frozen audit |
| **What** should be added to the target architecture? | [`docs/architecture/AETHRION_IDEAL_STRUCTURE.md`](docs/architecture/AETHRION_IDEAL_STRUCTURE.md) |
| **How** should agents work? | [`docs/architecture/AETHRION_SKILL_LAYER.md`](docs/architecture/AETHRION_SKILL_LAYER.md) · [`skills/README.md`](skills/README.md) |
| **Who** performs each role — human, model or code? | [Roles](#6-roles--who-is-accountable-for-what) below · [`AETHRION_ROLES.md`](docs/architecture/AETHRION_ROLES.md) — definitions and authority flows · [`AETHRION_ROLE_MODEL_ASSIGNMENT.md`](docs/architecture/AETHRION_ROLE_MODEL_ASSIGNMENT.md) — which model |
| How are the figures produced? | [`docs/figures/README.md`](docs/figures/README.md) — inventory and design specification |
| How are these documents written? | [`docs/DOCUMENT_STANDARD.md`](docs/DOCUMENT_STANDARD.md) — structure, status vocabulary, honesty rules |
| What has been decided, and why? | [`ADR-001`](docs/architecture/ADR-001_solo_operator_independence.md) independence · [`ADR-002`](docs/architecture/ADR-002_bootstrap_verification_control.md) verification control · [`ADR-003`](docs/architecture/ADR-003_trusted_control_and_policy.md) trusted control and policy |
| Licensing and attribution | [`NOTICE`](NOTICE) |
| What is **adopted** rather than invented? | [`docs/architecture/AETHRION_EXTERNAL_STANDARDS.md`](docs/architecture/AETHRION_EXTERNAL_STANDARDS.md) |
| How does this compare to Science One, PaperQA2, AI Scientist? | [`docs/architecture/AETHRION_RELATED_SYSTEMS.md`](docs/architecture/AETHRION_RELATED_SYSTEMS.md) |
| Which mature components does it build on? | [`docs/architecture/AETHRION_COMPONENT_REUSE.md`](docs/architecture/AETHRION_COMPONENT_REUSE.md) |
| **What has actually been measured?** | [`delivery/measurements/`](delivery/measurements/) — one real result so far |
| Architecture of the working vertical slice | [`docs/ARCHITECTURE_V0.md`](docs/ARCHITECTURE_V0.md) |
| Day-to-day operation | [`docs/OPERATIONS.md`](docs/OPERATIONS.md) |
| The full programme plan | [`planning/commissioning/README.md`](planning/commissioning/README.md) |

---

# Architecture

Full reference with every diagram: [`docs/architecture/AETHRION_ARCHITECTURE.md`](docs/architecture/AETHRION_ARCHITECTURE.md).
What follows is the shape of the system in one page.

## 1. Why this is not an assistant

A normal AI research assistant is a pipeline from a question to an answer, and
whatever comes out is trusted because a capable model produced it:

```mermaid
flowchart LR
    U["Human question"] --> L["LLM"] --> S["Search and summarise"] --> A["Answer"]
    style A fill:#FBEFD6,stroke:#E69F00,color:#000
```

AETHRION starts from the opposite assumption: **a fluent, confident, well-cited,
entirely wrong result is the normal failure mode of a capable model**, and no
amount of model capability detects it from the inside. So model output is a
*hypothesis* that must survive mechanical verification, independent review and a
human decision before it becomes a claim.

```mermaid
flowchart TD
    A["AGENT<br/>produces<br/>'I think this is right'"]
    M["MACHINE<br/>verifies what is verifiable<br/>hashes · statistics · entailment · independence"]
    H["HUMAN<br/>decides<br/>'I accept this claim on this evidence'"]
    A -->|"not sufficient on its own"| M
    M -->|"passes only what survives"| H
    H -->|"decision recorded, never delegated"| R["DecisionRecord"]
    M -.->|"fails: back with a finding, never a waiver"| A
    style A fill:#DDEAF4,stroke:#0072B2,color:#000
    style M fill:#E0F3EC,stroke:#009E73,color:#000
    style H fill:#F7E2D6,stroke:#D55E00,color:#000
    style R fill:#F5E4EE,stroke:#CC79A7,color:#000
```

The failure mode being designed out is the ordinary multi-agent pattern —
*agent A produces, agent B reads it, agent B says "looks good", accepted*. Two
models from the same family share training lineage and therefore share errors;
agreement between them is correlation, not confirmation.

**The assignment rule that follows from this:**

```mermaid
flowchart TD
    Q{"Can this step be<br/>verified mechanically?"}
    Q -->|Yes| M["The mechanical check runs FIRST<br/>and the model cannot override it"]
    Q -->|No| P["A model may produce,<br/>but its output must be falsifiable"]
    P --> F{"Can the output be reduced to<br/>something a machine can check?"}
    F -->|No| S["It is a suggestion, not evidence"]
    F -->|Yes| M
    style M fill:#E0F3EC,stroke:#009E73,color:#000
    style S fill:#FBEFD6,stroke:#E69F00,color:#000
```

## 2. The evidence chain

Nothing becomes knowledge by being asserted. It becomes knowledge by surviving a
chain in which **every link is addressable**:

![The evidence chain, with implemented and unimplemented links marked](docs/figures/aethrion_evidence_chain.svg)

*Figure 2 — The chain, its revision loop, and the attestation that makes a link
admissible. Solid nodes are implemented and verified locally; hollow dashed nodes
are designed and not built — nine of the ten.*

```mermaid
flowchart RL
    P["Published sentence"] -->|"cites"| D["DecisionRecord<br/>who accepted it, on what"]
    D -->|"rests on"| RV["Review · Reproduction<br/>who challenged it, did it hold"]
    RV -->|"rests on"| R["ExperimentRun<br/>code, data, environment, hash"]
    R -->|"tests"| C["ClaimVersion<br/>the assertion, versioned"]
    C -->|"grounded in"| ES["EvidenceSpan<br/>the exact sentence in the exact paper"]
    ES -->|"located in"| SR["SourceRepresentation<br/>parsed, hashed, re-derivable"]
    SR -->|"is"| S["Source"]
    RT(["Source retracted"]) -.->|"cascade forward:<br/>every dependent claim is flagged,<br/>none silently survives"| C
    style ES fill:#E0F3EC,stroke:#009E73,color:#000
    style D fill:#F7E2D6,stroke:#D55E00,color:#000
    style RT fill:#F5E4EE,stroke:#CC79A7,color:#000
```

The figure above draws the chain forwards, as it is built. This diagram draws it
**backwards, as it is interrogated** — because that is the direction that matters
when someone asks *"why do you believe that?"* or when a source is retracted
three years later. A chain that only runs forwards is a provenance log; a chain
that runs both ways is an accountability structure.

And **the loop closes**: a claim is never permanently true, and `VERIFIED` is
explicitly not an irreversible state. Monitoring runs after publication precisely
so that the arrow above can be drawn years later.

## 3. The G0–G10 research lifecycle

The spine of the system. Each gate has a frozen output that does not change
without a recorded supersession.

![The AETHRION research lifecycle: eleven gates by three actor classes](docs/figures/aethrion_lifecycle.svg)

*Figure 1 — Reading down is time; reading across is who may act. At every gate
the mechanical check runs first and cannot be overridden, a model may produce but
never decide, and a human holds authority. The hatched cells at G5 and G7a are
the design, not an omission. Generated by `scripts/fig_lifecycle.py`.*

```mermaid
flowchart TD
    G0["G0 Intake<br/>IntakeRecord"]
    G1["G1 Charter<br/>ProjectCharter · ControlPlan"]
    G2["G2 Protocol<br/>ProtocolManifest"]
    G2B["G2b Analysis Plan<br/>AnalysisPlanManifest"]
    IPA["In-Principle Acceptance<br/>accepted on method, not on outcome"]
    G3["G3 Literature<br/>LiteratureSetManifest"]
    G4["G4 Baseline<br/>BaselineBundle · FalsificationPlan"]
    G5["G5 Execute<br/>ExperimentRun · no agentic<br/>methodological discretion"]
    G6["G6 Assurance<br/>mechanical, blind, adversarial, disagreement"]
    G7A["G7a Reproduction<br/>same manifest, same seed · deterministic"]
    G7B["G7b Replication<br/>different implementation · distribution test"]
    G8["G8 Decision<br/>DecisionRecord · HUMAN ONLY"]
    G9["G9 Publish<br/>PublicationPackage"]
    G10["G10 Monitor<br/>retraction · citation · CVE · conflict"]
    G0 --> G1 --> G2 --> MODE{"research_mode?"}
    MODE -->|exploratory| G3
    MODE -->|replication| RC["Locked replication contract"] --> G3
    MODE -->|confirmatory| G2B --> IPA --> G3
    G3 --> G4 --> G5 --> G6
    G6 --> G7A --> G7B --> G8 --> G9 --> G10
    G10 -.->|"material signal"| G2
    G6 -.->|"three failed explanations"| G2
    style G5 fill:#E0F3EC,stroke:#009E73,color:#000
    style G7A fill:#E0F3EC,stroke:#009E73,color:#000
    style G8 fill:#F7E2D6,stroke:#D55E00,color:#000
    style IPA fill:#FBEFD6,stroke:#E69F00,color:#000
```

| Gate | The failure it exists to prevent |
|---|---|
| **G0** | Redoing work that already exists; unowned work |
| **G1** | A model inventing its own research objective |
| **G2** | Changing the method after seeing the result |
| **G2b** | Choosing the analysis that gives the nicest answer |
| **G3** | An evidence base that cannot be re-derived |
| **G4** | Only asking how to confirm, never how to refute |
| **G5** | Model bias entering the measurement itself |
| **G6** | "Looks good" counted as independent review |
| **G7a** | A result nobody can obtain twice |
| **G7b** | Confusing "same numbers" with "same conclusion" |
| **G8** | A model deciding what the laboratory believes |
| **G9** | A sentence claiming more than its evidence supports |
| **G10** | Treating a published claim as permanently true |

**In-principle acceptance** sits in the flow for one reason: without a
commitment made *before* the result exists, publication bias survives every
other control — the protocol is frozen, the result comes back negative, and the
human simply declines to publish.

It is **conditional, not universal**: required for `confirmatory` work, a locked
replication contract for `replication`, and not required for `exploratory` work —
which in exchange may never label its claims confirmatory. Forcing Registered
Report ceremony onto exploration would only teach people to mislabel confirmatory
work as exploratory. The classification is fail-closed: absent or ambiguous, it
resolves to `confirmatory`.

**"No model at G5"** means no *agentic methodological discretion* during a frozen
execution. The subject of the experiment may itself be a model — a frozen model
under test, a preregistered inference pipeline. What is forbidden is an agent
changing a threshold or a stopping point mid-run because the result looks wrong.
The model may be the instrument; it may not be the methodologist.

**Inside G6**, the heaviest gate:

```mermaid
flowchart TD
    IN["Result and evidence"] --> M["G6-0 Mechanical<br/>hashes · manifests · statcheck · GRIM<br/>citation entailment · schema · artifact integrity"]
    M -->|fails| BACK["Returned with a finding<br/>no model can waive this"]
    M -->|passes| B["G6-1 Blind review<br/>ReviewPacket built by a program<br/>reviewer never sees producer reasoning"]
    B --> A["G6-2 Adversarial<br/>ACH matrix: which hypotheses does<br/>this evidence eliminate?"]
    A --> D{"G6-3 Disagreement"}
    D -->|converges| OUT["Verdict and ProducerResponse"]
    D -->|"does not converge"| AR["Delphi / IDEA rounds, then arbiter<br/>bounded: round limit plus breaker"]
    AR --> OUT
    style M fill:#E0F3EC,stroke:#009E73,color:#000
    style BACK fill:#F7E2D6,stroke:#D55E00,color:#000
```

The `ReviewPacket` is built by a **deterministic program, not a prompt** — only
then can "what exactly did the reviewer see?" be answered afterwards. The
adversarial reviewer is scored on **the quality of its refutation**, not on
approval speed.

## 4. The planes

```mermaid
flowchart TD
    subgraph EXP["EXPERIENCE PLANE"]
        E1["Human intent · approvals · decision queue<br/>Obsidian vault · cockpit · dashboards"]
    end
    subgraph CTL["CONTROL PLANE"]
        C1["Temporal: G0-G10 lifecycle, gates<br/>retry · timeout · compensation"]
    end
    subgraph EVT["EVENT PLANE"]
        V1["NATS JetStream: post-commit events<br/>integration · fan-out · replay"]
    end
    subgraph COG["COGNITION PLANE"]
        G1["LangGraph: bounded agent reasoning<br/>inside a single task, never across gates"]
    end
    subgraph EXE["EXECUTION PLANE"]
        X1["Sandbox · Tool Broker · Execution Broker<br/>credentials never reach the agent"]
    end
    subgraph EVD["EVIDENCE AND OPERATIONS PLANE"]
        D1["Sources · claims · runs · manifests<br/>ledgers · object store · audit"]
    end
    subgraph MET["METASCIENCE PLANE - proposed, not accepted"]
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

### The trust boundary that cuts across all of them

The planes above answer *where* a thing runs. ADR-003 answers a different
question that no plane diagram can: *whose words are allowed to change what the
system does.*

![The trust boundary: an injected instruction followed to the point where it is denied](docs/figures/aethrion_trust.svg)

*Figure 7 — The control plane holds the goal and every privilege. The data plane
holds everything an outsider can write, including whatever a PDF hides in
white-on-white. Content crosses; authority does not. Generated by
`scripts/fig_trust.py`.*

```mermaid
flowchart TD
    subgraph TRUST["TRUSTED - may act"]
        T1["Task and plan"]
        T2["Tool broker · credentials · write paths"]
    end
    subgraph DATA["UNTRUSTED - may only be read"]
        U1["Paper full text · tool output<br/>web pages · reviewer comments"]
    end
    U1 -->|"content crosses:<br/>quoted, attributed, never obeyed"| T1
    U1 -.->|"authority never crosses"| BLOCK[["no such edge exists"]]
    T1 --> PDP{"Cedar<br/>permit or forbid?"}
    PDP -->|"permit"| ACT["Tool call executes,<br/>decision recorded with the run"]
    PDP -->|"forbid, and by default"| DENY["Denied.<br/>An anomaly is a denial, not a warning"]
    style TRUST fill:#DDEAF4,stroke:#0072B2,color:#000
    style DATA fill:#FBEFD6,stroke:#E69F00,color:#000
    style PDP fill:#F5E4EE,stroke:#CC79A7,color:#000
    style DENY fill:#F7E2D6,stroke:#D55E00,color:#000
    style BLOCK fill:#FFFFFF,stroke:#D55E00,color:#000
```

The design is borrowed rather than invented: it is the CaMeL pattern, adopted as
a `PATTERN` under the adoption taxonomy, with Cedar as the policy engine
`DEPENDENCY` and AgentDojo named as the `BENCHMARK` that would falsify it.
**None of it has been run here** — no policy set is authored in this repository.
The cut in Figure 7 is a decision on paper, and the figure says so.

**Temporal is the process authority; LangGraph is not.** A research project lives
for months and must survive process restarts, model changes and human absence —
an agent graph is the wrong place to keep that state. Conversely, Temporal is the
wrong place to reason. **NATS carries events, not authority**: if the entire
stream were deleted, gate state would still be recoverable from Temporal.

## 5. The skill layer — two families, one shared core

A `RoleContract` says **who** an agent is — purpose, tools, data classes, budget.
Every one of those is a *boundary*; none of them says **which procedure to
follow**. Skills close that gap.

```mermaid
flowchart TD
    R["using-aethrion<br/>router: classify first"]
    R --> Q{"What kind of task?"}
    Q -->|"building AETHRION"| ENG["ENGINEERING · 11<br/>vendored from obra/superpowers<br/>test-driven-development<br/>systematic-debugging · writing-plans<br/>worktrees · code review · subagents"]
    Q -->|"doing research"| SCI["SCIENTIFIC · 28<br/>AETHRION-native<br/>preregistration-discipline<br/>searching-literature · extracting-evidence<br/>blind and adversarial review · metascience"]
    Q -->|"always"| SH["SHARED · 10<br/>verification-before-completion<br/>independence-discipline<br/>evidence-before-claim · scope-discipline"]
    ENG --> TC["TaskContract<br/>skills_loaded plus skill_bundle_hash"]
    SCI --> TC
    SH --> TC
    TC --> EV["enters the evidence chain"]
    style ENG fill:#DDEAF4,stroke:#0072B2,color:#000
    style SCI fill:#E0F3EC,stroke:#009E73,color:#000
    style SH fill:#F5E4EE,stroke:#CC79A7,color:#000
```

> **Research adaptations extend their engineering counterparts; they never
> replace them.** AETHRION is simultaneously a laboratory and a software platform,
> and it needs both disciplines at once.

| Software engineering | Scientific research | The shared rule |
|---|---|---|
| Test before code | Preregistration before result | You do not get to pick the criterion after seeing the outcome |
| Bug root-cause tracing | Anomaly root-cause tracing | Three failed explanations means the architecture is wrong, not the fix |
| Fresh-context implementer | Fresh-context analyst | Whoever produced it cannot be the one who checks it |
| Reviewer sees the diff, not the reasoning | Reviewer sees the packet, not the trace | Information asymmetry is what makes review independent |
| Verification before "done" | Verification before "claimed" | Memory is not evidence |

Skills conform to the [Agent Skills open standard](https://agentskills.io),
which Claude Code, Codex, OpenCode, Cursor, Copilot, Gemini CLI and Hermes Agent
all implement — so the registry is **format-compatible** with each of them.
**A skill that does not load governs nothing**, so conformance is checked
mechanically by `scripts/validate_skills.py`.

> Format compatibility is not behavioural compatibility. Whether a harness loads
> the right skill at the right moment, and keeps it across context compaction, is
> what ACC-42, ACC-44 and ACC-45 establish under WP-048 — and that is **not**
> established today. Only the Claude Code path is wired, via `.claude/skills`.

## 6. Roles — who is accountable for what

Fourteen **durable functions**. Not fourteen people: a role is a function, and
one person may legally hold several of them.

![Role authority tiers and separation constraints](docs/figures/aethrion_roles.svg)

*Figure 3 — Authority tiers with the actor composition of each role (**X**
mechanical, **M** model, **H** human), and the constraint resolution that decides
whether one operator may hold two roles at once. Full definitions — mandate,
what each role decides, and what it may never do — are in
[`docs/architecture/AETHRION_ROLES.md`](docs/architecture/AETHRION_ROLES.md).*

```mermaid
flowchart TD
    subgraph AUTH["👤 HUMAN AUTHORITY — never a model"]
        A1["Project Decision Owner<br/>signs G8 · G9"]
        A2["Safety / Data Owner<br/>owns the data class · blocks anything"]
        A3["Research Integrity Officer<br/>judges integrity cases · blocks anything"]
        A4["Assurance Lead<br/>assigns reviewers · blocks G6 · G7"]
    end
    subgraph OWN["👤 + 🤖 OWNERSHIP — human decides, model drafts"]
        B1["Scientific Owner<br/>writes the decision question · G2"]
        B2["Statistical Methods Owner<br/>locks the analysis plan · G2 · G4 · G6"]
        B3["Evidence Lead<br/>freezes the literature set · G3"]
        B4["Engineering Owner<br/>approves code · G4 · G5"]
    end
    subgraph PROD["🤖 + 👤 PRODUCTION — model produces, human approves"]
        C1["Research Software Engineer<br/>reproducibility · badges · G7"]
        C2["Data Steward<br/>datasets · identifiers · G1 · G9"]
        C3["Red Team Lead<br/>pre-mortem · control injection · G4"]
    end
    subgraph MECH["⚙️ + 🤖 MECHANICAL-FIRST"]
        D1["Scientific Editor<br/>scope conformance · G9"]
        D2["Knowledge Steward<br/>contradiction sweeps · G0"]
        D3["Metascience Lead<br/>measures — <b>does not block</b>"]
    end
    AUTH -.->|"authority flows down"| OWN -.-> PROD -.-> MECH
    MECH -.->|"findings flow up · never waivers"| AUTH

    style AUTH fill:#F7E2D6,stroke:#D55E00,color:#000
    style OWN fill:#FBEFD6,stroke:#E69F00,color:#000
    style PROD fill:#DDEAF4,stroke:#0072B2,color:#000
    style MECH fill:#E0F3EC,stroke:#009E73,color:#000
```

| Role | Actor | Can block | The one thing it must never delegate |
|---|---|---|---|
| Project Decision Owner | 👤 | G8, G9 | Deciding what the laboratory believes |
| Safety / Data Owner | 👤 | all | The data-class decision |
| Research Integrity Officer | 👤 + ⚙️ | all | The judgement on an integrity case |
| Assurance Lead | 👤 + ⚙️ | G6, G7 | Who reviews whom |
| Scientific Owner | 👤 + 🤖 draft | G2 | Writing the decision question |
| Statistical Methods Owner | 👤 + 🤖 | G2, G4, G6 | Locking the analysis plan |
| Evidence Lead | 👤 + 🤖 | G3 | The freeze decision |
| Engineering Owner | 🤖 + 👤 approval | G4, G5 | Approving what ships |
| Research Software Engineer | 🤖 + 👤 approval | G7 | Assigning the reproducibility badge |
| Data Steward | 🤖 + 👤 approval | G1, G9 | Publishing an identifier |
| Scientific Editor | ⚙️ + 🤖 | G9 | — scope conformance is mechanical |
| Red Team Lead | 🤖 + 👤 | G4 | — |
| Knowledge Steward | ⚙️ + 🤖 | G0 | — |
| Metascience Lead | 👤 + ⚙️ | **nothing** | Measuring without gatekeeping |

**Metascience Lead blocks nothing on purpose.** A function that both measures the
laboratory and can veto its work stops measuring honestly.

### How a gate actually resolves

Every gate runs the same three-stage resolution, and the order is the whole
design:

```mermaid
flowchart TD
    IN["Gate entry"] --> MECH{"Is there a mechanical<br/>check for this?"}
    MECH -->|Yes| RUN["⚙️ Run it FIRST"]
    RUN --> PASS{"Passed?"}
    PASS -->|No| BLOCK["Gate blocked with a finding<br/><b>no model may waive it</b><br/><i>no human may waive a non-waivable one</i>"]
    PASS -->|Yes| MODEL
    MECH -->|No| MODEL["🤖 Model produces<br/>draft · review · refutation<br/><i>output must be falsifiable</i>"]
    MODEL --> AUTH{"Does this gate carry<br/>decision authority?"}
    AUTH -->|"G8 · G9 · freeze · lock · sign"| HUMAN["👤 Human decides<br/>recorded, never delegated"]
    AUTH -->|No| REC["Gate record produced<br/>and the flow continues"]
    HUMAN --> REC

    style RUN fill:#E0F3EC,stroke:#009E73,color:#000
    style BLOCK fill:#F7E2D6,stroke:#D55E00,color:#000
    style MODEL fill:#DDEAF4,stroke:#0072B2,color:#000
    style HUMAN fill:#F7E2D6,stroke:#D55E00,color:#000
```

Applied gate by gate, that produces:

| Gate | ⚙️ Mechanical | 🤖 Model | 👤 Human |
|---|---|---|---|
| **G0** intake | duplicate search | triage | greenlight |
| **G1** charter | risk → assurance policy engine | charter draft | **writes the decision question** |
| **G2** protocol | template + placeholder sweep | protocol draft · pre-mortem · different-family review | Scientific + Statistical Owner **sign** |
| **G2b** analysis plan | — | plan draft · power analysis | Statistical Methods Owner **locks** |
| **G3** literature | GROBID · DOI · dedup · hashing | query plan · screening | Evidence Lead **freezes** |
| **G4** baseline | the baseline run | compute plan · pre-mortem | budget approval |
| **G5** execute | **the experiment itself** | **none** — unless the model is the subject | — |
| **G6-0** mechanical | statcheck · GRIM · entailment · hashes | **none** | — |
| **G6-1** blind | `ReviewPacketBuilder`, a program | N reviewers, different family | — |
| **G6-2** adversarial | the ACH matrix | adversarial refutation | — |
| **G7a** reproduce | same manifest, same seed | **none** | — |
| **G7b** replicate | distribution test | — | RSE assigns the badge |
| **G8** decide | package completeness | **recommendation only** | **DECIDES — human only, under quota** |
| **G9** publish | **scope conformance** · RO-Crate · hashes | text draft | Decision Owner + Editor |
| **G10** monitor | Crossref · Retraction Watch · CVE | signal triage | decides on a material signal |

The empty model cells at **G5**, **G6-0** and **G7a** are the point, not an
omission: those are the layers that stay free of model bias.

### A role is a function, not a person

This is what makes the catalogue survivable in a one-person laboratory. Roles
are **bound**, and independence is expressed as separation constraints rather
than headcount:

```mermaid
flowchart TD
    R["RoleBinding<br/>role_id: statistical_methods_owner"]
    R --> ACT["actor<br/>human · model_profile · mechanical<br/><i>any of them may be empty</i>"]
    R --> SEP["separation"]
    SEP --> S1["must_be_independent_from:<br/>experiment_analyst"]
    SEP --> S2["can_combine_with:<br/>scientific_owner ✅"]
    SEP --> S3["cannot_combine_with:<br/>final_independent_verifier ❌"]
    S1 --> ENG["Constraint engine<br/>admits or refuses the binding"]
    S2 --> ENG
    S3 --> ENG
    ENG --> OK["One person, several roles —<br/>legally, and provably"]

    style ENG fill:#E0F3EC,stroke:#009E73,color:#000
    style S3 fill:#F7E2D6,stroke:#D55E00,color:#000
    style S2 fill:#E0F3EC,stroke:#009E73,color:#000
```

The question stops being *"where do I find 73 owners and 114 verifiers?"* and
becomes *"which combinations am I willing to declare independent, and which must
stay mechanical or external?"*

> **This is the shape of an answer to finding C2, not the answer.** Which
> combinations count as independent in a one-person operation is still an open
> decision, and until it is made no work package can reach `ACCEPTED`.

### Independence is measured, not asserted

Reviewer independence has a quota that scales with the assurance class:

| Assurance | Producer effort | Reviewer effort | Adversarial | Reviewer quota | Model policy |
|---|---|---|---|---|---|
| **R1** | `medium` | `high` | — | 1, any family | hosted OK |
| **R2** | `high` | `high` | `xhigh` | 2, **different provider family** | hosted + full I/O logging |
| **R3** | `xhigh` | `xhigh` | `max` | 3, **different family** | **local open-weight mandatory** |

R3 requires a local model because a hosted model has no pinnable snapshot, and
without one G7a reproduction is structurally impossible. That is a constraint,
not a preference.

And the family rule is itself only a **proxy**: what is permanent is the measured
pairwise error correlation ρ between reviewer profiles. When the calibration set
exists, the measurement replaces the rule. A laboratory that never measures its
own independence assumption is repeating an assumption and calling it
verification.

## 7. How a document is produced

A document is a **projection of verified state**, not a generative act. The
pipeline runs evidence → claims → structure → prose → figures → QA → render, and
a renderer exiting zero decides nothing.

![The document production pipeline and where authority sits](docs/figures/aethrion_reporting.svg)

*Figure 5 — Formatting is downstream: stages 0–2 finish before a renderer is
chosen. The four packaging objects are distinct, and only the first exists here.
Every external tool in the authority band produces a signal; none of them
decides. Written up in [`authoring-research-documents`](skills/authoring-research-documents/SKILL.md).*

## 8. What this builds, and what it stands on

Almost every layer of the target system is a component someone else maintains
and tests. What this project owns is the control layer.

![The target stack, with adoption type and build status marked](docs/figures/aethrion_stack.svg)

*Figure 4 — Adoption type is drawn rather than captioned, because "reuse" is not
one thing: a dependency, a standard, a pattern and a benchmark create entirely
different obligations. Solid borders mark the three cells that are implemented;
everything dashed is a decision, not a running component. Details and rationale
in [`AETHRION_COMPONENT_REUSE.md`](docs/architecture/AETHRION_COMPONENT_REUSE.md).*

> **AETHRION should not invent its own PDF parser, screening engine, policy
> language, sandbox, experiment tracker or scholarly identifier.** Its
> contribution is the layer above them: which evidence, having passed which
> gate, permits which claim to be accepted.

## 9. How evidence is signed

Acceptance requires a signed `EvidenceManifest` in an immutable store — and that
store is WP-026, far downstream, which deadlocked the entire programme
(finding **C1**). The deadlock existed only because the store was assumed to be
ours to build. It is not:

```mermaid
flowchart TD
    A["Work package artefacts<br/>tests · environment · schema and policy versions"] --> B["in-toto Statement<br/>subject = artefact digest<br/>predicate = EvidenceManifest"]
    B --> C["DSSE envelope"]
    C --> D["Sigstore keyless signature<br/>short-lived OIDC-bound cert"]
    D --> E["Rekor transparency log<br/>append-only · inclusion proof"]
    E --> F["OpenTimestamps anchor<br/>WP-139 · hash-only"]
    F --> G["Verifier accepts<br/>package may reach ACCEPTED"]
    E -.->|"when WP-026 lands"| H["WORM object store<br/>log entry remains<br/>as an independent witness"]
    style E fill:#E0F3EC,stroke:#009E73,color:#000
    style G fill:#F7E2D6,stroke:#D55E00,color:#000
```

**Immutability is delegated, not deferred.** Rekor is a tamper-evident
transparency record **for signed metadata**, not an artifact store — WP-026 is
deferred behind it, not cancelled. And this resolves the *storage* half of C1
only: finding **C2**, who may act as an independent verifier in a one-person
operation, is a decision no standard makes. What the architecture now supplies is
its *shape* — independence expressed as `RoleBinding` separation constraints
rather than headcount, so one person holding several roles can be modelled
honestly. See
[`AETHRION_EXTERNAL_STANDARDS.md`](docs/architecture/AETHRION_EXTERNAL_STANDARDS.md).

## 10. Target versus reality

Everything above is the target. This section is the distance to it, and it is
the section to read first if you are deciding whether to trust anything else.

```mermaid
flowchart LR
    subgraph WORKING["RUNNING - verified locally"]
        W["Zotero read-only client<br/>SQLite source registry<br/>Obsidian projection<br/>Hermes MCP, 5 tools<br/>systemd units · 25 tests<br/>plan seal · 10 status checks<br/>signed evidence manifest<br/>9 generated figures"]
    end
    subgraph WRITTEN["WRITTEN - never executed"]
        S["52 skills, none behaviour-tested<br/>141 package documents<br/>51 acceptance scenarios<br/>role-to-model assignment rules<br/>4 authoring profiles"]
    end
    subgraph DESIGNED["DESIGNED - no code"]
        D["Temporal · LangGraph · NATS<br/>Tool Broker · Execution Broker<br/>Claim and Evidence Ledger<br/>Run Registry · Model Gateway<br/>G0-G10 engine · review pipeline<br/>Cedar policy set · metascience plane"]
    end
    WORKING -->|"one work package<br/>of 141"| WRITTEN
    WRITTEN -->|"the distance is much larger<br/>than the page count implies"| DESIGNED
    style WORKING fill:#E0F3EC,stroke:#009E73,color:#000
    style WRITTEN fill:#F5E4EE,stroke:#CC79A7,color:#000
    style DESIGNED fill:#FBEFD6,stroke:#E69F00,color:#000
```

![The commissioning programme: eleven waves, and the single package that has produced anything](docs/figures/aethrion_waves.svg)

*Figure 6 — Waves are dependency order, not dates: the plan has none. Package
counts are counted from the plan directory when the figure is generated, so this
figure cannot disagree with the plan it describes. Generated by
`scripts/fig_waves.py`.*

**Where the blockers actually stand.** Two of the original five have been closed
by decisions rather than by code, which is progress of a specific and limited
kind — a decision removes an unknown, it does not remove work:

| | Blocker | State |
|---|---|---|
| **C1** | Storage split between SQLite and the plan's target stores | **Closed.** WP-000 executed; the bootstrap tooling runs and a specimen manifest verifies |
| **C2** | Reviewer independence under a solo operator | **Closed by ADR-001.** R1 solo, R2 declared-partial, R3 `BLOCKED` — the constraint is now enforced rather than argued about |
| **H1** | Zotero ingest capped at 100 records | **Open.** Fix M9 first: pagination would turn a masked truncation into active data loss |
| **H2** | No deletion reconciliation | **Open.** A record removed upstream persists downstream |
| **H3** | The read-only boundary has no behavioural test | **Open.** It is asserted in code and in prose, and never exercised |
| **H4** | The contract core has no consumers | **Open.** Written, imported by nothing |
| **H5** | No continuous integration | **Staged, not active.** The workflow exists at `deploy/bvc-01-verify.yml` and has never run; see ADR-002 |

The honest summary is one sentence: **the parts that are verified are small and
real, and the parts that are large are documents.**

---

## The working vertical slice: Literature Bridge V0

```mermaid
flowchart TD
    Z["Zotero local API<br/>127.0.0.1:23119<br/>bibliographic authority"]
    Z -->|"READ ONLY<br/>no key · no write · no delete · no merge"| SV["airl-bridge.service<br/>FastAPI · systemd user unit"]
    SV --> DB["SQLite canonical registry<br/>stable AIRL source identity<br/>idempotent upsert"]
    DB --> OB["Obsidian projection<br/>70 - Literature Sets/Zotero Sources<br/>atomic write · manifest-owned deletion"]
    DB --> MCP["Hermes MCP server<br/>five read-only tools"]
    T["sync timer<br/>every 30 min"] -.-> SV
    MCP --> AG["Hermes or any MCP agent"]
    OB --> HU["Human synthesis<br/>20 - Source Notes"]
    style Z fill:#FBEFD6,stroke:#E69F00,color:#000
    style DB fill:#E0F3EC,stroke:#009E73,color:#000
    style MCP fill:#DDEAF4,stroke:#0072B2,color:#000
```

**Generated and human-authored content cannot collide.** The bridge deletes only
files recorded in its own projection manifest, so a markdown file a human drops
into the generated folder is not "stale" — it is simply not the bridge's.

The service listens on `127.0.0.1` only. It holds no Zotero API key, and the
codebase contains no Zotero write operation.

### Install

```bash
cd /home/otonom/Desktop/FH/AETHRION
uv sync --extra dev
cp .env.example .env      # then fill in your own paths
```

### Enable the Zotero Local API

1. Start Zotero
2. **Settings → Advanced → General**
3. Enable **Allow other applications on this computer to communicate with Zotero**
4. Keep port `23119` local — do not forward or expose it

```bash
uv run airl-bridge doctor
```

### Run

```bash
uv run airl-bridge serve

systemctl --user status airl-bridge.service
systemctl --user status airl-bridge-sync.timer
journalctl --user -u airl-bridge.service -n 50
```

A user timer runs the same local synchronisation every 30 minutes.

Local endpoints: [`/health`](http://127.0.0.1:8765/health) ·
[`/ready`](http://127.0.0.1:8765/ready) · [`/docs`](http://127.0.0.1:8765/docs)

### First synchronisation

```bash
curl -X POST 'http://127.0.0.1:8765/v1/sync?limit=100'
curl 'http://127.0.0.1:8765/v1/sources?limit=10'

# or without starting the server
uv run airl-bridge sync --limit 100
```

Repeated synchronisation is idempotent for the same Zotero library and item key.
Zotero-derived files live under the automatically managed `Zotero Sources`
branch and are regenerated from the canonical registry. Human synthesis stays in
`20 - Source Notes`; curated sets stay at the root of `70 - Literature Sets`.

> ⚠️ **Known limitation:** ingest is hard-capped at 100 records; there is no
> pagination and no `since=` incremental sync. Once the library exceeds 100
> sources, synchronisation silently becomes partial. See finding **H1** in the
> audit report.

### Verify

```bash
uv run pytest                          # 25 tests
uv run python scripts/mcp_smoke.py     # asserts the five-tool boundary; exits 1 on failure
uv run python scripts/acceptance_v0.py # data-independent structural acceptance
python3 scripts/validate_skills.py     # Agent Skills format + AIRL metadata contract
python3 scripts/make_figures.py --check # figures match generators, text fits its box
python3 scripts/validate_commissioning_plan.py  # the plan is internally consistent
python3 scripts/make_plan_indexes.py --check    # workstream indexes match their packages
python3 scripts/check_doc_consistency.py        # documents agree with the repository
python3 scripts/check_stale_claims.py          # no prose the repository has outgrown
uv run python scripts/write_status.py          # regenerate docs/STATUS.md
uv run python scripts/evidence_manifest.py verify \
    --manifest delivery/WP-000/evidence.dsse.json --tamper-demo
uv run python scripts/verify_references.py   # needs network; not part of BVC-01
uv run python scripts/monitor_sources.py     # G10 sweep; fails if its control stays silent
uv run python scripts/check_document.py delivery/specimen/aethrion-measurement-report.qmd
python3 scripts/check_reporting_registry.py  # adopted components remain auditable
(cd planning/commissioning && sha256sum -c 00_PROGRAM/SHA256SUMS.txt)
```

They run by hand today. The first six are **written** as a push-triggered
control — [`BVC-01`](deploy/bvc-01-verify.yml), a temporary measure under
[`ADR-002`](docs/architecture/ADR-002_bootstrap_verification_control.md) with a
named expiry and WP-024 as its retirement package — but it is **staged, not
active**: activating it needs a token with GitHub's `workflow` scope, and the
activation command is in ADR-002 §6.

**Neither the staged control nor its activation closes finding H5.** H5 is the absence of a CI *platform* — schema
validation, policy bundles, security scanning, provenance attestation,
integration testing — and that is WP-024, which hard-depends on three unbuilt
packages. What BVC-01 closes is narrower and worth naming precisely: the gap
between *the checks exist* and *the checks ran*. The Bridge-dependent checks and
the vault mirror checks stay manual, and their absence is recorded in the
workflow rather than hidden.

## Hermes MCP access

Hermes starts the `airl-bridge-mcp` server over stdio and sees exactly five
read-only tools: status, source search, source detail, category counts, and
possible-duplicate reporting. No synchronisation, write, delete or Zotero
mutation tool is exposed. The Hermes configuration pins an explicit five-tool
include list; MCP prompt and resource capabilities are disabled.

## Licensing and what this repository is for

This repository is **public to read and proprietary to use** — see
[`NOTICE`](NOTICE). That is a deliberate position and worth stating plainly,
because a framework arguing for open standards, reproducibility and external
verification while keeping its own implementation closed invites a fair
question.

The answer is that the two are different things. **The architecture is meant to
be read, argued with and reused as a reference**; the implementation is one
person's research infrastructure, not a product seeking adopters. Nothing here
asks anyone to depend on it, and if this ever becomes something a community is
expected to build on, the licence has to change first — a proprietary framework
cannot credibly ask for the interoperability it preaches.

Vendored third-party content keeps its own licence: the eleven engineering
skills are MIT from `obra/superpowers`, pinned by commit and attributed in
`NOTICE`.

## Status semantics

`WORKING` means a component has been verified locally.
`ACCEPTED` means an independent verifier accepted its evidence package.

**No work package is currently `ACCEPTED`.** That is not an oversight — the
mechanisms required to reach that state (signed evidence manifests, an immutable
store, an independent verifier) do not yet exist. See finding **C1** in the audit
report.

[**WP-000**](planning/commissioning/01_GOVERNANCE/WP-000_interim_evidence_policy.md)
removes the *storage* half of that blocker: the `EvidenceManifest` is a signed
in-toto attestation, issued and verified by `scripts/evidence_manifest.py`, and
tamper detection is exercised by tests rather than asserted. The implemented
profile is `airl-interim-v0.1` — local key, **no transparency log** — and each
manifest carries its own `limitations` list so it cannot be read as more than it
is.

The *independence* half — finding **C2** — is now **decided** in
[`ADR-001`](docs/architecture/ADR-001_solo_operator_independence.md): R1 solo;
R2 solo only under a declared partial-independence profile; **R3 `BLOCKED`
unless an external verifier is named.** So packages have an acceptance path, and
the laboratory does not claim independence it does not have.

## Verification

![What each check proves, and what it cannot see](docs/figures/aethrion_verification.svg)

*Figure 8 — One command runs all ten. Each row states the claim the check earns
and, beside it, the claim it does not — because a bundle that reports only green
teaches its reader to trust it for things it never examined. Generated by
`scripts/fig_verification.py`.*

```mermaid
flowchart LR
    CH["A document, plan,<br/>skill or figure changes"] --> DER["Truth is re-derived<br/>from the repository,<br/>never from memory"]
    DER --> RUN{"The bundle runs.<br/>Any warning<br/>is a failure"}
    RUN -->|"fails"| CH
    RUN -->|"passes"| ST["STATUS.md is regenerated<br/>and its own --check<br/>catches hand-editing"]
    ST --> EV["The evidence manifest<br/>is signed again<br/>and verifies"]
    EV -->|"or the change does not land"| CH
    style RUN fill:#E0F3EC,stroke:#009E73,color:#000
    style EV fill:#F7E2D6,stroke:#D55E00,color:#000
```

```
25/25 tests pass · plan seal 221/221 OK · plan semantics OK · service and timer active
WP-000 attestation: signature OK, 3 subject digests OK, tamper rejected
MCP smoke: 5 read-only tools, exits 1 when the Bridge is down
Acceptance: 11 structural checks pass, data-independent
Skills: 52/52 conform to the Agent Skills format and the AIRL metadata contract
Documents: declared counts match the repository; no decision record contradicts itself
References: 27/33 registry sources corroborated against Crossref, OpenAlex and arXiv
Monitoring: G10 sweep clean over 15 DOI-bearing sources; positive control fired
Figures: 9/9 match their generators; 0 text overflows out of their boxes
Mirror drift: 0 (208 plan files, 67 skill/doc/figure files)
Obsidian baseline and vault identical
```

Every check above is reproducible from a clean checkout with the Bridge running.
**None of them runs automatically** — the workflow that would run them is staged
at `deploy/bvc-01-verify.yml` and has never executed. Until it does, the guarantee
is "someone ran this", not "this cannot regress".

And all of it is internal consistency. The bundle can confirm that this
repository says the same thing everywhere and that its evidence verifies — and
every one of those statements would still hold for a corpus describing a system
that does not work. External truth enters through exactly two doors: reference
verification against Crossref, OpenAlex and arXiv, and the benchmarks named in
the adoption matrix, none of which has been run.
