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
        / "01 - Dergi Makaleleri"
        / "A reproducible source.md"
    )
    content = target.read_text(encoding="utf-8")

    assert result.projected == 1
    assert result.dashboard_directory is not None
    assert target.is_file()
    assert "<script>" not in content
    assert "&lt;script&gt;" in content
    assert 'source_category: "01 - Dergi Makaleleri"' in content
    assert 'zotero_tags:' in content
    assert "İnsan sentezini `20 - Kaynak Notları` altında tutun" in content
    dashboard = (
        settings.obsidian_vault
        / settings.obsidian_generated_dir
        / "00 - Kontrol Panosu"
        / "Kaynak Kataloğu.md"
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
        / "01 - Dergi Makaleleri"
    )
    names = sorted(path.name for path in category.glob("*.md"))

    assert names == [
        "A reproducible source — Zotero ABCD1234.md",
        "A reproducible source — Zotero EFGH5678.md",
    ]
    duplicates = (
        settings.obsidian_vault
        / settings.obsidian_generated_dir
        / "00 - Kontrol Panosu"
        / "Olası Kopyalar.md"
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
