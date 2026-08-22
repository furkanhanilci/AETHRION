"""Source categorisation and duplicate detection.

Two responsibilities, deliberately kept small:

* **Category mapping.** Zotero ``itemType`` → the numbered folder used by the
  Obsidian projection. The names are English and stable; changing one renames a
  folder in the user's vault on the next projection.
* **Duplicate grouping.** Sources are grouped by a normalised title key
  (NFKC-folded, punctuation collapsed). The result is **reported, never acted
  on** — no merge, no deletion, no rewrite. Deciding that two records are the
  same work is a curation decision with a human owner (WP-062), not a string
  comparison.

Normalising by title alone is a weak signal: it can group two distinct works
that share a title, and it misses duplicates whose titles differ. That is
acceptable precisely because the output is a review queue rather than an action.
"""
from __future__ import annotations

import re
import unicodedata
from collections import defaultdict

from .models import SourceRecord


SOURCE_TYPE_FOLDERS = {
    "journalArticle": "01 - Journal Articles",
    "conferencePaper": "02 - Conference Papers",
    "report": "03 - Reports and Preprints",
    "preprint": "03 - Reports and Preprints",
    "book": "04 - Books",
    "bookSection": "05 - Book Sections",
    "thesis": "06 - Theses",
    "webpage": "07 - Web Sources",
    "dataset": "08 - Datasets",
    "patent": "09 - Patents",
    "document": "90 - Other Documents",
}
DEFAULT_SOURCE_FOLDER = "99 - Other Sources"


def source_category(item_type: str) -> str:
    return SOURCE_TYPE_FOLDERS.get(item_type, DEFAULT_SOURCE_FOLDER)


def normalized_title_key(title: str) -> str:
    normalized = unicodedata.normalize("NFKC", title).casefold()
    normalized = re.sub(r"[^\w]+", " ", normalized, flags=re.UNICODE)
    return " ".join(normalized.split())


def duplicate_source_groups(sources: list[SourceRecord]) -> list[list[SourceRecord]]:
    grouped: dict[str, list[SourceRecord]] = defaultdict(list)
    for source in sources:
        key = normalized_title_key(source.title)
        if key:
            grouped[key].append(source)
    duplicates = [group for group in grouped.values() if len(group) > 1]
    return sorted(
        (sorted(group, key=lambda item: item.zotero_key) for group in duplicates),
        key=lambda group: group[0].title.casefold(),
    )
