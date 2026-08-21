# ACC-36 — Model Snapshot Drift

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-36` |
| Kategori | Model/Monitoring |
| Severity | **Critical** |
| Accountable Owner | Eval Office |
| Bağımsız witness/verifier | Model Platform Lead / Safety |
| İlgili paketler | `WP-042`, `WP-044`, `WP-108`, `WP-124` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Model Snapshot Drift** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Provider alias aynı görünürken fingerprint/eval behavior veya dated snapshot değişmiştir; profile açık task'larda kullanılmaktadır.

**When:** Model monitor/qualification check drift'i algılar.

**Then:** Profile suspend/requalification'a gider, router cache invalid olur ve açık task/run/claim için ImpactScan açılır; unsafe fallback yoktur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Admitted profile/fingerprint ve open tasks seed et | Execution log + trace/event references |
| 2 | Changed provider response/fingerprint enjekte et | Execution log + trace/event references |
| 3 | Drift detector/regression eval çalıştır | Execution log + trace/event references |
| 4 | Profile lifecycle/route cache davranışını izle | Execution log + trace/event references |
| 5 | ImpactScan affected set'i doğrula | Execution log + trace/event references |
| 6 | Requalification veya disable disposition yap | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Profile not eligible until qualified
- [ ] New calls old profile'a gitmez
- [ ] Open task impact recall 100% fixture
- [ ] Historical runs unchanged
- [ ] No eligible route BLOCKED
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `CapabilityProfileVersions`
- `DriftReport`
- `RouteDecisions`
- `ImpactCases`
- `AdmissionDecision`

## Beklenen olaylar

- `model.drift_detected`
- `capability.suspended`
- `router.cache_invalidated`
- `impact.scan.started`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-36-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-36-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-36-state-before.json` ve `ACC-36-state-after.json`.
- `ACC-36-events.json`, `ACC-36-policy-decisions.json` ve `ACC-36-audit-export.json`.
- `ACC-36-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Provider fault fixture kaldırılır; profile yalnız requalification kararıyla geri alınır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
