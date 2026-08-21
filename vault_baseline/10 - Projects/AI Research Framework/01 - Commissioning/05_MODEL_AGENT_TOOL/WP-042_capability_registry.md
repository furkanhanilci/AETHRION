# WP-042 — Capability Registry ve Profil Yaşam Döngüsü

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-042` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Eval Office |
| Bağımsız doğrulayıcı | Model Platform Lead / Safety |
| Hard dependencies | WP-005, WP-006, WP-007, WP-011, WP-013, WP-016, WP-020, WP-025, WP-041 |
| İlgili gate | G1,G5,G10 |
| İlgili kontroller | CTL-MOD-01, CTL-MOD-02 |
| İlgili ACC senaryoları | ACC-36 |

## Amaç ve beklenen sonuç

Model snapshot/runtime adapter kombinasyonlarının admitted role, data, tool, risk, eval, cost, expiry ve ejection durumu canonical registry'de tutulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/WP-005_risk_assurance_profili.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/WP-006_execution_profili.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/WP-011_kimlik_korelasyon_standardi.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/WP-041_litellm_gateway.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-042-T01 | CapabilityProfile persistence/API kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-042-T02 | REGISTERED→SHADOW→ADVISORY→CONDITIONAL→MANDATORY/SUSPENDED/DISABLED state machine yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-042-T03 | Role/data/tool/risk eligibility query'si ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-042-T04 | Expiry/requalification/ejection trigger'larını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-042-T05 | Open task impact event'ini bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-042-T06 | Change/audit UI contract'ını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Capability Registry service`
- `Profile state machine`
- `Eligibility API`
- `Expiry/revoke scheduler`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Expired profile route dışı
- Suspended profile fallback olmaz
- Snapshot change requalification
- Revoke açık task ImpactCase
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Registry dışında model-role ataması yapılamaz
- [ ] Qualification süresi dolan profil otomatik askıya alınır
- [ ] Profile immutable eval bundle ref taşır
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

Yanlış profile revoke edilir; router cache invalidation ve impact scan çalışır, geçmiş run lineage korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
