---
title: "V2 Candidates"
cssclasses:
  - aethrion-reference
type: reference
category: architecture
summary: "V1 is the sealed commissioning baseline: WP-000–147, ACC-01–80, completed when the go-live checklist's entry conditions hold."
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
| Date | 2026-08-23 |

**In one paragraph.** V1 is the sealed commissioning baseline: WP-000–147, ACC-01–80, completed when the go-live checklist's entry conditions hold. Anything that is not in that baseline is not V1, and this file is where it waits. The register exists so that "should we also add…" has somewhere to go other than the sealed plan — an idea written down here costs nothing, while the same idea written into `planning/` costs a re-seal and quietly moves the finish line.

> **This file is deliberately outside the hash seal.** Putting V2 candidates
> inside the V1 baseline would contradict the thing the baseline is for. Nothing
> here is committed to, scheduled, or counted in any progress figure.

---

## 1. How something gets here, and how it leaves

An idea arrives during V1 work. Three outcomes, and only three:

| Outcome | When | What happens |
|---|---|---|
| **Fix in V1** | It corrects a defect in the sealed plan — a wrong number, a false claim, a broken reference | Edit the plan, regenerate the seal, bump the baseline, record the reason. v1.0.2 and v1.0.3 were both naming and claims only |
| **Park as V2** | It adds capability, changes a requirement, or reshapes scope | Append a row below. Do not touch `planning/` |
| **Drop** | It does not survive being written down | Nothing. Not writing it down is also an answer |

The distinction that matters: **a correction keeps the finish line where it is; an addition moves it.** V1 is finishable only if the second kind is refused for the duration.

> ### The exception, recorded rather than quietly taken
>
> **Baseline v1.2.0 moved the finish line.** It added
> `14_SCIENTIFIC_INTELLIGENCE` — WP-141–147 — and ACC-52–80. By the rule above
> that is an addition, and it was taken into V1 rather than parked here.
>
> The reason is specific, and it is the only kind of reason that should do this.
> The earlier baseline tested the **platform** thoroughly and did not test the
> **epistemic path**: nothing in ACC-01–51 refused a publication sentence with no
> claim behind it, a number with no verified value under it, a producer editing
> the evaluator that scores it, a compile error recorded as a refuted hypothesis,
> or a reproduction run in the environment that produced the result. V1 could
> have completed in full, every scenario passing, without one of those being
> caught — and a baseline whose completion would not demonstrate the thing it was
> built for is not finishable in any useful sense.
>
> It was also the cheapest moment it could have happened: nothing `ACCEPTED`, one
> package `READY`, no work done against the old line.
>
> **The rule is unchanged for the next proposal.** Moving the finish line happens
> with a version bump, a tag and a stated reason — not twice, and not quietly.
> Everything below is still parked.

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
| V2-08 | A collaboration desktop or mobile cockpit as a required research surface | The `CollaborationBackend` may ship one, and a backend's user interface is not an AETHRION requirement. V1's cockpit is WP-091–095, and nothing in the sealed plan needs a second one | Constant. Adopting the backend does not commit to its UI, and `ADR-020` keeps them separable |
| V2-09 | Voice, huddles and synchronous audio collaboration | Genuinely useful for humans and unrelated to any V1 acceptance criterion. Adopting it because the backend offers it is exactly the scope creep `AGENTS.md` §7.4 refuses | Constant |
| V2-10 | Signed identity and delegation protocol as canonical attribution | Recorded as `ASM-064`, `DEFER`. Binding AETHRION's identity model to a moving draft protocol is the coupling `ADR-004` exists to prevent | Grows if a delegation model is built without it, which is why the register entry exists rather than silence |
| V2-11 | Backend approvals as a decision-collection surface | `ASM-065`, `DEFER`. The interaction surface is worth having under WP-093's queue and WP-135's signed deep links; the canonical decision stays a signed `DecisionRecord` and a backend approval never moves G8 or G9 | Constant, provided the boundary is not blurred first — which is why it is written down as deferred rather than left as an obvious next step |

---

## 3. What this register is not

It is not a roadmap, not a backlog with estimates, and not a commitment. Eleven
entries after a full brand migration, four baseline corrections and one
architecture adoption is a deliberately small number: most of what surfaced during that work was a defect
and was fixed in V1, which is the outcome this file exists to keep separate from
the other one.
