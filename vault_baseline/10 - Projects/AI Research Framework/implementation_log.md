---
airl_id: AI-RESEARCH-FRAMEWORK-IMPLEMENTATION-LOG
type: execution-log
status: active
owner: otonom
updated_at: "2026-08-22"
tags:
  - ai-framework/execution
  - ai-framework/contracts
  - ai-framework/foundation
---

# AI Research Framework — Implementation Log

Every material implementation step is recorded here. Each entry separates **what
was observed** (evidence) from **what was concluded** (interpretation), states
its **limits**, and names the **exact next step**. Before starting a new step,
the last entry, the cockpit and the relevant WP files are read again.

---

## Step 005 — File-by-file review of the whole repository

**Time:** 2026-08-22
**Scope:** every directory and every tracked file
**Status:** `DOCUMENTATION_COMPLETE` + two audit findings actually closed

### What was done

A file-by-file pass over the repository. Three kinds of change:

**1. Documentation added where there was none.** Every module in `src/`, every
file in `tests/` and both entry scripts now carry a module docstring that states
what the module is responsible for, which invariant it upholds, and **which audit
findings apply to it**. Previously not a single source file had one. The point is
that an agent loading `obsidian.py` should learn, from the file itself, that this
is the code that deletes files in the user's vault and why manifest-owned
deletion is the reason no human note has been lost.

**2. Two evidence-theatre findings closed with real fixes.**

| Finding | Before | After |
|---|---|---|
| **M2** `mcp_smoke.py` | Reported `isError` without checking it; no `assert`, no `raise`, no `sys.exit`. Exited 0 with the Bridge completely down. | Asserts the **exact** five-tool set, both call results and a non-empty response. **Verified: exits 1 with the Bridge stopped, 0 with it running.** |
| **M3** `acceptance_v0.py` | Failed unless the user's personal library contained a paper matching the hard-coded term "LiDAR". Also asserted `zotero_write_enabled is False` — a tautology against a constant. | Split into 11 data-independent structural checks plus an optional live search reading `AIRL_ACCEPTANCE_QUERY`. An empty result is `SKIPPED`, not `FAIL`. The tautological check was **removed**, and the script now reports what it does *not* prove. |

Removing the `zotero_write_enabled` assertion matters more than it looks: an
assertion that cannot fail is worse than no assertion, because it manufactures
the appearance of evidence. The read-only claim is now honestly labelled as
verified by reading the code, not by testing it (finding **H3** stays open).

**3. Stale content corrected.**

- `docs/architecture/FOUNDATION.md` was a one-line stub — one of the empty
  "deliverables" behind finding **C3**. It is now a real document: what the
  foundation layer is, what exists, and the three gaps that block it.
- The systemd unit descriptions still said "SILBO" (a leftover of finding
  **M10**). Fixed in `deploy/` and re-installed so the running units match.
- `planning/commissioning/README.md` pointed at four programme documents by
  their **pre-rename uppercase names** — four broken references. Fixed, and an
  explicit inventory table added (140 WPs, 40 ACCs, 194 Markdown files, 195
  sealed).
- Every ACC file claimed "A Critical scenario can never be waived" regardless of
  its own severity. Now severity-aware: 26 Critical, 12 High, 2 Medium, each with
  the rule that actually applies to it.
- A stray blank line under "Out of scope" in 129 generated WP files.

### Evidence

```
uv run pytest                                  20 passed
plan seal                                      195/195 OK
uv run python scripts/mcp_smoke.py             PASS (exit 0; exit 1 when Bridge stopped)
uv run python scripts/acceptance_v0.py         PASS (exit 0; 11 structural checks)
mirror_plan.py --check                         196 files, 0 drift
mirror_vault.py --check                        44 files, 0 drift
plan links                                     1021, 0 broken
doc links                                      63, 0 broken
vault wikilinks                                148, 0 broken
Turkish characters in tracked files            0
vault == vault_baseline                        identical
```

### Limits

- **Still no CI (finding H5).** Every check above runs by hand. Nothing prevents
  a commit that never ran them.
- **H3 remains open.** The read-only boundary needs a `MockTransport` behavioural
  test plus a static check; this step made the claim *honest*, not *proven*.
- C1, C2, H1, H2, H4 and the remaining M-series are untouched.
- No gate, contract semantic or work-package status changed.

### Next step

Unchanged: **settle the role → model assignment**, then rename
`model_snapshot` → `capability_fingerprint`, then stand up CI.

---

## Step 004 — Full English revision of the corpus

**Time:** 2026-08-22
**Scope:** the whole repository and the Obsidian project tree
**Status:** `DOCUMENTATION_COMPLETE`

### What was done

The entire corpus was rewritten in English and expanded — not translated
mechanically, but re-authored so that each document carries more explicit
reasoning than the version it replaces.

| Area | Result |
|---|---|
| `planning/commissioning/00_PROGRAM/` | 12 documents rewritten and renamed to English file names |
| `planning/commissioning/` WP files | **140** work packages regenerated in English, with English file names |
| `planning/commissioning/12_ACCEPTANCE_SCENARIOS/` | **40** scenarios plus the index rewritten |
| `03_package_catalogue.md` + `package_dependency_matrix.csv` | Regenerated mechanically from the WP data |
| `docs/review/` | The audit report and the review prompt rewritten; remediation status added |
| `docs/architecture/` | The three architecture documents rewritten |
| `skills/` | Already English; unchanged in this step |
| `src/`, `tests/` | User-facing strings, category folder names and MCP tool descriptions moved to English |
| Obsidian vault | Regenerated from canonical sources; human-authored notes rewritten |

### New in this step: the mirror generators

Two scripts were added, closing part of finding **M4**:

- `scripts/mirror_plan.py` — generates the Obsidian plan mirror from
  `planning/commissioning/`, rewriting file names and intra-plan links.
- `scripts/mirror_vault.py` — generates the skills and docs mirrors from
  `skills/` and `docs/`.

Both accept `--check`, which writes nothing and exits non-zero on drift. That is
the CI drift check the audit asked for; **it is not yet wired into CI**, because
there is still no CI (finding H5).

### Why it was done

A laboratory operated by multiple models cannot afford a corpus in two languages:
every document is an agent context, and mixed-language context degrades both
retrieval and instruction-following. The expansion matters as much as the
translation — the audit measured 59.2% template repetition in the WP files, and
the rewrite raises the density of package-specific content.

### Evidence

- `uv run pytest` → **20 passed** (fresh run, exit 0)
- `grep -rlP '[Turkish characters]'` across the repository → only the historical
  quotation inside audit finding L3, since rephrased → **0**
- `scripts/mirror_plan.py --check` → 196 generated files, **0 drift entries**
- `scripts/mirror_vault.py --check` → 44 generated files, **0 drift entries**
- Plan seal regenerated and re-verified after the rename

### Limits

- This step changed **documentation and user-facing strings**. It changed no
  gate, no contract semantics and no WP status.
- CI still does not exist, so none of these checks runs automatically.
- Findings C1, C2, H1–H5 and most of the M-series remain open.

### Next step

Unchanged from Step 003: **settle the role → model assignment.** Then rename
`model_snapshot` → `capability_fingerprint`, then stand up the CI foundation
(which closes H5 and automates the evidence production the rest of the plan
depends on).

---

## Step 003 — Independent audit and target-structure design

**Time:** 2026-08-22
**Scope:** the whole framework — plan, implementation, architecture, skill layer
**Status:** `DESIGN_PROPOSED / HUMAN_DECISION_PENDING`

### What was done

Three documents were produced:

1. [[10 - Projects/AI Research Framework/02 - Reviews/claude_framework_audit_report|Claude Framework Audit Report]] —
   an evidence-based independent audit. 1,509 lines of Python, 20 tests, the live
   service, SQLite, Git, the vault and 186 plan files were examined.
2. [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|AIRL-OS Ideal Structure]] —
   the added roles, review mechanisms, the 7th plane (Metascience & Calibration),
   the role→model assignment architecture and the tool stack.
3. [[10 - Projects/AI Research Framework/04 - Architecture/airl_os_skill_layer|AIRL-OS Skill Layer]] —
   the integration of all 14 `obra/superpowers` skills into AIRL-OS.

### Why it was done

The existing `AIRL-OS-Architecture.md` defines *who* an agent is
(`RoleContract`) but not *how it works*. That gap is currently filled by an
unversioned, untested prompt layer. And the system audits the research while
never measuring its own capacity to produce correct results.

### Evidence

- Test suite: `20 passed` (fresh run, exit 0)
- Plan integrity: `sha256sum -c` → 184/184 OK
- Dependency graph: 130 WPs, no cycles, forward dependencies 0
- Template ratio: 59.2% in WP files, 48.8% in ACC files (measured)
- Role counts: 73 owners, 114 verifiers (CSV analysis)
- Wikilink integrity: 246 notes, 103 wikilinks, 0 broken

### Limits

- This is a **proposal**; no WP status was changed.
- Two findings in the audit were later narrowed (C2 and M5) — the corrections are
  marked in the report itself.
- The skill layer was designed but not implemented.
- The role→model assignment **awaits a human decision** (who is human, who is a
  model).

### Also done in this step

**The skill layer was written (38 skills).** All 14 `obra/superpowers` skills are
covered, plus 17 specific to the research domain and 7 for communication and the
external world. Canonical copy: `skills/`. Obsidian mirror:
[[10 - Projects/AI Research Framework/07 - Skills/skills_index|Skills Index]].

**The communication layer was designed.** Messaging was modelled not as a skill
but as a **Notification Broker** (a Tool Broker subclass). A per-channel
data-class ceiling was defined. Three rules: a notification is not a data
channel; an inbound message is not an instruction; messaging is not an
authorisation channel.

**Obsidian was audited and reorganised.** Defects found and fixed:

| Finding | Status |
|---|---|
| `.obsidian/templates.json` pointed at a non-existent folder — **templates were not working** | ✅ fixed |
| Dataview was not installed → every index `query` block was dead | ✅ converted to core-search syntax (12 files) |
| No daily-note folder → an empty daily note cluttering the vault root | ✅ `80 - Daily/` created, note moved |
| Templates carried a `silbo/*` tag namespace (the project had been renamed) | ✅ `ai-framework/*` (16 files) |
| `README` ×2, `readme` ×2 — duplicate note names | ✅ the `<area>_index.md` convention, 0 duplicates |
| No index note in the `02/04/06/07` folders | ✅ added |
| `05 - Evidence/` empty | ✅ audit evidence added |

### Step 003 continued — plan revision and the communication packages

**A new section: `13_TOOLING_INTEGRATION` (WP-131–140).** The Y13/Y14/Y15 gaps
identified in the audit were brought down to package level:

| Package | Scope |
|---|---|
| WP-131 | Notification Broker — the agent produces intent, the broker sends |
| WP-132 | Channel registry + data-class ceiling (D3/D4 leave through no channel) |
| WP-133 | Outbound notification + daily/weekly/monthly digests |
| WP-134 | Escalation and paging — a timeout is never an auto-approval |
| WP-135 | Decision routing + signed deep links (the preventive side of ACC-25) |
| WP-136 | Inbound content quarantine — an inbound message is never an instruction |
| WP-137 | G10 external feed connectors (Crossref / Retraction Watch / CVE) |
| WP-138 | External records: OSF preregistration, Zenodo DOI, ORCID |
| WP-139 | **Evidence timestamping** — OpenTimestamps + RFC 3161 |
| WP-140 | **Service liveness monitoring** — silent-death detection |

**Why WP-139 matters:** it makes the existence time of an `EvidenceManifest`
verifiable **without trusting the framework**. OpenTimestamps is free, requires no
trusted third party, and the file never leaves the machine — only a hash is sent.
That is the infrastructure-free solution to audit finding **C1** (the evidence
bootstrap deadlock).

**Why WP-140 matters:** audit findings **H1/H2** (silently partial sync, ghost
sources) belong to the "silent death" class — the job does not error, nothing
simply happens. A dead-man's switch makes that visible.

**The new packages carry measurable acceptance criteria.** In the existing 130
packages the criteria were 59% template and generic; in these 10, every criterion
is countable or testable.

### Limit

The content of the existing WP-001–130 was **not revised** in this step. Scope
reclassification (IN_SCOPE / DEFERRED) and the WP-000 Interim Evidence Policy
remain open.

### Next step

**Settle the role→model assignment.** For every role: human / model /
deterministic code / deferred. Without that decision the Independence Matrix
cannot be measured, the R classes cannot be applied, and the skills cannot enter
baseline testing.

Then: the baseline (RED) test for `writing-skills`, then pressure-testing the
five discipline skills in group B, then revising the WP files under
`planning/commissioning/` against this structure.

---

## Step 002 — Central project organisation and retrospective visibility correction

**Time:** 2026-08-21
**Scope:** all framework documentation, review, implementation, architecture,
evidence and component records
**Status:** `DOCUMENTATION_VISIBLE / REVIEW_READY`

### What changed

- General framework records were placed in the central Obsidian project tree
  rather than only under the Bridge application repository.
- Added `02 - Reviews/` for independent review prompts and results.
- Added `03 - Implementation/` for implementation indexes and step records.
- Added `04 - Architecture/` for repository and system maps.
- Added `05 - Evidence/` for test, acceptance, hash and review evidence.
- Added `06 - Components/Bridge/` so the Bridge is explicitly represented as one
  component rather than as the framework root.
- Added the complete review prompt and direct cockpit links.
- The complete commissioning mirror remains under `01 - Commissioning/`.

### Why

The previous layout made newly created general documents appear to belong to the
Bridge alone, and the actual Obsidian vault had not yet received the new project
folders. This separation makes the full project topology visible while keeping
code in the repository and user-facing project records in Obsidian.

### Evidence

- `04 - Architecture/framework_repository_and_obsidian_map.md`
- `02 - Reviews/claude_full_framework_review_prompt.md`
- `06 - Components/Bridge/bridge_component_status.md`
- `03 - Implementation/implementation_index.md`
- The cockpit section "Framework visibility map"

### Boundary

This is a documentation and navigation correction. It does not claim that the
work packages or acceptance scenarios are implemented. Implementation status
remains evidence-based and is tracked separately.

### Next

Use the central tree for every subsequent step: read the cockpit → the relevant
WP/ACC → implement in the correct repository component → test → record evidence
and the next step in this log → synchronise the Obsidian vault.

---

## Retroactive history — implementation steps completed before this log existed

This section records material steps completed before the Implementation Log was
created. The historical records are limited to what existing Git commits, test
output, systemd status and Obsidian hash comparisons can support; **intentions
without evidence are not shown as completed work.**

### Step 000-A — Existing installation discovery

- **What:** examined the Zotero Local API, Hermes MCP, the Obsidian vault, the
  Bridge working directory, the systemd unit and timer, and the existing file tree.
- **Why:** to avoid overwriting real paths and existing user data on an assumption.
- **Evidence:** the initial discovery and the subsequent Bridge V0 commit chain.
- **Limit:** discovery only; no production architecture is implied.
- **Next:** verify the read-only Zotero connection.

### Step 000-B — Zotero Local API and the read-only boundary

- **What:** enabled Zotero Local API loopback access; constrained the Bridge so
  that it performs no write, delete, merge or mutation of a Zotero human field.
- **Why:** to protect the user's bibliographic records from automated agent writes.
- **Evidence:** `zotero_write_enabled=false`; live acceptance output.
- **Limit:** ⚠️ **that evidence is weaker than it looks.** The field is a hard-coded
  constant, not a measured control — see audit finding **H3**. The boundary holds
  in the code as written, but nothing tests it.
- **Next:** the canonical local source registry and the Obsidian projection.

### Step 000-C — Literature Bridge V0

- **What:** built the FastAPI Bridge, the SQLite WAL registry, source identity
  and normalisation, the category and duplicate endpoints, and the Obsidian
  projection.
- **Why:** to run the first end-to-end vertical slice before moving to the large
  architecture.
- **Evidence:** commit `15d57af`; acceptance `33 sources / 3 categories`; the
  Bridge systemd service and timer active.
- **Limit:** SQLite V0; no PostgreSQL, no event bus, no Temporal, no production
  cutover. Ingest is capped at 100 records (finding **H1**).
- **Next:** separate the human and generated Obsidian areas.

### Step 000-D — Obsidian information architecture

- **What:** created the `00 - Home`, `10 - Projects`, `20 - Source Notes`,
  `30 - Concepts`, `40 - Claims`, `50 - Decisions`, `60 - Runs`,
  `70 - Literature Sets`, `90 - Archive` and `_Templates` structure; moved the
  Zotero projections under `70 - Literature Sets/Zotero Sources`.
- **Why:** so that human synthesis and automated projection files cannot
  overwrite one another.
- **Evidence:** commits `d3fc23a`, `2d64f02`; baseline/vault SHA-256 matches.
- **Limit:** this information architecture is not a full claim/evidence graph.
- **Next:** bring the plan Markdown into Obsidian and build the execution cockpit.

### Step 000-E — Commissioning plan import and cockpit

- **What:** imported the commissioning Markdown tree (130 WPs and 40 ACCs) into
  Obsidian; added the navigation/execution cockpit and the living status document.
- **Why:** so the plan is re-read at every step rather than living in chat memory.
- **Evidence:** 184 plan Markdown files in Obsidian; the cockpit's reading and
  step-closure rules.
- **Limit:** importing the plan does not mean the WPs have been built as services.
- **Next:** turn the plan into real foundation contract slices along the WP
  dependency order.

### Step 000-F — Naming and repository consolidation

- **What:** standardised the general root as `AI_RESEARCH_FRAMEWORK`; moved
  Obsidian folder and file names to a lowercase English standard; drove broken
  links to zero across 240 notes.
- **Why:** to separate the SILBO model name from the framework name and to prevent
  file and folder drift.
- **Evidence:** commit `d73b53e`; `notes=240, missing_links=0`; the generated
  dashboards `Source Catalog.md` and `Potential Duplicates.md`.
- **Limit:** Zotero article titles keep their original bibliographic form.
  ⚠️ The rename was **incomplete** — six documentation locations and the source
  category folder names kept their old values until Step 004 (finding **M10/L3**).
- **Next:** add the foundation and shared contract code.

### Step 000-G — SILBO readiness boundary

- **What:** produced capsule, mutation, byte-identical resume and drift-rejection
  evidence for FIX-005; inference was not started.
- **Why:** so the SILBO measurement line stays fail-closed while the framework
  advances.
- **Evidence:** SILBO target `b14b0b3`, evidence `3dd52e0`, handoff `ff696c7`.
- **Limit:** SILBO grants no inference authority without independent review.
  **This work lives in a separate repository and is outside the framework's
  evidence chain.**
- **Next:** implement the framework contract foundation slice; keep the SILBO
  review boundary separate.

---

## Step 001 — Foundation and contract core

**Time:** 2026-08-22
**Related plans:** WP-011, WP-014, WP-015, WP-020, ~~WP-022~~
**Status:** `TECH_COMPLETE / INDEPENDENT_REVIEW_PENDING`

### What was done

- Created the shared contract core under `src/airl_framework/contracts.py`:
  - `Identity`: validates project/workflow/task/source/claim/run/artifact/review
    identifiers in one format and derives a deterministic correlation key.
  - `ArtifactManifest`: requires SHA-256, size, producer, source revision, parent
    lineage and a `VALID/SUPERSEDED/REVOKED/QUARANTINED` state.
  - `EventEnvelope`: carries event type, schema version, actor, subject, payload
    reference, causation and correlation; it binds the payload by reference
    rather than silently embedding it.
  - `SchemaRegistry`: records the schema version, refuses redefinition and treats
    a major-version mismatch as a breaking change.
- Made the contract surface importable through `src/airl_framework/__init__.py`.
- Added `CODEOWNERS` and `dependency-rules.txt` boundary files.
- Tested both the accepting and the rejecting directions in
  `tests/test_contracts.py`.

### Correction (2026-08-22)

This step originally also claimed **WP-022 (repository topology)** as
`TECH_COMPLETE`. **That claim was wrong** and is retracted:

- The directories it created (`services/`, `workflows/`, `agents/`, `infra/`,
  `policy/`) were empty, and Git does not track empty directories — so they never
  existed in the remote repository at all.
- `CODEOWNERS` contained a single comment and enforced nothing;
  `dependency-rules.txt` was one unparseable line.

See audit finding **C3**. **WP-022 status: `NOT_STARTED`.** The two boundary
files now carry real content (Step 004), but without CI enforcement they are
still not a deliverable.

### Why it was done

The plan's target invariants require one correlation chain, immutable artifact
lineage, versioned events and canonical field authority. The existing bridge had
only the literature `SourceRecord` model; without this shared core, later claim,
run, review and decision services would each mint incompatible identities.

This step is not the production infrastructure. It establishes the shared
contract boundary that later services will bind to.

### Evidence

- `uv run pytest -q` → **20 passed**.
- The tests cover acceptance of valid identity/artifact/event/schema objects and
  rejection of lowercase identifiers, malformed digests, schema redefinition and
  a missing major version.

### Limits and open points

- ⚠️ **The contract core has zero production consumers** — nothing in
  `src/airl_bridge/` imports it, and its `content_hash` format already contradicts
  the format the bridge produces. See finding **H4**.
- `SchemaRegistry` is not yet a persistent registry service or a database; it is
  an in-process prototype that validates nothing against JSON Schema.
- The CODEOWNERS owners are placeholders; they must be settled by the WP-003 RACI
  and the WP-010 ADR decision.
- PostgreSQL, the object store, the event bus, the policy engine and Temporal have
  not been built.
- There is no independent verifier acceptance, so the step is `TECH_COMPLETE`,
  not `ACCEPTED`.

### Next step

Move the WP-011/014/015/020 contract surface into JSON Schema and
machine-readable manifest files, and give it **at least one real production
consumer** (route `SourceRecord.airl_id` generation through `Identity`). Then
bind the WP-013 project/task/role contract to the same registry.
