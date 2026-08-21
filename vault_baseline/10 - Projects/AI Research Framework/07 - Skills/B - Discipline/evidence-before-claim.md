---
name: evidence-before-claim
version: 1.0.0
description: Use when drafting any claim, when a claim has no linked EvidenceSpan, or when a sentence asserts a fact in a report or publication
gates: [G3, G6, G9]
roles: [Evidence Extractor, Scientific Owner, Scientific Editor]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [anchoring-spans]
emits: [ClaimEvidenceLink]
mechanical_checks: [every_claim_resolves_to_span, span_quote_exact_match]
---

# Evidence Before Claim

## Demir kural

> **HER İDDİA CÜMLESİ BİR `EvidenceSpan`'e VEYA BİR `ExperimentRun`'A ÇÖZÜLMELİDİR.**
>
> Çözülemeyen cümle yayınlanamaz.

## Prosedür

1. İddiayı yaz
2. Kaynağını belirle: literatür span'i mi, kendi koşumun mu?
3. Span ise: [[anchoring-spans]] ile çapala; **birebir alıntı** eşleşmeli
4. Koşum ise: `run_id` + artifact hash bağla
5. `support_type` ata: `supports` / `contradicts` / `qualifies` / `contextualizes`
6. Çelişen kanıtı da bağla — **`contradicted_by` boş bırakılmaz**

## Ayrım: kanıt tipi

| İddia tipi | Gerekli bağ |
|---|---|
| `empirical` | `ExperimentRun` + artifact hash |
| `methodological` | `EvidenceSpan` (kaynak) veya `ProtocolManifest` |
| `interpretive` | En az bir `EvidenceSpan` **ve** açık bir yorum işareti |

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Bu alanda genel kabul görmüş bilgi" | **Kaynağını göster.** Genel kabul de bir kaynağa dayanır. |
| "Sonuçlardan açıkça çıkıyor" | Açıksa `run_id`'yi bağlamak kolaydır. Bağla. |
| "Span'i bulamadım ama makale bunu söylüyor" | **Bulunamayan span = kanıt yok.** İddiayı düşür veya kaynağı yeniden çıkar. |
| "Alıntı yaklaşık, anlamı aynı" | **Birebir eşleşme zorunlu.** Yaklaşık alıntı uydurma riskidir. |
| "Çelişen kaynak zaten zayıf" | Zayıflığı yaz; **gizleme.** `contradicted_by` doldurulur. |

## Kırmızı bayraklar

- Alıntı metni kaynak temsilinde bulunamıyor (LLM uydurma imzası)
- DOI var ama span yok
- `contradicted_by` sistematik olarak boş
