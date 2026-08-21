# ACC-06 — Planner Self-Approval Attempt

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-06` |
| Kategori | Governance/Assurance |
| Severity | **Critical** |
| Accountable Owner | Assurance Lead |
| Bağımsız witness/verifier | Internal Audit |
| İlgili paketler | `WP-007`, `WP-088`, `WP-102`, `WP-105` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Planner Self-Approval Attempt** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Bir planı üreten actor/model profile aynı artifact için reviewer veya approver assignment adayı olarak sunulur.

**When:** Assignment service IndependenceProfile eligibility kontrolü yapar.

**Then:** Atama policy tarafından reddedilir; gate BLOCKED veya uygun bağımsız reviewer bekler ve ihlal denemesi audit edilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Producer identity/model/context/credential alanlarını kaydet | Execution log + trace/event references |
| 2 | Aynı actor'ı reviewer olarak ata | Execution log + trace/event references |
| 3 | Aynı insan farklı model ama kirli context varyantını dene | Execution log + trace/event references |
| 4 | R1 ve R3 policy sonuçlarını karşılaştır | Execution log + trace/event references |
| 5 | Uygun bağımsız reviewer ata ve akışı sürdür | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Self assignment deny
- [ ] Context contamination non-compliant
- [ ] R3 gerekli human/model separation
- [ ] Denied attempt gate'i PASS yapmaz
- [ ] Audit rule/bundle/input taşır
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `IndependenceProfile`
- `AssignmentDecision`
- `PolicyDecision`
- `GateRecord`
- `AuditRecord`

## Beklenen olaylar

- `review.assignment.denied`
- `independence.violated`
- `workflow.blocked`
- `review.assignment.created`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-06-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-06-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-06-state-before.json` ve `ACC-06-state-after.json`.
- `ACC-06-events.json`, `ACC-06-policy-decisions.json` ve `ACC-06-audit-export.json`.
- `ACC-06-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test assignments cancel edilir; denial/audit kayıtları retained kalır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
