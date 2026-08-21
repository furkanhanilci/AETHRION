# WP-111 — Reliability, Event ve FinOps Kabul Paketi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-111` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | FinOps / Control Plane Reviewer |
| Hard dependencies | WP-040, WP-053, WP-083, WP-100, WP-109 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-OPS-01, CTL-OPS-02, CTL-CST-01, CTL-CST-02 |
| İlgili ACC senaryoları | ACC-09..14, ACC-29, ACC-33..35 |

## Amaç ve beklenen sonuç

Budget, provider, event, worker, workflow deploy, preemption, DLQ, partial tool failure ve invoice variance senaryoları state/effect integrity ile kapanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-040 — Workflow Replay, Versioning ve Failure Test Suite](../04_CONTROL_EVENT/wp_040_workflow_replay_failure_suite.md), [WP-053 — Kueue Queue, Kota ve Öncelik Politikası](../06_EXECUTION_SECURITY/wp_053_kueue_quota.md), [WP-083 — ExperimentBatch ve Staged Execution](../08_EVIDENCE_ASSURANCE/wp_083_experiment_batch.md), [WP-100 — Cost Ledger, Bütçe Zarfları ve FinOps](../09_EXPERIENCE_OBSERVABILITY/wp_100_cost_ledger_finops.md), [WP-109 — Kırk Acceptance Senaryosu Registry ve Harness](../10_INTEGRATION_CUTOVER/wp_109_acceptance_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-111-T01 | ACC-09–14 ve ACC-29/33/34/35 fixture'larını çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-111-T02 | Budget/provider/worker/event/queue fault injection yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-111-T03 | State RPO, duplicate effect, DLQ ve cost ledger assertions doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-111-T04 | Runbook ve alert tepkisini ölç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-111-T05 | Reliability/FinOps dossier ve sign-off üret | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Reliability/FinOps scenario results`
- `Fault injection report`
- `SLO/cost evidence`
- `Owner sign-off`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-09,10,11,12,13,14,29,33,34,35
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Bütün critical senaryolar PASS
- [ ] RPO=0 workflow state
- [ ] Duplicate external effect=0
- [ ] Hard budget ve invoice reconciliation doğru
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

Failure cutover'ı bloklar; workload/provider/consumer config önceki release'e döner ve regression yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
