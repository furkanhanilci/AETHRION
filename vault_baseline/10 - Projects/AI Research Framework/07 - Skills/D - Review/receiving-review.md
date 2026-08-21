---
name: receiving-review
version: 1.0.0
description: Use when a ReviewVerdict arrives, when review conditions must be addressed, or when you disagree with a finding
gates: [G6, G8]
roles: [Engineering Owner, Scientific Owner, Evidence Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [ProducerResponse]
mechanical_checks: [every_condition_has_stance, no_unanswered_condition_at_gate]
---

# Receiving Review

## Genel ilke

> **Uygulamadan önce doğrula. Varsaymadan önce sor.
> Sosyal rahatlık yerine teknik doğruluk.**

## Demir kural

> **HER KOŞULUN BİR TUTUMU (`stance`) OLMAK ZORUNDA.**
>
> Cevapsız koşulla G8'e geçiş yasaktır.

## Sıra

```
Oku → Anla → DOĞRULA → Değerlendir → Yanıtla → Uygula
```

**Herhangi bir madde belirsizse: DUR.** Hiçbir şey uygulama.
Belirsizlikler birbirine bağlı olabilir; birini yanlış anlamak diğerini bozar.

Sonra sırayla: bloke ediciler → basit düzeltmeler → karmaşık düzeltmeler.
**Her biri tek tek, her birini ayrı doğrula**, sonunda regresyon kontrolü.

## İtiraz meşrudur

Şu durumlarda **itiraz et**:

- Bulgu mevcut çalışan davranışı bozuyorsa
- Reviewer tam bağlama sahip değilse
- Kapsamda olmayan bir şey isteniyorsa (YAGNI)
- Dondurulmuş protokolle çelişiyorsa
- Teknik olarak yanlışsa

**Nasıl:** Teknik gerekçeyle, savunmacı olmadan. Çalışan koşuma, teste veya
manifest'e referans ver.

## Yasak: performatif katılım

> "Harika nokta!", "Kesinlikle haklısınız!", "Çok iyi yakalamışsınız!"

Anlayışı **eylem** gösterir, iltifat değil. Bu, dil modellerinin bilinen bir
hata modudur ve review'u onay teatrosuna çevirir.

Düzeltme gerektiğinde tek cümle yeterli: *"Doğruladım, haklısınız. Düzeltiyorum."*

## `ProducerResponse` — zorunlu çıktı

```yaml
per_condition:
  - condition_id: "C-01"
    stance: "ACCEPTED"          # ACCEPTED | DISPUTED | CLARIFICATION_NEEDED
    action_taken: "..."
    evidence_ref: "..."
    verified_by: "mechanical:scope-conformance"   # KİM doğruladı
  - condition_id: "C-02"
    stance: "DISPUTED"
    technical_rationale: "..."
    escalated_to: "DisagreementCase disagree-..."
```

`ACCEPTED` ise **bağımsız doğrulama** zorunlu — producer'ın kendi beyanı yetmez.
`DISPUTED` ise `DisagreementCase`'e bağlanır.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Koşulu zaten karşılıyoruz" | **Kanıtla.** `verified_by` doldurulur. |
| "Bu minor, sonra bakarız" | Minor da bir `stance` alır. `PARKED` + sahip + süre. |
| "Reviewer yanlış anlamış" | Olabilir — `DISPUTED` yaz, gerekçe ver. **Sessizce geçme.** |
| "Hepsine katılıyorum" (hepsi tek seferde) | Şüpheli. Her koşul ayrı doğrulanır. |

## Kırmızı bayraklar

- Tüm koşullar tek hamlede `ACCEPTED`
- `verified_by` alanı producer'ın kendisi
- Yanıtta iltifat var, kanıt yok
