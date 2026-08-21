# WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-014` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Data Platform Lead |
| Bağımsız doğrulayıcı | Reproducibility Engineer |
| Hard dependencies | WP-011, WP-012 |
| İlgili gate | G3–G9 |
| İlgili kontroller | CTL-DAT-01, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-23 |

## Amaç ve beklenen sonuç

Kod, veri, ortam, doküman ve yayın artifact'ları content hash, lineage, retention, license ve validity durumuyla immutable olarak tanımlanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/wp_012_canonical_field_authority.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-014-T01 | ArtifactRecord ve ContentAddress şemasını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-014-T02 | DatasetManifest split/lineage/license alanlarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-014-T03 | Environment/OCI/SBOM referanslarını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-014-T04 | Overwrite yerine new-version/INVALIDATED semantiğini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-014-T05 | Object-lock, retention ve legal-hold metadata'sını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `ArtifactRecord schema`
- `DatasetManifest schema`
- `Environment reference schema`
- `Immutability lifecycle`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Aynı URI farklı bytes overwrite negatif testi
- Hash verify ve lineage traversal testi
- Invalidated artifact geçmiş referans testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Artifact bytes hash olmadan kabul edilmez
- [ ] Mutation yeni version üretir
- [ ] License/retention eksikse external use BLOCKED olur
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

Bozuk object yeni key'e restore edilir ve eski kayıt INVALIDATED işaretlenir; hash geçmişi korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
