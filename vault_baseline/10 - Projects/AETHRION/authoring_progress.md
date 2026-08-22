---
title: "Commissioning Authoring Progress"
airl_id: AETHRION-AUTHORING-PROGRESS
type: index
category: vault
status: active
summary: "Which package documents are authored. All 141 packages now carry a test procedure and an acceptance criteria document; this page is how that stays true."
generated: false
tags:
  - aethrion/index
  - aethrion/plan
---

# Commissioning Authoring Progress

> [!info] Why this page exists
> Every work package is three documents — the card, its **test procedures** and
> its **acceptance criteria**. The card's derived sections are generated and are
> always current. The two companions carry judgement, so they are authored one
> package at a time.

## Where this stands

| | |
|---|---:|
| Work packages | **141** |
| Test procedure documents authored | **141** |
| Acceptance criteria documents authored | **141** |
| Awaiting authorship | **0** |

Reached at baseline **v1.1.0**. The counts above are stated here and derived by
`scripts/check_doc_consistency.py`, so a document and the repository cannot
disagree about them.

## Still to author

```query
tag:#aethrion/authoring/pending
```

**This query should return nothing.** If it returns a page, a companion was added
or reset and needs writing — which is exactly what it is for. The
[[10 - Projects/AETHRION/graph_legend|graph]] colours those pages in the
`unauthored` colour, so a new one is visible before anyone runs a query.

## Authored

```query
tag:#aethrion/authoring/authored
```

## By workstream

| Workstream | Query |
|---|---|
| Governance | `tag:#aethrion/workstream/01-governance` |
| Contracts | `tag:#aethrion/workstream/02-contracts` |
| Foundation | `tag:#aethrion/workstream/03-foundation` |
| Control & event | `tag:#aethrion/workstream/04-control-event` |
| Model · agent · tool | `tag:#aethrion/workstream/05-model-agent-tool` |
| Execution & security | `tag:#aethrion/workstream/06-execution-security` |
| Literature & knowledge | `tag:#aethrion/workstream/07-literature-knowledge` |
| Evidence & assurance | `tag:#aethrion/workstream/08-evidence-assurance` |
| Experience & observability | `tag:#aethrion/workstream/09-experience-observability` |
| Integration & cutover | `tag:#aethrion/workstream/10-integration-cutover` |
| Day-2 operations | `tag:#aethrion/workstream/11-day2-operations` |
| Tooling integration | `tag:#aethrion/workstream/13-tooling-integration` |

## Useful filters

| Question | Query |
|---|---|
| Every test procedure | `tag:#aethrion/test-procedure` |
| Every acceptance criteria document | `tag:#aethrion/acceptance-criteria` |
| Packages in the contract-spine wave | `tag:#aethrion/wave/w1` |
| Large-effort packages | `tag:#aethrion/effort/l` |
| Packages touching G5 | `tag:#aethrion/gate/g5` |

The full vocabulary is in [[_meta/taxonomy|Tag Taxonomy]]. A tag outside it is a
lint finding — `scripts/check_vault.py` runs in the verification bundle.

## What being written does not mean

Every package now states how it would be tested and what would count as
acceptance. **None has been executed.** `docs/STATUS.md` reports the position
without softening it: no package is `ACCEPTED`, no acceptance scenario has been
run, and no research question has travelled G0 to G10.

Authoring made the programme executable. It did not execute it.

## Rule of use

These documents are **generated into the vault** from
`planning/commissioning/`. Editing one here is lost on the next mirror. Change
the canonical file in the repository, regenerate, re-sync — the same rule that
governs every *Generated view* in this vault.
