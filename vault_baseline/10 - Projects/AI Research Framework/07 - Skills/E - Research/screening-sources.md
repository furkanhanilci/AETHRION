---
name: screening-sources
version: 1.0.0
description: Use when candidate sources must be included or excluded, when a literature set is being narrowed, or before freezing a LiteratureSetManifest
gates: [G3]
roles: [Evidence Lead]
assurance_classes: [R1, R2, R3]
requires_skills: [searching-literature]
emits: [ScreeningDecision, LiteratureSetManifest]
mechanical_checks: [every_exclusion_has_reason, criteria_locked_before_screening]
---

# Screening Sources

## Genel ilke

Dahil etme kriterleri **taramadan önce** kilitlenir. Sonra değiştirilirse
tarama baştan yapılır.

## Demir kural

> **HER HARİÇ TUTMA BİR GEREKÇE TAŞIR.**
>
> Gerekçesiz hariç tutma `90_Excluded`'a yazılamaz.

## İki aşamalı tarama

**Aşama 1 — Başlık/özet.** Hızlı, kapsayıcı. Şüphedeysen **dahil et**.
**Aşama 2 — Tam metin.** Kesin. Her hariç tutmaya gerekçe kodu.

## Aktif öğrenme (büyük kümeler)

Yüzlerce/binlerce aday için: **ASReview** tarzı aktif öğrenme. İnsan bir
örneklem etiketler, model sıralar, insan sıradan devam eder.

**Durma kuralı önceden yazılır** — "son N kayıtta 0 dahil etme" gibi.
Model sıralaması durma kararını vermez; insan verir.

## Gerekçe kodları

| Kod | Anlam |
|---|---|
| `DUPLICATE` | Aynı kaynağın başka temsili |
| `OUT_OF_SCOPE` | Araştırma sorusuyla ilgisiz |
| `WRONG_POPULATION` | Farklı bağlam/örneklem |
| `NO_FULLTEXT` | Erişilemedi (**erişim denemesi kaydedilir**) |
| `RETRACTED` | Geri çekilmiş |
| `LANGUAGE` | Dil politikası dışı |
| `INSUFFICIENT_METHOD` | Yöntem raporlaması değerlendirmeye yetmiyor |

## Çift tarama (R2, R3)

İki bağımsız tarayıcı; anlaşmazlık üçüncüye. **Uyum ölçülür**
(bkz. [[measuring-agreement]]). Düşük uyum, kriterlerin belirsiz olduğunu gösterir
— kriterleri netleştir, taramayı tekrarla.

## Akış raporu

Aday sayısı → duplicate → aşama 1 hariç → aşama 2 hariç → dahil.
Her aşamada sayı ve gerekçe dağılımı.

## Kırmızı bayraklar

- Kriterler tarama sırasında değişmiş
- `NO_FULLTEXT` oranı yüksek ama erişim denemesi kaydı yok
- Çift taramada uyum ölçülmemiş
