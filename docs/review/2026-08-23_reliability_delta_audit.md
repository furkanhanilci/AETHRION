# Reliability Completion Delta — Pre-Edit Audit

| Field | Value |
|---|---|
| Document type | Review — dated, frozen. Never updated |
| Scope | The state of the repository immediately before the reliability completion delta was applied |
| Sibling documents | `2026-08-23_reliability_delta_id_remap.md` (the identifier decisions this audit forced) |
| Status | Frozen at `db2fe02` + the baseline v1.2.0 working tree |
| Date | 2026-08-23 |

**In one paragraph.** The reliability completion delta arrives as a second binding
package and instructs its implementer to re-audit the repository *before* editing
anything, because it was written against an assumed post-assimilation state
rather than an observed one. This record answers its eight audit questions from
what the repository actually contains, and names the two places where the package
and the repository disagree. Both disagreements are identifier collisions, and
neither changes a decision.

---

## 1. The questions the package asks, answered from the tree

| # | Question | Answer |
|---|---|---|
| 1 | Were WP-141–147 actually created? | **Yes.** `14_SCIENTIFIC_INTELLIGENCE/` holds seven packages, each with a card, test procedures and acceptance criteria |
| 2 | Were ACC-52–80 actually created? | **Yes.** 29 scenarios, ACC-52 through ACC-80, indexed and bidirectionally referenced |
| 3 | Is the 11/31/10 skill family split preserved? | **Yes.** `validate_skills.py` reports engineering 11 · scientific-research 31 · shared 10 |
| 4 | Are Temporal / NATS / LangGraph consistent in docs and code? | **In documents, yes.** In code, the question does not arise: none of the three exists. `src/` is 13 Python modules — the Zotero bridge and the contract core |
| 5 | Is the OPA vs Cedar contradiction resolved by ADR? | **Yes** — `ADR-010`, accepted 2026-08-23. Resolved by commissioning the `PolicyDecision` interface and deferring the engine to a bake-off that has not run |
| 6 | Are CoE, VerifiedValue, EvidenceGap, the artifact DAG, the discovery graph, the reproduction zones and the publication compiler `SPECIFIED` or `CODED`? | **All `SPECIFIED`.** None is coded. The only capability from the first package with running code is the upstream lineage register and its checker |
| 7 | Are generated indexes and figures produced from a source of truth? | **Yes.** 12 figures and 16 directory indexes, both reporting zero drift against their generators |
| 8 | Do the previous baseline seals verify? | **Yes.** 554/554, and the `v1.1.0` tag and its seal are untouched |

---

## 2. Where the package and the repository disagree

### 2.1 Identifier collision — the ADRs

The package proposes `ADR-004` through `ADR-012`. **All nine numbers are taken.**
Baseline v1.2.0 accepted `ADR-004` to `ADR-010` on 2026-08-23, and they decide
different questions.

The package's own rule settles this: *"Repository bu ID'leri daha önce
kullanmışsa asla overwrite etme; sonraki boş ID'leri ata."* The remapping and the
two semantic overlaps it exposes are recorded in
[`2026-08-23_reliability_delta_id_remap.md`](2026-08-23_reliability_delta_id_remap.md).

### 2.2 No collision — the work packages and scenarios

`WP-148`–`WP-159` and `ACC-081`–`ACC-120` are free. The first package stopped at
WP-147 and ACC-80, so the second package's preferred numbering lands exactly
where it expected to. No renumbering is required, and none is performed.

---

## 3. What this audit changes about how the delta is applied

**The delta's execution order assumes a runtime.** Steps 5 through 18 of
`42_CLAUDE_EXACT_EXECUTION_ORDER.md` say *implement* — regenerate SDKs, build the
naive fully-connected baseline harness, run faulty-agent fixtures, verify
ordering in UI and API tests. None of that is possible against a repository whose
`src/` is a Zotero bridge, and pretending otherwise would produce exactly the
defect this repository's document standard exists to prevent.

So the delta is applied **at the phase the repository is actually in**:
specification, plan, contracts-on-paper, acceptance criteria and the checks that
can run today. Every capability it adds is reported as `SPECIFIED`, and the
completion report says so per capability rather than in a footnote.

**This is not a reduction of the delta's scope.** Every mechanism it names is
recorded, with its tests, its acceptance criteria and its work package. What is
withheld is the claim that any of it runs.

---

## 3.1 Coverage of the delta's own documents

The delta is forty-two numbered documents plus five directories. Each is applied,
deferred with a reason, or absorbed into an existing repository control. Nothing
is silently dropped — a coverage claim with no per-document row is the same
sentence as "no findings" from a detector that never fired.

| Delta documents | Applied as | Note |
|---|---|---|
| 01–03 scope, target architecture, risk register | `01_target_state_and_invariants.md`, `07_programme_risk_register.md` PR-29–PR-58 | The risk register is the largest single absorption |
| 04–10 collaboration plane, topology, blackboard, governor, memory, resilience, budget | `ADR-011`, `ADR-013`, WP-148–153, ACC-081–102, figure 13 | The plane is also drawn into `README.md` §4.1 |
| 11–12 engineering discipline, spec conformance | `ADR-012`, `ADR-018`, WP-154, ACC-103–104 | The four non-synonym pairs became a test set, not a paragraph |
| 13–16 evidence integrity, adaptive assurance, human oversight, reproduction | `ADR-015` (extends `ADR-008`), `ADR-016`, WP-155–157, ACC-105–116 | `ADR-015` is an extension and is cross-linked both ways |
| 17–19 capability gate, benchmark firewall, supply chain | `ADR-017`, `ADR-019` (extends `ADR-004`), WP-155, WP-158–159, ACC-117–118, ACC-120 | Licences verified at the source; three changed the method |
| 20–21 canonical authority, publication and monitoring | `ADR-014`, WP-159, ACC-119, figure 14 | The one entry with running code — `monitor_sources.py` — is ASM-057 |
| 22–24 skill/role/compiler changes, contracts, code topology | `AETHRION_ROLES.md` §1.2, `AETHRION_SKILL_LAYER.md` §16, `schemas/README.md` v1.3.0 group | Seventeen contracts named and owned; none written |
| 25–27 impact matrices, numbering policy, test strategy | The remap record, and the WP/ACC extensions | Numbering: never overwrite; the semantic name is binding |
| **28 external benchmark qualification** | **`06_evidence_and_acceptance_strategy.md` — "E6"** | Five axes, three constraint rules, none run |
| **29 metascience and Pareto gates** | **`06` — "Release quality is a frontier, not a verdict"** | The measurement set is fixed and public so a favourable subset cannot be chosen afterwards |
| 30–31 documentation map, migration sequence | Figures 13–14, the plane section, and §3 above | The migration sequence is deferred with the runtime it assumes |
| **32 baseline freeze dossier** | **`09_change_and_configuration_control.md` — "The baseline freeze dossier"** | Fifteen inventory elements and the five-word maturity vocabulary |
| 33–34 edit checklist, master instruction | Executed rather than recorded | These are instructions to the applier, not content |
| **35 definition of done / final audit** | **`05_definition_of_ready_and_done.md`, and `check_stale_claims.py`** | The ten DONE conditions as prose; the eight stale wordings as **eight mechanical rules with a self-test** — findings J3 and J4 |
| 36–37 assimilation matrix, bibliography | `provenance/upstreams.json` ASM-037–058 | Verified by hand; four claims corrected against the package |
| **38 hard acceptance targets** | **`10_go_live_checklist.md` and `06`** | Hard zeros as checklist conditions; performance figures as **targets to be frozen after calibration**, never as constants |
| 39–42 summary, traceability matrices, execution order | The remap record and §3 above | Steps 5–18 assume a runtime and are deferred with the reason stated |
| `adrs/`, `risks/`, `sources/`, `templates/`, `wp_new/`, `wp_updates/` | ADR-011–019, PR-29–58, ASM-037–058, WP-148–159 | The templates were matched to the repository's existing format rather than adopted |

The five documents in bold were applied last and are the reason this section
exists: they were the ones most easily mistaken for summary material. Two of them
were not — 35 became a mechanical control, and 29 supplied the measurement set
that keeps the coordination numbers from being gamed by silencing the cohort.

## 3.2 The pre-existing scenarios, extended rather than duplicated

`ACC_001_080_EXISTING_IMPACT_MATRIX.md` marks fifty-five scenarios
`REVIEW/EXTEND` with the instruction *"avoid duplicate semantics"*. Twenty-nine of
those are ACC-052–080, authored at baseline v1.2.0 and already carrying the layer
the matrix is asking for. The remaining **twenty-six** predate it, and each has
been extended in place: two or three additional invariants, one additional test
step, and a short section naming the failure the scenario would otherwise pass
while leaving unexamined.

The extension is an extension, not a rewrite. Where the reliability layer needs a
scenario of its own it has one in ACC-081–120, and each added block says so
explicitly, so a reader who arrives at ACC-05 from an old reference finds the new
obligation without finding a second copy of ACC-117.

One correction fell out of the same pass: **ACC-08 described its counter-test as
run by "the mechanical verifier"** — precisely the wording `35` asks a final
audit to search for. It is a deterministic re-execution against a frozen target,
so it is now named as the **V1 computational verifier** it is. The regression rule
does not fire on it either way; the wording was wrong before the rule existed and
was found by reading, which is worth recording as the limit of the rule.

---

## 4. What this audit does not establish

It confirms that the first package's artifacts exist and that its checks pass. It
does not establish that any of those artifacts describes something that works —
the same limit `AGENTS.md` §11 states about the whole verification bundle. Every
answer in §1 marked "yes" is an answer about presence, not about behaviour.
