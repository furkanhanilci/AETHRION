# Evidence Index

Test, acceptance, hash, artifact, review ve operasyonel kanıtlar.

> **Kural:** Kanıt bulunmayan bir WP/ACC `IMPLEMENTED` kabul edilmez.
> Ve kanıt **taze** olmalıdır — hafızadan veya ajan raporundan alıntı kanıt
> değildir. Bkz. [[verification-before-completion]].

## Kanıt kayıtları

| Kayıt | Tarih | Kapsam |
|---|---|---|
| [[10 - Projects/AI Research Framework/05 - Evidence/2026-08-22_framework_audit_evidence\|Framework Audit Evidence]] | 2026-08-22 | Test, hash, plan bütünlüğü, servis durumu |

## Alt ayrım

- `tests/` — birim, contract ve integration çıktıları
- `acceptance/` — ACC-01–ACC-40 sonuçları
- `artifacts/` — manifest, digest ve provenance kayıtları
- `reviews/` — bağımsız review raporları
- `operations/` — servis, deployment ve readiness kanıtları

## Kanıt katmanları

| Katman | Soru |
|---|---|
| E0 Yapısal | Dosya/şema/referans var mı? |
| E1 Mekanik | Davranış deterministik testte doğru mu? |
| E2 Güvenlik | Yasak yol gerçekten engelleniyor mu? |
| E3 Bağımsız review | Üretici dışı aktör inceledi mi? |
| E4 Reproduction | Temiz ortamda tekrar çalışıyor mu? |
| E5 Operasyon | Failure, restore ve gözlemlenebilirlik doğru mu? |

## Eksik

`acceptance/` boş — ACC-01–ACC-40'tan hiçbiri otomatikleştirilmedi.
İlk aday: **ACC-22 (Obsidian Human Edit Preservation)** — mevcut test yarısını
zaten yapıyor.
