# WP-037 — G10 Temporal Schedule ve Kısa ImpactScan

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-037` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Knowledge Monitoring Lead |
| Bağımsız doğrulayıcı | Assurance Lead / SRE |
| Hard dependencies | WP-008, WP-015, WP-017, WP-018, WP-031, WP-032 |
| İlgili gate | G10 |
| İlgili kontroller | CTL-LIT-02, CTL-MOD-02 |
| İlgili ACC senaryoları | ACC-04, ACC-31, ACC-36 |

## Amaç ve beklenen sonuç

Retraction, source correction, model/data/policy drift ve incident sinyalleri periyodik Schedule ile kısa ömürlü ImpactScan başlatır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-018 — Claim, Evidence, Review ve Decision Şemaları](../02_CONTRACTS/WP-018_claim_review_decision_contracts.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-037-T01 | MonitoringPolicy ve schedule registry kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-037-T02 | Source/model/data/policy/incident trigger adapter'ları yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-037-T03 | Impact graph query ve affected claim/project listesi üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-037-T04 | ImpactCase priority/SLA/owner ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-037-T05 | Supersession/re-evaluation workflow dispatch et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-037-T06 | False-positive disposition ve audit ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `ImpactScan workflow`
- `Schedule registry`
- `ImpactCase service contract`
- `Supersession trigger`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Retraction→affected claim testi
- Model revoke→open task testi
- Schedule retry/idempotency
- Eski claim sessiz mutate negative test
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Uzun ömürlü tek monitoring workflow yoktur
- [ ] Her scan bounded ve idempotent'tır
- [ ] Etkilenen claim owner queue ve status değişimi alır
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

Hatalı impact sonucu yeni disposition ile kapatılır; kaynak/claim geçmişi silinmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
