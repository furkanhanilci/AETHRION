# ACC-33 — Kueue Preemption

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-33` |
| Kategori | Execution/Reliability |
| Severity | **High** |
| Accountable Owner | Compute Platform Lead |
| Bağımsız witness/verifier | SRE / Assurance |
| İlgili paketler | `WP-053`, `WP-083`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Kueue Preemption** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Düşük öncelikli scout workload kaynak tüketirken kritik reproduction queue kapasite ister.

**When:** Kueue priority/preemption policy çalışır.

**Then:** Scout checkpoint/pause/evict edilir, kritik repro kabul edilir; canonical task state/artifact kaybolmaz ve scout daha sonra resume olur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Low-priority checkpoint-capable scout başlat | Execution log + trace/event references |
| 2 | Queue/resource saturation oluştur | Execution log + trace/event references |
| 3 | Critical reproduction workload submit et | Execution log + trace/event references |
| 4 | Preemption/lease/budget/checkpoint events izle | Execution log + trace/event references |
| 5 | Repro tamamla | Execution log + trace/event references |
| 6 | Scout re-admit/resume ve state compare et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Critical repro wait SLO içinde
- [ ] Scout state/artifacts preserved
- [ ] No duplicate scout work effect
- [ ] Budget reservations correct
- [ ] Priority rule/audit visible
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `WorkloadRecords`
- `CheckpointArtifact`
- `KueueAdmission`
- `ExecutionLeases`
- `CostReservations`

## Beklenen olaylar

- `workload.preempted`
- `checkpoint.captured`
- `reproduction.admitted`
- `workload.resumed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-33-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-33-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-33-state-before.json` ve `ACC-33-state-after.json`.
- `ACC-33-events.json`, `ACC-33-policy-decisions.json` ve `ACC-33-audit-export.json`.
- `ACC-33-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Fixture workloads complete/cancel; queue quotas baseline'a döner.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
