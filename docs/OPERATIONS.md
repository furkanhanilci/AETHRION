# Operations Guide

| Field | Value |
|---|---|
| Document type | Operations runbook |
| Scope | Running, verifying and recovering the working components; not the target architecture |
| Sibling documents | `ARCHITECTURE_V0.md` (what the running slice is) · `architecture/AETHRION_ARCHITECTURE.md` (what it will become) |
| Status | `WORKING` — describes components that run today |
| Date | 2026-08-22 |

**In one paragraph.** Everything in this runbook concerns the one vertical slice that actually runs: the Zotero bridge, its canonical registry, the Obsidian projection and the read-only MCP surface. It covers day-to-day operation, the verification bundle, mirror integrity, and the three things that break together after a path change. The first six checks are also defined as a push-triggered control, **BVC-01**,
which is written but **not yet active**; the rest stay manual because they need a
live Bridge, a local Zotero library or the operator's vault. Finding **H5** —
the absence of the WP-024 CI platform — remains open either way.

## Daily status check

```bash
curl -fsS http://127.0.0.1:8765/ready
systemctl --user is-active airl-bridge.service airl-bridge-sync.timer
systemctl --user list-timers airl-bridge-sync.timer --no-pager
```

Expect `{"status":"ready","zotero":"reachable",...}` and two `active` results.

## Manual synchronisation

```bash
curl -fsS -X POST 'http://127.0.0.1:8765/v1/sync?limit=100'
```

This does not write to Zotero. It updates the SQLite registry and regenerates
only the `70 - Literature Sets/Zotero Sources` branch.

> ⚠️ `limit` is capped at 100 and there is no pagination. Above 100 sources the
> synchronisation is silently partial — see finding **H1**.

## Hermes verification

```bash
hermes mcp test airl_bridge
cd /home/otonom/Desktop/FH/AETHRION
uv run python scripts/mcp_smoke.py            # exit 0 = pass, 1 = fail
uv run python scripts/mcp_smoke.py --query attention
```

The smoke check asserts three things and **exits non-zero on any failure**: that
the server exposes exactly the five expected read-only tools and no others, that
neither `bridge_status` nor a search returns an error, and that the search
returns at least one content block. Verified behaviour: with the Bridge stopped
it exits `1`; with the Bridge running it exits `0`.

Adding a sixth tool is a boundary change and will fail this check until
`EXPECTED_TOOLS` in the script is deliberately updated. That is the intent.

> **Scope limit.** This verifies what *this* MCP server exposes. The
> `tools.include` restriction on the Hermes side lives in the Hermes
> configuration, outside this repository, and must be checked there: it must list
> exactly five tools, with `prompts` and `resources` disabled.

## Logs

```bash
journalctl --user -u airl-bridge.service -n 100 --no-pager
journalctl --user -u airl-bridge-sync.service -n 100 --no-pager
```

If Zotero is closed the scheduled run fails and the next timer retries. The
database and the last successful Obsidian projection are preserved.

## Plan integrity

```bash
sha256sum -c planning/commissioning/00_PROGRAM/SHA256SUMS.txt
```

All entries must report `OK`. A failure means a plan file changed without the
seal being regenerated — investigate before proceeding.

## Obsidian baseline parity

The repository copy under `vault_baseline/` and the live vault must be
byte-identical for every tracked file:

```bash
diff -rq vault_baseline "/home/otonom/Documents/Obsidian Vault" \
  | grep -v "Only in .*\(\.obsidian\|Zotero Sources\)"
```

No output means parity holds.

## Layout migration backups

Reversible local backups of earlier vault layouts:

```text
data/projection-backups/
  Sources-before-title-migration-<date>/
  vault-layout-before-<change>-<date>/
```

> ⚠️ These backups are excluded from version control and are not backed up
> elsewhere. Do not delete one without verifying it first, and do not rely on
> them as the only recovery path.

## Safe reinstall sequence

1. `uv sync --extra dev`
2. Copy `.env.example` to `.env` and set the vault path
3. Copy the units from `deploy/` into the user systemd directory
4. Enable the Bridge service and verify `/ready`
5. Copy the vault baseline files
6. Run one manual synchronisation
7. Add the Hermes MCP server and apply the five-tool allowlist
8. Enable the synchronisation timer
9. Run `scripts/acceptance_v0.py` and the test suite

## Acceptance check

```bash
uv run python scripts/acceptance_v0.py                          # structural only
AIRL_ACCEPTANCE_QUERY="attention" uv run python scripts/acceptance_v0.py
```

The structural checks are **data-independent**: registry, manifest and category
counts must agree with each other, every file the projection manifest claims must
exist on disk, and the vault landmarks must be present. They hold for whatever
sources happen to exist, so the result is reproducible on any machine.

The live search smoke is optional and reads its query from
`AIRL_ACCEPTANCE_QUERY`. An empty result is reported `SKIPPED`, never `FAIL` — an
empty library is not a defect in the Bridge.

> **What it does not prove.** That no write reaches Zotero. That claim still rests
> on reading the code (finding **H3**); proving it needs a `MockTransport` that
> raises on any non-`GET` method, driven through the whole sync flow, plus a
> static check in CI. The script says so in its own output under
> `not_proven_here`.

## Obsidian vault lint

The vault is the human knowledge workspace, and until the 2026-08-22 pass nothing
checked it. `check_vault.py` runs in the verification bundle against the
versioned baseline, and can be pointed at the live vault:

```bash
python3 scripts/check_vault.py                                    # the baseline
python3 scripts/check_vault.py "/home/otonom/Documents/Obsidian Vault"
python3 scripts/vault_frontmatter.py --write <vault>               # regenerate _meta/taxonomy.md
```

It checks that every wikilink and every intra-vault markdown link resolves, that
every projected page carries the Obsidian frontmatter its queries need **and
names the canonical file it projects**, that every `aethrion/` tag is in the
controlled vocabulary, that no page is unreachable, and that `_meta/taxonomy.md`
matches its generator.

> **What it cannot see.** Whether any note is worth reading. It reports the graph
> is well-formed, which is a different claim.

The mirrors inject that frontmatter at projection time — the repository keeps its
own `| Field | Value |` document header and gains nothing Obsidian-specific. The
derivation lives in `scripts/vault_frontmatter.py` and reads no wall clock, so a
mirror run that changes nothing rewrites nothing.

## Obsidian mirror integrity

The plan mirror, the skills mirror and the architecture/review mirrors in the
vault are **generated**. Verify they have not drifted:

```bash
V="/home/otonom/Documents/Obsidian Vault/10 - Projects/AETHRION"
python scripts/mirror_plan.py  "$V/01 - Commissioning" --check
python scripts/mirror_vault.py "$V" --check
```

Both must report `0 drift entries`. To regenerate after a canonical change, run
the same commands without `--check`.

> Edits made directly in a generated area are lost on the next regeneration, and
> the plan seal does not cover the mirror — so drift there is invisible unless you
> run this check.

## The verification bundle

Everything that currently produces real evidence, in one place:

```bash
uv run pytest                                              # 93 tests
(cd planning/commissioning && sha256sum -c 00_PROGRAM/SHA256SUMS.txt)
uv run python scripts/mcp_smoke.py
uv run python scripts/acceptance_v0.py
python3 scripts/validate_skills.py                         # 52 skills, format + metadata
python3 scripts/make_figures.py --check                    # generators match, and text fits its box
python3 scripts/validate_commissioning_plan.py             # plan references, phases and DAG
python3 scripts/make_plan_indexes.py --check                # workstream indexes
python3 scripts/check_doc_consistency.py                   # declared counts vs reality
python3 scripts/check_stale_claims.py                      # prose the repository has outgrown
uv run python scripts/write_status.py                      # regenerate docs/STATUS.md
uv run python scripts/evidence_manifest.py verify \
    --manifest delivery/WP-000/evidence.dsse.json --tamper-demo
python scripts/mirror_plan.py  "$V/01 - Commissioning" --check
python scripts/mirror_vault.py "$V" --check
```

Expected: `93 passed` · `554` OK · five MCP tools · 11 acceptance checks ·
`52 skills` conform · `14 figures, 0 drift, 0 overflow` · `plan semantics OK` ·
`0 drift entries`
twice (plan and vault mirrors, 0 drift).

The first six are written as a push-triggered control, **BVC-01**
(`deploy/bvc-01-verify.yml`), but it is **staged and not active** — activation
needs a workflow-scoped token; see `architecture/ADR-002_bootstrap_verification_control.md` §6.

⚠️ **The rest still run by hand,** and deliberately so: `mcp_smoke.py` and
`acceptance_v0.py` need a live Bridge and a local Zotero library, and the mirror
checks need the operator's vault. BVC-01 records that omission in its own output
rather than hiding it, and **it does not close finding H5** — H5 is the absence
of the WP-024 CI platform.

## After a path change

If the repository moves, three things break and must be repaired together:

1. **venv console scripts** — shebangs carry absolute paths
2. **The editable install** — `.venv/lib/*/site-packages/_editable_impl_*.pth`
3. **systemd units and the Hermes config** — absolute paths in both

Symptom of missing (2): `ModuleNotFoundError: No module named 'airl_bridge'`
while `python -m` still works.
