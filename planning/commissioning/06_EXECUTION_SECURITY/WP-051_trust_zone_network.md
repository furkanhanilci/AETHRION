# WP-051 — Dört Trust Zone ve Ağ Segmentasyonu

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-051` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Security Architecture Lead |
| Bağımsız doğrulayıcı | Independent Security Reviewer / SRE |
| Hard dependencies | WP-006, WP-010, WP-021 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-SEC-01, CTL-SEC-02 |
| İlgili ACC senaryoları | ACC-05, ACC-16 |

## Amaç ve beklenen sonuç

Zone 0 governance, Zone 1 control plane, Zone 2 execution ve Zone 3 untrusted content explicit identity, default-deny network ve audited gateways ile ayrılır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-006 — ExecutionProfile ve Route Politikası](../01_GOVERNANCE/WP-006_execution_profili.md), [WP-010 — Mimari Karar ve Reddedilen Alternatifler Baseline'ı](../01_GOVERNANCE/WP-010_adr_baseline.md), [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/WP-021_ortam_hesap_ag_baseline.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-051-T01 | Zone/asset/data-flow inventory çıkar | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-051-T02 | NetworkPolicy/firewall/security group'ları IaC ile uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-051-T03 | Control↔execution ve quarantine↔parser gateway'lerini belirle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-051-T04 | Default-deny ingress/egress ve DNS policy kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-051-T05 | Admin/audit/export path'lerini ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-051-T06 | Trust-boundary threat testlerini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Trust zone diagram/data flows`
- `Network IaC`
- `Boundary policy`
- `Threat-test suite`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Zone 3→Zone 1 direct access deny
- Execution unknown egress deny
- Control DB execution credential deny
- Audit export read-only path
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Zone geçişi identity+policy+schema+audit olmadan olmaz
- [ ] Untrusted content control prompt/command kanalına geçmez
- [ ] Network drift alarmı vardır
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

Yanlış network release GitOps rollback ile geri alınır; fail-closed kesinti unsafe geçişe tercih edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
