# WP-045 — Policy Router ve Minimum Yeterli Model Paketi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-045` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Model Platform Lead |
| Bağımsız doğrulayıcı | Safety / Eval / FinOps |
| Hard dependencies | WP-005, WP-006, WP-007, WP-013, WP-016, WP-041, WP-042, WP-044 |
| İlgili gate | G1,G5,G6 |
| İlgili kontroller | CTL-DAT-02, CTL-CST-01, CTL-MOD-01 |
| İlgili ACC senaryoları | ACC-09, ACC-10, ACC-11, ACC-18, ACC-38 |

## Amaç ve beklenen sonuç

TaskContract role/risk/data/tool/latency/bütçe/independence girdilerinden yalnız eligible ve minimum yeterli model/agent paketini deterministik seçer.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/wp_016_policy_control_exception_contracts.md), [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-042 — Capability Registry ve Profil Yaşam Döngüsü](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-044 — Model Qualification ve Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-045-T01 | OPA pre-filter ve Capability Registry query'sini bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-045-T02 | Quality-adjusted cost ve latency seçim sırasını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-045-T03 | Single model vs parallel/council fan-out kurallarını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-045-T04 | Independence-aware reviewer route uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-045-T05 | Fallback/retry/fan-out budget reservation ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-045-T06 | RouteDecision açıklaması ve telemetry üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Policy Router`
- `RouteDecision service`
- `Fan-out/budget rules`
- `Routing conformance suite`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Düşük risk en ucuz eligible route
- R3 cross-family constraint
- Budget insufficient pause
- No eligible route BLOCKED
- Fallback independence recalculation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Yasak provider/profile aday listesine girmez
- [ ] Council varsayılan değildir
- [ ] Route her rule, profile ve budget kararını kaydeder
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

Router rule release shadow comparison sonrası promote edilir; anomalide önceki bundle'a dönülür ve yanlış route'lar impact scan alır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
