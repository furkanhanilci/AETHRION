# WP-049 — Tool Registry ve Tool Broker Çekirdeği

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-049` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Tool Platform Lead |
| Bağımsız doğrulayıcı | Security Architect / Internal Audit |
| Hard dependencies | WP-006, WP-011, WP-013, WP-015, WP-016, WP-020, WP-025, WP-026, WP-028, WP-046 |
| İlgili gate | G3,G5,G9,Engineering |
| İlgili kontroller | CTL-OPS-01, CTL-SEC-01, CTL-SEC-03 |
| İlgili ACC senaryoları | ACC-05, ACC-12, ACC-35 |

## Amaç ve beklenen sonuç

T0–T5 bütün araç çağrıları imzalı tool schema, purpose, actor, scope, data class, idempotency, policy, credential lease ve audit zincirinden geçer.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/wp_015_event_envelope_taxonomy.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-028 — NATS JetStream ve Transactional Outbox Temeli](../03_FOUNDATION/wp_028_nats_jetstream_outbox.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-049-T01 | ToolDefinition registry/signature/versioning kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-049-T02 | InvocationEnvelope validate et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-049-T03 | OPA actor×purpose×data×tool×target×risk kararını bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-049-T04 | Idempotency/reconciliation store yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-049-T05 | Vault/SPIRE credential lease ve egress proxy adapter'ını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-049-T06 | Result quarantine/redaction/provenance ve ToolReceipt üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Tool Registry`
- `Tool Broker service`
- `Invocation/Receipt persistence`
- `Connector SDK`
- `Audit events`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Unsigned/free-form tool schema deny
- Duplicate invocation one effect
- Scoped target violation
- Secret redaction
- Partial response timeout reconciliation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Agent doğrudan connector/credential kullanamaz
- [ ] T3+ gerekli approval olmadan çalışmaz
- [ ] Her çağrı policy decision ve ToolReceipt taşır
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

Connector/broker hatasında idempotency state korunur; uncertain effect RECONCILIATION_REQUIRED olur, otomatik tekrar edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
