# Planın Kullanımı ve Yürütme Protokolü

## Amaç

Bu dosya, 130 iş paketinin tek program olarak nasıl yönetileceğini tanımlar. Paketler küçük tutulmuştur; fakat küçük paket bağımsız mimari karar anlamına gelmez. Her paket hedef mimarinin bir invariant'ını gerçekleştirir ve bağımlılık grafına bağlıdır.

## Temel yürütme kuralları

1. Her paketin bir `Accountable Owner`, bir `Responsible Implementer` ve üreticiden ayrı `Verifier`ı bulunur.
2. Paket yalnız listedeki önkoşulların kabul kanıtları erişilebilir olduğunda `READY` olur.
3. Uygulama başlamadan base revision, environment, policy bundle ve schema sürümü kaydedilir.
4. Kapsam genişlemesi aynı pakete sessizce eklenmez; change request veya yeni paket açılır.
5. Kod, policy, schema ve IaC değişikliği Git üzerinden; runtime sonucu immutable artifact üzerinden izlenir.
6. Dış sistem yazmaları Tool Broker contract'ı hazır değilken el ile otomasyona dönüştürülmez.
7. Geçici manuel işlem gerekiyorsa adı, owner'ı, bitiş tarihi ve silme kriteri olan `TemporaryControlRecord` gerekir.
8. Paket acceptance testi geçmeden bağımlı paket production-ready kabul edilmez.
9. Kritik bulgu kapatılmadan paket `ACCEPTED` olamaz; waiver yalnız non-waivable listesi dışında mümkündür.
10. Bir dalga bitişi özellik sayısıyla değil, tanımlı entegrasyon kanıtlarıyla ölçülür.

## Haftalık program ritmi

| Oturum | Girdi | Çıktı |
|---|---|---|
| Paket refinement | Backlog, bağımlılıklar, riskler | DoR sağlanmış paketler ve güncel tahmin |
| Mimari/contract kurulu | ADR, schema delta, interface etkisi | Onay, revise veya yeni karar ihtiyacı |
| Assurance triage | Test, review ve reproducer bulguları | Disposition ve correction packet |
| Entegrasyon checkpoint | Dikey dilim sonuçları | Bloke bağımlılık ve senaryo durumu |
| Program review | KPI, bütçe, risk, kapasite | Stop/pivot/continue ve owner kararları |

## Paket artefakt dizini

Her paket için çalışma sırasında aşağıdaki mantıksal dizin üretilir:

```text
delivery/WP-xxx/
  package-state.yaml
  design/
  implementation/
  tests/
  evidence/
    evidence-manifest.json
    verification-summary.json
  reviews/
  decisions/
  handoff/
```

Bu plan dosyaları uygulama repository'sinin yerini almaz. Uygulama repository yapısı WP-022 içinde kesinleştirilir.

## Non-waivable blocker'lar

- Karar sahibi veya aktör kimliği doğrulanamıyor.
- D3/D4 veri yanlış route'a gidebilir.
- Kritik producer/reviewer/reproducer bağımsızlığı sağlanamıyor.
- Kritik claim'in locator veya representation hash'i yok.
- Artifact overwrite edilebiliyor ya da provenance zinciri kırık.
- İmzalanmamış/mutable execution image kabul ediliyor.
- T4/T5 etkili işlem gerekli insan kararını atlayabiliyor.
- Temporal replay veya idempotency testi kritik state kaybı/çift etki gösteriyor.
- Clean-room sonuçları tanımlı tolerans dışında ve kök neden çözümlenmemiş.
- Restore tatbikatı RPO/RTO veya integrity sorgularını geçemiyor.
- Açık kritik security, assurance veya data bulgusu bulunuyor.

## Planın güncellenmesi

Plan yaşayan bir uygulama artifact'ıdır. Paket kimliği yeniden kullanılmaz. Kapsam değişirse dosya sürümü ve değişiklik kaydı güncellenir; kabul edilmiş paketin geçmiş şartları silinmez. Hedef mimari invariant'ını değiştiren güncelleme önce ADR ve Architecture Decision Owner onayı ister.

