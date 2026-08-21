# WP-005 — Araştırma Risk ve Assurance Profili

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-005` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Safety & Governance Owner |
| Bağımsız doğrulayıcı | Research Director / Assurance Lead |
| Hard dependencies | WP-001, WP-002 |
| İlgili gate | G0,G1 |
| İlgili kontroller | CTL-GOV-03 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Materiality, uncertainty, exposure ve safety/ethics/regulation boyutları küçük karar tablolarıyla R1/R2/R3 assurance sınıfı üretir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-001 — Commissioning Charter ve Program Yetkisi](../01_GOVERNANCE/wp_001_commissioning_charter.md), [WP-002 — Kapsam, NFR ve Gereksinim İzlenebilirliği](../01_GOVERNANCE/wp_002_scope_nfr_traceability.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-005-T01 | M/U/X/S boyutlarını 0–3 rubric ile tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-005-T02 | Max/precedence ve hard-promotion kurallarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-005-T03 | UNKNOWN değerinin fail-closed etkisini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-005-T04 | R1/R2/R3 review, literature ve reproduction derinliğini eşle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-005-T05 | Risk yükseltme/düşürme karar haklarını ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `RiskProfile schema semantics`
- `AssuranceClass decision tables`
- `Promotion rules`
- `Worked examples`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Boundary-value policy testleri
- Aynı vaka için tutarlılık/calibration testi
- UNKNOWN ve class downgrade negatif testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Karar tabloları çapraz-çarpım gerektirmez
- [ ] Aynı girdiler deterministik sınıf üretir
- [ ] R3 ve hard-promotion hiçbir düşük skorla telafi edilemez
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

Yeni tablo promote edilmeden önce shadow değerlendirilir; sorun halinde önceki imzalı policy sürümüne dönülür.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
