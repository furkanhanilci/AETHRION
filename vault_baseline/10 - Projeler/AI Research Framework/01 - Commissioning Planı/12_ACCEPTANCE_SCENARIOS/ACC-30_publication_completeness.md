# ACC-30 — Publication Completeness

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-30` |
| Kategori | Publication/Evidence |
| Severity | **Critical** |
| Accountable Owner | Provenance Curator |
| Bağımsız witness/verifier | Citation Auditor / Safety |
| İlgili paketler | `WP-080`, `WP-090`, `WP-106`, `WP-113` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Publication Completeness** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Publication draftında material/critical bir claim'in locator veya complete lineage bağlantısı eksiktir.

**When:** G9 publication builder, citation audit ve Verification Engine çalışır.

**Then:** Publication package/signature/release oluşmaz; G9 FAIL/REVISE ve düzeltme kuyruğu açılır. Eksik bağ tamamlanınca yeni package version geçebilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Complete baseline draft/package fixture hazırla | Execution log + trace/event references |
| 2 | Critical claim locator/ref'i çıkar | Execution log + trace/event references |
| 3 | Builder/audit/verification/Gate Service çalıştır | Execution log + trace/event references |
| 4 | Release endpoint ve object store'u kontrol et | Execution log + trace/event references |
| 5 | Eksik evidence'i yeni version ile ekle | Execution log + trace/event references |
| 6 | Yeni package build/pass ve old draft history doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Incomplete package release count=0
- [ ] G9 fail rule visible
- [ ] Critical lineage coverage target 100%
- [ ] Corrected package new version/hash
- [ ] Old failed draft retained
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `CitationAudit`
- `VerificationRecord`
- `GateRecord`
- `PublicationPackage(draft/final)`
- `CorrectionRecord`

## Beklenen olaylar

- `publication.validation_failed`
- `gate.revise`
- `claim.evidence_corrected`
- `publication.package_created`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-30-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-30-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-30-state-before.json` ve `ACC-30-state-after.json`.
- `ACC-30-events.json`, `ACC-30-policy-decisions.json` ve `ACC-30-audit-export.json`.
- `ACC-30-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Final test package public endpoint'ten kaldırılır; archive TEST namespace'te kalır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
