# Bridge Component Status

Bridge, AI Research Framework’ün tamamı değil; Zotero → canonical source store →
Obsidian projection → Hermes read-only akışını sağlayan ilk çalışan bileşendir.

## Current evidence

- Zotero Local API read-only sınırı tanımlı.
- FastAPI Bridge ve SQLite source registry mevcut.
- Obsidian projection ve Hermes read-only erişim mevcut.
- İlk contract foundation `src/airl_framework/` altında bulunuyor.
- Test kanıtı ve uygulama geçmişi [[implementation_log]] içinde tutuluyor.

## Not yet equivalent to full framework

Control/Event, model/agent/tool, execution security, evidence assurance,
observability, integration cutover ve Day-2 operations paketlerinin tamamı
Bridge tarafından karşılanmış sayılmaz. Bunlar plan ve ayrı teslimatlar olarak
izlenmelidir.

## Related records

- [[framework_repository_and_obsidian_map]]
- [[00_navigation_and_execution_cockpit]]
- [[implementation_log]]
- [[claude_full_framework_review_prompt]]
