---
name: anchoring-spans
version: 1.0.0
description: Use when creating an EvidenceSpan, when a source representation is re-extracted or updated, or when a span can no longer be located
gates: [G3, G6, G10]
roles: [Evidence Extractor, Knowledge Steward]
assurance_classes: [R1, R2, R3]
emits: [EvidenceSpan, ReanchorRecord, ImpactCase]
mechanical_checks: [multi_selector_present, old_representation_hash_immutable]
---

# Anchoring Spans

## Genel ilke

Kaynak değişir, kanıt kalmalıdır. Çapa **çoklu seçici** ile kurulur.

## Çoklu seçici (W3C Web Annotation)

Her span **en az üç** seçici taşır:

| Seçici | İçerik |
|---|---|
| `TextQuoteSelector` | `exact` + `prefix` + `suffix` |
| `TextPositionSelector` | `start` / `end` offset |
| `StructureSelector` | sayfa / paragraf / cümle |
| `PdfBoundingBoxSelector` | sayfa + koordinat + OCR motoru ve **sürümü** |

Tek seçici kırılgandır. Üçü birden nadiren aynı anda bozulur.

## Format bazlı strateji

| Format | Çapa | Kırılganlık |
|---|---|---|
| PDF | hash + sayfa + bbox + alıntı + OCR sürümü | Düşük |
| HTML | snapshot hash + URL + CSS seçici + alıntı | **Yüksek** — seçici değişir |
| EPUB | temsil hash + CFI + alıntı | Düşük |
| Dataset | sürüm hash + satır anahtarı + kolon + değer parmak izi | Düşük |
| Kod | commit hash + sembol yolu + satır aralığı | Düşük (AST yolu tercih) |
| Ön baskı | arXiv id + **sürüm** + sayfa + bbox | Orta — sürüm atlanırsa yüksek |

## Yeniden çapalama — durum makinesi

Kaynak yeni bir temsil kazandığında:

```
1. ESKİ content_hash IMMUTABLE KALIR      → v1 kanıtı hâlâ doğrulanabilir
2. Yeni temsilde exact quote aranır
3. Sonuç:
     RELOCATED       tek eşleşme       → claim: unchanged
     AMBIGUOUS       çok eşleşme       → claim: CHALLENGED  + ImpactCase
     NEEDS_REANCHOR  eşleşme yok       → claim: CHALLENGED  + ImpactCase
     ORPHANED        kaynak erişilemez → claim: ORPHANED    + cascade
4. G10 izleme akışı tetiklenir
```

## Demir kural

> **ESKİ TEMSİL HASH'İ ASLA ÜZERİNE YAZILMAZ.**
>
> Yeni temsil yeni bir kayıttır. Eski kanıtın doğrulanabilirliği korunur.

## Kırmızı bayraklar

- Tek seçicili span
- OCR motoru/sürümü kaydedilmemiş
- Ön baskıda sürüm numarası yok
- `ORPHANED` span'e bağlı claim hâlâ `ACTIVE`
