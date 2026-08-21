from __future__ import annotations

from typing import Any

import pytest

from airl_bridge import mcp_server


SOURCE: dict[str, Any] = {
    "airl_id": "zotero-users-0-ABC123",
    "title": "Test Makalesi",
    "creators": [{"firstName": "Ada", "lastName": "Lovelace"}],
    "publication_date": "2026",
    "doi": "10.1234/test",
    "item_type": "journalArticle",
    "zotero_key": "ABC123",
    "tags": [{"tag": "AIRL"}],
    "abstract_note": "Özet",
    "url": "https://example.test/article",
    "zotero_library_type": "users",
    "zotero_library_id": "0",
    "synced_at": "2026-08-21T12:00:00Z",
}


def test_search_sources_returns_compact_records(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_get(path: str, *, params: dict[str, Any] | None = None) -> Any:
        assert path == "/v1/sources/search"
        assert params == {"q": "AIRL", "limit": 25}
        return [SOURCE]

    monkeypatch.setattr(mcp_server, "_get", fake_get)

    result = mcp_server.search_sources(" AIRL ", limit=999)

    assert result == [
        {
            "airl_id": "zotero-users-0-ABC123",
            "title": "Test Makalesi",
            "authors": ["Ada Lovelace"],
            "publication_date": "2026",
            "doi": "10.1234/test",
            "item_type": "journalArticle",
            "zotero_key": "ABC123",
            "tags": ["AIRL"],
        }
    ]


def test_search_sources_rejects_too_short_query() -> None:
    with pytest.raises(ValueError, match="en az iki"):
        mcp_server.search_sources("x")


def test_get_source_adds_details(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(mcp_server, "_get", lambda path: SOURCE)

    result = mcp_server.get_source("zotero-users-0-ABC123")

    assert result["abstract"] == "Özet"
    assert result["url"] == "https://example.test/article"


def test_possible_duplicates_are_bounded(monkeypatch: pytest.MonkeyPatch) -> None:
    groups = [
        {"normalized_title": f"title-{index}", "source_count": 2, "sources": [SOURCE]}
        for index in range(60)
    ]
    monkeypatch.setattr(mcp_server, "_get", lambda path: groups)

    result = mcp_server.list_possible_duplicates(limit_groups=999)

    assert len(result) == 50
    assert "abstract" not in result[0]["sources"][0]
