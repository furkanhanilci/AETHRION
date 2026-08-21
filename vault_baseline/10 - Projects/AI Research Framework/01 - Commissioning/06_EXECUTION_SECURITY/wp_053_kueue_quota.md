# WP-053 — Kueue Queue, Kota ve Öncelik Politikası

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-053` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Compute Platform Lead |
| Bağımsız doğrulayıcı | FinOps / Assurance / SRE |
| Hard dependencies | WP-006, WP-052 |
| İlgili gate | G5–G7 |
| İlgili kontroller | CTL-CST-01, CTL-SEC-04 |
| İlgili ACC senaryoları | ACC-09, ACC-33 |

## Amaç ve beklenen sonuç

Araştırma scout, experiment, review, reproduction, incident ve critical assurance işleri bütçe/kota/admission ve güvenli preemption ile planlanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/wp_006_execution_profile.md), [WP-052 — Kubernetes Cluster ve Node Pool Baseline](../06_EXECUTION_SECURITY/wp_052_kubernetes_cluster.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-053-T01 | ClusterQueue/LocalQueue ve cohort modelini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-053-T02 | Project/portfolio quota ve resource flavor tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-053-T03 | PriorityClass/assurance reserve uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-053-T04 | Budget reservation ve Temporal task bağını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-053-T05 | Preemption/checkpoint/retry davranışı yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-053-T06 | Queue wait/utilization/cost telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Kueue configuration`
- `Quota/priority policy`
- `Budget admission adapter`
- `Queue dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Low-priority scout preemption
- Critical repro capacity reservation
- Quota/budget deny
- Checkpoint sonrası resume
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Preemption canonical state/artifact kaybetmez
- [ ] Assurance işleri feature fan-out ile aç bırakılmaz
- [ ] Quota bypass service account yoktur
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

Yanlış priority/quota bundle önceki sürüme döner; bekleyen workload yeniden değerlendirir, çalışan workload zorla kaybedilmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
