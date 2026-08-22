---
airl_id: AETHRION-SESSION-HANDOVER-2026-08-22
type: handover
status: active
owner: otonom
created_at: "2026-08-22"
content_valid_through_commit: 802738c
tags:
  - aethrion/handover
  - aethrion/execution
cssclasses:
  - aethrion-handover
---

# Session Handover — 2026-08-22

> **Read this after `AGENTS.md`, not before it.** `AGENTS.md` in the repository
> root is the operating manual — what this is, what runs, the rules, the
> hazards. This note adds only the one thing a manual cannot: *where the last
> session stopped, and why it stopped there.*
>
> Everything numeric below is also derivable. If this note and
> `docs/STATUS.md` disagree, **STATUS is right and this note is stale.**

## 1. Position in one paragraph

The repository is at **t0 of V1 execution**. V1 is the whole sealed commissioning
plan; it is complete when `00_PROGRAM/10_go_live_checklist.md`'s entry conditions
hold. One package is ready to start — **WP-001**, which authorises the programme
— one is `TECH_COMPLETE` (**WP-000**), and **none is accepted**. Nothing has run
end to end. The last session made the programme *startable*; it deliberately did
not start it.

## 2. What changed since the previous handover

Thirteen commits, in four groups.

**The visual layer was rebuilt.** Four structures had no figure at all — the
ADR-003 trust boundary, the commissioning wave map, the verification bundle and
the repository/vault topology. They exist now, and the wave figure counts its
packages from the plan directory at generation time so it cannot disagree with
the plan. Two existing figures still showed C1 and C2 as open blockers after both
were closed; corrected. Mermaid had been drawn in a Tailwind palette while every
SVG used Okabe–Ito — 38 inline diagrams now share one colour-vision-safe palette.

**The project was renamed.** It is **AETHRION — Agentic Intelligence Research
Layer**. `AIRL` survives only as a technical term and every retention is listed
with its reason in `docs/branding.md`; do not "finish the rename". The GitHub
repository, the working directory, the Obsidian project area, eight architecture
documents, nine figures and one skill directory all moved. The systemd units were
repointed and restarted.

**An external review found two stale claims in a corpus whose status page said
there were none.** Both were real. The stale-claim checker was a list of literal
regexes, and the sentence it printed was broader than anything it checked. It was
widened to derive truth from the repository; the widened version found **six**
defects, one of which was not stale but **false** — three programme documents
claimed the evidence manifest is recorded in a public transparency log, which the
interim profile explicitly disclaims. All fixed, and a regression test now plants
both defect classes and fails if either survives.

**The programme became executable.** Status used to live inside sealed files, so
starting WP-001 would have broken the seal. Progress moved to
`delivery/progress.json` outside the seal; `docs/READY.md` answers what can be
started today; `scripts/progress.py` moves packages and refuses what the plan
forbids, citing the document that forbids it.

## 3. What to do next, in order

The order matters, and it is not "start WP-001".

1. **Activate BVC-01.** The workflow exists at `deploy/bvc-01-verify.yml` and has
   never run; it needs a token with `workflow` scope. Until it runs, twelve green
   checks are a habit rather than a guarantee, and everything below can regress
   silently.
2. **Give the contract core one real consumer — finding H4.** `src/airl_framework`
   has none, and it already disagrees with the bridge about digest format
   (`ArtifactManifest` wants a bare 64-char SHA; the bridge emits
   `sha256:<hex>`). This is the first instance of "canonical schema exists, the
   running services speak another dialect", and it is cheapest to fix now.
3. **Give the read-only boundary a behavioural test — H3.** It is asserted in
   code and in prose and never exercised.
4. **Fix M9, then H1.** Zotero ingest is capped at 100 records. Adding pagination
   before M9 turns a masked truncation into active data loss.
5. **Only then** run the narrowest possible G0→G10 slice.

Rationale for the order: a vertical slice run today would produce a result nobody
could trust, because none of the controls that would make it trustworthy is
active. That is precisely the failure this system exists to prevent.

## 4. Standing constraints

- **`TECH_COMPLETE` is not `ACCEPTED`.** WP-000 has produced verified evidence
  and is still not accepted.
- **R3 work cannot be accepted here.** ADR-001 blocks it by design;
  `progress.py` refuses it and cites the record.
- **The plan is sealed.** Baseline **v1.0.5**, 221 files, tagged `v1.0.1`–`v1.0.5`.
  Re-sealing to silence a failing check is prohibited.
- **Additions are V2.** `docs/V2_CANDIDATES.md`, outside the seal.
- **`mirror_plan.py` replaces its target directory.** Pass the commissioning
  subtree, never a vault root. It refuses foreign targets now because it once
  deleted the vault.

## 5. Known-unresolved, carried forward

No package accepted · no skill behaviour-tested · no Cedar policy set authored ·
no adversarial benchmark run · no rendering toolchain installed, so the authoring
specimen has never been rendered · acceptance scenarios not tracked in the
ledger, so `COMMISSIONED` cannot yet be computed · eleven links in the Obsidian
mirror point outside the mirrored subset and do not resolve.

## 6. Where to look

| Question | File |
|---|---|
| How does this repository work? | `AGENTS.md` — **read first** |
| What is true right now? | `docs/STATUS.md` — generated |
| What can I start today? | `docs/READY.md` — generated |
| How do I run a work package? | `docs/EXECUTING_A_WORK_PACKAGE.md` |
| What happened, with evidence? | [[10 - Projects/AETHRION/implementation_log\|Implementation Log]] |
| What is the whole system? | [[10 - Projects/AETHRION/04 - Architecture/aethrion_architecture\|Architecture Reference]] — §10 first |
