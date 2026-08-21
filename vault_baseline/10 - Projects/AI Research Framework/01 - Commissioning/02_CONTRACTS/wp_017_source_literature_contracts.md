# WP-017 — Source Registry ve Literature Contract Şemaları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-017` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Lead |
| Bağımsız doğrulayıcı | Citation Auditor / Data Architect |
| Hard dependencies | WP-011, WP-012, WP-014 |
| İlgili gate | G3,G10 |
| İlgili kontroller | CTL-LIT-01, CTL-LIT-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Kaynak kimliği, representation, trust, search, screening, set manifest, Zotero binding ve status event şemaları canonical olarak tanımlanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md), [WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi](../02_CONTRACTS/wp_012_canonical_field_authority.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-017-T01 | SourceRecord identifiers ve merge lineage alanlarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-017-T02 | SourceRepresentation hash/format/license/locator alanlarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-017-T03 | SourceTrustCard ve RetractionStatus tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-017-T04 | SearchProtocol/ScreeningDecision/LiteratureSetManifest şemalarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-017-T05 | ZoteroBinding/SyncReceipt/AnnotationObservation şemalarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Literature schema bundle`
- `Status lifecycle`
- `Sample manifests`
- `Zotero binding contract`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- DOI/title collision fixtures
- Manifest immutability testi
- Annotation attachment-hash zorunluluk testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Zotero key canonical source ID değildir
- [ ] Manifest frozen Source Registry snapshot'ıdır
- [ ] Status ve representation sürümleri geçmiş seti değiştirmez
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

Yanlış merge split event ile düzeltilir; eski set manifestleri ve binding'ler korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
