---
name: investigating-integrity-concerns
version: 1.0.0
description: Use when fabrication, falsification or plagiarism is suspected, when a mechanical forensic check fails, or when data cannot be traced to a source
gates: [G5, G6, G7, G8, G9, G10]
roles: [Research Integrity Officer]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [IntegrityCase]
mechanical_checks: [statcheck, grim, grimmer, citation_entailment, artifact_hash]
---

# Investigating Integrity Concerns

## Genel ilke

Uydurma alıntı ve uydurma sayı, dil modellerinin en bilinen hata modudur.
Bu risk bir AI laboratuvarında **artar**, azalmaz.

## Demir kural

> **BÜTÜNLÜK ŞÜPHESİ HER GATE'İ DURDURUR.**
>
> Research Integrity Officer, Assurance Lead'den bağımsız raporlar ve
> herhangi bir gate'i durdurabilir.

## Mekanik tetikleyiciler — insan yorumu beklemez

| Kontrol | Ne yakalar |
|---|---|
| **statcheck** | Rapor edilen test istatistiği ↔ p-değeri tutarsızlığı |
| **GRIM** | Bildirilen ortalama, N ve granülerlikle **imkânsız** |
| **GRIMMER** | Aynısı standart sapma için |
| **SPRITE** | Ortalama+SD+N ile olası dağılımların yeniden kurulumu |
| **Alıntı entailment** | Alıntı, kaynak span'inde **bulunamıyor** |
| **Artifact hash** | Manifest ile bytes uyuşmuyor |
| **Benford** | Sayı dağılımı anomalisi |

Bunlardan biri kırmızıysa `IntegrityCase` **otomatik açılır**.

## Yaşam döngüsü

```
ALLEGED → TRIAGED → INVESTIGATING → SUBSTANTIATED    → CLOSED
                                  ↘ UNSUBSTANTIATED  → CLOSED
```

## Prosedür

1. **Koru** — ilgili artifact'lar dondurulur; hiçbir şey silinmez veya düzeltilmez
2. **Kapsamı belirle** — hangi claim'ler, hangi koşumlar, hangi model profili
3. **Yeniden üret** — mekanik kontrolü bağımsız olarak tekrarla
4. **Kaynağa git** — birincil kaynağa, producer'ın önbelleğine değil
5. **Hüküm ver** — `SUBSTANTIATED` / `UNSUBSTANTIATED`
6. **Sonuç uygula**

## `SUBSTANTIATED` sonrası

- İlgili claim'ler → `RETRACTED`
- Üreten **model profili** → `SUSPENDED` (Capability Registry)
- O profilin tüm geçmiş çıktıları taranır
- `ImpactCase` açılır; bağlı yayınlar bilgilendirilir
- Metascience'a olay kaydı

## `UNSUBSTANTIATED` sonrası

Kayıt kapanır ve **korunur**. Şüpheyi bildiren cezalandırılmaz. Yanlış
pozitif oranı Metascience tarafından izlenir.

## Kırmızı bayraklar

- Mekanik kontrol kırmızı ama case açılmamış
- Artifact case açılmadan önce değiştirilmiş
- Case'i, çıktıyı üreten rolün kendisi kapatmış
