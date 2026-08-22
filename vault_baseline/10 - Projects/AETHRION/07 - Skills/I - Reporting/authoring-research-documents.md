---
title: "Authoring Research Documents"
aliases:
  - "authoring-research-documents"
cssclasses:
  - aethrion-skill
type: skill
category: skill
status: WORKING
source: "skills/authoring-research-documents/SKILL.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/skill
  - aethrion/skill-family/scientific-research
  - aethrion/skill-origin/airl-native
---

> [!info] Generated view
> This note is generated from `skills/authoring-research-documents/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: authoring-research-documents
description: "Use when a research, scientific, technical or R&D document must be planned, drafted, revised, rendered or prepared for publication or formal delivery; also when choosing document structure, a target venue, or an output format"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G2,G3,G5,G6,G8,G9"
  airl.roles: "Scientific Owner,Scientific Editor,Evidence Lead,Statistical Methods Owner,Data Steward"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "false"
  airl.requires_skills: "evidence-before-claim,scope-discipline,reporting-results,producing-figures,curating-zotero"
  airl.emits: "DocumentContract,DocumentOutline,ClaimCitationMatrix,RenderManifest"
  airl.mechanical_checks: "no_unresolved_placeholders,citations_resolve,crossrefs_resolve,claims_resolve_to_evidence"
---

# Authoring Research Documents

## Core principle

> **A document is a projection of verified state, not a generative act.**
> The pipeline is `evidence → claims → structure → prose → figures → QA →
> render`, and it is never collapsed into "write me a paper".

This skill is a **conductor**, not the orchestra. It sequences work that other
skills own, and loads one reference module at a time.

## First: is there anything to write?

Before planning a document, establish that the evidence exists.

| Question | If the answer is no |
|---|---|
| Can every intended claim resolve to an `EvidenceSpan`, an `ExperimentRun` or a declared assumption? | The gap is a **finding**, not a paragraph to fill |
| Is the analysis complete, or is the writing hoping to settle it? | Stop. Writing is not a method |
| Is the target reader and their decision known? | Fix that first — structure follows purpose |

**Writing does not create evidence.** A document that would need a fact to be
invented is not ready to be drafted.

## The procedure

```
0  INTAKE            is the corpus complete enough to write?
1  MISSION           reader · their decision · the central message
2  EVIDENCE          inventory: sources, runs, results, gaps, contradictions
3  CLAIMS            candidate claims with type, support, scope — before prose
4  ARCHETYPE         document type → structure (IMRaD is not the default)
5  OUTLINE           sections, claims per section, budget
6  NARRATIVE         the reader's path
7  DRAFT             section by section, from the claim matrix
8  FIGURES/TABLES    inventories first, then `producing-figures`
9  RESOLUTION        citations, cross references, notation
10 SCIENTIFIC QA     does every statement match its source artifact?
11 STATISTICAL QA    do the reported numbers follow from the data?
12 GUIDELINE QA      the applicable reporting guideline only
13 LANGUAGE QA       deterministic linting; suggestions never auto-applied
14 VENUE QA          against current authoritative instructions
15 RENDER            requested formats only
16 ARTIFACT QA       inspect the rendered PDF/DOCX, not just the source
17 REVIEW            through the existing review skills
18 REVISION          without silent scope expansion
19 PACKAGE           PublicationPackage with provenance
```

Steps 0–6 happen **before** a renderer is chosen. Formatting is downstream.

## Reference modules — load one when its phase is reached

| Module | Load when |
|---|---|
| `references/reporting-architecture.md` | orienting: how this subsystem sits inside G0–G10 |
| `references/document-archetypes.md` | phase 4 — choosing the structure |
| `references/document-contract.md` | phase 1 — fixing scope, venue, limits |
| `references/claim-citation-matrix.md` | phase 3 and 9 |
| `references/writing-by-document-type.md` | phase 7 |
| `references/citations-and-bibliography.md` | phase 9 |
| `references/venue-and-reporting-guidelines.md` | phases 12 and 14 |
| `references/qa-and-accessibility.md` | phases 10–13, 16 |
| `references/rendering-export-and-packaging.md` | phases 15 and 19 |
| `references/revision-and-review.md` | phases 17–18 |
| `references/external-systems-and-standards.md` | choosing or defending a tool |
| `references/authoring-backend-bakeoff.md` | before fixing the authoring stack |

## Iron rules

1. **Evidence before prose.** No substantive assertion is written because it
   sounds plausible. Observation, measurement, external claim, internal result,
   interpretation, inference, hypothesis, recommendation and decision are
   **distinct categories** and are not flattened into fluent paragraphs.
2. **Never fabricate** a reference, DOI, author, number, uncertainty, method,
   dataset, limitation, contribution or causal relationship. Absent information
   is omitted, marked unresolved, or stated as a limitation.
3. **Structure follows purpose.** IMRaD is one archetype. An R&D report, a
   thesis chapter and a decision memo have different topologies.
4. **Venue instructions override generic style**, and are read from the current
   official source with the retrieval date recorded — never from memory.
5. **Rendering success is not validity.** `quarto render` exiting zero means the
   document rendered. It says nothing about whether it is true.
6. **Negative and null results are not rhetorically erased.** Under in-principle
   acceptance the direction of a result does not decide whether it is reported.
7. **A grammar suggestion may never silently change technical meaning.**

## Mechanical verification

```bash
uv run python scripts/check_document.py <document.qmd>   # placeholders · crossrefs · citations
uv run python scripts/verify_references.py               # every reference resolves
python3 scripts/check_reporting_registry.py              # adopted components are documented
```

## Rationalization table

| What gets said | Ruling |
|---|---|
| "The section needs a result here to feel complete" | **That is fabrication.** An empty section is a finding |
| "I'll add citations to support this paragraph" | **Backwards.** Citations follow evidence; evidence precedes the sentence |
| "Let's use the IEEE template, it looks professional" | **Formatting is downstream.** And the template comes from IEEE, not from memory |
| "The null result weakens the story" | **It is in protocol scope.** It stays |
| "It rendered, so it's done" | **Rendering is not validity.** Artifact QA and review come after |
| "The grammar checker suggested it, so I applied it" | **Not to a technical statement.** Review it |
| "IMRaD is standard" | **For journal articles.** Not for an R&D report |

## Red flags

- A renderer chosen before the claim inventory exists
- A citation added to make a sentence look supported
- A conclusion broader than any result behind it
- A figure inserted because the page looks text-heavy
- Venue compliance asserted without a retrieval timestamp
- `TODO`, `TBD` or `XXX` surviving into a rendered artifact
