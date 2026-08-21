# ACC-18 — D3 Data to Public Provider

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-18` |
| Kategori | Security/Privacy |
| Severity | **Critical** |
| Accountable Owner | Safety & Governance Owner |
| Bağımsız witness/verifier | Privacy Reviewer |
| İlgili paketler | `WP-041`, `WP-056`, `WP-057`, `WP-112` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **D3 Data to Public Provider** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** TaskContract D3 restricted veri içerir ve public external model profile'ı istenir.

**When:** Router/OPA/Gateway route kararı verir.

**Then:** Public provider çağrısı yapılmaz; secure/local eligible route varsa seçilir, yoksa BLOCKED olur ve audit kaydı çıkar.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | D3 synthetic data/TaskContract oluştur | Execution log + trace/event references |
| 2 | Public provider'ı explicit talep et | Execution log + trace/event references |
| 3 | OPA/router candidate filter çalıştır | Execution log + trace/event references |
| 4 | Secure route available ve unavailable varyantlarını dene | Execution log + trace/event references |
| 5 | Gateway provider call logs sorgula | Execution log + trace/event references |
| 6 | Decision/explanation UI kontrol et | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Public provider calls=0
- [ ] Policy deny D3 rule/bundle taşır
- [ ] Secure route only if admitted
- [ ] No route→BLOCKED
- [ ] Sensitive raw data trace/eventte yok
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `TaskContract`
- `PolicyDecision`
- `RouteDecision`
- `GatewayAudit`
- `WorkflowState`

## Beklenen olaylar

- `data.route.denied`
- `route.secure_selected_or_blocked`
- `workflow.blocked`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-18-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-18-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-18-state-before.json` ve `ACC-18-state-after.json`.
- `ACC-18-events.json`, `ACC-18-policy-decisions.json` ve `ACC-18-audit-export.json`.
- `ACC-18-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Synthetic D3 data secure deletion policy ile temizlenir; audit/evidence retained.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
