# ACC-09 — Budget Hard Stop

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-09` |
| Kategori | FinOps/Reliability |
| Severity | **Critical** |
| Accountable Owner | FinOps Lead |
| Bağımsız witness/verifier | Project Decision Owner / SRE |
| İlgili paketler | `WP-053`, `WP-083`, `WP-100`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Budget Hard Stop** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** C3 fan-out/experiment batch bütçenin %80'ine yaklaşmış ve sonraki iş %100 hard limit'i aşacaktır.

**When:** Yeni pahalı model/compute reservation istenir ve eşzamanlı retry denenir.

**Then:** %80 warning oluşur; %100'de yeni pahalı iş deny edilir, workflow state/checkpoints korunarak pause olur ve duplicate cost/reservation oluşmaz.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | BudgetEnvelope ve maliyet fixture'ını seed et | Execution log + trace/event references |
| 2 | %80'e geçecek çağrıyı çalıştır | Execution log + trace/event references |
| 3 | Hard limit'i aşan parallel requests gönder | Execution log + trace/event references |
| 4 | Temporal/Kueue/Gateway durumlarını gözle | Execution log + trace/event references |
| 5 | Owner budget decision queue'yu kontrol et | Execution log + trace/event references |
| 6 | Reservation release/reconcile yap | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] 80% event bir kez
- [ ] Hard-limit sonrası yeni expensive call/job sayısı 0
- [ ] Workflow PAUSED/BUDGET_BLOCKED
- [ ] Existing artifact/checkpoint sağlam
- [ ] Cost event idempotent
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `BudgetEnvelope`
- `ReservationRecords`
- `Route/Queue PolicyDecisions`
- `WorkflowState`
- `CostLedgerEntries`

## Beklenen olaylar

- `budget.threshold_80`
- `budget.exhausted`
- `workflow.paused`
- `decision.required`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-09-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-09-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-09-state-before.json` ve `ACC-09-state-after.json`.
- `ACC-09-events.json`, `ACC-09-policy-decisions.json` ve `ACC-09-audit-export.json`.
- `ACC-09-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test reservations release edilir; BudgetEnvelope TEST_CLOSED ve ledger entries test cost center'a alınır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
