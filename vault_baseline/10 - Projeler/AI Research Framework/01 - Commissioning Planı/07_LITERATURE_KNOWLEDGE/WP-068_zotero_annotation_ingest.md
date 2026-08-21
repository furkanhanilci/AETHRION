# WP-068 — Zotero Annotation → EvidenceCandidate Hattı

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-068` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Intake Lead |
| Bağımsız doğrulayıcı | Citation Auditor / Knowledge Curator |
| Hard dependencies | WP-017, WP-058, WP-061, WP-063, WP-065, WP-067 |
| İlgili gate | G3,G5 |
| İlgili kontroller | CTL-EPI-01, CTL-LIT-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Zotero highlight/comment'ları doğrudan kanıt sayılmadan parent attachment, representation hash, locator ve actor ile AnnotationObservation/EvidenceCandidate olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-065 — Kişisel Zotero Seed Ingest Hattı](../07_LITERATURE_KNOWLEDGE/WP-065_zotero_seed_ingest.md), [WP-067 — Zotero Çift Yönlü Sync ve Reconciliation](../07_LITERATURE_KNOWLEDGE/WP-067_zotero_sync_reconciliation.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-068-T01 | Annotation item incremental reader yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-068-T02 | Parent attachment→SourceRepresentation mapping yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-068-T03 | Text/comment/color/page/position/author/version alanlarını normalize et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-068-T04 | Attachment hash/locator resolution ve mismatch state'i uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-068-T05 | EvidenceCandidate promotion queue ve duplicate logic ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-068-T06 | Deleted/edited annotation impact davranışını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Annotation ingest service`
- `AnnotationObservation records`
- `EvidenceCandidate queue`
- `Promotion/disposition UI contract`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Highlight correct attachment promotion
- Mismatched PDF NEEDS_REANCHOR
- Edited/deleted annotation version
- Duplicate note/annotation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Annotation otomatik EvidenceSpan veya VERIFIED claim olmaz
- [ ] Attachment representation hash olmadan promotion yoktur
- [ ] İnsan yorumu ayrı alan ve provenance taşır
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

Yanlış mapping INVALIDATED candidate yapar; canonical Zotero annotation'a geri yazılmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
