from __future__ import annotations

import re
import unicodedata
from collections import defaultdict

from .models import SourceRecord


SOURCE_TYPE_FOLDERS = {
    "journalArticle": "01 - Dergi Makaleleri",
    "conferencePaper": "02 - Konferans Bildirileri",
    "report": "03 - Raporlar ve Ön Baskılar",
    "preprint": "03 - Raporlar ve Ön Baskılar",
    "book": "04 - Kitaplar",
    "bookSection": "05 - Kitap Bölümleri",
    "thesis": "06 - Tezler",
    "webpage": "07 - Web Kaynakları",
    "dataset": "08 - Veri Setleri",
    "patent": "09 - Patentler",
    "document": "90 - Diğer Belgeler",
}
DEFAULT_SOURCE_FOLDER = "99 - Diğer Kaynaklar"


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
