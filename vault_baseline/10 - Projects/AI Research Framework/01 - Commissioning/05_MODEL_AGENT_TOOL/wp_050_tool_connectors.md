# WP-050 — İlk Tool Connector Paketi

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-050` |
| Workstream | `05_MODEL_AGENT_TOOL` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Tool Platform Lead |
| Bağımsız doğrulayıcı | Security / Connector Owners |
| Hard dependencies | WP-049 |
| İlgili gate | G3,G5,G9 |
| İlgili kontroller | CTL-LIT-03, CTL-OPS-01, CTL-SEC-01 |
| İlgili ACC senaryoları | ACC-01, ACC-02, ACC-05, ACC-35 |

## Amaç ve beklenen sonuç

Web/Crossref/Zotero/Git/object store/MLflow ve kontrollü bildirim araçları broker contract'ına uygun, en az yetkili connector'lar olarak çalışır.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/wp_049_tool_registry_broker.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-050-T01 | Web read/search connector ve allowlist uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-050-T02 | Crossref/status lookup connector yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-050-T03 | Zotero read/candidate/update-proposal connector'larını ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-050-T04 | Git branch/worktree connector ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-050-T05 | Object store signed upload/ref connector kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-050-T06 | MLflow run/metric connector bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-050-T07 | Her connector için target resolver ve compensation yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Versioned connectors`
- `Connector permission profiles`
- `Connector contract tests`
- `Compensation/reconciliation playbooks`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Web injection quarantine
- Zotero personal write deny
- Git protected branch deny
- Object hash mismatch
- Connector timeout after external success
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her connector yalnız tanımlı T sınıfı ve target scope'ta çalışır
- [ ] Connector sonucu untrusted data olarak etiketlenir
- [ ] Dış write idempotent veya reconcile edilebilirdir
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

Connector feature flag ile disable edilir; uncertain writes reconciliation kuyruğuna, reads retry/backoff'a alınır.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
