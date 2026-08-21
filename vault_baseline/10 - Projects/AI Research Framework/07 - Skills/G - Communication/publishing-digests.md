---
name: publishing-digests
version: 1.0.0
description: Use when producing a recurring status summary, portfolio report, cost report or metascience report for humans
gates: [G10]
roles: [Notification Broker, Metascience Lead, FinOps Lead]
assurance_classes: [R1, R2, R3]
requires_skills: [notifying-humans]
emits: [DigestReport]
mechanical_checks: [read_only_sources, dlp_scan_passed, no_decision_embedded]
---

# Publishing Digests

## Genel ilke

Özet **salt-okunur bir türevdir**. Karar taşımaz, durum değiştirmez.

## Ritim

| Sıklık | İçerik | Alıcı |
|---|---|---|
| **Günlük** | Açık kararlar + SLA riski + dünkü koşumlar + bütçe | Decision Owner |
| **Haftalık** | Portföy durumu, gate akışı, bloke işler, açık bulgular | Tüm roller |
| **Aylık** | **Metascience**: kalibrasyon, uyum, gate yield, kontrol FP/FN, claim survival | Assurance + Metascience |
| **Çeyreklik** | Maliyet derinlemesine, model requalification, olay analizi | FinOps + Platform |

## Günlük özet — zorunlu bölümler

```
1. Karar bekleyenler      → sayı, en eski bekleyen, SLA riski
2. Bloke gate'ler         → hangi proje, hangi blocker, kim sahip
3. Açık CRITICAL bulgular → sayı ve yaş
4. Bütçe                  → kullanım oranı, hard limite kalan
5. Dün tamamlananlar      → koşum, review, karar sayısı
6. Dikkat bütçesi         → bu hafta kaç karar verildi / kota
```

## Aylık metascience özeti — en değerli olan

```
- Confidence kalibrasyonu: Brier skoru, boyut bazında
- Reviewer uyumu: κ ve ikili hata korelasyonu; kotayı bozan çiftler
- Gate yield: hangi gate kaç gerçek bulgu yakaladı, birim maliyeti
- Kontrol enjeksiyonu: yanlış pozitif / yanlış negatif oranı
- Claim survival: 6/12/24 aylık hayatta kalma oranı
- İnsan kararı: süre dağılımı, geri alma oranı, dissent override oranı
```

> Bu rapor laboratuvarın **karnesidir**. Kötü görünüyorsa gizlenmez.

## Kurallar

- Kaynaklar salt-okunur; özet üretimi hiçbir durumu değiştirmez
- Veri sınıfı tavanı [[notifying-humans]]'daki gibi uygulanır
- Sayılar **kalibre edilmiş** olanlardır; `UNCALIBRATED` alanlar öyle gösterilir
- Kötü haber gömülmez — özetin başında görünür

## Kırmızı bayraklar

- Özet üretimi bir durum değiştirmiş
- `UNCALIBRATED` alanlar sayı gibi sunulmuş
- Aylık metascience özeti hiç üretilmemiş
- Kötü metrikler yalnız ekte
