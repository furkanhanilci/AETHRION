---
name: curating-zotero
version: 1.0.0
description: Use when reading from or writing to Zotero, when a sync conflict occurs, or when agent-managed collections must be updated
gates: [G3, G9, G10]
roles: [Evidence Lead, Source Ingester, Evidence Linker]
assurance_classes: [R1, R2, R3]
non_waivable: true
data_class_ceiling: D1
emits: [SyncReceipt, ReconciliationTask]
mechanical_checks: [conditional_write_used, human_fields_untouched, idempotency_key_present]
---

# Curating Zotero

## Genel ilke

Zotero **çalışma yüzeyidir**, otorite değil. Kanonik kaynak kimliği
Source Registry'dedir.

## Demir kural

> **AJAN İNSAN ALANLARINA ASLA YAZMAZ.**
>
> `notes`, `user_tags`, `highlight_coords` — hiçbir koşulda.

## İki kütüphane

| | Kişisel | Proje grup |
|---|---|---|
| Ajan erişimi | **yalnız okuma** | managed namespace'e yazma |
| Managed namespace | — | `10_*`, `Project/*`, `80_*`, `90_*` |
| İnsan alanları | dokunulmaz | dokunulmaz |
| Yazma yolu | yok | Tool Broker → `PATCH` + `If-Match` |

## Veri sınıfı tavanı

> **Proje grup kütüphanesi bulut barındırmalıdır. `D1`'in üstünde veri
> yazılamaz.** Yayınlanmamış deney bağlamı (`D2`) grup kütüphanesine girmez.

## Çakışma — 412

```
PATCH ... If-Match: <version>
  → 200  başarılı, SyncReceipt üret
  → 412  ►► KÖRLEMESİNE TEKRAR DENEME ◄◄
          ReconciliationTask kuyruğa alınır
          İnsan düzenlemesi korunur
```

**Timeout durumunda da tekrar deneme yok** — idempotency anahtarı ile
durum sorgulanır, sonra karar verilir.

## Her yazma

- Managed namespace kontrolü
- Idempotency anahtarı
- `SyncReceipt`: item, alan kümesi, önceki/sonraki sürüm, zaman, aktör
- **Sessiz yazma yoktur**

## İnsan hareketleri

İnsan bir kaynağı `10_Agent_Candidates`'ten `Project/Methods`'a taşırsa bu
**bir karardır** ve ingest sırasında kaydedilir. Ajan bu kararı geri almaz.

## Kırmızı bayraklar

- `If-Match` olmadan yazma
- 412 sonrası otomatik tekrar
- `SyncReceipt` üretilmemiş yazma
- Grup kütüphanesinde D2+ içerik
