---
name: writing-protocols
version: 1.0.0
description: Use when authoring a ProtocolManifest, when freezing method at G2, or when a material method change requires a new protocol version
gates: [G2]
roles: [Scientific Owner, Statistical Methods Owner, Red Team Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [writing-analysis-plans]
emits: [ProtocolManifest, InPrincipleAcceptance]
mechanical_checks: [no_placeholders, required_sections_present, falsification_plan_nonempty]
---

# Writing Protocols

## Genel ilke

Protokol, sonucu görmeden yazılan sözleşmedir. Uygulayıcının yorumuna alan
bırakmaz.

## Zorunlu bölümler

`hypotheses` · `variables` · `dataset` · `baseline` · `success_metrics` ·
`falsification_plan` · `stop_rules` · `exclusion_rules` · `uncertainty` ·
`material_changes`

Eksik bölüm → `GATE_FAIL`. Mekanik kontrol.

## Placeholder yasağı

Yasak ifadeler: `TBD`, `edge case'leri ele al`, `benzer şekilde`,
`gerektiğinde ayarla`, `uygun bir eşik`, `standart yöntem`.

Her değer **tam** yazılır: eşik sayısı, tekrar sayısı, tolerans, sürüm.

## Dışlama kuralları — özel dikkat

`exclusion_rules` sonuçları şekillendirebilecek en tehlikeli alandır.
Her kural için **gerekçe ve önceden tanımlı eşik** zorunludur.

> Dışlama kuralı sonuçlar görüldükten sonra eklenemez veya değiştirilemez.
> Değişirse yeni `ProtocolManifest` versiyonu ve `exploratory` etiketi.

## Falsification ve severity

Her hipotez için: *"Bu iddia yanlış olsaydı, hangi gözlem bunu gösterirdi?"*
Ve ardından: *"Bu test onu **yakalar mıydı**?"* — güç değerlendirmesi
Statistical Methods Owner tarafından imzalanır.

Yakalamayan test kanıt üretmez.

## Pre-mortem (R2, R3)

G4 öncesi Red Team: *"Bir yıl geçti, proje tamamen başarısız oldu. Neden?"*
Çıkan maddeler `falsification_plan`'a eklenir.

## Öz-review kontrol listesi

Protokol insan onayına gitmeden önce **kendisi** kontrol edilir:

- [ ] Her gereksinim bir bölüme eşleniyor
- [ ] Hiçbir placeholder yok
- [ ] Değişken adları ve tipleri bölümler arası tutarlı
- [ ] Stop rule ile success metric çelişmiyor
- [ ] Dışlama kuralları önceden tanımlı ve gerekçeli

Geçemezse insan zamanı harcanmaz.

## Kırmızı bayraklar

- `success_metrics` var ama `falsification_plan` yok
- Eşik değeri "uygun görülen" gibi bir ifadeyle geçilmiş
- Protokol ve analiz planı aynı dosyada
