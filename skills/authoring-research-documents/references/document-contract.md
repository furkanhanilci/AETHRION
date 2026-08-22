# Document Contract

Fixed **before** drafting, and minimal for simple documents. A technical memo
needs six fields; a journal submission needs most of them.

```yaml
DocumentContract:
  document_id:
  project_id:
  document_type:            # see document-archetypes.md
  document_status:          # OUTLINE · DRAFT · EVIDENCE_REVIEW · SCIENTIFIC_REVIEW
                            # EDITORIAL_REVIEW · VENUE_QA · READY_FOR_DECISION
                            # ACCEPTED · SUBMITTED · SUPERSEDED
  objective:
  primary_reader:
  reader_decision_or_action:
  language:

  target_venue:
  venue_guideline_source:   # exact URL
  venue_guideline_retrieved_at:
  template_source:
  template_digest:

  canonical_source_format:
  output_formats:           # only what is actually required
  citation_style:           # CSL identifier + version/digest
  bibliography_source:

  reporting_guideline:      # or none_applicable, which is a legitimate value
  required_sections:
  forbidden_sections:
  word_limit:
  page_limit:
  abstract_limit:
  figure_limit:
  table_limit:
  supplement_policy:

  evidence_scope:
  claim_scope:
  confidentiality_class:    # D0–D4
  assurance_class:          # R1 · R2 · R3
  review_mode:
  human_approval_required:
```

## Rules

**`document_status` uses the repository's status vocabulary.** It does not
introduce a competing one — see `docs/DOCUMENT_STANDARD.md` §2.

**Venue fields are retrieved, never recalled.** `venue_guideline_retrieved_at`
is mandatory whenever `target_venue` is set. Without it the contract carries
`status: UNVERIFIED_CURRENT_REQUIREMENT` and **no compliance may be claimed**.

**`output_formats` is a decision, not a default.** Generating every format
because the toolchain can is how unreviewed artifacts reach a reader.

**`confidentiality_class` bounds the toolchain.** A D3/D4 document may not be
sent to a hosted grammar service; that is a routing constraint, not a preference.

## Freshness policy

| Source kind | Time-to-live |
|---|---|
| Venue submission instructions | short — re-check each submission cycle |
| Normative standard with an explicit version | long — pin the version |
| Pinned local library documentation | version-bound, no clock TTL |
