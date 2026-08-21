# ACC-28 — Zotero Full Resync

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-28` |
| Kategori | Literature/DR |
| Severity | **High** |
| Accountable Owner | Knowledge Platform Lead |
| Bağımsız witness/verifier | Knowledge Curator / SRE |
| İlgili paketler | `WP-067`, `WP-103`, `WP-114` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Zotero Full Resync** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Zotero bridge checkpoint/state kaybolmuştur; personal/group libraries ve Source Registry mapping/receipts sağlamdır.

**When:** Full resync ve dedup/rebind procedure sıfır checkpoint'ten çalışır.

**Then:** Duplicate veya human-field overwrite üretmeden item versions/bindings reconcile edilir; conflicts curator queue'ya gider.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Pre-resync counts/hashes/item versions al | Execution log + trace/event references |
| 2 | Bridge sync state'i kontrollü sil | Execution log + trace/event references |
| 3 | Full library reads ve resolver mapping çalıştır | Execution log + trace/event references |
| 4 | Existing receipts/bindings/idempotency ile reconcile et | Execution log + trace/event references |
| 5 | Conflicting edits fixture'ını işle | Execution log + trace/event references |
| 6 | Post-resync counts/diffs/conflicts doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] New duplicate count=0
- [ ] Human-authoritative fields unchanged
- [ ] Bindings complete
- [ ] Uncertain conflicts queued
- [ ] Personal library writes=0
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `SyncCheckpoints(new)`
- `ZoteroBindings`
- `SyncReceipts`
- `ConflictCases`
- `ResyncReport`

## Beklenen olaylar

- `zotero.full_resync_started`
- `source.rebound`
- `reconciliation.required`
- `zotero.full_resync_completed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-28-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-28-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-28-state-before.json` ve `ACC-28-state-after.json`.
- `ACC-28-events.json`, `ACC-28-policy-decisions.json` ve `ACC-28-audit-export.json`.
- `ACC-28-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

New checkpoint baseline olarak korunur; fixture conflicts curator disposition ile kapatılır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
