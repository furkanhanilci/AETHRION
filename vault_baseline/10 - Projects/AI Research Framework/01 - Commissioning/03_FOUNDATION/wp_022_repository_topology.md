# WP-022 — Repository Topolojisi ve Kod Sahipliği

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-022` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Chief Architect |
| Bağımsız doğrulayıcı | Platform Lead / Security |
| Hard dependencies | WP-010, WP-020 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-SUP-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Control plane, services, schemas, policy, IaC, workflows, agents, tests ve docs için sınırlar ve owner'lar açık repository yapısına dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-010 — Mimari Karar ve Reddedilen Alternatifler Baseline'ı](../01_GOVERNANCE/wp_010_adr_baseline.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-022-T01 | Monorepo/polyrepo kararını ADR ile kapat | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-022-T02 | Service/bounded-context dizinlerini kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-022-T03 | CODEOWNERS ve protected path'leri tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-022-T04 | Shared library ve dependency direction kurallarını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-022-T05 | Generated code, migration ve test fixture alanlarını ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Repository skeleton`
- `CODEOWNERS`
- `Dependency rules`
- `Developer guide`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Architecture dependency lint
- Protected path approval testi
- Build graph smoke test
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Canonical schema/policy/IaC owner'ları ayrıdır
- [ ] Circular bounded-context dependency yoktur
- [ ] Yeni service için standart scaffold vardır
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

Yanlış topology migration branch'inde geri alınır; repository history rewrite yapılmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
