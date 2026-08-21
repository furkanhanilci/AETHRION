# ACC-13 — Temporal Worker Crash

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-13` |
| Kategori | Reliability/Control |
| Severity | **Critical** |
| Accountable Owner | Control Plane Lead |
| Bağımsız witness/verifier | Independent SRE |
| İlgili paketler | `WP-031`, `WP-040`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Temporal Worker Crash** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Activity ortasında olan açık ProjectWorkflow ve idempotent external operation vardır.

**When:** Worker process node ile birlikte öldürülür ve activity timeout/retry gerçekleşir.

**Then:** Workflow history/state kaybolmaz; activity retry/reconcile eder, duplicate effect üretmez ve yeni worker devam eder.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Açık workflow/activity fixture'ını başlat | Execution log + trace/event references |
| 2 | External operation pre/post commit kill noktalarını kaydet | Execution log + trace/event references |
| 3 | Worker/node kill enjekte et | Execution log + trace/event references |
| 4 | Timeout/retry ve yeni worker poll gözle | Execution log + trace/event references |
| 5 | Workflow/gate/artifact state karşılaştır | Execution log + trace/event references |
| 6 | Duplicate effect ve audit query çalıştır | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Workflow state RPO=0
- [ ] Tek external effect
- [ ] Activity attempt history görünür
- [ ] New worker resumes
- [ ] No unsafe PASS transition
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `TemporalHistory`
- `ActivityAttempts`
- `ToolReceipt/ArtifactRecord`
- `WorkflowState`
- `FailureInjectionRecord`

## Beklenen olaylar

- `worker.lost`
- `activity.timed_out`
- `activity.retried_or_reconciled`
- `workflow.resumed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-13-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-13-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-13-state-before.json` ve `ACC-13-state-after.json`.
- `ACC-13-events.json`, `ACC-13-policy-decisions.json` ve `ACC-13-audit-export.json`.
- `ACC-13-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Fault kaldırılır; worker capacity restore, fixture workflow controlled completion/cancel ile kapanır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
