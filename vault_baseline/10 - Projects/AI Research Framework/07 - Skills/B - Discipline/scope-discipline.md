---
name: scope-discipline
version: 1.0.0
description: Use when writing a report, abstract, conclusion or any prose that states what the research found
gates: [G6, G8, G9]
roles: [Scientific Editor, Scientific Owner, Project Decision Owner]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [ScopeConformanceReport]
mechanical_checks: [prose_sentence_maps_to_claim, prose_scope_within_claim_scope]
---

# Scope Discipline

## Demir kural

> **METİN, `ClaimVersion.scope_qualification`'I AŞAMAZ.**
>
> Eşlenemeyen veya kapsamı aşan cümle → yayın `BLOCKED`.

## Neden bu bir AI laboratuvarında kritik

Aşırı genelleme, dil modellerinin en tutarlı hata modudur. Ve mekanik olarak
yakalanabilir — bu yüzden model yargısına bırakılmaz.

## Prosedür

1. Metindeki her iddia cümlesini çıkar
2. Her cümleyi bir `ClaimVersion`'a eşle
3. Cümlenin kapsamını claim'in `scope_qualification`'ı ile karşılaştır
4. Aşan cümleyi ya nitelendir ya düşür
5. `DecisionRecord.obligations` içindeki her yükümlülüğün metinde karşılığını doğrula

## Kapsam aşımı işaretleri

| Metin | Claim | Hüküm |
|---|---|---|
| "Consensus dayanıklıdır" | "senkron Byzantine, dürüst çoğunluk altında dayanıklıdır" | **AŞIM** |
| "Yöntem genel olarak uygulanabilir" | tek bir senaryoda test edilmiş | **AŞIM** |
| "X, Y'ye neden olur" | korelasyonel kanıt | **AŞIM** — nedensellik iddiası |
| "İlk kez gösterilmiştir" | literatür taraması bunu doğrulamıyor | **AŞIM** |

## Nitelendirme dili

Kapsam sınırı **başlıkta ve özette** görünür — yalnız "Limitations"ta değil.
Limitations bölümüne saklanan bir kapsam sınırı, kapsam sınırı sayılmaz.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Sınırlama bölümünde yazdım" | **Yetersiz.** İddia cümlesinin kendisi nitelenir. |
| "Okuyucu bağlamdan anlar" | Anlamayabilir. **Açık yaz.** |
| "Nitelendirince zayıf duruyor" | Doğru olan budur. Zayıflık gerekçe değildir. |
| "Diğer makaleler de böyle yazıyor" | Onların hatası bizim standardımız değildir. |

## Kırmızı bayraklar

- Özet, sonuç bölümünden daha güçlü iddia içeriyor
- Başlıkta kapsam sınırı yok ama claim'de var
- `obligations` yerine getirilmemiş
