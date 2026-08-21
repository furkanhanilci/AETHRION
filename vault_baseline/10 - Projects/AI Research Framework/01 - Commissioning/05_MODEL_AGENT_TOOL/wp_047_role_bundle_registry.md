# WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-047` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Agent Platform Lead |
| Bağımsız doğrulayıcı | Governance / Eval Office |
| Hard dependencies | WP-003, WP-007, WP-013, WP-020, WP-042, WP-045, WP-046 |
| İlgili gate | G1–G7 |
| İlgili kontroller | CTL-GOV-02, CTL-MOD-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Rol mandate'i, prompt/policy, input/output schema, allowed tools, context, eval ve acceptance şartı versioned RoleBundle'a derlenir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-003 — Rol Kataloğu ve RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-042 — Capability Registry ve Profil Yaşam Döngüsü](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/wp_046_langgraph_runtime.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-047-T01 | RoleBundle schema ve Git registry kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-047-T02 | RoleContract→runtime prompt/tool/context compiler yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-047-T03 | Planner, scout, extractor, methodologist, coder, reviewer, reproducer ve curator başlangıç bundle'larını oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-047-T04 | Context budget ve frozen-package policy bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-047-T05 | Bundle signature/admission/eval refs ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-047-T06 | Deprecation/migration yönetimi kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Role Bundle Registry`
- `Bundle compiler`
- `Core role bundles`
- `Bundle conformance tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Forbidden tool excluded
- Missing acceptance compile fail
- Reviewer producer trace contamination negative test
- Bundle signature validation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Rol model adı değildir
- [ ] Bundle explicit input/output/non-goal taşır
- [ ] Reviewer bundle blind context ve independence obligation uygular
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

Hatalı bundle revoke edilir; registry pointer önceki imzalı sürüme döner ve açık task'lar impact alır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
