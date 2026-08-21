# WP-113 — Evidence, Reproduction ve Publication Kabul Paketi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-113` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Assurance Lead |
| Bağımsız doğrulayıcı | Independent Reproducer / Citation Auditor |
| Hard dependencies | WP-085, WP-087, WP-088, WP-089, WP-090, WP-109 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-EPI-01, CTL-EPI-03, CTL-OPS-03 |
| İlgili ACC senaryoları | ACC-19..23, ACC-30, ACC-31, ACC-38, ACC-39 |

## Amaç ve beklenen sonuç

Clean-room pass/fail, graph rebuild, human note, artifact overwrite, publication completeness, supersession, reviewer availability ve negative result senaryoları epistemik invariant'larla kapanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-085 — Repeatability, Reproducibility, Robustness ve Replication Hattı](../08_EVIDENCE_ASSURANCE/WP-085_repro_robustness_replication.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family ve Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/WP-089_disagreement_arbitration.md), [WP-090 — PublicationPackage, RO-Crate ve Provenance Export](../08_EVIDENCE_ASSURANCE/WP-090_publication_package.md), [WP-109 — Kırk Acceptance Senaryosu Registry ve Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-113-T01 | ACC-19–23/30/31/38/39 fixture'larını koş | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-113-T02 | Claim/manifest/anchor/repro tolerans assertions doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-113-T03 | Graph/Obsidian derived rebuild ve human preservation yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-113-T04 | Publication/supersession audit et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-113-T05 | Reviewer capacity BLOCKED ve negative-result stop/pivot doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-113-T06 | Assurance dossier/sign-off üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Evidence/repro scenario results`
- `Reproduction certificates`
- `Lineage/integrity reports`
- `Assurance sign-off`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-19,20,21,22,23,30,31,38,39
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Critical claim lineage coverage %100
- [ ] Clean-room policy karşılanır
- [ ] Açık critical/high assurance finding yok
- [ ] Negative result korunur
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

Failure publish/cutover'ı bloklar; claim status CHALLENGED/PROVISIONAL kalır ve correction/repro planlanır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
