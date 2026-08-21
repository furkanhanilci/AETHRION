---
name: extracting-evidence
version: 1.0.0
description: Use when a ClaimCandidate exists without a linked EvidenceSpan and at least one SourceRepresentation is available
gates: [G3, G6]
roles: [Evidence Extractor]
assurance_classes: [R1, R2, R3]
requires_skills: [anchoring-spans, evidence-before-claim]
emits: [EvidenceSpan, ClaimEvidenceLink]
mechanical_checks: [quote_exact_match_in_representation, support_type_assigned]
---

# Extracting Evidence

## Genel ilke

Kanıt **kaynakta gerçekten yazan** şeydir — kaynağın söylediğini düşündüğün
şey değil.

## Demir kural

> **ALINTI, KAYNAK TEMSİLİNDE BİREBİR BULUNMALIDIR.**
>
> Bulunamayan alıntı kanıt değildir. Yaklaşık alıntı **uydurma riskidir**.

## Prosedür

1. Claim'i oku; **hangi tam ifadenin** destek sayılacağını belirle
2. Kaynak temsilinde ara — `SourceRepresentation` hash'i ile pinlenmiş olan
3. Bulunan span'i [[anchoring-spans]] ile çapala (çok seçicili)
4. `support_type` ata:
   - `supports` — iddiayı destekler
   - `contradicts` — iddiayı çürütür
   - `qualifies` — koşullandırır/sınırlar
   - `contextualizes` — arka plan sağlar
5. Confidence ver — **ham skor**; kalibrasyon ayrı katmanda
6. Bulunamadıysa: **`NOT_FOUND` kaydet.** Uydurma.

## Çıkarım kalitesi

PDF için **GROBID** tercih edilir: bölüm yapısı, referanslar ve koordinatlar
düz metin çıkarımından çok daha güvenilirdir. Kullanılan araç ve sürümü
`extraction_tool` alanına yazılır.

## Bağlam kaydı

Span yalnız cümle değildir. `prefix` ve `suffix` kaydedilir — çünkü
*"X doğru değildir"* ile *"X doğrudur"* arasındaki fark bağlamdadır.

Ve: **olumsuzlama, koşul ve sınırlama ifadelerini asla kırpma.**

## Çelişen kanıt

Claim'i çürüten span aranır ve bağlanır. `contradicted_by` boş bırakılmaz —
boşsa arandığına dair kanıt gerekir.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Makale bunu söylüyor ama tam cümleyi bulamadım" | **Kanıt yok.** İddiayı düşür veya kaynağı yeniden çıkar. |
| "Anlamı aynı, kelimeler farklı" | Birebir eşleşme zorunlu. |
| "Özetten aldım" | Özet bir temsildir; hangi temsil olduğunu pinle. |
| "Şekilde görünüyor" | Şekil verisi ayrı çıkarılır ve hash'lenir. |

## Kırmızı bayraklar

- `quote_exact_match` mekanik kontrolü kırmızı
- Aynı span birden çok çelişkili claim'i destekliyor
- `contradicted_by` sistematik olarak boş
