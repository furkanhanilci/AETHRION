# ACC-39 — Negative Research Result

## Senaryo kartı

| Alan | Değer |
|---|---|
| Senaryo | `ACC-39` |
| Kategori | Research/Portfolio |
| Severity | **Medium** |
| Accountable Owner | Scientific Owner |
| Bağımsız witness/verifier | Methodologist / Project Decision Owner |
| İlgili paketler | `WP-081`, `WP-082`, `WP-083`, `WP-104`, `WP-113` |
| Production kabulü | Critical senaryo SKIP veya waiver ile PASS sayılamaz |

## Amaç

Bu senaryo, **Negative Research Result** durumunda hedef mimarinin fail-safe ve kanıt üretme davranışını doğrular. Test aynı release candidate, policy bundle, schema bundle ve environment manifest üzerinde çalıştırılır.

## Given / When / Then

**Given:** Pre-registered protocol/baseline altında intervention/approach baseline'ı geçmemektedir.

**When:** Run, analysis, review ve portfolio decision tamamlanır.

**Then:** Sonuç kaybolmaz veya başarıya çevrilmez; negative Run/Claim artifact, limitation ve stop/pivot/continue DecisionRecord oluşur.

## Önkoşullar

- İlgili work package'lar `INTEGRATED` veya `COMMISSIONING_READY` durumundadır.
- Teste özel project/actor/data/artifact kimlikleri production verisinden ayrılmıştır.
- Release candidate digest ile policy, schema, model/tool ve infrastructure bundle sürümleri freeze edilmiştir.
- Beklenen canonical records, events, policy decisions, telemetry ve audit assertions registry'ye girilmiştir.
- Failure injection blast radius, kill switch, cleanup ve witness atanmıştır.

## Test adımları

| # | İşlem | Toplanacak anlık kanıt |
|---:|---|---|
| 1 | Frozen protocol/baseline/stop rule hazırla | Execution log + trace/event references |
| 2 | Baseline'ı geçmeyen reproducible run çalıştır | Execution log + trace/event references |
| 3 | Metric/uncertainty/robustness analiz et | Execution log + trace/event references |
| 4 | Claim/negative result artifact oluştur | Execution log + trace/event references |
| 5 | Review ve decision queue çalıştır | Execution log + trace/event references |
| 6 | Knowledge/Obsidian/portfolio write-back doğrula | Execution log + trace/event references |

## Zorunlu invariant ve assertions

- [ ] Run retained with FAILED_TO_BEAT_BASELINE/NEGATIVE
- [ ] No post-hoc metric/baseline mutation
- [ ] Decision rationale/next action
- [ ] Cost captured
- [ ] Knowledge searchable
- [ ] Expected canonical state ile actual state aynı veya açıklanmış güvenli failure state'indedir.
- [ ] Duplicate, stale, forged veya partial input unsafe yan etki üretmemiştir.
- [ ] Trace, event, audit ve business record aynı project/workflow/run correlation zincirindedir.
- [ ] Test sırasında oluşan her Critical/High finding Finding Registry'ye kaydedilmiştir.

## Beklenen canonical kayıtlar

- `RunManifest`
- `NegativeResultArtifact`
- `ClaimRecord`
- `ReviewRecord`
- `PortfolioDecision`

## Beklenen olaylar

- `experiment.negative_result`
- `claim.not_supported`
- `decision.required`
- `project.stopped_pivoted_or_continued`

Beklenen olay sayısı/idempotency ve sıra kısıtları test registry'deki machine-readable assertion dosyasında tutulur. NATS event'i tek başına canonical state kanıtı değildir; ilgili service/Temporal commit'i ayrıca doğrulanır.

## Kanıt paketi

- `ACC-39-result.json`: PASS/FAIL, RC digest ve assertion sonuçları.
- `ACC-39-execution-log.jsonl`: zaman sıralı test/fault/decision kayıtları.
- `ACC-39-state-before.json` ve `ACC-39-state-after.json`.
- `ACC-39-events.json`, `ACC-39-policy-decisions.json` ve `ACC-39-audit-export.json`.
- `ACC-39-evidence-manifest.json`: bütün dosyaların hash, producer ve environment referansı.
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

Test project CLOSED/ARCHIVED; negative artifact searchable test corpus'ta kalır.

Cleanup canonical evidence ve audit geçmişini silmez. Destructive test fixture işlemleri yalnız explicit test namespace/kimlikleri üzerinde ve iki aşamalı doğrulamayla yapılır.
