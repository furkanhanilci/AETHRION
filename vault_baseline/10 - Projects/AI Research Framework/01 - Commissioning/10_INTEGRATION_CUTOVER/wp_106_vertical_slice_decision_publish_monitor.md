# WP-106 — Dikey Dilim 5 — Human Decision → Publish → Monitor

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-106` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Project Decision Owner |
| Bağımsız doğrulayıcı | Citation Auditor / Safety / Archivist |
| Hard dependencies | WP-037, WP-074, WP-077, WP-080, WP-085, WP-089, WP-090, WP-093, WP-095, WP-099, WP-105 |
| İlgili gate | G8,G9,G10 |
| İlgili kontroller | CTL-GOV-01, CTL-EPI-01, CTL-LIT-02 |
| İlgili ACC senaryoları | ACC-04, ACC-25, ACC-30, ACC-31, ACC-36, ACC-40 |

## Amaç ve beklenen sonuç

Residual risk ve dissent ile human G8 kararı verilir; imzalı G9 package yayınlanır ve G10 retraction/supersession impact akışı çalışır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-037 — G10 Temporal Schedule ve Kısa ImpactScan](../04_CONTROL_EVENT/wp_037_g10_impactscan.md), [WP-074 — Obsidian Projection, Link Integrity ve Knowledge Write-Back](../07_LITERATURE_KNOWLEDGE/wp_074_obsidian_projection_sync.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-080 — Claim–Citation Entailment, Scope ve Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-085 — Repeatability, Reproducibility, Robustness ve Replication Hattı](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate ve Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-093 — Human Decision Queue ve Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/wp_093_decision_queue_ui.md), [WP-095 — Claim/Evidence Explorer ve Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-105 — Dikey Dilim 4 — Blind Review → Arbitration → Clean-Room](../10_INTEGRATION_CUTOVER/wp_105_vertical_slice_review_repro.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-106-T01 | Evidence-delta/decision rationale ve MFA update çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-106-T02 | Publication completeness/license/privacy checks yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-106-T03 | RO-Crate/signature/archive ve release event üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-106-T04 | Retraction/correction/model drift trigger et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-106-T05 | ImpactCase, claim challenge, owner queue ve superseding package oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-106-T06 | Audit export'ta tüm chain'i doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Decision/publish/monitor dossier`
- `DecisionRecord`
- `PublicationPackage`
- `ImpactCase/Supersession`
- `Audit export`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Missing locator G9 fail
- Forged decision deny
- Retraction impact
- Superseded publication old link
- Full chain audit
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Release yalnız named human decision ile olur
- [ ] Old publication erişilebilir ve superseded görünür
- [ ] G10 claim'i sessiz mutate etmez
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

Release öncesi rollback draft'ı invalidate eder; release sonrası yalnız superseding publication ve impact workflow uygulanır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
