"""The Obsidian projection: canonical registry → generated Markdown.

This module owns the most dangerous operation in the codebase — it **deletes
files inside the user's vault** — so its safety properties matter more than its
features:

* **Manifest-owned deletion.** Only files listed in
  ``.airl-projection-manifest.json`` are removed. A human note sitting in the
  same folder survives, and there is a real test for that
  (``tests/test_obsidian.py``). This is the primary defence against data loss.
* **Everything generated is in the manifest**, the two dashboards included. The
  rule cuts both ways: the projector removes nothing it did not record, and it
  records everything it writes, so a generated file it can no longer clean up
  cannot exist.
* **An unreadable manifest stops the run.** Parsing failure used to be swallowed
  and the manifest overwritten, which orphaned every file the old one listed.
  A projector that cannot read what it owns raises ``ProjectionError``.
* **Atomic writes.** ``mkstemp`` + ``fsync`` + ``os.replace`` — a partially
  written Markdown file cannot appear.
* **Path containment.** Every target path is resolved and checked to lie inside
  the vault before anything is written or removed.
* **Escaping.** Titles and abstracts pass through ``html.escape``; YAML string
  values are emitted via ``json.dumps``.

Known limitations:

* **No dry-run, and no refusal to adopt a populated directory (finding M7).** If
  ``AIRL_OBSIDIAN_GENERATED_DIR`` ever pointed at a human folder, the first run
  would generate there and write a manifest, and the second run would delete
  what that manifest lists. A path projected once is irreversibly taken under
  management.
* Generated notes carry no ``schema_version``, so they cannot be migrated later.
"""
from __future__ import annotations

import html
import json
import os
import re
import tempfile
import unicodedata
from collections import defaultdict
from pathlib import Path

from .catalog import duplicate_source_groups, source_category
from .config import Settings
from .models import ProjectionResult, SourceRecord


class ProjectionError(RuntimeError):
    pass


MANIFEST_NAME = ".airl-projection-manifest.json"
WINDOWS_RESERVED_NAMES = {
    "CON",
    "PRN",
    "AUX",
    "NUL",
    *(f"COM{number}" for number in range(1, 10)),
    *(f"LPT{number}" for number in range(1, 10)),
}


class ObsidianProjector:
    def __init__(self, settings: Settings):
        self.settings = settings

    def project_sources(self, sources: list[SourceRecord]) -> ProjectionResult:
        vault = self.settings.obsidian_vault.resolve()
        if not vault.is_dir():
            raise ProjectionError(f"Obsidian vault does not exist: {vault}")
        target_dir = (vault / self.settings.obsidian_generated_dir).resolve()
        try:
            target_dir.relative_to(vault)
        except ValueError as exc:
            raise ProjectionError("generated directory escapes the Obsidian vault") from exc
        target_dir.mkdir(parents=True, exist_ok=True)
        assignments = self._assign_paths(sources)
        current_paths: set[str] = set()
        for source, relative_path, category in assignments:
            target = target_dir / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            self._atomic_write(target, self._render(source, category))
            current_paths.add(relative_path.as_posix())
        # The dashboards are written *before* the manifest is sealed so they
        # enter it. A generated file outside the manifest is a file the
        # projector creates and can never clean up.
        generated_at = self._projection_timestamp(sources)
        dashboard_dir, dashboard_paths = self._write_dashboards(
            target_dir, assignments, generated_at
        )
        current_paths |= dashboard_paths
        removed_stale = self._remove_stale(target_dir, current_paths)
        self._write_manifest(target_dir, current_paths, generated_at)
        return ProjectionResult(
            projected=len(sources),
            directory=str(target_dir),
            removed_stale=removed_stale,
            dashboard_directory=str(dashboard_dir),
        )

    def _assign_paths(
        self, sources: list[SourceRecord]
    ) -> list[tuple[SourceRecord, Path, str]]:
        grouped: dict[tuple[str, str], list[SourceRecord]] = defaultdict(list)
        for source in sources:
            category = source_category(source.item_type)
            grouped[(category, self._filename_base(source.title))].append(source)

        assignments: list[tuple[SourceRecord, Path, str]] = []
        for (category, base), matching_sources in sorted(grouped.items()):
            duplicates = len(matching_sources) > 1
            for source in sorted(matching_sources, key=lambda item: item.zotero_key):
                suffix = f" — Zotero {source.zotero_key}" if duplicates else ""
                filename = self._filename_with_suffix(base, suffix)
                assignments.append((source, Path(category) / filename, category))
        return assignments

    @staticmethod
    def _filename_base(title: str) -> str:
        normalized = unicodedata.normalize("NFKC", " ".join(title.splitlines()))
        cleaned = re.sub(r'[<>:"/\\|?*\[\]\x00-\x1f]', " ", normalized)
        cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")
        if not cleaned:
            cleaned = "Untitled Source"
        if cleaned.upper() in WINDOWS_RESERVED_NAMES:
            cleaned = f"Kaynak - {cleaned}"
        return cleaned

    @classmethod
    def _filename_with_suffix(cls, base: str, suffix: str) -> str:
        extension = ".md"
        available_bytes = 200 - len((suffix + extension).encode("utf-8"))
        truncated = cls._truncate_utf8(base, max(40, available_bytes)).rstrip(" .")
        return f"{truncated}{suffix}{extension}"

    @staticmethod
    def _truncate_utf8(value: str, max_bytes: int) -> str:
        encoded = value.encode("utf-8")
        if len(encoded) <= max_bytes:
            return value
        truncated = encoded[:max_bytes]
        while truncated:
            try:
                return truncated.decode("utf-8")
            except UnicodeDecodeError:
                truncated = truncated[:-1]
        return "Untitled Source"

    def _remove_stale(self, target_dir: Path, current_paths: set[str]) -> int:
        manifest = target_dir / MANIFEST_NAME
        if not manifest.is_file():
            # No manifest yet: this directory has never been projected into, so
            # there is nothing this projector owns and nothing to remove.
            return 0
        try:
            payload = json.loads(manifest.read_text(encoding="utf-8"))
            previous_paths = set(payload.get("generated_files", []))
        except (OSError, json.JSONDecodeError, TypeError) as exc:
            # Refuse rather than continue. Swallowing this returned 0 and then
            # overwrote the manifest, which permanently orphaned every file the
            # unreadable manifest listed: no longer current, no longer tracked,
            # no longer removable. A projector that cannot read what it owns
            # must not write.
            raise ProjectionError(
                f"projection manifest is unreadable and will not be overwritten: "
                f"{manifest} ({exc}). Inspect it, then either repair it or remove "
                f"it deliberately to re-adopt this directory."
            ) from exc
        removed = 0
        for relative in sorted(previous_paths - current_paths):
            candidate = (target_dir / relative).resolve()
            try:
                candidate.relative_to(target_dir)
            except ValueError:
                continue
            if candidate.is_file() and candidate.suffix == ".md":
                candidate.unlink()
                removed += 1
                self._remove_empty_parents(candidate.parent, target_dir)
        return removed

    @staticmethod
    def _remove_empty_parents(directory: Path, root: Path) -> None:
        current = directory
        while current != root:
            try:
                current.rmdir()
            except OSError:
                return
            current = current.parent

    @staticmethod
    def _projection_timestamp(sources: list[SourceRecord]) -> str:
        """When the projected content was last current — not when it was written.

        Every generated file used to stamp ``datetime.now()``, so a run that
        changed nothing still rewrote the manifest and both dashboards. Deriving
        the stamp from the newest ``synced_at`` makes the whole projection a
        pure function of the registry: unchanged input, byte-identical output.
        """
        if not sources:
            return "1970-01-01T00:00:00+00:00"
        return max(source.synced_at for source in sources).isoformat()

    def _write_manifest(
        self, target_dir: Path, current_paths: set[str], generated_at: str
    ) -> None:
        payload = {
            "schema_version": 1,
            "generated_at": generated_at,
            "generated_files": sorted(current_paths),
        }
        self._atomic_write(
            target_dir / MANIFEST_NAME,
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        )

    def _write_dashboards(
        self,
        target_dir: Path,
        assignments: list[tuple[SourceRecord, Path, str]],
        generated_at: str,
    ) -> tuple[Path, set[str]]:
        vault = self.settings.obsidian_vault.resolve()
        dashboard_dir = (target_dir / "00 - Control Dashboard").resolve()
        try:
            dashboard_dir.relative_to(vault)
        except ValueError as exc:
            raise ProjectionError("dashboard directory escapes the Obsidian vault") from exc
        dashboard_dir.mkdir(parents=True, exist_ok=True)

        by_category: dict[
            str, list[tuple[SourceRecord, Path, str]]
        ] = defaultdict(list)
        for assignment in assignments:
            by_category[assignment[2]].append(assignment)

        catalog_lines = [
            "---",
            "airl_id: AIRL-GENERATED-SOURCE-CATALOG",
            "tags:",
            "  - aethrion/index",
            "  - aethrion/source",
            "  - aethrion/source-catalog",
            "type: generated-index",
            "cssclasses:",
            "  - aethrion-index",
            f'generated_at: {self._yaml_string(generated_at)}',
            "provenance: airl-bridge-api",
            "---",
            "",
            "# Source Catalog",
            "",
            "> [!warning] Generated projection",
            "> This file is regenerated by the Bridge API. Do not edit it by hand.",
            "",
            "| Category | Source count |",
            "|---|---:|",
        ]
        for category in sorted(by_category):
            catalog_lines.append(f"| {category} | {len(by_category[category])} |")
        for category in sorted(by_category):
            catalog_lines.extend(["", f"## {category}", ""])
            for source, relative_path, _ in sorted(
                by_category[category], key=lambda item: item[0].title.casefold()
            ):
                link = self._obsidian_link(relative_path)
                display = self._safe_link_display(source.title)
                catalog_lines.append(
                    f"- [[{link}|{display}]] — Zotero `{source.zotero_key}`"
                )

        sources = [assignment[0] for assignment in assignments]
        path_by_airl_id = {
            assignment[0].airl_id: assignment[1] for assignment in assignments
        }
        duplicate_lines = [
            "---",
            "airl_id: AIRL-GENERATED-POSSIBLE-DUPLICATES",
            "tags:",
            "  - aethrion/index",
            "  - aethrion/source",
            "  - aethrion/duplicate-review",
            "type: generated-quality-report",
            "cssclasses:",
            "  - aethrion-index",
            f'generated_at: {self._yaml_string(generated_at)}',
            "provenance: airl-bridge-api",
            "---",
            "",
            "# Potential Duplicates",
            "",
            "> [!important] Review required",
            "> This list only shows records sharing a normalised title. No Zotero record is merged or deleted automatically.",
        ]
        groups = duplicate_source_groups(sources)
        if not groups:
            duplicate_lines.extend(["", "No potential duplicates found."])
        for group in groups:
            duplicate_lines.extend(
                ["", f"## {html.escape(' '.join(group[0].title.splitlines()))}", ""]
            )
            for source in group:
                relative_path = path_by_airl_id[source.airl_id]
                link = self._obsidian_link(relative_path)
                doi = f" — DOI `{source.doi}`" if source.doi else ""
                duplicate_lines.append(
                    f"- [[{link}|Zotero {source.zotero_key}]]{doi}"
                )

        self._atomic_write(
            dashboard_dir / "Source Catalog.md", "\n".join(catalog_lines) + "\n"
        )
        self._atomic_write(
            dashboard_dir / "Potential Duplicates.md",
            "\n".join(duplicate_lines) + "\n",
        )
        written = {
            (dashboard_dir / name).relative_to(target_dir).as_posix()
            for name in ("Source Catalog.md", "Potential Duplicates.md")
        }
        return dashboard_dir, written

    def _obsidian_link(self, relative_path: Path) -> str:
        full_relative = self.settings.obsidian_generated_dir / relative_path
        return full_relative.with_suffix("").as_posix()

    @staticmethod
    def _safe_link_display(value: str) -> str:
        return " ".join(value.splitlines()).replace("|", "-").replace("]", "")

    @staticmethod
    def _atomic_write(target: Path, content: str) -> None:
        # Identical bytes are not rewritten. Rewriting them changed nothing a
        # reader could see while still touching mtime on every timer run, which
        # made "has the vault changed?" unanswerable by inspection.
        if target.is_file():
            try:
                if target.read_text(encoding="utf-8") == content:
                    return
            except (OSError, UnicodeDecodeError):
                pass
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{target.name}.", suffix=".tmp", dir=target.parent
        )
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary_name, target)
        finally:
            temporary_path = Path(temporary_name)
            if temporary_path.exists():
                temporary_path.unlink()

    @staticmethod
    def _yaml_string(value: str) -> str:
        return json.dumps(value, ensure_ascii=False)

    def _render(self, source: SourceRecord, category: str) -> str:
        creators = []
        for creator in source.creators:
            name = creator.get("name") or " ".join(
                part
                for part in [creator.get("firstName"), creator.get("lastName")]
                if part
            )
            if name:
                creators.append(str(name))
        creator_lines = "\n".join(
            f"  - {self._yaml_string(name)}" for name in creators
        ) or "  []"
        abstract = html.escape(source.abstract_note or "No abstract supplied by Zotero.")
        title = html.escape(" ".join(source.title.splitlines()), quote=True)
        publication_date = html.escape(
            " ".join(source.publication_date.splitlines()), quote=True
        )
        item_type = html.escape(" ".join(source.item_type.splitlines()), quote=True)
        zotero_uri = f"zotero://select/library/items/{source.zotero_key}"
        return f"""---
airl_id: {self._yaml_string(source.airl_id)}
type: source
cssclasses:
  - aethrion-source
status: ingested
source_category: {self._yaml_string(category)}
zotero_item_key: {self._yaml_string(source.zotero_key)}
zotero_version: {source.zotero_version}
doi: {self._yaml_string(source.doi)}
source_url: {self._yaml_string(source.url)}
content_hash: {self._yaml_string(source.content_hash)}
generated_at: {self._yaml_string(source.synced_at.isoformat())}
provenance: airl-bridge-api
tags:
{self._obsidian_tags(source, category)}
zotero_tags:
{self._tag_lines(source)}
creators:
{creator_lines}
---

<h1>{title}</h1>

> [!warning] Generated Zotero view
> This file is regenerated from the canonical source registry; do not edit it by hand. Keep human synthesis under `20 - Source Notes`.

- Zotero: [{source.zotero_key}]({zotero_uri})
- Publication date: <code>{publication_date}</code>
- Item type: <code>{item_type}</code>

## Abstract from Zotero

<pre>{abstract}</pre>
"""

    @staticmethod
    def _obsidian_tags(source: SourceRecord, category: str) -> str:
        """Obsidian tags, kept separate from the Zotero author's own keywords.

        ``zotero_tags`` is what a human wrote in Zotero and is reproduced
        faithfully. ``tags`` is this vault's controlled vocabulary — without it
        a projected source cannot be reached by tag, which is how 33 of the
        vault's notes were invisible to every query that filtered on one.
        """
        slug = re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-")
        item = re.sub(r"[^a-z0-9]+", "-", source.item_type.lower()).strip("-")
        tags = ["aethrion/source", f"aethrion/source-category/{slug}"]
        if item:
            tags.append(f"aethrion/item-type/{item}")
        if source.doi:
            tags.append("aethrion/has-doi")
        return "\n".join(f"  - {tag}" for tag in tags)

    def _tag_lines(self, source: SourceRecord) -> str:
        tag_values = [
            str(tag.get("tag", "")).strip()
            for tag in source.tags
            if isinstance(tag, dict) and str(tag.get("tag", "")).strip()
        ]
        return "\n".join(
            f"  - {self._yaml_string(tag)}" for tag in tag_values
        ) or "  []"
