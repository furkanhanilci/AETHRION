# ACC-32 — Secret in Prompt/Trace

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-32` |
| Kategori | Security/Observability |
| Severity | **Critical** |
| Accountable Owner | AI Observability Lead |
| Bağımsız witness/verifier | Privacy/Security Reviewer |
| İlgili paketler | `WP-057`, `WP-097`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Secret in Prompt/Trace** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Synthetic canary credential model prompt/tool input'unda bulunur.

**When:** Gateway/LangGraph/Langfuse/OTel/log pipelines request'i işler.

**Then:** Secret raw telemetry, event veya UI'da görünmez; redaction/quarantine ve security event oluşur, credential revoke edilir.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Canary secret ve lookup detector hazırla | Execution log + trace/event references |
| 2 | Prompt/tool input'a canary ekle | Execution log + trace/event references |
| 3 | Model/tool trace pipeline çalıştır | Execution log + trace/event references |
| 4 | Langfuse/OTel/log/NATS/audit/search stores tarat | Execution log + trace/event references |
| 5 | UI/export sample kontrol et | Execution log + trace/event references |
| 6 | Revoke/incident davranışını doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Raw canary occurrences permitted stores=0
- [ ] Redaction marker/provenance present
- [ ] Security event/lease revoke
- [ ] DLP detector false-negative yok
- [ ] Canonical task result policy'ye uygun
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `DLPRecord`
- `RedactedTrace`
- `SecurityEvent`
- `VaultLeaseRecord`
- `AuditRecord`

## Beklenen olaylar

- `trace.secret_detected`
- `telemetry.redacted_or_quarantined`
- `credential.revoked`
- `incident.opened`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-32-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-32-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-32-state-before.json` ve `ACC-32-state-after.json`.
- `ACC-32-events.json`, `ACC-32-policy-decisions.json` ve `ACC-32-audit-export.json`.
- `ACC-32-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Canary revoke/delete; telemetry test records retention'a göre redacted halde saklanır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
