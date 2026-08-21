# ACC-26 — Approval, Delegation ve Exception Expiry

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-26` |
| Kategori | Governance |
| Severity | **Critical** |
| Accountable Owner | Safety & Governance Owner |
| Bağımsız witness/verifier | Internal Audit |
| İlgili paketler | `WP-004`, `WP-009`, `WP-038`, `WP-093`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Approval, Delegation ve Exception Expiry** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Süreli delegation/control exception veya approval açık/çalışan task tarafından kullanılmaktadır.

**When:** Expiry zamanı gelir ve scheduled policy re-evaluation çalışır.

**Then:** Yetki auto-revoke olur; yeni işlem deny, running task policy'ye göre pause/contain olur; otomatik uzatma/onay yoktur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Kısa expiry'li record ve scoped task oluştur | Execution log + trace/event references |
| 2 | Expiry öncesi izinli operation çalıştır | Execution log + trace/event references |
| 3 | Clock/schedule expiry tetikle | Execution log + trace/event references |
| 4 | Yeni/running operation davranışını izle | Execution log + trace/event references |
| 5 | Escalation/owner queue ve audit kontrol et | Execution log + trace/event references |
| 6 | Expired token replay dene | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Record EXPIRED/REVOKED
- [ ] New action deny
- [ ] Running task re-evaluated
- [ ] No auto-extension
- [ ] Owner/escalation/audit complete
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `Delegation/ExceptionRecord`
- `PolicyDecisions`
- `WorkflowState`
- `Revocation/AuditRecord`

## Beklenen olaylar

- `authorization.expired`
- `credential_or_exception.revoked`
- `task.re_evaluated`
- `workflow.paused`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-26-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-26-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-26-state-before.json` ve `ACC-26-state-after.json`.
- `ACC-26-events.json`, `ACC-26-policy-decisions.json` ve `ACC-26-audit-export.json`.
- `ACC-26-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test scope temizlenir; record geçmişi retained, task controlled cancel/close.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
