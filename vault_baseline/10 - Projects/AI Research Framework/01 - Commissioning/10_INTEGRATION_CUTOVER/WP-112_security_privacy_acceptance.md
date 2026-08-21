# WP-112 — Security ve Privacy Kabul Paketi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-112` |
| Workstream | `10_INTEGRATION_CUTOVER` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Safety & Governance Owner |
| Bağımsız doğrulayıcı | Independent Red Team / Privacy Reviewer |
| Hard dependencies | WP-060, WP-109 |
| İlgili gate | Commissioning |
| İlgili kontroller | CTL-SEC-01..05, CTL-OBS-02 |
| İlgili ACC senaryoları | ACC-15..18, ACC-24..26, ACC-32, ACC-37, ACC-40 |

## Amaç ve beklenen sonuç

Sandbox escape, egress exfiltration, unsigned image, D3 route, policy rollback/expiry, forged approval, secret trace, eval contamination ve audit tampering fail-closed kapanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-060 — Agentic Security Attack Suite ve Red-Team Kabulü](../06_EXECUTION_SECURITY/WP-060_security_attack_suite.md), [WP-109 — Kırk Acceptance Senaryosu Registry ve Harness](../10_INTEGRATION_CUTOVER/WP-109_acceptance_registry.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-112-T01 | Security acceptance fixtures/attack identities hazırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-112-T02 | ACC-15–18/24–26/32/37/40 ilgili security yollarını çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-112-T03 | Deny/contain/lease revoke/incident/audit assertions doğrula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-112-T04 | Forensic artifacts ve alert/runbook tepkisini review et | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-112-T05 | Critical finding correction/retest yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-112-T06 | Security acceptance statement imzala | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Security scenario results`
- `Red-team report`
- `Forensic evidence`
- `Security acceptance statement`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- ACC-15,16,17,18,24,25,26,32,37,40
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Critical attacks deny/contain ve audit üretir
- [ ] D3/D4 violation=0
- [ ] Unsigned artifact=0
- [ ] Açık critical/high security finding=0
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

Failure production access ve cutover'ı bloklar; compromised credentials/artifacts revoke edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
