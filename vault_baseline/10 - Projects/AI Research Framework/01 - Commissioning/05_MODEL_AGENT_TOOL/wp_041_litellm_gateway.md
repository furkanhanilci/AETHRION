# WP-041 — LiteLLM Model Gateway Temeli

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-041` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Model Platform Lead |
| Bağımsız doğrulayıcı | Security / FinOps / SRE |
| Hard dependencies | WP-006, WP-011, WP-013, WP-016, WP-020, WP-021, WP-025 |
| İlgili gate | G2–G7 |
| İlgili kontroller | CTL-DAT-02, CTL-CST-01, CTL-MOD-01 |
| İlgili ACC senaryoları | ACC-09, ACC-10, ACC-11, ACC-18 |

## Amaç ve beklenen sonuç

Bütün model çağrıları provider bağımsız gateway üzerinden kimlikli, data-class kontrollü, bütçeli, rate-limited ve gözlemlenebilir hale gelir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/wp_025_postgres_ha_foundation.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-041-T01 | Gateway HA deployment ve provider adapter'larını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-041-T02 | Workload identity, project/role tags ve auth bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-041-T03 | Data/region/retention route filtrelerini uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-041-T04 | Timeout/rate-limit/circuit-breaker ve admitted fallback kuralı ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-041-T05 | Prompt/output redaction ile usage/cost event üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-041-T06 | Pinned snapshot ve cache policy'sini uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `LiteLLM deployment`
- `Provider configuration`
- `Gateway policy adapter`
- `Model-call audit/cost events`
- `Gateway runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- D3 public provider deny
- Primary 5xx admitted fallback
- No eligible fallback BLOCKED
- Hard budget deny
- Snapshot/usage correlation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Doğrudan provider credential kullanımı yoktur
- [ ] Fallback aynı policy kapsamına admitted olmalıdır
- [ ] Model alias yerine snapshot kaydedilir
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

Provider/config değişikliği canary+shadow ile promote edilir; hata halinde route eski imzalı config'e döner.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
