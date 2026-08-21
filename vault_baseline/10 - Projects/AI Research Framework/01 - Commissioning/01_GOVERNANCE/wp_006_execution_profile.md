# WP-006 — ExecutionProfile ve Route Politikası

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-006` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Platform Security Lead |
| Bağımsız doğrulayıcı | Safety Owner / SRE |
| Hard dependencies | WP-002 |
| İlgili gate | G1,G5 |
| İlgili kontroller | CTL-DAT-02, CTL-SEC-04 |
| İlgili ACC senaryoları | ACC-15, ACC-18 |

## Amaç ve beklenen sonuç

DataClass, CodeTrust, ToolEffect ve Network/Credential kapsamı ayrı eksenlerle sandbox, route, approval ve isolation kontrolü üretir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-006-T01 | D0–D4 DataClass rubric'i tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-006-T02 | C0–C3 CodeTrust ve T0–T5 ToolEffect rubric'lerini yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-006-T03 | Network/credential scope seviyelerini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-006-T04 | Dominance ve minimum execution tier kurallarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-006-T05 | Model, broker, Kueue ve sandbox enforcement noktalarını eşle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `ExecutionProfile semantics`
- `Route/control decision tables`
- `Enforcement map`
- `Negative examples`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- D0+untrusted code hardened sandbox testi
- D4+signed code isolated route testi
- T4/T5 human-only negative test
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Data sınıfı sandbox ile eşitlenmez
- [ ] En yüksek gerekli kontrol diğer eksenlerle düşürülemez
- [ ] Her route açıklanabilir policy rule ID taşır
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

Policy değişikliği shadow mode'da doğrulanır; yanlış route durumunda profiller revoke edilip workload'lar pause edilir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
