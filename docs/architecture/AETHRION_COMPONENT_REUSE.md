# AETHRION — Mature Components to Build On

| Field | Value |
|---|---|
| Document type | Architecture reference — component adoption register |
| Scope | Existing implementations, standards, patterns and benchmarks this project builds on rather than reinvents |
| Sibling documents | `AETHRION_EXTERNAL_STANDARDS.md` (formats) · `AETHRION_RELATED_SYSTEMS.md` (systems) · `ADR-003` (security architecture) |
| Status | §3 is **implemented and measured**; §4–§9 are decided and unbuilt; §10 is rejected or deferred with reasons |
| Date | 2026-08-22 |

**In one paragraph.** The purpose of adopting an existing implementation is
**not** to reduce scope — it is that a gate backed by something a community
maintains and tests is **stronger** than the same gate backed by code written
here for the first time. This register names, for each control, the component it
should stand on and *how* that component is taken: as a dependency, behind an
adapter, as a format, as a benchmark that measures us, as a pattern we implement
ourselves, or as a deployment choice. The governing principle is that AETHRION
should not invent its own parser, screening engine, policy language, sandbox,
experiment tracker or scholarly identifier — its contribution is the control
layer that decides **which evidence, having passed which gate, permits which
claim to be accepted.**

---

## 1. The adoption taxonomy

"Reuse" is not one thing, and treating it as one produces bad decisions —
importing a dependency where a pattern was needed, or reimplementing a pattern
as if it were a library.

| Type | Meaning | Obligation it creates |
|---|---|---|
| **DEPENDENCY** | Runtime component, called directly | Version pinning, upgrade path, failure semantics |
| **ADAPTER** | External component behind an AIRL contract | The contract must survive replacing it |
| **DIRECT_ADAPT** | Source code taken and refactored into AETHRION contracts | Permissive licence read at the source · pinned commit · named file list · characterisation suite written **before** the code moves · SPDX and `NOTICE` |
| **ADAPTIVE_REIMPLEMENT** | The mechanism is specified from paper or implementation, then written natively. No code copied | A written mechanism specification — inputs, outputs, states, invariants, failure conditions, forbidden behaviour — before any implementation |
| **STANDARD** | A format or model implemented as specified | Conformance testing |
| **BENCHMARK** | Not part of the system; it **measures** the system | Agreeing to publish the score |
| **PATTERN** | An architectural idea implemented here, no code taken | Attribution, and honesty about divergence |
| **OPTIONAL BACKEND** | A deployment choice behind a capability interface | The interface, not the backend, is the contract |
| **DEFER** | Plausible, examined, not taken now | Recording the reason, so it is not re-examined from scratch |
| **REJECTED** | Examined and deliberately not taken | Recording why |

The two new types were added at baseline v1.2.0, when the register stopped being
only about *components called at runtime* and started covering *mechanisms
implemented here*. The distinction they draw is the one that matters legally and
architecturally: **DIRECT_ADAPT moves files and therefore moves a licence
obligation; ADAPTIVE_REIMPLEMENT moves an idea and does not.** A register entry
that claims the second while naming source files is a defect, and
`scripts/check_upstream_lineage.py` refuses it — see `ADR-004`.

---

## 2. The selection rule

A component is adopted when it makes a control **more likely to catch what the
control exists to catch**:

1. **Maintained by people closer to the problem** — Crossref knows about DOIs;
   this project never will.
2. **Already tested against reality** — a validated implementation has survived
   cases nobody here would imagine.
3. **Failure is legible** — when it is wrong, that is visible and attributable.
4. **Adoption supplies a signal, never authority** — Crossref decides whether a
   record exists; it does not decide whether a package is accepted.

5. **What it may never decide is stated before it is adopted** — every entry
   carries an `authority_boundary`, because the recurring failure of adoption is
   not a component behaving badly but a component quietly acquiring authority.

Rule 4 is why this register is separate from gate policy, and why a BENCHMARK
can never become a gate. Rule 5 is why `provenance/upstreams.json` refuses an
entry without an authority boundary.

---

## 3. Implemented and measured

### 3.1 Reference verification · **DEPENDENCY** · CoE Audit check 1

| | |
|---|---|
| Components | **Crossref** · **OpenAlex** · **arXiv** APIs |
| Where | `scripts/verify_references.py` |
| Gate | G3 freeze · G9 publication conformance |

| Authorities | Corroborated | Rate |
|---|---:|---:|
| Crossref + OpenAlex | 25 / 33 | 75.8 % |
| **+ arXiv** | **27 / 33** | **81.8 %** |

The first run scored 75.8 %, and the instructive part was *why*: every unresolved
entry was a **DOI-less preprint**, which a DOI-registration authority
structurally cannot see. **The measurement did not find bad sources; it found an
inadequate check.**

> **What the number is not.** It measures whether records *exist* in public
> authorities, not whether a claim is supported by them. An unresolved DOI-less
> item means *unindexed*, not *fabricated*. The CoE Audit benchmark measured
> hallucinated references in **generated** bibliographies; this registry is
> human-curated, so the numbers are **not comparable**.

### 3.2 Source monitoring · **DEPENDENCY** · the first slice of G10

| | |
|---|---|
| Component | **Crossref**, which now carries Retraction Watch data and exposes `update-to` / `updated-by` |
| Where | `scripts/monitor_sources.py` |
| Gate | G10 |

| Measure | Value |
|---|---:|
| Sources swept | **15** of 33 |
| Sources invisible — no DOI | **18** |
| Material signals | 0 |
| **Positive control** | **FIRED** |

**A clean report proves nothing unless the check can fire**, so every run
includes a DOI known to be retracted and the script **exits non-zero if the
control stays silent**. This is the metascience plane's control-injection
principle applied to the smallest possible check, and it is the difference
between "no retractions" and "no detector".

The sweep also surfaced its own boundary: **18 of 33 sources carry no DOI and are
invisible to it.** A clean report over a DOI-less registry would be a false
reassurance, and the report says so.

> **Claim impact analysis is not implemented.** Nothing maps a retracted source
> to dependent claims, because no Claim Ledger exists. G10's loop is opened, not
> closed.

---

## 4. Evaluation and assurance

| Component | Type | Where | Why it is stronger than building it |
|---|---|---|---|
| **Inspect AI** (UK AI Security Institute) | **DEPENDENCY** | WP-043 behaviour evaluation · WP-048 harness adapters · ACC-46–51 | Its `Dataset → Solver → Scorer` model, sandboxing, limits, retry/resume and transcripts are exactly what skill-behaviour testing needs — and it can drive **real agent harnesses** (Claude Code, Codex CLI, Gemini CLI) as evaluation subjects. Writing an eval runner here would reproduce a worse version of a framework built for frontier safety testing |
| **AgentDojo** | **BENCHMARK** | Prompt-injection assurance, WP-136 | A published attack/defence suite. AETHRION's untrusted-content boundary should be measured against someone else's attacks, not its own |
| **Agent Security Bench (ASB)** | **BENCHMARK** | WP-060 · WP-058 | Ten scenarios, 400+ tools, 27 attack and defence methods across 13 model backbones. Its headline finding is the architectural argument for the capability gate: a highest average attack success rate of **84.3%** with defences reported as of limited effectiveness. **If prompt-layer defences are weak, the boundary must be that the capability is unavailable** — ADR-003, ACC-117 |
| **WASP** | **BENCHMARK** (non-commercial) | WP-060 · WP-136 | Realistic web-agent injection where the attacker is an ordinary user of a site rather than its owner. Attacks partially succeed in up to **86%** of cases against top-tier agents. **Licence: majority CC-BY-NC 4.0**, with one bundled component MIT — usable as a benchmark under those terms and **not adaptable into this repository at all**, which is why ADR-019 requires a file-level licence position |
| **MAST** | **PATTERN + BENCHMARK** | WP-152 · WP-128 | Fourteen failure modes in three categories from 1,600+ annotated traces across seven frameworks, κ=0.88. The three categories map onto this architecture's COORDINATION, VERIFICATION and design-time classes, which is why the taxonomy is a pattern rather than an adoption |
| **Who&When** | **BENCHMARK** | WP-152 | 127 annotated multi-agent failure logs. Its reported ceilings — around 53.5% for the responsible agent and 14.2% for the exact failing step — are the reason `UNKNOWN` is a first-class classification here rather than a gap. **A taxonomy that names a cause for every failure would be wrong most of the time at step level** — ACC-094 |
| **Search-Time Contamination** | **PATTERN + BENCHMARK** | WP-158 | Three leakage severities over six public benchmarks, with measured inflation up to 4%. The point is not the size: **nothing about the model is contaminated — the measurement is**, so the firewall is a property of the run — ADR-017 |
| **CoE Audit** | **BENCHMARK** | G6-0 · G9 | Adopted in `AETHRION_EXTERNAL_STANDARDS.md` §4.3; check 1 implemented |
| **PaperBench** | **PATTERN + BENCHMARK** | G7a / G7b | Its three-container separation — the agent builds in one, reproduction runs fresh in a second, grading happens in a third — is the working demonstration of the producer / reproducer / reviewer split this architecture asserts. The pattern is taken; the runtime is not embedded |
| **ResearchClawBench** | **BENCHMARK** | End-to-end metascience | 40 real research tasks across 10 domains, each grounded in a real published paper with the target paper hidden and expert-curated weighted rubrics. It enables the experiment that would make this project's central claim testable — see §11 |
| **AstaBench** | **BENCHMARK** | WP-043 · WP-044 · verifier and actor qualification | Eleven benchmarks and 2,400+ examples across literature search, code execution, data analysis and end-to-end discovery — with **standardised tools and explicit control for model cost and tool access**. That last property is what the rest of this portfolio lacks: without cost normalisation, a governed-versus-ungoverned comparison cannot separate the effect of governance from the effect of spend |
| **CORE-Bench** | **BENCHMARK** | G7a reproduction | 270 tasks over 90 papers across computer science, social science and medicine, at three difficulty levels including vision-language tasks. The oldest and most-cited of the reproduction benchmarks, and the one covering disciplines the 2026 preprints do not — a reproduction suite made only of recent work measures recent work |
| **SciReplicate-Bench · Artisan-Bench · REPRO-Bench** | **BENCHMARK + PATTERN** | G7 | Three different questions about reproduction that a single benchmark conflates: can the paper be *understood* before code is written; can the agent emit a package that runs **after the agent is gone**; and does the recomputed output actually match the claim. The patterns are taken into WP-085; the runtimes are not embedded |
| **ScienceAgentBench · EXP-Bench** | **BENCHMARK** | WP-043 · WP-083 | Scientific coding and analysis capability, and whether an experiment was actually *conducted* rather than well described. EXP-Bench's reported difficulty is why G5 acceptance tests execution rather than the quality of experiment-plan prose |

**WP-043 changes character:** from *build an evaluation engine* to **encode AIRL
behaviours as Inspect tasks and scorers**. The engine is not the contribution;
the behaviours and their pass criteria are.

---

## 5. Document representation and literature

| Component | Type | Where | Why |
|---|---|---|---|
| **GROBID** | **DEPENDENCY** | `SourceRepresentation` | Scholarly PDF → TEI XML, developed over years against real publisher output. A first-attempt PDF parser makes `EvidenceSpan` unreliable at its foundation |
| **Pub2TEI** | **DEPENDENCY** | Structured publisher ingestion | Normalises Elsevier, Springer, Wiley, JATS/NLM XML into the *same* TEI representation, so a span means the same thing regardless of where the source came from |
| **PaperQA2** | **ADAPTER** | G3 retrieval | Far more mature retrieval than this project will build. The contribution is how retrieval binds to provenance and claim scope |
| **OpenScholar** | **ADAPTER** (second implementation) | G3 retrieval | Kept behind the *same* adapter contract as PaperQA2, deliberately. The two are not ranked here — the choice is settled by measurement on the same questions, the same corpus and the same budget, against source recall, citation correctness, entailment, coverage, unsupported-claim rate, latency and cost. Hard-coding a winner today would be a preference wearing a decision's clothes |
| **ASReview** | **ADAPTER** | G3 screening | Active-learning screening published in *Nature Machine Intelligence*, pairing directly with the SAFE stopping rule already adopted |

### 5.1 What canonical representation buys `EvidenceSpan`

```
Publisher XML ──► Pub2TEI ─┐
PDF only ──────► GROBID ───┼──► canonical TEI ──► SourceRepresentation ──► EvidenceSpan
LaTeX source ──► LaTeXML ──┘
```

A span stops being *"page 4, paragraph 3"* and becomes addressable:

```yaml
EvidenceSpan:
  source_digest:          sha256:...
  representation_digest:  sha256:...
  parser:                 grobid
  parser_version:         0.8.x
  tei_xpath:              //body/div[2]/p[3]/s[4]
  exact_text:             "..."
  text_digest:            sha256:...
```

Because the original bytes are kept, a later parser produces
`representation-v2` **without invalidating claims anchored to v1** — the claim
stays bound to the representation that actually supported it.

---

## 6. Policy, security and execution

| Component | Type | Where | Why |
|---|---|---|---|
| **`PolicyDecision` interface** | **the commissioned contract** | Tool Broker · Execution Broker | What WP-056 delivers. The engine behind it is configuration |
| **Cedar** | **OPTIONAL BACKEND** | same | `principal · action · resource · context` already matches `TaskContract`; `forbid` overrides `permit`; formal semantics and schema validation |
| **OPA / Rego** | **OPTIONAL BACKEND** | same | General-purpose, mature bundle distribution, large operator familiarity |

> **Neither engine is chosen — [`ADR-010`](ADR-010_policy_backend.md).** This
> register previously called Cedar a first-candidate dependency while the plan's
> WP-056 was titled *OPA Policy Platform*. Both are now optional backends behind
> one interface, and the bake-off that decides between them cannot run until a
> policy set exists, because there is nothing yet to measure them on.
| **CaMeL** | **PATTERN** | WP-136 | Control flow comes from *trusted* intent; untrusted content may supply values but can never create actions or expand permissions. Reported 67–77 % of AgentDojo tasks solved with provable security depending on paper version |
| **Inspect sandboxes · gVisor · E2B** | **OPTIONAL BACKEND** | Execution Broker | AETHRION should own the `ExecutionBackend` interface and the **risk-profile → backend** routing, not the isolation technology |

**WP-136 changes character:** from *prompt-injection detection* to **trusted
control / untrusted data architecture**. A detector is defence in depth; it is
not a security boundary.

**And the boundary has a concrete form: the capability gate.** *Prompt says safe*
is not security; *the capability is unavailable unless policy grants it* is.
External content is quarantined into a data object; the agent forms a
`ToolIntent`; policy decides; only then is a scoped credential injected. ASB's
finding that existing defences are of limited effectiveness against an 84.3%
average attack success rate is the empirical case for putting the boundary at the
capability rather than at the text — WP-058, ACC-117.

---

## 7. Provenance, identity and storage

| Component | Type | Where | Why |
|---|---|---|---|
| **Workflow Run RO-Crate** (Process / Workflow / Provenance profiles) | **STANDARD** | G5 `ExperimentRun` · G7 | Machine-actionable, engine-independent, re-execution aware, mapped to W3C PROV. **Priority raised: adopt before the first slice**, so the run format is never forked |
| **Croissant 1.1** (MLCommons) | **STANDARD** | Dataset records | Adds machine-actionable provenance via PROV-O and structured usage conditions via ODRL/DUO — which connects directly to policy: a dataset's `usagePolicy` becomes a policy input |
| **SWHID — ISO/IEC 18670** | **STANDARD** | G7 · G9 software identity | An intrinsic identifier computed from content, verifiable without a registry. Works for private code too, because computing it does not require archiving |
| **S3 Object Lock semantics** | **OPTIONAL BACKEND** | WP-026 | Compliance-mode WORM that no account, including root, can delete within retention |
| **lakeFS** | **OPTIONAL BACKEND** | Working datasets | Git-like branching over object storage for *mutable* research data — a different problem from accepted-evidence immutability, and worth keeping separate |
| **MLflow + OpenTelemetry** | **DEPENDENCY** | Observability | Traces, token usage, cost and tool calls over OTLP. **Operational observability only** — never the scientific truth store |
| **OpenSSF Scorecard** | **DEPENDENCY** | WP-159 · WP-059 | Project security posture before depending on something. A heuristic, not a safety property — a high score is not evidence that a dependency is secure |
| **OSV-Scanner** | **DEPENDENCY** | WP-159 · WP-024 | Known vulnerabilities in the lockfile and images. **Silence means nothing is known, not that nothing is there**, and a finding with no available fix becomes an owned, expiring residual risk rather than a suppression |
| **SLSA** | **STANDARD** | WP-159 · WP-027 | What built an artifact, from which source. Provenance establishes origin; it says nothing about correctness |

**WP-026 changes character:** from *build a content-addressed WORM store* to
**integrate and verify an existing object-lock implementation** behind an
`ImmutableObjectStore` contract.

> **The line that must not blur.** MLflow answers *what did the system do*.
> Workflow Run RO-Crate plus a signed `EvidenceManifest` answers *what may be
> believed*. Operational telemetry is not provenance.

---

## 8. Attestation

| Component | Type | Status |
|---|---|---|
| **`sigstore-python`** | **DEPENDENCY** | The named upgrade out of `airl-interim-v0.1`: keyless OIDC identity and a Rekor inclusion proof, neither of which the local-key interim profile has |
| **OpenSSF `model-signing`** | **DEPENDENCY** | Signs local open-weight model files — the R3 requirement in `AETHRION_ROLE_MODEL_ASSIGNMENT.md` |
| **OpenTimestamps** | **DEPENDENCY** | WP-139, replacing WP-000's interim anchor |

Today one operator controls the repository, the signing key, the manifest
generator and the clock. That makes the current profile **tamper-evident but not
externally witnessed**, and the Sigstore/Rekor path is what closes it.

---

## 9. Claim and evidence model

| Component | Type | Where | Why |
|---|---|---|---|
| **SEPIO** | **STANDARD** (as an AIRL profile) | `ClaimVersion` · `EvidenceSpan` · review links | Domain-agnostic core model for **assertions, evidence and provenance**, designed to be specialised through profiles. Its shape is the shape AETHRION already has, and its relation types include *challenges* as well as *supports* — which is what adversarial review needs |
| **LinkML** | **DEPENDENCY** | `SchemaRegistry`, WP-020 | One model generating JSON Schema, Pydantic, JSON-LD, SHACL and SQL DDL. This attacks a real debt: contracts currently risk being defined three times in three shapes, which is how the bridge and the contract core came to disagree about digests |
| **CiTO — the Citation Typing Ontology** | **STANDARD** | `EvidenceTag.support_relation` | `EvidenceTag` was about to carry an invented three-value enum — supports, challenges, contextualises. CiTO already publishes that vocabulary — `cito:supports`, `cito:disagreesWith`, `cito:usesMethodIn` and the rest — from the same SPAR family as the rest of the scholarly stack. Binding to its IRIs costs nothing now and makes an evidence tag mean the same thing outside this system as inside it. See `ADR-009` §5 |
| **`nanopub-py`** | **ADAPTER**, deferred | Public claim export | A published claim as a FAIR nanopublication — **an export representation, not the operational ledger**. Its structure (assertion · provenance · publication info) is close to an exact match for `ClaimVersion` + `EvidenceTag` + `DecisionRecord`, so the publication compiler is built so this projection stays addable. Deferred until the compiler exists, because a projection nobody consumes is cost without benefit |
| **`krippendorff`** · statsmodels · scikit-learn | **DEPENDENCY** | Metascience plane | Standard estimators with known small-sample and missing-data behaviour |
| **statcheck · `grim` · `pysprite`** | **DEPENDENCY** | G6-0 forensics | Validated implementations of tests whose edge cases — scale granularity, rounding, integer constraints — are exactly where a fresh implementation goes wrong |

**SEPIO + LinkML is promoted from the deferred queue.** The reason is that
`SchemaRegistry` is currently a dictionary with no validation, and generating the
contract surface from one model is a better answer than writing that registry by
hand.

---

## 9.1 Authoring, reporting and publication

The full register, with an `authority_boundary` per component, is
[`skills/authoring-research-documents/references/external-systems-and-standards.md`](../../skills/authoring-research-documents/references/external-systems-and-standards.md).
Summary:

| Component | Type | Role |
|---|---|---|
| **Quarto** | `DEPENDENCY` (**provisional**) | Manuscript orchestration, cross references, multi-format render, JATS output and a MECA bundle. Provisional until the bake-off runs |
| **Pandoc** | `DEPENDENCY` | Document AST, citeproc, DOCX reference templates, Lua filters. **AIRL transformations are AST filters, never regexes over a manuscript** |
| **MyST** | `OPTIONAL_BACKEND` | The competing stack in the bake-off |
| **Typst · LaTeX** | `OPTIONAL_BACKEND` | PDF backends; a venue mandate overrides preference |
| **Manubot** | `PATTERN` | Manuscript-as-code, continuous rebuild, citation by identifier — taken as discipline, not as a second engine |
| **Docling** | `ADAPTER` | Ingesting an existing report for revision. **Kept off the scholarly evidence path**, which is GROBID/Pub2TEI, unless a measured comparison says otherwise |
| **Better BibTeX** | `ADAPTER` | Project bibliography projection with stable keys. Not canonical identity |
| **CSL** | `STANDARD` | Citation styles; AIRL does not invent one |
| **DataCite 4.7** | `STANDARD` | Released 2026-03-03; adds `SWHID` as a related-identifier type, which links directly to AIRL's SWHID adoption |
| **ORCID · ROR · CRediT** | `STANDARD` | Identity, affiliation and contribution metadata — **never authorship authority** |
| **CITATION.cff** | `STANDARD` | Citable software in a package |
| **JATS · JATS4R · MECA** | `STANDARD` / optional export | Interchange and submission, never the authoring format |
| **EQUATOR family · Z39.18 · ISO 7144** | `STANDARD` / `PATTERN` | Reporting guidelines and report structure, applied only where the study type fits |
| **Vale** | `DEPENDENCY` | Deterministic prose linting |
| **LanguageTool** | `OPTIONAL_BACKEND` | Grammar — **local or licensed instance only**; its public free endpoint asks for no automated traffic |
| **WCAG 2.2 · veraPDF** | `STANDARD` / `DEPENDENCY` | Accessibility contracts, validated against the rendered artifact |
| **PaperBanana · DiagramRAG · figure skill repositories** | `PATTERN` | Figure methodology; no code or text copied, licences unverified until they are |

> **None of this toolchain is installed here.** Docker is, so the bake-off can be
> run in pinned containers. Until it is, "this project uses Quarto" states an
> intention, not a measurement.

## 9.2 Mechanisms assimilated rather than called

The sections above answer *which running implementation does this control stand
on*. This one answers a different question that the register did not previously
cover: **which mechanisms are implemented here, having been solved somewhere else
first.**

The distinction is not pedantic. A DEPENDENCY is installed and called — GROBID
parses a PDF and the parsing happens in GROBID. An assimilated mechanism runs as
this system's own code: there is nothing to install, nothing to call, and no
runtime trace of where it came from. That is exactly why it needs a register of
its own, and why `ADR-004` makes taking one an auditable act.

**The rule, stated once:** a mechanism may be taken; an architecture may not. No
external project appears here as a runtime module, a directory, a backend, a
class name or a configuration key. What arrives is a mechanism re-expressed in
this system's vocabulary — a candidate node becomes a `SearchNode` bound to an
`ArtifactRecord`, a scalar score becomes a `VerifiedValue` bound to a
`RawEvaluatorArtifact`, a budget counter becomes a `CampaignStopRecord` that
explicitly satisfies no gate.

### Where the registers live

There are two, and the split is the difference between installing something and
becoming something.

`provenance/upstreams.json` records **mechanisms assimilated** into this
repository's own code — `ADR-004`'s subject. **[`provenance/README.md`](../../provenance/README.md)**
is generated from it. `scripts/check_upstream_lineage.py` validates it and can be
made to fail on demand: `--self-test` injects a defect per rule and reports any
rule that stays silent.

`provenance/components.json` records **components adopted at runtime** — the
decisions in §3–§9.1 above, in machine-readable form.
**[`provenance/COMPONENTS.md`](../../provenance/COMPONENTS.md)** is generated
from it, and `scripts/check_wp_implementation_sources.py` validates it under the
same discipline.

Both are joined to the work package that has to execute the decision, and
projected into that package's **Implementation acquisition and assimilation**
block by `scripts/expand_acquisition.py`. That binding is the part that did not
exist: the decisions were sound and they reached nobody, so `WP-144` specified a
candidate state machine without naming AIDE, and `WP-041` was titled after a
component neither register knew.

The counts below were prose, and prose drifted — this section read **36 entries**
against a register that held fifty-eight, and named no `DEPENDENCY` at all
because the type had been added after the sentence was written. A count nobody
derives is a count nobody maintains, so it is derived.

<!-- generated:register-state — produced by scripts/check_wp_implementation_sources.py; do not edit inside this block -->

| Register | Entries | By type |
|---|---:|---|
| `provenance/upstreams.json` — mechanisms assimilated | **59** | ADAPTIVE_REIMPLEMENT 22 · BENCHMARK 10 · DEFER 5 · DEPENDENCY 3 · DIRECT_ADAPT 7 · PATTERN 8 · REJECT 1 · STANDARD 3 |
| `provenance/components.json` — components adopted | **44** | ADAPTER 6 · DEPENDENCY 24 · OPTIONAL_BACKEND 7 · PATTERN 2 · STANDARD 5 |

Together they are bound to **84 of 160** work packages and carry **117** open obligations.

**0 entries have reached `ADAPTING`**, and **2 components are `INTEGRATED`** — the Zotero and Obsidian adapters, which are the part of this system that actually runs. Every other row is a decision on paper: `pinned_commit` is `null` throughout, no `MS-*` mechanism specification has been written, and the rules that demand a pin, a file list and a characterisation suite begin to bite at the moment the first line of code moves.

<!-- /generated:register-state -->

### What the register refuses, and why those examples

Four entries record a capability being deliberately narrowed rather than copied.
They are worth naming here because each one is a place where adopting the
mechanism as-is would have handed authority to something that should not have it:

| Upstream capability | What was taken | What was refused |
|---|---|---|
| Automatic fulfilment of a broadcast information need | The typed `EvidenceGap` with an acceptance condition and a lifecycle | The autonomy. Upstream, an unmet need scored by urgency triggers a peer agent to run a skill. An open gap here authorises nothing; work is created by gate policy |
| A retrieval loop that stops when the model judges evidence sufficient | `EvidenceSufficiencyAssessment`, advisory | Its authority. A confirmatory campaign's stopping rule is frozen before results are seen, and cannot be changed by the loop that reads them |
| `auto_proceed_on_timeout`, a boolean defaulting to false | The human-intervention action vocabulary — approve, reject, edit, guidance, request revision, rollback, abort | The flag itself. At G8 and every mandatory human gate the capability is **absent**, not defaulted off, because a setting that can be turned on is a control that will be |
| A search tree whose node score drives the whole loop | The selection mechanism and its revisit-interior-nodes property | The score's reach. It allocates compute; writing it into a claim assessment is refused by schema and by policy — `ADR-006` |

### What baseline v1.3.0 added, and the three licences that changed a decision

Twenty-two entries arrived with the reliability layer, and three of them are
worth naming because the **licence changed the method rather than the decision** —
which is the case ADR-004 exists to handle and the one most often got wrong.

| Upstream | Licence | Consequence |
|---|---|---|
| **MAS-Resilience** — faulty-agent resilience, Challenger and Inspector | **GPL-3.0** | Incompatible with this repository's licence, so **no file may be copied under any circumstance**. The mechanism is specified from the paper and written natively — which creates no obligation and is recorded anyway |
| **WASP** — web-agent injection benchmark | **CC-BY-NC 4.0** for the majority; one bundled component MIT | Non-commercial. Usable as a benchmark under those terms, adaptable **not at all**. The split inside one repository is the concrete reason a repository-level licence is not a per-file licence |
| **AgentSlimming** — workflow optimisation | **MIT** | Legally adaptable, and still reimplemented. Its core mechanism is node pruning and cheap-model substitution — **the one optimisation ADR-011 refuses by name.** A permissive licence makes copying legal; it does not make copying correct |

The fourth case is the opposite: **BATS** is Apache-2.0 with two compact,
isolable modules (`agent_budget_tracker.py`, `agent_bats.py`), which makes it the
strongest direct-adaptation candidate in the register — and it still cannot move
until it has a pinned commit and a characterisation suite.

### An end-to-end paper generator was examined and rejected

One candidate overlapped this system's entire scope — idea, experiment,
analysis, paper, review. It is recorded as `REJECT` for two independent reasons,
either of which would suffice: its licence is neither MIT nor Apache and attaches
conditions to publications produced with it, which is the kind of obligation a
research system must not acquire silently; and adopting something with that scope
would be adopting a competing architecture rather than a mechanism. The entry
exists so the question is not reopened without new information.

---

## 10. External witnesses

| Component | Type | Where | Why |
|---|---|---|---|
| **OSF Registries** | **DEPENDENCY** | G2 · G2b preregistration | A local hash proves a plan existed; it does not prove *when*, to anyone who does not trust the operator. A timestamped external registration does |

| Assurance class | OSF registration |
|---|---|
| R1 exploratory | optional |
| R1 confirmatory | recommended |
| R2 confirmatory | **required** |
| R3 | **required**, plus an external verifier |

> OSF is a **witness, not an authority**: it attests that a plan existed on a
> date. Whether the protocol is scientifically acceptable stays an AETHRION
> decision. Integrate against the **Registries** workflow specifically — OSF
> Projects is being sunset through 2026–27 while Registries continues.

---

## 11. The experiment this makes possible

ResearchClawBench holds the same model, tools, budget and task fixed and varies
only the governance layer:

```
CONTROL     same model · same task · same tools · same budget · ungoverned agent
TREATMENT   same model · same task · same tools · same budget · AIRL-governed agent
```

Measured on both: ResearchClaw score · protocol mismatch · evidence mismatch ·
reference verification · reproduction success · CoE score · unsupported claims ·
human interventions · cost · runtime.

> **This is the paper worth writing**, and it is not "we built a better agent":
> *does research governance improve autonomous research integrity, and at what
> cost?* The agent is the constant; the governance is the variable. Current
> reported ResearchClawBench performance is low across the board — the strongest
> autonomous agent averages around 21 — so the honest expectation is that
> governance costs runtime and may not raise the score, while changing what can
> be believed about the output. **Both outcomes are publishable; only one is
> flattering.**

---

## 12. Deferred and rejected

| Component | Type | Reason |
|---|---|---|
| **AiiDA** | OPTIONAL BACKEND, deferred | Strong for HPC/computational workflows; no such workload exists here yet |
| **ReproZip** | deferred | A forensic-capture fallback for legacy runs that were never containerised |
| **GRADE · RoB 2 · ROBINS-I** | deferred | Domain-dependent appraisal instruments; premature before a domain is chosen |
| **IDEA / repliCATS** | deferred | Refines G6-3 disagreement once that gate is implemented |
| Prompt-injection *detector* libraries | **REJECTED as a boundary** | A detector is defence in depth. The boundary is CaMeL-style control/data separation — see §6 and `ADR-003` |

---

## 13. What this changes about the plan

Nothing is deleted. Several packages become **thinner and stronger at once** —
their job stops being *implement this capability* and becomes *integrate this
component under our contract, and verify it behaves*. **The verification is the
part AETHRION actually contributes.**

| Package | Was | Becomes |
|---|---|---|
| WP-000 | build attestation | integrate `sigstore-python`; keep the interim profile as fallback |
| WP-020 | hand-write the schema registry | generate the contract surface from one **LinkML** model |
| WP-026 | build a WORM store | integrate and verify an object-lock backend |
| WP-043 | build an evaluation engine | encode behaviours as **Inspect** tasks and scorers |
| WP-048 | write per-harness adapters | drive real harnesses through Inspect's agent bridge |
| WP-049/050 | write a policy evaluator | a policy engine behind the `PolicyDecision` interface; the engine is chosen by the ADR-010 bake-off, which has not run |
| WP-061-class | build a PDF parser | **GROBID + Pub2TEI** into canonical TEI |
| WP-068-class | build a screener | **ASReview**, owning the stopping-rule evidence |
| WP-075 | design a claim model | an **AIRL-SEPIO profile** in LinkML |
| WP-080 | build reference checking | **done for the reference half**; entailment remains |
| WP-082 | design a run record | emit **Workflow Run RO-Crate** |
| WP-136 | detect prompt injection | **CaMeL-style** trusted control / untrusted data |
| G10 packages | design monitoring | **done for the retraction sweep**; claim impact remains |

---

## 14. Sources

- Inspect AI — <https://github.com/UKGovernmentBEIS/inspect_ai> · <https://inspect.aisi.org.uk/>
- CaMeL, *Defeating Prompt Injections by Design* — <https://arxiv.org/abs/2503.18813> · AgentDojo — <https://github.com/ethz-spylab/agentdojo>
- Cedar — <https://docs.cedarpolicy.com/> · OPA — <https://www.openpolicyagent.org/docs>
- GROBID — <https://github.com/kermitt2/grobid> · Pub2TEI — <https://github.com/kermitt2/Pub2TEI>
- PaperQA2 — <https://github.com/Future-House/paper-qa> · ASReview — <https://github.com/asreview/asreview>
- Workflow Run RO-Crate — <https://www.researchobject.org/workflow-run-crate/> · Croissant 1.1 — <https://mlcommons.org/2026/02/croissant-1-1-standard/>
- SWHID ISO/IEC 18670 — <https://www.iso.org/standard/89985.html> · Software Heritage — <https://www.swhid.org/>
- SEPIO (LinkML) — <https://github.com/sepio-framework/sepio-linkml> · LinkML — <https://linkml.io/linkml/>
- `sigstore-python` — <https://github.com/sigstore/sigstore-python> · `model-signing` — <https://github.com/sigstore/model-transparency>
- OSF Registries API — <https://developer.osf.io/> · lakeFS — <https://docs.lakefs.io/> · MLflow tracing — <https://mlflow.org/docs/latest/genai/tracing/opentelemetry/>
- PaperBench — <https://github.com/openai/preparedness/blob/main/project/paperbench/README.md> · ResearchClawBench — <https://github.com/InternScience/ResearchClawBench>
- AstaBench — <https://github.com/allenai/asta-bench> · <https://arxiv.org/abs/2510.21652> · CORE-Bench — <https://arxiv.org/abs/2409.11363>
- ScienceAgentBench — <https://github.com/OSU-NLP-Group/ScienceAgentBench> · EXP-Bench — <https://arxiv.org/abs/2505.24785>
- SciReplicate-Bench — <https://arxiv.org/abs/2504.00255> · Artisan — <https://arxiv.org/abs/2602.10046> · REPRO-Bench — <https://arxiv.org/abs/2507.18901>
- OpenScholar — <https://github.com/AkariAsai/OpenScholar> · <https://arxiv.org/abs/2411.14199>
- CiTO — <https://sparontologies.github.io/cito/current/cito.html> · nanopublications — <https://nanopub.net/>
- AgentPrune / *Cut the Crap* — <https://arxiv.org/abs/2410.02506> · S2-MAD — <https://arxiv.org/abs/2502.04790>
- AgentSlimming — <https://github.com/CitrusYL/AgentSlimming> · MAD-M2 — <https://github.com/HongduanTian/MAD-MM>
- CONSENSAGENT — <https://aclanthology.org/2025.findings-acl.1141/> · MAS-Resilience — <https://arxiv.org/abs/2408.00989>
- MAST — <https://arxiv.org/abs/2503.13657> · Who&When — <https://arxiv.org/abs/2505.00212>
- BATS — <https://github.com/google-research/budget-aware-agent> · <https://arxiv.org/abs/2511.17006>
- Agent Security Bench — <https://arxiv.org/abs/2410.02644> · WASP — <https://arxiv.org/abs/2504.18575>
- Search-Time Contamination — <https://arxiv.org/abs/2606.05241> · Eval4NLP nondeterminism — <https://aclanthology.org/2025.eval4nlp-1.12/>
- OpenSSF Scorecard — <https://openssf.org/projects/scorecard/> · OSV-Scanner — <https://google.github.io/osv-scanner/> · SLSA — <https://slsa.dev/>
- **Assimilated mechanisms and their upstreams: [`provenance/README.md`](../../provenance/README.md)**, generated from `provenance/upstreams.json`
- statcheck (Python) — <https://github.com/hplisiecki/statcheck_python> · `grim` — <https://pypi.org/project/grim/> · `pysprite` — <https://github.com/QuentinAndre/pysprite> · `krippendorff` — <https://pypi.org/project/krippendorff/>
