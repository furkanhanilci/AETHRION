# ACC-12 — Duplicate Event Delivery

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-12` |
| Kategori | Reliability/Event |
| Severity | **Critical** |
| Accountable Owner | Event Platform Lead |
| Bağımsız witness/verifier | Independent SRE |
| İlgili paketler | `WP-028`, `WP-039`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Duplicate Event Delivery** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Bir business mutation event'i canonical kayıttan yayımlanmış ve consumer idempotency store bozulmamıştır.

**When:** Aynı event_id/idempotency_key iki veya daha çok kez teslim edilir; consumer ilk commit sonrası crash de eder.

**Then:** Tek business effect oluşur, duplicate ACK/audit edilir ve side effect ikinci kez yapılmaz.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Canonical record+outbox event üret | Execution log + trace/event references |
| 2 | Consumer'a duplicate delivery enjekte et | Execution log + trace/event references |
| 3 | İlk business commit sonrası ACK öncesi process kill yap | Execution log + trace/event references |
| 4 | Consumer restart/re-delivery yap | Execution log + trace/event references |
| 5 | DB/external effect/audit/offset'i karşılaştır | Execution log + trace/event references |
| 6 | Replay_mode ile tekrar dene | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Business effect count=1
- [ ] Unique idempotency record=1
- [ ] ACK canonical commit sonrası
- [ ] Replay external mutation yapmaz
- [ ] Audit duplicate disposition taşır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `OutboxRecord`
- `ConsumerIdempotencyRecord`
- `BusinessRecord`
- `AuditRecord`
- `ConsumerOffset`

## Beklenen olaylar

- `event.published`
- `consumer.effect_committed`
- `event.duplicate_ignored`
- `event.acked`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-12-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-12-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-12-state-before.json` ve `ACC-12-state-after.json`.
- `ACC-12-events.json`, `ACC-12-policy-decisions.json` ve `ACC-12-audit-export.json`.
- `ACC-12-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test consumer/stream fixture purge değil scoped cleanup ile kaldırılır; audit/evidence retained.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
