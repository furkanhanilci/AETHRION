# ACC-15 — Sandbox Escape Attempt

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-15` |
| Kategori | Security/Execution |
| Severity | **Critical** |
| Accountable Owner | Execution Security Lead |
| Bağımsız witness/verifier | Red Team / SRE |
| İlgili paketler | `WP-054`, `WP-060`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Sandbox Escape Attempt** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Malicious code fixture host mount, privileged syscall, namespace escape ve metadata/credential endpoint erişimi dener.

**When:** Kod gVisor execution cell'de çalıştırılır.

**Then:** Escape yolları deny/contain edilir; credential/host veri sızmaz, cell durdurulur ve forensic SecurityEvent üretilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Signed malicious test image'i attack registry'den çöz | Execution log + trace/event references |
| 2 | ExecutionProfile ile sandbox başlat | Execution log + trace/event references |
| 3 | Syscall/mount/namespace/metadata attacks çalıştır | Execution log + trace/event references |
| 4 | Runtime/network/Vault telemetry izle | Execution log + trace/event references |
| 5 | Contain/stop/snapshot/node action'ını doğrula | Execution log + trace/event references |
| 6 | Post-test host/cluster integrity kontrol et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Host file read/write=0
- [ ] Privileged syscall/escape deny
- [ ] Secret lease minimum/none
- [ ] Forensic artifact tam
- [ ] Node/other workload etkilenmez
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `SandboxAttestation`
- `RuntimeSecurityRecord`
- `ForensicArtifact`
- `SecurityIncident`
- `ExecutionLease`

## Beklenen olaylar

- `sandbox.escape_attempted`
- `runtime.denied`
- `execution.contained`
- `incident.opened`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-15-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-15-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-15-state-before.json` ve `ACC-15-state-after.json`.
- `ACC-15-events.json`, `ACC-15-policy-decisions.json` ve `ACC-15-audit-export.json`.
- `ACC-15-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Malicious cell destroy; gerekiyorsa node drain/reimage, fixture image yalnız test registry'de tutulur.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
