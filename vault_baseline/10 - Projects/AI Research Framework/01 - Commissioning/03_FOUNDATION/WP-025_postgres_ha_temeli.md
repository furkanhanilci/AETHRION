# WP-025 — PostgreSQL HA ve Registry Veri Temeli

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-025` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Database Platform Lead |
| Bağımsız doğrulayıcı | SRE / Security |
| Hard dependencies | WP-021, WP-020 |
| İlgili gate | Platform |
| İlgili kontroller | CTL-OPS-03, CTL-SEC-03 |
| İlgili ACC senaryoları | ACC-27 |

## Amaç ve beklenen sonuç

Project, source, claim, policy, cost ve ledger servisleri için şifreli, yedekli, point-in-time restore edilebilir PostgreSQL temeli kurulur.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-021 — Development, Staging ve Production Ortam Baseline'ı](../03_FOUNDATION/WP-021_ortam_hesap_ag_baseline.md), [WP-020 — Schema Registry, Compatibility ve Contract SDK](../02_CONTRACTS/WP-020_schema_registry_sdk.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-025-T01 | HA topology ve failure domain seç | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-025-T02 | Encryption/TLS/RBAC ve workload identity bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-025-T03 | Migration framework ve schema ownership kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-025-T04 | PITR backup, retention ve restore environment hazırla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-025-T05 | Connection pooling, quotas ve slow-query telemetry ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-025-T06 | RPO/RTO ve integrity query'lerini tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `PostgreSQL clusters`
- `DB role matrix`
- `Migration pipeline`
- `Backup/restore configuration`
- `DB SLO dashboard`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Primary failover testi
- PITR restore ve integrity query
- Cross-service role permission negative testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Failover veri tutarlılığı korur
- [ ] Restore hedef RPO/RTO'yu karşılar
- [ ] Servisler shared superuser kullanmaz
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

Migration hatasında forward-fix veya doğrulanmış down migration; irreversible işlem dual-write/expand-contract ile yapılır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
