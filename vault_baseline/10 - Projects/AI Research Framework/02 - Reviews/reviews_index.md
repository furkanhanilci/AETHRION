# Reviews Index

Independent review instructions and their results. **A review is not evidence
unless it is independent of the producer.**

## Review records

| Document | Type | Status |
|---|---|---|
| [[10 - Projects/AI Research Framework/02 - Reviews/claude_framework_audit_report\|Claude Framework Audit Report]] | Evidence-based independent audit | 2026-08-22 — complete |
| [[10 - Projects/AI Research Framework/02 - Reviews/claude_full_framework_review_prompt\|Full Framework Review Prompt]] | Review instruction | In use — corrected 2026-08-22 |

> **Note:** three incorrect directory paths were found in the review prompt
> (`09_OPERATIONS`, `11_DECOMMISSION` and `13_CHANGE_CONTROL` do not exist).
> They have since been corrected in the prompt itself. Detail: audit report,
> Section K.

## Review discipline

- [[requesting-review]] — how a package is prepared
- [[receiving-review]] — how findings are answered
- [[blind-reviewing]] — blind review
- [[adversarial-reviewing]] — counter-argument and ACH
- [[arbitrating-disagreement]] — disagreement and the breaker

## The rule

A review result is accepted only when all three exist: the frozen package hash,
a record of independence from the producer, and a `ProducerResponse` for every
condition raised.
