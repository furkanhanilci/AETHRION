# WP-056 — OPA Policy Platform ve Bundle Dağıtımı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-056` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Policy Platform Lead |
| Bağımsız doğrulayıcı | Safety / Security / Internal Audit |
| Hard dependencies | WP-005, WP-006, WP-007, WP-009, WP-016, WP-020, WP-021, WP-055 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-GOV-02, CTL-DAT-02, CTL-SEC-02 |
| İlgili ACC senaryoları | ACC-06, ACC-18, ACC-24, ACC-26 |

## Amaç ve beklenen sonuç

Role, data, tool, model, environment, gate, exception ve budget kararları testli, imzalı, açıklanabilir OPA bundle'larıyla bütün enforcement noktalarına dağıtılır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/WP-005_risk_assurance_profili.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/WP-006_execution_profili.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-009 — Control Kataloğu, Exception ve Non-Waivable Blocker'lar](../01_GOVERNANCE/WP-009_control_exception_katalogu.md), [WP-016 — PolicyDecision, Control ve Exception Şemaları](../02_CONTRACTS/WP-016_policy_control_exception_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/WP-021_ortam_hesap_ag_baseline.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-056-T01 | Policy repository/module sınırlarını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-056-T02 | Input document ve decision API standardını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-056-T03 | Unit/negative/property test harness yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-056-T04 | Signed bundle build/promotion/rollback kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-056-T05 | Decision log redaction/WORM export bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-056-T06 | Shadow evaluation ve drift/coverage telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `OPA platform`
- `Policy bundle v1`
- `Policy test suite`
- `Bundle promotion pipeline`
- `Decision log pipeline`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- D3 route/T4 action/self-review deny
- Expired exception deny
- Bundle rollback
- Unknown input fail-closed
- Shadow decision diff
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Untested/unsigned bundle production'a gidemez
- [ ] Karar rule ID, bundle digest ve obligations taşır
- [ ] Policy unavailable critical action fail-closed olur
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

Hatalı bundle imzalı önceki version'a atomik döner; karar history korunur ve impact scan açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
