# Revision and Review

## Diff-aware revision

Every material revision records: which claims changed · which evidence links
changed · which figures or tables changed · which interpretation changed · the
reviewer request or rationale · who approved it.

**Change classes are separated**, because recording a typo as a claim revision
destroys the signal the log exists to carry:

| Class | Example | Triggers |
|---|---|---|
| `EDITORIAL` | wording, typo | no re-review |
| `STRUCTURAL` | section moved | outline check |
| `SEMANTIC` | a claim's meaning changed | scientific QA |
| `EVIDENCE` | support added, removed or replaced | evidence review |
| `RESULT` | a number changed | statistical QA + re-review |
| `POLICY` | venue or template changed | venue QA |

**No silent evidence drift.** A changed number is never an editorial change.

## Reviewer response

Reuse the existing `receiving-review` skill rather than building a parallel
review authority. Each comment is decomposed, checked against evidence, and given
a stance:

| Stance | Means |
|---|---|
| `ACCEPTED` | change made — location recorded |
| `PARTIALLY_ACCEPTED` | part made, part declined with reasons |
| `CLARIFIED` | no change; the text already said it, or now says it more clearly |
| `DECLINED_WITH_EVIDENCE` | the request is not supported by the evidence |
| `REQUIRES_HUMAN_DECISION` | scope, authorship, or a scientific judgement |

> **A scientifically incorrect reviewer request is not conceded for smoothness.**
> Performative agreement is forbidden here for the same reason it is forbidden in
> `receiving-review`: it converts a disagreement into a silent error.

## Human authority

Never inferred by an agent, in any document:

authorship inclusion or exclusion · author order · corresponding author ·
CRediT disputes · conflicts of interest · funding declarations · ethics approval ·
acknowledgements implying someone's consent.

An agent may **draft these from supplied records**. A human confirms. An ORCID is
never invented, and an affiliation is never rewritten because fuzzy matching
guessed a different organisation.
