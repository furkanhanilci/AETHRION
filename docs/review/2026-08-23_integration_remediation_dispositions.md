# Integration-Consistency Remediation — Finding Dispositions

| Field | Value |
|---|---|
| Document type | Evidence — a dated disposition record, frozen once written |
| Source package | `AETHRION_V1_3X_INTEGRATION_REMEDIATION`, 110 files, seal verified 110/110 |
| Scope | Every finding in that package, adjudicated against the repository |
| Baseline before | `v1.3.0` |
| Baseline after | `v1.3.1` |
| Date | 2026-08-23 |

**In one paragraph.** The package's own `README.md` refuses "could not reproduce"
as a disposition unless the current file, generator, registry and test evidence
are cited. This document is that citation, one row per finding. Every P0 and P1
claim was verified computationally rather than by reading, because the defects
are of a kind reading does not catch — a dependency graph that is acyclic and
unexecutable, a figure that is deterministic and false.

## How each finding was adjudicated

Four dispositions, from the package's `README.md`:

- **`CONFIRMED_AND_FIXED`** — reproduced here, repaired, with a regression fixture.
- **`ALREADY_FIXED_EQUIVALENTLY`** — the repository had solved it another way.
- **`SUPERSEDED_BY_NEWER_CANONICAL_DESIGN`** — the finding is right and its
  proposed remedy is not the one this architecture takes.
- **`NOT_APPLICABLE_WITH_EVIDENCE`** — reproduced as absent, with the check that
  says so.

## P0 — blocks baseline promotion

| # | Finding | Verified as | Disposition | Canonical source after fix | Regression fixture |
|---|---|---|---|---|---|
| 1 | Aggregate commissioning scenario binding is a stale enumeration | `WP-115`/`WP-119`/`WP-120` each bound `ACC-01;ACC-40` while their cards said "derived, never enumerated". 2 scenarios where the rule means **118** | `CONFIRMED_AND_FIXED` | `scenario_selector` column + `programme_metadata.json` → `aggregate_packages.required` | `test_removing_an_aggregate_selector_is_a_failure_not_a_silence`, `test_adding_a_pre_go_live_scenario_reaches_the_aggregators_with_no_package_edit` |
| 2 | Pre-go-live / Day-2 dependency deadlocks | BFS over all 160 packages found **exactly two**, exactly the two named: `WP-152 → WP-128`, `WP-155 → WP-126` | `CONFIRMED_AND_FIXED` | `scheduling_phase` column; rule `V-PHASE-001` | `test_a_pre_go_live_package_may_not_depend_on_a_day2_package` |
| 3 | Benchmark firewall ordering becomes cyclic once §1 is fixed | Confirmed **and understated**. Applying the selector produced **nine** cycles, not one — `WP-119`, `WP-120`, `WP-124`, `WP-126`, `WP-127`, `WP-129`, `WP-152`, `WP-155` and the predicted `WP-158` | `CONFIRMED_AND_FIXED` | combined graph, rule `V-GRAPH-001` | `test_the_benchmark_firewall_may_not_depend_on_the_regression_that_aggregates_it` |

**On finding 3.** The audit found the cycle it went looking for and stopped. The
other eight are the same defect in packages it did not check, and eight of the
nine are only reachable *after* finding 1 is fixed — which is the argument for
fixing them in one baseline rather than two.

## P1 — architecture can be misread, or a validator certifies the wrong invariant

| # | Finding | Verified as | Disposition | Canonical source after fix | Regression fixture |
|---|---|---|---|---|---|
| 4 | `WP-154` sequenced after the `WP-107` slice it governs | Confirmed: `WP-154 deps = WP-023;WP-047;WP-081;WP-107` | `CONFIRMED_AND_FIXED` | direction reversed; `WP-107` now depends on `WP-154` | covered by `V-GRAPH-001` and the plan validator's acyclicity check |
| 5 | Wave generator encodes the old `WP-000–140` universe | Confirmed and **live**: the rendered SVG said *"141 work-package documents in eleven waves"* against a registry of 160. `WP-141–159` were in no wave at all — `expand_packages.wave_of` returned the string `"unassigned"` for all nineteen | `CONFIRMED_AND_FIXED` | `wave_id` column + wave registry; both private wave tables deleted | `test_a_grown_package_registry_is_detected`, `test_the_wave_bars_sum_to_the_registry` |
| 6 | Lifecycle figure's G5 semantics too coarse | Confirmed: one row labelled `NO MODEL`, which reads as banning the model-driven discovery `WP-144` performs exactly there | `CONFIRMED_AND_FIXED` | G5 drawn as `G5·D` / `G5·E` — two lanes, no new gate | `check_no_model_consistency` compares figure and inventory |
| 7 | Scope matrix retains stale counts and backend-specific labels | Confirmed: *"The fifty-one acceptance scenarios"* at a registry of 120; `SPIFFE / Vault / OPA / egress` | `CONFIRMED_AND_FIXED` | registry-neutral wording; `PolicyDecision` contract + selected backend | dynamic-fact rules; `check_matrix_references` |
| 8 | Stale-claim checker is phrase-oriented, not fact-derived | **Half already true.** `check_doc_consistency.py` derives twelve facts. It enforces them only where a rule names document *and* pattern, so seven live surfaces carried "141 packages"/"fifty-one scenarios" and passed | `CONFIRMED_AND_FIXED` | fourth rule family: 4 dynamic facts over 12 live surfaces | the family fires on a stale count and stays silent on a dated historical one |
| 9 | Plan validator's DAG check insufficiently bound to phase | **Right conclusion, wrong reason.** A phase rule existed at `validate_commissioning_plan.py:151` — but only on the **scenario→package** axis, with Day-2 hard-coded as `range(122,131)`. Both real deadlocks are **package→package** edges it structurally cannot see | `CONFIRMED_AND_FIXED` | `check_programme_graph.py`, seven rules over three node classes | `--self-test`, six mutations |
| 10 | Efficiency thresholds have no release-specific freeze artifact | Confirmed absent | `CONFIRMED_AND_FIXED` (`SPECIFIED`) | `EfficiencyQualificationProfile` in `WP-149` and the schema index; ACC-086 binds it | ACC-086 criteria; no code exists |

## P2 — hygiene and metadata

| # | Finding | Verified as | Disposition | Note |
|---|---|---|---|---|
| 11 | Duplicate headings in generated/expanded WP cards | Confirmed: **19** documents, and they are exactly `WP-141–159` — the ones authored at v1.2.0 and v1.3.0, where a hand-written heading met the generator's own | `CONFIRMED_AND_FIXED` | This was my defect, not an inherited one |
| 12 | Broken or renamed figure-skill links | **0 broken relative links** in 748 governed documents; `producing-figures` exists. The 66 hits in an initial scan were `zotero://` URIs inside `data/projection-backups/` | `NOT_APPLICABLE_WITH_EVIDENCE` | `check_document_hygiene.py` now proves it on every run |
| 13 | Baseline and version labels readable inconsistently | Partly confirmed: `progress.json` was unambiguous, but no machine-readable baseline object existed and `09_change_and_configuration_control.md` had said "the current baseline is v1.1.0" two baselines late | `CONFIRMED_AND_FIXED` | `programme_metadata.json` owns it; `check_baseline_agreement` compares the ledger to it |
| 14 | Historical "51 scenarios"/"141 packages" language in dynamic surfaces | Confirmed in **7** surfaces | `CONFIRMED_AND_FIXED` | see finding 8 |

## Four defects the package does not name

Found while verifying its findings. Recorded separately because a coverage claim
that quietly absorbs extra findings into existing rows is not a coverage claim.

| # | Defect | Why it was invisible |
|---|---|---|
| A | **11 `PRE_GO_LIVE` scenarios were bound in the matrix to Day-2 packages** — ACC-07, 08, 09, 10, 11, 17, 27, 29, 36, 38, 40 | The validator's phase rule read *"Related packages"* from the **scenario document**; the binding that violated it lived in the **matrix column**. One rule, two sources, and it was reading the compliant one |
| B | **The WP↔ACC relation had two owners that disagreed on 98 of 120 scenarios**, and the matrix bound 91 of 120 at all | This is the repository's own finding **M5**, recorded in `00_PROGRAM/06` and never closed. It is the *mechanism* behind P0-1, which the package describes as a generator problem. It is not — it is an ownership problem, exactly as the package's own `03_CANONICAL_TRUTH_MODEL.md` argues |
| C | **`aethrion_topology.svg` claimed "221 planning files, byte-identical to baseline v1.0.5"** — the seal covers 631 at v1.3.1 | Same class as finding 5, in a figure the package did not check. Both are now compared to the registries from the rendered SVG |
| D | **`docs/figures/README.md` said "three gates admit no model at all"** while the lifecycle figure hatched two | A figure's inventory entry is prose and the figure is an SVG. Nothing compared them |

## Two places this repair departs from the package's proposal

Both are `SUPERSEDED_BY_NEWER_CANONICAL_DESIGN` in the narrow sense: the finding
is accepted, the remedy differs, and the reason is this architecture's own rule.

**The scenario column was deleted, not synchronised.** `patch_specs/02` proposes
`explicit_scenarios` alongside `scenario_selector` as package fields. Keeping an
`explicit_scenarios` column would preserve two representations of one relation
and add a drift check between them — and `ADR-014`'s answer to two
representations of one fact is not a better check. The scenario document's
`Related packages` row is now the only place the binding is written, and
`programme_model.load()` derives the reverse.

**`WP-119` was left selector-free, deliberately.** `04_P0` asks that this be
decided rather than inferred. It is the cutover **rehearsal**, and a rehearsal
that must first pass the entire commissioning suite is not a rehearsal — it is
the suite. It consumes `WP-115`'s dossier through an ordinary hard dependency.
The decision and its reason are recorded in `programme_metadata.json` under
`aggregate_packages`, so a later reader finds a decision rather than an omission.

## What the repair does not establish

The package's `28_CLAUDE_MASTER_IMPLEMENTATION_INSTRUCTION.md` ends by forbidding
one sentence, and it is the right one to forbid: *do not state that AETHRION is
commissioned merely because the remediation specification is internally
consistent.*

So, in the vocabulary that instruction requires:

| Maturity | What is at this level after v1.3.1 |
|---|---|
| `SPECIFIED` | Everything in workstreams 14 and 15. The `EfficiencyQualificationProfile`. All eighteen v1.3.x contracts |
| `CODED` | `programme_model.py` and the four checkers. The Zotero bridge |
| `TESTED` | Those same five, at 93 tests, each checker with a self-test that reproduces the defect it was written for |
| `ACCEPTED` | **Nothing.** No work package has an independent verifier's record |
| `INTEGRATED` | **Nothing** |
| `COMMISSIONED` | **Nothing** |
| `MEASURED` | **Nothing.** No calibration run exists, so every performance figure in the plan remains a target |

The plan is now executable. That is a statement about the plan, not about the
system it describes — and the distance between those two is the whole of the
remaining work.
