# ACC-14 — Workflow Code Deploy ve Replay

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-14` |
| Kategori | Reliability/Control |
| Severity | **Critical** |
| Accountable Owner | Platform Assurance Lead |
| Bağımsız witness/verifier | Control Plane Reviewer |
| İlgili paketler | `WP-032`, `WP-040`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Workflow Code Deploy ve Replay** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Eski worker build ile farklı gate'lerde pause/active açık workflow history'leri vardır.

**When:** Yeni workflow kodu replay CI ve versioned deployment'tan geçirilir.

**Then:** Bütün golden/açık histories deterministik replay eder; uyumsuz workflow uygun worker version'da kalır ve state drift olmaz.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Temsilci histories snapshot al | Execution log + trace/event references |
| 2 | Yeni build replay suite çalıştır | Execution log + trace/event references |
| 3 | Patch/version marker paths doğrula | Execution log + trace/event references |
| 4 | Canary worker queue'ya deploy et | Execution log + trace/event references |
| 5 | Açık workflow update/query/activity test et | Execution log + trace/event references |
| 6 | Eski worker drain/rollback prova et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Replay error=0
- [ ] History-derived state before/after aynı
- [ ] Version marker deterministic
- [ ] Incompatible build promote olmaz
- [ ] Open workflows orphan olmaz
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `ReplayReport`
- `WorkerBuildManifest`
- `DeploymentRecord`
- `WorkflowStateDiff`

## Beklenen olaylar

- `workflow.replay.checked`
- `worker.version.deployed`
- `workflow.version_routed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-14-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-14-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-14-state-before.json` ve `ACC-14-state-after.json`.
- `ACC-14-events.json`, `ACC-14-policy-decisions.json` ve `ACC-14-audit-export.json`.
- `ACC-14-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Canary worker kaldırılır veya promote edilir; old worker yalnız compatible histories bitene kadar korunur.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
