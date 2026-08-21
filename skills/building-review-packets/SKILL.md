---
name: building-review-packets
version: 1.0.0
description: Use when assembling a frozen packet for any reviewer, reproducer or arbiter
gates: [G6, G7]
roles: [Assurance Lead, Platform]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [ReviewPacket]
mechanical_checks: [allowlist_enforced_in_code, packet_hash_recorded, no_inline_context]
---

# Building Review Packets

## Demir kural

> **PAKET BİR PROGRAM TARAFINDAN ÜRETİLİR, BİR PROMPT TARAFINDAN DEĞİL.**

Allowlist kodda tanımlıdır, testi vardır ve ACL ile zorlanır. Bir insanın veya
ajanın "şunu da ekle" demesiyle genişlemez.

## Neden

Reviewer'ın **ne gördüğü** kanıt zincirinin parçasıdır. Prompt ile üretilen
paket denetlenemez; program ile üretilen paket hash'lenebilir.

## Allowlist — pakete girenler

```
protocol_manifest_hash
analysis_plan_hash
literature_set_hash
aggregated_metrics          # dağılım özetleri
figure_digests              # spec_hash + data_hash + renderer_version
claim_drafts
global_constraints          # spec'ten KELİMESİ KELİMESİNE
exclusion_rule_application  # hangi kayıt neden dışlandı
```

## Denylist — asla girmeyenler

```
producer_worktree
intermediate_logs
model_reasoning_traces
self_scores
producer_identity / contact
other_reviewers_verdicts
session_history
```

## Dışlama şeffaflığı

Reviewer yalnız toplu metrik görürse **seçici dışlamayı denetleyemez.**
Bu yüzden `exclusion_rule_application` pakete **girer**: hangi kayıt, hangi
önceden tanımlı kurala göre dışlandı.

Bu, bağlam izolasyonu ile denetlenebilirlik arasındaki gerilimin çözümüdür.

## Teslim biçimi

- **Dosya + hash.** Inline metin yasak.
- Erişim listesi, oluşturma ve son kullanma tarihi
- İndirme takibi açık
- `packet_hash` `ReviewVerdict`'e yazılır

## Kırmızı bayraklar

- Paket elle derlenmiş
- `packet_hash` kaydedilmemiş
- Reviewer'a ek bilgi sohbet içinde verilmiş
- Denylist öğesi pakette
