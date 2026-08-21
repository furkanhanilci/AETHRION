# WP-126 — Reviewer, Judge ve Reproducer Kalibrasyonu

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-126` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Assurance Lead |
| Bağımsız doğrulayıcı | Eval Office / Independent Human Reviewer |
| Hard dependencies | WP-007, WP-043, WP-085, WP-086, WP-087, WP-088, WP-089, WP-113, WP-121 |
| İlgili gate | G6,G7,Day-2 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-07, ACC-08, ACC-38 |

## Amaç ve beklenen sonuç

Reviewer precision, disagreement, order/identity/verbosity bias, false positive, escaped defect ve reproducer consistency düzenli golden/counter-testlerle ölçülür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-043 — Rol Bazlı Model Eval ve Golden Set Yönetimi](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md), [WP-085 — Repeatability, Reproducibility, Robustness ve Replication Hattı](../08_EVIDENCE_ASSURANCE/wp_085_repro_robustness_replication.md), [WP-086 — Frozen ve Kör Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family ve Adversarial Review](../08_EVIDENCE_ASSURANCE/wp_088_blind_cross_family_review.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-113 — Evidence, Reproduction ve Publication Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_113_evidence_repro_acceptance.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/wp_121_hypercare_stabilization.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-126-T01 | Calibration set ve hidden counter-tests periyodik çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-126-T02 | Order swap/blind/unblind leakage audit et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-126-T03 | Validated precision/recall, disagreement ve triage time hesapla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-126-T04 | Reviewer/reproducer profile expiry/suspend kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-126-T05 | Rubric/training/bundle correction ve requalification yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Calibration reports`
- `Reviewer capability decisions`
- `Bias/quality dashboard`
- `Improvement actions`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Order bias
- Identity leak
- Strong counter-test
- False-positive reproducer
- Cross-family correlated miss
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Çok reviewer yüksek kalite varsayımı yapılmaz
- [ ] Calibration fail critical role eligibility'yi askıya alır
- [ ] Human ve model reviewer aynı evidence rubric ile ölçülür
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

Failed reviewer profile suspend edilir; açık review'lar impact/reassignment alır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
