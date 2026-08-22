---
name: extracting-evidence
description: "Use when a ClaimCandidate exists without a linked EvidenceSpan and at least one SourceRepresentation is available"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.adopted_components: "GROBID · Pub2TEI"
  airl.gates: "G3,G6"
  airl.roles: "Evidence Extractor"
  airl.assurance_classes: "R1,R2,R3"
  airl.requires_skills: "anchoring-spans,evidence-before-claim"
  airl.emits: "EvidenceSpan,ClaimEvidenceLink"
  airl.mechanical_checks: "quote_exact_match_in_representation,support_type_assigned"
---

# Extracting Evidence

## Adopted components

> **GROBID · Pub2TEI**

Scholarly PDFs and publisher XML become one canonical TEI representation, so a span addresses `tei_xpath` under a `representation_digest` rather than a page number.

Adoption type and authority boundary: `docs/architecture/AIRL_OS_COMPONENT_REUSE.md`.

## Core principle

Evidence is what the source **actually says** — not what you believe it says.

## Iron law

> **THE QUOTE MUST MATCH THE SOURCE REPRESENTATION EXACTLY.**
>
> A quote that cannot be located is not evidence. An approximate quote is a
> fabrication risk.

## Procedure

1. Read the claim; decide **which exact statement** would constitute support
2. Search the source representation — the one pinned by hash
3. Anchor the span with `anchoring-spans` (multi-selector)
4. Assign `support_type`:
   - `supports` — supports the claim
   - `contradicts` — refutes it
   - `qualifies` — conditions or limits it
   - `contextualizes` — provides background
5. Give a confidence score — **raw**; calibration happens in a separate layer
6. If not found: record `NOT_FOUND`. **Do not invent one.**

## Extraction quality

For PDFs, prefer structure-aware extraction (section structure, references,
coordinates) over flat text extraction — the difference shows up directly in
anchor stability. Record the tool and its version in `extraction_tool`.

## Context capture

A span is not only a sentence. `prefix` and `suffix` are recorded, because the
difference between *"X is not true"* and *"X is true"* lives in the context.

And: **never trim negation, condition or limitation clauses.** "X holds under
condition C" quoted as "X holds" is a fabricated claim assembled from real words.

## Contradicting evidence

Spans that refute the claim are sought and bound. `contradicted_by` is not left
empty; if it is, evidence of the search is required.

## Rationalization table

| Justification | Ruling |
|---|---|
| "The paper says this but I couldn't find the sentence" | **No evidence.** Drop the claim or re-extract the source. |
| "The wording differs but the meaning is the same" | Exact match required. |
| "I took it from the abstract" | An abstract is a representation. Pin which one. |
| "It's visible in the figure" | Figure data is extracted and hashed separately. |
| "The negation clause wasn't relevant" | It is always relevant. Quote it. |

## Red flags

- `quote_exact_match` is red — the signature of a fabricated citation
- One span supporting two mutually inconsistent claims
- `contradicted_by` systematically empty
- Extraction tool and version not recorded
