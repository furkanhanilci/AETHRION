# ACC-08 — Strong Counter-Test

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-08` |
| Kategori | Research/Assurance |
| Severity | **Critical** |
| Accountable Owner | Falsification Lead |
| Bağımsız witness/verifier | Assurance Lead / Arbiter |
| İlgili paketler | `WP-077`, `WP-087`, `WP-088`, `WP-089`, `WP-105` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Strong Counter-Test** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Üç reviewer PASS vermiş fakat pre-registered deterministic counter-test claim'i çürütecek fixture'a sahiptir.

**When:** Mechanical verifier counter-test'i frozen target üzerinde çalıştırır.

**Then:** Oy çoğunluğu testin üstüne çıkmaz; claim CHALLENGED/REJECTED olur, DisagreementCase açılır ve G6 geçmez.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | PASS ReviewRecords fixture'ını üret | Execution log + trace/event references |
| 2 | Frozen target ve counter-test hash'ini sabitle | Execution log + trace/event references |
| 3 | Verification Engine ile test çalıştır | Execution log + trace/event references |
| 4 | Finding'i structural/reproducer validation'dan geçir | Execution log + trace/event references |
| 5 | Disagreement/arbitration çalıştır | Execution log + trace/event references |
| 6 | Gate/claim disposition'ı doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Counter-test fail VALIDATED finding olur
- [ ] G6 verdict PASS değildir
- [ ] Claim state CHALLENGED/REJECTED
- [ ] Arbiter evidence rationale taşır
- [ ] Review sayısı anti-metric olarak kalır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `VerificationRecord`
- `ValidatedFinding`
- `DisagreementCase`
- `ClaimAssessment`
- `GateRecord`

## Beklenen olaylar

- `counter_test.failed`
- `finding.validated`
- `disagreement.opened`
- `claim.challenged`
- `gate.blocked`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-08-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-08-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-08-state-before.json` ve `ACC-08-state-after.json`.
- `ACC-08-events.json`, `ACC-08-policy-decisions.json` ve `ACC-08-audit-export.json`.
- `ACC-08-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Fixture claim TEST_CHALLENGED olarak arşivlenir; reviewer calibration datasetine anonim finding eklenir.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
