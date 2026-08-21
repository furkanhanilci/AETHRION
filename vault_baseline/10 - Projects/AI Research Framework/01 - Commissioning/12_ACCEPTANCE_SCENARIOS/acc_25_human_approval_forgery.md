# ACC-25 — Human Approval Forgery

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-25` |
| Kategori | Security/Governance |
| Severity | **Critical** |
| Accountable Owner | Governance Lead |
| Bağımsız witness/verifier | Security / Internal Audit |
| İlgili paketler | `WP-038`, `WP-055`, `WP-093`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Human Approval Forgery** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** G8/G9 decision request vardır; saldırgan missing/invalid OIDC-MFA context veya payload replay ile onay göndermeye çalışır.

**When:** Temporal Human Update API forged/expired/duplicate request alır.

**Then:** Karar reddedilir; gate state değişmez, security event/audit oluşur. Geçerli owner MFA ve idempotent request karşı örneği geçer.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Decision request/evidence snapshot hazırla | Execution log + trace/event references |
| 2 | Missing token/invalid signature/wrong subject/expired MFA dene | Execution log + trace/event references |
| 3 | Valid request'i capture/replay et | Execution log + trace/event references |
| 4 | Gate/history/DecisionRecord kontrol et | Execution log + trace/event references |
| 5 | Doğru owner ile re-auth valid decision gönder | Execution log + trace/event references |
| 6 | Security alert/incident threshold doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Forged decisions count=0
- [ ] Gate unchanged
- [ ] Replay one decision
- [ ] Valid actor/role/evidence snapshot required
- [ ] Audit contains attempts
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `DecisionRequest`
- `PolicyDecision`
- `SecurityEvent`
- `DecisionRecord(valid)`
- `TemporalHistory`

## Beklenen olaylar

- `approval.forgery_detected`
- `decision.denied`
- `security.event`
- `decision.recorded`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-25-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-25-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-25-state-before.json` ve `ACC-25-state-after.json`.
- `ACC-25-events.json`, `ACC-25-policy-decisions.json` ve `ACC-25-audit-export.json`.
- `ACC-25-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test tokens revoke; synthetic decision/project TEST_CLOSED olarak arşivlenir.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
