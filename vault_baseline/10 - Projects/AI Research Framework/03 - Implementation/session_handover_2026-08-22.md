---
airl_id: AIRL-SESSION-HANDOVER-2026-08-22
type: handover
status: active
owner: otonom
created_at: "2026-08-22"
session_end_commit: cf57f1f
tags:
  - ai-framework/handover
  - ai-framework/execution
---

# Session Handover — 2026-08-22

> **Read this first when resuming.** It is the single document that answers
> "where was I, and what do I do next?" without re-reading the whole corpus.
> Reading order after this note: the
> [[10 - Projects/AI Research Framework/00_navigation_and_execution_cockpit|Cockpit]]
> → the top of the
> [[10 - Projects/AI Research Framework/implementation_log|Implementation Log]]
> → the relevant WP file.

---

## 1. Where things stand right now

| Field | Value |
|---|---|
| Repository | `/home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK` |
| Branch | `main`, working tree **clean** |
| HEAD = origin/main | **`cf57f1f`** — 0 ahead / 0 behind |
| Remote | `github.com/furkanhanilci/AI-Research-Framework` (private) — **the only authorised remote** |
| Last two steps | Step 004 (full English revision), Step 005 (file-by-file review) |
| Bridge service | `active` · sync timer `active` |
| Sources in registry | 33 |

### The last three commits

```text
cf57f1f  Add a session handover note so the next session resumes without re-reading
10395af  File-by-file review: document every module, make two evidence checks real
622aeb8  Rewrite the entire corpus in English, expanded
8415342  Restructure repository root, add skill layer and tooling packages
```

> The Zotero projection files carry a `generated_at` timestamp, so the 30-minute
> sync timer produces routine churn under `70 - Literature Sets/Zotero Sources`.
> A diff limited to those files after a timer run is expected, not a change.

---

## 2. Verify the state before touching anything

Run this whole block from the repository root. Everything must pass; if
something does not, **that is the first thing to investigate**, not the planned
work.

```bash
cd /home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK
V="/home/otonom/Documents/Obsidian Vault/10 - Projects/AI Research Framework"

git status --short                                   # expect: empty
git log --oneline -1                                 # expect: cf57f1f (or later)

uv run pytest                                        # expect: 20 passed
(cd planning/commissioning && sha256sum -c 00_PROGRAM/SHA256SUMS.txt | grep -c ': OK$')
                                                     # expect: 195
uv run python scripts/mcp_smoke.py     >/dev/null && echo "smoke OK"
uv run python scripts/acceptance_v0.py >/dev/null && echo "acceptance OK"
python3 scripts/mirror_plan.py  "$V/01 - Commissioning" --check | tail -1
python3 scripts/mirror_vault.py "$V" --check | tail -1
                                                     # expect: 0 drift entries, both
systemctl --user is-active airl-bridge.service airl-bridge-sync.timer
```

Expected end state: `20 passed`, `195`, `smoke OK`, `acceptance OK`,
`0 drift entries` twice, `active active`.

---

## 3. What was finished in this session

### Step 004 — the whole corpus rewritten in English, expanded

Not a translation — a re-authoring. Each document carries more explicit
reasoning than the version it replaced.

- 12 programme documents, renamed to English file names
- **140** work packages regenerated, English file names
- **40** acceptance scenarios plus the index
- `03_package_catalogue.md` and `package_dependency_matrix.csv` regenerated
  **mechanically** from the WP data — they are no longer hand-maintained
- the audit report, the review prompt, the three architecture documents
- category folder names, MCP tool descriptions and generated Obsidian banners in
  the code
- **two mirror generators added**: `scripts/mirror_plan.py` and
  `scripts/mirror_vault.py`, both with a `--check` drift mode

### Step 005 — file-by-file review of every tracked file

- **Module docstrings everywhere.** Not one source file had one before. Each now
  states its responsibility, its invariant, and **which audit findings apply to
  it**.
- **Finding M2 closed for real.** `scripts/mcp_smoke.py` used to exit `0` with
  the Bridge completely down. It now asserts the exact five-tool set and exits
  `1` on failure — verified behaviourally both ways.
- **Finding M3 closed for real.** `scripts/acceptance_v0.py` used to require the
  word "LiDAR" in the personal library. It is now 11 data-independent structural
  checks plus an optional live search.
- The tautological `zotero_write_enabled` assertion was **removed**, not kept.
- `docs/architecture/FOUNDATION.md` stub → a real document.
- "SILBO" removed from the systemd unit descriptions (an M10 leftover); units
  re-installed so the running copies match the repository.
- Four broken programme references in `planning/commissioning/README.md`.
- ACC severity rules made severity-aware (26 Critical / 12 High / 2 Medium).

---

## 4. What is explicitly NOT done

**Do not assume any of these are handled.**

| Finding | What is still missing | Why it matters |
|---|---|---|
| **C1** | **WP-000 Interim Evidence Policy is not written** | Every DoD requires a signed `EvidenceManifest` in an immutable store; that store is WP-026, far downstream. **No package — including WP-001 — can reach `ACCEPTED`.** The programme cannot start. |
| **C2** | No written decision on scope or on what "independent verifier" means for one person | 73 owners / 114 verifiers assumed; R3 is permanently `BLOCKED` |
| **H1** | Zotero ingest still capped at 100 records, no pagination, no `since=` | Above 100 sources the sync goes **silently partial** and still records `SUCCEEDED` |
| **H2** | No deletion reconciliation, no tombstones | A source deleted in Zotero lives on forever as a ghost |
| **H3** | No behavioural test of the read-only boundary | The strongest security claim is verified only by reading the code |
| **H4** | The contract core still has **zero** production consumers | `src/airl_bridge` imports nothing from `src/airl_framework`, and their hash formats contradict |
| **H5** | **No CI** | Every verification in §2 runs by hand; nothing stops a commit that never ran them |
| M1, M6, M7, M8, M9, M11 | untouched | see the audit report |

Also not done: no gate, contract semantic or work-package status has changed in
either session. Nothing is `ACCEPTED`.

---

## 5. The next steps, in order

### Step A — the blocking decision (yours, not mine) 🔴

**Settle the role → model assignment.** For every role: human / model /
deterministic code / deferred. The table to fill is Section 3.1 of
[[10 - Projects/AI Research Framework/04 - Architecture/airl_os_role_model_assignment|Role → Model Assignment]],
and the empty column is `A8` in
[[10 - Projects/AI Research Framework/04 - Architecture/airl_os_ideal_structure|Ideal Structure]].

**Nothing downstream can proceed without it:** the Independence Matrix cannot be
measured, the R classes cannot be applied, and the skills cannot enter baseline
testing.

Four decisions are waiting alongside it:

1. **R3 → local open-weight mandatory?** (Hosted Claude models have no
   date-suffixed identity, so `model_snapshot` cannot be pinned and Invariant 4
   cannot hold. Section 0 of the Role → Model document.)
2. **A non-Anthropic reviewer provider** — required for R2/R3 independence.
3. **In-principle acceptance at G2** — so G8 cannot reject on the *direction* of
   a result (closes publication bias, finding K4).
4. **The Zotero group library's data-class ceiling** (proposal: ≤ D1).

### Step B — `model_snapshot` → `capability_fingerprint`

A field rename plus a `GET /v1/models` snapshot. It stops the schema promising
something that cannot be delivered.

### Step C — write **WP-000 Interim Evidence Policy** `document-only`

Without it nothing can ever be accepted. Format proposed in
`delivery/README.md`; the external time anchor comes from **WP-139**
(OpenTimestamps — free, no trusted third party, hash-only).

### Step D — stand up CI 🔧 *highest leverage implementable step*

One GitHub Actions workflow closes **four findings at once**:
`uv sync` → `ruff check` → `pytest` → the read-only static check (half of H3) →
`sha256sum -c` (mechanises M4/M11) → the two `--check` mirror runs.

The verification bundle in §2 is already exactly what this workflow should run.

---

## 6. Gotchas to remember

**Ordering trap — fix M9 before H1.** The 10,000-row truncation in
`service.py` is masked today by the 100-record ingest cap. If H1 (pagination) is
fixed first, M9 becomes an **active data-loss path**: the projection would not
see sources beyond 10,000 and `_remove_stale` would then delete their files as
stale.

**Never edit a generated area.** `01 - Commissioning/`, `02 - Reviews/`,
`04 - Architecture/` and `07 - Skills/` in the vault are generated. Change the
canonical file, then regenerate:

```bash
python3 scripts/mirror_plan.py  "$V/01 - Commissioning"
python3 scripts/mirror_vault.py "$V"
rsync -a --delete --exclude '.obsidian/' "/home/otonom/Documents/Obsidian Vault/" vault_baseline/
```

The plan seal does **not** cover the mirror, so drift there is invisible unless
`--check` is run.

**Re-seal after any plan change.** Editing anything under
`planning/commissioning/` requires regenerating `00_PROGRAM/SHA256SUMS.txt`
(195 files) — deliberately, as part of a recorded change, never to silence a
failing check.

**Never push to the SILBO repository.** `furkanhanilci/AI-Research-Framework` is
the only authorised remote. SILBO (`/home/otonom/silbo-fix-00*`) is a separate
authority boundary, and no SILBO acceptance implies any framework acceptance.

**No Zotero writes.** No API key exists and no write path exists. Keep it that
way until WP-064/066 define a group library and an audit policy.

**After a path change, three things break together:** venv console-script
shebangs, the editable-install `.pth` file, and the absolute paths in the systemd
units and the Hermes config. Symptom of the second:
`ModuleNotFoundError: No module named 'airl_bridge'` while `python -m` still
works.

---

## 7. Where the source of truth lives

| Question | File |
|---|---|
| What is the state, what is next? | this note, then the Cockpit |
| What happened, with evidence? | `implementation_log.md` (Steps 000–005) |
| What is actually broken? | `docs/review/FRAMEWORK_REVIEW_2026-08-21_CLAUDE.md` |
| What should be added to the architecture? | `docs/architecture/AIRL_OS_IDEAL_STRUCTURE.md` |
| How should agents work? | `docs/architecture/AIRL_OS_SKILL_LAYER.md` + `skills/` |
| Who executes what? | `docs/architecture/AIRL_OS_ROLE_MODEL_ASSIGNMENT.md` |
| The plan itself | `planning/commissioning/` (canonical, hash-sealed) |
| Where is everything kept? | `04 - Architecture/framework_repository_and_obsidian_map` |

---

## 8. One-paragraph summary

Two full sessions turned the corpus into English and expanded it, added mirror
generators so the Obsidian tree is no longer hand-maintained, documented every
module against the audit findings that apply to it, and closed findings **M2**
and **M3** by making two fake verification scripts into real ones. **Nothing
about the framework's actual capability changed**: the Bridge is still the only
working vertical slice, no work package is `ACCEPTED`, and the two critical
blockers (**C1** evidence deadlock, **C2** scope versus organisation) are exactly
where they were. The next move is a decision, not code: **who executes each
role — human, model, or deterministic code.**
