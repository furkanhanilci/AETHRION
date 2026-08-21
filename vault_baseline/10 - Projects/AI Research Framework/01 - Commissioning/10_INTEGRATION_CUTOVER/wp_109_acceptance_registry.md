# WP-109 — Kırk Acceptance Senaryosu Registry ve Harness

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-109` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Platform Assurance Lead |
| Bağımsız doğrulayıcı | Commissioning Board |
| Hard dependencies | WP-002, WP-009, WP-020, WP-024, WP-040, WP-060, WP-090, WP-099, WP-102, WP-103, WP-104, WP-105, WP-106, WP-107, WP-108 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-OPS-02, CTL-SEC-04 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

ACC-01–ACC-40 Given/When/Then, fixture, expected event/invariant, evidence, owner, severity ve cleanup ile versioned test registry'sinde otomatik/manuel çalıştırılabilir olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md), [WP-009 — Control Kataloğu, Exception ve Non-Waivable Blocker'lar](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-024 — CI Temeli ve Deterministik Kalite Kapıları](../03_FOUNDATION/wp_024_ci_quality_gates.md), [WP-040 — Workflow Replay, Versioning ve Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite ve Red-Team Kabulü](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-090 — PublicationPackage, RO-Crate ve Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-102 — Dikey Dilim 1 — Intake → Protocol Freeze](../10_INTEGRATION_CUTOVER/wp_102_vertical_slice_intake_protocol.md), [WP-103 — Dikey Dilim 2 — İki Yönlü Literatür ve Set Freeze](../10_INTEGRATION_CUTOVER/wp_103_vertical_slice_literature.md), [WP-104 — Dikey Dilim 3 — Baseline → Run → Claim/Evidence](../10_INTEGRATION_CUTOVER/wp_104_vertical_slice_run_claim.md), [WP-105 — Dikey Dilim 4 — Blind Review → Arbitration → Clean-Room](../10_INTEGRATION_CUTOVER/wp_105_vertical_slice_review_repro.md), [WP-106 — Dikey Dilim 5 — Human Decision → Publish → Monitor](../10_INTEGRATION_CUTOVER/wp_106_vertical_slice_decision_publish_monitor.md), [WP-107 — Engineering Dikey Dilim — Spec → Worktree → Signed Release](../10_INTEGRATION_CUTOVER/wp_107_engineering_vertical_slice.md), [WP-108 — Retraction, Drift ve Supersession Dikey Dilimi](../10_INTEGRATION_CUTOVER/wp_108_retraction_drift_vertical_slice.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-109-T01 | 40 senaryoyu machine-readable registry'ye aktar | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-109-T02 | Fixture/environment/data seeding standardı yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-109-T03 | Expected canonical/event/audit/policy assertions ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-109-T04 | Test runner, evidence capture ve result signing kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-109-T05 | Manual human/DR steps için witness protocol yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-109-T06 | Retry/flakiness/skip/waiver ve cleanup kuralı ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Acceptance Registry`
- `Scenario runner`
- `Fixture catalog`
- `Evidence capture/signing`
- `Result dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Registry schema validation
- Known-pass/fail scenario
- Same RC digest enforcement
- Critical SKIP not pass
- Cleanup isolation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her senaryo owner ve immutable result taşır
- [ ] Sonuçlar aynı release candidate/policy/schema bundle'dadır
- [ ] Critical senaryo skipped/waived olamaz
- [ ] Bütün zorunlu testler aynı target revision üzerinde geçmiştir.
- [ ] Açık Critical/High finding yoktur; non-waivable blocker bulunmamaktadır.
- [ ] Bağımsız verifier kanıt paketini kabul etmiştir.
- [ ] Rollback/compensation davranışı denenmiş ve audit edilmiştir.
- [ ] İlgili dashboard, alert, audit query veya integrity query çalışma kanıtı üretmiştir.

## Kabul kanıtı paketi

- Aynı target revision/digest üzerinde alınmış test sonuçları
- Environment, schema, policy ve dependency sürümlerini içeren EvidenceManifest
- Bağımsız verifier ReviewRecord veya VerificationRecord'u
- Rollback/compensation denemesi ve sonuç referansı
- Açık finding, residual risk ve owner/expiry listesi

## Riskler ve kontrol noktaları

- Contract veya canonical sahiplik belirsizse implementasyon durur ve Architecture Board'a eskale edilir.
- Identity, data route, artifact integrity, bağımsızlık veya kritik evidence problemi waiver ile geçirilemez.
- Geçici manuel kontrol gerekiyorsa owner, scope, expiry, compensating control ve kaldırma paketi kaydedilir.
- Paket tamamlandı beyanı acceptance değildir; verifier kararı olmadan yalnız `TECH_COMPLETE` olabilir.

## Rollback / compensation

Harness release canary fixture ile doğrulanır; bozuk harness sonuçları INVALIDATED ve tüm etkilenmiş senaryolar yeniden koşulur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
