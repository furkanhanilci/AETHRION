# WP-001 — Commissioning Charter ve Program Yetkisi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-001` |
| Workstream | `01_GOVERNANCE` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Executive Sponsor |
| Bağımsız doğrulayıcı | Internal Audit / Commissioning Board |
| Hard dependencies | Yok |
| İlgili gate | Program |
| İlgili kontroller | CTL-GOV-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Programın amacı, üretim sınırı, finansman yetkisi, karar organları ve tek-cutover kuralı imzalı bir charter ile yürürlüğe girer.

## Kapsam dışı

- Teknoloji seçimi
- Detaylı iş takvimi

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: Yok — programın başlangıç paketidir.
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-001-T01 | İş sonucunu, kapsamı ve kapsam dışını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-001-T02 | Executive Sponsor, Program Lead, Chief Architect, Assurance ve Safety yetkilerini ata | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-001-T03 | Production cutover ve abort yetkisini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-001-T04 | Başlangıç bütçe zarfı ile procurement sınırlarını kaydet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-001-T05 | Success KPI, anti-metric ve stop/pivot koşullarını onaylat | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `CommissioningCharter`
- `Program authority matrix`
- `Initial budget envelope`
- `Executive DecisionRecord`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Charter schema ve zorunlu alan kontrolü
- Yetki çakışması tabletop testi
- Cutover/abort karar senaryosu
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Bütün accountable roller isimlidir
- [ ] Tek-cutover ve sıfır kritik bulgu şartı açıktır
- [ ] Bütçe, kapsam ve stop/pivot yetkileri imzalıdır
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

Charter kabul edilmezse hiçbir platform procurement veya production bağlantısı açılmaz; taslak arşivlenir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
