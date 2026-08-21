# ACC-29 — Provider Invoice Variance

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-29` |
| Kategori | FinOps |
| Severity | **Medium** |
| Accountable Owner | FinOps Lead |
| Bağımsız witness/verifier | Internal Audit |
| İlgili paketler | `WP-100`, `WP-111`, `WP-127` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Provider Invoice Variance** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Provider invoice toplamı Cost Ledger tahakkukundan policy threshold üzerinde farklıdır.

**When:** Aylık reconciliation job invoice ve usage/cost events'i karşılaştırır.

**Then:** VarianceCase; provider/project/model/time bucket kırılımı, owner, SLA ve adjustment/dispute path ile açılır; ledger geçmişi silinmez.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Synthetic usage/cost events ve farklı invoice seed et | Execution log + trace/event references |
| 2 | Currency/rate/time-zone normalization çalıştır | Execution log + trace/event references |
| 3 | Reconciliation/threshold uygula | Execution log + trace/event references |
| 4 | Missing/duplicate usage buckets analiz et | Execution log + trace/event references |
| 5 | VarianceCase owner/disposition üret | Execution log + trace/event references |
| 6 | Adjustment entry ve close test et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Variance detected at threshold
- [ ] No destructive ledger rewrite
- [ ] Adjustment references original entries
- [ ] Owner/SLA/audit complete
- [ ] Dashboard variance visible
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `InvoiceRecord`
- `CostLedgerEntries`
- `VarianceCase`
- `AdjustmentEntry`
- `DecisionRecord`

## Beklenen olaylar

- `invoice.ingested`
- `cost.variance_detected`
- `reconciliation.case_opened`
- `cost.adjusted`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-29-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-29-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-29-state-before.json` ve `ACC-29-state-after.json`.
- `ACC-29-events.json`, `ACC-29-policy-decisions.json` ve `ACC-29-audit-export.json`.
- `ACC-29-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Synthetic invoice/cost center TEST_CLOSED; financial audit evidence retained.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
