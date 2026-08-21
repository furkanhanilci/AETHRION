# WP-089 — DisagreementCase ve Evidence-Weighted Arbitration

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-089` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Assurance Lead / Arbiter |
| Bağımsız doğrulayıcı | Project Decision Owner / Internal Audit |
| Hard dependencies | WP-004, WP-007, WP-018, WP-075, WP-077, WP-087, WP-088 |
| İlgili gate | G6,G8 |
| İlgili kontroller | CTL-GOV-02, CTL-EPI-04 |
| İlgili ACC senaryoları | ACC-08 |

## Amaç ve beklenen sonuç

Çelişen reviewer verdict'leri, producer correction itirazı ve evidence uyuşmazlığı otomatik case olur; arbiter hangi kanıtın neden ağır bastığını kaydeder.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/WP-004_insan_karar_sla_delegasyon.md), [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-087 — Mekanik Verification Engine](../08_EVIDENCE_ASSURANCE/WP-087_mechanical_verifier.md), [WP-088 — Blind, Cross-Family ve Adversarial Review](../08_EVIDENCE_ASSURANCE/WP-088_blind_cross_family_review.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-089-T01 | Conflict detection ve DisagreementCase lifecycle yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-089-T02 | Verdict/claim/evidence graph'ını case snapshot'a bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-089-T03 | Arbiter eligibility/independence check uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-089-T04 | Evidence-weighted disposition rubric ve counter-test request ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-089-T05 | Unresolved material risk'in G8'e taşınmasını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-089-T06 | Appeal/supersession/audit akışını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Disagreement service`
- `Arbitration rubric`
- `Disposition workflow`
- `Appeal/decision integration`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- PASS/REJECT conflict auto-case
- Three votes vs deterministic failing test
- Arbiter conflict-of-interest deny
- Unresolved risk G8 visible
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Çelişki sessizce ezilmez
- [ ] Çözüm oy çokluğu değil evidence gerekçesi taşır
- [ ] Non-waivable blocker arbiter ile waive edilemez
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

Hatalı disposition appeal/superseding record ile düzeltilir; eski verdict/case korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
