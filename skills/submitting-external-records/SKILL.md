---
name: submitting-external-records
version: 1.0.0
description: Use when a protocol or analysis plan must be externally timestamped, when artifacts need a persistent DOI, or when a publication package is being deposited
gates: [G2, G9]
roles: [Data Steward, Research Software Engineer, Project Decision Owner]
assurance_classes: [R1, R2, R3]
tool_effect: T3
data_class_ceiling: D1
emits: [ExternalRegistrationRecord, DOIRecord]
mechanical_checks: [human_approved_before_submission, data_class_ceiling_enforced, doi_recorded_in_manifest]
---

# Submitting External Records

## Genel ilke

İç kayıtlarınız kendi kendini doğrular. **Dış kayıt bağımsız bir tanıktır.**

Ön-kayıt disiplininizin en güçlü hali, kilidin **dışarıda ve değiştirilemez**
olmasıdır.

## Demir kural

> **DIŞ GÖNDERİM GERİ ALINAMAZ — HER BİRİ AÇIK İNSAN ONAYI GEREKTİRİR.**
>
> Ajan hazırlar, insan gönderir.

## Ne, nereye, ne zaman

| Kayıt | Hedef | Gate | Kazanç |
|---|---|---|---|
| Ön-kayıt (protokol + analiz planı) | **OSF Registries** | **G2** | Zaman damgalı, değiştirilemez kayıt + kalıcı DOI |
| Kod + ortam | **Zenodo** / Software Heritage | G9 | Kalıcı arşiv + DOI ("Artifacts Available") |
| Veri seti | Zenodo / alan repository | G9 | DOI + **Croissant** metadata |
| Yayın paketi | Zenodo / kurum repository | G9 | RO-Crate + DOI |
| Yazar kimliği | **ORCID** | G9 | Kalıcı yazar kimliği |
| Ön baskı | arXiv / bioRxiv | G9 | Görünürlük (**gönderim otomasyonu sınırlı**) |

> **Doğrulama notu:** OSF kayıtları zaman damgalı, değiştirilemez ve DOI'lidir;
> programatik gönderim yolu (OSF API v2) uygulama öncesi doğrulanmalıdır.
> arXiv gönderimi tam otomatikleştirilemez — insan adımı gerekir.

## Neden G2'de dış ön-kayıt

İç `AnalysisPlanManifest` hash'i sizin sisteminizde tutulur. Dış bir kayıt,
**sizin sisteminize güvenmeyen** birine karşı da kanıttır. In-principle
acceptance'ın dış çapası budur.

Hassas çalışmalar için OSF **ambargo** seçeneği vardır: kayıt zaman damgalanır
ama belirli bir süre gizli kalır.

## Gönderim öncesi

- [ ] İnsan onayı alındı (**tam kelime**: `SUBMIT`)
- [ ] Veri sınıfı ≤ D1
- [ ] DLP taraması geçti
- [ ] Lisans ve atıf bilgisi tam (`CITATION.cff`, `CodeMeta`)
- [ ] Ambargo kararı verildi
- [ ] Geri alınamazlık kabul edildi

## Sonrası

Dönen DOI **manifest'e ve `EvidenceManifest`'e yazılır.** Kaydedilmeyen DOI
kanıt zincirinin dışında kalır ve işe yaramaz.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Sonra düzeltiriz" | **Dış kayıt geri alınamaz.** Düzeltme yeni sürümdür, silme değil. |
| "Önce gönderelim, ambargo sonra" | Ambargo gönderim anında seçilir. |
| "İç hash yeterli" | İç hash sizin sisteminize güvenmeyi gerektirir. |

## Kırmızı bayraklar

- Dış gönderim ajan tarafından tetiklenmiş
- DOI dönmüş ama manifest'e yazılmamış
- D2+ içerik dış kayda gitmiş
