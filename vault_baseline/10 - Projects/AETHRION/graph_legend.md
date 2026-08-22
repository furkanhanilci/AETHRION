---
title: "Graph Legend"
type: index
category: vault
status: active
summary: "What each colour in the graph view means, and why colour is never the only carrier of the distinction."
generated: true
provenance: scripts/make_vault_graph.py
tags:
  - aethrion/index
---

# Graph Legend

> [!info] Generated view
> Produced by `scripts/make_vault_graph.py`, which also writes
> `.obsidian/graph.json`. Change the generator, not this page.

The graph is coloured by **kind**, using the same Okabe-Ito palette as the
figures in `docs/figures/` — so a colour means the same thing in a diagram
and in the graph. Okabe-Ito is used because it stays distinguishable under
the common forms of colour vision deficiency. Two colours from Paul Tol's
muted palette were added to separate the vault's two halves: the projection
of the repository, and the second brain the researcher writes in.

**Every page takes a colour.** An audit found thirty nodes matching no group
— the programme documents, the project workspace, the human areas, the daily
notes and the templates — and a node with no group is a node the graph cannot
say anything about, which is the one thing this view exists to fix.

**Colour never carries a distinction alone.** Every group below is also a
tag, so the same separation is available in search, in a query and in
[[_meta/taxonomy|the taxonomy]] to a reader who cannot use the colour.

| | Group | Tag | Why this colour |
|---|---|---|---|
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#D55E00;border-radius:2px"></span> `#D55E00` | Unauthored — needs work | `aethrion/authoring/pending` | human authority: these are the documents waiting on judgement, and the cluster shape is the most useful thing the graph shows |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#E69F00;border-radius:2px"></span> `#E69F00` | Work package | `aethrion/work-package` | frozen artifact: the sealed plan |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#009E73;border-radius:2px"></span> `#009E73` | Test procedure | `aethrion/test-procedure` | mechanical check: how a package is tested |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#0072B2;border-radius:2px"></span> `#0072B2` | Acceptance criteria | `aethrion/acceptance-criteria` | the verifier's document — read by someone who did not do the work |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#CC79A7;border-radius:2px"></span> `#CC79A7` | Acceptance scenario | `aethrion/acceptance-scenario` | revision / feedback: what the system must demonstrate end to end |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#56B4E9;border-radius:2px"></span> `#56B4E9` | Architecture and decisions | `aethrion/architecture` | reference material: the target design and its ADRs |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#0072B2;border-radius:2px"></span> `#0072B2` | Skill | `aethrion/skill` | model production: the discipline agents execute under |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#F0E442;border-radius:2px"></span> `#F0E442` | Literature source | `aethrion/source` | external source: projected from Zotero, never authored here |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#63666A;border-radius:2px"></span> `#63666A` | Index and navigation | `aethrion/index` | navigation: hubs rather than content |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#CC79A7;border-radius:2px"></span> `#CC79A7` | Review and findings | `aethrion/review` | revision / feedback: frozen audits and the findings register |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#E69F00;border-radius:2px"></span> `#E69F00` | Programme document | `aethrion/commissioning` | frozen artifact: 00_PROGRAM is the plan's own constitution, so it shares the plan's colour |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#882255;border-radius:2px"></span> `#882255` | Project workspace | `aethrion/project` | where the operator works: cockpit, status, handover, evidence, components |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#44AA99;border-radius:2px"></span> `#44AA99` | Human synthesis | `aethrion/claim` | the second brain: the areas a human writes in, distinct from everything projected from the repository |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#63666A;border-radius:2px"></span> `#63666A` | Daily note | `aethrion/daily` | navigation: entered by date rather than by link |
| <span style="display:inline-block;width:0.9em;height:0.9em;background:#63666A;border-radius:2px"></span> `#63666A` | Template | `path:"_Templates"` | navigation: deliberately unlinked, and not content |

## The group worth watching

**Unauthored — needs work.** Every package is three documents, and the two
companions carry judgement rather than derivation. An unauthored one says
so rather than pretending otherwise, and in the graph they cluster: a dense
patch of that colour around one workstream is a fact about the programme
that no status page states as directly.

Track the count on [[10 - Projects/AETHRION/authoring_progress|Authoring Progress]].

## Where these colours appear

The graph is one surface. `scripts/make_vault_theme.py` generates a CSS
snippet — loaded natively from `.obsidian/snippets/`, no plugin — that
carries the same eight colours to:

| Surface | What is coloured |
|---|---|
| File explorer | Each top-level area gets a left border in its colour, so the shape of the vault is legible before anything is opened |
| File explorer | `.tests.md` and `.acceptance.md` are tinted, separating a package's three documents at a glance |
| Tag pills | Every `aethrion/` namespace takes its group colour |
| The `type` property | Shown on every generated page, coloured by kind |
| Search results | Test and acceptance documents are distinguishable in a result list |
| Callouts | *Generated view* is muted; **warning** stays loud, because it marks the two places this vault destroys work |

Every colour is defined twice — once for the light theme, once for dark —
so switching theme does not lose the mapping.

## Orphans stay visible

`showOrphans` is on deliberately. An unreachable page is a finding —
`scripts/check_vault.py` reports it in the verification bundle — and hiding
it in the view would remove the only place it is obvious.

