---
name: measuring-agreement
version: 1.0.0
description: Use when assigning reviewers or reproducers, when independence must be demonstrated, or when multiple raters produce verdicts
gates: [G6, G7]
roles: [Metascience Lead, Assurance Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [AgreementReport, IndependenceRecord]
mechanical_checks: [pairwise_error_correlation_computed, quota_rule_enforced]
---

# Measuring Agreement

## Genel ilke

> **Farklı model ailesi kullanmak bağımsızlık garantisi vermez.**
>
> Frontier modeller örtüşen korpuslarda eğitiliyor. Aynı hatayı aynı güvenle
> yapabilirler. İki reviewer'ın hemfikir olması, hata korelasyonu ölçülmediği
> sürece kanıt değeri taşımaz.

## Demir kural

> **`Model Lineage` BOYUTU BEYAN DEĞİL ÖLÇÜMDÜR.**
>
> Hata korelasyonu eşiği aşan iki profil, aynı claim'in bağımsızlık kotasına
> **birlikte sayılamaz**.

## Agreement calibration set

Kalıcı bir küme tutulur:
- Doğru cevabı bilinen review görevleri
- Her nitelikli model profili periyodik olarak işler
- Ölçülen: doğruluk, **ikili hata korelasyonu** `ρ`, şansı aşan uyum (κ / α)

## Uyum istatistikleri

| Ölçü | Ne zaman |
|---|---|
| Cohen's κ | İki değerlendirici, kategorik |
| Fleiss' κ | İkiden çok değerlendirici |
| Krippendorff's α | Eksik veri, karışık ölçek |
| Pairwise error correlation | **Bağımsızlık kotası için birincil ölçü** |

## Yorumlama — iki yönlü alarm

| Durum | Anlam | Aksiyon |
|---|---|---|
| Düşük uyum | Görev belirsiz veya kriterler net değil | Kriterleri netleştir |
| Sağlıklı uyum | Beklenen | — |
| **κ ≈ 1.0** | **Bağımsızlık şüpheli** | Profilleri ayır, korelasyonu ölç |
| Yüksek `ρ` | Aynı hataları yapıyorlar | **Kotaya birlikte sayılmaz** |

> Çok yüksek uyum, iyi haber değildir. Bağımsız yargıçlarda beklenmez.

## Kota kuralı

```
claim başına bağımsız reviewer kotası:
  R1: 1   R2: 2   R3: 3
ve seçilen profillerin ikili ρ değerleri eşiğin ALTINDA olmalı
```

Eşiği geçen profil çiftinden yalnız biri sayılır; diğeri ek görüştür.

## Kırmızı bayraklar

- Bağımsızlık `PASS` ama korelasyon ölçümü yok
- Aynı iki profil her claim'de birlikte kullanılıyor
- Calibration set aylardır güncellenmemiş
