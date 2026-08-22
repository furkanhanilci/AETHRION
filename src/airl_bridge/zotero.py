"""The Zotero Local API client — the read-only boundary of the system.

**Invariant: this module performs no write.** There is no API key, no ``post``,
``put``, ``patch`` or ``delete`` call, and no code path that mutates a Zotero
record. That is the framework's strongest security claim.

⚠️ **It is not proven by a test.** The ``zotero_write_enabled`` field reported by
``/health`` is a hard-coded constant, so the three artifacts that appear to
verify this claim are testing ``False is False`` (audit finding **H3**). The
real check would be a ``MockTransport`` that raises on any method other than
``GET``, driven through the whole ``sync`` flow, plus a static check in CI.

⚠️ **Coverage limit (finding H1).** ``fetch_top_items`` issues a single
``GET /items/top`` call capped at 100 records. There is no ``start`` pagination,
no reading of the ``Total-Results`` header and no ``since=`` incremental
parameter. Beyond 100 sources the sync becomes **silently partial** — the run is
still recorded as ``SUCCEEDED``.

The ``airl_id`` is derived from the Zotero binding, not the title, so the
identity survives a title edit. It is a 64-bit truncated hash with no collision
handling (finding **L2**).
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any

import httpx

from .config import Settings
from .models import SourceRecord


SKIPPED_ITEM_TYPES = {"attachment", "note", "annotation"}


class ZoteroUnavailable(RuntimeError):
    pass


class InvalidZoteroItem(ValueError):
    pass


class ZoteroClient:
    def __init__(
        self, settings: Settings, transport: httpx.AsyncBaseTransport | None = None
    ):
        self.settings = settings
        self.transport = transport

    @property
    def library_url(self) -> str:
        return (
            f"{self.settings.zotero_base_url}/"
            f"{self.settings.zotero_library_type}/"
            f"{self.settings.zotero_library_id}"
        )

    async def fetch_top_items(self, limit: int = 100) -> list[dict[str, Any]]:
        safe_limit = max(1, min(limit, 100))
        headers = {"Zotero-API-Version": "3"}
        try:
            async with httpx.AsyncClient(
                transport=self.transport, timeout=5.0, headers=headers
            ) as client:
                response = await client.get(
                    f"{self.library_url}/items/top",
                    params={"limit": safe_limit, "format": "json"},
                )
                response.raise_for_status()
        except (httpx.HTTPError, OSError) as exc:
            raise ZoteroUnavailable(
                f"Zotero Local API is unavailable at {self.library_url}: {exc}"
            ) from exc
        payload = response.json()
        if not isinstance(payload, list):
            raise ZoteroUnavailable("Zotero Local API returned a non-list response")
        return payload

    async def ping(self) -> bool:
        await self.fetch_top_items(limit=1)
        return True


def normalize_item(
    raw: dict[str, Any], settings: Settings
) -> tuple[SourceRecord, dict[str, Any]]:
    data = raw.get("data")
    if not isinstance(data, dict):
        raise InvalidZoteroItem("item has no data object")
    zotero_key = str(raw.get("key") or data.get("key") or "").strip()
    if not zotero_key:
        raise InvalidZoteroItem("item has no Zotero key")
    item_type = str(data.get("itemType") or "unknown")
    if item_type in SKIPPED_ITEM_TYPES:
        raise InvalidZoteroItem(f"item type {item_type} is not a top-level source")

    binding = (
        f"zotero:{settings.zotero_library_type}:"
        f"{settings.zotero_library_id}:{zotero_key}"
    )
    airl_id = "SRC-ZOT-" + hashlib.sha256(binding.encode("utf-8")).hexdigest()[:16].upper()
    canonical_payload = {
        "item_type": item_type,
        "title": str(data.get("title") or "Untitled source"),
        "creators": data.get("creators") or [],
        "publication_date": str(data.get("date") or ""),
        "doi": str(data.get("DOI") or "").strip().lower(),
        "url": str(data.get("url") or "").strip(),
        "abstract_note": str(data.get("abstractNote") or ""),
        "tags": data.get("tags") or [],
    }
    encoded = json.dumps(
        canonical_payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return (
        SourceRecord(
            airl_id=airl_id,
            zotero_library_type=settings.zotero_library_type,
            zotero_library_id=settings.zotero_library_id,
            zotero_key=zotero_key,
            zotero_version=int(raw.get("version") or data.get("version") or 0),
            content_hash="sha256:" + hashlib.sha256(encoded).hexdigest(),
            synced_at=datetime.now(timezone.utc),
            **canonical_payload,
        ),
        raw,
    )
