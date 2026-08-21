# WP-076 — Evidence Span Anchoring ve Re-anchoring

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-076` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Engineering Lead |
| Bağımsız doğrulayıcı | Citation Auditor / Reproducibility Engineer |
| Hard dependencies | WP-014, WP-017, WP-018, WP-026, WP-058, WP-063, WP-068, WP-075 |
| İlgili gate | G5,G6,G10 |
| İlgili kontroller | CTL-EPI-01 |
| İlgili ACC senaryoları | ACC-04, ACC-30 |

## Amaç ve beklenen sonuç

Evidence üçlü çıpa—representation content hash, yapısal konum ve metin fingerprint—ile PDF/HTML/dataset docs üzerinde çözümlenir ve representation değişiminde açık state alır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall](../06_EXECUTION_SECURITY/WP-058_content_quarantine_firewall.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/WP-063_source_representation_status.md), [WP-068 — Zotero Annotation → EvidenceCandidate Hattı](../07_LITERATURE_KNOWLEDGE/WP-068_zotero_annotation_ingest.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-076-T01 | Format-specific locator adapters yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-076-T02 | Text/table/figure/code/data-cell span modelini uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-076-T03 | Fingerprint/fuzzy relocation ve confidence rule kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-076-T04 | RELOCATED/AMBIGUOUS/NEEDS_REANCHOR/ORPHANED state machine ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-076-T05 | Human re-anchor queue ve audit trail yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-076-T06 | Affected claim impact event üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Anchor resolver`
- `Format adapters`
- `Re-anchor queue`
- `Anchor regression corpus`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Stable PDF exact resolve
- Layout-changed PDF RELOCATED
- Ambiguous duplicate text
- Old rep available not ORPHANED
- Unavailable rep ORPHANED
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Anchor confidence tek başına claim support değildir
- [ ] State değişimi bağlı claim'i impact değerlendirmesine alır
- [ ] Eski evidence version erişilebilir kalır
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

Hatalı relocation revert edilmez; yeni AnchorResolution kaydı ve curator decision ile supersede edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
