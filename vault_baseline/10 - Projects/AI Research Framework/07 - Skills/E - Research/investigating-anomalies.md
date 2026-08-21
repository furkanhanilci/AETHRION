---
name: investigating-anomalies
version: 1.0.0
description: Use when a result is unexpected, when a run fails, when metrics disagree between runs, or when data looks wrong
gates: [G5, G6, G7]
roles: [Engineering Owner, Statistical Methods Owner, Research Software Engineer]
assurance_classes: [R1, R2, R3]
non_waivable: true
emits: [AnomalyRecord, ProtocolChallenge]
mechanical_checks: [reproduced_before_explained, no_exclusion_without_root_cause]
---

# Investigating Anomalies

## Demir kural

> **KÖK NEDEN ANLAŞILMADAN HİÇBİR ANOMALİ "DÜZELTİLEMEZ" VEYA DIŞLANAMAZ.**

Kök neden anlaşılmadan uygulanan bir dışlama, veri temizliği değil
**sonuç şekillendirmedir**.

## Dört faz

**Faz 1 — Kök neden**
1. Hata/uyarı çıktısını **tam** oku
2. Anomaliyi **tutarlı biçimde yeniden üret** — üretemiyorsan henüz anomali değil, gözlem
3. Son değişiklikleri kontrol et: kod, veri, ortam, model snapshot, policy
4. Pipeline **sınırlarına** ölçüm ekle — nerede bozuluyor?
5. Veriyi **kaynağa kadar geriye izle**

**Faz 2 — Örüntü**
1. Aynı koşulun **çalışan** koşumlarını bul
2. Referansı **tam** oku, kısmi değil
3. **Her farkı** listele: seed, düğüm, sürüm, veri dilimi, sıra
4. Varsayımları ve bağımlılıkları çıkar

**Faz 3 — Hipotez**
1. Spesifik hipotez: *"X kök nedendir çünkü Y"*
2. **En küçük** değişiklikle test et
3. Sonucu doğrula
4. Başarısızsa **yeni hipotez** — üst üste düzeltme ekleme

**Faz 4 — Uygulama**
1. Önce başarısız bir doğrulama koşumu
2. **Tek** düzeltme, kök nedene yönelik
3. Regresyon kontrolü
4. Anomali koşumu ayrı `run_id` alır; ana sonuç kümesine karıştırılmaz

## Üç-düzeltme kuralı

> **Üç açıklama girişimi başarısız olduysa DUR.**
> Sorgulanacak olan uygulama değil, **`ProtocolManifest`**'tir.
> → `ProtocolChallenge` açılır, G2'ye dönüş değerlendirilir.

Ve ikinci sinyal: **her düzeltme farklı bir alanda yeni sorun doğuruyorsa**,
sorun ölçümde değil modeldedir.

## Etiketleme

Anomali araştırması **`exploratory`** yürür. Bu araştırmadan çıkan hiçbir
düzeltme `confirmatory` sonucu geriye dönük değiştiremez.

## Rasyonalizasyon tablosu

| Gerekçe | Hüküm |
|---|---|
| "Açıkça bir aykırı değer" | Aykırılık kök neden değildir. **Neden aykırı?** |
| "Muhtemelen donanım gürültüsü" | Muhtemelen kanıt değildir. Göster. |
| "Yeniden çalıştırınca düzeldi" | **Düzelmedi, gizlendi.** İki koşum arasındaki farkı bul. |
| "Zamanımız yok, dışlayalım" | Dışlama kuralı önceden tanımlıysa uygula; değilse dışlama yok. |

## Kırmızı bayraklar

- Anomali yeniden üretilmeden açıklanmış
- Dışlama kuralı anomaliden **sonra** eklenmiş
- Üçüncü düzeltme denemesi ve `ProtocolChallenge` yok
