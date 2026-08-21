# Program Risk Register ve Tedavi Kuralları

| ID | Risk | Erken sinyal | Önleyici kontrol | Owner | Cutover etkisi |
|---|---|---|---|---|---|
| PR-01 | Platform kapsamı kontrolsüz büyür | Paketler sürekli L üstüne çıkar | Contract-first, scope lock, retirement kriteri | Chief Architect | High |
| PR-02 | Policy kombinatorikleşir | Büyük çapraz tablolar, açıklanamayan karar | Ayrı profiller, precedence ve hard-promotion kuralları | Governance Lead | Critical |
| PR-03 | Canonical sahiplik bulanıklaşır | Zotero/Registry/Obsidian değerleri ayrışır | Field authority ve reconciliation | Knowledge Lead | Critical |
| PR-04 | Verification backlog büyür | G6/G7 bekleme ve bypass talebi | Risk bazlı derinlik, C0 mekanik kontroller, kapasite rezervi | Assurance Lead | Critical |
| PR-05 | Reviewer bağımsızlığı kağıt üzerinde kalır | Aynı trace/credential/model ailesi | Machine-checkable IndependenceProfile | Assurance Lead | Critical |
| PR-06 | Agent tool yetkisi fazla genişler | Direct credential veya connector kullanımı | Broker-only, purpose-bound identity | Safety Owner | Critical |
| PR-07 | Event/state ikili otorite oluşur | NATS tüketicisi gate state değiştirir | Temporal-only transition, outbox contract | Control Plane Lead | Critical |
| PR-08 | Artifact overwrite/lineage kaybı | Aynı URI'de farklı bytes | Content addressing, object lock | Data Platform Lead | Critical |
| PR-09 | Cost runaway | Fan-out/retry/token artışı | Hard budget, queue quota, minimum bundle | FinOps Lead | High |
| PR-10 | Vendor lock-in | Provider alanları role contract'a sızar | Adapter conformance ve canonical contract | Model Platform Lead | High |
| PR-11 | Human rubber-stamping | Çok hızlı/generic onay | Evidence delta UI, rationale rubric, sampling | Governance Lead | High |
| PR-12 | False rigor | Çok artifact, zayıf entailment | Outcome audit, anti-metrics, citation audit | Research Director | Critical |
| PR-13 | Restore yalnız kağıtta kalır | Backup var, tatbikat yok | İki restore drill + integrity query | SRE Lead | Critical |
| PR-14 | Kaynak lisansı ihlal edilir | PDF'ler kontrolsüz çoğalır | License policy, hash-only fallback, access log | Knowledge/Safety | Critical |
| PR-15 | Eval contamination | Golden set prompt/trace'te görünür | Ayrı credential/store, canary, invalidate/re-eval | Eval Office | Critical |

## Skorlama

Program riskleri 1–5 impact ve likelihood ile takip edilir; ancak critical güvenlik, identity, evidence, reproduction ve data blocker'ları sayısal toplamla aşağı indirilemez. Sayısal skor önceliklendirme içindir, waiver mekanizması değildir.

## Risk kapanışı

Risk yalnız “mitigation uygulandı” ile kapanmaz. Control effectiveness testi, evidence referansı, residual risk sahibi ve yeniden değerlendirme tarihi gerekir. Cutover gününde tüm critical riskler `CLOSED` veya policy tarafından açıkça `ACCEPTABLE` sınıfında olmalıdır; non-waivable riskler `ACCEPTABLE` olamaz.

