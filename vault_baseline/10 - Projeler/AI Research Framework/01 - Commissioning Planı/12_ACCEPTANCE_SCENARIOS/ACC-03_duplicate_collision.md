# ACC-03 — Duplicate ve Metadata Collision

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-03` |
| Kategori | Research/Literature |
| Severity | **High** |
| Accountable Owner | Source Resolver Lead |
| Bağımsız witness/verifier | Knowledge Curator |
| İlgili paketler | `WP-062`, `WP-067`, `WP-094`, `WP-103` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Duplicate ve Metadata Collision** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Aynı DOI için iki Zotero kütüphanesinde farklı title/year ve bir fuzzy title eşleşmesi vardır.

**When:** Full/incremental sync ve resolver aynı anda kayıtları işler.

**Then:** Güvenli exact eşleşme tek SourceRecord'a bağlanır; çelişen alanlar sessiz overwrite edilmez ve curator ConflictCase açılır.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Conflicting fixtures ve başlangıç item versions kaydet | Execution log + trace/event references |
| 2 | İki sync'i eşzamanlı tetikle | Execution log + trace/event references |
| 3 | Resolver match feature/decision'larını al | Execution log + trace/event references |
| 4 | ConflictCase'i Workbench'te incele | Execution log + trace/event references |
| 5 | Curator doğru field authority ile disposition versin | Execution log + trace/event references |
| 6 | Tekrar full resync çalıştır | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Canonical duplicate sayısı bir veya açıklanmış split'tir
- [ ] Human-authoritative field korunur
- [ ] ConflictCase rationale ve actor taşır
- [ ] Full resync yeni duplicate üretmez
- [ ] Eski external bindings kaybolmaz
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `ResolverRecord`
- `ConflictCase`
- `Merge/SplitRecord`
- `ZoteroBinding`
- `SyncReceipt`

## Beklenen olaylar

- `source.collision_detected`
- `reconciliation.required`
- `source.merge_dispositioned`
- `zotero.sync.completed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-03-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-03-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-03-state-before.json` ve `ACC-03-state-after.json`.
- `ACC-03-events.json`, `ACC-03-policy-decisions.json` ve `ACC-03-audit-export.json`.
- `ACC-03-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Fixture item'larını test kütüphanesinden kaldır; resolver decisions TEST retention ile saklanır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
