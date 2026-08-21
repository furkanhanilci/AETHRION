---
name: arbitrating-disagreement
version: 1.0.0
description: Use when reviewer verdicts conflict, when a producer disputes a finding, or when a finding remains open after repeated fix rounds
gates: [G6]
roles: [Assurance Lead, Arbiter]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [agent-driven-research]
emits: [DisagreementCase, FindingLedger, ArbitrationRecord]
mechanical_checks: [finding_ledger_complete, round_counter_present]
---

# Arbitrating Disagreement

## Genel ilke

Uyuşmazlık bir arıza değil, sistemin bilgi ürettiği andır. Sessizce kapanamaz.

## Demir kural

> **HİÇBİR AÇIK BULGU STATÜSÜZ KAPANAMAZ.**
>
> Her bulgu ya `RESOLVED` ya da gerekçe + sahip + süre ile `PARKED`.

## Delphi turları — tek hakem yerine

```
Tur 1  N reviewer bağımsız verdict + gerekçe. Birbirini GÖRMEZ.

Tur 2  Anonimleştirilmiş gerekçe özeti dağıtılır.
       Herkes verdict'ini revize edebilir.
       ►► DEĞİŞTİREN GEREKÇE YAZMAK ZORUNDA ◄◄

Tur 3  Hâlâ uzlaşma yoksa → insan Arbiter.
       Arbiter TÜM turları görür — yalnız son durumu değil.
```

**Yakınsama ölçülür.** Turlar arası verdict değişim oranı kaydedilir.
Çok hızlı yakınsama = sürü etkisi şüphesi → Metascience'a sinyal.

## Arbiter'ın soruları

1. **Locator kontrolü** — verdict'ler aynı kanıtı mı gördü?
2. **Tanım hizalaması** — tartışma terim tanımından mı kaynaklanıyor?
3. **Kapsam** — kısıtlama uyuşmazlığı çözer mi?
4. **Karşı test** — hangi ek gözlem bunu kesin çözerdi?

## Çözüm biçimleri

| Çözüm | Ne zaman |
|---|---|
| `ACCEPT` | Bulgu geçersiz veya karşılanmış |
| `QUALIFIED_ACCEPT` | Kapsam kısıtı uyuşmazlığı çözüyor |
| `REJECT` | Bulgu geçerli ve giderilemiyor |
| `ADVERSARIAL_COLLABORATION` | Uyuşmazlık gerçek ve derin |

## Adversarial collaboration — R3 varsayılanı

Arbitration çözemezse: **iki taraf birlikte** anlaşmazlığı çözecek deneyi
tasarlar ve **hangi sonucun ne anlama geleceğini önceden** yazar. Yeni bir
`ProtocolManifest` üretilir.

Pahalıdır. Ama tek kesin çözümdür ve karar sonuca bakılarak yapılamaz.

## Breaker

Tur 5 sonunda hâlâ açıksa: dispatch durur, **insan her bulguyu tek tek hükme
bağlar**, her hüküm deftere yazılır.

## Kırmızı bayraklar

- Arbiter yalnız son verdict'leri görmüş
- Verdict değiştiren reviewer gerekçe yazmamış
- Defterde statüsüz satır varken case kapanmış
- Tek turda tam uzlaşma (κ ≈ 1.0)
