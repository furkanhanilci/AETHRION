# ACC-02 — Agent-Used Source Write-Back

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-02` |
| Kategori | Research/Literature |
| Severity | **Critical** |
| Accountable Owner | Evidence Lead |
| Bağımsız witness/verifier | Knowledge Curator |
| İlgili paketler | `WP-066`, `WP-072`, `WP-103` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Agent-Used Source Write-Back** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Agent keşfinde bulunan yeni kaynak bir material claim tarafından kullanılmış, Source Registry kaydı tamamlanmış ve grup kütüphanesinde henüz yoktur.

**When:** Used-source eligibility policy geçer ve Zotero write-back connector'ı çağrılır.

**Then:** Kaynak yalnız doğru AIRL grup kütüphanesindeki `40_Used` ve ilgili proje koleksiyonuna idempotent yazılır; registry binding ve receipt oluşur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Kaynağı agent candidate olarak ingest et | Execution log + trace/event references |
| 2 | EvidenceSpan ve material Claim bağlantısı oluştur | Execution log + trace/event references |
| 3 | Eligibility policy kararını doğrula | Execution log + trace/event references |
| 4 | Write-back çağrısını iki kez aynı idempotency key ile gönder | Execution log + trace/event references |
| 5 | Zotero item/collections/version ve registry binding'i oku | Execution log + trace/event references |
| 6 | Manifest/export içinde kaynağı doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Zotero'da tek item vardır
- [ ] Item doğru managed collections içindedir
- [ ] İkinci çağrı yeni item/yan etki üretmez
- [ ] SyncReceipt previous/new version ve policy ID taşır
- [ ] Kişisel library'de write yoktur
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `SourceRecord`
- `ClaimRecord`
- `EvidenceSpan`
- `ZoteroBinding`
- `SyncReceipt(write)`

## Beklenen olaylar

- `source.used`
- `zotero.write.requested`
- `zotero.write.completed`
- `literature.source.promoted`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-02-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-02-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-02-state-before.json` ve `ACC-02-state-after.json`.
- `ACC-02-events.json`, `ACC-02-policy-decisions.json` ve `ACC-02-audit-export.json`.
- `ACC-02-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test grup item'ını managed cleanup policy ile trash'e al; canonical source/claim test kayıtlarını TEST disposition ile koru.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
