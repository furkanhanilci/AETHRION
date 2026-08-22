from __future__ import annotations

import os
from typing import Any
from urllib.parse import quote

import httpx
from mcp.server.fastmcp import FastMCP


DEFAULT_BRIDGE_URL = "http://127.0.0.1:8765"
BRIDGE_TIMEOUT_SECONDS = 8.0


def _bridge_url() -> str:
    return os.environ.get("AIRL_BRIDGE_BASE_URL", DEFAULT_BRIDGE_URL).rstrip("/")


def _get(path: str, *, params: dict[str, Any] | None = None) -> Any:
    try:
        response = httpx.get(
            f"{_bridge_url()}{path}",
            params=params,
            timeout=BRIDGE_TIMEOUT_SECONDS,
        )
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        detail = exc.response.text[:500]
        raise RuntimeError(
            f"AIRL Bridge request failed ({exc.response.status_code}): {detail}"
        ) from exc
    except httpx.HTTPError as exc:
        raise RuntimeError(f"AIRL Bridge is unreachable: {exc}") from exc
    return response.json()


def _creator_name(creator: dict[str, Any]) -> str:
    if creator.get("name"):
        return str(creator["name"])
    return " ".join(
        part
        for part in (str(creator.get("firstName", "")), str(creator.get("lastName", "")))
        if part
    ).strip()


def _compact_source(source: dict[str, Any]) -> dict[str, Any]:
    return {
        "airl_id": source.get("airl_id", ""),
        "title": source.get("title", ""),
        "authors": [
            name
            for creator in source.get("creators", [])
            if (name := _creator_name(creator))
        ],
        "publication_date": source.get("publication_date", ""),
        "doi": source.get("doi", ""),
        "item_type": source.get("item_type", ""),
        "zotero_key": source.get("zotero_key", ""),
        "tags": [
            str(tag.get("tag", ""))
            for tag in source.get("tags", [])
            if tag.get("tag")
        ],
    }


def bridge_status() -> dict[str, Any]:
    """Return the operating status of AIRL Bridge, the Zotero connection and the record count."""
    health = _get("/health")
    ready = _get("/ready")
    return {
        "status": ready.get("status"),
        "version": health.get("version"),
        "zotero": ready.get("zotero"),
        "obsidian_vault_ready": ready.get("obsidian_vault"),
        "source_count": ready.get("source_count"),
        "zotero_write_enabled": health.get("zotero_write_enabled", False),
    }


def search_sources(query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Search Zotero sources across title, abstract, DOI, tags and authors."""
    query = query.strip()
    if len(query) < 2:
        raise ValueError("The search query must be at least two characters long.")
    bounded_limit = max(1, min(limit, 25))
    sources = _get("/v1/sources/search", params={"q": query, "limit": bounded_limit})
    return [_compact_source(source) for source in sources]


def get_source(airl_id: str) -> dict[str, Any]:
    """Return the details of a single source identified by its AIRL identifier."""
    source = _get(f"/v1/sources/{quote(airl_id.strip(), safe='')}")
    result = _compact_source(source)
    result.update(
        {
            "abstract": source.get("abstract_note", ""),
            "url": source.get("url", ""),
            "zotero_library_type": source.get("zotero_library_type", ""),
            "zotero_library_id": source.get("zotero_library_id", ""),
            "synced_at": source.get("synced_at", ""),
        }
    )
    return result


def list_categories() -> list[dict[str, Any]]:
    """List source types with their category names and record counts."""
    return _get("/v1/categories")


def list_possible_duplicates(limit_groups: int = 20) -> list[dict[str, Any]]:
    """List, read-only, the groups of possible duplicate sources sharing a normalised title."""
    bounded_limit = max(1, min(limit_groups, 50))
    groups = _get("/v1/duplicates")[:bounded_limit]
    return [
        {
            "normalized_title": group.get("normalized_title", ""),
            "source_count": group.get("source_count", 0),
            "sources": [_compact_source(source) for source in group.get("sources", [])],
        }
        for group in groups
    ]


mcp = FastMCP("AIRL Bridge")
mcp.tool()(bridge_status)
mcp.tool()(search_sources)
mcp.tool()(get_source)
mcp.tool()(list_categories)
mcp.tool()(list_possible_duplicates)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
