---
name: notifying-humans
version: 1.0.0
description: Use when a human must be informed of a gate state, budget threshold, anomaly, integrity concern, SLA risk or completed run
gates: [G0, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10]
roles: [Notification Broker]
assurance_classes: [R1, R2, R3]
non_waivable: true
tool_effect: T3
emits: [NotificationReceipt, ToolReceipt]
mechanical_checks: [data_class_ceiling_enforced, dlp_scan_passed, idempotency_key_present, rate_limit_respected]
---

# Notifying Humans

## Genel ilke

Bildirim **giden trafiktir** ve dış sisteme yazmadır. Ajan bir bildirim
**niyeti** üretir; Notification Broker gönderir.

## Demir kural

> **AJAN DOĞRUDAN MESAJ GÖNDERMEZ.**
>
> Her gönderim Notification Broker üzerinden geçer: kimlik → policy →
> veri sınıfı → DLP → idempotency → gönderim → `NotificationReceipt`.

## Veri sınıfı tavanı — kanal başına

| Kanal | Tavan | Neden |
|---|---|---|
| **ntfy (self-hosted)** | **D2** | Kendi sunucunuz, dış işleme yok |
| **Matrix (self-hosted)** | **D2** | E2E şifreleme, kendi homeserver |
| **Signal** | D2 | E2E; otomasyonu zor |
| **E-posta (kendi SMTP)** | D1 | Transit şifreli, sunucuda değil |
| **Telegram** | **D1** | Bulut, sunucu tarafı okunabilir |
| **Discord** | **D1** | Bulut, üçüncü taraf |
| **Slack** | D1 | Bulut |
| **WhatsApp** | **D0** | Bulut + şablon zorunluluğu (aşağıya bak) |

> **D3/D4 hiçbir mesajlaşma kanalına gitmez.** Yalnız "kimlikli bir olay var,
> konsola bak" biçiminde **içeriksiz** bir tetikleyici gönderilebilir.

## WhatsApp uyarısı

WhatsApp Business Cloud API'de, kullanıcının son mesajından itibaren **24 saatlik
pencere** dışında yalnız **önceden onaylanmış şablonlar** gönderilebilir.
Bu, ajan-başlatmalı bildirim için WhatsApp'ı **en kötü kanal** yapar.

Kullanılacaksa: yalnız önceden onaylanmış, sabit şablonlarla ve yalnız D0.

## Kanal seçimi — aciliyet × sınıf

| Aciliyet | Kanal |
|---|---|
| Bilgi (günlük özet) | E-posta / Matrix |
| Eylem gerekli (SLA açık) | Telegram / Matrix + e-posta |
| Acil (bütçe hard-stop, bütünlük) | ntfy push + Telegram + e-posta |
| Kritik (hat durdu) | Yukarıdakiler + [[escalating-and-paging]] |

## Gönderim öncesi zorunlu

- [ ] **DLP taraması** — secret, token, kimlik bilgisi, PII (Presidio)
- [ ] Veri sınıfı tavanı kontrolü
- [ ] **Idempotency anahtarı** — retry'da tekrar gönderilmez
- [ ] Rate limit ve sessiz saat politikası
- [ ] Şablon kullanımı — serbest metin değil

## Mesaj içeriği

**Var:** ne oldu, hangi proje/gate, ne gerekiyor, **imzalı derin bağlantı**.
**Yok:** ham veri, claim metni, kanıt içeriği, kimlik bilgisi, iç muhakeme.

> Bildirim bir **işaret fişeğidir**, veri aktarım kanalı değil.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Sonucu mesajda göndersem daha pratik" | Veri sınıfı tavanı. **Bağlantı gönder.** |
| "Gönderilmemiş olabilir, tekrar atayım" | Idempotency anahtarıyla **durumu sorgula**, körlemesine gönderme. |
| "Acil, DLP taramasını atlayalım" | Aciliyet DLP muafiyeti değildir. |
| "Kişisel Telegram'ıma D2 gönderiyorum, sorun yok" | Kanal tavanı kişiye göre değişmez. |

## Kırmızı bayraklar

- `NotificationReceipt` üretilmeyen gönderim
- Aynı olay için iki bildirim (idempotency yok)
- Mesajda claim metni veya ham metrik
