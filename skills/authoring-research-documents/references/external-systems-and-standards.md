# External Systems and Standards — Authoring and Reporting

**Retrieved 2026-08-22.** Every version, licence and capability below is a
snapshot. Re-verify at implementation time and update `docs_retrieved_at`. A
claim such as *"the current JATS version"* or *"the venue's page limit"* is
**re-verified before it enters durable documentation**, never recalled.

**Evidence hierarchy for these decisions** — a lower-ranked source never
overrides a higher one:

1. Normative standard (NISO · ISO · W3C · DataCite · ORCID · ROR)
2. Official project documentation
3. Official maintained repository
4. Peer-reviewed paper describing the system
5. Preprint
6. Maintainer-authored technical writing
7. Third-party tutorials — **discovery only**

## Adoption types

`DEPENDENCY` · `ADAPTER` · `STANDARD` · `BENCHMARK` · `PATTERN` ·
`OPTIONAL_BACKEND` · `REJECTED` — defined in
`docs/architecture/AETHRION_COMPONENT_REUSE.md` §1.

**Every record carries an `authority_boundary`.** A component that cannot be
given one does not enter a gate.

---

## 1. Authoring and rendering

### 1.1 Quarto — `DEPENDENCY` (provisional orchestrator)

```yaml
id: quarto
category: authoring-orchestrator
adoption_type: DEPENDENCY
airl_integration_point: AuthoringBackend · DocumentSource render path
primary_official_url: https://quarto.org/docs/manuscripts/
docs_retrieved_at: 2026-08-22
capability_used: manuscript projects · citations · cross references · multi-format
  render (HTML · PDF · DOCX · LaTeX) · JATS output · MECA bundle when jats is an
  output format
capability_not_used: scientific judgement of any kind
authority_boundary:
  external_tool_may: "render a document and resolve its internal references"
  external_tool_may_not: "decide whether a claim is supported, or whether a
    document may be published"
known_failure_modes: a successful render is silently read as a valid document;
  template drift against venue requirements
fallback: Pandoc directly
decision: PROVISIONAL — confirmed only by the bake-off in
  `authoring-backend-bakeoff.md`, which has NOT been run
```

> **`quarto render` exiting zero means the document rendered.** It does not mean
> the document is correct, complete, venue-compliant or true.

### 1.2 Pandoc — `DEPENDENCY`

Document AST, `--reference-doc` DOCX styling, citeproc, BibTeX/BibLaTeX/CSL-JSON
input, Lua filters. **AIRL transformations are Lua filters over the AST, never
regular expressions over a manuscript.**

`authority_boundary` — Pandoc transforms structure; it does not certify meaning.

### 1.3 MyST — `OPTIONAL_BACKEND`

A competing scientific authoring stack with HTML, LaTeX, Typst, JATS, DOCX and
journal templates. The review reported *"more than 400 journal templates"*; that
figure is **UNVERIFIED here** and must be checked against `mystmd.org` before it
is repeated.

**The rule that matters more than the choice:** the canonical objects stay AIRL
objects. The same `DocumentContract`, `ClaimCitationMatrix` and bibliography
projection must render through either backend, or the loss of portability is
recorded explicitly.

### 1.4 Typst — `OPTIONAL_BACKEND`

Likely default PDF backend where the venue does not mandate LaTeX. Evaluate
bibliography/CSL support, PDF standard conformance, font embedding, equations,
cross references and deterministic build before use.

### 1.5 LaTeX and official venue templates — `OPTIONAL_BACKEND` + `ADAPTER`

> **The AIRL generic template never overrides an official venue template.**

Venue tooling is invoked where it exists — IEEE's template selector, reference
preparation assistant, LaTeX analyzer and PDF checker; ACM's `acmart` and TAPS;
publisher-specific guides. Each `VenueProfile` records the exact page retrieved
and when.

### 1.6 Manubot — `PATTERN`

Manuscript-as-code: Git source, pull-request review, continuous rebuild,
citation by persistent identifier, transparent history. **Taken as a pattern,
not as a second manuscript engine.**

| Manubot | AIRL |
|---|---|
| Git manuscript source | `DocumentSource` |
| CI build | reporting QA bundle |
| citation by identifier | Source Registry projection |
| PR review | AIRL review workflow |
| continuous rebuild | `RenderManifest` regeneration |
| history | evidence-backed revision log |

---

## 2. Document ingestion

### 2.1 Docling — `ADAPTER`

Converts PDF, DOCX, PPTX, HTML and images into a structured representation. Used
for **importing an existing report for revision**, not for evidence extraction.

> **The boundary with GROBID is not negotiable without measurement.**
>
> ```
> scholarly evidence PDF  → GROBID / Pub2TEI → canonical EvidenceSpan
> general editable report → Docling          → authoring normalisation
> ```
>
> Replacing GROBID with Docling on the evidence path requires a measured
> comparison, not convenience.

---

## 3. Bibliography and citation

| Component | Type | Role | Boundary |
|---|---|---|---|
| **Zotero** | existing system | Human literature workspace: PDFs, annotations, metadata curation | Not replaced by any authoring tool |
| **Better BibTeX** | `ADAPTER` | Project-scoped, version-control-friendly BibLaTeX/CSL-JSON export with stable keys and auto-export | **Not canonical identity.** Identity stays with the AIRL Source Registry, Zotero item identity and DOI/arXiv identifiers |
| **CSL** | `STANDARD` | Citation styles. AIRL does **not** invent a citation-style language | Records style, version/digest and venue mapping |
| **Crossref** | `DEPENDENCY` | Reference verification — **implemented** in `scripts/verify_references.py` | May say a record exists or changed; may **not** say a source supports a claim |

---

## 4. Identity and contribution metadata

| Standard | Type | Snapshot (2026-08-22) | Boundary |
|---|---|---|---|
| **DataCite Metadata Schema** | `STANDARD` | **4.7, released 3 March 2026**; adds `SWHID` as a `relatedIdentifierType` — which connects directly to AIRL's SWHID adoption | Describes an object; does not decide what is published |
| **ORCID** | `STANDARD` | Prefer authenticated collection where a submission workflow supports it | A manually supplied ORCID is preserved with its verification state. **An agent never invents an ORCID** |
| **ROR** | `STANDARD` | Structured affiliations | **Never rewrite an author's affiliation because fuzzy matching guessed another organisation** |
| **CRediT** | `STANDARD` | 14 contributor roles; ANSI/NISO Z39.104-2022 — **version to re-verify** | Describes contribution. Does **not** decide authorship eligibility, order, corresponding authorship, or disputes |
| **CITATION.cff** | `STANDARD` / optional output | Emitted when a package ships software | Not a replacement for the manuscript bibliography |

---

## 5. Scholarly interchange

| Standard | Type | Snapshot | Use |
|---|---|---|---|
| **JATS** | `STANDARD` / optional export | 1.4 / ANSI-NISO Z39.96-2024 claimed by review — **re-verify** | Journal workflows and machine-readable interchange. **Never the default authoring format** |
| **JATS4R** | `STANDARD` / conformance reference | Recommendations on authors, ORCID, ROR, CRediT, citations, data availability, figures, funding, ethics, peer review | **JATS-valid is not JATS-reusable.** A JATS export is validated against the applicable recommendations |
| **MECA** | `STANDARD` / optional package | NISO RP-30-2023 claimed by review — **re-verify** | Submission exchange archive. Quarto emits a MECA bundle when `jats` is an output format. Not required for internal reports |

---

## 6. Reporting guidelines and report structure

| Reference | Type | Scope caution |
|---|---|---|
| **EQUATOR Network** | `STANDARD` resolver | **Primarily health research.** Do not import CONSORT or STROBE into autonomous-driving, robotics or software-engineering work because they sound rigorous |
| **PRISMA / PRISMA-S / PRISMA-LSR** | `STANDARD` | Already adopted for G3 and G10 |
| **ANSI/NISO Z39.18-2005 (R2010)** | `PATTERN` / reference | Scientific and technical reports: elements, organisation, front and back matter, visual matter. Old — **verify status**, and never let it override current customer, institutional or accessibility requirements |
| **ISO 7144:1986** | reference | Presentation of theses. **University regulations always override it** |

The resolver returns a guideline, its version, an applicability rationale and the
checklist — or **`none_applicable`**, which is a legitimate result. Forcing a
checklist that does not fit is worse than having none.

---

## 7. Quality assurance

| Component | Type | Use | Boundary |
|---|---|---|---|
| **Vale** | `DEPENDENCY` | Deterministic prose linting: terminology, acronyms, placeholders, banned promotional language, heading conventions | Reliable only for lexical and structural rules. *"This claim is weak"* is not a linter's judgement |
| **LanguageTool** | `OPTIONAL_BACKEND` | Grammar and spelling | **The public free API states automated traffic should not be sent to it** — AIRL uses a local or licensed instance. Suggestions never carry authority over technical meaning |
| **WCAG 2.2** | `STANDARD` | HTML output accessibility | A few automated checks are not a complete accessibility audit |
| **veraPDF** | `DEPENDENCY` / validation backend | PDF/A and PDF/UA conformance of the **rendered artifact**, not the renderer's configuration | Machine-verifiable rules only; passing is not proof of human accessibility |

---

## 8. Figure methodology

Recorded as `PATTERN` in every case, with **no upstream code treated as a runtime
dependency and no text copied**: Paper Framework Figure Studio Pro (semantic
graph contract, visible-text allowlist, negative constraints), Scientific Figure
Generator (topology matching), Academic Figure Skills (staged separation of
content, architecture, specification, palette), ResearchFigureSkill (evidence
locking, five-second message), Academic Figure Generator (editable diagram
generation), **PaperBanana** (`PATTERN` + `BENCHMARK`: retrieval → content
planning → style planning → rendering → self-critique → refinement), **DiagramRAG**
(`PATTERN`: structural rather than cosmetic reference matching).

> **Licences are verified before anything is copied.** A public repository is not
> a licence, a paper is not a code licence, and a template is not redistribution
> permission. Architectural patterns may be referenced without copying
> implementation text — which is what is being done here.

The extracted methodology lives in `skills/producing-figures/`.

---

## 9. Rejected

| Candidate | Why |
|---|---|
| A bespoke Markdown dialect | Pandoc's AST and Quarto's syntax already exist and are maintained |
| A bespoke citation-style language | CSL exists and journals publish styles for it |
| A bespoke PDF typesetter, DOCX renderer, grammar engine or cross-reference engine | Each is a solved problem with maintained implementations |
| A report-specific reference database | Zotero plus the Source Registry already hold identity |
| LanguageTool's public free endpoint for automated runs | The service's own documentation says not to |
