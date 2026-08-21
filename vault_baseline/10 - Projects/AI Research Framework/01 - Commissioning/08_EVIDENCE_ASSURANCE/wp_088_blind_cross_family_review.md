# WP-088 — Blind, Cross-Family ve Adversarial Review

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-088` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Assurance Lead |
| Bağımsız doğrulayıcı | Independent Human Reviewer / Eval Office |
| Hard dependencies | WP-007, WP-018, WP-042, WP-043, WP-044, WP-045, WP-047, WP-077, WP-086, WP-087 |
| İlgili gate | G6 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-06, ACC-07, ACC-08, ACC-38 |

## Amaç ve beklenen sonuç

Risk ve review rubric'ine göre bağımsız method/claim/code/security/adversarial reviewer'lar frozen paketi inceler; verdict finding ve claim referansıyla gelir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/wp_007_independence_profile.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-042 — Capability Registry ve Profil Yaşam Döngüsü](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-043 — Rol Bazlı Model Eval ve Golden Set Yönetimi](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md), [WP-044 — Model Qualification ve Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/wp_045_policy_router_budget.md), [WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi](../05_MODEL_AGENT_TOOL/wp_047_role_bundle_registry.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-086 — Frozen ve Kör Review Package Builder](../08_EVIDENCE_ASSURANCE/wp_086_frozen_review_package.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/wp_087_mechanical_verifier.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-088-T01 | Review role/rubric/assignment service kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-088-T02 | IndependenceProfile eligibility check bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-088-T03 | Blind package dispatch ve sealed response uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-088-T04 | Cross-family/order-randomized parallel review yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-088-T05 | Adversarial counterexample/falsification task'ı bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-088-T06 | Verdict/finding aggregation ve calibration telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Review service`
- `Assignment/eligibility engine`
- `Review rubrics`
- `ReviewRecord storage`
- `Calibration dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Self-review assignment deny
- R3 cross-family/human separation
- Order-swap bias detection
- Critical counter-test beats PASS majority
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Oy çokluğu acceptance değildir
- [ ] Her finding target locator ve severity taşır
- [ ] Bağımsızlık sağlanamazsa BLOCKED olur
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

Contaminated/biased review invalidate edilir; yeni assignment ve corrected frozen package açılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
