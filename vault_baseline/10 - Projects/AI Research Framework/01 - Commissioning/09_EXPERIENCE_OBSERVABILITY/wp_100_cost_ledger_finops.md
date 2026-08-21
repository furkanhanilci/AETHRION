# WP-100 — Cost Ledger, Bütçe Zarfları ve FinOps

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-100` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | FinOps Lead |
| Bağımsız doğrulayıcı | Project Decision Owner / Internal Audit |
| Hard dependencies | WP-011, WP-013, WP-015, WP-016, WP-025, WP-028, WP-041, WP-045, WP-049, WP-052, WP-053, WP-082, WP-096 |
| İlgili gate | G0,G4,G5,G8 |
| İlgili kontroller | CTL-CST-01, CTL-CST-02 |
| İlgili ACC senaryoları | ACC-09, ACC-29 |

## Amaç ve beklenen sonuç

Model, compute, retrieval, storage, verification ve human triage maliyeti project/workflow/run/role/profile/outcome'a bağlanır; 80% uyarı ve 100% hard stop uygulanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md), [WP-053 — Kueue Queue, Kota ve Öncelik Politikası](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-100-T01 | BudgetEnvelope/C0–C4 class ve reservation API kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-100-T02 | Gateway/Kueue/tool/storage/human cost event ingest et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-100-T03 | Estimate/reserve/commit/release ve retry/fan-out attribution yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-100-T04 | 80/100% Temporal pause/decision entegrasyonu yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-100-T05 | Provider invoice reconciliation/variance case ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-100-T06 | Quality-adjusted cost/outcome dashboard ve forecast kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Cost Ledger`
- `Budget service`
- `Cost adapters`
- `Invoice reconciliation`
- `FinOps dashboard/runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- 80% warning
- 100% new expensive work deny
- Cancelled reservation release
- Duplicate cost event idempotency
- Invoice variance case
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Hard budget aşıldığında state kaybolmaz
- [ ] Maliyet salt token değildir
- [ ] Critical assurance kapasitesi budget policy'de görünürdür
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

Yanlış cost adapter etkisi reconciliation ile düzeltilir; hard stop manual disable edilmez, owner DecisionRecord gerekir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
