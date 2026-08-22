# Claim–Citation Matrix

A **document projection** of the canonical claim/evidence relationships. It is
**not** a second Claim Ledger, and it never becomes the place a claim is defined.

```yaml
ClaimCitationRow:
  claim_id:                 # resolves into the Claim Ledger
  document_id:
  section_id:
  paragraph_id:
  claim_text_or_digest:
  claim_type:               # observation · measurement · external-source claim
                            # internal result · interpretation · inference
                            # hypothesis · recommendation · decision · assumption
  support_type:             # evidence_span · experiment_run · project_artifact
                            # declared_assumption · common_knowledge
  evidence_ids:
  citation_keys:
  experiment_run_ids:
  scope_qualification:
  status:                   # RESOLVED · UNRESOLVED · CONTESTED
  review_state:
```

## Why claim_type is not decoration

The characteristic failure of generated prose is not a false sentence — it is a
**category slide**: an interpretation written in the grammar of an observation.
Typing each row forces the distinction that fluent writing erases.

| Written as | Actually a | Consequence |
|---|---|---|
| "the method improves accuracy" | interpretation of one measurement | reader infers generality |
| "the sources confirm X" | external-source claim | reader infers internal verification |
| "the system is robust" | recommendation dressed as measurement | nothing supports it |

## Mechanically detectable

| Check | Fails when |
|---|---|
| Citation resolution | a key appears in text and not in the bibliography |
| Bibliography grounding | an entry maps to no canonical source record |
| Required evidence | a `measurement` or `internal result` row has no `experiment_run_ids` |
| Result linkage | a numeric result in prose resolves to no run |
| Orphan claims | a `RESOLVED` row whose evidence ids do not exist |
| Scope | sentence scope exceeds `scope_qualification` |

`scripts/check_document.py` implements the citation, cross-reference and
placeholder checks over a document source.

## The limit of the mechanism

Whether a cited passage **entails** the claim is not decided here. Entailment
checkers are instruments with their own error rates, not oracles — see
`AETHRION_EXTERNAL_STANDARDS.md` §5.1. The matrix proves a citation *resolves*;
a human or a measured checker decides whether it *supports*.
