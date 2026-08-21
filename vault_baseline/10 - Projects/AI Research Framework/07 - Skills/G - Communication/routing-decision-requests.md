---
name: routing-decision-requests
version: 1.0.0
description: Use when a human decision or approval is required, when a DecisionRequest enters the queue, or when an approval arrives through a messaging channel
gates: [G1, G4, G8, G9]
roles: [Notification Broker, Project Decision Owner, Safety/Data Owner]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [notifying-humans]
emits: [DecisionRequest, DecisionRecord]
mechanical_checks: [approval_surface_authenticated, deep_link_signed_and_expiring, no_approval_via_chat_reply]
---

# Routing Decision Requests

## Demir kural

> **MESAJLAŞMA BİR BİLDİRİM KANALIDIR, YETKİLENDİRME KANALI DEĞİL.**
>
> Hiçbir karar bir sohbet cevabıyla verilemez.

## Neden

Telegram/Discord/WhatsApp/e-posta hesapları ele geçirilebilir, taklit
edilebilir, iletilir. Bir `DecisionRecord` **imzalı ve hukuken bağlayıcı**
bir kayıttır. Kanıt zincirinin sonunu bir sohbet mesajına bağlamak, tüm
zinciri o kanalın güvenliğine indirger.

`ACC-25 Human Approval Forgery` senaryosunun önleyici tarafı budur.

## Doğru akış

```
1. DecisionRequest kuyruğa girer
2. Bildirim gönderilir: "Karar bekliyor — <proje> <gate>"
   + İMZALI, SÜRELİ, TEK KULLANIMLIK derin bağlantı
3. İnsan bağlantıyı açar → KİMLİK DOĞRULAMALI YÜZEYE gider
4. Dondurulmuş kanıt paketini görür
5. Kararı ORADA verir → DecisionRecord imzalanır
6. Onay bildirimi geri gönderilir
```

## Derin bağlantı kuralları

- İmzalı (HMAC veya asimetrik)
- **Süreli** — kısa TTL
- **Tek kullanımlık**
- Karar yetkisini değil, **yüzeye erişimi** taşır
- Yönlendirilirse geçersiz (kullanıcı-bağlı)

## Sohbet cevabı ne yapabilir

| Eylem | İzin |
|---|---|
| "Gördüm" / okundu bilgisi | ✅ |
| Ek bilgi isteme | ✅ — kuyruğa not düşer |
| SLA uzatma talebi | ✅ — talep, karar değil |
| **Onay / ret** | ❌ **asla** |
| **Yıkıcı işlem** (`RETRACT` vb.) | ❌ **asla** |

## Zaman aşımı

> **Otomatik onay yoktur.** SLA dolduğunda ya bir üst role eskale olur ya da
> workflow pause kalır. Sessizlik onay değildir.

## Dikkat bütçesi

Karar kuyruğu **sert kotalıdır** (ör. haftada 5 G8 kararı). Kota dolduğunda
kuyruk **bekler**. Hızlı gözden geçirme modu yoktur.

Ölçülen: karar süresi dağılımı, açılan kanıt bölümleri, G10'da geri alma
oranı, adversarial `REJECT`'e rağmen `ACCEPT` oranı.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Telegram'dan 'onaylıyorum' yazdım, yeterli" | **Değil.** Bağlantıyı aç, yüzeyde onayla. |
| "Acil, hızlı onaylayalım" | Aciliyet kimlik doğrulama muafiyeti değildir. |
| "Ben zaten tek kullanıcıyım" | Hesap ele geçirilmesi tek kullanıcıda da olur. |
| "Bot benim olduğumu biliyor" | Bot kanalın kimliğini bilir, kişinin değil. |

## Kırmızı bayraklar

- `DecisionRecord` kaynağı bir mesajlaşma kanalı
- Derin bağlantı süresiz veya çok kullanımlık
- SLA dolunca durum otomatik ilerlemiş
