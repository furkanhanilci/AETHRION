---
title: "Naming and Terminology"
cssclasses:
  - aethrion-reference
type: reference
category: architecture
status: WORKING
summary: "The project is called AETHRION, and its official descriptor is Agentic Intelligence Research Layer."
source: "docs/branding.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
---

> [!info] Generated view
> This note is generated from `docs/branding.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Naming and Terminology

| Field | Value |
|---|---|
| Document type | Convention — canonical naming |
| Scope | What this project is called, what the acronym means, and which older names survive and why |
| Sibling documents | `DOCUMENT_STANDARD.md` (how documents are written) · `assets/branding/README.md` (the logo asset) |
| Status | `WORKING` — enforced by review, not yet by a checker |
| Date | 2026-08-22 |

**In one paragraph.** The project is called **AETHRION**, and its official descriptor is **Agentic Intelligence Research Layer**. `AIRL` is the abbreviation of that descriptor and survives as a technical term — in the control layer's name, in a metadata namespace, in a schema field, in service and package names — but it is not the product name and is not used as one. Older names appear only inside dated records, where changing them would falsify history.

---

## 1. Canonical forms

| Term | Meaning | Use |
|---|---|---|
| **AETHRION** | The project, the framework, the platform | The name. Use it. |
| **Agentic Intelligence Research Layer** | The official descriptor of AETHRION | Pairs with the name on first use |
| **AETHRION — Agentic Intelligence Research Layer** | Canonical first-use form | Once per document, at the top |
| **AIRL** | Abbreviation of *Agentic Intelligence Research Layer* | Technical contexts only — see §3 |

First meaningful use in a document:

> AETHRION — Agentic Intelligence Research Layer is an evidence-centred research
> system in which …

Every use after that: **AETHRION**.

## 2. What the name is not

The project is **not** called AETHRION OS, AETHRION-OS, AIRL-OS, AIROL-OS, or
"the AI Research Framework". There is no tagline. There is no slogan. A
descriptor is not a slogan: *Agentic Intelligence Research Layer* says what the
thing is, and nothing about how it will change your life.

"Research operating system" remains available as an **architectural analogy**,
because the architecture genuinely borrows the shape of one: a control plane
that owns process state, an execution layer that isolates work, a policy
decision point, an evidence store. It describes the design. It is not part of
the name, and it must not be capitalised into one.

## 3. When AIRL is correct

`AIRL` stays wherever it names the technical layer or an identifier that other
software depends on. It is retained deliberately, not left behind:

| Occurrence | Kind | Why it stays |
|---|---|---|
| `AIRL control layer` — the G0–G10 layer in the stack figure | Architecture | It *is* the Agentic Intelligence Research Layer; the acronym is accurate there |
| `airl.version`, `airl.domain`, `airl.origin`, `airl.gates`, … | Metadata namespace | Every skill's frontmatter carries it; `scripts/validate_skills.py` requires it |
| `airl.origin: airl-native` | Enum value | One of exactly two accepted values, the other being `superpowers` |
| `airl_id` | Schema field | Column in the source registry, field in `SourceRecord`, path segment in the MCP tool contract |
| `airl-bridge`, `airl-bridge-sync` | Service and unit names | Installed systemd units on a running machine |
| `src/airl_bridge/`, `src/airl_framework/` | Python packages | Import paths; renaming breaks every consumer |
| `AIRL_API_TOKEN`, `AIRL_API_HOST`, `AIRL_ZOTERO_LIBRARY_TYPE`, `X-AIRL-Token` | Environment and header names | Deployment contract |
| `airl-interim-v0.1` | Attestation profile | Named inside signed evidence; changing it invalidates the signature |
| `https://airl-os.local/EvidenceManifest/v0.1` | `predicateType` URI | Inside the signed DSSE payload of the issued attestation |
| `AIRL-SEPIO` | Mapping profile | A named crosswalk to an external standard |

The rule in one line:

> **AIRL names a layer or an identifier. AETHRION names the project.**

Where both appear together and a reader might be confused, say the relationship
once and move on:

> AIRL (Agentic Intelligence Research Layer) is the control layer inside
> AETHRION.

In prose, a skill authored here is an **AETHRION-native skill**; the machine
value recording that fact is `airl.origin: airl-native`. Prose and metadata are
allowed to differ, because one is read by people and the other by
`validate_skills.py` — but never in the same sentence without the backticks that
mark which is which.

## 4. Historical names

The project was documented as **AIRL-OS** before this migration, and before that
as the **AI Research Framework**. Both names survive in exactly two places:

1. **Dated, frozen records** under `review/` — an audit report describes what was
   true on a date, under the name in use on that date. Rewriting it would make
   the record disagree with the evidence it cites.
2. **Named historical inputs** — `AIRL-OS-Architecture.md` v1.0 is cited as the
   source document several architecture documents were derived from. It is a
   provenance reference, not a live link.

Where such a name appears, it carries a marker:

> *Historical name; current project identity: AETHRION.*

The sealed commissioning plan was re-sealed as **baseline v1.0.2** to carry the
current name, and again as **v1.0.3** to remove a false assurance claim the
rename pass had not touched. That is a recorded change under
`00_PROGRAM/09_change_and_configuration_control.md`, not a silent rewrite: the
seal was regenerated deliberately, the reason is written down, and the three
plan-integrity checks were re-run afterwards.

## 5. Visual identity

The logo lives at `assets/branding/aethrion-logo.png` and its provenance rules
are in `assets/branding/README.md`. It appears on the repository front page, the
principal architecture document and the Obsidian landing page — nowhere else.

Documentation accents follow the logo: crimson for emphasis, charcoal for text,
white ground. This is a **documentation** convention, not a stylesheet: figures
keep the Okabe–Ito palette specified in `figures/README.md`, because colour there
carries meaning and must survive colour-vision deficiency and greyscale printing.
Brand colour and information colour are different jobs, and this repository does
not let the first override the second.

## 6. What this document does not do

It does not rename code. A branding decision is not a licence to break an import
path, a schema field or a signature, and every identifier in §3 stays until
there is a technical reason and a migration for it. Candidate renames, with
their blast radius, are listed at the end of the migration report rather than
performed here.
