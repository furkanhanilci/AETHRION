from pathlib import Path

import pytest

from airl_bridge.config import Settings


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    vault = tmp_path / "vault"
    vault.mkdir()
    return Settings(
        api_host="127.0.0.1",
        api_port=8765,
        database_path=tmp_path / "bridge.sqlite3",
        zotero_base_url="http://127.0.0.1:23119/api",
        zotero_library_type="users",
        zotero_library_id="0",
        obsidian_vault=vault,
        obsidian_generated_dir=Path("70 - Literature Sets/Zotero Sources"),
    )


@pytest.fixture
def zotero_item() -> dict:
    return {
        "key": "ABCD1234",
        "version": 7,
        "data": {
            "key": "ABCD1234",
            "version": 7,
            "itemType": "journalArticle",
            "title": "A reproducible source",
            "creators": [
                {"creatorType": "author", "firstName": "Ada", "lastName": "Lovelace"}
            ],
            "date": "2026",
            "DOI": "10.1234/EXAMPLE",
            "url": "https://example.test/paper",
            "abstractNote": "An abstract.",
            "tags": [{"tag": "airl", "type": 1}],
        },
    }
