# WP-116 — Resilience, Chaos ve Failure-Injection Commissioning

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-116` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Platform Assurance / Service Owners |
| Hard dependencies | WP-040, WP-060, WP-101, WP-111, WP-114, WP-115 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-OPS-01, CTL-OPS-02, CTL-OPS-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Worker, provider, DB, NATS, node, object store, policy, identity ve network arızaları altında fail-closed, recovery, alert ve data integrity davranışı doğrulanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-040 — Workflow Replay, Versioning ve Failure Test Suite](../04_CONTROL_EVENT/WP-040_workflow_replay_failure_suite.md), [WP-060 — Agentic Security Attack Suite ve Red-Team Kabulü](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-111 — Reliability, Event ve FinOps Kabul Paketi](../10_INTEGRATION_CUTOVER/WP-111_reliability_finops_acceptance.md), [WP-114 — Operations, DR ve Restore Kabul Paketi](../10_INTEGRATION_CUTOVER/WP-114_operations_dr_acceptance.md), [WP-115 — Tam Sistem Regression ve Commissioning Dossier](../10_INTEGRATION_CUTOVER/WP-115_full_system_regression.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-116-T01 | Failure model ve blast-radius guard yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-116-T02 | Service/node/provider/network/credential fault injection çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-116-T03 | Retry/circuit breaker/idempotency/compensation gözle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-116-T04 | SLO alert/on-call/runbook tepkisini ölç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-116-T05 | Post-recovery canonical integrity ve queue drain doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-116-T06 | Chaos findings ve steady-state scorecard üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Chaos test suite/results`
- `Steady-state hypotheses`
- `Recovery/integrity report`
- `Resilience sign-off`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Worker/provider/DB/NATS/node/network/Vault/policy faults
- Cascading retry/cost control
- Recovery without duplicate effect
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Critical steady-state invariant'ları korunur
- [ ] Fault blast radius sınır içindedir
- [ ] Alarm/runbook/owner SLA'sı çalışır
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

Beklenmeyen blast radius'ta experiment kill switch; environment restore ve incident review olmadan devam edilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
