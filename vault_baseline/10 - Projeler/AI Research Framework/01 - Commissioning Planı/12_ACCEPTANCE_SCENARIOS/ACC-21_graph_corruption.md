# ACC-21 — Derived Graph Corruption ve Rebuild

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-21` |
| Kategori | Data/Knowledge |
| Severity | **High** |
| Accountable Owner | Knowledge Data Lead |
| Bağımsız witness/verifier | Data Platform Lead / Assurance |
| İlgili paketler | `WP-030`, `WP-074`, `WP-113`, `WP-114` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Derived Graph Corruption ve Rebuild** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Neo4j/pgvector/OpenSearch derived read modelinde bilerek node/edge/index corruption vardır; canonical records sağlamdır.

**When:** Integrity check corruption'ı bulur ve full rebuild/swap procedure çalışır.

**Then:** Canonical service etkilenmez; yeni projection beklenen count/hash/lineage ile kurulur ve atomik promote edilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Canonical fixture snapshot/count/hash al | Execution log + trace/event references |
| 2 | Derived node/edge/index boz | Execution log + trace/event references |
| 3 | Integrity monitor alarmını doğrula | Execution log + trace/event references |
| 4 | New namespace full replay/rebuild yap | Execution log + trace/event references |
| 5 | Canonical vs projection reconciliation çalıştır | Execution log + trace/event references |
| 6 | Alias/read traffic swap ve old index retire et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Canonical mutation yok
- [ ] Corruption detected
- [ ] Rebuild count/hash fixture ile eşleşir
- [ ] Claim lineage query tam
- [ ] Downtime/SLO policy içinde
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `ProjectionIntegrityRecord`
- `RebuildManifest`
- `ReconciliationReport`
- `AliasPromotionDecision`

## Beklenen olaylar

- `projection.corrupt`
- `projection.rebuild_started`
- `projection.verified`
- `projection.promoted`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-21-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-21-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-21-state-before.json` ve `ACC-21-state-after.json`.
- `ACC-21-events.json`, `ACC-21-policy-decisions.json` ve `ACC-21-audit-export.json`.
- `ACC-21-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Corrupt test index delete; new test projection test alias'tan çıkarılır veya baseline'a döndürülür.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
