"""Tests for the projection — the most safety-critical code in the repository.

Two assertions matter more than the rest:

* **A human note in the generated folder survives a projection run.** Only files
  listed in the projection manifest are deleted. This is the primary defence
  against losing user work, and it is the reason the projection may run
  unattended every 30 minutes.
* **External content is escaped.** A ``<script>`` tag in a Zotero abstract must
  not reach the vault unescaped.

Not covered: the dry-run and populated-directory refusal that finding **M7**
asks for — they do not exist yet.
"""
from airl_bridge.obsidian import ObsidianProjector
from airl_bridge.zotero import normalize_item


def test_projection_stays_in_generated_zone_and_escapes_abstract(settings, zotero_item):
    malicious = {
        **zotero_item,
        "data": {
            **zotero_item["data"],
            "abstractNote": "<script>doBadThing()</script>",
        },
    }
    source, _ = normalize_item(malicious, settings)

    result = ObsidianProjector(settings).project_sources([source])
    target = (
        settings.obsidian_vault
        / settings.obsidian_generated_dir
        / "01 - Journal Articles"
        / "A reproducible source.md"
    )
    content = target.read_text(encoding="utf-8")

    assert result.projected == 1
    assert result.dashboard_directory is not None
    assert target.is_file()
    assert "<script>" not in content
    assert "&lt;script&gt;" in content
    assert 'source_category: "01 - Journal Articles"' in content
    assert 'zotero_tags:' in content
    assert "Keep human synthesis under `20 - Source Notes`" in content
    dashboard = (
        settings.obsidian_vault
        / settings.obsidian_generated_dir
        / "00 - Control Dashboard"
        / "Source Catalog.md"
    )
    assert "A reproducible source" in dashboard.read_text(encoding="utf-8")


def test_same_title_sources_receive_stable_zotero_key_suffixes(settings, zotero_item):
    first, _ = normalize_item(zotero_item, settings)
    second_item = {
        **zotero_item,
        "key": "EFGH5678",
        "data": {**zotero_item["data"], "key": "EFGH5678"},
    }
    second, _ = normalize_item(second_item, settings)

    ObsidianProjector(settings).project_sources([second, first])
    category = (
        settings.obsidian_vault
        / settings.obsidian_generated_dir
        / "01 - Journal Articles"
    )
    names = sorted(path.name for path in category.glob("*.md"))

    assert names == [
        "A reproducible source — Zotero ABCD1234.md",
        "A reproducible source — Zotero EFGH5678.md",
    ]
    duplicates = (
        settings.obsidian_vault
        / settings.obsidian_generated_dir
        / "00 - Control Dashboard"
        / "Potential Duplicates.md"
    ).read_text(encoding="utf-8")
    assert "Zotero ABCD1234" in duplicates
    assert "Zotero EFGH5678" in duplicates


def test_manifest_removes_only_previous_generated_files(settings, zotero_item):
    source, _ = normalize_item(zotero_item, settings)
    projector = ObsidianProjector(settings)
    projector.project_sources([source])
    root = settings.obsidian_vault / settings.obsidian_generated_dir
    human_file = root / "human-note.md"
    human_file.write_text("keep me", encoding="utf-8")

    result = projector.project_sources([])

    assert result.removed_stale == 1
    assert human_file.read_text(encoding="utf-8") == "keep me"
    assert (root / ".airl-projection-manifest.json").is_file()


def test_dashboards_are_recorded_in_the_manifest(settings, zotero_item):
    """The projector records everything it writes, dashboards included.

    Manifest-owned deletion cuts both ways: a generated file outside the
    manifest is one the projector creates and can never clean up again.
    """
    import json

    source, _ = normalize_item(zotero_item, settings)
    ObsidianProjector(settings).project_sources([source])
    root = settings.obsidian_vault / settings.obsidian_generated_dir
    manifest = json.loads(
        (root / ".airl-projection-manifest.json").read_text(encoding="utf-8")
    )

    assert "00 - Control Dashboard/Source Catalog.md" in manifest["generated_files"]
    assert "00 - Control Dashboard/Potential Duplicates.md" in manifest["generated_files"]
    for relative in manifest["generated_files"]:
        assert (root / relative).is_file(), relative


def test_unreadable_manifest_refuses_rather_than_orphaning_files(settings, zotero_item):
    """Swallowing a parse failure overwrote the manifest and orphaned every file
    the old one listed — no longer current, no longer tracked, no longer
    removable. The run must stop instead."""
    import pytest

    from airl_bridge.obsidian import ProjectionError

    source, _ = normalize_item(zotero_item, settings)
    projector = ObsidianProjector(settings)
    projector.project_sources([source])
    root = settings.obsidian_vault / settings.obsidian_generated_dir
    manifest = root / ".airl-projection-manifest.json"
    manifest.write_text("{ this is not json", encoding="utf-8")

    with pytest.raises(ProjectionError, match="unreadable"):
        projector.project_sources([])

    assert manifest.read_text(encoding="utf-8") == "{ this is not json"


def test_projection_is_byte_stable_when_nothing_changed(settings, zotero_item):
    """Unchanged registry in, byte-identical vault out — every generated file.

    Each generated file used to carry a wall-clock `generated_at`, so a run that
    changed nothing still rewrote all of them. That made the documented vault
    parity check report a diff on every timer run, which teaches an operator to
    ignore it.
    """
    source, _ = normalize_item(zotero_item, settings)
    projector = ObsidianProjector(settings)
    projector.project_sources([source])
    root = settings.obsidian_vault / settings.obsidian_generated_dir
    before = {
        path: (path.read_bytes(), path.stat().st_mtime_ns)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }
    assert len(before) >= 4, "expected notes, two dashboards and the manifest"

    projector.project_sources([source])

    after = {
        path: (path.read_bytes(), path.stat().st_mtime_ns)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }
    assert set(after) == set(before)
    changed = [p.name for p in before if after[p][0] != before[p][0]]
    rewritten = [p.name for p in before if after[p][1] != before[p][1]]
    assert changed == [], f"content changed with no input change: {changed}"
    assert rewritten == [], f"files rewritten with no input change: {rewritten}"


def test_projected_note_carries_controlled_obsidian_tags(settings, zotero_item):
    """A projected source must be reachable by tag.

    `zotero_tags` reproduces what a human wrote in Zotero; `tags` is this
    vault's controlled vocabulary. Without the second, every projected source
    is invisible to any query that filters on a tag.
    """
    source, _ = normalize_item(zotero_item, settings)
    ObsidianProjector(settings).project_sources([source])
    note = (
        settings.obsidian_vault
        / settings.obsidian_generated_dir
        / "01 - Journal Articles"
        / "A reproducible source.md"
    ).read_text(encoding="utf-8")

    assert "\ntags:\n" in note
    assert "  - aethrion/source\n" in note
    assert "  - aethrion/source-category/01-journal-articles\n" in note
    assert "  - aethrion/item-type/journalarticle\n" in note
    assert "  - aethrion/has-doi\n" in note
    assert "\nzotero_tags:\n" in note, "the human's own Zotero keywords stay separate"
