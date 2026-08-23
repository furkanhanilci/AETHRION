---
title: "Findings Register"
cssclasses:
  - aethrion-review
type: review
category: review
status: WORKING
summary: "The 2026-08-21 review raised twenty-four findings."
source: "docs/FINDINGS.md"
generated: true
provenance: mirror_vault.py
tags:
  - aethrion/review
---

> [!info] Generated view
> This note is generated from `docs/FINDINGS.md` in the repository. Edit the
> canonical file and regenerate; edits made here are overwritten.

# Findings Register

| Field | Value |
|---|---|
| Document type | Register — every audit finding and its current state |
| Scope | Findings raised against this repository, from any source |
| Sibling documents | `review/` holds the frozen reports that raised them · `STATUS.md` is generated |
| Status | `WORKING` — maintained by hand; each state below was re-checked against the working tree |
| Date | 2026-08-23 |

**In one paragraph.** The 2026-08-21 review raised twenty-four findings. Eight of
them were tracked in prose across `README.md` and `AGENTS.md`; the other sixteen
had no home at all — nine survived only as a sentence in a module docstring, and
seven existed nowhere outside a frozen report. A finding whose only record is a
docstring disappears the day that file is refactored, and several of the sixteen
had in fact been fixed with nothing saying so. This register exists so that the
state of a finding is written down once, in one place, rather than inferred.

> **This file is not generated.** A finding's state is a judgement, not a
> measurement, so no script can derive it. What *is* mechanical is the evidence
> column: every "closed" row below names a command or a file you can check.

---

## 1. Open

These are live. Nothing below is scheduled; the packages named are where the
work belongs, not a commitment to a date.

| # | Finding | Where | Why it is still open |
|---|---|---|---|
| **H1** | Zotero ingest is capped at 100 records — no pagination, no `Total-Results`, no `since=` | `src/airl_bridge/zotero.py` | Fix **M9 first.** Pagination without it turns a masked truncation into active data loss |
| **H2** | A record deleted in Zotero persists in the registry and in Obsidian forever | `src/airl_bridge/database.py` | No tombstone path and the `/deleted` endpoint is never read |
| **H3** | The read-only boundary has no behavioural test | `src/airl_bridge/zotero.py` · `tests/test_api.py` | `zotero_write_enabled` is a hard-coded constant, so the artifacts that appear to verify it test `False is False`. The fix is a `MockTransport` that raises on any non-`GET`, driven through the whole sync flow |
| **H4** | The contract core has no production consumer, and contradicts the live system | `src/airl_framework/contracts.py` | Nothing in `src/airl_bridge` imports it; `ArtifactManifest` requires a bare 64-character digest while the bridge produces `sha256:<hex>`. Its only importer is a test. Binding it is WP-020 |
| **H5** | No continuous integration | `deploy/bvc-01-verify.yml` | The workflow is written and has never run: activation needs a workflow-scoped token. BVC-01 is a temporary control and does **not** close H5, which is the absence of the WP-024 CI platform |
| **M1** | Mutating endpoints are unauthenticated; no `Host` validation | `src/airl_bridge/main.py` | Loopback narrows this without closing it. Two low-cost fixes: a trusted-host middleware, and an `X-AIRL-Token` header on the mutating endpoints — a custom header alone forces a preflight and closes CSRF |
| **M6** | No transaction boundary or compensation in `sync` | `src/airl_bridge/service.py` | The ingest commits before the projection runs; if the projection fails the registry has advanced and nothing records the divergence |
| **M7** | The projection has no dry-run and does not refuse a populated directory | `src/airl_bridge/obsidian.py` | A path projected once is irreversibly taken under management. Partially narrowed by **I4** below, which stops the run when the manifest is unreadable — but adoption of a human folder is still silent |
| **M8** | SQLite connections are never closed | `src/airl_bridge/database.py` | `with self.connect()` is a *transaction* context manager; it does not close. Every request leaks one until garbage collection |
| **M9** | Silent truncation at 10,000 rows in the projection | `src/airl_bridge/service.py` | Above that the projection would not see some sources and `_remove_stale` would delete their files as stale. The 100-record ingest cap masks this today |
| **L2** | `airl_id` is a 64-bit truncated hash with no collision handling | `src/airl_bridge/zotero.py` | Acceptable at 33 sources; it is not a property to discover at scale |
| **L4** | No test coverage of the security and error paths | `tests/test_api.py` | None of the three `POST` endpoints, the 503 and 422 handlers, the loopback refusal, the path-traversal refusal or `library_type` validation is exercised — which contradicts the plan's own Definition of Done |

## 2. Closed

| # | Finding | Closed by | Check it |
|---|---|---|---|
| **C1** | Evidence-chain bootstrap deadlock: no package could become `ACCEPTED` | WP-000 — the interim evidence policy, implemented and issued | `uv run python scripts/evidence_manifest.py verify --manifest delivery/WP-000/evidence.dsse.json --tamper-demo` |
| **C2** | The plan assumed 73 owners and 114 verifiers; the organisation is one person | ADR-001 — R1 solo · R2 under a declared partial profile · **R3 `BLOCKED`**, declared rather than waived | `docs/architecture/ADR-001_solo_operator_independence.md` |
| **C3** | WP-022 was declared `TECH_COMPLETE` with its deliverable absent | The claim was withdrawn; only WP-000 is `TECH_COMPLETE` | `python3 scripts/progress.py show WP-022` |
| **M2** | `mcp_smoke.py` asserted nothing and exited 0 under all conditions | Rewritten: asserts the exact five-tool set, exits 1 with the Bridge down | `uv run python scripts/mcp_smoke.py` |
| **M3** | `acceptance_v0.py` depended on the operator's personal library | Rewritten as 11 data-independent structural checks | `uv run python scripts/acceptance_v0.py` |
| **M4** | The plan lived in four physical copies with contradictory authority | One canonical tree under `planning/commissioning/`, hash-sealed; the vault copy is a generated mirror | `(cd planning/commissioning && sha256sum -c 00_PROGRAM/SHA256SUMS.txt)` |
| **M5** | WP↔ACC traceability was inconsistent in 39 of 40 cases | References now resolve in both directions and are checked | `python3 scripts/validate_commissioning_plan.py` |
| **M10** | Documentation drift after renames — prior-project names leaked into the unit descriptions | Units reinstalled | `grep -i silbo deploy/` returns nothing |
| **M11** | The canonical plan tree was not under version control | It is: 222 tracked files | `git ls-files planning/commissioning \| wc -l` |
| **L1** | `.env` and `.env.example` were byte-identical; the example carried real paths | The example carries `<VAULT_ABSOLUTE_PATH>`; `.env` is git-ignored | `grep VAULT_ABSOLUTE_PATH .env.example` |
| **L3** | Category folder names mixed English and Turkish | All twelve are English | `src/airl_bridge/catalog.py` |
| **L5** | A fake `.git`, an empty `.codex` and an empty `.agents` at the root | Removed | `ls -d .codex .agents` fails |

---

## 3. Findings raised by the 2026-08-22 repository inspection

A separate namespace, because the 2026-08-21 audit is frozen evidence and its
`C`/`H`/`M`/`L` identifiers belong to it. All twelve were fixed in the same pass
that raised them; each names the test or check that would catch a regression.

| # | Finding | Fixed by | Regression guard |
|---|---|---|---|
| **I1** | `docs/STATUS.md` is a signed subject of the WP-000 attestation and carried a timestamp refreshed on every run, so the session-start command invalidated the session-end verification **deterministically** — teaching the operator to re-sign without reading | `write_status.py` rewrites the page only when a check result changes | Run `write_status.py` twice; the second prints `unchanged` |
| **I2** | An `unchanged` ingest still wrote `synced_at`, which the projection renders as each note's `generated_at` — so a run reporting `unchanged: 33` rewrote 36 vault files every 30 minutes | `database.upsert_sources` no longer writes an unchanged record; only a moved upstream version is reconciled | `tests/test_database.py::test_unchanged_source_is_not_rewritten` |
| **I3** | The two dashboards were generated *outside* the projection manifest — files the projector creates and can never clean up | Dashboards are written before the manifest is sealed and are recorded in it | `tests/test_obsidian.py::test_dashboards_are_recorded_in_the_manifest` |
| **I4** | An unreadable manifest was swallowed (`return 0`) and then overwritten, permanently orphaning every file it listed | `_remove_stale` raises `ProjectionError` instead | `tests/test_obsidian.py::test_unreadable_manifest_refuses_rather_than_orphaning_files` |
| **I5** | `pydantic` was imported directly by `airl_bridge.models` and declared nowhere — it arrived only transitively through FastAPI | Declared in `pyproject.toml` | — |
| **I6** | Six counts were stale across four documents while `check_doc_consistency.py` reported that documents agree: the test count in nine places, the bundle size in three, the attestation's subject count, and the figure count in the runbook. Every one was a number nobody had written a rule for | Fifteen rules added; `tests`, `bundle_checks` and `attestation_subjects` are now derived | `python3 scripts/check_doc_consistency.py` |
| **I8** | `mirror_plan.py` replaced its target directory wholesale. Beyond the recorded data-loss hazard, it broke a running Obsidian's file watcher — the editor kept showing a stale index of files that no longer existed at those inodes, so a reader could not see their own updates | Both mirrors write **differentially**: only changed files, removing only what is no longer generated | `tests/test_mirrors.py` |
| **I7** | `docs/figures/aethrion_verification.svg` drew ten rows for a twelve-check bundle and named `seal_commissioning_plan.py`, a script that does not exist | `fig_verification.py` derives its rows from `write_status.CHECKS` and **raises** if the bundle grows a check it has no prose for | `python3 scripts/make_figures.py --check` |
| **I9** | The vault mirror carried every leaf document and none of the folder maps. `docs/architecture/README.md` indexes the twenty architecture notes, `docs/review/README.md` the reviews, `README.md` the repository — eighteen such documents, none projected. A reader who opened `04 - Architecture/` in Obsidian got an alphabetical list where the repository has a structure | The eighteen are mirrored, each landing in the vault folder it indexes, and linked from that folder's own index note | `python3 scripts/check_vault.py` reports **no orphan pages** |
| **I10** | Two of those eighteen targets were the names of **hand-authored** vault notes, and the mirror overwrote both. They were recoverable only because `vault_baseline/` is tracked, which is luck rather than a control | The mirrored pages were renamed, and the mirror now **refuses** to write over any page whose frontmatter says `generated: false` | `tests/test_mirrors.py::test_vault_mirror_refuses_to_overwrite_a_hand_authored_note` |
| **I11** | `watch_mirror.py` held a hand-written list of four watched sources. The mirror then read eighteen more — `AGENTS.md`, `scripts/README.md`, `src/*/README.md` — so editing the operating manual left the vault showing the previous one, with nothing reporting a difference | `WATCHED` is derived from the mirror's own source map | `tests/test_mirrors.py::test_the_watcher_watches_every_source_the_mirror_reads` |
| **I12** | `check_doc_consistency.py` read spelled-out numbers from a hand-written table that reached *forty-five*. The suite grew to forty-six, the document was updated correctly, and the checker reported the **old** number — failing a document for being right | The table is generated for one to ninety-nine | `python3 scripts/check_doc_consistency.py` |

---

## 4. Findings raised by the 2026-08-23 baseline v1.2.0 and v1.3.0 work

Four defects surfaced while running the checks the verification bundle does **not**
cover, and they are recorded in their own namespace for the same reason the
08-22 inspection is: the earlier reports are frozen evidence and their identifiers
belong to them.

| # | Finding | Fixed by | Regression guard |
|---|---|---|---|
| **J1** | `acceptance_v0.py`'s `manifest_matches_registry_count` compared the **whole** projection manifest against the registry's source count. Finding **I3** had deliberately moved the two dashboards *inside* the manifest — a generated file outside it is one the projector can never clean up again — so from the moment I3 landed the check failed by exactly the number of dashboards, on a correct system. It reported `manifest=35 registry=33` and the defect was in the check | The dashboards and the source notes are counted separately; the manifest check now compares source notes to the registry and reports the dashboard count beside it | `uv run python scripts/acceptance_v0.py` → `"result": "accepted"`, 11 PASS, 0 FAIL |

| **J2** | `check_upstream_lineage.py`'s licence rule matched `licence.upper() == "UNVERIFIED"` **exactly**, so an entry reading `"UNVERIFIED — repository licence not confirmed on 2026-08-23"` — strictly more informative — slipped past it in silence. The same rule was also wrong in principle: it forbade every assimilation type except `DEFER` and `REJECT`, which contradicts `ADR-004`, where reimplementing a published mechanism creates no licence obligation and an unverified licence is a *reason* to reimplement rather than a reason to stop | The rule now matches a prefix and forbids only what an unverified licence actually forbids — `DIRECT_ADAPT`. Three regression tests: the rule fires on a direct adaptation, does **not** fire on a reimplementation, and is not defeated by a longer string | `uv run pytest tests/test_upstream_lineage.py` — 14 tests |

> **Both J1 and J2 are the same failure in different clothes.** A check that is
> narrower than the sentence it prints. J1 compared the wrong two numbers and
> reported a defect that was in the check; J2 matched the wrong string and
> reported clean because nothing it could see was wrong. The register's own
> `--self-test` did not catch J2 either, because the injection it used happened
> to write the bare word the rule matched — **a control tested only with the
> input it was written for is a control tested against itself.**

> **Why this was not caught earlier.** `acceptance_v0.py` needs a live Bridge and
> the operator's Zotero library, so it is one of the two checks the bundle
> deliberately excludes — `AGENTS.md` §5 and `docs/OPERATIONS.md` both say so.
> A check outside the bundle is a check that runs when somebody remembers, and
> this one had been silently red across at least one release of fixes.
>
> The general lesson is the one this register keeps re-learning: **a check that
> nothing forces to run will eventually be a check nobody has run.** It is
> recorded here rather than fixed and forgotten.

| **J3** | The final-audit list in the reliability delta asks a human to grep for eight wordings that contradict a decision record. Written that way it is not a control at all: **every one of the eight phrases already appears in this repository, every time inside a sentence that forbids it.** A hand grep returns a wall of correct prose, and the one affirmative use is somewhere in the middle of it. A checklist item that produces a hundred false positives is a checklist item that gets ticked without being read | The list is implemented as a third rule family in `check_stale_claims.py` with two guards at different scopes — a paragraph-level prohibition marker and a local negation check on the thirty characters before the match — and every rule carries a specimen that must trip it **and** one that must not | `python3 scripts/check_stale_claims.py --self-test` · `uv run pytest tests/test_architectural_regressions.py` — 10 tests |

| **J4** | Two rules in that new family were **silent on the sentences written to trip them**, and the self-test found both before they ever ran on the corpus: the fully-connected rule read left-to-right only, and English does not; and the timeout rule was suppressed by a paragraph guard containing the bare word `not`, so *"if the reviewer does **not** respond the gate auto-approves"* read as a refusal. The corpus scan then produced four more false positives — `Expiry \| WP-024 acceptance` in a decision-record table, the heading `Timeout escalation path with no approval branch` in nine packages, and two scenarios naming a derived store and the canonical records in one breath | The bare `not` and `fails` were removed from the prohibition guard, which now carries only idioms that do the refusing; a local-negation guard was added for text with no sentence around it; and both loose patterns were tightened to require an actual copula or an actual causal verb | The four false positives are pinned as tests in `tests/test_architectural_regressions.py` |

> **J3 and J4 are the pair, and the second is the more useful one.** J3 says a
> control expressed as a checklist is not a control. J4 says the control that
> replaces it does not work the first time either — and the only reason that is
> known is that the rules were required to demonstrate themselves before being
> trusted. **Two of eight rules were dead on arrival.** A regression checker
> shipped without a self-test would have printed the same reassuring line as one
> that worked, and this repository would have recorded eight controls where it
> had six.
>
> It is the same sentence as J2, one layer up: *a control tested only with the
> input it was written for is a control tested against itself.* The difference
> here is that the negative specimen was mandatory too — because for this rule
> family, false positives are not an annoyance, they are the failure mode. A
> checker that flags every correct paragraph gets switched off, and a switched-off
> checker and an absent one are the same thing.

---

## 5. Findings from the 2026-08-23 integration-consistency remediation

An external audit package attacked the seam between the architecture and the
machinery that enforces it, which is where the defects from the v1.2.0 and
v1.3.0 expansions had collected. Its findings are adjudicated one by one in
[`review/2026-08-23_integration_remediation_dispositions.md`](review/2026-08-23_integration_remediation_dispositions.md).
Recorded here are the ones that are defects *in this repository's own controls*
rather than in the plan they check.

| # | Finding | Fixed by | Regression guard |
|---|---|---|---|
| **K1** | **A dependency graph can be acyclic and impossible to execute, and nothing said so.** Two packages required before go-live depended on Day-2 packages that exist only after it. The plan validator did have a phase rule — but it read the *scenario document* while the violating edge lived in the *matrix*, and it only looked at scenario→package edges while both real deadlocks are package→package | `check_programme_graph.py`, seven rules over package, scenario and milestone nodes, with shortest-path diagnostics | `--self-test`, six mutations · `tests/test_programme_graph.py` |
| **K2** | **A deterministic generator reproduced a false claim exactly as faithfully as a true one.** `aethrion_waves.svg` rendered "141 work-package documents" against a registry of 160 for two baselines, and `aethrion_topology.svg` said "221 planning files, baseline v1.0.5" against a seal of 631. Both passed the containment check and the drift check — the latter compares a figure to the generator that drew it, and the generator was the thing that was wrong | `check_figure_semantics.py`, reading the rendered SVG and comparing to the registries by a path that does not pass through any generator | four registry mutations · `tests/test_figure_and_hygiene_checks.py` |
| **K3** | **One relation, two owners, disagreeing on 98 of 120 scenarios.** The WP↔ACC binding was written in the scenario documents *and* in a matrix column. Among the disagreements: eleven `PRE_GO_LIVE` scenarios the column bound to Day-2 packages, invisible because the validator read the document and the generator read the column. This is the repository's own finding **M5**, open since the first audit | the column was **deleted**. `programme_model` derives the reverse from the scenario documents, so there is no second representation left to drift | `test_the_wp_acc_binding_has_exactly_one_owner` |
| **K4** | **Two aggregators enumerated two scenarios where their own cards said the set was derived.** `WP-115`'s card: *"the set is derived, never enumerated here, because an enumeration drifts the moment a scenario is added."* 185 lines below, inside the generated block an independent verifier actually works from, sat `ACC-01` and `ACC-40` | a `scenario_selector` grammar, with the required aggregators **declared** in `programme_metadata.json` | `test_removing_an_aggregate_selector_is_a_failure_not_a_silence` |

> **K4's second half is the one worth keeping.** The first version of the rule
> iterated over packages that *had* a selector — so deleting `WP-115`'s selector
> made the check pass in silence and restored exactly the enumeration it was
> written to prevent. **A check anchored on the thing it checks can be switched
> off by deleting that thing.** The self-test found it, because the mutation
> "remove the selector" was on the list before the rule was written.
>
> That happened four times while building `check_programme_graph.py`: two rules
> could not fire at all, one crashed before its own diagnostic printed, and one
> was disabled by the mutation it was meant to catch. And twice more in
> `check_figure_semantics.py`, where the first bijection rule invented a naming
> convention — `fig_X.py → aethrion_X.svg` — and reported two findings against a
> repository that had no defect. **A checker that invents a rule and then
> enforces it is worse than none, because its findings look like the real ones.**

---

## 6. What this register does not do

It does not rank, schedule or assign. It records what is known to be wrong and
whether it still is. Two limits are worth stating plainly:

- **A closed finding is closed against the check named beside it**, not in
  general. `M2` is closed because `mcp_smoke.py` now asserts and can fail — not
  because the MCP boundary is proven correct.
- **The list is only as complete as the reviews that produced it.** An external
  reader once found two stale claims in a corpus whose status page reported
  none, and these inspections found eleven more. Assume the same is possible now.
