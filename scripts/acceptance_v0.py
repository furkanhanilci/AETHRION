from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx

from airl_bridge.config import Settings
from airl_bridge.obsidian import MANIFEST_NAME


BASE_URL = "http://127.0.0.1:8765"


def get(path: str, **params: Any) -> Any:
    response = httpx.get(f"{BASE_URL}{path}", params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    settings = Settings.from_env()
    generated = settings.obsidian_vault / settings.obsidian_generated_dir
    dashboard = generated / "00 - Control Dashboard"
    home = settings.obsidian_vault / "00 - Home/ai_research_framework_home.md"
    literature_index = (
        settings.obsidian_vault / "70 - Literature Sets/literature_sets.md"
    )

    health = get("/health")
    ready = get("/ready")
    categories = get("/v1/categories")
    lidar_results = get("/v1/sources/search", q="LiDAR", limit=2)

    require(health["zotero_write_enabled"] is False, "Zotero write must be off")
    require(ready["status"] == "ready", "Bridge is not ready")
    require(ready["zotero"] == "reachable", "Zotero is not reachable")
    require(home.is_file(), "AI Research Framework main page is missing")
    require(literature_index.is_file(), "Literature-set index is missing")
    require(not (settings.obsidian_vault / "80_Generated").exists(), "Legacy tree remains")
    require((dashboard / "Source Catalog.md").is_file(), "Catalog is missing")
    require((dashboard / "Potential Duplicates.md").is_file(), "Duplicate report is missing")
    require(bool(lidar_results), "Source search returned no LiDAR result")

    manifest_path = generated / MANIFEST_NAME
    require(manifest_path.is_file(), "Projection manifest is missing")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    generated_files = manifest["generated_files"]
    require(
        len(generated_files) == ready["source_count"],
        "Manifest/source registry count mismatch",
    )
    require(
        all((generated / relative).is_file() for relative in generated_files),
        "A projected source file is missing",
    )
    require(
        sum(category["source_count"] for category in categories)
        == ready["source_count"],
        "Category/source registry count mismatch",
    )

    print(
        json.dumps(
            {
                "status": "accepted",
                "source_count": ready["source_count"],
                "category_count": len(categories),
                "generated_directory": str(generated),
                "main_page": str(home),
                "zotero_write_enabled": False,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
