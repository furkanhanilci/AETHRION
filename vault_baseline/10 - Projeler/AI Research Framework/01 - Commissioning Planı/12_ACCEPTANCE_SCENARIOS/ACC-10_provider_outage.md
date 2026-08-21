# ACC-10 — Primary Model Provider Outage

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-10` |
| Kategori | Reliability/Model |
| Severity | **High** |
| Accountable Owner | Model Platform Lead |
| Bağımsız witness/verifier | SRE / Eval Office |
| İlgili paketler | `WP-041`, `WP-045`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Primary Model Provider Outage** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Primary profile outage vermekte, aynı role/data/tool/risk için admitted fallback bulunmaktadır.

**When:** Gateway circuit breaker açılır ve router yeniden seçim yapar.

**Then:** Yalnız admitted fallback seçilir; route/family/independence yeniden hesaplanır, SLO ve cost kaydı oluşur, task duplicate olmaz.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Primary provider 5xx/timeout fault enjekte et | Execution log + trace/event references |
| 2 | Circuit breaker threshold'a ulaş | Execution log + trace/event references |
| 3 | Aynı TaskContract için fallback route al | Execution log + trace/event references |
| 4 | Reviewer independence ihtiyacı varsa yeniden hesapla | Execution log + trace/event references |
| 5 | AgentResult ve cost/trace correlation doğrula | Execution log + trace/event references |
| 6 | Primary recovery half-open dene | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Fallback eligibility tamdır
- [ ] Tek task sonucu vardır
- [ ] Unsafe provider route yoktur
- [ ] RouteDecision gerekçe/profile refs taşır
- [ ] Outage alert/SLO ölçülür
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `RouteDecision`
- `CapabilityProfileRefs`
- `ModelCallRecords`
- `TaskResult`
- `Incident/SLORecord`

## Beklenen olaylar

- `model.provider.degraded`
- `route.fallback_selected`
- `task.completed`
- `provider.recovered`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-10-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-10-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-10-state-before.json` ve `ACC-10-state-after.json`.
- `ACC-10-events.json`, `ACC-10-policy-decisions.json` ve `ACC-10-audit-export.json`.
- `ACC-10-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Fault kaldırılır; circuit breaker kontrollü reset, synthetic health doğrulaması yapılır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
