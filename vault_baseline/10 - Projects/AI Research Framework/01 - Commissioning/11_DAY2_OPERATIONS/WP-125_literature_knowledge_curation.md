# WP-125 — Literatür, Zotero ve Obsidian Kürasyon Ritmi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-125` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Lead |
| Bağımsız doğrulayıcı | Citation Auditor / Knowledge Curator |
| Hard dependencies | WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-073, WP-074, WP-121 |
| İlgili gate | G3,G10,Day-2 |
| İlgili kontroller | CTL-LIT-01, CTL-LIT-02, CTL-LIT-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Sync conflict, candidate aging, screening backlog, broken link, source status, annotation promotion ve human/generated zone kalite işleri tanımlı SLA ile sürekli yönetilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-064 — Zotero Kütüphane, Koleksiyon ve Yetki Modeli](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_kutuphane_yetki.md), [WP-065 — Kişisel Zotero Seed Ingest Hattı](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate ve Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md), [WP-067 — Zotero Çift Yönlü Sync ve Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Hattı](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol ve LiteratureCampaign Orkestrasyonu](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — İnsan + Agent Çift Yönlü Literatür Keşfi](../07_LITERATURE_KNOWLEDGE/WP-070_cift_yonlu_literatur.md), [WP-071 — Screening, Inclusion/Exclusion ve Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze ve İnsan-Okunur Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-073 — Obsidian Vault, Human/Generated Zones ve Şablonlar](../07_LITERATURE_KNOWLEDGE/WP-073_obsidian_vault_modeli.md), [WP-074 — Obsidian Projection, Link Integrity ve Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/WP-074_obsidian_projection_sync.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilizasyon.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-125-T01 | Daily sync/conflict/lag ve weekly curator queue review yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-125-T02 | Candidate TTL/Used promotion/duplicate metrics izle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-125-T03 | Monthly status/retraction and broken-link scan çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-125-T04 | Obsidian human/generated diff ve projection integrity kontrol et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-125-T05 | Quarterly library/group/permission/license review yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Curation calendar`
- `Queue/SLA reports`
- `Library quality scorecard`
- `Knowledge integrity report`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Full resync sample
- Human note preservation
- Broken locator/link repair
- Retraction impact sampling
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Conflict SLA ve owner bellidir
- [ ] Library item sayısı başarı metriği değildir
- [ ] Used source identity/locator/status coverage %100 hedeflenir
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

Sync veya projection sorununda connector/renderer durdurulur; personal/human data overwrite edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
