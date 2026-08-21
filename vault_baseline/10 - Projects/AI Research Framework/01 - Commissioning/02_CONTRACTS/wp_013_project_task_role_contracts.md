# WP-013 — Project, Task ve Role Contract Şemaları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-013` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Control Plane Lead |
| Bağımsız doğrulayıcı | Governance Lead |
| Hard dependencies | WP-003, WP-004, WP-005, WP-006, WP-007, WP-011 |
| İlgili gate | G0–G6 |
| İlgili kontroller | CTL-GOV-01, CTL-DAT-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Yaşam döngüsü ve agent runtime arasında proje niyeti, rol, risk, veri, araç, bütçe, kabul ve bağımsızlık alanları versioned contract'larla taşınır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-003 — Rol Kataloğu ve RACI Baseline](../01_GOVERNANCE/wp_003_role_catalog_raci.md), [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-005 — Araştırma Risk ve Assurance Profili](../01_GOVERNANCE/wp_005_risk_assurance_profile.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-013-T01 | ProjectCharter/ControlPlan contract'ını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-013-T02 | TaskContract input/output/non-goal/acceptance alanlarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-013-T03 | RoleContract mandate/tool/data/risk/prohibited alanlarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-013-T04 | AgentResult ve gap/assumption formatını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-013-T05 | Backward compatibility ve contract version rules yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `ProjectContract schemas`
- `TaskContract schema`
- `RoleContract schema`
- `AgentResult schema`
- `Contract examples`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Schema positive/negative fixtures
- Unknown field/version compatibility testi
- Forbidden tool ve missing acceptance testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Runtime provider-specific alan canonical contract'a sızmaz
- [ ] Her task owner, budget, acceptance ve allowed scope taşır
- [ ] Gap ve assumption self-declaration olarak görünürdür, pass sayılmaz
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

Uyumsuz contract reddedilir; adapter eski contract sürümünü açık converter ile destekler.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
