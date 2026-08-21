# WP-012 — Canonical Sahiplik ve Alan Bazlı Otorite Matrisi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-012` |
| Workstream | `02_CONTRACTS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Chief Architect |
| Bağımsız doğrulayıcı | Internal Audit / Knowledge Lead |
| Hard dependencies | WP-010, WP-011 |
| İlgili gate | Platform,G3,G10 |
| İlgili kontroller | CTL-LIT-01, CTL-OPS-01 |
| İlgili ACC senaryoları | ACC-03, ACC-21, ACC-22 |

## Amaç ve beklenen sonuç

Aynı verinin birden fazla yüzeyde görünmesi durumunda system-of-record, field authority, sync yönü ve conflict davranışı kesinleşir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-010 — Mimari Karar ve Reddedilen Alternatifler Baseline'ı](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-011 — Kimlik ve Uçtan Uca Korelasyon Standardı](../02_CONTRACTS/wp_011_identity_correlation_standard.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-012-T01 | Her bounded context için canonical record'u ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-012-T02 | Source Registry–Zotero insan/agent alan otoritesini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-012-T03 | Obsidian human/generated blok otoritesini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-012-T04 | Derived graph/index rebuild kuralını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-012-T05 | Conflict, merge, tombstone ve reconciliation owner'larını ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Canonical Ownership Matrix`
- `Field Authority Table`
- `Sync direction map`
- `Conflict ownership matrix`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Çift-canonical çelişki taraması
- İnsan alanı overwrite negatif testi
- Derived view rebuild tabletop testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her field tek authority taşır
- [ ] İki yönlü sync sahiplik belirsizliği yaratmaz
- [ ] Derived veri kaybı canonical veri kaybı sayılmaz ve rebuild edilebilir
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

Conflict'te otomatik winner seçilmez; son güvenli canonical sürüm korunur ve reconciliation case açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
