# ACC-35 — Tool Partial Failure

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-35` |
| Kategori | Tool/Reliability |
| Severity | **Critical** |
| Accountable Owner | Tool Platform Lead |
| Bağımsız witness/verifier | SRE / Connector Owner |
| İlgili paketler | `WP-049`, `WP-050`, `WP-111` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Tool Partial Failure** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** External reversible write başarılı olur fakat response Broker'a ulaşmadan timeout/connection loss oluşur.

**When:** Broker retry isteği alır.

**Then:** Kör retry ikinci yan etki üretmez; read/reconcile ile remote effect bulunur, tek ToolReceipt finalized veya RECONCILIATION_REQUIRED olur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | External fixture endpoint/idempotency key hazırla | Execution log + trace/event references |
| 2 | Write success sonrası response drop enjekte et | Execution log + trace/event references |
| 3 | Broker timeout state'ini al | Execution log + trace/event references |
| 4 | Aynı invocation retry et | Execution log + trace/event references |
| 5 | Remote read/reconciliation çalıştır | Execution log + trace/event references |
| 6 | Effect count/receipt/outbox/audit doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] External effect count=1
- [ ] Uncertain state explicit
- [ ] Reconciliation finds effect
- [ ] One finalized receipt/event
- [ ] No silent success before evidence
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `ToolInvocation`
- `IdempotencyRecord`
- `ToolReceipt`
- `ReconciliationCase`
- `OutboxRecord`

## Beklenen olaylar

- `tool.invocation_started`
- `tool.response_unknown`
- `reconciliation.started`
- `tool.effect_confirmed`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-35-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-35-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-35-state-before.json` ve `ACC-35-state-after.json`.
- `ACC-35-events.json`, `ACC-35-policy-decisions.json` ve `ACC-35-audit-export.json`.
- `ACC-35-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

External test effect compensation/delete; reconciliation case TEST_CLOSED.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
