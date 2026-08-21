# WP-044 — Model Qualification ve Admission Pipeline

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-044` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Eval Office |
| Bağımsız doğrulayıcı | Admission Board / Safety / FinOps |
| Hard dependencies | WP-041, WP-042, WP-043 |
| İlgili gate | G1,G5,G10 |
| İlgili kontroller | CTL-MOD-01, CTL-MOD-02 |
| İlgili ACC senaryoları | ACC-10, ACC-36, ACC-37 |

## Amaç ve beklenen sonuç

Yeni veya değişen model profili shadow koşum, kalite, safety, data, availability ve quality-adjusted cost kanıtıyla role kabul edilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-041 — LiteLLM Model Gateway Temeli](../05_MODEL_AGENT_TOOL/wp_041_litellm_gateway.md), [WP-042 — Capability Registry ve Profil Yaşam Döngüsü](../05_MODEL_AGENT_TOOL/wp_042_capability_registry.md), [WP-043 — Rol Bazlı Model Eval ve Golden Set Yönetimi](../05_MODEL_AGENT_TOOL/wp_043_model_eval_golden_sets.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-044-T01 | Qualification request ve immutable model snapshot çözümle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-044-T02 | Role eval/safety/latency/cost batch çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-044-T03 | Baseline karşılaştırma ve incremental value hesapla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-044-T04 | Data/provider contract ve retention kontrolü yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-044-T05 | Admission Board karar workflow'u ve expiry yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-044-T06 | Regression/drift schedule ile revoke path bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Qualification pipeline`
- `Admission dossier`
- `CapabilityProfile update`
- `Regression schedule`
- `Ejection procedure`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Passing ve failing candidate fixtures
- Provider silent snapshot change
- Availability/SLO fail
- Data policy fail
- Human triage cost threshold
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Admission model popülerliğine değil role eval'e dayanır
- [ ] Expired/failed profile route edilemez
- [ ] Qualification evidence reproducible run manifest taşır
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

Başarısız admission profili SHADOW/SUSPENDED kalır; mevcut admitted profile etkilenmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
