# AIRL Bridge API

Local-first bridge for the first AIRL literature vertical slice:

```text
Zotero Local API (read-only)
        -> SQLite canonical source registry
        -> Obsidian 70 - Literatür Setleri/Zotero Kaynakları projections
```

The V0 service binds only to `127.0.0.1`. It does not accept a Zotero API key
and contains no Zotero write operation.

## Install

```bash
cd /home/otonom/Desktop/FH/AIRL_OS_DEVREYE_ALMA_PLANI_v1.0/airl_bridge_api
uv sync --extra dev
```

The local `.env` is already configured for:

- Zotero Local API: `http://127.0.0.1:23119/api`
- personal local library: `users/0`
- Obsidian vault: `/home/otonom/Documents/Obsidian Vault`
- generated notes: `70 - Literatür Setleri/Zotero Kaynakları`
- Bridge API: `http://127.0.0.1:8765`

## Enable Zotero Local API

1. Start Zotero.
2. Open **Settings -> Advanced -> General**.
3. Enable **Allow other applications on this computer to communicate with Zotero**.
4. Keep port `23119` local; do not forward or expose it.

Check all components:

```bash
uv run airl-bridge doctor
```

## Start the API

```bash
uv run airl-bridge serve
```

The installed user service can be managed with:

```bash
systemctl --user status airl-bridge.service
systemctl --user restart airl-bridge.service
journalctl --user -u airl-bridge.service -n 50
```

The user timer performs the same local synchronization every 30 minutes:

```bash
systemctl --user status airl-bridge-sync.timer
systemctl --user list-timers airl-bridge-sync.timer
journalctl --user -u airl-bridge-sync.service -n 50
```

Useful local URLs:

- Health: <http://127.0.0.1:8765/health>
- Readiness: <http://127.0.0.1:8765/ready>
- OpenAPI UI: <http://127.0.0.1:8765/docs>

## First synchronization

With the server running:

```bash
curl -X POST 'http://127.0.0.1:8765/v1/sync?limit=100'
curl 'http://127.0.0.1:8765/v1/sources?limit=10'
```

Or without starting the server:

```bash
uv run airl-bridge sync --limit 100
```

Repeated sync is idempotent for the same Zotero library/item key. Zotero-derived
files live under the automatically managed `Zotero Kaynakları` branch and are
overwritten from the canonical registry. Human synthesis lives in
`20 - Kaynak Notları`; curated literature-set notes live directly in
`70 - Literatür Setleri`. Sources are grouped into readable Turkish
publication-type folders. File names begin with the Zotero title; only same-title
collisions receive a stable `Zotero ITEMKEY` suffix.

## Test

```bash
uv run pytest
uv run python scripts/mcp_smoke.py
uv run python scripts/acceptance_v0.py
```

See [V0 architecture](docs/ARCHITECTURE_V0.md) and the
[operations guide](docs/OPERATIONS.md) for boundaries, recovery, and routine
checks.

## Hermes MCP access

Hermes starts `airl-bridge-mcp` over stdio. The server exposes only five
read-only tools: status, source search, source detail, category counts, and
possible-duplicate reporting. It exposes no synchronization, write, delete,
or Zotero mutation tool. The Hermes configuration also pins an explicit
five-tool include list and disables MCP prompts and resources for this server.
