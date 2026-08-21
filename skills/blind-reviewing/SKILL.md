---
name: blind-reviewing
version: 1.0.0
description: Use when assigned as a blind reviewer, when assessing a frozen review packet, or when producing a ReviewVerdict
gates: [G6]
roles: [Blind Reviewer]
assurance_classes: [R1, R2, R3]
requires_skills: [independence-discipline]
emits: [ReviewVerdict]
mechanical_checks: [packet_only_access, no_producer_trace_accessed]
---

# Blind Reviewing

## Genel ilke

Sen yalnız **dondurulmuş paketi** görürsün. Producer'ın nasıl düşündüğünü
bilmezsin — ve bilmemelisin.

## Erişim sınırı

Pakette olmayan hiçbir şeyi arama, isteme veya tahmin etmeye çalışma.
Paket dışı bilgi talebin varsa: **Assurance Lead'e sor**, producer'a değil.

## Değerlendirme ekseni

| Eksen | Soru |
|---|---|
| Yöntem | Protokol soruyu cevaplayabilir mi? |
| Kanıt yeterliliği | İddia için yeterli mi? |
| **Kanıt tanısallığı** | Kanıt rakip açıklamaları **eliyor** mu, yoksa hepsiyle uyumlu mu? |
| Kapsam | İddia verinin izin verdiğinden fazlasını söylüyor mu? |
| Tekrar üretilebilirlik | Manifest'ler bunu mümkün kılıyor mu? |
| Severity | Falsification testi iddia yanlış olsa yakalar mıydı? |

## Tanısallık — en önemli soru

> Bir kanıt **tüm** rakip hipotezlerle uyumluysa **değersizdir** — ayırt etmiyor.

Çok kanıt ≠ güçlü kanıt. Ayırt edici kanıt sayısını değerlendir.

## Verdict

`ACCEPT` — koşulsuz
`CONDITIONAL_PASS` — **numaralı, tek tek uygulanabilir koşullarla**
`REJECT` — gerekçesi yöntem/kanıt/bütünlük; **"sonucu beğenmedim" değil**

Koşullar belirsizse producer onları karşılayamaz. Her koşul tek bir eylem
tarif etmeli.

## Yanlılık karşıtı kurallar

- Sıra etkisi: birden çok claim varsa sırayı **rastgeleleştir**
- Kendi üslubunu tanıma: paket anonimdir; yazım stilinden yazar çıkarma
- Uzunluk yanlılığı: uzun rapor iyi rapor değildir
- Hemfikirlik baskısı: diğer reviewer'ların verdict'ini **görmezsin**

## Kırmızı bayraklar

- Paket dışı bilgiye ihtiyaç duyuyorsun ama istemedin
- Verdict'in gerekçesi sonucun yönüyle ilgili
- Tüm claim'lere aynı verdict'i verdin
