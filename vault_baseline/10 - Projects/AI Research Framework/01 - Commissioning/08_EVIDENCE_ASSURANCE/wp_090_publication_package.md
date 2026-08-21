# WP-090 — PublicationPackage, RO-Crate ve Provenance Export

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-090` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Provenance Curator |
| Bağımsız doğrulayıcı | Citation Auditor / Safety / Archivist |
| Hard dependencies | WP-014, WP-018, WP-026, WP-072, WP-075, WP-077, WP-080, WP-081, WP-082, WP-085, WP-087, WP-088, WP-089 |
| İlgili gate | G9,G10 |
| İlgili kontroller | CTL-EPI-01, CTL-DAT-03, CTL-SUP-01 |
| İlgili ACC senaryoları | ACC-30, ACC-31, ACC-40 |

## Amaç ve beklenen sonuç

Onaylı claim, limitation, source set, protocol, run, code/data/env, review, reproduction ve DecisionRecord taşınabilir, imzalı ve supersede edilebilir yayın paketine dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/wp_014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/wp_026_object_store_worm.md), [WP-072 — LiteratureSetManifest Freeze ve İnsan-Okunur Archive](../07_LITERATURE_KNOWLEDGE/wp_072_literature_manifest_freeze.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope ve Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline ve Falsification Registry](../08_EVIDENCE_ASSURANCE/wp_081_protocol_baseline_registry.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-085 — Repeatability, Reproducibility, Robustness ve Replication Hattı](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family ve Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-090-T01 | PublicationPackage/RO-Crate profile ve manifest yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-090-T02 | Claim narrative→ledger link materializer kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-090-T03 | CSL citation/locator/audit sonuçlarını bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-090-T04 | Code/data/env/run/repro artifact referanslarını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-090-T05 | License/privacy/redaction/release checks uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-090-T06 | Signature/archive/access/supersession ve public landing metadata üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Publication builder`
- `RO-Crate profile`
- `Signed publication package`
- `Release checklist`
- `Supersession record`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Critical claim missing locator fail
- Restricted data redaction
- Package hash/signature verify
- Superseded package old link accessible
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Narrative ledger'daki certainty/limitation'ı değiştiremez
- [ ] Package complete lineage ve DecisionRecord taşır
- [ ] Eski package silinmez, supersession link alır
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

Release öncesi hata draft package'i INVALIDATED yapar; yayın sonrası düzeltme new version/supersession ve ImpactCase gerektirir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
