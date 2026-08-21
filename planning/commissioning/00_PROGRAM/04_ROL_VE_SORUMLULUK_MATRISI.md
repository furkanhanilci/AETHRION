# Rol ve Sorumluluk Matrisi

## Kalıcı program fonksiyonları

| Fonksiyon | Accountable rol | Sorumluluk |
|---|---|---|
| Research Strategy & Portfolio | Research Director | Değer, portföy, stop/pivot/continue |
| Scientific Discovery | Scientific Owner | Soru, yöntem, literatür, yorum |
| Engineering & Platform | Chief Architect / Platform Lead | Sistem, contract, execution ve release |
| Evaluation & Assurance | Assurance Lead | Review, falsification, verifier, reproduction |
| Safety & Governance | Safety & Governance Owner | Risk, data, policy, exception ve veto |
| Knowledge & Communication | Knowledge Lead | Source, Zotero, Obsidian, publication ve archive |
| Operations & Economics | SRE Lead / FinOps Lead | SLO, incident, DR, kapasite ve maliyet |

## Paket rol modeli

Her iş paketinde en az şu roller atanır:

- `A — Accountable`: Kabul veya risk kararının tek sahibi.
- `R — Responsible`: Uygulayan kişi/ekip; birden çok olabilir.
- `V — Verifier`: Üreticiden bağımsız test ve evidence doğrulayıcı.
- `C — Consulted`: Contract, güvenlik, bilim veya operasyon uzmanı.
- `I — Informed`: Downstream owner ve program yönetimi.

## Karar hakları

| Karar | Accountable | Bağımsız kontrol | Devredilebilirlik |
|---|---|---|---|
| ProjectCharter kabulü | Project Decision Owner | Research Director/Safety | R1 sınırında süreli olabilir |
| Protocol freeze | Scientific Owner | Methodologist/Statistician | Material protokolde hayır |
| Literature set freeze | Evidence Lead | Citation Auditor/Methodologist | R1'de kapsamlı delegation olabilir |
| Compute/budget açma | Scientific + FinOps Owner | Safety/Platform | Hard limit override devredilemez |
| Review disposition | Assurance Lead | Mechanical verifier/Arbiter | Kritik blocker waiver yok |
| Clean-room certificate | Reproduction Owner | Assurance Lead | Producer'a devredilemez |
| Residual risk kabulü | Project Decision Owner | Safety/Assurance | R3'te devredilemez |
| Publication/release | Project Decision Owner | Provenance/Citation/Safety | Devredilemez |
| Production cutover | Executive Sponsor + SRE/Safety | Commissioning Board | Devredilemez |

## Küçük ekipte rol birleştirme

Aynı kişi birden çok şapka taşıyabilir; fakat aynı artifact üzerinde gerekli bağımsızlık boyutları sağlanmalıdır. R1'de aynı insan gözetiminde farklı model ailesi, context izolasyonu ve ayrı credential yeterli olabilir. R3'te producer, reviewer ve reproducer için insan boyutu dahil tam ayrım gerekir. Sağlanamıyorsa görev `BLOCKED` kalır.

## Escalation zinciri

```text
Implementer → Package Owner → Workstream Lead
            → Chief Architect / Assurance / Safety (konuya göre)
            → Project Decision Owner
            → Executive Sponsor / Commissioning Board
```

Timeout otomatik onaya dönüşmez. SLA dolduğunda karar bir üst role eskale olur veya workflow pause kalır.

