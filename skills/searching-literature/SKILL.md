---
name: searching-literature
version: 1.0.0
description: Use when a literature campaign starts, when coverage of a topic must be established, or when seed sources need expansion
gates: [G3]
roles: [Evidence Lead, Search Strategist]
assurance_classes: [R1, R2, R3]
emits: [SearchProtocol, SourceCandidate]
mechanical_checks: [queries_recorded_verbatim, databases_and_dates_pinned]
---

# Searching Literature

## Genel ilke

Arama **protokoldür**, keşif değil. Tekrar çalıştırıldığında aynı sonucu
vermelidir.

## Ön kayıt

Arama başlamadan önce yazılır ve kilitlenir:

```yaml
queries: [...]              # kelimesi kelimesine, operatörlerle
databases: [...]            # ve her birinin sürümü/erişim tarihi
date_range: "..."
inclusion_criteria: [...]
exclusion_criteria: [...]
language_policy: "..."
```

## Kaynak çeşitliliği — tek kaynak yeterli değil

| Kaynak | Ne için |
|---|---|
| **OpenAlex** | Geniş kapsam, atıf ağı, ücretsiz |
| **Crossref** | DOI otoritesi, metadata |
| **Semantic Scholar / S2ORC** | Tam metin, alıntı bağlamı |
| arXiv / bioRxiv | Ön baskı |
| **Unpaywall** | Yasal açık erişim tam metin |
| Alan-özel (PubMed, DBLP, IEEE) | Kapsam tamamlama |

**Çok modlu tarama:** anahtar kelime, atıf ağı (ileri + geri), yazar, ve
alan-özel taksonomi. Tek yöntem her şeyi bulmaz.

## Seed genişletme

1. `01_Human_Seed`'den başla — insanın seçtiği çekirdek
2. **Geriye atıf** (referanslar) ve **ileriye atıf** (kim atıf verdi)
3. Anahtar kelime çıkarımı → yeni sorgular
4. Doygunluk: **son N kaynak yeni kavram getirmiyorsa** dur

## Kapsam analizi

Konu bazında kapsam raporlanır. Kapsanmamış alt konu **açıkça listelenir** —
"tam kapsam" iddiası kanıt ister.

## Çelişen kaynak

> Bulguları **çürüten** kaynaklar aktif olarak aranır ve
> `Project/Contradictory`'ye yazılır. Bulunamadıysa bu da raporlanır.

## Kırmızı bayraklar

- Sorgular kelimesi kelimesine kaydedilmemiş
- Tek veritabanı kullanılmış
- Çelişen kaynak bölümü boş ve arandığına dair kanıt yok
- Erişim tarihi yok (sonuçlar tekrar üretilemez)
