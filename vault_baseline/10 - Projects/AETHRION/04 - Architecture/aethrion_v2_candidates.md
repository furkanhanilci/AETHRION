---
title: "V2 Candidates"
type: reference
category: architecture
summary: "V1 is the sealed commissioning baseline: WP-000–140, ACC-01–51, completed when the go-live checklist's entry conditions hold."
source: "docs/V2_CANDIDATES.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/architecture
---

> [!info] Generated view
> This note is generated from `docs/V2_CANDIDATES.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# V2 Candidates

| Field | Value |
|---|---|
| Document type | Register — proposals deliberately outside the V1 baseline |
| Scope | Things worth doing that are **not** part of V1, and why they are parked |
| Sibling documents | `../planning/commissioning/README.md` (what V1 is) · `../planning/commissioning/00_PROGRAM/09_change_and_configuration_control.md` (how a change is recorded) |
| Status | Register — appended to, never used as authority |
| Date | 2026-08-22 |

**In one paragraph.** V1 is the sealed commissioning baseline: WP-000–140, ACC-01–51, completed when the go-live checklist's entry conditions hold. Anything that is not in that baseline is not V1, and this file is where it waits. The register exists so that "should we also add…" has somewhere to go other than the sealed plan — an idea written down here costs nothing, while the same idea written into `planning/` costs a re-seal and quietly moves the finish line.

> **This file is deliberately outside the hash seal.** Putting V2 candidates
> inside the V1 baseline would contradict the thing the baseline is for. Nothing
> here is committed to, scheduled, or counted in any progress figure.

---

## 1. How something gets here, and how it leaves

An idea arrives during V1 work. Three outcomes, and only three:

| Outcome | When | What happens |
|---|---|---|
| **Fix in V1** | It corrects a defect in the sealed plan — a wrong number, a false claim, a broken reference | Edit the plan, regenerate the seal, bump the baseline, record the reason. Two such changes have happened: v1.0.2 and v1.0.3, both naming and claims only |
| **Park as V2** | It adds capability, changes a requirement, or reshapes scope | Append a row below. Do not touch `planning/` |
| **Drop** | It does not survive being written down | Nothing. Not writing it down is also an answer |

The distinction that matters: **a correction keeps the finish line where it is; an addition moves it.** V1 is finishable only if the second kind is refused for the duration.

Leaving happens exactly once — when V1 reaches go-live and a V2 baseline is opened. Until then this file only grows.

---

## 2. Register

Each entry states what it is, why it is not V1, and what it would cost. Entries
are not ranked, because ranking implies a plan and there is no V2 plan.

| # | Candidate | Why not V1 | Cost if done later |
|---|---|---|---|
| V2-01 | Rename the Python packages `airl_bridge` → `aethrion_bridge`, `airl_framework` → `aethrion_framework` | Cosmetic. Breaks every import, the console script, the systemd units and the venv at once | Grows with each new consumer. Cheapest now, and still not worth a V1 slot |
| V2-02 | Rename the `airl_id` field to `aethrion_id` | Schema change: SQLite column, `SourceRecord`, the MCP tool contract and every vault frontmatter entry | Needs a data migration. Grows with the number of stored records |
| V2-03 | Rename the `airl.*` skill-metadata namespace | 52 skills, `validate_skills.py`, and eleven vendored skills whose upstream owns their frontmatter | Grows with the registry; the vendored eleven may never be renameable |
| V2-04 | Retire the `airl-interim-v0.1` attestation profile in favour of a keyless, transparency-logged one | **Already V1**: WP-139 is in the baseline. Listed here only so nobody adds it twice | — |
| V2-05 | Mirror the skill sub-resources (prompt templates, agent definitions) into the vault | Eleven links in the mirror point outside the mirrored subset and do not resolve in Obsidian. Cosmetic; the canonical files are one directory away in the repository | Constant. The alternative — deleting the links from the source documents — would make the repository worse to read |
| V2-07 | Rename the `AIRL-GENERATED-*` note identifiers the bridge writes into the vault | Emitted by `src/airl_bridge/obsidian.py`; a code change plus a regeneration of every projected note | Constant, and bounded — two identifiers, two lines |
| V2-06 | Rename the systemd unit files from `airl-bridge*` | Installed names on a running machine. A deployment change, not a documentation one | Grows with the number of machines; today that is one |

---

## 3. What this register is not

It is not a roadmap, not a backlog with estimates, and not a commitment. Six
entries after a full brand migration and three baseline corrections is a
deliberately small number: most of what surfaced during that work was a defect
and was fixed in V1, which is the outcome this file exists to keep separate from
the other one.
