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
| **H5** | No continuous integration | `deploy/bvc-01-verify.yml` | The workflow is written, covers the whole automatable bundle including every self-test, and **has never run**: activating it means copying it to `.github/workflows/` with a workflow-scoped token, which is an operator action this session cannot perform. BVC-01 is a temporary control and does **not** close H5, which is the absence of the WP-024 CI platform |

> **H5's blocker is now tested rather than assumed.** Activation was attempted on
> 2026-08-23 — the workflow copied to `.github/workflows/verify.yml`, committed
> and pushed. GitHub refused:
>
> ```
> ! [remote rejected] main -> main (refusing to allow an OAuth App to create
>   or update workflow `.github/workflows/verify.yml` without `workflow` scope)
> ```
>
> The commit was reverted. That refusal is better documentation than the previous
> note, which asserted the same thing without having tried it — and this register
> spent an entire baseline on the principle that a control nobody has watched
> refuse is not evidence. The same standard applies to a blocker.

> **H5 is the only one left, and it is the one that cannot be closed from
> inside the repository.** Every other finding in this section was a defect in
> code or in test coverage. This one is a permission: `gh auth refresh -h
> github.com -s workflow`, then copy the file. Until then the eleven closures
> below are proven by a suite somebody has to remember to run, which is the
> weaker half of the same claim.

## 2. Closed

### Closed on 2026-08-23 — the bridge findings

Eleven of the twelve open findings closed together, because most of them were
one property looked at from different angles: **the system did things it could
not report on.** A partial fetch reported `SUCCEEDED`; a deleted source lived on
forever; a projection that failed left a registry that had moved; a read-only
boundary was asserted by a constant.

| # | Finding | Fixed by | Regression guard |
|---|---|---|---|
| **H1** | Zotero ingest capped at 100 records — no pagination, no `Total-Results`, no completeness signal | `fetch_top_items` paginates and returns `(items, **complete**)`. `Total-Results` is a cross-check where the server sends it; termination is decided by a short page, because a client that *requires* a header stops working the day the header stops arriving | `test_pagination_walks_past_the_first_hundred` · `test_an_exact_multiple_of_the_page_size_terminates` · `test_a_total_results_disagreement_refuses_rather_than_reconciling` |
| **H2** | A record deleted in Zotero persisted in the registry and in Obsidian forever | `reconcile_deletions` writes a **tombstone**, not a row deletion. A registry is the system of record for source identity, and an identity that silently vanishes cannot afterwards be told apart from one that never existed — which is the question an audit asks about a citation that no longer resolves | `test_a_source_absent_upstream_is_withdrawn_not_deleted` · `test_a_withdrawn_source_that_returns_keeps_its_identity` |
| **H3** | The read-only boundary had no behavioural test | A transport that **raises** on any method other than `GET`, driven through the whole ingest — and a test proving that transport can raise. `zotero_write_enabled` is still a constant and is no longer the evidence for anything | `test_a_full_sync_issues_only_gets` · `test_the_read_only_transport_can_actually_fail` |
| **H4** | The contract core had no production consumer and contradicted the live system | `airl_bridge.zotero` mints every `content_hash` through `airl_framework.contracts.content_digest`. The reconciliation went the **bridge's** way: the prefixed `sha256:<hex>` form names its own algorithm, where a bare digest is 64 characters of ambiguity. Bare digests are normalised on read so nothing already written became unreadable | `test_content_hash_is_minted_through_the_contract_core` · `tests/test_contracts.py` |
| **M1** | Mutating endpoints unauthenticated; no `Host` validation | **Two** controls, because it was two vulnerabilities. `X-AIRL-Token` on the writes — a custom header is off the CORS safelist, so a cross-site page cannot send it without a preflight it cannot satisfy. A `Host` check on **every** request, including reads, because DNS rebinding makes `GET /v1/sources` same-origin and a token on the writes does nothing about that | `test_a_mutating_endpoint_refuses_without_a_token` · `test_an_unrecognised_host_is_rejected` · `test_an_unconfigured_token_refuses_rather_than_opening` |
| **M6** | No transaction boundary or compensation in `sync` | The ordering was never the defect — there is no transaction spanning SQLite and a directory of Markdown files. The defect was that a failing projection left the registry advanced and *nothing said so*. `sync` records a `DIVERGED` run and returns a result a caller cannot misread | `tests/test_service_divergence.py`, including the negative control that a healthy sync records nothing |
| **M7** | The projection had no dry-run and adopted a populated directory silently | It refuses a directory holding files it did not create and carrying no manifest, and `dry_run=True` reports what would change without changing it. The timing is what made this dangerous: a hand-written folder was destroyed on the **second** run, so the first one looked like it worked | `test_a_populated_unmanaged_directory_is_refused` · `test_a_dry_run_writes_nothing_and_reports_what_would_change` |
| **M8** | SQLite connections never closed | A `session()` context manager that commits, rolls back **and** closes. `with sqlite3.connect(...)` reads like a resource manager and is not one | `test_a_session_closes_its_connection` · `test_a_failing_session_rolls_back_and_still_closes` |
| **M9** | Silent truncation at 10,000 rows in the projection | `list_sources(limit=None)`. The cap was not merely a ceiling: `_remove_stale` deletes any projected file whose source is absent from the list it was handed, so a truncated read became **deletion** of everything past the cut | `test_a_partial_walk_does_not_reconcile_deletions` |
| **L2** | `airl_id` is a 64-bit truncated hash with no collision handling | A collision now raises `SourceIdentityCollision` naming both bindings. The width is unchanged and that is deliberate — the point was never 64 bits, it was that a collision must be **detected** rather than discovered later as two merged bibliographies | `test_an_airl_id_collision_is_refused_rather_than_merged` |
| **L4** | No test coverage of the security and error paths | Every mechanism that exists to refuse something is exercised: both M1 controls, the 503 and 422 handlers, the 404, the loopback refusal, the path-traversal refusal and `library_type` validation. The plan's Definition of Done requires "security, data and policy negative tests have passed", and it was being satisfied by nothing at all | `tests/test_api.py`, sixteen tests |

> **Two of these were fixed in the order the register demanded, and the order
> mattered.** H1 said *"fix M9 first"* — pagination without it turns a masked
> truncation into active data loss, because a complete walk authorises the
> deletion reconciliation and a reconciliation against a partial library
> withdraws everything it did not reach. `test_a_partial_walk_does_not_reconcile_deletions`
> is that coupling written down as a test rather than as a warning in a
> docstring.
>
> **And one defect was introduced while fixing another.** The dry run parsed the
> projection manifest itself and read the wrong key — `files` instead of
> `generated_files` — so it reported zero deletions forever. A planner that
> cannot see what a real run would delete is worse than no planner, because it
> is reassuring. The test caught it, and the parse is now shared with
> `_remove_stale` rather than duplicated: the same one-owner rule that closed
> **K3** one baseline earlier, applied two hundred lines lower down.



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

## 6. Finding from the 2026-08-23 skill baseline work

| # | Finding | Fixed by | Regression guard |
|---|---|---|---|
| **L6** | **Seventeen of fifty-two skills were reachable by no chain of references from the router.** `validate_skills.py` proved all 52 parse and carry their metadata, and every one of the seventeen passed it. A skill nobody can be routed to never loads, so whatever it says is unreachable rather than merely untested — and the check that appeared to cover the registry was measuring a different property | The router names every skill, and `check_skill_baseline.py` R1 fails when one becomes unreachable — transitively, so a skill reached only through another still counts | `scripts/check_skill_baseline.py --self-test` · `tests/test_skill_baseline.py` — 9 tests |
| **L7** | **The staged CI workflow ran thirteen of the bundle's twenty checks**, and nothing compared the two. `fig_verification.py` has refused since finding **I7** to draw a figure that under-reports the bundle; the same rule was never applied to the workflow. Activating it would have produced a green badge covering two thirds of what it appeared to cover | The workflow runs every automatable check; `check_ci_covers_the_bundle` fails when one is absent from both the workflow and the declared-manual list, so adding a check to the bundle now forces a decision — automate it, or name the resource a runner lacks | `tests/test_architectural_regressions.py` — three tests, including one proving a script named only in a **comment** does not count as covered |

> **L7's first version had the defect it was written to catch.** The rule
> matched the whole workflow file, so `scripts/check_vault.py` — which appears
> *only* in the comment block listing what CI does **not** run — counted as
> covered. The comment satisfied the check that the comment exists to explain.
> It now reads `run:` lines alone, and a test pins that specific false negative.

> **L6's consequence was not abstract, and it is the part worth keeping.** Two of
> the seventeen were the *scientific* halves of pairs `ADR-012` §2 says must
> never be substituted — `dispatching-parallel-analysts` and
> `adversarial-reviewing` — while their engineering counterparts sat in the
> router table. So a task needing genuinely independent analyses routed to
> `dispatching-parallel-agents`, which decomposes work that has one right answer.
>
> **That is worse than both halves being missing.** With neither routable the
> task stalls and somebody looks. With one routable it proceeds, plausibly, into
> the wrong discipline — and produces a merged answer where the method required a
> spread. `ADR-012` was written to prevent exactly that substitution, and it was
> being reached not through a bad judgement but through the correct option being
> absent from the table.
>
> The general shape: **a conformance check and a reachability check are different
> claims, and the first reads like the second.** "All 52 skills conform" was true
> the whole time.

---

## 7. Findings from the 2026-08-23 visual completion pass

| # | Finding | Fixed by | Regression guard |
|---|---|---|---|
| **L8** | **`check_figures.py` could not see a paragraph that had fallen through the bottom of its own box.** Text below its box has no enclosing box either, so the code treated it as free-standing and `continue`d. Three captions were drawn across the border of the box they belong to, in a corpus reporting zero overflows | a `box bottom` rule requiring **paragraph continuity** — a sibling line one line-height above, inside the box — because the naive version fired on every zebra-striped table | `tests/test_figure_and_hygiene_checks.py`; the rule fires on a planted straddle and stays silent on a striped row |
| **L9** | **Nothing compared two strings to each other.** Seven collisions were live: a section heading under a boundary label, an edge caption on the node title it pointed at, a command column running into the prose beside it | a `collision` rule on near-identical baselines with overlapping x-ranges | the seven were fixed and the rule now runs on every figure |
| **L10** | **`text_width` had no monospace mode**, so a monospace column measured with proportional metrics came out too narrow and `must_be_independent_from:` overwrote its own value | `text_width(..., mono=True)`; every glyph in the mono stack advances the same | the roles figure regenerates clean |
| **L11** | **A count typed into a figure.** `aethrion_assurance.svg` said *"four questions"* beside a list of five — in the figure whose subject is that one word was carrying two jobs | both numbers derived from the list | `check_figure_semantics.py` compares figure claims to registries; this one is now derived at generation |
| **L12** | **A status overclaim inside a figure.** `aethrion_roles.svg` said the RoleBinding constraint is *"now enforced instead of argued about"*. The engine that would admit or refuse a binding is WP-013 and is not built | the sentence says `SPECIFIED`, and names the package that would build it | — |

> **The pattern under most of them is one line of code appearing twice.** A box
> height and the offset of whatever follows it were two independent literals.
> Grow the box to hold a paragraph that got longer, and the heading below it is
> now underneath it — and nothing notices, because both numbers are individually
> reasonable. Six figures had this; they now derive the second from the first.
>
> **And the finding behind the findings: none of this was reachable by
> measurement.** Every one was found by rendering the SVG and looking at it.
> `check_figures.py` measures strings against boxes and cannot see a connector
> drawn through a heading, a panel placed over a label, a sequence held together
> by its own numbering, or a column of dead space. `scripts/render_figures.py`
> makes that pass a command, and is deliberately **not** in the verification
> bundle — a row reading "figures rendered" would be read as "figures reviewed",
> and only one of those happened.

---

## 8. What this register does not do

It does not rank, schedule or assign. It records what is known to be wrong and
whether it still is. Two limits are worth stating plainly:

- **A closed finding is closed against the check named beside it**, not in
  general. `M2` is closed because `mcp_smoke.py` now asserts and can fail — not
  because the MCP boundary is proven correct.
- **The list is only as complete as the reviews that produced it.** An external
  reader once found two stale claims in a corpus whose status page reported
  none, and these inspections found eleven more. Assume the same is possible now.
