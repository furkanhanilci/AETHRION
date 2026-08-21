# ACC-40 — Complete Project Audit Export

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-40` |
| Kategori | Audit/Operations |
| Severity | **Critical** |
| Accountable Owner | Internal Audit Lead |
| Bağımsız witness/verifier | Independent Auditor |
| İlgili paketler | `WP-099`, `WP-106`, `WP-109`, `WP-112`, `WP-114` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Complete Project Audit Export** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** G0–G10'u geçmiş bir proje policy, identity, model, tool, source, claim, run, artifact, cost, review, repro ve decision kayıtlarına sahiptir.

**When:** Auditor project/time scope ile export ve offline verifier çalıştırır.

**Then:** İmzalı export tam korelasyon ve hash zinciriyle doğrulanır; eksik/tamper edilmiş fixture fail ve incident üretir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Completed synthetic project ve expected object/event counts al | Execution log + trace/event references |
| 2 | Least-privilege audit export request yap | Execution log + trace/event references |
| 3 | Export manifest/objects/hash chain/signature üret | Execution log + trace/event references |
| 4 | Offline verifier ile chain/links/counts doğrula | Execution log + trace/event references |
| 5 | Bir kopyada record tamper/drop et ve tekrar verify et | Execution log + trace/event references |
| 6 | Access/audit-of-audit ve retention kontrol et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Complete export verifies
- [ ] REQ→WP→test/evidence→decision chain query
- [ ] Tamper/missing record detected
- [ ] Auditor read-only
- [ ] Sensitive fields policy-compliant
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `AuditExportManifest`
- `WORMRecords`
- `VerificationReport`
- `AuditAccessRecord`
- `SecurityIncident(tamper fixture)`

## Beklenen olaylar

- `audit.export_requested`
- `audit.export_created`
- `audit.export_verified`
- `audit.integrity_failed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-40-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-40-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-40-state-before.json` ve `ACC-40-state-after.json`.
- `ACC-40-events.json`, `ACC-40-policy-decisions.json` ve `ACC-40-audit-export.json`.
- `ACC-40-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Export test copy secure destruction; canonical signed export/audit access retained.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
