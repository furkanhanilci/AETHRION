> [!info] Generated view
> This note is generated from `docs/architecture/AIRL_OS_RELATED_SYSTEMS.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# AIRL-OS — Related Systems and Positioning

| Field | Value |
|---|---|
| Document type | Architecture reference — comparative positioning |
| Scope | What comparable systems do, what AIRL-OS does differently, and what it does **not** do better |
| Sibling documents | `AIRL_OS_ARCHITECTURE.md` · `AIRL_OS_EXTERNAL_STANDARDS.md` |
| Status | `SPECIFIED` — the comparison is documented; **no head-to-head evaluation has been run** |
| Date | 2026-08-22 |

**In one paragraph.** The idea that every claim must carry a traceable chain back
to its evidence is **not original to this project**, and a reader who assumes
otherwise has been misled. Google Research published **Science One /
ScientistOne** in mid-2026 around exactly that principle, named **Chain-of-Evidence**,
and — unlike this repository — measured it on 75 generated papers. This document
states where AIRL-OS sits relative to that work and to the other systems in the
space, what it is genuinely doing differently, and where those systems are
simply ahead.

---

## 1. Why this document exists

An architecture that describes itself only against its own goals will always look
strong. The useful question is the one an external reviewer asks first:

> *"How is this different from Science One, and why not just use PaperQA2?"*

Answering it honestly costs some of the novelty claim and is worth more than
keeping it.

---

## 2. The systems

| System | What it is | Where it is ahead of AIRL-OS |
|---|---|---|
| **ScientistOne / Science One** (Google Research, 2026) | End-to-end autonomous research built natively around **Chain-of-Evidence**, plus a post-hoc **CoE Audit** | Everything measurable. It ran, produced papers, and was audited |
| **The AI Scientist v2** (Sakana AI) | Autonomous hypothesis → experiment → analysis → manuscript, via agentic tree search | It actually completes the loop end to end |
| **Robin** (FutureHouse) | Multi-agent discovery that produced a real therapeutic hypothesis, published in the literature | Empirical outcome in a real scientific domain |
| **PaperQA2** (FutureHouse) | Retrieval and evidence-gathering over scientific literature with in-text citations | A far more mature literature subsystem than G3 will be for a long time |
| **AI co-scientist** (Google DeepMind) | Multi-agent hypothesis generation with explicit ranking | Hypothesis generation and tournament ranking |
| **LangGraph / AutoGen research agents** | General multi-agent orchestration | Maturity, adoption, ecosystem |

---

## 3. Chain-of-Evidence — the overlap, stated plainly

ScientistOne's principle is that **every claim must be traceable to its evidence
source**, and its **CoE Audit** applies four post-hoc integrity checks:

| CoE Audit check | What it catches |
|---|---|
| **Score verification** | Reported numbers that the artifacts do not support |
| **Specification violation** | Constraints the work claimed to respect and did not |
| **Reference verification** | Hallucinated citations — resolved against Semantic Scholar, arXiv, OpenAlex and Crossref |
| **Method–code alignment** | A method section that does not describe what the code does |

Reported results across **75 papers, five systems, five tasks**: every baseline
showed at least one systematic integrity failure — hallucinated reference rates
up to **21 %**, score verification passing in as few as **42 %** of papers,
method–code alignment between **20 % and 80 %** — while ScientistOne reported
**0/337 hallucinated references**, **12/12** score verification and **14/15**
method–code alignment.

> **This is the number that matters to AIRL-OS.** Not because it is a
> competitor's score, but because it is **evidence** for a claim this repository
> has only ever asserted: that retrofitting verification at write-up time does
> not work, and that the chain must be maintained during production. Science One
> demonstrated it; AIRL-OS argued it.

**AIRL-OS's evidence chain and Science One's Chain-of-Evidence are the same
idea.** The overlap is real and predates this repository's articulation of it.

---

## 4. Where AIRL-OS is actually different

The difference is **scope**, not the chain.

| | ScientistOne | AIRL-OS |
|---|---|---|
| Primary question | *Can an autonomous system produce research whose claims are verifiable?* | *Under what governance may a claim be believed at all?* |
| Chain built by | The producing system, natively | The producing system, and enforced by a gate that can **refuse** |
| Verification | Post-hoc audit of a finished paper | Gate-by-gate, **mechanical check before model judgement**, unwaivable |
| Human role | Consumer of the audit | **Decision authority that cannot be delegated** — G8 is human-only |
| Independence | Not the central concern | The central concern: measured error correlation, separation constraints, R1/R2/R3 |
| Negative results | Not addressed | In-principle acceptance before results exist |
| After publication | Out of scope | G10 monitoring, supersession, claim survival |
| Self-measurement | CoE Audit measures the papers | The metascience plane measures **the laboratory** |
| Status | **Built and measured** | **Specified, barely built** |

The honest one-line positioning:

> **Science One shows an autonomous researcher can produce verifiable papers.
> AIRL-OS asks what an institution must do before it believes any of them —
> including its own.** The second question is broader, harder to demonstrate,
> and currently answered only on paper.

---

## 5. What AIRL-OS should take from these systems

| From | Take | Why |
|---|---|---|
| **CoE Audit** | The four checks, **adopted as an external benchmark** for G6-0 and G9 | They are concrete, published, and measure exactly what AIRL-OS claims to enforce. Reference verification and method–code alignment are directly implementable |
| **CoE Audit** | Its benchmark discipline | AIRL-OS has no measurement of its own. A framework about evidence that produces none about itself is in a weak position |
| **PaperQA2** | Reuse rather than reimplement at G3 | AIRL-OS's value is not the best retrieval algorithm; it is how retrieval binds to provenance and claim scope |
| **Robin** | Its ranking with **measured concordance against human experts** | The model for `measuring-agreement` |
| **AI Scientist v2** | Its sandbox insistence | Autonomous code execution is a real hazard; the Execution Broker exists for this |

**The first row is a decision, not an observation** — see
`AIRL_OS_EXTERNAL_STANDARDS.md` §4.3.

---

## 6. Where AIRL-OS is behind, without qualification

- **No end-to-end run.** Not one research question has travelled G0 → G10.
- **No measurement.** No score verification rate, no hallucinated-reference rate,
  no method–code alignment figure — nothing comparable to the 75-paper benchmark.
- **A much smaller literature subsystem** than PaperQA2, and it will stay smaller.
- **No empirical outcome** of the kind Robin produced.
- **No external users, no independent bug reports, no production history.** The
  repository is weeks old.

> A reader deciding whether to use something today should use one of the systems
> in §2. AIRL-OS is an architecture with a working literature bridge attached,
> and saying otherwise would violate this repository's own document standard.

---

## 7. What would make the comparison meaningful

The claim *"governance produces more trustworthy research"* is currently
unmeasured. It becomes measurable when:

1. **CoE Audit runs against AIRL-OS output** — the same four checks, the same way,
   on whatever the first end-to-end slice produces.
2. **Control injection reports a false-positive rate** — the metascience plane's
   own measurement, on hidden positive and negative controls.
3. **Claim survival is tracked** over the first year of accepted claims.

Until at least the first exists, this document records a *position*, not a
result.

---

## 8. Sources

- ScientistOne — <https://arxiv.org/abs/2605.26340> · Science One Framework — <https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/>
- The AI Scientist v2 — <https://github.com/SakanaAI/AI-Scientist-v2>
- Robin — <https://www.futurehouse.org/research/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system>
- PaperQA2 — <https://github.com/Future-House/paper-qa>
