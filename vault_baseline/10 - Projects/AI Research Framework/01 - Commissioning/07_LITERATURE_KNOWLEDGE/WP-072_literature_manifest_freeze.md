# WP-072 — LiteratureSetManifest Freeze ve İnsan-Okunur Archive

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-072` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Lead |
| Bağımsız doğrulayıcı | Citation Auditor / Archivist |
| Hard dependencies | WP-014, WP-017, WP-026, WP-061, WP-062, WP-063, WP-067, WP-069, WP-070, WP-071 |
| İlgili gate | G3,G9,G10 |
| İlgili kontroller | CTL-EPI-01, CTL-LIT-01 |
| İlgili ACC senaryoları | ACC-01, ACC-02, ACC-04, ACC-30 |

## Amaç ve beklenen sonuç

Dahil/hariç kaynaklar, representation hash'leri, sorgular, screening kararları, status ve actor'larla immutable LiteratureSetManifest olur; Zotero 90_Frozen_View yalnız aynasıdır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-067 — Zotero Çift Yönlü Sync ve Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-069 — SearchProtocol ve LiteratureCampaign Orkestrasyonu](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — İnsan + Agent Çift Yönlü Literatür Keşfi](../07_LITERATURE_KNOWLEDGE/WP-070_cift_yonlu_literatur.md), [WP-071 — Screening, Inclusion/Exclusion ve Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-072-T01 | Manifest snapshot query ve deterministic serializer yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-072-T02 | Included/excluded/query/screening/status/license refs ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-072-T03 | Hash/signature ve object-lock write uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-072-T04 | CSL-JSON/BibTeX/RIS taşınabilir export üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-072-T05 | Zotero 90_Frozen_View selective sync yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-072-T06 | Manifest diff/new-version ve synthesis invalidation kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `LiteratureSetManifest`
- `Signed frozen package`
- `Portable exports`
- `Zotero frozen view`
- `Freeze/diff report`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Same input same manifest hash
- New source creates v2 not mutation
- Zotero frozen view edit manifesti değiştirmez
- Missing locator/status hard fail
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Manifest Source Registry snapshot'ıdır
- [ ] Zotero arşivi kanıtın kendisi değildir
- [ ] Eski set ve representations erişilebilir kalır
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

Eksik/yanlış manifest INVALIDATED olur ve düzeltilmiş yeni version üretilir; eski claim/run bağı korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
