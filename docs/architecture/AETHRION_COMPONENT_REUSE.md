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
| **STANDARD** | A format or model implemented as specified | Conformance testing |
| **BENCHMARK** | Not part of the system; it **measures** the system | Agreeing to publish the score |
| **PATTERN** | An architectural idea implemented here, no code taken | Attribution, and honesty about divergence |
| **OPTIONAL BACKEND** | A deployment choice behind a capability interface | The interface, not the backend, is the contract |
| **REJECTED** | Examined and deliberately not taken | Recording why |

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

Rule 4 is why this register is separate from gate policy, and why a BENCHMARK
can never become a gate.

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
| **CoE Audit** | **BENCHMARK** | G6-0 · G9 | Adopted in `AETHRION_EXTERNAL_STANDARDS.md` §4.3; check 1 implemented |
| **PaperBench** | **PATTERN + BENCHMARK** | G7a / G7b | Its three-container separation — the agent builds in one, reproduction runs fresh in a second, grading happens in a third — is the working demonstration of the producer / reproducer / reviewer split this architecture asserts. The pattern is taken; the runtime is not embedded |
| **ResearchClawBench** | **BENCHMARK** | End-to-end metascience | 40 real research tasks across 10 domains with expert rubrics. It enables the experiment that would make this project's central claim testable — see §11 |

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
| **Cedar** | **DEPENDENCY** (first candidate) | Tool Broker · Execution Broker | Its `principal · action · resource · context` model already matches `TaskContract`, `forbid` overrides `permit`, and it has a formal semantics and schema validation. See `ADR-003` |
| **OPA / Rego** | **OPTIONAL BACKEND** | same | The general-purpose alternative, kept as the fallback in a recorded bake-off |
| **CaMeL** | **PATTERN** | WP-136 | Control flow comes from *trusted* intent; untrusted content may supply values but can never create actions or expand permissions. Reported 67–77 % of AgentDojo tasks solved with provable security depending on paper version |
| **Inspect sandboxes · gVisor · E2B** | **OPTIONAL BACKEND** | Execution Broker | AETHRION should own the `ExecutionBackend` interface and the **risk-profile → backend** routing, not the isolation technology |

**WP-136 changes character:** from *prompt-injection detection* to **trusted
control / untrusted data architecture**. A detector is defence in depth; it is
not a security boundary.

---

## 7. Provenance, identity and storage

| Component | Type | Where | Why |
|---|---|---|---|
| **Workflow Run RO-Crate** (Process / Workflow / Provenance profiles) | **STANDARD** | G5 `ExperimentRun` · G7 | Machine-actionable, engine-independent, re-execution aware, mapped to W3C PROV. **Priority raised: adopt before the first slice**, so the run format is never forked |
| **Croissant 1.1** (MLCommons) | **STANDARD** | Dataset records | Adds machine-actionable provenance via PROV-O and structured usage conditions via ODRL/DUO — which connects directly to policy: a dataset's `usagePolicy` becomes a Cedar input |
| **SWHID — ISO/IEC 18670** | **STANDARD** | G7 · G9 software identity | An intrinsic identifier computed from content, verifiable without a registry. Works for private code too, because computing it does not require archiving |
| **S3 Object Lock semantics** | **OPTIONAL BACKEND** | WP-026 | Compliance-mode WORM that no account, including root, can delete within retention |
| **lakeFS** | **OPTIONAL BACKEND** | Working datasets | Git-like branching over object storage for *mutable* research data — a different problem from accepted-evidence immutability, and worth keeping separate |
| **MLflow + OpenTelemetry** | **DEPENDENCY** | Observability | Traces, token usage, cost and tool calls over OTLP. **Operational observability only** — never the scientific truth store |

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
| **`nanopub-py`** | **ADAPTER** | Public claim export | A published claim as a FAIR nanopublication — **an export representation, not the operational ledger** |
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
| WP-049/050 | write a policy evaluator | **Cedar** policies, with a recorded OPA bake-off |
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
- statcheck (Python) — <https://github.com/hplisiecki/statcheck_python> · `grim` — <https://pypi.org/project/grim/> · `pysprite` — <https://github.com/QuentinAndre/pysprite> · `krippendorff` — <https://pypi.org/project/krippendorff/>
