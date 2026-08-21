# ACC-31 — Superseded Publication

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-31` |
| Kategori | Publication/Monitoring |
| Severity | **High** |
| Accountable Owner | Publication Owner |
| Bağımsız witness/verifier | Archivist / Citation Auditor |
| İlgili paketler | `WP-090`, `WP-106`, `WP-108`, `WP-113` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Superseded Publication** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Yayınlanmış package için yeni evidence/decision düzeltilmiş replacement publication gerektirir.

**When:** Yeni package yayınlanır ve supersession relation/event işlenir.

**Then:** Eski package erişilebilir fakat açıkça superseded; yeni package predecessor ve reason'a bağlı, tüketiciler impact event alır.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Publication v1 fixture ve stable URL/hash hazırla | Execution log + trace/event references |
| 2 | New claim/decision/package v2 üret | Execution log + trace/event references |
| 3 | Supersession decision ve release çalıştır | Execution log + trace/event references |
| 4 | v1/v2 landing metadata/linkleri sorgula | Execution log + trace/event references |
| 5 | Search/index/consumer/Obsidian projection güncellemesini izle | Execution log + trace/event references |
| 6 | Audit chain verify et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] v1 bytes/hash unchanged and accessible
- [ ] v1 superseded banner/link
- [ ] v2 supersedes v1 and reason
- [ ] Consumers notified once
- [ ] Ledger/history complete
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `PublicationPackages v1/v2`
- `SupersessionRecord`
- `DecisionRecord`
- `ProjectionRecords`
- `AuditExport`

## Beklenen olaylar

- `publication.released`
- `publication.superseded`
- `consumers.impact_notified`
- `knowledge.projection_updated`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-31-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-31-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-31-state-before.json` ve `ACC-31-state-after.json`.
- `ACC-31-events.json`, `ACC-31-policy-decisions.json` ve `ACC-31-audit-export.json`.
- `ACC-31-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Synthetic publications TEST/unpublished visibility'ye alınır; supersession chain retained.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
