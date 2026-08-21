# WP-091 — Lab Cockpit Bilgi Mimarisi ve Uygulama Kabuğu

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-091` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Product/Experience Lead |
| Bağımsız doğrulayıcı | Accessibility Reviewer / Governance |
| Hard dependencies | WP-002, WP-012, WP-013, WP-020, WP-025, WP-030, WP-032, WP-033, WP-055 |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-GOV-01, CTL-OBS-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

İnsan; portfolio, proje, gate, task, evidence, review, decision, cost ve incident durumunu tek korelasyonla gören, fakat canonical state'i kopyalamayan güvenli cockpit'e sahip olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği](../01_GOVERNANCE/WP-002_kapsam_nfr_izlenebilirlik.md), [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/WP-012_canonical_field_authority.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-025 — PostgreSQL HA ve Registry Veri Temeli](../03_FOUNDATION/WP-025_postgres_ha_temeli.md), [WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models](../03_FOUNDATION/WP-030_derived_read_models.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service ve GateRecord Değerlendirmesi](../04_CONTROL_EVENT/WP-033_gate_service_records.md), [WP-055 — SPIFFE/SPIRE Workload Identity ve Vault](../06_EXECUTION_SECURITY/WP-055_spiffe_vault_identity.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-091-T01 | Persona/task ve bilgi mimarisini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-091-T02 | OIDC/MFA/RBAC ve session güvenliğini bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-091-T03 | Project/gate timeline shell ve deep-link standardı kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-091-T04 | Canonical API aggregation/read-model BFF yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-091-T05 | State freshness/projection lag göstergesi ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-091-T06 | Accessibility/i18n/error/empty/loading patterns uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Cockpit application shell`
- `Navigation/IA`
- `BFF/read APIs`
- `RBAC matrix`
- `Accessibility baseline`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Role-based view/access negative test
- Stale projection banner
- Keyboard/screen-reader flows
- Canonical link deep navigation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] UI gate state sahibi değildir
- [ ] Kritik karar kanıt özeti ve freshness gösterir
- [ ] Yetkisiz D2+ field browser'a dönmez
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

UI release feature flag/canary ile geri alınır; canonical workflow etkilenmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
