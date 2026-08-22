---
name: evidence-before-claim
description: "Use when drafting any claim, when a claim has no linked EvidenceSpan, or when a sentence asserts a fact in a report or publication"
metadata:
  airl.version: "1.0.0"
  airl.domain: "shared"
  airl.origin: "airl-native"
  airl.gates: "G3,G6,G9"
  airl.roles: "Evidence Extractor,Scientific Owner,Scientific Editor"
  airl.assurance_classes: "R1,R2,R3"
  airl.non_waivable: "true"
  airl.requires_skills: "anchoring-spans"
  airl.emits: "ClaimEvidenceLink"
  airl.mechanical_checks: "every_claim_resolves_to_span,span_quote_exact_match"
---

# Evidence Before Claim

## Iron law

> **EVERY ASSERTION MUST RESOLVE TO AN `EvidenceSpan` OR AN `ExperimentRun`.**
>
> An assertion that resolves to neither cannot be published.

## Procedure

1. Write the claim
2. Identify its basis: a literature span, or your own run
3. If a span: anchor it with `anchoring-spans`. The quote must match the source
   representation **exactly**
4. If a run: bind `run_id` plus the artifact hash
5. Assign `support_type`: `supports` / `contradicts` / `qualifies` /
   `contextualizes`
6. Bind contradicting evidence too — `contradicted_by` is not left empty
7. If no basis can be found: record `NOT_FOUND` and **drop the claim**

## Evidence type by claim type

| Claim type | Required binding |
|---|---|
| `empirical` | `ExperimentRun` + artifact hash |
| `methodological` | `EvidenceSpan` (source) or `ProtocolManifest` |
| `interpretive` | At least one `EvidenceSpan` **and** an explicit interpretation marker |

An interpretive claim presented without its marker reads as empirical. That is
the most common way overclaiming enters a report.

## Contradicting evidence is part of the claim

A claim whose `contradicted_by` list is empty asserts that no contradicting
evidence exists. That is itself a claim, and it requires evidence that the
search was performed. Record the search, not just the absence.

## Rationalization table

| Justification | Ruling |
|---|---|
| "This is common knowledge in the field" | **Show the source.** Common knowledge also has one. |
| "It follows obviously from the results" | If it is obvious, binding the `run_id` is trivial. Bind it. |
| "The paper says this but I could not find the exact sentence" | **A span you cannot find is not evidence.** Drop the claim or re-extract the source. |
| "The quote is approximate but the meaning is the same" | Exact match is required. Approximate quoting is the signature of fabrication. |
| "I took it from the abstract" | An abstract is a representation. Pin which representation. |
| "It is visible in the figure" | Figure data is extracted and hashed separately. |
| "The contradicting source is weak anyway" | Then say so in the record. **Do not omit it.** |

## Red flags

- The `quote_exact_match` mechanical check is red
- A DOI is present but no span is
- One span is cited as support for two mutually inconsistent claims
- `contradicted_by` is systematically empty across a whole project
