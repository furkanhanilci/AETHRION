# WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-101` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Service Owners / Internal Audit |
| Hard dependencies | WP-002, WP-022, WP-025, WP-026, WP-028, WP-031, WP-041, WP-049, WP-052, WP-055, WP-056, WP-061, WP-075, WP-096, WP-098, WP-099, WP-100 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-OBS-01, CTL-OPS-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Her servisin owner, tier, dependency, data class, SLI/SLO, error budget, dashboard, alert, runbook ve DR sınıfı katalogda tutulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği](../01_GOVERNANCE/WP-002_kapsam_nfr_izlenebilirlik.md), [WP-022 — Repository Topolojisi ve Kod Sahipliği](../03_FOUNDATION/WP-022_repository_topolojisi.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/WP-028_nats_jetstream_outbox.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/WP-052_kubernetes_cluster.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/WP-096_otel_correlation.md), [WP-098 — Grafana ve Altı Operasyon Grafiği](../09_EXPERIENCE_OBSERVABILITY/WP-098_grafana_six_graphs.md), [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-100 — Cost Ledger, Bütçe Zarfları ve FinOps](../09_EXPERIENCE_OBSERVABILITY/WP-100_cost_ledger_finops.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-101-T01 | Service Catalog schema/registry kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-101-T02 | Tier ve critical user journey mapping yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-101-T03 | Availability/latency/correctness/freshness/durability SLI'ları tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-101-T04 | Error budget ve release freeze rule yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-101-T05 | Alert owner/escalation/runbook link checker ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-101-T06 | Dependency/SLO roll-up ve quarterly review kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Service Catalog`
- `SLO catalog`
- `Error-budget policy`
- `Alert-runbook link checker`
- `Ownership dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Orphan service/alert detection
- Synthetic SLO breach
- Error budget release freeze
- Owner departure continuity
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Production servis owner/runbook/SLO olmadan açılmaz
- [ ] Correctness/freshness SLO uptime'ın yanında ölçülür
- [ ] Kritik alert 24x7 escalation taşır
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

Yanlış SLO değişikliği service owner+SRE review ile rollback; alarmı susturmak kontrolü kapatmak sayılır ve süreli exception ister.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
