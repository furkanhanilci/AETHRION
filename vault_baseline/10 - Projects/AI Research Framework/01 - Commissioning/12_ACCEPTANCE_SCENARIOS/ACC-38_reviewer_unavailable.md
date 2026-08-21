# ACC-38 — Critical Reviewer Unavailable

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-38` |
| Kategori | Assurance/Operations |
| Severity | **High** |
| Accountable Owner | Assurance Lead |
| Bağımsız witness/verifier | Project Decision Owner |
| İlgili paketler | `WP-045`, `WP-088`, `WP-105`, `WP-113`, `WP-126` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Critical Reviewer Unavailable** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** R3 artifact için gerekli bağımsız/cross-family/human reviewer pool'da eligible ve available aktör yoktur.

**When:** Assignment service reviewer ister ve SLA dolar.

**Then:** Producer/self-review veya ineligible fallback kullanılmaz; gate BLOCKED, human scheduling/escalation ve capacity signal oluşur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | R3 review request/frozen package oluştur | Execution log + trace/event references |
| 2 | Bütün eligible reviewer availability'yi unavailable yap | Execution log + trace/event references |
| 3 | Assignment/route attempts çalıştır | Execution log + trace/event references |
| 4 | SLA timeout/escalation gözle | Execution log + trace/event references |
| 5 | Producer/ineligible model atama bypass dene | Execution log + trace/event references |
| 6 | Reviewer available yapıp yeni assignment tamamla | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] No self/ineligible assignment
- [ ] Gate BLOCKED not PASS
- [ ] SLA escalation/capacity metric
- [ ] Frozen package unchanged
- [ ] Later eligible review valid
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `ReviewRequest`
- `AssignmentDecisions`
- `Workflow/GateState`
- `EscalationRecord`
- `CapacitySignal`

## Beklenen olaylar

- `review.no_eligible_reviewer`
- `workflow.blocked`
- `assurance.capacity_alert`
- `review.assignment_created`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-38-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-38-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-38-state-before.json` ve `ACC-38-state-after.json`.
- `ACC-38-events.json`, `ACC-38-policy-decisions.json` ve `ACC-38-audit-export.json`.
- `ACC-38-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Availability fixture baseline'a döner; blocked test request valid review veya controlled cancel ile kapanır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
