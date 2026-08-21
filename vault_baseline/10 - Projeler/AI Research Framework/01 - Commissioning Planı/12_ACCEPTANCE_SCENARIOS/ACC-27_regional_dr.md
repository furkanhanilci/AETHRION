# ACC-27 — Regional/Management Plane DR

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-27` |
| Kategori | Operations/DR |
| Severity | **Critical** |
| Accountable Owner | SRE Lead |
| Bağımsız witness/verifier | Independent DR Witness |
| İlgili paketler | `WP-114`, `WP-129` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Regional/Management Plane DR** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Production-equivalent management region/control services erişilemez; güncel backup/replica ve açık workflow'lar vardır.

**When:** DR declaration, restore/failover ve traffic/DNS/control-plane switch runbook'u uygulanır.

**Then:** Temporal workflow state RPO=0, canonical registries/artifacts/audit bütün ve RTO hedefi içinde hizmet geri gelir; derived views rebuild edilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Pre-drill manifests/open workflow/integrity baselines al | Execution log + trace/event references |
| 2 | Region/control dependencies isolate et | Execution log + trace/event references |
| 3 | Incident/DR decision ve communication başlat | Execution log + trace/event references |
| 4 | Temporal/Postgres/object/NATS/identity restore/failover yap | Execution log + trace/event references |
| 5 | Projections/caches rebuild et | Execution log + trace/event references |
| 6 | Integrity/ACC smoke/RPO/RTO ve failback doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Workflow RPO=0
- [ ] Restore RTO target
- [ ] Registry/artifact/audit hashes match
- [ ] No duplicate effect
- [ ] Derived views rebuild
- [ ] Decision/audit complete
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `DRDecision`
- `RestoreManifests`
- `IntegrityQueryResults`
- `RPO/RTOReport`
- `IncidentRecord`

## Beklenen olaylar

- `dr.declared`
- `service.failed_over`
- `restore.completed`
- `integrity.verified`
- `dr.closed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-27-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-27-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-27-state-before.json` ve `ACC-27-state-after.json`.
- `ACC-27-events.json`, `ACC-27-policy-decisions.json` ve `ACC-27-audit-export.json`.
- `ACC-27-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

DR environment/failover state runbook'a göre failback veya retained; fault isolation kaldırılır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
