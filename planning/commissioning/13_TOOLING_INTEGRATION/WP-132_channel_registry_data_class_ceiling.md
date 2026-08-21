# WP-132 — Kanal Kaydı ve Veri Sınıfı Tavanı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-132` |
| Workstream | `13_TOOLING_INTEGRATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Safety & Governance Owner |
| Bağımsız doğrulayıcı | Platform Security Lead |
| Hard dependencies | WP-131, WP-006 (ExecutionProfile) |
| İlgili gate | Platform |
| İlgili kontroller | CTL-DAT-02, CTL-DAT-03 |
| İlgili ACC senaryoları | ACC-41 |
| İlgili skill | `notifying-humans` |

## Amaç ve beklenen sonuç

Her bildirim kanalı için **veri sınıfı tavanı** kayıt altına alınır ve
kod içinde zorlanır. Tavan bir öneri değil, gönderim öncesi bir kapıdır.

| Kanal | Tavan | Gerekçe |
|---|---|---|
| ntfy (self-hosted) | **D2** | Kendi sunucunuz, dış işleme yok |
| Matrix (self-hosted) | **D2** | E2E şifreleme + kendi homeserver |
| Signal | D2 | E2E; otomasyonu zor |
| E-posta (kendi SMTP) | D1 | Transit şifreli, sunucuda değil |
| Telegram | **D1** | Bulut, sunucu tarafı okunabilir |
| Discord / Slack | **D1** | Bulut, üçüncü taraf |
| **WhatsApp** | **D0** | Bulut + 24 saat penceresi + onaylı şablon zorunluluğu |

> **D3/D4 hiçbir mesajlaşma kanalına gitmez.** Yalnız içeriksiz tetikleyici
> gönderilebilir: "kimlikli bir olay var, konsola bak".

**WhatsApp operasyonel uyarısı:** Business Cloud API'de kullanıcının son
mesajından itibaren 24 saatlik pencere dışında yalnız önceden onaylanmış
şablonlar gönderilebilir. Bu, ajan-başlatmalı bildirim için WhatsApp'ı en
kırılgan kanal yapar; en sona bırakılır.

## Kapsam dışı

- Kanal konnektörlerinin kendi implementasyon detayı (taşıyıcı kütüphane işi)
- Gelen mesaj yönü (WP-136)

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: WP-131, WP-006 (ExecutionProfile)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Tamamlanma kanıtı |
|---|---|---|
| WP-132-T01 | `ChannelRegistry` şemasını tanımla (kanal, tavan, egress host, kimlik) | Şema + kayıt dosyası |
| WP-132-T02 | Tavanı kod içinde zorla; policy engine'e bağla | Tavan üstü gönderim testte reddedilir |
| WP-132-T03 | DLP taraması (secret, token, PII) gönderim öncesi zorunlu | Secret içeren mesaj gönderilmez |
| WP-132-T04 | Şablon kaydı — serbest metin gönderimi kapalı | Şablonsuz gönderim reddedilir |
| WP-132-T05 | İlk kanallar: ntfy (self-hosted) + Telegram | İki kanal uçtan uca çalışır |
| WP-132-T06 | Egress allowlist'i her kanal için ayrı tanımla | Allowlist dışı host'a çıkış engellenir |

## Zorunlu teslimatlar

- `ChannelRegistry` şeması ve dolu kayıt
- Veri sınıfı tavanı zorlaması (kod + test)
- DLP tarama entegrasyonu
- Mesaj şablon kaydı
- Kanal başına egress allowlist

## Test ve doğrulama planı

- **Tavan zorlaması:** her kanal için tavan+1 sınıfında içerik → gönderim reddedilir
- **D3/D4:** hiçbir kanala içerik gitmez; yalnız içeriksiz tetikleyici üretilir
- **DLP:** API anahtarı, token ve PII içeren örnek mesajlar yakalanır
- **Şablon:** serbest metin gönderimi reddedilir
- **Egress:** allowlist dışı host'a giden istek engellenir

## Kabul kriterleri

- [ ] Kanal başına tavan **kodda** tanımlı ve testle zorlanıyor; yalnız dokümanda değil
- [ ] D3/D4 içerik hiçbir kanaldan çıkamaz (negatif test)
- [ ] DLP taraması atlanabilir bir yol yok
- [ ] WhatsApp yalnız D0 ve yalnız onaylı şablonla erişilebilir
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.

## Riskler ve kontrol noktaları

- Kanal tavanı kişiye göre değişmez; "benim kendi Telegram'ım" istisnası yoktur
- Yeni kanal eklemek Safety/Data Owner onayı ve yeni bir tavan kaydı gerektirir
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Kanal kaydından çıkarılır; bekleyen mesajlar o kanal için düşürülmez, kuyrukta
kalır ve alternatif kanala yönlendirilmez (yönlendirme tavan ihlali doğurabilir).

## Handoff ve sonraki paketlere giriş

WP-133 ve WP-134 bu kayıttaki kanalları kullanır. Kayıtta olmayan kanal
kullanılamaz.
