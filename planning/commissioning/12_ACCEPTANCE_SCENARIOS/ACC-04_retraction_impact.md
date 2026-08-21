# ACC-04 — Retraction Impact

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-04` |
| Kategori | Research/Monitoring |
| Severity | **Critical** |
| Accountable Owner | Knowledge Monitoring Lead |
| Bağımsız witness/verifier | Project Decision Owner / Citation Auditor |
| İlgili paketler | `WP-063`, `WP-037`, `WP-108`, `WP-106` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Retraction Impact** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** CORE trust seviyesindeki bir source bir VERIFIED claim, karar ve yayın paketini desteklemektedir.

**When:** Status monitor doğrulanmış retraction/correction olayı alır ve ImpactScan çalışır.

**Then:** Eski manifest/yayın değişmez; claim CHALLENGED/impact-pending olur, doğru projeler ve owner için ImpactCase ve supersession/review işi açılır.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | CORE source→claim→publication fixture zinciri hazırla | Execution log + trace/event references |
| 2 | Retraction feed event'ini enjekte et | Execution log + trace/event references |
| 3 | Schedule/ImpactScan çalıştır | Execution log + trace/event references |
| 4 | Affected set'i expected fixture ile karşılaştır | Execution log + trace/event references |
| 5 | Decision Queue ve publication banner'ını kontrol et | Execution log + trace/event references |
| 6 | Duplicate retraction event'ini tekrar gönder | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Affected critical claim recall %100
- [ ] Tek ImpactCase/idempotent trigger
- [ ] Old LiteratureSetManifest hash değişmez
- [ ] Claim status rule ile değişir
- [ ] Named owner/SLA ve public supersession uyarısı vardır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `SourceStatusRecord`
- `ImpactCase`
- `ClaimAssessment`
- `MonitoringRun`
- `SupersessionPlan`

## Beklenen olaylar

- `source.retracted`
- `impact.scan.started`
- `claim.challenged`
- `decision.required`
- `publication.impact_detected`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-04-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-04-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-04-state-before.json` ve `ACC-04-state-after.json`.
- `ACC-04-events.json`, `ACC-04-policy-decisions.json` ve `ACC-04-audit-export.json`.
- `ACC-04-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Synthetic retraction statusunu superseding test statusuyla kapat; ImpactCase'i TEST_RESOLVED yap.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
