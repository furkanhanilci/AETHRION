# WP-032 — ProjectLifecycle Workflow İskeleti

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-032` |
| Workstream | `04_CONTROL_EVENT` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Workflow Engineering Lead |
| Bağımsız doğrulayıcı | Control Plane Architect / Assurance |
| Hard dependencies | WP-008, WP-013, WP-015, WP-020, WP-031 |
| İlgili gate | G0–G10 |
| İlgili kontroller | CTL-OPS-02 |
| İlgili ACC senaryoları | ACC-13, ACC-14 |

## Amaç ve beklenen sonuç

Project lifecycle, gate durumları, pause/resume, versioned transition ve child/task çağrıları deterministik Temporal workflow iskeletine dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-008 — G0–G10 Gate ve Assurance Politikası](../01_GOVERNANCE/WP-008_gate_policy_g0_g10.md), [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-015 — Event Envelope, Subject ve Schema Taxonomy](../02_CONTRACTS/WP-015_event_envelope_taxonomy.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md), [WP-031 — Temporal Platform, Namespace ve HA](../04_CONTROL_EVENT/WP-031_temporal_platform.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-032-T01 | ProjectWorkflow state machine'i yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-032-T02 | G0–G10 GateRecord referanslarını bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-032-T03 | Workflow input/version ve Continue-as-New stratejisini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-032-T04 | Activity boundaries ile external I/O'yu ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-032-T05 | Pause/resume/cancel query/update API'lerini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-032-T06 | State projection event'lerini outbox'a bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `ProjectWorkflow implementation`
- `State transition table`
- `Workflow API`
- `Replay fixtures`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- G0→G10 dry-run
- Invalid transition negative test
- Continue-as-New history continuity
- Worker crash replay
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Temporal tek lifecycle otoritesidir
- [ ] Workflow kodunda ağ/clock/random side effect yoktur
- [ ] Her transition input snapshot ve policy ref taşır
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

Yeni workflow code patch/version marker ile dağıtılır; replay fail ederse deployment durur ve önceki worker build sürdürülür.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
