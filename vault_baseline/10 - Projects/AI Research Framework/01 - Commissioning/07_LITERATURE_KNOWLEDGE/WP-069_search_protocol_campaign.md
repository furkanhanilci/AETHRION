# WP-069 — SearchProtocol ve LiteratureCampaign Orkestrasyonu

## Paket kartı

| Alan | Değer |
|---|---|
| İş paketi | `WP-069` |
| Workstream | `07_LITERATURE_KNOWLEDGE` |
| İlk efor sınıfı | **L** — refinement'ta O/M/P tahmini zorunlu |
| Accountable Owner | Evidence Lead |
| Bağımsız doğrulayıcı | Methodologist / Citation Auditor |
| Hard dependencies | WP-013, WP-017, WP-032, WP-035, WP-046, WP-047, WP-049, WP-050, WP-061, WP-062 |
| İlgili gate | G2,G3 |
| İlgili kontroller | CTL-EPI-02, CTL-LIT-01 |
| İlgili ACC senaryoları | İlgili dikey dilim ve commissioning sırasında atanır |

## Amaç ve beklenen sonuç

Araştırma sorusu; veri tabanları, sorgular, tarih, dil, inclusion/exclusion, stop rule ve known-item testleriyle tekrar çalıştırılabilir literatür kampanyasına dönüşür.

## Kapsam dışı

- Bağımlı paketin kendi iç implementasyonu
- Production cutover ve nihai operasyon onayı

## Önkoşullar ve Definition of Ready

- Bağımlılıklar kabul edilmiştir: [WP-013 — Project, Task ve Role Contract Şemaları](../02_CONTRACTS/WP-013_project_task_role_contracts.md), [WP-017 — Source Registry ve Literature Contract Şemaları](../02_CONTRACTS/WP-017_source_literature_contracts.md), [WP-032 — ProjectLifecycle Workflow İskeleti](../04_CONTROL_EVENT/WP-032_project_lifecycle_skeleton.md), [WP-035 — G2 Protocol, G3 Literature ve G4 Baseline Workflow'ları](../04_CONTROL_EVENT/WP-035_g2_g4_workflows.md), [WP-046 — LangGraph Bounded Cognition Runtime](../05_MODEL_AGENT_TOOL/WP-046_langgraph_runtime.md), [WP-047 — Role Bundle Registry ve Agent Sözleşme Derleyicisi](../05_MODEL_AGENT_TOOL/WP-047_role_bundle_registry.md), [WP-049 — Tool Registry ve Tool Broker Çekirdeği](../05_MODEL_AGENT_TOOL/WP-049_tool_registry_broker.md), [WP-050 — İlk Tool Connector Paketi](../05_MODEL_AGENT_TOOL/WP-050_tool_connectors.md), [WP-061 — Canonical Source Registry Servisi](../07_LITERATURE_KNOWLEDGE/WP-061_source_registry_service.md), [WP-062 — Kaynak Kimlik Çözümleme, Dedup ve Merge](../07_LITERATURE_KNOWLEDGE/WP-062_source_identity_resolver.md)
- Named owner, implementer ve producer'dan bağımsız verifier atanmıştır.
- Etkilenen canonical kayıtlar, interface'ler ve ADR'lar refinement'ta ilişkilendirilmiştir.
- DataClass, CodeTrust, ToolEffect ve ağ/credential kapsamı sınıflandırılmıştır.
- Test fixture, environment, rollback noktası ve acceptance ölçüm yöntemi erişilebilirdir.
- Efor için O/M/P kişi-gün tahmini ve gerçek kapasite rezervasyonu kaydedilmiştir.

## Uygulama görevleri

| Alt iş | Yapılacak iş | Sorumlu | Tamamlanma kanıtı |
|---|---|---|---|
| WP-069-T01 | Question→concept/query authoring akışı yaz | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-069-T02 | Database/source connector katalog ve coverage tanımla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-069-T03 | SearchProtocol freeze/version ve amendment kur | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-069-T04 | Query execution log/response snapshot/ref kaydet | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-069-T05 | Known-item recall, saturation ve stop rule hesapla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |
| WP-069-T06 | Temporal LiteratureCampaign ve bounded scout task'larını bağla | Uygulama sahibi | Commit/konfigürasyon/kayıt referansı |

## Zorunlu teslimatlar

- `SearchProtocol service`
- `LiteratureCampaign workflow`
- `Query log`
- `Known-item/coverage tests`
- Güncellenmiş runbook/operasyon notu ve servis/contract ownership kaydı
- İmzalı `EvidenceManifest`

## Test ve doğrulama planı

- Frozen query rerun
- Known-item missing fail
- Provider partial failure resume
- Protocol amendment new version
- Yetkisiz, eksik, stale, duplicate ve partial-failure girdileri için en az bir negatif test
- İlgili interface'lerde producer/consumer contract compatibility testi
- Telemetry correlation ve audit kayıt bütünlüğü kontrolü

## Kabul kriterleri

- [ ] Her sonuç sorgu/provider/timestamp'a bağlıdır
- [ ] Arama sonucu sayısı coverage kanıtı değildir
- [ ] Kritik karşı-kanıt sorgusu zorunludur
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

Provider başarısızlığı query durumunu PARTIAL yapar; set freeze coverage kararı verilmeden geçmez.

Immutable artifact, review ve karar geçmişi rollback sırasında silinmez; yeni durum supersession veya invalidation kaydıyla gösterilir.

## Handoff ve sonraki paketlere giriş

Paket kabul edildiğinde teslim artifact'larının version/digest'leri Package Registry'ye yazılır, dependency event'i yayımlanır ve bu pakete bağlı READY adayları yeniden değerlendirilir. Downstream paket yalnız burada listelenen contract ve kanıt referanslarını tüketir; implementasyon iç ayrıntılarına bağlanmaz.
