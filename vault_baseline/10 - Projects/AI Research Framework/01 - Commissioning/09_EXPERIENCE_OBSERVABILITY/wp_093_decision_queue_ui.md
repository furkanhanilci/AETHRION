# WP-093 — Human Decision Queue ve Evidence-Delta UI

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-093` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Governance Product Lead |
| Bağımsız doğrulayıcı | Project Decision Owner / Accessibility Reviewer |
| Hard dependencies | WP-004, WP-018, WP-038, WP-075, WP-077, WP-089, WP-091 |
| İlgili gate | G1,G8,G9 |
| İlgili kontroller | CTL-GOV-01, CTL-GOV-03 |
| İlgili ACC senaryoları | ACC-25, ACC-26 |

## Amaç ve beklenen sonuç

Karar sahibi; seçenek, değişen kanıt, dissent, residual risk, policy, delegation, SLA ve expiry'yi görerek imzalı accept/reject/revise/defer kararı verir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası](../01_GOVERNANCE/wp_004_human_decision_sla_delegation.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/wp_018_claim_review_decision_contracts.md), [WP-038 — Human Update, Cancellation ve Compensation Semantiği](../04_CONTROL_EVENT/wp_038_human_updates_compensation.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-089 — DisagreementCase ve Evidence-Weighted Arbitration](../08_EVIDENCE_ASSURANCE/wp_089_disagreement_arbitration.md), [WP-091 — Lab Cockpit Bilgi Mimarisi ve Uygulama Kabuğu](../09_EXPERIENCE_OBSERVABILITY/wp_091_lab_cockpit_shell.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-093-T01 | Decision inbox/filter/escalation ve ownership view yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-093-T02 | Frozen evidence snapshot/delta/dissent özetini tasarla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-093-T03 | Rationale rubric ve required field validation uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-093-T04 | Delegation scope/expiry ve non-delegable banner ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-093-T05 | MFA re-auth/sign/update idempotency bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-093-T06 | Decision history/revoke/supersede view yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Decision Queue UI`
- `Evidence-delta component`
- `Rationale forms`
- `Delegation/escalation views`
- `Decision audit export`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Forged/expired approval deny
- Duplicate submit one decision
- SLA escalation
- Non-delegable action
- Generic rationale quality rule
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Timeout otomatik onay olmaz
- [ ] Karar target/evidence/policy snapshot taşır
- [ ] Material dissent gizlenmez
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

UI error submit receipt ile reconcile edilir; uncertain decision yeniden read edilir, ikinci karar gönderilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
