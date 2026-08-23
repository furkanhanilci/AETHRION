"""The Zotero Local API client — the read-only boundary of the system.

**Invariant: this module performs no write.** There is no API key, no ``post``,
``put``, ``patch`` or ``delete`` call, and no code path that mutates a Zotero
record. That is the framework's strongest security claim.

⚠️ **It is not proven by a test.** The ``zotero_write_enabled`` field reported by
``/health`` is a hard-coded constant, so the three artifacts that appear to
verify this claim are testing ``False is False`` (audit finding **H3**). The
real check would be a ``MockTransport`` that raises on any method other than
``GET``, driven through the whole ``sync`` flow, plus a static check in CI.

``fetch_top_items`` paginates and returns ``(items, complete)`` — finding **H1**,
closed. The second element is what matters: it says whether the walk reached the
end, and the deletion reconciliation added for **H2** refuses to run without it.
Reconciling a library against a quarter of itself would withdraw the other three
quarters, which is why the register said to fix **M9** before **H1**.

The ``airl_id`` is derived from the Zotero binding, not the title, so the
identity survives a title edit. It is a 64-bit truncated digest, and
``normalize_item`` now carries the full binding so a collision is **detected**
rather than silently merging two sources (finding **L2**).
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any

import httpx

from airl_framework.contracts import content_digest

from .config import Settings
from .models import SourceRecord


SKIPPED_ITEM_TYPES = {"attachment", "note", "annotation"}


class ZoteroUnavailable(RuntimeError):
    pass


class InvalidZoteroItem(ValueError):
    pass


class ZoteroClient:
    # A guard against an upstream that never returns a short page. Chosen far
    # above any plausible personal library so it is a runaway backstop, not a
    # cap: a cap that silently truncates is the defect this replaced.
    MAX_ITEMS = 200_000

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

    PAGE_SIZE = 100

    async def _get(self, client: httpx.AsyncClient, path: str,
                   params: dict[str, Any]) -> httpx.Response:
        try:
            response = await client.get(f"{self.library_url}{path}", params=params)
            response.raise_for_status()
        except (httpx.HTTPError, OSError) as exc:
            raise ZoteroUnavailable(
                f"Zotero Local API is unavailable at {self.library_url}: {exc}"
            ) from exc
        return response

    async def fetch_top_items(
        self, limit: int | None = None
    ) -> tuple[list[dict[str, Any]], bool]:
        """Every top-level item, paginated — finding H1.

        Returns `(items, complete)`. **`complete` is the point.** The previous
        version issued one `GET /items/top` capped at 100 and returned a list, so
        a library of 400 sources produced 100 records and a run recorded as
        `SUCCEEDED`. Nothing anywhere could tell a full sync from a quarter of
        one, which is why the deletion reconciliation added for H2 must refuse to
        run on a partial fetch: reconciling against a quarter of a library would
        withdraw three quarters of it.

        `Total-Results` is read where the server sends it and used only as a
        cross-check. Zotero's local API does not always send it, and a client
        that *requires* a header to know it has finished stops working the day
        the header stops arriving. Termination is decided by a short page.
        """
        headers = {"Zotero-API-Version": "3"}
        items: list[dict[str, Any]] = []
        total: int | None = None
        start = 0
        async with httpx.AsyncClient(
            transport=self.transport, timeout=5.0, headers=headers
        ) as client:
            while True:
                want = self.PAGE_SIZE
                if limit is not None:
                    want = min(self.PAGE_SIZE, limit - len(items))
                    if want <= 0:
                        break
                response = await self._get(client, "/items/top", {
                    "limit": want, "start": start, "format": "json"})
                payload = response.json()
                if not isinstance(payload, list):
                    raise ZoteroUnavailable(
                        "Zotero Local API returned a non-list response")
                if total is None and "Total-Results" in response.headers:
                    try:
                        total = int(response.headers["Total-Results"])
                    except ValueError:
                        total = None
                items.extend(payload)
                if len(payload) < want:
                    break
                start += len(payload)
                if start > self.MAX_ITEMS:
                    raise ZoteroUnavailable(
                        f"pagination exceeded {self.MAX_ITEMS} items without a "
                        f"short page — refusing to loop indefinitely")

        # Complete means "we walked to the end", not "we asked for everything".
        complete = limit is None or len(items) < limit
        if total is not None and complete and len(items) != total:
            raise ZoteroUnavailable(
                f"Zotero reported Total-Results={total} but pagination yielded "
                f"{len(items)} items — refusing to treat a partial walk as "
                f"complete, because a deletion reconciliation would then "
                f"withdraw the difference")
        return items, complete

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
            # Minted through the contract core, not beside it — finding H4.
            # The two used to define "a digest" differently and nothing imported
            # anything, so neither could discover the disagreement.
            content_hash=content_digest(encoded),
            synced_at=datetime.now(timezone.utc),
            **canonical_payload,
        ),
        raw,
    )
