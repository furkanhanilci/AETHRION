# WP-080 — Claim–Citation Entailment, Scope ve Locator Audit

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-080` |
| Workstream | `08_EVIDENCE_ASSURANCE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Citation Audit Lead |
| Bağımsız doğrulayıcı | Independent Methodologist / Human Reviewer |
| Hard dependencies | WP-007, WP-018, WP-072, WP-075, WP-076, WP-077, WP-078, WP-079 |
| İlgili gate | G6,G9 |
| İlgili kontroller | CTL-EPI-01 |
| İlgili ACC senaryoları | ACC-30 |

## Amaç ve beklenen sonuç

Her material cümlenin bağlı evidence span'i iddiayı gerçekten destekliyor mu, kapsamı uygun mu ve contradiction var mı yapılandırılmış audit ile doğrulanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-007 — IndependenceProfile ve Separation-of-Duties Politikası](../01_GOVERNANCE/WP-007_independence_profili.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-072 — LiteratureSetManifest Freeze ve İnsan-Okunur Arşiv](../07_LITERATURE_KNOWLEDGE/WP-072_literature_manifest_freeze.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/WP-075_claim_evidence_ledger.md), [WP-076 — Evidence Span Anchoring ve Re-anchoring](../08_EVIDENCE_ASSURANCE/WP-076_evidence_anchor_resolver.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/WP-077_claim_state_dependency.md), [WP-078 — Yapılandırılmış Evidence Extraction Hattı](../08_EVIDENCE_ASSURANCE/WP-078_evidence_extraction_pipeline.md), [WP-079 — SourceTrustCard ve Çalışma Kalitesi Değerlendirmesi](../08_EVIDENCE_ASSURANCE/WP-079_source_trust_cards.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-080-T01 | Claim–evidence relationship rubric yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-080-T02 | Locator integrity ve quote/fingerprint mekanik kontrol ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-080-T03 | Entailment/scope/hedging/secondary-citation review graph kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-080-T04 | Counter-evidence ve citation laundering checks ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-080-T05 | Risk bazlı human sampling/full audit uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-080-T06 | CitationAudit verdict ve G9 blocker entegrasyonu yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Citation audit service`
- `Audit rubric`
- `Mechanical locator checker`
- `Audit report/scorecard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Correct support pass
- Citation only related not support
- Overgeneralized scope fail
- Secondary citation laundering
- Missing locator G9 fail
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Citation varlığı destek kanıtı değildir
- [ ] Critical claim locator/entailment coverage %100
- [ ] Reviewer verdict evidence span ve gerekçe taşır
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

Failed audit claim/report'u revise eder; source veya eski evidence overwrite edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
