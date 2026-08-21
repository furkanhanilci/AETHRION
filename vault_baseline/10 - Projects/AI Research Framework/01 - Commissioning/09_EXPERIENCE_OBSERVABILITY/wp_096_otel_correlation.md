# WP-096 — OpenTelemetry Uçtan Uca Correlation Spine

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-096` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Observability Lead |
| Bağımsız doğrulayıcı | Security / SRE |
| Hard dependencies | WP-011, WP-015, WP-020, WP-021, WP-025, WP-028, WP-031, WP-041, WP-046, WP-049, WP-052, WP-055, WP-057, WP-082 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-OBS-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Console komutundan Temporal workflow, agent/model/tool, sandbox, DB/event, artifact, claim ve cost kaydına aynı project/workflow/run/trace korelasyonu taşınır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md), [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-057 — Default-Deny Egress Proxy, DLP ve Allowlist](../06_EXECUTION_SECURITY/wp_057_egress_proxy_dlp.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-096-T01 | OTel collector/gateway HA ve tenant/data-class routing kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-096-T02 | Trace/span/log/metric semantic conventions yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-096-T03 | Context propagation SDK'larını servislere bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-096-T04 | Temporal activity, LangGraph, model, tool, DB, NATS, K8s instrumentation ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-096-T05 | Sampling/error escalation ve clock policy uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-096-T06 | Trace completeness SLO/query kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `OTel platform`
- `Semantic conventions`
- `Instrumentation libraries`
- `Trace completeness dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- End-to-end request trace
- Async NATS causation link
- Retry/duplicate span semantics
- Missing correlation alarm
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Correlation ID canonical recordlarla eşleşir
- [ ] Trace absence business state kaybı değildir fakat SLO ihlalidir
- [ ] D3/D4 raw payload span attribute olmaz
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

Collector outage telemetry buffer/drop policy ile iş akışını unsafe yapmaz; config rollback ve gap IncidentRecord açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
