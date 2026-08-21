# WP-123 — Control Effectiveness ve Policy Regression Ritmi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-123` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Safety & Governance Owner |
| Bağımsız doğrulayıcı | Internal Audit / Red Team |
| Hard dependencies | WP-009, WP-056, WP-060, WP-112, WP-121 |
| İlgili gate | Day-2 |
| İlgili kontroller | Tüm kontroller |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Policy ve kontroller yalnız varlıklarıyla değil, düzenli negative test, attack, exception, coverage ve false-positive sonuçlarıyla etkinlik açısından ölçülür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-009 — Control Kataloğu, Exception ve Non-Waivable Blocker'lar](../01_GOVERNANCE/wp_009_control_exception_catalog.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/wp_056_opa_policy_platform.md), [WP-060 — Agentic Security Attack Suite ve Red-Team Kabulü](../06_EXECUTION_SECURITY/wp_060_security_attack_suite.md), [WP-112 — Security ve Privacy Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_112_security_privacy_acceptance.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-123-T01 | Control test calendar ve sampling rate uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-123-T02 | OPA/identity/data/tool/supply-chain negative regression çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-123-T03 | Exception expiry/usage/residual risk audit et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-123-T04 | Control coverage/gap ve false-positive review yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-123-T05 | İki material failure'da ADR/policy reopen tetikle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Control effectiveness reports`
- `Policy regression results`
- `Exception audit`
- `Control improvement backlog`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Non-waivable deny tests
- Expired exception scan
- Attack regression sample
- Decision log coverage
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Critical control effectiveness failure aynı gün incident/containment üretir
- [ ] Exception otomatik uzamaz
- [ ] Kontrol başarısı yalnız denial sayısıyla ölçülmez
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

Hatalı policy bundle rollback; etkilenen decisions/tasks impact scan alır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
