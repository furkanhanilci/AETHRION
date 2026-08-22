---
title: "Review records"
type: review
category: review
summary: "These documents are evidence, and evidence that gets edited to stay current stops being evidence."
source: "docs/review/README.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/review
---

> [!info] Generated view
> This note is generated from `docs/review/README.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Review records

| Field | Value |
|---|---|
| Document type | Index — frozen evidence about what was true on a date |
| Scope | Independent audits and verification reports |
| Sibling documents | `../STATUS.md` (live status, generated) |
| Status | **Frozen.** Nothing here is edited to match the present |
| Date | 2026-08-22 |

**In one paragraph.** These documents are evidence, and evidence that gets edited
to stay current stops being evidence. Their counts are wrong *today* and correct
*for their date*, which is exactly what a snapshot should be. Anything that must
stay current lives in `../STATUS.md`, which is generated rather than written.

| Record | Date | What it is |
|---|---|---|
| `FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md` | 2026-08-21 | The independent audit that produced findings C1, C2 and H1–H5. **Frozen** — its "130 work packages" is correct for that day |
| `2026-08-22_remediation_verification.md` | 2026-08-22 | What had been remediated against that audit. **Frozen**, superseded by `STATUS.md` |
| `CLAUDE_FULL_FRAMEWORK_REVIEW_PROMPT.md` | — | The prompt used to commission the audit, kept so the review can be repeated on the same terms |

## The rule, and its one exception

`DOCUMENT_STANDARD.md` §3 rule 4: **evidence is never edited.** The single
permitted exception is adding a banner that marks a document frozen and points to
what superseded it — which both reports above carry, and which is itself recorded
in the implementation log.

`scripts/check_stale_claims.py` exempts this directory by name, so its
deliberately-stale numbers never appear as findings.
