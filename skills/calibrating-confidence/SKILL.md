---
name: calibrating-confidence
version: 1.0.0
description: Use when confidence scores are produced or displayed, when a claim reaches a terminal outcome, or when confidence numbers need interpreting
gates: [G6, G8, G10]
roles: [Metascience Lead, Statistical Methods Owner]
assurance_classes: [R1, R2, R3]
emits: [CalibrationReport]
mechanical_checks: [raw_and_calibrated_stored, uncalibrated_flag_when_insufficient_data]
---

# Calibrating Confidence

## Genel ilke

Ölçülmemiş bir güven skoru süslemedir. Ve süsleme, **false rigor**'un tam
tanımıdır.

## Demir kural

> **KALİBRE EDİLMEMİŞ SKOR SAYI OLARAK GÖSTERİLMEZ.**
>
> Yeterli sonuç verisi yoksa `UNCALIBRATED` yazılır. Sahte hassasiyet yasaktır.

## İki alan, tek gerçek

```yaml
confidence_dimensions:
  entailment:
    raw: 0.90            # modelin ham çıktısı
    calibrated: 0.72     # sonuçlarla kalibre edilmiş
    n_outcomes: 47       # kaç sonuçla kalibre edildi
    status: CALIBRATED   # CALIBRATED | UNCALIBRATED
```

## Kalibrasyon döngüsü

1. **Tahmin kaydedilir** — claim üretildiğinde ham skorlar
2. **Sonuç beklenir** — G7 doğrulaması, G10 hayatta kalma
3. **Skor hesaplanır** — Brier skoru + kalibrasyon eğrisi
4. **Yeniden kalibre edilir** — izotonik regresyon veya Platt ölçekleme
5. **Yayınlanır** — hangi boyut ne kadar güvenilir

## Birleştirme kuralı — çarpma yok, ortalama yok

Yedi boyut bağımsız değil ve farklı şeyler ölçüyor. Çarpım yapay olarak
düşük, ortalama yapay olarak yüksek sonuç verir.

> **En zayıf halka:** `claim_strength = min(calibrated_dimensions)`
> ve **hangi boyutun bağladığı** açıkça gösterilir.

Bir claim, en zayıf kanıt boyutu kadar güçlüdür.

## Yorumlama

| Brier | Anlam |
|---|---|
| Düşük | İyi kalibre — sayılar anlamlı |
| Yüksek + aşırı güven | Model kendine fazla güveniyor → skorları sıkıştır |
| Yüksek + az güven | Model çekingen → skorları genişlet |

## Kırmızı bayraklar

- Üç haneli hassasiyette skor, `n_outcomes` yok
- `raw` ve `calibrated` aynı
- Yedi boyut çarpılarak tek skora indirilmiş
- Kalibrasyon hiç güncellenmemiş
