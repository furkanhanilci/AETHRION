> [!info] Generated view
> This note is generated from `skills/searching-literature/SKILL.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

---
name: searching-literature
description: "Use when a literature campaign starts, when coverage of a topic must be established, or when seed sources need expansion"
metadata:
  airl.version: "1.0.0"
  airl.domain: "scientific-research"
  airl.origin: "airl-native"
  airl.gates: "G3"
  airl.roles: "Evidence Lead,Search Strategist"
  airl.assurance_classes: "R1,R2,R3"
  airl.emits: "SearchProtocol,SourceCandidate"
  airl.mechanical_checks: "queries_recorded_verbatim,databases_and_dates_pinned"
---

# Searching Literature

## Core principle

A search is a **protocol**, not an exploration. Re-run later, it must return the
same result — or the difference must be explainable.

## Pre-registration

Written and locked before searching begins:

```yaml
queries: [...]              # verbatim, including operators
databases: [...]            # each with version and access date
date_range: "..."
inclusion_criteria: [...]
exclusion_criteria: [...]
language_policy: "..."
```

## Source diversity — one source is never enough

| Source | Purpose |
|---|---|
| **OpenAlex** | Broad coverage, citation graph, open |
| **Crossref** | DOI authority, metadata |
| **Semantic Scholar / S2ORC** | Full text, citation context |
| arXiv / bioRxiv | Preprints |
| **Unpaywall** | Lawful open-access full text |
| Domain-specific (PubMed, DBLP, IEEE) | Coverage completion |

**Multi-modal searching:** keyword, citation graph (forward **and** backward),
author, and domain taxonomy. No single method finds everything, and the items
each method misses are not random.

## Seed expansion

1. Start from `01_Human_Seed` — the human-selected core
2. **Backward citation** (references) and **forward citation** (who cited it)
3. Extract keywords from what you find → new queries
4. **Saturation:** stop when the last N sources introduce no new concept

Saturation is a stopping rule, not a feeling. State N in advance.

## Coverage analysis

Coverage is reported per topic. Uncovered sub-topics are **listed explicitly** —
a claim of "complete coverage" requires evidence, and the honest report names
what was not covered.

## Contradicting sources

> Sources that **refute** the finding are actively sought and written to
> `Project/Contradictory`. If none were found, that fact is reported along with
> evidence that the search was made.

An empty contradictory set with no search record is indistinguishable from not
having looked.

## Red flags

- Queries not recorded verbatim
- A single database used
- The contradictory section is empty with no evidence of searching
- No access date recorded — results are not reproducible
- Saturation asserted without a stated stopping rule
