# Operations Guide

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
cd /home/otonom/Desktop/FH/AI_RESEARCH_FRAMEWORK
.venv/bin/python scripts/mcp_smoke.py
```

The `tools.include` list in the Hermes configuration must contain exactly five
tools. `prompts` and `resources` must remain disabled.

> ⚠️ `mcp_smoke.py` currently reports `isError` without asserting on it, so it
> exits 0 even when every call fails. Read its output; do not treat exit status
> as a pass. See finding **M2**.

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

## After a path change

If the repository moves, three things break and must be repaired together:

1. **venv console scripts** — shebangs carry absolute paths
2. **The editable install** — `.venv/lib/*/site-packages/_editable_impl_*.pth`
3. **systemd units and the Hermes config** — absolute paths in both

Symptom of missing (2): `ModuleNotFoundError: No module named 'airl_bridge'`
while `python -m` still works.
