# WP-004 — İnsan Kararı, SLA, Delegasyon ve Eskalasyon Politikası

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-004` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Project Decision Owner |
| Bağımsız doğrulayıcı | Safety & Governance Owner |
| Hard dependencies | WP-003 |
| İlgili gate | G1,G8,G9 |
| İlgili kontroller | CTL-GOV-01, CTL-GOV-03 |
| İlgili ACC senaryoları | ACC-25, ACC-26 |

## Amaç ve beklenen sonuç

Human Decision Queue'daki her karar tipinin SLA'sı, kanıt özeti, delegasyon sınırı, expiry ve fail-closed davranışı tanımlanır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-003 — Rol Kataloğu ve RACI Baseline](../01_GOVERNANCE/WP-003_rol_katalogu_raci.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-004-T01 | Karar tiplerini material/non-material sınıflandır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-004-T02 | Her karar için SLA ve escalation zinciri ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-004-T03 | DelegationRecord kapsam/süre/rol kurallarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-004-T04 | Devredilemez G8, publication, retraction ve cutover kararlarını kilitle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-004-T05 | Approval expiry, revocation ve evidence-delta davranışını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Decision policy`
- `SLA/escalation table`
- `Delegation matrix`
- `Decision rationale rubric`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- SLA timeout otomatik onay olmama testi
- Sahte/expired delegation negatif testi
- Devredilemez karar denemesi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Timeout yalnız BLOCKED veya escalation üretir
- [ ] Material karar named owner ve gerekçe taşır
- [ ] Delegation kapsam dışı kullanım policy tarafından reddedilir
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

Hatalı delegation revoke edilir; etkilediği açık kararlar yeniden değerlendirme kuyruğuna alınır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
