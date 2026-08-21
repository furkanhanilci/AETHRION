# ACC-16 — Egress Exfiltration Attempt

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-16` |
| Kategori | Security/Network |
| Severity | **Critical** |
| Accountable Owner | Network Security Lead |
| Bağımsız witness/verifier | Red Team / Privacy Owner |
| İlgili paketler | `WP-057`, `WP-060`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Egress Exfiltration Attempt** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Sandbox içindeki payload unknown domain/raw IP/DNS tunnel üzerinden canary secret göndermeyi dener.

**When:** Execution egress proxy ve DLP üzerinden çalışır.

**Then:** Trafik deny edilir, canary dışarı çıkmaz, credential lease revoke ve security incident/audit oluşur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Canary secret/attack destination kur | Execution log + trace/event references |
| 2 | Sandbox workload'a scoped lease ver | Execution log + trace/event references |
| 3 | HTTPS/raw IP/DNS/proxy bypass attempts çalıştır | Execution log + trace/event references |
| 4 | Egress/DLP/Vault/network logs gözle | Execution log + trace/event references |
| 5 | Lease revoke ve incident workflow doğrula | Execution log + trace/event references |
| 6 | Canary destination'a byte ulaşmadığını teyit et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Exfiltrated bytes=0
- [ ] Unknown domain/raw IP/DNS deny
- [ ] DLP canary match
- [ ] Lease revoked
- [ ] Security event correlation complete
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `EgressDecision`
- `DLPRecord`
- `VaultLeaseRecord`
- `SecurityIncident`
- `NetworkTrace`

## Beklenen olaylar

- `egress.denied`
- `dlp.secret_detected`
- `credential.revoked`
- `incident.opened`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-16-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-16-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-16-state-before.json` ve `ACC-16-state-after.json`.
- `ACC-16-events.json`, `ACC-16-policy-decisions.json` ve `ACC-16-audit-export.json`.
- `ACC-16-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Canary credentials revoke/rotate; malicious workload destroy, destination/log fixture cleanup.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
