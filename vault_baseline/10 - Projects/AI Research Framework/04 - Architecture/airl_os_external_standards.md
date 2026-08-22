> [!info] Generated view
> This note is generated from `docs/architecture/AIRL_OS_EXTERNAL_STANDARDS.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# AIRL-OS — External Standards Register

| Field | Value |
|---|---|
| Document type | Architecture decision record — adoption register |
| Scope | Which external standards AIRL-OS **adopts** rather than invents, and which it defers |
| Sibling documents | `AIRL_OS_ARCHITECTURE.md` · `AIRL_OS_SKILL_LAYER.md` §14 · `AIRL_OS_IDEAL_STRUCTURE.md` |
| Date | 2026-08-22 |
| Status | Sections 2–4 **decided**; Section 5 is a deferred queue |

---

## 1. The rule

> **Adopt before inventing.** Every format this laboratory invents is a format it
> must also specify, validate, document and maintain. Where a standard already
> exists, is machine-checkable, and has tooling, AIRL-OS conforms to it and
> spends its own effort on what is genuinely specific to it.

A candidate is adopted only when all four hold:

1. **Mechanically checkable** — conformance can be a script, not an opinion
2. **Has a consumer** — something in the repository can use it now, or the
   package that will use it is already in the plan
3. **Reduces surface** — it removes an invention, rather than adding a layer
4. **Does not silently import authority** — a standard describes a format; it
   never decides what AIRL-OS accepts

Failing (2) is not a rejection: it moves the item to §5, dated and reasoned.

---

## 2. Adopted — the agent layer

### 2.1 Agent Skills open format · `agentskills.io`

| | |
|---|---|
| Replaces | An AIRL-specific skill schema and per-harness bootstrap adapters |
| Integration point | `skills/**/SKILL.md`; `scripts/validate_skills.py`; WP-048 |
| Closes | "38 skills exist, none of them loads" |
| Status | **Done** — 49/49 skills conform, checked mechanically |

The format was opened by Anthropic in December 2025 and is implemented by Claude
Code, Codex, OpenCode, Cursor, Copilot, Gemini CLI **and Hermes Agent** — every
harness AIRL-OS targets, including the one in daily use. Conformance *is* the
bootstrap, so **WP-048 shrinks**: what remained a per-harness adapter is now
mostly a directory location.

Six top-level fields are permitted (`name`, `description`, `license`,
`compatibility`, `metadata`, `allowed-tools`); every AIRL field lives under
`metadata` behind an `airl.` prefix. Progressive disclosure — name+description at
startup, body on activation, `references/` on demand — is also the token-budget
discipline the skill layer asked for.

**Consequence for provenance:** `airl.derived_from` + `airl.upstream_commit` make
the upstream relationship a machine-readable fact, so "upstream changed — what
must be re-examined?" becomes a query rather than an archaeology exercise.

---

## 3. Adopted — the evidence layer, and how it unlocks C1

This is the register's most consequential entry. **Finding C1** — the evidence
bootstrap deadlock — blocks the entire commissioning programme: every Definition
of Done requires a signed `EvidenceManifest` in an immutable store, and that
store is WP-026, far downstream. Nothing, including WP-001, can reach `ACCEPTED`.

**The deadlock is an artefact of assuming the store must be built here.** Supply
chain security solved this problem years ago, and its solution is free, hosted,
and requires no trusted third party of ours.

| Layer | Standard | What it gives AIRL-OS |
|---|---|---|
| Signed claim envelope | **in-toto attestation (ITE-6)** — `subject` / `predicateType` / `predicate`, wrapped in a **DSSE** envelope | The exact shape of `EvidenceManifest`: what artefact, what claim about it, signed as one unit |
| Signing identity | **Sigstore** — keyless, OIDC-bound short-lived certificates | No long-lived key for a one-person operation to manage or leak |
| **Immutable store** | **Rekor transparency log** | **Append-only, publicly verifiable inclusion proofs — without building WP-026** |
| Time anchor | **OpenTimestamps** (already WP-139) | Bitcoin-anchored, hash-only, no third party |
| Model weight integrity | **`sigstore/model-transparency` + OpenSSF Model Signing (OMS)** | The GGUF hash-and-signature that R3 requires |

### 3.1 The WP-000 shape this produces

An interim evidence policy no longer needs to invent anything:

```
EvidenceManifest  ==  in-toto Statement
    subject:        [{name, digest: {sha256: ...}}]      # the artefact under acceptance
    predicateType:  https://airl-os.local/EvidenceManifest/v0.1
    predicate:      {work_package, gate, tests, environment, schema_versions,
                     policy_versions, verifier, findings, residual_risk}
        ↓ DSSE envelope, Sigstore keyless signature
        ↓ Rekor transparency log entry  → immutable, third-party-verifiable
        ↓ OpenTimestamps anchor on the entry hash
```

**Immutability is delegated, not deferred.** When WP-026 (content-addressed WORM
store) lands, the manifests migrate into it and the log entry remains as an
independent witness — which is strictly better than either alone.

### 3.2 What this does *not* settle

The store was only half of C1. The other half is **who the independent verifier
is** in a one-person operation — finding C2, which no standard can answer. WP-000
therefore still requires the scope decision; adopting these standards removes the
*technical* blocker only, and saying otherwise would be exactly the kind of
overstatement this repository is trying to avoid.

**R3 note.** OMS/model-transparency gives the local open-weight requirement
(`AIRL_OS_ROLE_MODEL_ASSIGNMENT.md` §0, layer 3) a real implementation: the GGUF
is hashed and signed, and the signature is what the frozen manifest points at.

---

## 4. Adopted — the literature layer

### 4.1 PRISMA 2020 + PRISMA-S + PRISMA-LSR

| | |
|---|---|
| Integration point | G3 `LiteratureSetManifest`; `searching-literature`, `screening-sources`; G10 |
| Closes | G3 freezes a set but reports nothing about *how* it was assembled |
| Status | **Adopted as the G3/G10 reporting contract**; fields to be added to the manifest |

- **PRISMA 2020** — the reporting baseline; notably it already requires declaring
  the **use of automation tools during screening**, which is exactly what AIRL-OS
  does and currently records nowhere.
- **PRISMA-S** — the search-strategy extension: every database, every query
  string, every filter, verbatim and reproducible. This is what makes a frozen
  literature set re-derivable rather than merely archived.
- **PRISMA-LSR** — the living systematic review extension. **G10 is a living
  review**; there is an existing standard for what "the evidence base changed"
  must report, and AIRL-OS should not invent a second one.

### 4.2 A defensible stopping rule for screening

Active-learning screening has no natural end, and "we stopped when it looked
done" is not a recordable decision. The **SAFE** heuristic (and the
confidence-based stopping literature around it) turns the stop into a
**preregistered, recomputable rule**: it is fixed in the analysis plan before
screening starts, and the record shows the rule, not a judgement call.

`screening-sources` gains a mechanical check: *the stopping rule was declared
before screening began, and the recorded stop matches it.*

---

## 5. Deferred queue — with the reason, not just the name

Each entry is real and each is currently **out of scope**, because adopting all
of them would enlarge exactly the thing this repository already suffers from:
specified surface with no implementation behind it.

| Standard | What it would give | Waits on | Where it lands |
|---|---|---|---|
| **Nanopublication** (assertion + provenance + publication-info) and **Micropublication** (claims *plus supporting and contradicting* evidence lines and arguments); **SEPIO**'s explicit `EvidenceItem` | A ready data model for `ClaimVersion` / `EvidenceSpan`, and a shape that already matches ACH and adversarial review | WP-018 claim/evidence schemas | WP-018, WP-075 |
| **Workflow Run RO-Crate** — Process / Workflow / **Provenance** Run Crate profiles, mapped to **W3C PROV-O**, with re-execution support | A machine-actionable, engine-independent run record; removes the need to invent a run manifest | WP-082 run registry | WP-082, G7a |
| **GRADE** certainty of evidence; **RoB 2** / **ROBINS-I** signalling questions | Structured, mechanically-checkable appraisal feeding claim strength — the framework has seven confidence scales and no appraisal instrument | WP-079 source trust cards | WP-079, `calibrating-confidence` |
| **CAE** (Claims–Arguments–Evidence) and **GSN** | A mature, certified-industry structure and notation for the G8 decision package — literally the objects AIRL-OS already has | WP-088-class decision packaging | G8 `DecisionRecord` |
| Attribution metrics: **AIS**, ALCE-style NLI citation recall/precision, **FActScore**, **AttributionBench** | A measured basis for the G6-0 citation-entailment check | WP-080 | WP-080 |
| **IDEA protocol** (Investigate → Estimate → Discuss → Aggregate, from repliCATS) | A validated refinement of the G6-3 Delphi round that measurably reduces overconfidence | G6-3 implementation | `arbitrating-disagreement` |
| **DARPA SCORE / Replication Markets** priors | An external prior for the claim-survival KPI | C6 metascience plane | WP-093-class metascience |
| **spec-kit / AGENTS.md** "executable specification" pattern | The answer to §13.5 — the commissioning plan is not agent-consumable | S5 plan projection | WP-047 |

### 5.1 Two warnings that came out of the same research

**Entailment checkers are instruments, not oracles.** The attribution literature
finds NLI-based verifiers brittle, prone to shallow heuristics, and — critically —
that the metrics **do not transfer across datasets and constructs**. The G6-0
citation check must therefore ship with its own calibration set and a measured
error rate, exactly like any other instrument in the metascience plane. Treating
it as ground truth would reproduce, one layer down, the very failure mode the
gate exists to catch.

**Publishing a checklist does not change behaviour.** Eighteen months after
TRIPOD+AI was published, reporting quality in the field it targeted had **not**
measurably improved. This is external evidence for the core AIRL-OS thesis: a
rule that is not mechanically enforced is decorative. Any reporting guideline
adopted here (§4.1, and the EQUATOR family at G9) must arrive as a **blocking
mechanical check**, never as documentation.

---

## 6. Systems studied but deliberately not adopted

| System | What was taken |
|---|---|
| **FutureHouse Robin / PaperQA2** | The hypothesis **tournament with measured human-expert concordance** — a model for G1/G2 ranking and for `measuring-agreement`. PaperQA2 is a **benchmark for G3, not a component to build** |
| **Google AI co-scientist** | Multi-agent hypothesis generation with an explicit ranking stage |
| **12-factor agents / harness engineering** | "Own your context window and your control flow" — independent confirmation of the Temporal ↔ LangGraph split |
| **GitHub spec-kit** | Specifications as first-class executable artefacts, plus the repo-root constitution pattern |

None of these is imported as a dependency. They are recorded here so that a later
reader can see what the alternatives were and why AIRL-OS is shaped as it is.

---

## 7. Sources

- Agent Skills — <https://agentskills.io/specification>
- in-toto attestation / SLSA — <https://slsa.dev/blog/2023/05/in-toto-and-slsa>
- Sigstore model transparency — <https://github.com/sigstore/model-transparency> · OpenSSF Model Signing — <https://github.com/ossf/model-signing-spec>
- Micropublications — <https://link.springer.com/article/10.1186/2041-1480-5-28> · Nanopublications — <https://arxiv.org/pdf/1809.06532>
- Workflow Run RO-Crate — <https://www.researchobject.org/workflow-run-crate/>
- PRISMA-LSR — <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036629/> · SAFE stopping heuristic — <https://link.springer.com/article/10.1186/s13643-024-02502-7>
- GRADE guidelines 18 (ROBINS-I) — <https://pubmed.ncbi.nlm.nih.gov/29432858/>
- EQUATOR AI/ML guidelines — <https://www.equator-network.org/reporting-guidelines-study-design/artificial-intelligence-machine-learning-studies/> · TRIPOD+AI compliance study — <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12627258/>
- Do LLM attribution metrics transfer? — <https://arxiv.org/html/2606.23915> · ALCE — <https://arxiv.org/pdf/2305.14627>
- repliCATS / IDEA protocol — <https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0274429> · DARPA SCORE — <https://ncbi.nlm.nih.gov/pmc/articles/PMC7428244>
- FutureHouse Robin — <https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system>
