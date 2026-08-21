# Hedef Durum, Sistem Sınırı ve Değişmezler

## Hedef işletim sonucu

AIRL-OS devreye alındığında bir araştırma talebi G0'dan G10'a kadar; kimliği, bütçesi, kaynak seti, protokolü, çalıştırmaları, claim'leri, bağımsız review'u, reproduction'ı, insan kararı, yayın paketi ve sonraki etki izlemesiyle tek korelasyon zincirinde ilerler.

## Sorumluluk düzlemleri

| Düzlem | Sahip olduğu konu | Canonical state örneği |
|---|---|---|
| Experience | İnsan niyeti, görünür karar ve çalışma yüzeyi | Onay komutu, insan annotation'ı |
| Control | Yaşam döngüsü, gate, retry, timeout, compensation | Temporal event history |
| Event | Commit sonrası entegrasyon ve replay | NATS stream/consumer offset |
| Cognition | Sınırlandırılmış agent task graph'ı | LangGraph checkpoint ve AgentResult |
| Execution | İzole compute, queue, tool ve workload lease | ExecutionLease, SandboxAttestation |
| Evidence & Operations | Source, artifact, claim, run, telemetry, cost ve audit | Registries, immutable manifests |

Policy/model yönlendirme ve identity/security bütün düzlemleri yatay keser.

## Canonical sahiplik

| Bilgi | Canonical sahip | Görünüm/türev |
|---|---|---|
| Workflow ve gate state | Temporal | Cockpit, NATS, dashboard |
| Proje/task metadata | PostgreSQL Project Registry | Neo4j, dashboard |
| Bibliyografik kimlik ve durum | Source Registry/PostgreSQL | Zotero, Obsidian |
| İnsan bibliyografik notları | Zotero insan alanları | Source Registry ingest görünümü |
| Claim/evidence | Claim Ledger/PostgreSQL | Neo4j, rapor, Obsidian linki |
| Kod/policy/schema | Git | OCI image, deployed bundle |
| Dataset/büyük artifact | Object store + immutable manifest | MLflow ve cache |
| Experiment/eval | MLflow + Run Registry | Grafana/rapor |
| İnsan sentezi | Obsidian Markdown + Git history | Derived concept graph |
| Model admission | Capability Registry | Router cache |
| Maliyet | Cost Ledger | Dashboard/forecast |

## Yaşam döngüsü

| Gate | Dondurulan ana çıktı | Geçişi engelleyen örnek |
|---|---|---|
| G0 Intake | IntakeRecord | Amaç, owner veya başlangıç sınıfı yok |
| G1 Charter | ProjectCharter ve ControlPlan | Test edilebilir sonuç/karar hakkı yok |
| G2 Protocol | ProtocolManifest | Material assumption/stop rule açık |
| G3 Literature | LiteratureSetManifest | Kimlik, inclusion veya locator eksik |
| G4 Baseline | BaselineBundle/FalsificationPlan | Leakage veya karşı test yok |
| G5 Execute | RunManifest ve artifacts | Policy, budget, identity veya lineage fail |
| G6 Review | ReviewBundle/Disposition | Kritik bulgu/bağımsızlık sorunu açık |
| G7 Repro | ReproductionReport | Manifest eksik veya tolerans dışı |
| G8 Decision | DecisionRecord | Owner/delegation/rationale geçersiz |
| G9 Publish | PublicationPackage | Claim lineage/citation audit eksik |
| G10 Monitor | MonitoringPolicy/ImpactCase | Supersession sessiz veya etki işlenmemiş |

Risk yalnız gate derinliğini değiştirir; gate kimliği ve GateRecord zorunluluğu değişmez.

## Güven sınırları

- Zone 0: İnsan ve governance; MFA, named decision ve audit export.
- Zone 1: Control plane; Temporal, Gate, registries ve policy decision.
- Zone 2: Execution fabric; sandbox, broker, workload identity ve egress proxy.
- Zone 3: Untrusted content; dış doküman, web, repository ve tool çıktısı karantinası.

Zone geçişleri explicit identity, policy, schema ve audit olmadan yapılamaz.

## Başarı invariant'ları

1. Material her claim tek sorguyla source representation, evidence span, run, review ve decision'a bağlanır.
2. Aynı external side effect retry/replay sonrası bir kez gerçekleşir.
3. Reviewer producer trace'ini görmeden frozen paketle çalışabilir.
4. G7 clean-room run, frozen manifest ile tanımlı toleransı üretir veya claim'i CHALLENGED yapar.
5. Kişisel Zotero kaydına agent yazamaz; insan alanı sessizce üzerine yazılamaz.
6. Derived graph/index sıfırdan canonical kayıtlardan yeniden kurulabilir.
7. Model snapshot değişimi requalification ve açık task impact değerlendirmesi üretir.
8. D3/D4 route ve T4/T5 action fail-closed davranır.
9. Bütçe hard limitinde yeni pahalı iş açılmaz; workflow state kaybolmadan pause olur.
10. Production cutover ancak tüm commissioning kanıtları imzalı olduğunda yapılır.
