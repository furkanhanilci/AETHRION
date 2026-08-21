---
name: using-isolated-environments
version: 1.0.0
description: Use before starting any producing, reviewing or reproducing work that touches files, state or compute
gates: [G5, G6, G7]
roles: [Engineering Owner, Research Software Engineer, Reproducer]
assurance_classes: [R1, R2, R3]
emits: [EnvironmentManifest, BaselineVerificationRecord]
mechanical_checks: [clean_baseline_verified, environment_digest_pinned]
---

# Using Isolated Environments

## Genel ilke

İzole olmayan çalışma alanı, bağımsızlık iddiasını geçersiz kılar. Ve
"harness ile savaşma" — mevcut izolasyon mekanizmaları varsa onları kullan.

## Prosedür

**Adım 0 — Mevcut izolasyonu tespit et.** Zaten izole bir alandaysan yenisini
kurma. Emin değilsen sor; varsayma.

**Adım 1 — Alanı oluştur.** Yerel araç varsa onu kullan; yoksa manuel.
Oluşturmadan önce hedef dizinin **ignore edildiğini** doğrula.

**Adım 2 — Bağımlılıkları kur.** Sürümler pinlenir; digest kaydedilir.

**Adım 3 — TEMİZ BASELINE DOĞRULA.**

> Mevcut doğrulama paketini çalıştır. **Hepsi yeşil değilse devam etme.**
>
> Sebep: kirli bir baseline üzerinde yapılan iş, kimin neyi bozduğunu
> ayırt edilemez hale getirir.

## İzolasyon boyutları (Independence Matrix ile eşleşir)

| Boyut | Kontrol |
|---|---|
| Dizin | Ayrı çalışma alanı |
| Önbellek | Temizlenmiş — paylaşılan build artifact yok |
| Kimlik | Ayrı workload identity |
| Ağ | Varsayılan BLOCK |
| Veri yolu | Kaynak **yeniden çekilir**, producer'ın önbelleğinden alınmaz |
| Düğüm/namespace | Ayrı (R2, R3) |

## Reproduction için ek kural

G7'de reproducer, producer'ın ürettiği hiçbir ara çıktıyı kullanamaz —
yalnız dondurulmuş manifest ve **birincil kaynaklar**.

## Temizlik

İş bittiğinde alan kaldırılır. Ama **kanıt kaldırılmaz**: manifest, hash ve
loglar immutable store'da kalır.

## Kırmızı bayraklar

- Baseline doğrulanmadan işe başlanmış
- Reviewer ve producer aynı çalışma alanında
- Bağımlılık sürümleri pinlenmemiş
- "Zaten temizdi" varsayımı — komut çıktısı yok
