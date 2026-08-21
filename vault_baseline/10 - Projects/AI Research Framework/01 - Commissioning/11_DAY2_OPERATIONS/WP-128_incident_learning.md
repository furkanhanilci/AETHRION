# WP-128 — Incident, Postmortem ve Learning Closure

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-128` |
| Workstream | `11_DAY2_OPERATIONS` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Incident Commander / SRE Lead |
| Bağımsız doğrulayıcı | Safety / Assurance / Service Owner |
| Hard dependencies | WP-037, WP-060, WP-099, WP-101, WP-116, WP-118, WP-121 |
| İlgili gate | G10,Day-2 |
| İlgili kontroller | CTL-OPS-03, CTL-MOD-02, CTL-LIT-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Security, data, reliability, cost ve epistemik incident'ler contain→recover→learn→control/eval/runbook closure yaşam döngüsünde yönetilir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-037 — G10 Temporal Schedule ve Kısa ImpactScan](../04_CONTROL_EVENT/WP-037_g10_impactscan.md), [WP-060 — Agentic Security Attack Suite ve Red-Team Kabulü](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-099 — WORM Audit Ledger ve Bağımsız Export](../09_EXPERIENCE_OBSERVABILITY/WP-099_audit_worm_export.md), [WP-101 — Service Catalog, SLO ve Alert/Runbook Bağlama](../09_EXPERIENCE_OBSERVABILITY/WP-101_service_slo_alerting.md), [WP-116 — Resilience, Chaos ve Failure-Injection Commissioning](../10_INTEGRATION_CUTOVER/WP-116_resilience_chaos.md), [WP-118 — Operasyonel Hazırlık, On-Call ve Runbook Simulation](../10_INTEGRATION_CUTOVER/WP-118_operasyonel_hazirlik.md), [WP-121 — Hypercare, Stabilizasyon ve Program Kapanışı](../10_INTEGRATION_CUTOVER/WP-121_hypercare_stabilizasyon.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-128-T01 | Severity/classification ve IncidentWorkflow işlet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-128-T02 | Containment/credential revoke/pause/communication yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-128-T03 | Forensic/audit/canonical integrity ve root-cause analizi yürüt | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-128-T04 | Blameless postmortem ve decision timeline yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-128-T05 | Action'ı WP/control/eval/runbook/ImpactCase'e bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-128-T06 | Effectiveness verify ve closure decision al | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `IncidentRecords`
- `Forensic packages`
- `Postmortems`
- `Learning/action register`
- `Closure evidence`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Security containment
- Duplicate effect/data integrity
- Epistemic escaped claim
- Action effectiveness re-test
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Material incident yalnız dokümanla kapanmaz
- [ ] Her action owner/date/evidence taşır
- [ ] Affected claim/project/model/control impact scan alır
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

Recovery yanlışsa incident yeniden açılır; evidence/postmortem versioned kalır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
