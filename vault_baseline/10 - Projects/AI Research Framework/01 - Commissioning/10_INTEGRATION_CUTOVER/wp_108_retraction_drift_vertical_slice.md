# WP-108 — Retraction, Drift ve Supersession Dikey Dilimi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-108` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Monitoring Lead |
| Bağımsız doğrulayıcı | Assurance / Eval Office / Decision Owner |
| Hard dependencies | WP-037, WP-042, WP-044, WP-063, WP-075, WP-077, WP-090, WP-095, WP-106 |
| İlgili gate | G10 |
| İlgili kontroller | CTL-LIT-02, CTL-MOD-02 |
| İlgili ACC senaryoları | ACC-04, ACC-31, ACC-36 |

## Amaç ve beklenen sonuç

Source retraction/correction, model snapshot revoke, dataset/policy change ve incident; etkilenen claim/run/publication/task'ları doğru owner ve yeniden değerlendirme yoluna taşır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-037 — G10 Temporal Schedule ve Kısa ImpactScan](../04_CONTROL_EVENT/wp_037_g10_impactscan.md), [WP-042 — Capability Registry ve Profil Yaşam Döngüsü](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-044 — Model Qualification ve Admission Pipeline](../05_MODEL_AGENT_TOOL/wp_044_model_qualification_admission.md), [WP-063 — Source Representation, Lisans ve Durum İzleme](../07_LITERATURE_KNOWLEDGE/wp_063_source_representation_status.md), [WP-075 — Canonical Claim/Evidence Ledger Servisi](../08_EVIDENCE_ASSURANCE/wp_075_claim_evidence_ledger.md), [WP-077 — Claim State, Dependency ve Assessment Motoru](../08_EVIDENCE_ASSURANCE/wp_077_claim_state_dependency.md), [WP-090 — PublicationPackage, RO-Crate ve Provenance Export](../08_EVIDENCE_ASSURANCE/wp_090_publication_package.md), [WP-095 — Claim/Evidence Explorer ve Provenance Graph](../09_EXPERIENCE_OBSERVABILITY/wp_095_claim_evidence_explorer.md), [WP-106 — Dikey Dilim 5 — Human Decision → Publish → Monitor](../10_INTEGRATION_CUTOVER/wp_106_vertical_slice_decision_publish_monitor.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-108-T01 | Retraction/correction/model/data/policy/incident fixtures üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-108-T02 | Schedule/event→ImpactScan ve graph query çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-108-T03 | Affected claim/task/project/publication setini karşılaştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-108-T04 | Priority/SLA/owner ve provisional/challenged state uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-108-T05 | Re-review/repro/republish veya no-impact disposition yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-108-T06 | False-positive ve duplicate trigger idempotency test et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Impact vertical dossier`
- `ImpactCase set`
- `Affected-object accuracy report`
- `Supersession/re-evaluation records`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-04/31/36
- Duplicate trigger one case
- False-positive disposition
- Open task model revoke
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Affected set recall critical fixtures için %100
- [ ] Eski object sessiz mutate edilmez
- [ ] Her material impact named owner ve deadline taşır
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

Hatalı case disposition supersede edilir; trigger ve eski status audit history'de kalır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
