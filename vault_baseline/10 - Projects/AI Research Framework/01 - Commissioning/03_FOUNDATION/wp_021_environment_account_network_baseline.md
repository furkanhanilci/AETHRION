# WP-021 — Development, Staging ve Production Ortam Baseline'ı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-021` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Platform Lead |
| Bağımsız doğrulayıcı | Security Architect / SRE |
| Hard dependencies | WP-001, WP-006, WP-010, WP-020 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-DAT-02, CTL-SEC-02 |
| İlgili ACC senaryoları | ACC-18, ACC-27 |

## Amaç ve beklenen sonuç

Hesap/subscription, region, VPC/network, DNS, encryption, admin erişimi ve environment promotion sınırları production'a hazır biçimde ayrılır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-001 — Commissioning Charter ve Program Yetkisi](../01_GOVERNANCE/wp_001_commissioning_charter.md), [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-010 — Mimari Karar ve Reddedilen Alternatifler Baseline'ı](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-021-T01 | Dev/staging/prod hesap ve trust boundary'lerini ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-021-T02 | Management/data/execution network segmentlerini tasarla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-021-T03 | Region/data residency ve encryption key modelini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-021-T04 | Admin/break-glass erişimini MFA ile sınırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-021-T05 | Environment promotion ve seed-data kuralını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-021-T06 | Baseline IaC planını review et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Environment topology`
- `Account/network IaC`
- `Access baseline`
- `Environment promotion policy`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Cross-environment access negative testi
- Encryption/key ownership kontrolü
- Production route ve break-glass tabletop
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Production credentials hiçbir alt ortamda yoktur
- [ ] D3/D4 region ve network politikası uygulanabilir
- [ ] Ortam bütünü IaC'den yeniden kurulabilir
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

IaC apply hatasında transaction kapsamına göre rollback/destroy; shared production kaynağına manuel müdahale yapılmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
