# WP-027 — Git, OCI Registry ve Build Provenance Temeli

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-027` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Supply Chain Security Lead |
| Bağımsız doğrulayıcı | Security Reviewer / SRE |
| Hard dependencies | WP-021, WP-022, WP-024, WP-026 |
| İlgili gate | G5,Platform |
| İlgili kontroller | CTL-SEC-05, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-17 |

## Amaç ve beklenen sonuç

Kaynak commit'ten digest-pinned OCI image'a kadar SBOM, provenance, imza, vulnerability ve promotion zinciri kurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/wp_021_environment_account_network_baseline.md), [WP-022 — Repository Topolojisi ve Kod Sahipliği](../03_FOUNDATION/wp_022_repository_topology.md), [WP-024 — CI Temeli ve Deterministik Kalite Kapıları](../03_FOUNDATION/wp_024_ci_quality_gates.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-027-T01 | OCI registry environment/repository yapısını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-027-T02 | Reproducible build ve provenance metadata üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-027-T03 | SBOM ve vulnerability scan ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-027-T04 | Sigstore keyless/key policy'sini bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-027-T05 | Mutable tag kullanımını yasakla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-027-T06 | Dev→staging→prod digest promotion akışını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `OCI registry`
- `Build/promotion pipeline`
- `SBOM/provenance artifacts`
- `Signature policy seed`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Unsigned image negative promotion
- Mutable tag admission fixture
- Aynı commit reproducible build karşılaştırması
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Production yalnız imzalı digest çalıştırır
- [ ] Build artifact source commit ve dependency lock'a bağlıdır
- [ ] Critical vulnerability policy kararı olmadan promote olmaz
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

Compromised digest revoke/quarantine edilir; önceki imzalı image'a rollback ve impact scan yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
