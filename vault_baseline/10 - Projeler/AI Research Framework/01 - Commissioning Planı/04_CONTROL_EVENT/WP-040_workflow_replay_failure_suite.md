# WP-040 — Workflow Replay, Versioning ve Failure Test Suite

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-040` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Platform Assurance Lead |
| Bağımsız doğrulayıcı | Independent SRE / Control Plane Reviewer |
| Hard dependencies | WP-024, WP-031, WP-032, WP-033, WP-034, WP-035, WP-036, WP-037, WP-038, WP-039 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-OPS-01, CTL-OPS-02 |
| İlgili ACC senaryoları | ACC-10, ACC-11, ACC-13, ACC-14, ACC-35 |

## Amaç ve beklenen sonuç

Açık workflow geçmişleri kod deploy'u, worker/provider/DB kaybı, retry, timeout ve compensation altında state kaybetmeden çalışır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-024 — CI Temeli ve Deterministik Kalite Kapıları](../03_FOUNDATION/WP-024_ci_kalite_kapilari.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-033 — Gate Service ve GateRecord Değerlendirmesi](../04_CONTROL_EVENT/WP-033_gate_service_records.md), [WP-034 — G0 Intake ve G1 Charter Workflow'ları](../04_CONTROL_EVENT/WP-034_g0_g1_workflows.md), [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-036 — G5 Execute–G9 Publish Workflow'ları](../04_CONTROL_EVENT/WP-036_g5_g9_workflows.md), [WP-037 — G10 Temporal Schedule ve Kısa ImpactScan](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-038 — Human Update, Cancellation ve Compensation Semantiği](../04_CONTROL_EVENT/WP-038_human_updates_compensation.md), [WP-039 — Event Consumer, DLQ ve Güvenli Replay Çerçevesi](../04_CONTROL_EVENT/WP-039_event_consumer_dlq_replay.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-040-T01 | Golden event histories oluştur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-040-T02 | Her workflow build için deterministic replay CI ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-040-T03 | Worker kill/activity timeout fault injection yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-040-T04 | DB/NATS/provider outage senaryolarını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-040-T05 | Patch/version marker ve Continue-as-New testlerini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-040-T06 | State/artifact/integrity karşılaştırma raporu üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Replay test suite`
- `Golden histories`
- `Fault-injection harness`
- `Workflow compatibility report`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Açık history yeni kodla replay
- Worker crash mid-activity
- Provider timeout/fallback yoksa BLOCKED
- NATS/DB kesinti recovery
- Compensation partial fail
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Critical replay testlerinin %100'ü geçer
- [ ] State RPO=0 korunur
- [ ] Failure hiçbir unsafe route veya duplicate effect üretmez
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

Replay fail eden worker build promote edilmez; önceki compatible worker version açık workflow'ları işlemeye devam eder.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
