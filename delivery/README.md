# Delivery — Evidence Packages

Her iş paketi ve kabul senaryosu için kanıt paketi burada tutulur.

```
delivery/
  WP-xxx/
    evidence-manifest.json     # zorunlu
    evidence-manifest.json.ots # OpenTimestamps kanıtı (WP-139)
    tests/                     # taze koşum çıktıları
    reviews/                   # bağımsız review kayıtları
    decisions/                 # ilgili DecisionRecord referansları
  ACC-xx/
    ...
```

## `evidence-manifest.json` minimum alanları

```json
{
  "package_id": "WP-xxx",
  "target_revision": "<git commit sha>",
  "produced_at": "<ISO 8601>",
  "producer": "<rol / model profili>",
  "verifier": "<üreticiden bağımsız aktör>",
  "environment": {"python": "...", "os": "...", "deps_lock_sha256": "..."},
  "artifacts": [{"path": "...", "sha256": "...", "size_bytes": 0}],
  "commands": [{"cmd": "...", "exit_code": 0, "output_sha256": "..."}],
  "open_findings": [],
  "decision": "<decision-id veya null>"
}
```

## Kurallar

1. **Manifest'siz teslimat kabul edilmez.** Bir paket `TECH_COMPLETE` olabilir;
   `ACCEPTED` olması bağımsız verifier kararına bağlıdır.
2. **Kanıt taze koşumdan gelir.** Hafızadan, önceki koşumdan veya ajan
   raporundan alıntı kanıt değildir — bkz. `skills/verification-before-completion/`.
3. **Zaman kanıtı dış çapaya bağlanır** (WP-139). `.ots` dosyası olmadan bir
   manifest'in "ne zaman var olduğu" yalnız bu depoya güvenerek doğrulanabilir.
4. **Bu dizin append-only ruhundadır.** Silme, bir `IntegrityCase` gerektirir.

> ⚠️ **Şu an boş.** Hiçbir iş paketi `ACCEPTED` değil ve bu doğru:
> imzalı `EvidenceManifest` ve immutable store mekanizmaları henüz kurulmadı.
> Ayrıntı: `docs/review/` bulgu **C1** ve önerilen **WP-000 Interim Evidence Policy**.
