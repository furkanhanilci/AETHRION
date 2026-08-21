# ACC-23 — Artifact Overwrite Attempt

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-23` |
| Kategori | Data/Integrity |
| Severity | **Critical** |
| Accountable Owner | Data Platform Lead |
| Bağımsız witness/verifier | Archivist / Security |
| İlgili paketler | `WP-026`, `WP-087`, `WP-104`, `WP-113` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Artifact Overwrite Attempt** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Canonical content-addressed URI'de hash A bytes vardır; istemci aynı URI/key için hash B bytes yazmak ister.

**When:** Object write/finalize veya manifest update çağrısı yapılır.

**Then:** Overwrite reddedilir; yeni bytes yalnız yeni content address/version olarak yazılabilir ve eski references değişmez.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Artifact A upload/finalize et | Execution log + trace/event references |
| 2 | Aynı key'e B upload/overwrite dene | Execution log + trace/event references |
| 3 | Hash mismatch response/audit al | Execution log + trace/event references |
| 4 | B'yi yeni content address ile yaz | Execution log + trace/event references |
| 5 | Old run/claim/publication ref'lerini sorgula | Execution log + trace/event references |
| 6 | Tamper/integrity scan çalıştır | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] A bytes/hash değişmez
- [ ] Overwrite operation deny
- [ ] B unique address/version
- [ ] Old references A'ya devam eder
- [ ] Audit tamper attempt taşır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `ArtifactRecords A/B`
- `ObjectStoreAudit`
- `PolicyDecision`
- `IntegrityScanRecord`

## Beklenen olaylar

- `artifact.created`
- `artifact.overwrite_denied`
- `artifact.version_created`
- `integrity.checked`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-23-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-23-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-23-state-before.json` ve `ACC-23-state-after.json`.
- `ACC-23-events.json`, `ACC-23-policy-decisions.json` ve `ACC-23-audit-export.json`.
- `ACC-23-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

B test version retention policy ile temizlenebilir; A baseline test artifact olarak kalır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
