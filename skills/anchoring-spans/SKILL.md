---
name: anchoring-spans
description: "Use when creating an EvidenceSpan, when a source representation is re-extracted or updated, or when a span can no longer be located"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.adopted_components: "GROBID · Pub2TEI canonical TEI"
  airl.gates: "G3,G6,G10"
  airl.roles: "Evidence Extractor,Knowledge Steward"
  airl.assurance_classes: "R1,R2,R3"
  airl.emits: "EvidenceSpan,ReanchorRecord,ImpactCase"
  airl.mechanical_checks: "multi_selector_present,old_representation_hash_immutable"
---

# Anchoring Spans

## Adopted components

> **GROBID · Pub2TEI canonical TEI**

Because the original bytes are kept, a later parser produces `representation-v2` **without invalidating claims anchored to v1**.

Adoption type and authority boundary: `docs/architecture/AIRL_OS_COMPONENT_REUSE.md`.

## Core principle

Sources change; evidence must survive. Anchoring uses **multiple selectors**
precisely because any single one is fragile.

## Multi-selector (W3C Web Annotation)

Every span carries **at least three**:

| Selector | Content |
|---|---|
| `TextQuoteSelector` | `exact` + `prefix` + `suffix` |
| `TextPositionSelector` | `start` / `end` offsets |
| `StructureSelector` | page / paragraph / sentence |
| `PdfBoundingBoxSelector` | page + coordinates + OCR engine **and version** |

One selector is brittle. Three rarely break simultaneously — and when they
disagree, the disagreement itself is diagnostic.

## Strategy by format

| Format | Anchor | Fragility |
|---|---|---|
| PDF | hash + page + bbox + quote + OCR version | Low |
| HTML | snapshot hash + URL + CSS selector + quote | **High** — selectors change |
| EPUB | representation hash + CFI + quote | Low |
| Dataset | version hash + row key + column + value fingerprint | Low |
| Code | commit hash + symbol path + line range | Low (prefer AST path) |
| Preprint | arXiv id + **version** + page + bbox | Medium — high if version omitted |

## Re-anchoring state machine

When a source gains a new representation:

```
1. THE OLD content_hash REMAINS IMMUTABLE   → v1 evidence stays verifiable
2. The exact quote is searched in the new representation
3. Outcome:
     RELOCATED       single match     → claim: unchanged
     AMBIGUOUS       several matches  → claim: CHALLENGED  + ImpactCase
     NEEDS_REANCHOR  no match         → claim: CHALLENGED  + ImpactCase
     ORPHANED        source unreachable → claim: ORPHANED  + cascade
4. The G10 monitoring flow is triggered
```

## Iron law

> **AN OLD REPRESENTATION HASH IS NEVER OVERWRITTEN.**
>
> A new representation is a new record. The verifiability of prior evidence is
> preserved.

Overwriting would silently invalidate every claim anchored to the old text while
leaving the claims looking healthy.

## Red flags

- A single-selector span
- OCR engine or version not recorded
- No version number on a preprint anchor
- A claim still `ACTIVE` while its span is `ORPHANED`
- A re-anchor that produced `AMBIGUOUS` and was resolved by picking one silently
