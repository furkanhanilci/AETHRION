# Dalga ve Bağımlılık Haritası

## İlke

Dalga, üretim fazı değildir. Dalgalar geliştirme/staging üzerinde paralel kurulum sırasını gösterir. Üretim tek integrated cutover ile açılır.

## Dalgalar

| Dalga | Hedef | Paket aralığı | Çıkış kanıtı |
|---|---|---|---|
| W0 — Program kilidi | Kapsam, sahiplik, risk ve kabul sistemini sabitlemek | WP-001–010 | İmzalı operating model ve policy taslakları |
| W1 — Contract spine | Kimlik, schema ve canonical sahipliği sabitlemek | WP-011–020 | Contract compatibility ve schema registry pass |
| W2 — Platform omurgası | Ortam, GitOps, veri, event ve artifact temelini kurmak | WP-021–031, WP-051, WP-055–059 | Foundation health, identity ve policy smoke test |
| W3 — Kontrol ve runtime | Workflow, agent, model, broker ve sandbox'ı çalıştırmak | WP-032–060 | Replay, route, tool ve sandbox testleri |
| W4 — Bilgi ve kanıt | Literatür, Source Registry, Claim Ledger, experiment ve review hattı | WP-061–090 | Source→claim→run→review lineage pass |
| W5 — İnsan ve görünürlük | Cockpit, karar kuyruğu, graphs, telemetry ve FinOps | WP-091–101 | İnsan karar ve uçtan uca correlation pass |
| W6 — Dikey entegrasyon | G0–G10 ve engineering akışlarını bütünleştirmek | WP-102–115 | Dikey dilimler ve 40 acceptance testi |
| W7 — Commissioning | Security, resilience, DR, capacity, audit ve pilot | WP-116–119 | Commissioning dossier; sıfır kritik bulgu |
| W8 — Cutover | Rehearsal, production açılışı ve hypercare | WP-120–121 | Go-live DecisionRecord ve stabilizasyon |
| W9 — Day-2 | Sürekli güvence ve işletim | WP-122–130 | Periyodik control effectiveness kayıtları |

## Kritik yol

```text
WP-001
  → WP-005/WP-006/WP-007
  → WP-011/WP-012
  → WP-020
  → WP-021/WP-025/WP-026/WP-028/WP-031/WP-051/WP-056/WP-058
  → WP-032/WP-035/WP-047/WP-049/WP-062/WP-077
  → WP-102..WP-106
  → WP-115
  → WP-116..WP-119
  → WP-120
```

## Güvenli paralelleşme kümeleri

- W0'da WP-003, WP-005, WP-006 ve WP-007; WP-001 scope lock sonrası paralel ilerleyebilir.
- W1'de identifier standardı hazır olduğunda event, artifact, source, claim ve decision schema'ları ayrı ekiplerce paralel üretilebilir; WP-020 bunları birleştirir.
- W2'de Postgres, object store, NATS, MLflow ve derived indexes ayrı platform owner'larıyla paralel kurulabilir.
- W3'te control plane, model/agent ve execution/security hatları contract'lar üzerinden paralel ilerler.
- W4'te literature ve evidence ekipleri SourceRecord/SourceRepresentation interface'i sabitlenince paralel çalışabilir.
- W5, temel API contract'ları hazır olduğunda backend completion beklemeden mock contract'larla başlayabilir; commissioning gerçek servislerle yapılır.

## Paralelleştirilmemesi gereken işler

- Aynı canonical schema'nın iki bağımsız sürümünü üretmek.
- Policy semantics sabitlenmeden OPA rule ve UI explanation'ını farklı yorumlarla yazmak.
- Review independence contract'ı kapanmadan reviewer routing yapmak.
- Source identity/dedup kuralı kapanmadan Zotero write-back'i production benzeri veri üzerinde açmak.
- Immutable artifact ve RunManifest hazır olmadan clean-room reproduction ilan etmek.
- Restore kanıtı olmadan cutover rehearsal yapmak.

## Bağımlılık değişikliği kuralı

Bir paket yeni hard dependency bulursa katalog güncellenir, etkilenen `READY` paketleri tekrar değerlendirilir ve program event'i üretilir. Tarih baskısı nedeniyle bağımlılık atlanamaz; yalnız açık geçici kontrol ve son kullanma tarihiyle staging deneyi yapılabilir.
