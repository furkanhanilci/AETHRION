# ACC-37 — Evaluation Set Contamination

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-37` |
| Kategori | Model/Eval/Security |
| Severity | **Critical** |
| Accountable Owner | Eval Office |
| Bağımsız witness/verifier | Security / Independent Auditor |
| İlgili paketler | `WP-043`, `WP-060`, `WP-112`, `WP-124` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Evaluation Set Contamination** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Golden eval item canary'si prompt log, training/context store veya runtime erişim yolunda görülmüştür.

**When:** Contamination detector/audit taraması alarm üretir.

**Then:** Eval bundle invalidate edilir; ilişkili qualification/profile kararları askıya alınır, temiz set ve re-eval süreci açılır.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Golden canary ve access policy baseline oluştur | Execution log + trace/event references |
| 2 | Unauthorized exposure fixture enjekte et | Execution log + trace/event references |
| 3 | Trace/store/access audit taraması çalıştır | Execution log + trace/event references |
| 4 | Bundle/profile lineage ve affected decisions sorgula | Execution log + trace/event references |
| 5 | Invalidate/revoke/impact workflow'u çalıştır | Execution log + trace/event references |
| 6 | Clean replacement set/re-eval planı üret | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Contaminated bundle INVALIDATED
- [ ] Affected profiles suspended
- [ ] Golden store access isolation restored
- [ ] Historical eval not silently edited
- [ ] Impact/re-eval complete
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `EvalDatasetManifest`
- `ContaminationIncident`
- `CapabilityProfileDecision`
- `ImpactCases`
- `ReplacementPlan`

## Beklenen olaylar

- `eval.contamination_detected`
- `eval.bundle.invalidated`
- `capability.suspended`
- `requalification.required`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-37-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-37-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-37-state-before.json` ve `ACC-37-state-after.json`.
- `ACC-37-events.json`, `ACC-37-policy-decisions.json` ve `ACC-37-audit-export.json`.
- `ACC-37-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Exposed fixture stores sanitize; canary rotate, incident evidence retained.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
