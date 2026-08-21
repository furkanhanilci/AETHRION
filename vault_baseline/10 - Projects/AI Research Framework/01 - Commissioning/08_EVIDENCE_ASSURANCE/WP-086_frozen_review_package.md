# WP-086 — Frozen ve Kör Review Package Builder

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-086` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Assurance Platform Lead |
| Bağımsız doğrulayıcı | Privacy/Security / Blind Reviewer |
| Hard dependencies | WP-007, WP-014, WP-018, WP-026, WP-075, WP-077, WP-080, WP-081, WP-082 |
| İlgili gate | G6 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-06, ACC-07 |

## Amaç ve beklenen sonuç

Reviewer'a yalnız immutable target, spec/protocol, relevant evidence, verification summary ve rubric verilir; producer kimliği/modeli/trace'i ve ikna edici ara muhakeme çıkarılır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope ve Locator Audit](../08_EVIDENCE_ASSURANCE/WP-080_citation_entailment_audit.md), [WP-081 — Protocol, Analysis, Baseline ve Falsification Registry](../08_EVIDENCE_ASSURANCE/WP-081_protocol_baseline_registry.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/WP-082_run_registry_mlflow.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-086-T01 | Review package profile'larını artifact türüne göre tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-086-T02 | Frozen target/hash/manifest assembly yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-086-T03 | Producer identity/model/trace redaction ve leak detector ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-086-T04 | Context minimum/relevant excerpt selection uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-086-T05 | Package signature/access/expiry ve one-way reviewer credential kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-086-T06 | Unblinding audit ve correction delta package yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Review Package Builder`
- `Blind/redaction rules`
- `Package manifests`
- `Leak detection tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Producer metadata removed
- Target hash immutable
- Hidden identity leak fixture
- Reviewer unauthorized source access deny
- Correction delta new package
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Review frozen aynı target üzerinde yapılır
- [ ] Reviewer producer session/trace görmez
- [ ] Package değişirse review invalidate edilir
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

Leak tespitinde review INVALIDATED olur; yeni reviewer ve temiz package ile tekrar yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
