---
name: escalating-and-paging
version: 1.0.0
description: Use when an SLA is breached, when a budget hard limit is hit, when a pipeline integrity alert fires, or when a decision has been pending beyond its deadline
gates: [G0, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10]
roles: [Notification Broker, SRE Lead, Assurance Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [notifying-humans]
emits: [EscalationRecord]
mechanical_checks: [no_auto_approve_on_timeout, escalation_chain_followed, acknowledgement_required]
---

# Escalating and Paging

## Demir kural

> **ZAMAN AŞIMI ASLA OTOMATİK ONAYA DÖNÜŞMEZ.**
>
> Ya bir üst role eskale olur ya da workflow pause kalır.

## Eskalasyon zinciri

```
Uygulayıcı → Paket Sahibi → Workstream Lead
           → Chief Architect / Assurance / Safety (konuya göre)
           → Project Decision Owner
           → Executive Sponsor / Commissioning Board
```

Her basamakta **onaylama (acknowledgement) zorunlu**. Onaylanmayan eskalasyon
bir sonraki basamağa çıkar; kaybolmaz.

## Tetikleyiciler ve şiddet

| Tetikleyici | Şiddet | Kanal |
|---|---|---|
| Gate SLA 1 gün aşıldı | WARN | E-posta |
| Gate SLA 3 gün aşıldı | HIGH | Telegram + e-posta |
| Bütçe %80 | WARN | E-posta |
| **Bütçe hard limit** | **CRITICAL** | Push + Telegram + e-posta; **işler durur** |
| Anomali 3. düzeltme denemesi | HIGH | Assurance Lead |
| **Bütünlük şüphesi** | **CRITICAL** | Research Integrity Officer, doğrudan |
| **Negatif kontrolde bulgu** | **CRITICAL** | Hat durur; Metascience Lead |
| `ORPHANED` kanıt | CRITICAL | ImpactCase + Knowledge Steward |
| Tool Broker hata oranı > eşik | HIGH | SRE |
| Sandbox kaçış girişimi | **CRITICAL** | Güvenlik + hat durur |

## Sessiz saatler

Sessiz saat politikası vardır — **ama `CRITICAL` onu delip geçer.** Bütünlük,
güvenlik ve bütçe hard-stop beklemez.

## Gürültü kontrolü

Aynı olay için tekrar eden eskalasyon **birleştirilir**, tekrar gönderilmez.
Eskalasyon yorgunluğu, eskalasyonun kendisinden daha tehlikelidir.

Ölçülen: eskalasyon başına ortalama yanıt süresi, onaylanmayan oranı,
yanlış pozitif oranı. Yüksek yanlış pozitif → eşikler yeniden ayarlanır.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Kimse cevap vermiyor, devam edelim" | **Hayır.** Pause veya üst basamak. |
| "Gece, sabah bakarız" | `CRITICAL` sessiz saat tanımaz. |
| "Zaten haberdar" | Onaylama kaydı yoksa haberdar değildir. |
| "Bu eşik çok hassas, kapatalım" | Eşiği **ölçerek** ayarla, kapatma. |

## Kırmızı bayraklar

- SLA dolduktan sonra durum kendiliğinden ilerlemiş
- `CRITICAL` bildirimi sessiz saatte bastırılmış
- Onaylanmamış eskalasyon üst basamağa çıkmamış
