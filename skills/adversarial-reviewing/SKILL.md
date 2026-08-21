---
name: adversarial-reviewing
version: 1.0.0
description: Use when assigned as adversarial reviewer, when a claim needs the strongest possible counter-case, or when competing hypotheses must be discriminated
gates: [G2, G6]
roles: [Adversarial Reviewer, Red Team Lead]
assurance_classes: [R2, R3]
requires_skills: [blind-reviewing]
emits: [ReviewVerdict, ACHMatrix]
mechanical_checks: [all_hypotheses_enumerated, diagnosticity_scored]
---

# Adversarial Reviewing

## Genel ilke

Görevin iddiayı **desteklemek değil, çürütmeye çalışmaktır.** Çürütemezsen
iddia güçlenir. Bu senin başarısızlığın değil, sistemin çalışmasıdır.

## Metrik

> **Senin performansın onay hızıyla değil, reddetme kalitesiyle ölçülür.**
>
> Hiçbir şey bulamamak da geçerli bir sonuçtur — ama aramadığın için değilse.

## ACH — Rakip Hipotezlerin Analizi

1. **Tüm makul hipotezleri listele** — yazarın favorisini değil, hepsini.
   Sıradan açıklamaları da yaz (ölçüm hatası, seçim yanlılığı, artifact,
   şans, ters nedensellik)
2. **Tüm kanıtı listele**
3. **Matris kur:** her kanıt × her hipotez → `tutarlı` / `tutarsız` / `ilgisiz`
4. **Tanısallık:** bir kanıt tüm hipotezlerle tutarlıysa **değersizdir**
5. **En çok tutarsızlığa sahip hipotezleri ele**; kalanı sırala

> ACH'nin mantığı terstir: *"hangisini destekliyor"* değil,
> **"hangilerini eliyor"**.

## Saldırı yüzeyleri

| Yüzey | Soru |
|---|---|
| Nedensellik | Korelasyon nedensellik olarak sunulmuş mu? |
| Seçim | Dışlama kuralları sonucu şekillendiriyor mu? |
| Güç | Test iddiayı yanlışlayabilecek güçte mi? |
| Genelleme | Test edilen koşul iddia edilen koşul mu? |
| Ölçüm | Ölçülen şey iddia edilen şey mi? |
| Bağımsızlık | Kanıtlar birbirinden gerçekten bağımsız mı? |
| Çoklu karşılaştırma | Kaç test yapıldı, kaçı raporlandı? |
| Ters nedensellik | Yön tersine olabilir mi? |

## Pre-mortem (G4 öncesi)

*"Bir yıl geçti, bu proje tamamen başarısız oldu. Neden?"*

Gelecek zamandan geçmiş zamana geçmek savunmacılığı kırar. Çıkan maddeler
`falsification_plan`'a eklenir.

## Kırmızı bayraklar

- Yalnız yazarın hipotezini değerlendirdin
- Tanısallık skoru vermedin
- Sıradan açıklamaları (ölçüm hatası, şans) listelemedin
