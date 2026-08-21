# WP-105 — Dikey Dilim 4 — Blind Review → Arbitration → Clean-Room

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-105` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Assurance Lead |
| Bağımsız doğrulayıcı | Independent Reproducibility Lead / Decision Owner |
| Hard dependencies | WP-084, WP-085, WP-086, WP-087, WP-088, WP-089, WP-093, WP-095, WP-104 |
| İlgili gate | G6,G7 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-03, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-06, ACC-07, ACC-08, ACC-19, ACC-20, ACC-38 |

## Amaç ve beklenen sonuç

Frozen claim/run paketi bağımsız, kör, gerektiğinde cross-family review; disagreement arbitration ve clean-room reproduction sonrası G6/G7'yi geçer veya kontrollü geri döner.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-084 — Clean-Room Reproduction Ortamı](../08_EVIDENCE_ASSURANCE/WP-084_clean_room_environment.md), [WP-085 — Repeatability, Reproducibility, Robustness ve Replication Hattı](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-086 — Frozen ve Kör Review Package Builder](../08_EVIDENCE_ASSURANCE/WP-086_frozen_review_package.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family ve Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-093 — Human Decision Queue ve Evidence-Delta UI](../09_EXPERIENCE_OBSERVABILITY/WP-093_decision_queue_ui.md), [WP-095 — Claim/Evidence Explorer ve Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/WP-095_claim_evidence_explorer.md), [WP-104 — Dikey Dilim 3 — Baseline → Run → Claim/Evidence](../10_INTEGRATION_CUTOVER/WP-104_dikey_dilim_run_claim.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-105-T01 | Independence-eligible reviewer/reproducer ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-105-T02 | Frozen/blind package üret ve dispatch et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-105-T03 | Mechanical, method, adversarial/cross-family review çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-105-T04 | Conflicting verdict ve strong counter-test arbitration yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-105-T05 | Clean-room repeatability/repro/robustness koş | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-105-T06 | Pass/fail root cause ve G4/G5 reopen davranışını doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Review/repro vertical dossier`
- `ReviewRecords/DisagreementCase`
- `ReproductionReport`
- `Gate histories`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Self-review deny
- Order bias
- Strong deterministic counter-test
- Clean-room pass/fail
- Reviewer unavailable BLOCKED
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] R3 gerekli independence tüm boyutlarda sağlanır
- [ ] Oy çokluğu failed evidence'i geçemez
- [ ] G7 fail history silmeden claim'i CHALLENGED yapar
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

Contaminated review/repro invalidate edilir; yeni assignment/environment ile tekrar edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
