# WP-058 — Untrusted Content Quarantine ve Prompt-Injection Firewall

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-058` |
| Workstream | `06_EXECUTION_SECURITY` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Content Security Lead |
| Bağımsız doğrulayıcı | Red Team / Knowledge Lead |
| Hard dependencies | WP-014, WP-017, WP-026, WP-049, WP-050, WP-051, WP-054, WP-056, WP-057 |
| İlgili gate | G3,G5 |
| İlgili kontroller | CTL-SEC-01, CTL-LIT-01 |
| İlgili ACC senaryoları | ACC-05 |

## Amaç ve beklenen sonuç

Web, PDF, repo ve tool çıktısı active content çalıştırılmadan karantina, malware/MIME/license/size, parsing, instruction tagging ve read-only extraction hattından geçer.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-014 — Artifact, Dataset ve Immutable Manifest Şemaları](../02_CONTRACTS/WP-014_artifact_manifest_contracts.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-026 — Content-Addressed Object Store ve WORM](../03_FOUNDATION/WP-026_object_store_worm.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-051 — Dört Trust Zone ve Ağ Segmentasyonu](../06_EXECUTION_SECURITY/WP-051_trust_zone_network.md), [WP-054 — gVisor Sandbox ve Execution Cell Lifecycle](../06_EXECUTION_SECURITY/WP-054_gvisor_sandbox.md), [WP-056 — OPA Policy Platform ve Bundle Dağıtımı](../06_EXECUTION_SECURITY/WP-056_opa_policy_platform.md), [WP-057 — Default-Deny Egress Proxy, DLP ve Allowlist](../06_EXECUTION_SECURITY/WP-057_egress_proxy_dlp.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-058-T01 | Quarantine bucket ve ingest gateway kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-058-T02 | MIME/malware/archive bomb/size/license scan uygula | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-058-T03 | PDF/HTML/OCR parser'ı izole cell'de çalıştır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-058-T04 | Text/metadata/link/script/instruction kanallarını ayır | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-058-T05 | Instruction-like segmentleri untrusted quoted data etiketle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-058-T06 | Extraction tool profilini T0/T1 read-only yap | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-058-T07 | Security event/quarantine disposition ekle | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `Content firewall`
- `Parser workers`
- `ContentSafetyRecord`
- `Injection detector`
- `Quarantine UI/API`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- PDF tool-command injection
- Malware/archive bomb
- Parser crash containment
- Extraction write/tool deny
- False-positive curator disposition
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Dış içerik workflow command olamaz
- [ ] Extraction secret/write/unrestricted network almaz
- [ ] Her span source representation hash ve parser version taşır
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

Şüpheli içerik karantinada kalır; parser/detector rollback edilip content yeni version ile tekrar işlenir.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
