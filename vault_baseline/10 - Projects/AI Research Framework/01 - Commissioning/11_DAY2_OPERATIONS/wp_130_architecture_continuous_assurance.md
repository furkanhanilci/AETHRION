# WP-130 — Architecture ve Platform Continuous Assurance

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-130` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Chief Architect / Platform Assurance Lead |
| Bağımsız doğrulayıcı | Architecture Board / Internal Audit |
| Hard dependencies | WP-010, WP-030, WP-040, WP-060, WP-109, WP-115, WP-121, WP-123, WP-124, WP-125, WP-126, WP-127, WP-128, WP-129 |
| İlgili gate | G0–G10,Platform,Day-2 |
| İlgili kontroller | Tüm kontroller |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Mimari invariant, canonical sahiplik, contract compatibility, workflow replay, derived rebuild, golden research path ve control effectiveness düzenli olarak yeniden doğrulanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-010 — Mimari Karar ve Reddedilen Alternatifler Baseline'ı](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-040 — Workflow Replay, Versioning ve Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite ve Red-Team Kabulü](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-109 — Kırk Acceptance Senaryosu Registry ve Harness](../10_INTEGRATION_CUTOVER/wp_109_acceptance_registry.md), [WP-115 — Tam Sistem Regression ve Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md), [WP-123 — Control Effectiveness ve Policy Regression Ritmi](../11_DAY2_OPERATIONS/wp_123_control_effectiveness.md), [WP-124 — Model Requalification, Drift ve Ejection Ritmi](../11_DAY2_OPERATIONS/wp_124_model_requalification_drift.md), [WP-125 — Literatür, Zotero ve Obsidian Kürasyon Ritmi](../11_DAY2_OPERATIONS/wp_125_literature_knowledge_curation.md), [WP-126 — Reviewer, Judge ve Reproducer Kalibrasyonu](../11_DAY2_OPERATIONS/wp_126_assurance_calibration.md), [WP-127 — FinOps, Kapasite ve Portfolio Review Ritmi](../11_DAY2_OPERATIONS/wp_127_finops_portfolio.md), [WP-128 — Incident, Postmortem ve Learning Closure](../11_DAY2_OPERATIONS/wp_128_incident_learning.md), [WP-129 — Quarterly DR, Supply-Chain ve Audit Tatbikatı](../11_DAY2_OPERATIONS/wp_129_quarterly_dr_supply_chain.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-130-T01 | Monthly architecture drift/canonical owner scan yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-130-T02 | Schema/adapter/policy compatibility suite çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-130-T03 | Golden-path synthetic research ve engineering koş | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-130-T04 | Derived graph/index/Obsidian rebuild sample çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-130-T05 | Platform chaos/replay/backup evidence'ını review et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-130-T06 | ADR re-open triggers, service retirement ve technical debt kararları üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Continuous Assurance report`
- `Architecture drift findings`
- `Golden-path results`
- `ADR/retirement decisions`
- `Assurance backlog`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Canonical dual-write drift
- Workflow replay regression
- Graph rebuild
- Golden G0–G10
- Policy/control two-failure trigger
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Platform kendi araştırma assurance sistemiyle doğrulanır
- [ ] İki tekrarlı material control failure ADR'ı yeniden açar
- [ ] Target architecture sessizce ürün bağımlılığına kaymaz
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

Drift critical ise ilgili release/route/control pause; son validated baseline'a dönülür ve impact scan yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
