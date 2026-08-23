---
title: "ADR-009 — Publication as Projection"
aliases:
  - "ADR-009"
cssclasses:
  - aethrion-decision-record
type: decision-record
category: architecture
status: ACCEPTED
summary: "The natural way to produce a paper from an AI research system is to give a model the results and ask it to write."
source: "docs/architecture/ADR-009_publication_as_projection.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
  - aethrion/adr
---

> [!info] Generated view
> This note is generated from `docs/architecture/ADR-009_publication_as_projection.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# ADR-009 — Publication as Projection

| Field | Value |
|---|---|
| Document type | Architecture decision record |
| Scope | Where a paper's sentences come from, and what a compiler refuses to emit |
| Sibling documents | `AETHRION_ARCHITECTURE.md` · ADR-007 · ADR-008 · WP-090 · WP-080 · ACC-52 · ACC-53 · ACC-76 |
| Status | **ACCEPTED — 2026-08-23.** Compiler contract decided; nothing is built |
| Date | 2026-08-23 |

**In one paragraph.** The natural way to produce a paper from an AI research
system is to give a model the results and ask it to write. That produces good
prose and an unfalsifiable document: the text is the only artifact, every
sentence has equal standing, and a fabricated number sits beside a measured one
in the same typeface. This record inverts the direction. The canonical state is
the claim, evidence and value graph; the document is a **projection** of it; and
the compiler's job is not to write well but to **refuse** — a factual sentence
with no claim behind it, or a number with no verified value under it, fails the
build.

---

## 1. The decision

> **The document is generated from canonical records, not from a model's account
> of them.** Every factual assertion is a `PublicationAssertion` bound to a
> `ClaimVersion` and to its evidence through `EvidenceTag`s. Every result number
> resolves to a `VerifiedValue`. **A factual sentence without a claim reference
> does not enter a final package**, and the build fails naming its location.

---

## 2. The direction of authority

```
ClaimVersions · EvidenceTags · VerifiedValues · Findings
Review findings · Reproduction status · DecisionRecord
                        │
                        ▼
              Publication Compiler
                        │
     ┌──────────┬───────┴────┬──────────┬──────────┐
     ▼          ▼            ▼          ▼          ▼
   PDF        DOCX         JATS      HTML      RO-Crate
```

A language model may draft wording. It is never the source of what the document
asserts, and the mapping from each sentence back to the record it renders is kept
rather than discarded — which is what makes the document traversable in the
direction that matters at G10: *this source was retracted; which published
sentences depend on it?*

---

## 3. Not every sentence is a claim

A rule that every sentence needs evidence would be unusable — headings,
transitions and declared limitations are not factual assertions, and a compiler
that blocks them blocks the document.

So assertions carry a `text_role`. Structural and editorial text is marked as
such and passes. Factual assertions require a `claim_ref`.

The discrimination is the test. ACC-52 puts a heading, a transition and one
unreferenced factual sentence into the same build and requires exactly one
failure. A checker that blocks all prose has not demonstrated anything except
that it can block.

---

## 4. Number grounding

Every result number resolves to a `VerifiedValue` (ADR-007). Formatting is
permitted and recorded: a declared rounding of a registered value passes and
writes its display transform to the manifest, while the canonical value is
unchanged.

The failure this closes is small and consequential. A writer stage substitutes
89.1% for 87.3% — a plausible number, in the right range, in fluent prose. No
reviewer reading for argument quality will catch it. The registry does, because
89.1 is not in it. ACC-53.

---

## 5. Support relations, and why they use a published vocabulary

An `EvidenceTag` binds an assertion to evidence with a relation: it supports,
challenges or contextualises. That looked like a three-value enum worth
inventing, and it is not — the Citation Typing Ontology already publishes exactly
this vocabulary, and this architecture's own rule is not to invent an identifier
scheme where one is maintained by people closer to the problem.

Binding the enum to CiTO IRIs costs nothing now and makes an evidence tag mean
the same thing outside this system as inside it. Recorded in
`provenance/upstreams.json` as a STANDARD.

---

## 6. Scope: the failure that survives every other check

The hardest defect to catch is a sentence where the citation is real, the
locator resolves, the passage is genuinely on topic — and the sentence claims
more than the passage supports.

```
Evidence:  "+4.2% over baseline B on dataset D under protocol P."
Refused:   "Method X solves this problem."
Permitted: "Method X improved metric M over baseline B by 4.2% on dataset D
            under protocol P."
```

Nothing was fabricated. The reference exists, the number is real, and the
sentence is wrong — it asserts generality the evidence does not carry. This is a
V2 check (ADR-008) and needs a qualified verifier before it can block anything.

The verifier proposes a bounded restatement; it does not apply one. A suggested
narrowing goes through the writer and the reviewer, because a system that
silently rewrites its own claims to make them pass has replaced one integrity
problem with a worse one.

---

## 7. Method sections are rendered, not written

The method section is rendered from the executed protocol, code and configuration
artifacts. Where prose is edited by hand afterwards, the method–code alignment
check is invalidated and must run again — an alignment result is about a specific
pair of texts, and editing one of them retires it.

---

## 8. Consequences

**Accepted:** authoring is less fluent. Sentences that would read well and cannot
be grounded do not survive, and some of them will have been true.

**Accepted:** the compiler is a real piece of infrastructure — assertion
extraction, claim binding, value resolution, tag verification, multi-format
rendering — and it is on the critical path for G9.

**Gained:** a published sentence can be traced to a source span, and a retracted
source can be traced to every sentence depending on it. Both directions, which is
the property the evidence chain exists to have.

**Gained:** the integrity audit becomes possible at all. Checking whether a paper
overclaims requires knowing which sentences are claims.

**Rejected:** a model as the source of truth for the document, with citations
attached afterwards. That is the arrangement in which references are
retro-fitted, and retro-fitted references are where fabricated ones come from.

---

## 9. Decision

**Accepted, 2026-08-23.** The compiler contract is what WP-090 delivers.
**Nothing is built** — there is no compiler, no assertion registry and no value
registry, and no document produced by this project has been through any of it.
