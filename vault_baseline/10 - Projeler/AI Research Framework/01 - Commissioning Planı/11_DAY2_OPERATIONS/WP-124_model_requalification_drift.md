# WP-124 — Model Requalification, Drift ve Ejection Ritmi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-124` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Eval Office |
| Bağımsız doğrulayıcı | Admission Board / Safety / FinOps |
| Hard dependencies | WP-042, WP-043, WP-044, WP-045, WP-108, WP-121 |
| İlgili gate | G10,Day-2 |
| İlgili kontroller | CTL-MOD-01, CTL-MOD-02 |
| İlgili ACC senaryoları | ACC-10, ACC-11, ACC-36 |

## Amaç ve beklenen sonuç

Model snapshot, provider davranışı, eval kalite, latency, cost, safety veya data contract değişimi periyodik requalification ve gerektiğinde ejection üretir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-042 — Capability Registry ve Profil Yaşam Döngüsü](../05_MODEL_AGENT_TOOL/WP-042_capability_registry.md), [WP-043 — Rol Bazlı Model Eval ve Golden Set Yönetimi](../05_MODEL_AGENT_TOOL/WP-043_model_eval_golden_sets.md), [WP-044 — Model Qualification ve Admission Pipeline](../05_MODEL_AGENT_TOOL/WP-044_model_qualification_admission.md), [WP-045 — Policy Router ve Minimum Yeterli Model Paketi](../05_MODEL_AGENT_TOOL/WP-045_policy_router_budget.md), [WP-108 — Retraction, Drift ve Supersession Dikey Dilimi](../10_INTEGRATION_CUTOVER/WP-108_retraction_drift_dikey_dilim.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilizasyon.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-124-T01 | Profile expiry calendar ve provider change monitor işlet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-124-T02 | Role regression/adversarial eval koş | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-124-T03 | Production validated precision/quality/cost drift analiz et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-124-T04 | SHADOW→admission veya admitted→suspend/eject kararını yönet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-124-T05 | Open task/run/claim impact scan ve router cache invalidate et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Requalification reports`
- `CapabilityProfile decisions`
- `Drift/ejection events`
- `ImpactCase results`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Silent snapshot change
- Quality/latency/cost drift
- Safety/data contract change
- No eligible route after ejection
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Expired profile otomatik route dışı
- [ ] Ejection geçmiş run'ı değiştirmez fakat impact üretir
- [ ] Yeni popüler model eval olmadan role girmez
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

Yanlış ejection DecisionRecord ile supersede edilebilir; tekrar admission kanıt ister.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
