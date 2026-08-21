# ACC-11 — No Eligible Fallback

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-11` |
| Kategori | Reliability/Model |
| Severity | **Critical** |
| Accountable Owner | Model Platform Lead |
| Bağımsız witness/verifier | Safety Owner |
| İlgili paketler | `WP-041`, `WP-045`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **No Eligible Fallback** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Primary provider down ve alternatiflerin hiçbiri task'ın D3/data-region/tool/risk/independence şartlarını karşılamamaktadır.

**When:** Router fallback arar.

**Then:** Unsafe route seçilmez; task/workflow BLOCKED olur, insan planlama/escalation kuyruğu açılır.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | D3 critical TaskContract oluştur | Execution log + trace/event references |
| 2 | Primary outage enjekte et | Execution log + trace/event references |
| 3 | Alternatif profilleri her farklı policy nedeni ile ineligible yap | Execution log + trace/event references |
| 4 | Router decision ve candidate filtering'i al | Execution log + trace/event references |
| 5 | Workflow/decision queue'yu kontrol et | Execution log + trace/event references |
| 6 | Policy bypass denemesi yap | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Model call sayısı 0
- [ ] RouteDecision NO_ELIGIBLE_ROUTE
- [ ] Workflow BLOCKED
- [ ] Bütün candidate denial rule'ları görünür
- [ ] Bypass/unknown allow olmaz
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `RouteDecision`
- `PolicyDecisions`
- `WorkflowState`
- `DecisionRequest`

## Beklenen olaylar

- `route.no_eligible_profile`
- `workflow.blocked`
- `decision.required`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-11-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-11-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-11-state-before.json` ve `ACC-11-state-after.json`.
- `ACC-11-events.json`, `ACC-11-policy-decisions.json` ve `ACC-11-audit-export.json`.
- `ACC-11-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Fault/policy fixtures temizlenir; task TEST_CANCELLED veya eligible profile sonrası yeni attempt olarak kapatılır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
