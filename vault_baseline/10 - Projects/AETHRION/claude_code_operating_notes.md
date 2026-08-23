---
title: "Claude Code Operating Notes"
aliases:
  - "CLAUDE"
  - "CLAUDE.md"
cssclasses:
  - aethrion-index
type: index
category: project
source: "CLAUDE.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/project
  - aethrion/index
---

> [!info] Generated view
> This note is generated from `CLAUDE.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# AETHRION

**Read [`AGENTS.md`](agent_operating_manual.md) first, completely.** It is the operating manual —
what this repository is, what actually runs versus what is only designed, the
rules that are not negotiable, the common tasks, and the hazards that have
already bitten. It is written for any agent, and it is validated by
`scripts/check_agent_guide.py` in the verification bundle.

This file exists because Claude Code reads it automatically. It adds only what is
specific to Claude Code; everything else is in `AGENTS.md` and is not repeated
here, because two copies of a rule become two versions of it.

## Start of session

```bash
uv run python scripts/write_status.py    # must print 20/20
python3 scripts/ready_queue.py
git log --oneline -5
```

## Skills

`skills/` holds 52 Agent Skills in the open format, and `.claude/skills` is
wired to it, so they load in this harness. Two families over one shared
discipline core:

| Family | Count | Origin |
|---|---:|---|
| Engineering | 11 | Vendored verbatim from `obra/superpowers`, pinned commit |
| Scientific research | 31 | AETHRION-native |
| Shared discipline | 10 | AETHRION-native |

Start from `skills/using-aethrion/SKILL.md` — it is the router that classifies a
task before any other skill is chosen. **None of the 52 has a behaviour
baseline**: they conform to the format and load, and that is a different claim
from working.

Do not rewrite the vendored eleven. They keep upstream attribution, their licence
and their pinned commit; changes belong upstream or in a native skill that
records `airl.derived_from`.

## Taking a mechanism from elsewhere

Much of what this system needs was solved somewhere else first, and adapting a
mechanism is expected rather than exceptional. Two rules make it auditable, and
both live in [`ADR-004`](04 - Architecture/adr_004_mechanism_assimilation.md):

**A mechanism may be taken; an architecture may not.** No external project is a
runtime module, directory, backend, class name or configuration key here. If you
are about to write `src/third_party/<name>`, that is the signal to stop.

**Nothing moves without a register entry.** `provenance/upstreams.json`, checked
by `python3 scripts/check_upstream_lineage.py`. Direct adaptation needs a
permissive licence read at the source, a pinned commit, a named file list and a
characterisation suite written *before* the code moves. Reimplementation needs a
mechanism specification and must name **no** source files. Every entry states
what the mechanism may never decide.

The Bash tool here has **no network access**, so a commit cannot be pinned from
this session. Leave `pinned_commit` as `null` and the status as `PROPOSED` rather
than inventing a digest — the checker will refuse the entry the moment anyone
tries to move code under it, which is the intended behaviour.

## Model assignment

`docs/architecture/AETHRION_ROLE_MODEL_ASSIGNMENT.md` derives which actor class
executes each gate. The rule that overrides any preference: **a mechanical check,
where one exists, runs first and cannot be overridden by a model**; no model at
G5 or G7a; at G8 a model may only recommend.
