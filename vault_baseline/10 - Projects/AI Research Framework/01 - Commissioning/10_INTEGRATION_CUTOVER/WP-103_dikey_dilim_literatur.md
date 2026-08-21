# WP-103 — Dikey Dilim 2 — İki Yönlü Literatür ve Set Freeze

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-103` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Lead |
| Bağımsız doğrulayıcı | Citation Auditor / Security |
| Hard dependencies | WP-035, WP-058, WP-061, WP-062, WP-063, WP-064, WP-065, WP-066, WP-067, WP-068, WP-069, WP-070, WP-071, WP-072, WP-094, WP-099 |
| İlgili gate | G3 |
| İlgili kontroller | CTL-LIT-01, CTL-LIT-03, CTL-SEC-01 |
| İlgili ACC senaryoları | ACC-01, ACC-02, ACC-03, ACC-05, ACC-28 |

## Amaç ve beklenen sonuç

Human Zotero seed ve agent keşif sonuçları Source Registry'de birleşir, screening/annotation promotion yapılır ve immutable G3 seti freeze edilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-064 — Zotero Kütüphane, Koleksiyon ve Yetki Modeli](../07_LITERATURE_KNOWLEDGE/WP-064_zotero_kutuphane_yetki.md), [WP-065 — Kişisel Zotero Seed Ingest Hattı](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-066 — Agent Candidate ve Used-Source Write-Back](../07_LITERATURE_KNOWLEDGE/WP-066_zotero_agent_writeback.md), [WP-067 — Zotero Çift Yönlü Sync ve Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md), [WP-068 — Zotero Annotation → EvidenceCandidate Hattı](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-069 — SearchProtocol ve LiteratureCampaign Orkestrasyonu](../07_LITERATURE_KNOWLEDGE/WP-069_search_protocol_campaign.md), [WP-070 — İnsan + Agent Çift Yönlü Literatür Keşfi](../07_LITERATURE_KNOWLEDGE/WP-070_cift_yonlu_literatur.md), [WP-071 — Screening, Inclusion/Exclusion ve Coverage](../07_LITERATURE_KNOWLEDGE/WP-071_screening_inclusion.md), [WP-072 — LiteratureSetManifest Freeze ve İnsan-Okunur Archive](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-094 — Literature Workbench ve Reconciliation UI](../09_EXPERIENCE_OBSERVABILITY/WP-094_literature_workbench.md), [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-103-T01 | Kişisel seed fixture'ı ingest et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-103-T02 | Agent literature campaign/snowball/counter search çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-103-T03 | Duplicate/conflict/412 ve human-field preservation test et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-103-T04 | Screening/disagreement/trust/status akışını tamamla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-103-T05 | Annotation'ı candidate→span promotion'a hazırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-103-T06 | Manifest/export/Zotero frozen view ve audit'i doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Literature vertical dossier`
- `Frozen LiteratureSetManifest`
- `Zotero SyncReceipts`
- `Coverage/screening report`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-01/02/03/05/28
- Manifest hash repeat
- Human note preservation
- Prompt-injection PDF containment
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Source IDs ve representations complete
- [ ] Zotero hiçbir canonical/human alanı sessiz ezmez
- [ ] Manifest immutable ve signed'dır
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

Test group collection/archive korunur; connector writes kapatılır ve conflicts temizlenmeden dilim kabul edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
