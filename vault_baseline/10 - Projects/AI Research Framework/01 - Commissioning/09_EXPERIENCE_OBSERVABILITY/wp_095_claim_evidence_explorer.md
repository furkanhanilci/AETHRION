# WP-095 — Claim/Evidence Explorer ve Provenance Graph

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-095` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Product Lead |
| Bağımsız doğrulayıcı | Citation Auditor / Accessibility Reviewer |
| Hard dependencies | WP-030, WP-075, WP-076, WP-077, WP-078, WP-079, WP-080, WP-082, WP-085, WP-087, WP-088, WP-089, WP-090, WP-091 |
| İlgili gate | G5–G10 |
| İlgili kontroller | CTL-EPI-01 |
| İlgili ACC senaryoları | ACC-04, ACC-08, ACC-21, ACC-30, ACC-31 |

## Amaç ve beklenen sonuç

Kullanıcı claim'in sürümünü, certainty/conditions, evidence spans, contradictions, source trust, run, review, reproduction, decision ve supersession zincirini inceleyebilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring ve Re-anchoring](../08_EVIDENCE_ASSURANCE/wp_076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-078 — Yapılandırılmış Evidence Extraction Hattı](../08_EVIDENCE_ASSURANCE/wp_078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard ve Çalışma Kalitesi Değerlendirmesi](../08_EVIDENCE_ASSURANCE/wp_079_source_trust_cards.md), [WP-080 — Claim–Citation Entailment, Scope ve Locator Audit](../08_EVIDENCE_ASSURANCE/wp_080_citation_entailment_audit.md), [WP-082 — Run Registry ve MLflow Lineage Entegrasyonu](../08_EVIDENCE_ASSURANCE/wp_082_run_registry_mlflow.md), [WP-085 — Repeatability, Reproducibility, Robustness ve Replication Hattı](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family ve Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate ve Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-091 — Lab Cockpit Bilgi Mimarisi ve Uygulama Kabuğu](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-095-T01 | Claim list/detail/version/diff view yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-095-T02 | Evidence span source preview ve locator state ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-095-T03 | Dependency/support/contradiction graph görselleştir | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-095-T04 | Assessment vector ve blocker explanation göster | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-095-T05 | Run/review/repro/decision timeline bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-095-T06 | Impact/supersession ve citation audit view ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Claim Explorer`
- `Evidence preview`
- `Provenance graph`
- `Assessment/blocker panels`
- `Audit drill-down`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Broken locator visible
- Contradictory evidence not hidden
- Derived graph corruption fallback query
- Critical claim lineage traversal
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Tek confidence yüzdesi sunulmaz
- [ ] Graph derived olduğu belirtilir ve canonical linkler vardır
- [ ] Material claim tam chain tek sorguyla erişilir
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

Graph UI/derived projection rollback canonical ledger'ı etkilemez; direct ledger fallback view korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
