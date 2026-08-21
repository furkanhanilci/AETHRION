---
name: preregistration-discipline
version: 1.0.0
description: Use when any analysis is about to run, when a confirmatory claim is being drafted, or when analysis choices are being changed after seeing results
gates: [G2, G4, G5, G6]
roles: [Scientific Owner, Statistical Methods Owner, Engineering Owner]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [writing-analysis-plans]
emits: [AnalysisPlanManifest, ClaimVersion]
mechanical_checks: [plan_hash_precedes_result_timestamp, claim_labeled_exploratory_or_confirmatory]
---

# Preregistration Discipline

## Demir kural

> **ÖN-KAYIT KİLİTLENMEDEN CONFIRMATORY İDDİA ÜRETİLEMEZ.**
>
> Plan kilitlenmeden hesaplanan her sonuç kalıcı olarak `exploratory` etiketlenir.

## Neden kod disiplininden daha sert

Kodda testten önce yazılan kod silinebilir. Araştırmada **sonucu gördükten
sonra görmemiş olamazsınız.** Bu yüzden ceza silme değil, **kalıcı yeniden
etiketleme**dir. O analiz bir daha asla `confirmatory` olamaz.

## Prosedür

**FREEZE** — `AnalysisPlanManifest` kilitle. Hangi sonucun ne anlama geleceği,
hangi testin uygulanacağı, dışlama kuralları ve stop rule önceden yazılır.
Hash kaydedilir.

**SEVERITY** — Falsification planının gerçekten ayırt edici olduğunu doğrula:
*iddia yanlış olsaydı bu test onu yakalar mıydı?* Yakalamazsa test değersizdir.

**EXECUTE** — Plana tam olarak uy.

**REPORT** — Plandan her sapma açıkça listelenir. Plan dışı her analiz
`exploratory`.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Analiz planı zaten protokolde ima ediliyor" | **İma ≠ kilit.** `AnalysisPlanManifest` ayrı bir hash'tir. |
| "Sonucu görmeden hangi testin uygun olduğunu bilemezdim" | **Doğru — ve tam bu yüzden `exploratory`.** Etiketle, devam et. |
| "Bu yalnız küçük bir kovaryat eklemesi" | **Küçük değişiklik diye bir şey yok.** Plan sonrası her değişiklik `exploratory`. |
| "Ön analiz keşifsel amaçlıydı, asıl analiz plana uygun" | Keşif aynı veriden geldiyse bağımsız değildir. **İkisi de `exploratory`.** |
| "Zaman baskısı var, plan sonradan yazılır" | Plan kilitlenmeden G5 başlamaz. |
| "Sonuç zaten çok net" | Netlik ön-kayıt muafiyeti değildir. |

## Doğrulama kontrol listesi

- [ ] Her confirmatory claim için kilitli bir `AnalysisPlanManifest` var
- [ ] Plan hash'i sonuç üretiminden **önce** kaydedildi (timestamp kanıtı)
- [ ] Falsification testi severity açısından değerlendirildi
- [ ] Plandan her sapma raporda listelendi
- [ ] Plan dışı her analiz `exploratory` etiketli

Hepsini işaretleyemiyorsan: bu claim `confirmatory` olamaz.

## Kırmızı bayraklar

- Analiz planı ile sonuç aynı commit'te
- "HARKing" — hipotez sonuçlardan sonra yazılmış
- Dışlama kuralı sonuçlar görüldükten sonra eklenmiş
