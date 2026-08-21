# ACC-01 — Human Seed Literature

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-01` |
| Kategori | Research/Literature |
| Severity | **Critical** |
| Accountable Owner | Knowledge Lead |
| Bağımsız witness/verifier | Citation Auditor |
| İlgili paketler | `WP-065`, `WP-062`, `WP-069`, `WP-072`, `WP-103` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Human Seed Literature** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Araştırmacının kişisel Zotero kütüphanesinde AIRL ingest için açıkça seçilmiş, Source Registry'de bulunmayan DOI'li ve PDF ekli bir seed vardır.

**When:** Read-only personal seed sync çalışır ve proje LiteratureCampaign'i kaynağı işler.

**Then:** Kaynak tek SourceRecord/Representation'a çözülür, G3 aday/set zincirine girer ve kişisel Zotero'da hiçbir alan değiştirilmez.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Test kullanıcısı ve read-only API key doğrula | Execution log + trace/event references |
| 2 | Seed item/PDF/annotation fixture'ını seçili koleksiyona ekle | Execution log + trace/event references |
| 3 | Incremental sync'i tetikle | Execution log + trace/event references |
| 4 | Resolver, status/license ve project binding'i bekle | Execution log + trace/event references |
| 5 | LiteratureSetManifest freeze denemesi yap | Execution log + trace/event references |
| 6 | Kişisel item version/alanlarını başlangıçla karşılaştır | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Tek canonical SourceRecord vardır
- [ ] Representation hash fixture ile aynıdır
- [ ] Personal item version AIRL yüzünden değişmemiştir
- [ ] Search/seed provenance ve project binding tamdır
- [ ] Manifest source identity, locator ve status taşır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `SourceRecord`
- `SourceRepresentation`
- `ZoteroBinding`
- `SyncReceipt(read)`
- `LiteratureSetManifest`

## Beklenen olaylar

- `source.discovered`
- `source.resolved`
- `source.bound_to_project`
- `literature.set.frozen`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-01-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-01-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-01-state-before.json` ve `ACC-01-state-after.json`.
- `ACC-01-events.json`, `ACC-01-policy-decisions.json` ve `ACC-01-audit-export.json`.
- `ACC-01-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test seed seçimini kaldır; SourceRecord'ı silme, test projesini CLOSED/TEST olarak arşivle.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
