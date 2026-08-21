# WP-023 — Git, Worktree ve Protected Path Politikası

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-023` |
| Workstream | `03_FOUNDATION` |
| İlk efor sınıfı | **S** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Engineering Lead |
| Bağımsız doğrulayıcı | Security Reviewer |
| Hard dependencies | WP-022 |
| İlgili gate | G5,Engineering |
| İlgili kontroller | CTL-GOV-02, CTL-SUP-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

İnsan ve agent değişiklikleri ayrı branch/worktree'de, izinli dosya kapsamı ve target commit sabitlemesiyle yürür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-022 — Repository Topolojisi ve Kod Sahipliği](../03_FOUNDATION/WP-022_repository_topolojisi.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-023-T01 | Branch/commit naming ve signed-commit politikasını yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-023-T02 | Agent task worktree lifecycle'ını tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-023-T03 | Allowed/protected path manifesti uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-023-T04 | Freeze commit ve correction branch davranışını kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-023-T05 | Cleanup, abandoned task ve forensic retention kuralını ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Git policy`
- `Worktree controller contract`
- `Protected-path rules`
- `Freeze procedure`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- İki agent aynı ownership zone negatif testi
- Protected path write deny
- Frozen target değişirse review invalidate testi
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her task base/target commit taşır
- [ ] Agent yalnız task worktree ve allowed path'e yazar
- [ ] Correction yeni frozen commit üretir
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

Task iptalinde worktree karantinaya alınır; artifact/evidence saklanır, branch owner kararıyla arşivlenir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
