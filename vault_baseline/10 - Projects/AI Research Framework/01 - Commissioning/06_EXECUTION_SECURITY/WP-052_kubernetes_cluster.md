# WP-052 — Kubernetes Cluster ve Node Pool Baseline

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-052` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Platform Infrastructure Lead |
| Bağımsız doğrulayıcı | SRE / Security |
| Hard dependencies | WP-021, WP-027, WP-051 |
| İlgili gate | G5,Platform |
| İlgili kontroller | CTL-SEC-04, CTL-OPS-03 |
| İlgili ACC senaryoları | ACC-27, ACC-33 |

## Amaç ve beklenen sonuç

Management, service, standard execution, secure/D3+ ve untrusted compute node pool'ları HA, quota, isolation ve signed workload admission ile kurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/WP-021_ortam_hesap_ag_baseline.md), [WP-027 — Git, OCI Registry ve Build Provenance Temeli](../03_FOUNDATION/WP-027_git_oci_supply_chain.md), [WP-051 — Dört Trust Zone ve Ağ Segmentasyonu](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-052-T01 | Cluster topology/control plane HA kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-052-T02 | Node pool/taint/toleration ayrımını uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-052-T03 | Pod Security/namespace/resource quota baseline yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-052-T04 | Storage/network/ingress classes kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-052-T05 | Autoscaling/capacity reserve ve maintenance policy ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-052-T06 | Cluster backup/upgrade/restore runbook yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Kubernetes clusters`
- `Node pool catalog`
- `Namespace/security baseline`
- `Upgrade/restore runbook`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Node failure/reschedule
- Secure workload wrong node deny
- Cluster upgrade canary
- Capacity pressure test
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] D3/D4 ve untrusted workload uygun pool dışında çalışmaz
- [ ] Control plane worker pod'ları execution namespace'ten ayrıdır
- [ ] Critical assurance capacity rezerve edilir
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

Cluster/node upgrade rollback veya blue-green control plane; workload manifest ve artifacts korunur.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
