---
name: requesting-review
version: 1.0.0
description: Use when an artifact is ready for independent assessment, before any gate transition that requires review, or when a claim needs a verdict
gates: [G2, G6, G9]
roles: [Assurance Lead, Engineering Owner, Scientific Owner]
assurance_classes: [R1, R2, R3]
requires_skills: [building-review-packets, independence-discipline]
emits: [ReviewPacket, ReviewVerdict]
mechanical_checks: [packet_hash_recorded, reviewer_independence_verified]
---

# Requesting Review

## Genel ilke

Reviewer **standalone bir paket** alır — asla oturum geçmişi, asla producer'ın
muhakemesi.

## Paketin içeriği

| Var | Yok |
|---|---|
| Ne üretildiğinin kısa tanımı | Producer'ın çalışma alanı |
| `ProtocolManifest` + `AnalysisPlanManifest` hash'leri | Ara loglar |
| Toplu metrikler | Model muhakeme izleri |
| Figür digest'leri | Öz-skorlar |
| Claim taslakları | Producer kimliği/iletişim bilgisi |
| Global kısıtlar (**kelimesi kelimesine**) | Önceki review'lar |

Paket **dosya + hash** olarak verilir. **Inline metin geçilmez.**

## Severity kademeleri

| Kademe | Anlam | Aksiyon |
|---|---|---|
| **Critical** | Devam edilemez | Derhal düzelt; gate BLOCKED |
| **Important** | Sonraki adıma geçilemez | Bu gate'te çöz |
| **Minor** | Kayda geçer | Gelecek için belgele |

## Reviewer'ın değerlendirdiği

- Yöntem sağlamlığı
- Kanıt yeterliliği ve **tanısallığı**
- Claim kapsamının verinin izin verdiğiyle uyumu
- Tekrar üretilebilirlik
- Hata riski ve kenar durumlar

## Çıktı formatı

```
1. Güçlü yanlar
2. Bulgular — severity'ye göre gruplu, her biri konum + gerekçe ile
3. Değerlendirme — ACCEPT | CONDITIONAL_PASS | REJECT
4. CONDITIONAL_PASS ise: koşullar, tek tek numaralı
```

## Erken ve sık review

Review'u sona saklama. Erken review bulguların birikmesini engeller ve
producer bağlamı hâlâ tazeyken düzeltme yapılır.

## Kırmızı bayraklar

- Paket hash'i kaydedilmemiş → reviewer'ın ne gördüğü denetlenemez
- Reviewer producer tarafından atanmış
- Koşullar numaralandırılmamış (bkz. [[receiving-review]])
