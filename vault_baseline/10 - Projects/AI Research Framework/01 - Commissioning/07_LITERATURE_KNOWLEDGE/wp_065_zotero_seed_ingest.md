# WP-065 — Kişisel Zotero Seed Ingest Hattı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-065` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Platform Lead |
| Bağımsız doğrulayıcı | Knowledge Curator / Security |
| Hard dependencies | WP-017, WP-049, WP-050, WP-061, WP-062, WP-064 |
| İlgili gate | G3 |
| İlgili kontroller | CTL-LIT-01, CTL-LIT-03 |
| İlgili ACC senaryoları | ACC-01 |

## Amaç ve beklenen sonuç

Araştırmacının kişisel Zotero'da seçtiği seed kaynaklar read-only incremental sync ile Source Registry ve proje intake kuyruğuna alınır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/wp_017_source_literature_contracts.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/wp_050_tool_connectors.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/wp_061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/wp_062_source_identity_resolver.md), [WP-064 — Zotero Kütüphane, Koleksiyon ve Yetki Modeli](../07_LITERATURE_KNOWLEDGE/wp_064_zotero_library_access.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-065-T01 | Dedicated read-only API key/OAuth kapsamını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-065-T02 | Selected collection/tag opt-in mekanizması yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-065-T03 | Version/since token incremental reader uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-065-T04 | Item/attachment/note/annotation binding'lerini normalize et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-065-T05 | Resolver/dedup ve project seed event'ine bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-065-T06 | Deletion/move/permission change davranışını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Personal seed adapter`
- `Opt-in configuration`
- `Sync state/receipts`
- `Seed ingest dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- New seed ingest
- Same seed re-read no duplicate
- Personal edit new version
- Credential write deny
- Permission revoked pause
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] AIRL tüm kişisel library'yi varsayılan ingest etmez
- [ ] Kişisel kayıt değiştirilmez
- [ ] Source Registry mapping version ve provenance taşır
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

Sync state kaybında full read+dedup yapılır; kişisel Zotero'ya hiçbir reconciliation write gönderilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
