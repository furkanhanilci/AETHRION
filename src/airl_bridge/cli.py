"""The ``airl-bridge`` command-line entry point.

Subcommands: ``doctor`` (environment and Zotero reachability), ``serve`` (run the
API), ``sync`` (ingest plus projection without starting the server), ``ingest``
and ``project``.

``sync`` exists so the systemd timer does not have to depend on the HTTP surface
— but the installed timer currently calls ``POST /v1/sync`` anyway, so the
service must be running for periodic sync to work.

⚠️ The ``--limit`` choices are bounded at 100, mirroring the Zotero client cap
(finding **H1**). When pagination lands, this bound must be removed with it.
"""
from __future__ import annotations

import argparse
import asyncio
import json
from typing import Sequence

import uvicorn

from .config import Settings
from .database import Database
from .obsidian import ObsidianProjector
from .service import BridgeService
from .zotero import ZoteroClient


def _components(settings: Settings) -> tuple[Database, ZoteroClient, BridgeService]:
    database = Database(settings.database_path)
    database.initialize()
    zotero = ZoteroClient(settings)
    service = BridgeService(database, zotero, ObsidianProjector(settings))
    return database, zotero, service


async def _doctor(settings: Settings) -> int:
    database, zotero, _ = _components(settings)
    report: dict[str, object] = {
        "database": {"status": "ok", "path": str(database.path)},
        "obsidian": {
            "status": "ok" if settings.obsidian_vault.is_dir() else "missing",
            "vault": str(settings.obsidian_vault),
        },
        "zotero": {"status": "checking", "url": zotero.library_url},
        "zotero_write_enabled": False,
    }
    exit_code = 0
    try:
        await zotero.ping()
        report["zotero"] = {"status": "ok", "url": zotero.library_url}
    except Exception as exc:
        report["zotero"] = {
            "status": "unavailable",
            "url": zotero.library_url,
            "error": str(exc),
        }
        exit_code = 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return exit_code


async def _sync(settings: Settings, limit: int) -> int:
    _, _, service = _components(settings)
    result = await service.sync(limit=limit)
    print(json.dumps(result.model_dump(mode="json"), ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="airl-bridge")
    subparsers = parser.add_subparsers(dest="command", required=True)

    serve = subparsers.add_parser("serve", help="Start the local Bridge API")
    serve.add_argument("--reload", action="store_true")

    subparsers.add_parser("doctor", help="Check database, Zotero and Obsidian")

    sync = subparsers.add_parser("sync", help="Ingest Zotero and project Obsidian")
    sync.add_argument("--limit", type=int, default=100, choices=range(1, 101))
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    settings = Settings.from_env()
    if args.command == "serve":
        uvicorn.run(
            "airl_bridge.main:app",
            host=settings.api_host,
            port=settings.api_port,
            reload=args.reload,
        )
        return
    if args.command == "doctor":
        raise SystemExit(asyncio.run(_doctor(settings)))
    if args.command == "sync":
        raise SystemExit(asyncio.run(_sync(settings, args.limit)))
    raise SystemExit(2)
