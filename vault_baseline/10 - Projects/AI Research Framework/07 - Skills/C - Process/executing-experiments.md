---
name: executing-experiments
version: 1.0.0
description: Use when running experiment batches at G5, when jobs are being dispatched to compute, or when a run fails mid-batch
gates: [G4, G5]
roles: [Engineering Owner, Research Software Engineer]
assurance_classes: [R1, R2, R3]
requires_skills: [preregistration-discipline, using-isolated-environments, verification-before-completion]
emits: [ExperimentRun, ToolReceipt]
mechanical_checks: [manifest_hashes_pinned, budget_within_hard_limit, artifacts_scanned]
---

# Executing Experiments

## Genel ilke

Koşum, dondurulmuş manifest'in mekanik uygulanmasıdır. Koşum sırasında karar
verilmez.

## Ön koşullar — hepsi zorunlu

- [ ] `ProtocolManifest` kilitli
- [ ] `AnalysisPlanManifest` kilitli
- [ ] `LiteratureSetManifest` dondurulmuş
- [ ] Baseline koşumu tamamlanmış ve raporlanmış
- [ ] Bütçe onaylı; soft/hard limit tanımlı
- [ ] Model/tool qualification geçerli

Biri eksikse **G5 başlamaz.**

## Her koşumda pinlenen

```
code_commit · container_digest · model_snapshot · policy_revision
protocol_hash · analysis_plan_hash · literature_set_hash · seed
```

Bunlar `ExperimentRun`'a yazılır. **Pinlenmemiş koşum kanıt üretmez.**

## Prosedür

1. `TaskContract` doğrula → `ExecutionProfile` hesapla
2. Kueue rezervasyonu (bütçe)
3. İmzalı image + read-only girdiler
4. Sandbox aç; **ağ varsayılan olarak BLOCK**
5. Koş
6. Çıktıyı tara (malware, secret, DLP)
7. Manifest + hash üret
8. Immutable store'a yaz
9. Lease, workload identity ve secret'ları iptal et

## Negatif sonuç

> **Negatif sonuç bir artifact'tır, bir istisna değil.** Silinmez, tekrar
> koşulmaz, "başarısız koşum" olarak sınıflandırılmaz.

## Bütçe

Soft limitte uyarı, hard limitte **durdur**. Workflow state kaybolmadan pause
olur. Hard limit aşımı için waiver yoktur.

## Batch içi hata

Bir koşum düşerse: **tüm batch yeniden koşulmaz.** Düşen koşum ayrı incelenir
([[investigating-anomalies]]). Yeniden koşulan koşum yeni bir `run_id` alır;
eskisinin üzerine yazılmaz.

## Kırmızı bayraklar

- Aynı `run_id` iki kez yazılmış
- `model_snapshot` alanı boş
- Başarısız koşumlar rapordan çıkarılmış
- Koşum sırasında protokol parametresi değişmiş
