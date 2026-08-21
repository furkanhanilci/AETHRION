# WP-098 — Grafana ve Altı Operasyon Grafiği

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-098` |
| Workstream | `09_EXPERIENCE_OBSERVABILITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Observability Lead |
| Bağımsız doğrulayıcı | Service Owners / FinOps / Assurance |
| Hard dependencies | WP-030, WP-096, WP-097 |
| İlgili gate | G0–G10,Platform |
| İlgili kontroller | CTL-OBS-01, CTL-OBS-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Execution, workflow, experiment, knowledge/evidence, service/SLO ve cost grafiklerinin korelasyonlu dashboard ve alert seti oluşur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-030 — Neo4j, pgvector ve OpenSearch Derived Read Models](../03_FOUNDATION/wp_030_derived_read_models.md), [WP-096 — OpenTelemetry Uçtan Uca Correlation Spine](../09_EXPERIENCE_OBSERVABILITY/wp_096_otel_correlation.md), [WP-097 — Langfuse Model/Agent Trace ve Prompt Governance](../09_EXPERIENCE_OBSERVABILITY/wp_097_langfuse_llm_trace.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-098-T01 | Metric/log/trace stores ve Grafana RBAC kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-098-T02 | Workflow/gate latency/blocker dashboard yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-098-T03 | Execution queue/sandbox/tool dashboard yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-098-T04 | Experiment/repro/eval quality dashboard yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-098-T05 | Literature/claim/impact integrity dashboard yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-098-T06 | Service/SLO/incident ve cost/budget dashboard yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-098-T07 | Alert routing, owner ve runbook linklerini ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Grafana platform`
- `Six graph dashboards`
- `Alert rules`
- `Dashboard/alert ownership catalog`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Synthetic SLO breach alert
- Budget 80/100 events
- Projection lag
- G6/G7 backlog
- Security deny/egress event
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her alert named owner ve runbook taşır
- [ ] Dashboard vanity metric yerine decision/action destekler
- [ ] Sensitive labels/logs redacted'dır
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

Hatalı alert/dashboard config GitOps rollback; alert suppression süreli, owner'lı ve auditlidir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
