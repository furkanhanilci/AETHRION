# WP-046 — LangGraph Bounded Cognition Runtime

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-046` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Agent Platform Lead |
| Bağımsız doğrulayıcı | Control Plane Architect / Security |
| Hard dependencies | WP-013, WP-020, WP-031, WP-032, WP-041, WP-045 |
| İlgili gate | G2–G7 |
| İlgili kontroller | CTL-OPS-02, CTL-DAT-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

LangGraph yalnız TaskContract kapsamındaki node/state, checkpoint, interrupt ve AgentResult üretimini yönetir; lifecycle state ve side effect sahiplenmez.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/wp_013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/wp_031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/wp_032_project_lifecycle_skeleton.md), [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-046-T01 | Canonical task graph wrapper ve state schema kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-046-T02 | Temporal activity/child task adapter'ını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-046-T03 | Checkpoint store ve TTL/data-class policy bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-046-T04 | Node timeout/retry/cancel semantiği uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-046-T05 | Tool/Execution Broker dışında side effect'i engelle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-046-T06 | AgentResult/artifact upload ve trace correlation ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `LangGraph runtime`
- `Temporal adapter`
- `Checkpoint policy`
- `Agent graph SDK`
- `Conformance tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Task cancel propagation
- Checkpoint resume
- Direct side-effect negative test
- Runtime kaybı sonrası TaskContract'tan rebuild
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] LangGraph gate/workflow state'i kopyalamaz
- [ ] Her dış etki broker çağrısıdır
- [ ] Checkpoint hassas veri retention politikasına uyar
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

Runtime release task bazında canary edilir; başarısız task yeni runtime ile yeniden dispatch veya son checkpoint'ten resume edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
