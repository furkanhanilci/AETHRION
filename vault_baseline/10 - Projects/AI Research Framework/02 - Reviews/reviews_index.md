# Reviews Index

Bağımsız inceleme talimatları ve sonuçları. Bir review, üreticiden bağımsız
olmadıkça kanıt sayılmaz.

## Review kayıtları

| Belge | Tür | Durum |
|---|---|---|
| [[10 - Projects/AI Research Framework/02 - Reviews/claude_framework_audit_report\|Claude Framework Audit Report]] | Kanıt bazlı bağımsız denetim | 2026-08-22 — tamamlandı |
| [[10 - Projects/AI Research Framework/02 - Reviews/claude_full_framework_review_prompt\|Claude Full Framework Review Prompt]] | Review talimatı | Kullanımda — düzeltme bekliyor |

> **Not:** Review promptunda üç hatalı dizin yolu tespit edildi
> (`09_OPERATIONS`, `11_DECOMMISSION`, `13_CHANGE_CONTROL` mevcut değil).
> Ayrıntı: denetim raporu Bölüm K.

## Review disiplini

- [[requesting-review]] — paket nasıl hazırlanır
- [[receiving-review]] — bulgulara nasıl yanıt verilir
- [[blind-reviewing]] — kör review
- [[adversarial-reviewing]] — karşı-tez ve ACH
- [[arbitrating-disagreement]] — uyuşmazlık ve breaker

## Kural

Bir review sonucu ancak şu üçü varsa kabul edilir: dondurulmuş paket hash'i,
üreticiden bağımsızlık kaydı, ve her koşula karşılık bir `ProducerResponse`.
