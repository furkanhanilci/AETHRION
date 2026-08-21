---
name: verification-before-completion
version: 1.0.0
description: Use before any statement implying work is done, correct, passing, ready, complete, or before any gate transition request
gates: [G0, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10]
roles: [all]
assurance_classes: [R1, R2, R3]
non_waivable: true
mechanical_checks: [fresh_command_execution, exit_code_captured]
---

# Verification Before Completion

## Demir kural

> **TAZE DOĞRULAMA KANITI OLMADAN "TAMAMLANDI" DENMEZ.**

## Prosedür

1. İddiayı kanıtlayacak komutu **belirle**
2. Komutu **taze** çalıştır — hafızadan, önceki koşumdan veya ajan raporundan alıntı yapma
3. Tam çıktıyı **oku**: exit code, hata sayısı, uyarılar
4. Çıktının iddiayı gerçekten desteklediğini **doğrula**
5. Kanıtı iddiaya **ekli** olarak raporla

## Kanıt nedir

| İddia | Kabul edilen kanıt |
|---|---|
| Testler geçiyor | Taze koşumda `0 failures`, exit 0 |
| Şema geçerli | Validator çıktısı, 0 hata |
| Artifact bozulmamış | Yeniden hesaplanan SHA-256 = manifest |
| Anomali düzeldi | Orijinal belirti artık üretilemiyor |
| Kriter karşılandı | Satır satır kontrol listesi |

## Yasak ifadeler (doğrulamadan önce)

"çalışmalı", "muhtemelen doğru", "görünüşe göre", "büyük ihtimalle",
"Harika!", "Mükemmel!", "Tamamlandı" — ve **ajan raporuna bağımsız doğrulama
olmadan güvenmek**.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Az önce çalıştırmıştım" | **Taze çalıştır.** Arada durum değişmiş olabilir. |
| "Ajan geçtiğini raporladı" | **Ajan raporu kanıt değildir.** Kendin doğrula. |
| "Bu kadar basit bir şey bozulamaz" | Basitlik doğrulama muafiyeti değildir. |
| "Kısmi kontrol yeterli" | Kısmi kontrol kısmi kanıttır; iddia tam. |
| "Zaman yok" | O zaman iddia da yok. Durumu `IN_PROGRESS` bırak. |

## Kırmızı bayraklar

- Rapor içinde exit code yok
- "Testler geçiyor" cümlesinin yanında çıktı yok
- Kanıt başka bir ajanın metnine dayanıyor
