# WP-118 — Operasyonel Hazırlık, On-Call ve Runbook Simulation

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-118` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | SRE Lead |
| Bağımsız doğrulayıcı | Internal Audit / Service Owners |
| Hard dependencies | WP-099, WP-101, WP-114, WP-115, WP-116, WP-117 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-OPS-03, CTL-GOV-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Service owner, on-call, escalation, incident command, break-glass, backup/restore, reconciliation, security ve business continuity runbook'ları staging'de uygulanmış olur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/wp_099_audit_worm_export.md), [WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama](../09_EXPERIENCE_OBSERVABILITY/wp_101_service_slo_alerting.md), [WP-114 — Operations, DR ve Restore Kabul Paketi](../10_INTEGRATION_CUTOVER/wp_114_operations_dr_acceptance.md), [WP-115 — Tam Sistem Regression ve Commissioning Dossier](../10_INTEGRATION_CUTOVER/wp_115_full_system_regression.md), [WP-116 — Resilience, Chaos ve Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/wp_116_resilience_chaos.md), [WP-117 — Performans, Kapasite ve Yük Commissioning](../10_INTEGRATION_CUTOVER/wp_117_performance_capacity.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-118-T01 | Runbook katalog ve freshness/link check tamamla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-118-T02 | On-call rota, escalation ve paging test et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-118-T03 | Incident commander/tabletop ve live simulation yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-118-T04 | Break-glass two-person ve credential revoke dene | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-118-T05 | Zotero/tool/event/policy/model reconciliation runbook'larını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-118-T06 | Handover/training ve readiness sign-off al | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Operational Readiness Review`
- `Runbook execution records`
- `On-call simulation`
- `Training/ownership sign-offs`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- After-hours page/escalation
- Tool uncertain write reconcile
- Policy rollback
- Model revoke
- Security containment
- Restore invocation
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her critical service 24x7 owner ve runbook taşır
- [ ] Runbook yalnız okunmamış doküman değil uygulanmış kanıttır
- [ ] Break-glass audit ve revoke çalışır
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

Readiness fail cutover'ı bloklar; eksik owner/runbook çözülmeden tarih onaylanmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
