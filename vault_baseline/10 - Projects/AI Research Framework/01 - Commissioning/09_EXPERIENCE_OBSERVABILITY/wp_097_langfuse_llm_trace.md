# WP-097 — Langfuse Model/Agent Trace ve Prompt Governance

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-097` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | AI Observability Lead |
| Bağımsız doğrulayıcı | Privacy/Security / Eval Office |
| Hard dependencies | WP-006, WP-013, WP-020, WP-025, WP-026, WP-041, WP-046, WP-047, WP-055, WP-056, WP-057, WP-096 |
| İlgili gate | G2–G7 |
| İlgili kontroller | CTL-OBS-02, CTL-DAT-03 |
| İlgili ACC senaryoları | ACC-32 |

## Amaç ve beklenen sonuç

Agent/model çağrılarında prompt/template/model/tool/token/latency/cost ve eval sinyalleri data-class retention/redaction ile izlenir; private chain-of-thought talep edilmez.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md), [WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/wp_055_spiffe_vault_identity.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-057 — Default-Deny Egress Proxy, DLP ve Allowlist](../06_EXECUTION_SECURITY/wp_057_egress_proxy_dlp.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-097-T01 | Langfuse deployment/project/RBAC/data routing kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-097-T02 | Trace hierarchy ve AIRL correlation mapping uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-097-T03 | Prompt/template version registry bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-097-T04 | Input/output/tool schema redaction/minimization ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-097-T05 | No-chain-of-thought ve rationale summary policy uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-097-T06 | Eval feedback/cost/export/retention ve backup kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Langfuse platform`
- `Prompt registry`
- `Trace/redaction policy`
- `Retention/export runbook`
- `Trace quality dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Secret in prompt redacted/quarantined
- D3 trace minimum fields
- Prompt version correlation
- Private reasoning not stored
- Backup/restore
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Trace canonical workflow/claim state değildir
- [ ] Sensitive data TTL ve purpose'a uyar
- [ ] Model outcome kısa gerekçe/evidence/gap taşır, gizli düşünce dökümü değil
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

Trace pipeline disable/redact-first moduna alınabilir; canonical run/evidence devam eder ve telemetry gap kaydedilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
