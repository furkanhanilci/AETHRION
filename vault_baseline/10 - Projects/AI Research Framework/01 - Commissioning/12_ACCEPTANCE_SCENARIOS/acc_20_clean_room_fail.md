# ACC-20 — Clean-Room Reproduction Fail

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-20` |
| Kategori | Evidence/Reproduction |
| Severity | **Critical** |
| Accountable Owner | Reproducibility Lead |
| Bağımsız witness/verifier | Assurance Lead / Methodologist |
| İlgili paketler | `WP-084`, `WP-085`, `WP-105`, `WP-113` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Clean-Room Reproduction Fail** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Frozen claim/run paketi ve predeclared tolerance vardır; fixture environment/data mismatch veya gerçek sonuç sapması üretir.

**When:** Bağımsız reproduction çalışır ve tolerans dışına çıkar.

**Then:** G7 FAIL/REVISE olur, claim CHALLENGED; environment/data/code/stochastic/method root-cause sınıflaması ve G4/G5 controlled return açılır.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Manifest ve deliberate mismatch fixture'ını hazırla | Execution log + trace/event references |
| 2 | Clean-room run çalıştır | Execution log + trace/event references |
| 3 | Metric/tolerance fail kaydet | Execution log + trace/event references |
| 4 | Hash/environment/data diff ve root cause triage yap | Execution log + trace/event references |
| 5 | Claim/gate/workflow transition'ını izle | Execution log + trace/event references |
| 6 | Correction sonrası yeni manifest/repro planını oluştur | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] G7 PASS değildir
- [ ] Claim CHALLENGED
- [ ] Old producer/repro artifacts retained
- [ ] RootCauseCase owner/SLA taşır
- [ ] G4/G5 return new version üretir
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `ReproductionReport(fail)`
- `ClaimAssessment`
- `GateRecord`
- `RootCauseCase`
- `WorkflowHistory`

## Beklenen olaylar

- `reproduction.failed`
- `claim.challenged`
- `gate.revise`
- `workflow.returned_to_g4_or_g5`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-20-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-20-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-20-state-before.json` ve `ACC-20-state-after.json`.
- `ACC-20-events.json`, `ACC-20-policy-decisions.json` ve `ACC-20-audit-export.json`.
- `ACC-20-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Mismatch fixture kapatılır; failed report değişmeden saklanır, correction yeni run olarak yapılır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
