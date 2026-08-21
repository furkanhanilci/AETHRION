# ACC-24 — Policy Bundle Rollback

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-24` |
| Kategori | Security/Governance |
| Severity | **High** |
| Accountable Owner | Policy Platform Lead |
| Bağımsız witness/verifier | Safety / Internal Audit |
| İlgili paketler | `WP-056`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Policy Bundle Rollback** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Yeni imzalı policy bundle geçerli workload'u yanlış engelliyor; önceki imzalı bundle bilinmektedir.

**When:** Canary/shadow farkı ve production denial alert'i rollback prosedürünü tetikler.

**Then:** Önceki bundle atomik geri gelir, karar logları/bundle digests korunur, open task'lar yeniden değerlendirilir ve unsafe geçici allow yapılmaz.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Old/new signed bundles ve golden decisions hazırla | Execution log + trace/event references |
| 2 | New bundle canary/shadow diff çalıştır | Execution log + trace/event references |
| 3 | Controlled promote ve expected false denial üret | Execution log + trace/event references |
| 4 | Rollback authorization/procedure uygula | Execution log + trace/event references |
| 5 | PolicyDecision history ve cache convergence kontrol et | Execution log + trace/event references |
| 6 | Affected tasks re-evaluate et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Rollback target signature valid
- [ ] All enforcement points converge
- [ ] Old/new decisions retained
- [ ] No manual permanent bypass
- [ ] Open tasks safe re-evaluation
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `PolicyBundles`
- `Promotion/RollbackDecision`
- `PolicyDecisionLogs`
- `ImpactScanResult`

## Beklenen olaylar

- `policy.bundle.promoted`
- `policy.regression_detected`
- `policy.bundle.rolled_back`
- `task.re_evaluated`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-24-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-24-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-24-state-before.json` ve `ACC-24-state-after.json`.
- `ACC-24-events.json`, `ACC-24-policy-decisions.json` ve `ACC-24-audit-export.json`.
- `ACC-24-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test bundle disabled/revoked; false denial finding correction backlog'una alınır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
