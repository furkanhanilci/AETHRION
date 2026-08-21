---
name: injecting-controls
version: 1.0.0
description: Use when the lab's own false positive or false negative rate must be measured, or when validating that the research pipeline detects known signals and rejects null data
gates: [G0, G5, G6]
roles: [Metascience Lead, Red Team Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [ControlInjectionRecord, PipelineIntegrityAlert]
mechanical_checks: [controls_indistinguishable_from_real, agents_blind_to_control_status]
---

# Injecting Controls

## Genel ilke

Diğer her metrik **süreç** metriğidir. Bu **sonuç** metriğidir:
laboratuvar doğru sonuç üretiyor mu?

## Demir kural

> **KONTROL PROJELERİ AJANLARDAN GİZLİDİR.**
>
> Yalnız Metascience Lead ve Red Team Lead bilir. Gerçek projelerden
> ayırt edilemez olmalıdır.

## İki kontrol tipi

| Tip | Nedir | Beklenen |
|---|---|---|
| **Pozitif kontrol** | Cevabı önceden bilinen soru | Laboratuvar **bulmalı** |
| **Negatif kontrol** | Null veri / permüte edilmiş veri | Laboratuvar **bulmamalı** |

## Oran

Projelerin **%5–10'u** tohumlanmış olarak açılır. Çok düşükse istatistiksel
güç yok; çok yüksekse maliyet.

## Ölçülen

```
yanlış_pozitif_oranı = negatif kontrolde "bulgu" / toplam negatif kontrol
yanlış_negatif_oranı = pozitif kontrolde kaçırılan / toplam pozitif kontrol
```

Ve **hangi gate'in yakaladığı** kaydedilir — gate yield ölçümünü besler.

## Tek istisna: bu skill bloke edebilir

Metascience düzlemi normalde ölçer, bloke etmez (Goodhart yasası).
**Tek istisna:**

> **Negatif kontrolde bir "etki" bulunursa pipeline bozuktur.**
> Hat durur, kök neden bulunana kadar yeni confirmatory koşum açılmaz.

## Gizlilik yönetimi

- Kontrol durumu ayrı bir kayıtta, ana veritabanında değil
- Korelasyon zincirinde işaretlenmez
- Açığa çıkarsa: o kontrol geçersiz, yenisi üretilir, sızıntı kaydedilir

## Etik sınır

Kontroller **insan karar sahiplerini** de test eder. Bu önceden bildirilir —
kimin test edildiği değil, **testlerin var olduğu** bilinir. Gizli olan
hangi projenin kontrol olduğudur.

## Kırmızı bayraklar

- Kontrol projeleri gerçek projelerden ayırt edilebiliyor
- Ajan bir projenin kontrol olduğunu tahmin edebilmiş
- FP/FN oranı hiç raporlanmamış
- Negatif kontrolde bulgu var ama hat durmamış
