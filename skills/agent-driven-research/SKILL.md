---
name: agent-driven-research
version: 1.0.0
description: Use when dispatching an agent to produce any research artifact, when a produced artifact needs review, or when review findings remain open after fixes
gates: [G2, G3, G5, G6]
roles: [Task Compiler, Assurance Lead]
assurance_classes: [R1, R2, R3]
non_waivable: true
requires_skills: [independence-discipline, requesting-review, receiving-review]
emits: [TaskContract, ProducerReport, ReviewVerdict, FindingLedger]
mechanical_checks: [no_session_history_passed, artifacts_passed_as_files, finding_ledger_complete]
---

# Agent-Driven Research

## Genel ilke

Taze ajan + görev review'u + geniş final review = yüksek kalite, hızlı döngü.

## Dispatch paketi

Her producer dispatch'i **tam olarak** şunları alır:

1. Projedeki yerini anlatan **tek satır**
2. **Task brief dosya yolu** — mekanik olarak çıkarılmış, tam değerlerle
3. Önceki task'ların **yalnız dokunduğu arayüzler**
4. Belirsizlik çözümleri (senin yorumun)
5. Rapor dosyası yolu ve sözleşmesi

**Oturum geçmişi asla geçilmez.**

## Bilgi asimetrisi

| | Producer | Reviewer |
|---|---|---|
| Task brief | ✅ | ✅ |
| Global kısıtlar (spec'ten **kelimesi kelimesine**) | ✅ | ✅ |
| Önceki arayüzler | ✅ | — |
| Producer raporu | yazar | ✅ |
| Üretilen artifact / diff | üretir | ✅ |
| **Producer'ın iç muhakemesi** | — | ❌ **asla** |
| Oturum geçmişi | ❌ | ❌ |

## Dispatch kuralları

- Task başına **taze** ajan
- Task başına **tek** producer dispatch'i — paralel producer yok (çakışma)
- Küçük, aynı şekilli işler **tek dispatch'te** toplanır
- **Bağlam yapıştırma yok** — artifact dosya olarak verilir, inline metin olarak değil
- **Producer asla ajan çağırmaz** (bkz. `independence-discipline`)

## Eskalasyon merdiveni

```
Tur 1–3   Aynı producer. Bağlam korunur.
          Açık bulgular KELİMESİ KELİMESİNE iletilir — özetlenmez.
          Düzeltme raporu AYNI dosyaya EKLENİR (kalıcı hafıza).
          Yalnız değişen kısım yeniden review edilir.

Tur 4–5   TAZE producer, DAHA YETENEKLİ model.
          Çerçeveleme: "Önceki producer bunu N kez denedi; artık senin."

Tur 5+    ►► BREAKER ◄◄
          Dispatch DURUR. İnsan her açık bulguyu tek tek hükme bağlar.
          Her hüküm deftere yazılır. SESSİZ İSKARTA YASAK.
```

## Finding Ledger

`DisagreementCase` yalnızca defterdeki **her satır** `RESOLVED` veya
(gerekçe + sahip + süre ile) `PARKED` olduğunda kapanır.
Statüsüz bulguyla kapanış **yasak**.

## Final review

Görev review'larından ayrı olarak, **bütün paket üzerinde** ve **en yetenekli
modelle** tek bir final review yapılır. Parçaları geçen bir bütün, bütün olarak
tutarsız olabilir.

## Kırmızı bayraklar

- Reviewer'a inline metin geçilmiş
- Bulgular reviewer'a özetlenerek iletilmiş
- Tur sayacı yok
- Defterde statüsüz bulgu var
