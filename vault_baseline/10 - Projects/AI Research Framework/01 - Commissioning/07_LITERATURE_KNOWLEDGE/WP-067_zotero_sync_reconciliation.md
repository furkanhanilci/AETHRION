# WP-067 — Zotero Çift Yönlü Sync ve Reconciliation

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-067` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Platform Lead |
| Bağımsız doğrulayıcı | Knowledge Curator / SRE |
| Hard dependencies | WP-061, WP-062, WP-064, WP-065, WP-066 |
| İlgili gate | G3,G10 |
| İlgili kontroller | CTL-LIT-01, CTL-OPS-01 |
| İlgili ACC senaryoları | ACC-03, ACC-28 |

## Amaç ve beklenen sonuç

İnsan değişikliği, agent proposal, concurrent version, deletion, duplicate ve bridge-state kaybı alan otoritesine göre otomatik veya insan kontrollü uzlaştırılır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-064 — Zotero Kütüphane, Koleksiyon ve Yetki Modeli](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_kutuphane_yetki.md), [WP-065 — Kişisel Zotero Seed Ingest Hattı](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate ve Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-067-T01 | Per-library/item version ve since checkpoint store kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-067-T02 | Field-level three-way merge sınıflarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-067-T03 | 412/deletion/permission/duplicate ConflictCase üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-067-T04 | Manual reconciliation UI/API ve curator SLA bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-067-T05 | Full resync+dedup/rebind procedure yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-067-T06 | Sync lag/error/overwrite detector telemetry kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Sync engine`
- `Reconciliation queue`
- `Full-resync runbook`
- `Conflict metrics/dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Concurrent human/agent edit
- Deleted remote item
- Bridge state loss full resync
- Cross-library duplicate
- Human note preservation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Sessiz last-write-wins yoktur
- [ ] Full resync duplicate üretmez
- [ ] Human-authoritative field hiçbir agent merge'inde ezilmez
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

Sync durdurulup checkpoints/receipts korunur; resolver+remote versions ile kontrollü rebuild yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
