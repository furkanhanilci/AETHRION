# Değişiklik ve Konfigürasyon Kontrolü

## Baseline'lar

Program en az şu baseline'ları ayrı sürümler:

- Architecture decision bundle
- Role and policy contract bundle
- Event/schema bundle
- Infrastructure/IaC bundle
- Model capability/admission bundle
- Tool registry bundle
- Data/source/claim schema bundle
- Acceptance scenario bundle
- Production release candidate manifest

## Değişiklik sınıfları

| Sınıf | Örnek | Onay |
|---|---|---|
| Editorial | Anlam değiştirmeyen açıklama | Package owner |
| Compatible | Backward-compatible optional field | Schema owner + contract test |
| Material | Gate, route, owner, retention veya acceptance değişikliği | Architecture/Governance board |
| Critical | Trust zone, data boundary, canonical owner, blocker waiver | Decision Owner + Safety + Assurance |

## Değişiklik akışı

```text
Change Request → Impact Scan → ADR/Schema Proposal → Independent Review
               → Decision → Implementation Packages → Regression/Replay
               → Baseline Promotion
```

Impact Scan açık workflow'ları, frozen literature setlerini, claim'leri, admission profile'larını, runbook'ları ve kabul senaryolarını listeler. Material değişiklik yalnız yeni baseline ile yürürlüğe girer; eski karar ve artifact'lar değişmeden kalır.

## Konfigürasyon drift

- Production değişiklikleri GitOps dışında yapılamaz; break-glass değişikliği incident ve reconciliation açar.
- Model alias değişimi pinned snapshot olarak kabul edilmez; requalification gerekir.
- Policy bundle rollback imzalı önceki sürüme yapılır ve karar logu korunur.
- Database migration forward ve rollback/downgrade stratejisi taşır; irreversible migration iki aşamalı uygulanır.
- Zotero ve Obsidian dış düzenlemeleri canonical registries'e otomatik gerçek olarak geçmez; ingest/reconciliation kuralları çalışır.

## Plan dosyalarının sürümü

Kabul edilmiş WP dosyası geriye dönük değiştirilmez. Yeni şart için dosya revision notu ve ilgili change ID eklenir; önceki evidence manifest hangi revision ile kabul edildiğini korur.

