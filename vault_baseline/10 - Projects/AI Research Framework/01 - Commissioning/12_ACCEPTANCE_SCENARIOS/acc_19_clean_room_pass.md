# ACC-19 — Clean-Room Reproduction Pass

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-19` |
| Kategori | Evidence/Reproduction |
| Severity | **High** |
| Accountable Owner | Reproducibility Lead |
| Bağımsız witness/verifier | Assurance Lead / Statistician |
| İlgili paketler | `WP-084`, `WP-085`, `WP-105`, `WP-113` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Clean-Room Reproduction Pass** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Frozen protocol/data/code/environment/model/seed manifest ve önceden tanımlı stochastic tolerance vardır.

**When:** Bağımsız reproducer temiz ortamda manifestten run'ı çalıştırır.

**Then:** Sonuç tolerance içindedir; ReproductionReport/Certificate ve independence attestation oluşur, G7 geçebilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Producer run ve frozen package oluştur | Execution log + trace/event references |
| 2 | Independent reproducer/credential/environment ata | Execution log + trace/event references |
| 3 | Manifest hashes verify ve environment build yap | Execution log + trace/event references |
| 4 | Run/metrics/tolerance calculation çalıştır | Execution log + trace/event references |
| 5 | Producer vs repro lineage/outputs karşılaştır | Execution log + trace/event references |
| 6 | G7 Gate Service evaluation yap | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Bütün input digests eşleşir
- [ ] IndependenceProfile compliant
- [ ] Metric tolerance içinde
- [ ] Reproduction certificate signed
- [ ] G7 hard checks PASS
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `RunManifest`
- `EnvironmentManifest`
- `IndependenceProfile`
- `ReproductionReport`
- `GateRecord`

## Beklenen olaylar

- `reproduction.started`
- `reproduction.passed`
- `claim.reproduction_updated`
- `gate.passed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-19-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-19-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-19-state-before.json` ve `ACC-19-state-after.json`.
- `ACC-19-events.json`, `ACC-19-policy-decisions.json` ve `ACC-19-audit-export.json`.
- `ACC-19-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Clean room destroy; artifact/report immutable store'da test retention ile kalır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
