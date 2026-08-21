# ACC-34 — DLQ Repair ve Corrected Replay

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-34` |
| Kategori | Event/Reliability |
| Severity | **High** |
| Accountable Owner | Event Platform Lead |
| Bağımsız witness/verifier | SRE / Schema Owner |
| İlgili paketler | `WP-028`, `WP-039`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **DLQ Repair ve Corrected Replay** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Consumer için incompatible/poison payload vardır.

**When:** Consumer validation fail eder, event DLQ'ya gider ve repair workflow düzeltici adapter/schema ile replay yapar.

**Then:** Consumer loop oluşmaz; owner/diagnostic/audit tam, corrected event bir kez işlenir ve original causation korunur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Poison event fixture publish et | Execution log + trace/event references |
| 2 | Validation/retry threshold ve DLQ transferini izle | Execution log + trace/event references |
| 3 | DLQ case/owner/diagnostic kontrol et | Execution log + trace/event references |
| 4 | Schema adapter veya corrected payload üret | Execution log + trace/event references |
| 5 | Dry-run sonra corrected replay yap | Execution log + trace/event references |
| 6 | Business effect/idempotency/offset/audit doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Original event business effect=0
- [ ] DLQ one record/no loop
- [ ] Corrected effect count=1
- [ ] Causation/original ref retained
- [ ] Queue drains
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `DLQRecord`
- `RepairCase`
- `CorrectedEvent`
- `ConsumerIdempotencyRecord`
- `AuditRecord`

## Beklenen olaylar

- `event.rejected`
- `event.dlq_entered`
- `event.repaired`
- `event.replayed`
- `consumer.effect_committed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-34-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-34-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-34-state-before.json` ve `ACC-34-state-after.json`.
- `ACC-34-events.json`, `ACC-34-policy-decisions.json` ve `ACC-34-audit-export.json`.
- `ACC-34-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test DLQ case CLOSED; fixture subject/consumer cleanup ve retained evidence.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
