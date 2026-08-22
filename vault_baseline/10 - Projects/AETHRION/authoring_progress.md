---
title: "Commissioning Authoring Progress"
airl_id: AETHRION-AUTHORING-PROGRESS
type: index
category: vault
status: active
summary: "Which package documents are authored and which still say so. Every package is three documents; this page tracks the two that carry judgement."
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
> package at a time, and an unauthored one says `*Not yet authored.*` rather than
> pretending otherwise.

## Still to author

```query
tag:#aethrion/authoring/pending
```

## Authored

```query
tag:#aethrion/authoring/authored
```

## By workstream

| Workstream | Packages |
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
| Packages on the critical path, by wave | `tag:#aethrion/wave/w1` |
| Large-effort packages | `tag:#aethrion/effort/l` |
| Packages touching G5 | `tag:#aethrion/gate/g5` |

The full vocabulary is in [[_meta/taxonomy|Tag Taxonomy]]. A tag outside it is a
lint finding — `scripts/check_vault.py` runs in the verification bundle.

## Rule of use

These documents are **generated into the vault** from
`planning/commissioning/`. Editing one here is lost on the next mirror. Change
the canonical file in the repository, regenerate, re-sync — the same rule that
governs every *Generated view* in this vault.
