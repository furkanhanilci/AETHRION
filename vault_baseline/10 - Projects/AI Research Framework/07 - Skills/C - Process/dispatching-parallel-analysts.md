---
name: dispatching-parallel-analysts
version: 1.0.0
description: Use when the same data can be analysed in more than one defensible way, when multiple independent failures span different subsystems, or when analytic degrees of freedom need measuring
gates: [G6]
roles: [Assurance Lead, Statistical Methods Owner, Metascience Lead]
assurance_classes: [R2, R3]
requires_skills: [independence-discipline, measuring-agreement]
emits: [MultiAnalystReport]
mechanical_checks: [analysts_blind_to_each_other, same_analysis_plan_hash]
---

# Dispatching Parallel Analysts

## Genel ilke

Aynı veri, aynı soru, farklı savunulabilir analiz yolları farklı sonuç verir.
Bu farka **analitik serbestlik dereceleri** denir ve **ölçülebilir**.

İnsan laboratuvarları bunu yapamaz — pahalıdır. Bu laboratuvar yapabilir.

## Ne zaman fan-out

**Evet:** Analiz yolları gerçekten bağımsızsa, her biri diğerinin sonucunu
beklemeden ilerleyebiliyorsa.

**Hayır:** Nedensel olarak bağlıysa, veya çözüm bütün sistemi anlamayı
gerektiriyorsa.

## Her analiste verilen

- Aynı `AnalysisPlanManifest` (aynı hash)
- Aynı veri (aynı artifact hash)
- Dar kapsam, **kendi kendine yeten** brief
- Kısıt: **diğer analistlerin çıktısını görme veya kullanma**
- Farklı model ailesi — ve [[measuring-agreement]] ile **ölçülmüş** bağımsızlık

## Sonuçların birleştirilmesi

1. Her raporu oku
2. **Çakışma kontrolü** — analistler aynı ara artifact'ı değiştirmiş mi?
3. Sonuç **dağılımını** çıkar — nokta tahminlerini değil
4. Yorumla:

| Dağılım | Anlamı | Aksiyon |
|---|---|---|
| Dar | Sonuç analiz yoluna duyarsız | `reproducibility` boyutu yükselir |
| Geniş | Sonuç analiz seçimine bağlı | **`confidence` düşer**, `scope_qualification` zorunlu |
| İki kutuplu | Yöntemsel uyuşmazlık var | `DisagreementCase` aç |
| **Aşırı dar (κ ≈ 1.0)** | **Bağımsızlık şüpheli** | Metascience'a sinyal |

## Multiverse uzantısı

Tek yol yerine tüm savunulabilir yolları (dönüşümler, kovaryatlar, dışlama
eşikleri) çalıştır; sonucun **specification curve**'ünü raporla. p-hacking'e
karşı doğrudan savunma.

## Kırmızı bayraklar

- Analistlerden biri diğerinin çıktısını görmüş
- Yalnız "en iyi" analiz raporlanmış, dağılım gizlenmiş
- Dağılım geniş ama confidence düşmemiş
