# ACC-17 — Unsigned veya Mutable Image

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-17` |
| Kategori | Security/Supply Chain |
| Severity | **Critical** |
| Accountable Owner | Supply Chain Security Lead |
| Bağımsız witness/verifier | Independent Security Reviewer |
| İlgili paketler | `WP-027`, `WP-059`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Unsigned veya Mutable Image** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Workload unsigned image veya mutable tag ile production/staging secure namespace'e alınmak istenir.

**When:** Kubernetes admission controller manifesti değerlendirir.

**Then:** Pod oluşturulmaz; signature/provenance/digest policy deny ve audit/alert üretir. İmzalı digest karşı örneği geçer.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Unsigned image fixture push et | Execution log + trace/event references |
| 2 | Mutable tag manifest submit et | Execution log + trace/event references |
| 3 | Wrong builder provenance imzalı fixture dene | Execution log + trace/event references |
| 4 | Admission deny reason/audit al | Execution log + trace/event references |
| 5 | Approved signed digest submit et | Execution log + trace/event references |
| 6 | Running revoked digest impact behavior izle | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Unsigned/mutable/wrong provenance pod count=0
- [ ] Deny rule/digest görünür
- [ ] Approved signed digest çalışır
- [ ] Revocation alert/impact oluşturur
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `AdmissionDecision`
- `ImageSignature/SBOM/Provenance`
- `SecurityEvent`
- `WorkloadRecord`

## Beklenen olaylar

- `supply_chain.denied`
- `unsigned_image.detected`
- `artifact.revoked`
- `workload.admitted`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-17-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-17-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-17-state-before.json` ve `ACC-17-state-after.json`.
- `ACC-17-events.json`, `ACC-17-policy-decisions.json` ve `ACC-17-audit-export.json`.
- `ACC-17-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test images quarantine/delete retention policy ile; approved fixture workload destroy edilir.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
