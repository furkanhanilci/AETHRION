# WP-024 — CI Temeli ve Deterministik Kalite Kapıları

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-024` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **M** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Engineering Productivity Lead |
| Bağımsız doğrulayıcı | Mechanical Verifier |
| Hard dependencies | WP-020, WP-022, WP-023 |
| İlgili gate | G5–G9,Engineering |
| İlgili kontroller | CTL-SUP-01, CTL-OPS-02 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Format, lint, type, unit, integration, schema, policy, security ve build testleri standart arayüz ve evidence çıktısı üretir.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/wp_020_schema_registry_sdk.md), [WP-022 — Repository Topolojisi ve Kod Sahipliği](../03_FOUNDATION/wp_022_repository_topology.md), [WP-023 — Git, Worktree ve Protected Path Politikası](../03_FOUNDATION/wp_023_git_worktree_branch_policy.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-024-T01 | CI job taxonomy ve target revision pinle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-024-T02 | Schema/policy/architecture lint ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-024-T03 | Test sonuçlarını machine-readable artifact yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-024-T04 | Fail-fast ile tam-suite ayrımını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-024-T05 | Flaky test quarantine ve owner SLA'sını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-024-T06 | Signed build provenance tetikle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `CI pipelines`
- `Verification summary schema adapter`
- `Test ownership registry`
- `Flake policy`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Known-fail fixture CI'ı durdurur
- Farklı commit artifact karıştırma negatif testi
- Retry/flaky sınıflandırma testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Başarısız required check bypass edilemez
- [ ] Evidence target commit ve environment taşır
- [ ] Test silme/zayıflatma owner review ister
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

Hatalı pipeline önceki imzalı version'a döner; required check kapatılmaz.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
