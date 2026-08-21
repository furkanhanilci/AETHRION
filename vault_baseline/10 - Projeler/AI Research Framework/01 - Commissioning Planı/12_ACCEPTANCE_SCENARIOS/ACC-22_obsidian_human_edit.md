# ACC-22 — Obsidian Human Edit Preservation

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-22` |
| Kategori | Knowledge |
| Severity | **High** |
| Accountable Owner | Knowledge Lead |
| Bağımsız witness/verifier | Knowledge Curator |
| İlgili paketler | `WP-073`, `WP-074`, `WP-113` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Obsidian Human Edit Preservation** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Bir Obsidian notunda human-authored alan ve generated block vardır; insan generated refresh ile eşzamanlı kendi alanını değiştirir.

**When:** Projection renderer yeni source/claim state'iyle notu yeniler.

**Then:** İnsan alanı byte/semantic olarak korunur, yalnız generated zone güncellenir; unexpected conflict otomatik overwrite yerine curator case açar.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Vault test branch/base hash al | Execution log + trace/event references |
| 2 | Human zone'a edit uygula | Execution log + trace/event references |
| 3 | Canonical claim update event üret | Execution log + trace/event references |
| 4 | Renderer refresh'i eşzamanlı çalıştır | Execution log + trace/event references |
| 5 | Git diff/zone parser/link integrity kontrol et | Execution log + trace/event references |
| 6 | Zone dışı conflict fixture'ı dene | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Human content unchanged
- [ ] Generated block new provenance/version taşır
- [ ] Git history complete
- [ ] Zone conflict case açılır
- [ ] Broken link yok veya curator queue'dadır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `VaultCommit`
- `ProjectionRecord`
- `HumanPreservationDiff`
- `ConflictCase`
- `LinkIntegrityReport`

## Beklenen olaylar

- `knowledge.projection.requested`
- `obsidian.generated_updated`
- `human_edit.preserved`
- `reconciliation.required`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-22-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-22-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-22-state-before.json` ve `ACC-22-state-after.json`.
- `ACC-22-events.json`, `ACC-22-policy-decisions.json` ve `ACC-22-audit-export.json`.
- `ACC-22-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
- Bağımsız witness `VerificationRecord` ve varsa finding/disposition kayıtları.

## PASS ölçütü

- Bütün scenario-specific assertions ve ortak integrity assertions geçer.
- Beklenen fail-closed/block/revise davranışı happy-path başarı kadar geçerli bir PASS olabilir; beklenen state ile aynı olmalıdır.
- Açık Critical/High finding yoktur.
- Kanıt manifesti eksiksiz, hashleri doğrulanmış ve witness tarafından imzalanmıştır.
- Aynı release candidate dışındaki sonuçlar birleştirilmemiştir.

## FAIL ve yeniden test

Bir invariant, kanıt bütünlüğü veya beklenen kayıt/event assertion'ı başarısızsa senaryo FAIL olur. Correction yalnız VALIDATED finding üzerinden açılır. Target revision veya ilgili policy/schema/model/tool bundle değişirse önceki sonuç geçersiz olur; senaryo ve etkilenen regression kümesi yeniden çalıştırılır.

## Cleanup ve geri dönüş

Test branch archive/delete; human fixture baseline Git history'de test tag'iyle tutulur.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
