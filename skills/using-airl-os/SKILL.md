---
name: using-airl-os
version: 1.0.0
description: Use when starting any AIRL-OS work, when unsure which procedure applies, or when a gate transition is about to be attempted
gates: [G0, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10]
roles: [all]
assurance_classes: [R1, R2, R3]
non_waivable: true
---

# Using AIRL-OS

## Genel ilke

AIRL-OS'ta hiçbir iş prosedürsüz yapılmaz. Her adımda bir skill yüklüdür.

## Nereden başlanır

| Durum | Skill |
|---|---|
| Yeni bir araştırma fikri | `framing-research` |
| Yöntem yazılacak | `writing-protocols` → `writing-analysis-plans` |
| Deney çalıştırılacak | `preregistration-discipline` → `executing-experiments` |
| Ajana iş verilecek | `agent-driven-research` |
| Review istenecek | `requesting-review` |
| Review geldi | `receiving-review` |
| Beklenmeyen sonuç | `investigating-anomalies` |
| Uydurma/tahrifat şüphesi | `investigating-integrity-concerns` |
| İş bitti denecek | `verification-before-completion` |
| Proje kapanacak | `finishing-a-project` |

## Değişmez üç kural

1. **Ajan üretir, makine doğrular, insan karar verir.** Bu sıra bozulmaz.
2. **Taze doğrulama kanıtı olmadan hiçbir şey "tamamlandı" değildir.**
3. **Şüphedeyken ağır olan yolu seç.** Eksik bilgi en yüksek assurance sınıfına düşer.

## Kırmızı bayraklar

- Hangi skill'in yüklü olduğunu söyleyemiyorsan → dur, bu skill'i oku
- Gate geçişi "açıkça uygun" görünüyorsa → gate kaydı yine de üretilir
