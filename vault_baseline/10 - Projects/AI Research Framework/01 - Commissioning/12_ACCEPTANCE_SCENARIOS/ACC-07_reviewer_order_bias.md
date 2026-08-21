# ACC-07 — Reviewer Order Bias

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-07` |
| Kategori | Model/Eval |
| Severity | **High** |
| Accountable Owner | Eval Office |
| Bağımsız witness/verifier | Independent Human Calibrator |
| İlgili paketler | `WP-043`, `WP-088`, `WP-126` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Reviewer Order Bias** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Aynı iki çözüm/claim paketi A/B ve B/A sırasıyla kör reviewer profile'ına verilebilen calibration fixture'ıdır.

**When:** Order-randomized repeated eval çalışır ve verdict/score/finding farkları ölçülür.

**Then:** Material order etkisi profile calibration'ını fail eder; reviewer critical role'e admitted edilmez veya suspend edilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Frozen identical package pair oluştur | Execution log + trace/event references |
| 2 | Balanced order ve seed'lerle review batch koş | Execution log + trace/event references |
| 3 | Identity/label leakage olmadığını doğrula | Execution log + trace/event references |
| 4 | Verdict/finding/latency farklarını hesapla | Execution log + trace/event references |
| 5 | Threshold ve statistical rule uygula | Execution log + trace/event references |
| 6 | CapabilityProfile disposition üret | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Order effect threshold içindeyse pass, dışındaysa fail
- [ ] Fail profile critical route dışıdır
- [ ] Raw reviews ve run manifests yeniden üretilebilir
- [ ] Human calibration decision kayıtlıdır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `EvalRun`
- `CalibrationReport`
- `ReviewRecords`
- `CapabilityProfileDecision`

## Beklenen olaylar

- `review.calibration.started`
- `review.bias.detected`
- `capability.suspended_or_admitted`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-07-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-07-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-07-state-before.json` ve `ACC-07-state-after.json`.
- `ACC-07-events.json`, `ACC-07-policy-decisions.json` ve `ACC-07-audit-export.json`.
- `ACC-07-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Calibration fixture'ı golden store'da korunur; model/profile sonucu test namespace'ten temizlenmez.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
