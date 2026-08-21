---
name: independence-discipline
version: 1.0.0
description: Use when dispatching any agent, assigning a reviewer or reproducer, or when an agent requests help from another agent
gates: [G5, G6, G7]
roles: [all]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [IndependenceRecord]
mechanical_checks: [no_producer_spawned_agents, reviewer_assigned_by_assurance_only]
---

# Independence Discipline

## Demir kural

> **PRODUCER KENDİ DOĞRULAYICISINI VEYA YARDIMCISINI ÇAĞIRAMAZ.**
>
> Ne yardımcı, ne reviewer, ne "ikinci görüş". Hiçbiri.

## Neden bu boyut tüm sınıflarda non-compensable

İhlal edilirse **diğer yedi bağımsızlık boyutunun ölçümü de geçersizdir.**
Producer'ın çağırdığı yardımcı fiilen ortak yazardır; ama bağımsızlık
defterinde görünmez. Matris yanlış `PASS` verir.

## Kim kimi atar

| İş | Atayan |
|---|---|
| Producer task'ı | Task Compiler |
| Reviewer | Assurance Lead |
| Reproducer | Assurance Lead |
| Arbiter | Assurance Lead (her iki tarafı da görür) |
| Yardımcı ajan | **Hiç kimse — yoktur** |

## Sekiz boyut

| Boyut | R1 | R2 | R3 | Non-compensable |
|---|---|---|---|---|
| **Delegation Boundary** | PASS | PASS | PASS | **R1, R2, R3** |
| Context Isolation | PASS | PASS | PASS | R2, R3 |
| Human Identity | PARTIAL | PASS | PASS | R3 |
| Incentive & Reporting | PASS | PASS | PASS | R3 |
| Model Lineage (**ölçülmüş**) | PARTIAL | PASS | PASS | — |
| Credentials | PARTIAL | PASS | PASS | — |
| Runtime Environment | PARTIAL | PASS | PASS | — |
| Data & Retrieval Path | PARTIAL | PASS | PASS | — |

**Model Lineage beyan değil ölçümdür.** Bkz. [[measuring-agreement]]: hata
korelasyonu eşiği aşan iki profil aynı bağımsızlık kotasına sayılmaz.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Sadece bir formatlama yardımcısı" | Yardımcı yardımcıdır. **Yasak.** |
| "Kendi işimi kontrol ettim, bu iyi bir pratik" | Öz-kontrol iyidir; **bağımsız review değildir.** Kayda `self_check` olarak geçer. |
| "Farklı model kullandım, yani bağımsız" | Farklı model, aynı çağıran. **Delegation ihlali.** |
| "Reviewer meşguldü" | Kuyruk bekler. Auto-approve yoktur. |
| "R1 projesi, gevşek olabilir" | Bu boyut **R1'de de** non-compensable. |

## Kırmızı bayraklar

- Korelasyon zincirinde producer'dan türeyen ikinci bir agent invocation
- Reviewer'ın producer ile aynı workload identity'yi kullanması
- Review paketinin producer tarafından üretilmiş olması
