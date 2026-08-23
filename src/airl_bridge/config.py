"""Configuration loading and the two boundaries it enforces.

Settings come from the environment, seeded from ``.env`` at the project root.
Two of the checks in this module are **security boundaries**, not conveniences:

1. ``api_host`` must be a loopback address. The service refuses to start
   otherwise. This is a fail-closed default: the V0 Bridge has no
   authentication (audit finding **M1**), so binding it to a routable interface
   would expose the whole literature registry unauthenticated.
2. ``AIRL_OBSIDIAN_GENERATED_DIR`` must be a *relative* path containing no
   ``..`` segment. The projection deletes every file registered in its own
   manifest (see :mod:`airl_bridge.obsidian`); a path that escaped the vault
   would make that deletion escape with it.

Neither check has a negative test today (finding **L4**). They hold because the
code says so, not because anything proves it.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key.startswith("AIRL_"):
            os.environ.setdefault(key, value)


def _resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path.resolve()


@dataclass(frozen=True)
class Settings:
    api_host: str
    api_port: int
    database_path: Path
    zotero_base_url: str
    zotero_library_type: str
    zotero_library_id: str
    obsidian_vault: Path
    obsidian_generated_dir: Path
    # Finding M1. `api_token` gates the three mutating endpoints; `allowed_hosts`
    # is checked against the request's Host header. Both default to values that
    # are safe rather than convenient — an unset token means the mutating
    # endpoints refuse, not that they are open.
    api_token: str
    allowed_hosts: tuple[str, ...]

    @classmethod
    def from_env(cls) -> "Settings":
        _load_dotenv(PROJECT_ROOT / ".env")
        api_host = os.getenv("AIRL_API_HOST", "127.0.0.1")
        if api_host not in {"127.0.0.1", "::1", "localhost"}:
            raise ValueError("V0 Bridge API may only listen on the local loopback interface")
        vault = _resolve_path(
            os.getenv("AIRL_OBSIDIAN_VAULT", str(PROJECT_ROOT / "vault"))
        )
        generated_rel = Path(
            os.getenv(
                "AIRL_OBSIDIAN_GENERATED_DIR",
                "70 - Literature Sets/Zotero Sources",
            )
        )
        if generated_rel.is_absolute() or ".." in generated_rel.parts:
            raise ValueError(
                "AIRL_OBSIDIAN_GENERATED_DIR must be a safe path relative to the vault"
            )
        library_type = os.getenv("AIRL_ZOTERO_LIBRARY_TYPE", "users")
        if library_type not in {"users", "groups"}:
            raise ValueError("AIRL_ZOTERO_LIBRARY_TYPE must be users or groups")
        return cls(
            api_host=api_host,
            api_port=int(os.getenv("AIRL_API_PORT", "8765")),
            database_path=_resolve_path(
                os.getenv("AIRL_DATABASE_PATH", "./data/airl_bridge.sqlite3")
            ),
            zotero_base_url=os.getenv(
                "AIRL_ZOTERO_BASE_URL", "http://127.0.0.1:23119/api"
            ).rstrip("/"),
            zotero_library_type=library_type,
            zotero_library_id=os.getenv("AIRL_ZOTERO_LIBRARY_ID", "0"),
            obsidian_vault=vault,
            obsidian_generated_dir=generated_rel,
            api_token=os.getenv("AIRL_API_TOKEN", "").strip(),
            allowed_hosts=tuple(
                h.strip() for h in os.getenv(
                    "AIRL_ALLOWED_HOSTS",
                    "127.0.0.1,localhost,[::1]",
                ).split(",") if h.strip()
            ),
        )
