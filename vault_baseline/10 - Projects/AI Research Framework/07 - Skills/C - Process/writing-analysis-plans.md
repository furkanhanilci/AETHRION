---
name: writing-analysis-plans
version: 1.0.0
description: Use before any data is analysed, when defining decision rules for results, or when the statistical approach is being chosen
gates: [G2, G4]
roles: [Statistical Methods Owner]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [AnalysisPlanManifest]
mechanical_checks: [locked_before_execution, decision_rules_precommitted]
---

# Writing Analysis Plans

## Genel ilke

Protokol **ne ölçeceğimizi** söyler. Analiz planı **nasıl karar vereceğimizi**
söyler. İkisi ayrı kilitlenir.

## Neden ayrı

Birleştirilirse, sonuçları gördükten sonra karar kuralını değiştirme kapısı
açık kalır. Klinik araştırmada SAP (Statistical Analysis Plan) protokolden
ayrı ve unblinding'den önce kilitlenir — sebep budur.

## Zorunlu içerik

| Alan | Ne yazılır |
|---|---|
| `primary_endpoint` | Tek birincil sonuç ölçüsü |
| `secondary_endpoints` | Sıralı liste — sonradan eklenemez |
| `decision_rule` | Hangi değer hangi kararı verir |
| `power_analysis` | Tespit edilebilir minimum etki + varsayımlar |
| `n_and_stopping` | Tekrar sayısı, seed matrisi, durma kuralı |
| `multiplicity` | Çoklu karşılaştırma düzeltmesi |
| `missing_data` | Eksik veri politikası |
| `deviation_policy` | Sapma olursa ne olur |
| `tolerance` | G7a (deterministik) ve G7b (dağılımsal) ayrı |

## Tolerans — iki ayrı tanım

- **G7a Reproduction:** aynı manifest, aynı seed → **deterministik**.
  Tolerans ≈ 0. Tek bir yüzde değil.
- **G7b Replication:** farklı seed/uygulama → **dağılım karşılaştırması**
  (CI örtüşmesi veya eşdeğerlik testi). Nokta tahmini yüzdesi **kullanılmaz**.

## Kilitleme

Plan hash'i, herhangi bir sonuç üretilmeden **önce** kaydedilir. Timestamp
kanıtı `EvidenceManifest`'e girer.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Analiz protokolde zaten var" | Ayrı hash, ayrı kilit. **Yeniden yaz.** |
| "Güç analizi için ön veri lazım" | Ön veri ayrı bir `exploratory` koşumdur; ana veriden gelmez. |
| "Birincil sonucu sonra seçeriz" | **Tek birincil sonuç, önceden.** Gerisi ikincil. |
| "Çoklu karşılaştırma bu ölçekte önemsiz" | Statistical Methods Owner karar verir, uygulayıcı değil. |

## Kırmızı bayraklar

- Birden çok "birincil" sonuç
- Güç analizi yok ama örneklem sayısı belirlenmiş
- Tolerans tek bir yüzde olarak yazılmış
