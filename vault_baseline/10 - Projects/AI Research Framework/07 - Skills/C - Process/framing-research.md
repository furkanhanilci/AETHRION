---
name: framing-research
version: 1.0.0
description: Use when a research idea arrives, when scope is unclear, or before any protocol, experiment or implementation work begins
gates: [G0, G1]
roles: [Scientific Owner, Project Decision Owner, Knowledge Steward]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [ResearchOpportunity, ProjectCharter, RiskProfile]
mechanical_checks: [assurance_class_computed_by_policy_engine, duplicate_scan_executed]
---

# Framing Research

## Genel ilke

Hiçbir iş, ne yapılacağı ve neyin başarı sayılacağı yazılı olmadan başlamaz.

## Önce sınıflandır

| Sınıf | Nedir | Çıktı |
|---|---|---|
| **Exploratory** | Fizibilite / keşif; iddia üretmez | Öneri + `exploratory` etiketli bulgular |
| **Replication** | Mevcut bir sonucun yeniden üretimi | `ReproductionRecord` |
| **Confirmatory** | Yeni iddia üretir | Tam G0–G10 |

> **Şüphedeyken ağır olanı seç.** İki sınıf arasında kararsızsan ağır olanı al.

## Onay kapısı — kaybolmaz

> **Charter onaylanmadan hiçbir ajan sürüsü çalıştırılmaz, hiçbir bütçe açılmaz,
> hiçbir protokol dondurulmaz.**

Töreni ölçeklenir: Exploratory'de iki cümlelik bir çerçeve yeterlidir.
**Kapının kendisi asla kaybolmaz.**

## Prosedür

1. **Mevcut durumu tara** — Knowledge Steward ile duplicate/benzer araştırma sorgusu
2. **Tek tek soru sor** — amaç, kısıt, başarı ölçütü. Mümkünse çoktan seçmeli
3. **Kapsam sorununu hemen bildir** — birden çok bağımsız alt sistem varsa **böl**
4. **RiskProfile vektörünü** doldur (7 boyut) — eksik alan bırakma
5. **AssuranceClass'ı policy engine hesaplar** — model değil
6. **Karar sorusunu insan yazar** — ajan taslak verebilir, sahiplenemez

## Fail-closed sınıflandırma

```
RiskProfile eksikse           → R3
decision_external_impact ≥ material → R3
safety_critical               → R3
data_class ∈ {D3, D4}         → R3
fallthrough (belirsiz)        → R2      # R1 DEĞİL
```

## Yol yükseltme

Gizli karmaşıklık iş sırasında ortaya çıkarsa: **dur, yükseltmeyi ilan et,
ağır seviyeden yeniden başla.** `RiskReclassificationEvent` üretilir; hafif
sınıfta geçilmiş gate'ler yeniden değerlendirilir.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Basit bir soru, charter gereksiz" | **Basit işler varsayımın en pahalıya patladığı yerdir.** Charter kısalır, kaybolmaz. |
| "Sınıfı sonra netleştiririz" | Sınıf gate derinliğini belirler. **Önce.** |
| "R1 gibi duruyor" | Duruyorsa R2 yaz. Şüphe ağır tarafa yazılır. |

## Kırmızı bayraklar

- Karar sorusu bir ajan tarafından yazılmış
- `RiskProfile`'da boş alan var ama sınıf R1
- Kapsam birden çok bağımsız alt sistemi kapsıyor
