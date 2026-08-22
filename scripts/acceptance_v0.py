"""End-to-end acceptance check for the Literature Bridge V0.

Closes audit finding **M3**, and stops asserting finding **H3**.

**What changed and why.** The previous version failed unless the user's personal
Zotero library happened to contain a paper matching the hard-coded term
"LiDAR" — so "acceptance" passed only on one machine with one library, and would
turn red if the user deleted those papers. It also asserted
``health["zotero_write_enabled"] is False``, which is a **hard-coded constant**:
that check is a tautology (``False is False``) and would stay green even if a
write path were added tomorrow. Asserting it was worse than not asserting it,
because it created the appearance of evidence.

This version is split in two:

* **Structural checks (always required).** Registry, manifest and category counts
  must agree, every projected file must exist, and the vault landmarks must be
  present. None of this depends on *which* sources exist — only on the invariants
  holding for whatever is there. This part is reproducible on any machine.
* **A live search smoke (optional).** The query comes from
  ``AIRL_ACCEPTANCE_QUERY``. An empty result is reported ``SKIPPED``, never
  ``FAIL`` — an empty library is not a defect in the Bridge.

**What this check still does not prove.** That no write reaches Zotero. That
requires a behavioural test — a ``MockTransport`` raising on any method other
than ``GET``, driven through the whole sync flow — plus a static check in CI.
Neither exists yet (finding **H3**), so the read-only claim remains verified by
reading the code, not by evidence.

Requires the Bridge to be running. Exits non-zero on failure.

Usage:
    uv run python scripts/acceptance_v0.py
    AIRL_ACCEPTANCE_QUERY="attention" uv run python scripts/acceptance_v0.py
"""
from __future__ import annotations

import json
import os
import sys
from typing import Any

import httpx

from airl_bridge.config import Settings
from airl_bridge.obsidian import MANIFEST_NAME


BASE_URL = os.environ.get("AIRL_BRIDGE_BASE_URL", "http://127.0.0.1:8765").rstrip("/")

_failures: list[str] = []
_checks: list[dict[str, str]] = []


def get(path: str, **params: Any) -> Any:
    response = httpx.get(f"{BASE_URL}{path}", params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def check(name: str, condition: bool, detail: str = "") -> None:
    """Record a mandatory check. A failure does not stop the run.

    Collecting every failure rather than raising on the first one matters: a
    partial report hides which invariants also broke, and the whole point of an
    acceptance run is to know the full state.
    """
    _checks.append({"check": name, "result": "PASS" if condition else "FAIL",
                    "detail": detail})
    if not condition:
        _failures.append(f"{name}: {detail}" if detail else name)


def skip(name: str, detail: str) -> None:
    """Record a check that could not run — explicitly not a failure."""
    _checks.append({"check": name, "result": "SKIPPED", "detail": detail})


def main() -> int:
    settings = Settings.from_env()
    generated = settings.obsidian_vault / settings.obsidian_generated_dir
    dashboard = generated / "00 - Control Dashboard"
    home = settings.obsidian_vault / "00 - Home/aethrion_home.md"
    literature_index = (
        settings.obsidian_vault / "70 - Literature Sets/literature_sets.md"
    )

    # --- Service reachability -------------------------------------------------
    ready = get("/ready")
    check("service_ready", ready["status"] == "ready", str(ready))
    check("zotero_reachable", ready["zotero"] == "reachable", str(ready))

    # --- Vault landmarks ------------------------------------------------------
    check("home_page_present", home.is_file(), str(home))
    check("literature_index_present", literature_index.is_file(),
          str(literature_index))
    check("legacy_tree_removed",
          not (settings.obsidian_vault / "80_Generated").exists(),
          "the pre-rename generated tree must not reappear")
    check("source_catalog_present", (dashboard / "Source Catalog.md").is_file())
    check("duplicate_report_present",
          (dashboard / "Potential Duplicates.md").is_file())

    # --- Registry / manifest / projection agreement ---------------------------
    # These are the real invariants: three independent counts of the same set
    # must agree, and every file the manifest claims must exist on disk.
    manifest_path = generated / MANIFEST_NAME
    check("projection_manifest_present", manifest_path.is_file(),
          str(manifest_path))

    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        generated_files = manifest["generated_files"]
        check(
            "manifest_matches_registry_count",
            len(generated_files) == ready["source_count"],
            f"manifest={len(generated_files)} registry={ready['source_count']}",
        )
        missing = [rel for rel in generated_files if not (generated / rel).is_file()]
        check("every_projected_file_exists", not missing,
              f"missing={missing[:5]}")
    else:
        skip("manifest_matches_registry_count", "no manifest to compare")
        skip("every_projected_file_exists", "no manifest to compare")

    categories = get("/v1/categories")
    check(
        "category_counts_sum_to_registry",
        sum(c["source_count"] for c in categories) == ready["source_count"],
        f"categories={sum(c['source_count'] for c in categories)} "
        f"registry={ready['source_count']}",
    )

    # --- Optional live search smoke ------------------------------------------
    query = os.environ.get("AIRL_ACCEPTANCE_QUERY", "").strip()
    if not query:
        skip("live_search_smoke", "AIRL_ACCEPTANCE_QUERY not set")
    else:
        results = get("/v1/sources/search", q=query, limit=2)
        if results:
            check("live_search_smoke", True, f"query={query!r} hits={len(results)}")
        else:
            skip("live_search_smoke",
                 f"query={query!r} matched nothing — an empty library is not a defect")

    report = {
        "result": "accepted" if not _failures else "rejected",
        "source_count": ready["source_count"],
        "category_count": len(categories),
        "generated_directory": str(generated),
        "checks": _checks,
        "failures": _failures,
        "not_proven_here": [
            "the Zotero read-only boundary (finding H3 — needs a behavioural test)",
        ],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

    for failure in _failures:
        print(f"FAIL: {failure}", file=sys.stderr)
    return 1 if _failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
