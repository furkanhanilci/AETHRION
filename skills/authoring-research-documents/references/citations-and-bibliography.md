# Citations and Bibliography

## The flow

```
Zotero                      human workspace: PDFs, annotations, curation
   ↓
AIRL Source Registry        canonical identity (airl_id, DOI, digest)
   ↓
project bibliography        Better BibTeX / CSL-JSON projection
   ↓
Quarto · Pandoc citeproc    rendering
```

**Identity flows one way.** The bibliography file is a *projection*; if a
citation key and the registry disagree, the registry is right and the projection
is regenerated.

## Rules

1. **Never fabricate a citation.** Not a DOI, not an author, not a year, not a
   venue. A missing source is a finding.
2. **No citation dumping.** Three references after a sentence, none of which was
   read, is worse than none — it manufactures the appearance of support.
3. **Cite the claim, not the topic.** A citation supports *this* sentence.
4. **Every reference resolves.** `scripts/verify_references.py` checks the
   registry against Crossref, OpenAlex and arXiv. **81.8 %** of the current
   registry corroborates; the unresolved remainder is DOI-less preprint material,
   which is *unindexed*, not fabricated.
5. **Citation style comes from CSL**, with the style version recorded. AIRL does
   not invent a citation-style language.
6. **Better BibTeX is an adapter.** Stable keys and auto-export make text
   authoring workable; they do not make BBT the identity authority.

## Zotero 8 note

Zotero 8 provides native citation keys. Before adding a Better BibTeX
dependency, check whether native behaviour already covers the project's needs —
**do not stand up a second citation-key authority for its own sake.**

## What is checked mechanically

| Check | Where |
|---|---|
| Key in text → entry in bibliography | `scripts/check_document.py` |
| Entry → canonical source record | Source Registry lookup |
| Reference resolves in a public authority | `scripts/verify_references.py` |
| Post-publication change or retraction | `scripts/monitor_sources.py` |

Whether the cited passage **supports** the claim is not among them.
